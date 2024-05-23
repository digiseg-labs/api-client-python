from typing import List
import digiseg_api
import os
import sys
import re

DELIM_CSV = ";"
DELIM_AUDIENCE_CODES = ","
BATCH_SIZE = 100

def batched(lines: List[str], n):
    batch = []
    for line in lines:
        line = line.strip()
        batch.append(line)
        if len(batch) == n:
            yield batch
            batch = []
    if len(batch) > 0:
        yield batch


def enrichLines(lines: List[str], apiKey: str):
    ips = dict()  # line index to IP address
    pattern = re.compile(r"\b(\d+\.\d+\.\d+\.\d+)\b")
    idx = 0
    for line in lines:
        m = re.search(pattern, line)
        if m:
            ips[idx] = m.group(1)
        idx = idx + 1
    if len(ips) == 0:
        return lines
    queries = map(lambda kv: {"id": f"{kv[0]}", "ip_address": kv[1]}, ips.items())
    configuration = digiseg_api.Configuration()
    configuration.api_key['apiKeyHeaderAuth'] = apiKey
    with digiseg_api.ApiClient(configuration) as api_client:
        audiencesApi = digiseg_api.AudiencesApi(api_client)
        response = audiencesApi.resolve_audiences_of_multiple({
            "queries": list(queries)
        })
        for result in response.results:
            lineNo = int(result.id)
            line = lines[lineNo]
            codes = []
            if result.audiences:
                for audience in result.audiences:
                    codes.append(audience.code)
            allCodes = DELIM_AUDIENCE_CODES.join(codes)
            newCsvLine = f"{line}{DELIM_CSV}{result.status}{DELIM_CSV}{allCodes}"
            lines[lineNo] = newCsvLine
    return lines


def main():
    filename = " ".join(sys.argv[1:])
    if len(filename) < 2:
        print("Usage: python examples/enrich_csv_file.py <filename>", file=sys.stderr)
        print("Example: python examples/enrich_csv_file.py input.csv > output.csv", file=sys.stderr)
        exit(1)
    if not os.path.isfile(filename):
        print(f"File '{filename}' does not exist", file=sys.stderr)
        exit(1)
    apiKey = os.getenv("DIGISEG_API_KEY")
    if not apiKey:
        print("Please provide a Digiseg API key in environment variable DIGISEG_API_KEY", file=sys.stderr)
        exit(1)

    with open(filename, "r") as file:
        lines = file.readlines()
        for batch in batched(lines, BATCH_SIZE):
            lines = enrichLines(batch, apiKey)
            for line in lines:
                print(line)


if __name__ == "__main__":
    main()
