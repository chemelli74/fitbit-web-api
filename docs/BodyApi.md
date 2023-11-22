# swagger_client.BodyApi

All URIs are relative to *https://api.fitbit.com/*

| Method                                                                    | HTTP request                                                       | Description          |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------ | -------------------- |
| [**add_body_fat_log**](BodyApi.md#add_body_fat_log)                       | **POST** /1/user/-/body/log/fat.json                               | Log Body Fat         |
| [**add_weight_log**](BodyApi.md#add_weight_log)                           | **POST** /1/user/-/body/log/weight.json                            | Log Weight           |
| [**delete_body_fat_log**](BodyApi.md#delete_body_fat_log)                 | **DELETE** /1/user/-/body/log/fat/{body-fat-log-id}.json           | Delete Body Fat Log  |
| [**delete_weight_log**](BodyApi.md#delete_weight_log)                     | **DELETE** /1/user/-/body/log/weight/{body-weight-log-id}.json     | Delete Weight Log    |
| [**get_body_fat_by_date**](BodyApi.md#get_body_fat_by_date)               | **GET** /1/user/-/body/log/fat/date/{date}.json                    | Get Body Fat Logs    |
| [**get_body_fat_by_date_period**](BodyApi.md#get_body_fat_by_date_period) | **GET** /1/user/-/body/log/fat/date/{date}/{period}.json           | Get Body Fat Logs    |
| [**get_body_fat_by_date_range**](BodyApi.md#get_body_fat_by_date_range)   | **GET** /1/user/-/body/log/fat/date/{base-date}/{end-date}.json    | Get Body Fat Logs    |
| [**get_body_goals**](BodyApi.md#get_body_goals)                           | **GET** /1/user/-/body/log/{goal-type}/goal.json                   | Get Body Goals       |
| [**get_weight_by_date**](BodyApi.md#get_weight_by_date)                   | **GET** /1/user/-/body/log/weight/date/{date}.json                 | Get Weight Logs      |
| [**get_weight_by_date_period**](BodyApi.md#get_weight_by_date_period)     | **GET** /1/user/-/body/log/weight/date/{date}/{period}.json        | Get Body Fat Logs    |
| [**get_weight_by_date_range**](BodyApi.md#get_weight_by_date_range)       | **GET** /1/user/-/body/log/weight/date/{base-date}/{end-date}.json | Get Body Fat Logs    |
| [**update_body_fat_goal**](BodyApi.md#update_body_fat_goal)               | **POST** /1/user/-/body/log/fat/goal.json                          | Update Body Fat Goal |
| [**update_weight_goal**](BodyApi.md#update_weight_goal)                   | **POST** /1/user/-/body/log/weight/goal.json                       | Update Weight Goal   |

# **add_body_fat_log**

> add_body_fat_log(fat, \_date, time)

Log Body Fat

Creates a log entry for body fat and returns a response in the format requested.

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
api_instance = swagger_client.BodyApi(swagger_client.ApiClient(configuration))
fat = 56 # int | Body fat in the format of X.XX in the unit system that corresponds to the Accept-Language header provided.
_date = '2013-10-20' # date | Log entry date in the format yyyy-MM-dd.
time = 'time_example' # str | Time of the measurement in hours and minutes in the format HH:mm:ss that is set to the last second of the day if not provided.

try:
    # Log Body Fat
    api_instance.add_body_fat_log(fat, _date, time)
except ApiException as e:
    print("Exception when calling BodyApi->add_body_fat_log: %s\n" % e)
```

### Parameters

| Name       | Type     | Description                                                                                                                    | Notes |
| ---------- | -------- | ------------------------------------------------------------------------------------------------------------------------------ | ----- |
| **fat**    | **int**  | Body fat in the format of X.XX in the unit system that corresponds to the Accept-Language header provided.                     |
| **\_date** | **date** | Log entry date in the format yyyy-MM-dd.                                                                                       |
| **time**   | **str**  | Time of the measurement in hours and minutes in the format HH:mm:ss that is set to the last second of the day if not provided. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_weight_log**

> add_weight_log(weight, \_date, time=time)

Log Weight

Creates log entry for a body weight using units in the unit systems that corresponds to the Accept-Language header provided and gets a response in the format requested.

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
api_instance = swagger_client.BodyApi(swagger_client.ApiClient(configuration))
weight = 56 # int | Weight in the format of X.XX.
_date = '2013-10-20' # date | Log entry date in the format yyyy-MM-dd.
time = 'time_example' # str | Time of the measurement; hours and minutes in the format of HH:mm:ss, which is set to the last second of the day if not provided. (optional)

try:
    # Log Weight
    api_instance.add_weight_log(weight, _date, time=time)
except ApiException as e:
    print("Exception when calling BodyApi->add_weight_log: %s\n" % e)
```

### Parameters

| Name       | Type     | Description                                                                                                                       | Notes      |
| ---------- | -------- | --------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **weight** | **int**  | Weight in the format of X.XX.                                                                                                     |
| **\_date** | **date** | Log entry date in the format yyyy-MM-dd.                                                                                          |
| **time**   | **str**  | Time of the measurement; hours and minutes in the format of HH:mm:ss, which is set to the last second of the day if not provided. | [optional] |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_body_fat_log**

> delete_body_fat_log(body_fat_log_id)

Delete Body Fat Log

Deletes a user's body fat log entry with the given ID.

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
api_instance = swagger_client.BodyApi(swagger_client.ApiClient(configuration))
body_fat_log_id = 56 # int | The ID of the body fat log entry.

try:
    # Delete Body Fat Log
    api_instance.delete_body_fat_log(body_fat_log_id)
except ApiException as e:
    print("Exception when calling BodyApi->delete_body_fat_log: %s\n" % e)
```

### Parameters

| Name                | Type    | Description                       | Notes |
| ------------------- | ------- | --------------------------------- | ----- |
| **body_fat_log_id** | **int** | The ID of the body fat log entry. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_weight_log**

> delete_weight_log(body_weight_log_id)

Delete Weight Log

Deletes a user's body weight log entrywith the given ID.

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
api_instance = swagger_client.BodyApi(swagger_client.ApiClient(configuration))
body_weight_log_id = 56 # int | The ID of the body weight log entry.

try:
    # Delete Weight Log
    api_instance.delete_weight_log(body_weight_log_id)
except ApiException as e:
    print("Exception when calling BodyApi->delete_weight_log: %s\n" % e)
```

### Parameters

| Name                   | Type    | Description                          | Notes |
| ---------------------- | ------- | ------------------------------------ | ----- |
| **body_weight_log_id** | **int** | The ID of the body weight log entry. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_body_fat_by_date**

> get_body_fat_by_date(\_date)

Get Body Fat Logs

Retreives a list of all user's body fat log entries for a given day in the format requested.

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
api_instance = swagger_client.BodyApi(swagger_client.ApiClient(configuration))
_date = '2013-10-20' # date | The date in the format yyyy-MM-dd.

try:
    # Get Body Fat Logs
    api_instance.get_body_fat_by_date(_date)
except ApiException as e:
    print("Exception when calling BodyApi->get_body_fat_by_date: %s\n" % e)
```

### Parameters

| Name       | Type     | Description                        | Notes |
| ---------- | -------- | ---------------------------------- | ----- |
| **\_date** | **date** | The date in the format yyyy-MM-dd. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_body_fat_by_date_period**

> get_body_fat_by_date_period(\_date, period)

Get Body Fat Logs

Retreives a list of all user's body fat log entries for a given day in the format requested.

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
api_instance = swagger_client.BodyApi(swagger_client.ApiClient(configuration))
_date = '2013-10-20' # date | The date in the format yyyy-MM-dd.
period = 'period_example' # str | The range for which data will be returned. Options are 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, or max.

try:
    # Get Body Fat Logs
    api_instance.get_body_fat_by_date_period(_date, period)
except ApiException as e:
    print("Exception when calling BodyApi->get_body_fat_by_date_period: %s\n" % e)
```

### Parameters

| Name       | Type     | Description                                                                                     | Notes |
| ---------- | -------- | ----------------------------------------------------------------------------------------------- | ----- |
| **\_date** | **date** | The date in the format yyyy-MM-dd.                                                              |
| **period** | **str**  | The range for which data will be returned. Options are 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, or max. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_body_fat_by_date_range**

> get_body_fat_by_date_range(base_date, end_date)

Get Body Fat Logs

Retreives a list of all user's body fat log entries for a given day in the format requested.

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
api_instance = swagger_client.BodyApi(swagger_client.ApiClient(configuration))
base_date = '2013-10-20' # date | The range start date in the format yyyy-MM-dd or today.
end_date = '2013-10-20' # date | The end date of the range.

try:
    # Get Body Fat Logs
    api_instance.get_body_fat_by_date_range(base_date, end_date)
except ApiException as e:
    print("Exception when calling BodyApi->get_body_fat_by_date_range: %s\n" % e)
```

### Parameters

| Name          | Type     | Description                                             | Notes |
| ------------- | -------- | ------------------------------------------------------- | ----- |
| **base_date** | **date** | The range start date in the format yyyy-MM-dd or today. |
| **end_date**  | **date** | The end date of the range.                              |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_body_goals**

> get_body_goals(goal_type)

Get Body Goals

Retreives a user's current body fat percentage or weight goal using units in the unit systems that corresponds to the Accept-Language header providedin the format requested.

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
api_instance = swagger_client.BodyApi(swagger_client.ApiClient(configuration))
goal_type = 'goal_type_example' # str | weight or fat.

try:
    # Get Body Goals
    api_instance.get_body_goals(goal_type)
except ApiException as e:
    print("Exception when calling BodyApi->get_body_goals: %s\n" % e)
```

### Parameters

| Name          | Type    | Description    | Notes |
| ------------- | ------- | -------------- | ----- |
| **goal_type** | **str** | weight or fat. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_weight_by_date**

> get_weight_by_date(\_date)

Get Weight Logs

Retreives a list of all user's body weight log entries for a given day using units in the unit systems which corresponds to the Accept-Language header provided.

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
api_instance = swagger_client.BodyApi(swagger_client.ApiClient(configuration))
_date = '2013-10-20' # date | The date in the format yyyy-MM-dd.

try:
    # Get Weight Logs
    api_instance.get_weight_by_date(_date)
except ApiException as e:
    print("Exception when calling BodyApi->get_weight_by_date: %s\n" % e)
```

### Parameters

| Name       | Type     | Description                        | Notes |
| ---------- | -------- | ---------------------------------- | ----- |
| **\_date** | **date** | The date in the format yyyy-MM-dd. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_weight_by_date_period**

> get_weight_by_date_period(\_date, period)

Get Body Fat Logs

Retreives a list of all user's body weight log entries for a given day in the format requested.

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
api_instance = swagger_client.BodyApi(swagger_client.ApiClient(configuration))
_date = '2013-10-20' # date | The date in the format yyyy-MM-dd.
period = 'period_example' # str | The range for which data will be returned. Options are 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, or max.

try:
    # Get Body Fat Logs
    api_instance.get_weight_by_date_period(_date, period)
except ApiException as e:
    print("Exception when calling BodyApi->get_weight_by_date_period: %s\n" % e)
```

### Parameters

| Name       | Type     | Description                                                                                     | Notes |
| ---------- | -------- | ----------------------------------------------------------------------------------------------- | ----- |
| **\_date** | **date** | The date in the format yyyy-MM-dd.                                                              |
| **period** | **str**  | The range for which data will be returned. Options are 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, or max. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_weight_by_date_range**

> get_weight_by_date_range(base_date, end_date)

Get Body Fat Logs

Retreives a list of all user's body fat log entries for a given day in the format requested.

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
api_instance = swagger_client.BodyApi(swagger_client.ApiClient(configuration))
base_date = '2013-10-20' # date | The range start date in the format yyyy-MM-dd or today.
end_date = '2013-10-20' # date | The end date of the range.

try:
    # Get Body Fat Logs
    api_instance.get_weight_by_date_range(base_date, end_date)
except ApiException as e:
    print("Exception when calling BodyApi->get_weight_by_date_range: %s\n" % e)
```

### Parameters

| Name          | Type     | Description                                             | Notes |
| ------------- | -------- | ------------------------------------------------------- | ----- |
| **base_date** | **date** | The range start date in the format yyyy-MM-dd or today. |
| **end_date**  | **date** | The end date of the range.                              |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_body_fat_goal**

> update_body_fat_goal(fat)

Update Body Fat Goal

Updates user's fat percentage goal.

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
api_instance = swagger_client.BodyApi(swagger_client.ApiClient(configuration))
fat = 'fat_example' # str | Target body fat percentage; in the format X.XX.

try:
    # Update Body Fat Goal
    api_instance.update_body_fat_goal(fat)
except ApiException as e:
    print("Exception when calling BodyApi->update_body_fat_goal: %s\n" % e)
```

### Parameters

| Name    | Type    | Description                                     | Notes |
| ------- | ------- | ----------------------------------------------- | ----- |
| **fat** | **str** | Target body fat percentage; in the format X.XX. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_weight_goal**

> update_weight_goal(start_date, start_weight, weight=weight)

Update Weight Goal

Updates user's fat percentage goal.

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
api_instance = swagger_client.BodyApi(swagger_client.ApiClient(configuration))
start_date = 'start_date_example' # str | Weight goal start date; in the format yyyy-MM-dd.
start_weight = 'start_weight_example' # str | Weight goal start weight; in the format X.XX, in the unit systems that corresponds to the Accept-Language header provided.
weight = 'weight_example' # str | Weight goal target weight; in the format X.XX, in the unit systems that corresponds to the Accept-Language header provided; required if user doesn't have an existing weight goal. (optional)

try:
    # Update Weight Goal
    api_instance.update_weight_goal(start_date, start_weight, weight=weight)
except ApiException as e:
    print("Exception when calling BodyApi->update_weight_goal: %s\n" % e)
```

### Parameters

| Name             | Type    | Description                                                                                                                                                                             | Notes      |
| ---------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **start_date**   | **str** | Weight goal start date; in the format yyyy-MM-dd.                                                                                                                                       |
| **start_weight** | **str** | Weight goal start weight; in the format X.XX, in the unit systems that corresponds to the Accept-Language header provided.                                                              |
| **weight**       | **str** | Weight goal target weight; in the format X.XX, in the unit systems that corresponds to the Accept-Language header provided; required if user doesn&#x27;t have an existing weight goal. | [optional] |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
