# Digiseg API client for Python

This module provides a SDK for interacting with the Digiseg API.

Documentation for the API can be found on https://developer.digiseg.net/

## Installing and using the SDK

Install the package:

```sh
pip install git+https://github.com/digiseg-labs/api-client-python.git
```

Import the package and start using it:

```python
import digiseg_api

# look up audiences
configuration = digiseg_api.Configuration()
configuration.api_key['apiKeyHeaderAuth'] = apiKey
with digiseg_api.ApiClient(configuration) as api_client:
    audiencesApi = digiseg_api.AudiencesApi(api_client)
    audiencesResponse = audiencesApi.resolve_audiences_of_single("152.115.123.174", include="core,category")
```

## Examples

More code examples for how to use this module can be found in the `examples` directory.

## Development notes

### Code generation

The code in this repo is generated based on the OpenAPI spec of the APIs.

To regenerate, run:

```sh
make codegen
make clean
```
