# swagger_client.AuthorizationApi

All URIs are relative to *https://api.fitbit.com/*

| Method                                             | HTTP request                    | Description                                          |
| -------------------------------------------------- | ------------------------------- | ---------------------------------------------------- |
| [**introspect**](AuthorizationApi.md#introspect)   | **POST** /1.1/oauth2/introspect | Retrieve the active state of an OAuth 2.0 token      |
| [**oauth_token**](AuthorizationApi.md#oauth_token) | **POST** /oauth2/token          | Get OAuth 2 access token                             |
| [**revoke**](AuthorizationApi.md#revoke)           | **POST** /oauth2/revoke         | Revokes consent of the access token or refresh token |

# **introspect**

> introspect(token)

Retrieve the active state of an OAuth 2.0 token

Retrieves the active state of an OAuth 2.0 token. It follows https://tools.ietf.org/html/rfc7662.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.AuthorizationApi(swagger_client.ApiClient(configuration))
token = 'token_example' # str |

try:
    # Retrieve the active state of an OAuth 2.0 token
    api_instance.introspect(token)
except ApiException as e:
    print("Exception when calling AuthorizationApi->introspect: %s\n" % e)
```

### Parameters

| Name      | Type    | Description | Notes |
| --------- | ------- | ----------- | ----- |
| **token** | **str** |             |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_token**

> oauth_token(client_id, grant_type, authorization=authorization, code=code, expires_in=expires_in, redirect_uri=redirect_uri, refresh_token=refresh_token, state=state)

Get OAuth 2 access token

Retrieves an OAuth 2 access token.

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthorizationApi()
client_id = 'client_id_example' # str | This is your Fitbit API application id from your settings on dev.fitbit.com.
grant_type = 'grant_type_example' # str | Authorization grant type. Valid values are 'authorization_code' and 'refresh_token'.
authorization = 'authorization_example' # str | The Authorization header must be set to 'Basic' followed by a space, then the Base64 encoded string of your application's client id and secret concatenated with a colon. For example, 'Basic Y2xpZW50X2lkOmNsaWVudCBzZWNyZXQ='. The Base64 encoded string, 'Y2xpZW50X2lkOmNsaWVudCBzZWNyZXQ=', is decoded as 'client_id:client secret'. (optional)
code = 'code_example' # str | Authorization code received in the redirect as URI parameter. Required if using the Authorization Code flow. (optional)
expires_in = 'expires_in_example' # str | Specify the desired access token lifetime. Defaults to 28800 for 8 hours. The other valid value is 3600 for 1 hour. (optional)
redirect_uri = 'redirect_uri_example' # str | Uri to which the access token will be sent if the request is successful. Required if specified in the redirect to the authorization page. Must be exact match. (optional)
refresh_token = 'refresh_token_example' # str | Refresh token issued by Fitbit. Required if 'grant_type' is 'refresh_token'. (optional)
state = 'state_example' # str | Required if specified in the redirect uri of the authorization page. Must be an exact match. (optional)

try:
    # Get OAuth 2 access token
    api_instance.oauth_token(client_id, grant_type, authorization=authorization, code=code, expires_in=expires_in, redirect_uri=redirect_uri, refresh_token=refresh_token, state=state)
except ApiException as e:
    print("Exception when calling AuthorizationApi->oauth_token: %s\n" % e)
```

### Parameters

| Name              | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                     | Notes      |
| ----------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **client_id**     | **str** | This is your Fitbit API application id from your settings on dev.fitbit.com.                                                                                                                                                                                                                                                                                                                    |
| **grant_type**    | **str** | Authorization grant type. Valid values are &#x27;authorization_code&#x27; and &#x27;refresh_token&#x27;.                                                                                                                                                                                                                                                                                        |
| **authorization** | **str** | The Authorization header must be set to &#x27;Basic&#x27; followed by a space, then the Base64 encoded string of your application&#x27;s client id and secret concatenated with a colon. For example, &#x27;Basic Y2xpZW50X2lkOmNsaWVudCBzZWNyZXQ&#x3D;&#x27;. The Base64 encoded string, &#x27;Y2xpZW50X2lkOmNsaWVudCBzZWNyZXQ&#x3D;&#x27;, is decoded as &#x27;client_id:client secret&#x27;. | [optional] |
| **code**          | **str** | Authorization code received in the redirect as URI parameter. Required if using the Authorization Code flow.                                                                                                                                                                                                                                                                                    | [optional] |
| **expires_in**    | **str** | Specify the desired access token lifetime. Defaults to 28800 for 8 hours. The other valid value is 3600 for 1 hour.                                                                                                                                                                                                                                                                             | [optional] |
| **redirect_uri**  | **str** | Uri to which the access token will be sent if the request is successful. Required if specified in the redirect to the authorization page. Must be exact match.                                                                                                                                                                                                                                  | [optional] |
| **refresh_token** | **str** | Refresh token issued by Fitbit. Required if &#x27;grant_type&#x27; is &#x27;refresh_token&#x27;.                                                                                                                                                                                                                                                                                                | [optional] |
| **state**         | **str** | Required if specified in the redirect uri of the authorization page. Must be an exact match.                                                                                                                                                                                                                                                                                                    | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke**

> revoke(token)

Revokes consent of the access token or refresh token

Revokes consent of the access token or refresh token

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.AuthorizationApi(swagger_client.ApiClient(configuration))
token = 'token_example' # str |

try:
    # Revokes consent of the access token or refresh token
    api_instance.revoke(token)
except ApiException as e:
    print("Exception when calling AuthorizationApi->revoke: %s\n" % e)
```

### Parameters

| Name      | Type    | Description | Notes |
| --------- | ------- | ----------- | ----- |
| **token** | **str** |             |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
