# fitbit_web_api.FriendsApi

All URIs are relative to *https://api.fitbit.com/*

| Method                                                               | HTTP request                                 | Description             |
| -------------------------------------------------------------------- | -------------------------------------------- | ----------------------- |
| [**get_friends**](FriendsApi.md#get_friends)                         | **GET** /1.1/user/-/friends.json             | Get Friends             |
| [**get_friends_leaderboard**](FriendsApi.md#get_friends_leaderboard) | **GET** /1.1/user/-/leaderboard/friends.json | Get Friends Leaderboard |

# **get_friends**

> get_friends()

Get Friends

Returns data of a user's friends in the format requested using units in the unit system which corresponds to the Accept-Language header provided.

### Example

```python
from __future__ import print_function
import time
import fitbit_web_api
from fitbit_web_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = fitbit_web_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = fitbit_web_api.FriendsApi(fitbit_web_api.ApiClient(configuration))

try:
    # Get Friends
    api_instance.get_friends()
except ApiException as e:
    print("Exception when calling FriendsApi->get_friends: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_friends_leaderboard**

> get_friends_leaderboard()

Get Friends Leaderboard

Returns data of a user's friends in the format requested using units in the unit system which corresponds to the Accept-Language header provided.

### Example

```python
from __future__ import print_function
import time
import fitbit_web_api
from fitbit_web_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = fitbit_web_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = fitbit_web_api.FriendsApi(fitbit_web_api.ApiClient(configuration))

try:
    # Get Friends Leaderboard
    api_instance.get_friends_leaderboard()
except ApiException as e:
    print("Exception when calling FriendsApi->get_friends_leaderboard: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
