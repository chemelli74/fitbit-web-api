# swagger_client.SleepApi

All URIs are relative to *https://api.fitbit.com/*

| Method                                                             | HTTP request                                               | Description                  |
| ------------------------------------------------------------------ | ---------------------------------------------------------- | ---------------------------- |
| [**add_sleep**](SleepApi.md#add_sleep)                             | **POST** /1.2/user/-/sleep.json                            | Log Sleep                    |
| [**delete_sleep**](SleepApi.md#delete_sleep)                       | **DELETE** /1.2/user/-/sleep/{log-id}.json                 | Delete Sleep Log             |
| [**get_sleep_by_date**](SleepApi.md#get_sleep_by_date)             | **GET** /1.2/user/-/sleep/date/{date}.json                 | Get Sleep Log                |
| [**get_sleep_by_date_range**](SleepApi.md#get_sleep_by_date_range) | **GET** /1.2/user/-/sleep/date/{base-date}/{end-date}.json | Get Sleep Logs by Date Range |
| [**get_sleep_goal**](SleepApi.md#get_sleep_goal)                   | **GET** /1.2/user/-/sleep/goal.json                        | Get Sleep Goal               |
| [**get_sleep_list**](SleepApi.md#get_sleep_list)                   | **GET** /1.2/user/-/sleep/list.json                        | Get Sleep Logs List          |
| [**update_sleep_goal**](SleepApi.md#update_sleep_goal)             | **POST** /1.2/user/-/sleep/goal.json                       | Update Sleep Goal            |

# **add_sleep**

> add_sleep(start_time, duration, \_date)

Log Sleep

Creates a log entry for a sleep event and returns a response in the format requested.

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
api_instance = swagger_client.SleepApi(swagger_client.ApiClient(configuration))
start_time = 'start_time_example' # str | Start time includes hours and minutes in the format HH:mm.
duration = 56 # int | Duration in milliseconds.
_date = '2013-10-20' # date | Log entry in the format yyyy-MM-dd.

try:
    # Log Sleep
    api_instance.add_sleep(start_time, duration, _date)
except ApiException as e:
    print("Exception when calling SleepApi->add_sleep: %s\n" % e)
```

### Parameters

| Name           | Type     | Description                                                | Notes |
| -------------- | -------- | ---------------------------------------------------------- | ----- |
| **start_time** | **str**  | Start time includes hours and minutes in the format HH:mm. |
| **duration**   | **int**  | Duration in milliseconds.                                  |
| **\_date**     | **date** | Log entry in the format yyyy-MM-dd.                        |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sleep**

> delete_sleep(log_id)

Delete Sleep Log

Deletes a user's sleep log entry with the given ID.

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
api_instance = swagger_client.SleepApi(swagger_client.ApiClient(configuration))
log_id = 'log_id_example' # str | The ID of the sleep log to be deleted.

try:
    # Delete Sleep Log
    api_instance.delete_sleep(log_id)
except ApiException as e:
    print("Exception when calling SleepApi->delete_sleep: %s\n" % e)
```

### Parameters

| Name       | Type    | Description                            | Notes |
| ---------- | ------- | -------------------------------------- | ----- |
| **log_id** | **str** | The ID of the sleep log to be deleted. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sleep_by_date**

> get_sleep_by_date(\_date)

Get Sleep Log

The Get Sleep Logs by Date endpoint returns a summary and list of a user's sleep log entries (including naps) as well as detailed sleep entry data for a given day.

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
api_instance = swagger_client.SleepApi(swagger_client.ApiClient(configuration))
_date = '2013-10-20' # date | The date of records to be returned. In the format yyyy-MM-dd.

try:
    # Get Sleep Log
    api_instance.get_sleep_by_date(_date)
except ApiException as e:
    print("Exception when calling SleepApi->get_sleep_by_date: %s\n" % e)
```

### Parameters

| Name       | Type     | Description                                                   | Notes |
| ---------- | -------- | ------------------------------------------------------------- | ----- |
| **\_date** | **date** | The date of records to be returned. In the format yyyy-MM-dd. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sleep_by_date_range**

> get_sleep_by_date_range(base_date, end_date)

Get Sleep Logs by Date Range

The Get Sleep Logs by Date Range endpoint returns a list of a user's sleep log entries (including naps) as well as detailed sleep entry data for a given date range (inclusive of start and end dates).

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
api_instance = swagger_client.SleepApi(swagger_client.ApiClient(configuration))
base_date = '2013-10-20' # date | The date of records to be returned. In the format yyyy-MM-dd.
end_date = '2013-10-20' # date | The date of records to be returned. In the format yyyy-MM-dd.

try:
    # Get Sleep Logs by Date Range
    api_instance.get_sleep_by_date_range(base_date, end_date)
except ApiException as e:
    print("Exception when calling SleepApi->get_sleep_by_date_range: %s\n" % e)
```

### Parameters

| Name          | Type     | Description                                                   | Notes |
| ------------- | -------- | ------------------------------------------------------------- | ----- |
| **base_date** | **date** | The date of records to be returned. In the format yyyy-MM-dd. |
| **end_date**  | **date** | The date of records to be returned. In the format yyyy-MM-dd. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sleep_goal**

> get_sleep_goal()

Get Sleep Goal

Returns the user's sleep goal.

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
api_instance = swagger_client.SleepApi(swagger_client.ApiClient(configuration))

try:
    # Get Sleep Goal
    api_instance.get_sleep_goal()
except ApiException as e:
    print("Exception when calling SleepApi->get_sleep_goal: %s\n" % e)
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

# **get_sleep_list**

> get_sleep_list(sort, offset, limit, before_date=before_date, after_date=after_date)

Get Sleep Logs List

The Get Sleep Logs List endpoint returns a list of a user's sleep logs (including naps) before or after a given day with offset, limit, and sort order.

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
api_instance = swagger_client.SleepApi(swagger_client.ApiClient(configuration))
sort = 'sort_example' # str | The sort order of entries by date asc (ascending) or desc (descending).
offset = 0 # int | The offset number of entries. (default to 0)
limit = 56 # int | The maximum number of entries returned (maximum;100).
before_date = '2013-10-20' # date | The date in the format yyyy-MM-ddTHH:mm:ss. Only yyyy-MM-dd is required. Either beforeDate or afterDate should be specified. (optional)
after_date = '2013-10-20' # date | The date in the format yyyy-MM-ddTHH:mm:ss. (optional)

try:
    # Get Sleep Logs List
    api_instance.get_sleep_list(sort, offset, limit, before_date=before_date, after_date=after_date)
except ApiException as e:
    print("Exception when calling SleepApi->get_sleep_list: %s\n" % e)
```

### Parameters

| Name            | Type     | Description                                                                                                                  | Notes          |
| --------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------- | -------------- |
| **sort**        | **str**  | The sort order of entries by date asc (ascending) or desc (descending).                                                      |
| **offset**      | **int**  | The offset number of entries.                                                                                                | [default to 0] |
| **limit**       | **int**  | The maximum number of entries returned (maximum;100).                                                                        |
| **before_date** | **date** | The date in the format yyyy-MM-ddTHH:mm:ss. Only yyyy-MM-dd is required. Either beforeDate or afterDate should be specified. | [optional]     |
| **after_date**  | **date** | The date in the format yyyy-MM-ddTHH:mm:ss.                                                                                  | [optional]     |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sleep_goal**

> update_sleep_goal(min_duration)

Update Sleep Goal

Create or update the user's sleep goal and get a response in the JSON format.

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
api_instance = swagger_client.SleepApi(swagger_client.ApiClient(configuration))
min_duration = 'min_duration_example' # str | Duration of sleep goal.

try:
    # Update Sleep Goal
    api_instance.update_sleep_goal(min_duration)
except ApiException as e:
    print("Exception when calling SleepApi->update_sleep_goal: %s\n" % e)
```

### Parameters

| Name             | Type    | Description             | Notes |
| ---------------- | ------- | ----------------------- | ----- |
| **min_duration** | **str** | Duration of sleep goal. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
