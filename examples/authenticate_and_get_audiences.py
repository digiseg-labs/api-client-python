import digiseg_api
import os


def authenticate():
    authRequest = digiseg_api.AuthTokenRequest.from_dict({
        "username": os.getenv("DIGISEG_USERNAME"),
        "password": os.getenv("DIGISEG_PASSWORD"),
    })

    authResponse = digiseg_api.AuthApi().create_access_token(authRequest)
    accessToken = authResponse.access_token
    return accessToken


def getAudiences(accessToken: str):
    configuration = digiseg_api.Configuration(access_token=accessToken)
    with digiseg_api.ApiClient(configuration) as api_client:
        audiencesApi = digiseg_api.AudiencesApi(api_client)
        audiencesResponse = audiencesApi.resolve_audiences_of_single("152.115.123.174")
        return audiencesResponse


def main():
    accessToken = authenticate()
    print(f"Access token: {accessToken}")
    audiencesResponse = getAudiences(accessToken)
    print(f"Status: {audiencesResponse.status}")
    for audience in audiencesResponse.audiences:
        print(f"Audience:\t{audience.code}\t{audience.name}")


if __name__ == "__main__":
    main()
