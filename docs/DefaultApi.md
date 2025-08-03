# fitbit_web_api.DefaultApi

All URIs are relative to *https://api.fitbit.com*

| Method                                                                           | HTTP request                    | Description |
| -------------------------------------------------------------------------------- | ------------------------------- | ----------- |
| [**call_1_user_profile_json_post**](DefaultApi.md#call_1_user_profile_json_post) | **POST** /1/user/-/profile.json |

# **call_1_user_profile_json_post**

> GetProfileResponse call_1_user_profile_json_post()

### Example

```python
import fitbit_web_api
from fitbit_web_api.models.get_profile_response import GetProfileResponse
from fitbit_web_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fitbit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fitbit_web_api.Configuration(
    host = "https://api.fitbit.com"
)


# Enter a context with an instance of the API client
async with fitbit_web_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fitbit_web_api.DefaultApi(api_client)

    try:
        api_response = await api_instance.call_1_user_profile_json_post()
        print("The response of DefaultApi->call_1_user_profile_json_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->call_1_user_profile_json_post: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetProfileResponse**](GetProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description           | Response headers |
| ----------- | --------------------- | ---------------- |
| **200**     | A successful request. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
