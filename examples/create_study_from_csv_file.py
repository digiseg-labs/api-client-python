from typing import List
import digiseg_api
import os
import sys
import re


def submitEventsFromLines(studyId: str, lines: List[str], apiKey: str):
    configuration = digiseg_api.Configuration()
    configuration.api_key['apiKeyHeaderAuth'] = apiKey
    api_client = digiseg_api.ApiClient(configuration)
    requestNumber = 0
    with digiseg_api.ApiClient(configuration) as api_client:
        studiesApi = digiseg_api.StudiesApi(api_client)
        pattern = re.compile(r"\b(\d+\.\d+\.\d+\.\d+)\b")
        for line in lines:
            m = re.search(pattern, line)
            if m:
                requestNumber = requestNumber+1
                ip = m.group(1)
                response = studiesApi.create_study_event_with_http_info(studyId, {
                    "ip_address": ip,
                    "event_type": "impression"
                })
                print(f"Submitted req. no. {requestNumber} - IP {ip} - HTTP response: {response.status_code}")
    print(f"Done. {requestNumber} requests from {len(lines)} lines")


def main():
    filename = " ".join(sys.argv[1:])
    if len(filename) < 2:
        print("Usage: python examples/create_study_from_csv.py <filename>", file=sys.stderr)
        exit(1)
    if not os.path.isfile(filename):
        print(f"File '{filename}' does not exist", file=sys.stderr)
        exit(1)
    studyId = os.getenv("DIGISEG_STUDY_ID")
    if not studyId:
        print("Please provide a Digiseg Study ID in environment variable DIGISEG_STUDY_ID", file=sys.stderr)
        exit(1)
    apiKey = os.getenv("DIGISEG_API_KEY")
    if not apiKey:
        print("Please provide a Digiseg API key in environment variable DIGISEG_API_KEY", file=sys.stderr)
        exit(1)

    with open(filename, "r") as file:
        lines = file.readlines()
        submitEventsFromLines(studyId, lines, apiKey)


if __name__ == "__main__":
    main()
