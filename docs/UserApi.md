# fitbit_web_api.UserApi

All URIs are relative to *https://api.fitbit.com*

| Method                                    | HTTP request                   | Description |
| ----------------------------------------- | ------------------------------ | ----------- |
| [**get_badges**](UserApi.md#get_badges)   | **GET** /1/user/-/badges.json  | Get Badges  |
| [**get_profile**](UserApi.md#get_profile) | **GET** /1/user/-/profile.json | Get Profile |

# **get_badges**

> GetBadgesResponse get_badges()

Get Badges

Retrieves the user's badges in the format requested. Response includes all badges for the user as seen on the Fitbit website badge locker (both activity and weight related.) The endpoint returns weight and distance badges based on the user's unit profile preference as on the website.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_badges_response import GetBadgesResponse
from fitbit_web_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fitbit.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fitbit_web_api.Configuration(
    host = "https://api.fitbit.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with fitbit_web_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fitbit_web_api.UserApi(api_client)

    try:
        # Get Badges
        api_response = await api_instance.get_badges()
        print("The response of UserApi->get_badges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_badges: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetBadgesResponse**](GetBadgesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                                                                                                                          | Response headers |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                                                                                                                                                | -                |
| **201**     | Returned if a new subscription was created in response to your request.                                                                                                                              | -                |
| **409**     | Returned if the given user is already subscribed to this stream using a different subscription ID, OR if the given subscription ID is already used to identify a subscription to a different stream. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile**

> GetProfileResponse get_profile()

Get Profile

Returns a user's profile. The authenticated owner receives all values. However, the authenticated user's access to other users' data is subject to those users' privacy settings. Numerical values are returned in the unit system specified in the Accept-Language header.

### Example

- OAuth Authentication (oauth2):

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with fitbit_web_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fitbit_web_api.UserApi(api_client)

    try:
        # Get Profile
        api_response = await api_instance.get_profile()
        print("The response of UserApi->get_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_profile: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetProfileResponse**](GetProfileResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                                                                                                                                                          | Response headers |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                                                                                                                                                                | -                |
| **201**     | Returned if a new subscription was created in response to your request.                                                                                                                              | -                |
| **401**     | The request requires user authentication.                                                                                                                                                            | -                |
| **409**     | Returned if the given user is already subscribed to this stream using a different subscription ID, OR if the given subscription ID is already used to identify a subscription to a different stream. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
