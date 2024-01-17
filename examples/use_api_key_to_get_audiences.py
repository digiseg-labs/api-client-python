import digiseg_api
import os


def getAudiences(apiKey: str):
    configuration = digiseg_api.Configuration()
    configuration.api_key['apiKeyHeaderAuth'] = apiKey
    with digiseg_api.ApiClient(configuration) as api_client:
        audiencesApi = digiseg_api.AudiencesApi(api_client)
        audiencesResponse = audiencesApi.resolve_audiences_of_single("152.115.123.174")
        return audiencesResponse


def main():
    apiKey = os.getenv("DIGISEG_API_KEY")
    if not apiKey:
        print("Please provide a Digiseg API key in environment variable DIGISEG_API_KEY")
        exit(1)
    audiencesResponse = getAudiences(apiKey)
    print(f"Status: {audiencesResponse.status}")
    for audience in audiencesResponse.audiences:
        print(f"Audience:\t{audience.code}\t{audience.name}")


if __name__ == "__main__":
    main()
