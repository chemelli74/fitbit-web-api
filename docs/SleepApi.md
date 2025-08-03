# fitbit_web_api.SleepApi

All URIs are relative to *https://api.fitbit.com*

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

> add_sleep(start_time, duration, var_date)

Log Sleep

Creates a log entry for a sleep event and returns a response in the format requested.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
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
    api_instance = fitbit_web_api.SleepApi(api_client)
    start_time = 'start_time_example' # str | Start time includes hours and minutes in the format HH:mm.
    duration = 56 # int | Duration in milliseconds.
    var_date = '2013-10-20' # date | Log entry in the format yyyy-MM-dd.

    try:
        # Log Sleep
        await api_instance.add_sleep(start_time, duration, var_date)
    except Exception as e:
        print("Exception when calling SleepApi->add_sleep: %s\n" % e)
```

### Parameters

| Name           | Type     | Description                                                | Notes |
| -------------- | -------- | ---------------------------------------------------------- | ----- |
| **start_time** | **str**  | Start time includes hours and minutes in the format HH:mm. |
| **duration**   | **int**  | Duration in milliseconds.                                  |
| **var_date**   | **date** | Log entry in the format yyyy-MM-dd.                        |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                       | Response headers |
| ----------- | ----------------------------------------------------------------- | ---------------- |
| **200**     | Successful request.                                               | -                |
| **401**     | The request requires user authentication.                         | -                |
| **403**     | The server understood the request, but is refusing to fulfill it. | -                |
| **201**     | A successful request.                                             | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sleep**

> delete_sleep(log_id)

Delete Sleep Log

Deletes a user's sleep log entry with the given ID.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
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
    api_instance = fitbit_web_api.SleepApi(api_client)
    log_id = 'log_id_example' # str | The ID of the sleep log to be deleted.

    try:
        # Delete Sleep Log
        await api_instance.delete_sleep(log_id)
    except Exception as e:
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

### HTTP response details

| Status code | Description                                             | Response headers |
| ----------- | ------------------------------------------------------- | ---------------- |
| **204**     | No Content. The request was successful.                 | -                |
| **400**     | Bad Request. The request likely contained bad syntax.   | -                |
| **401**     | Unauthorized. The request requires user authentication. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sleep_by_date**

> GetSleepLogByDateResponse get_sleep_by_date(var_date)

Get Sleep Log

The Get Sleep Logs by Date endpoint returns a summary and list of a user's sleep log entries (including naps) as well as detailed sleep entry data for a given day.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_sleep_log_by_date_response import GetSleepLogByDateResponse
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
    api_instance = fitbit_web_api.SleepApi(api_client)
    var_date = '2013-10-20' # date | The date of records to be returned. In the format yyyy-MM-dd.

    try:
        # Get Sleep Log
        api_response = await api_instance.get_sleep_by_date(var_date)
        print("The response of SleepApi->get_sleep_by_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SleepApi->get_sleep_by_date: %s\n" % e)
```

### Parameters

| Name         | Type     | Description                                                   | Notes |
| ------------ | -------- | ------------------------------------------------------------- | ----- |
| **var_date** | **date** | The date of records to be returned. In the format yyyy-MM-dd. |

### Return type

[**GetSleepLogByDateResponse**](GetSleepLogByDateResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                       | Response headers |
| ----------- | ----------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                             | -                |
| **401**     | The request requires user authentication.                         | -                |
| **403**     | The server understood the request, but is refusing to fulfill it. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sleep_by_date_range**

> GetSleepLogByDateRangeResponse get_sleep_by_date_range(base_date, end_date)

Get Sleep Logs by Date Range

The Get Sleep Logs by Date Range endpoint returns a list of a user's sleep log entries (including naps) as well as detailed sleep entry data for a given date range (inclusive of start and end dates).

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_sleep_log_by_date_range_response import GetSleepLogByDateRangeResponse
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
    api_instance = fitbit_web_api.SleepApi(api_client)
    base_date = '2013-10-20' # date | The date of records to be returned. In the format yyyy-MM-dd.
    end_date = '2013-10-20' # date | The date of records to be returned. In the format yyyy-MM-dd.

    try:
        # Get Sleep Logs by Date Range
        api_response = await api_instance.get_sleep_by_date_range(base_date, end_date)
        print("The response of SleepApi->get_sleep_by_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SleepApi->get_sleep_by_date_range: %s\n" % e)
```

### Parameters

| Name          | Type     | Description                                                   | Notes |
| ------------- | -------- | ------------------------------------------------------------- | ----- |
| **base_date** | **date** | The date of records to be returned. In the format yyyy-MM-dd. |
| **end_date**  | **date** | The date of records to be returned. In the format yyyy-MM-dd. |

### Return type

[**GetSleepLogByDateRangeResponse**](GetSleepLogByDateRangeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                       | Response headers |
| ----------- | ----------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                             | -                |
| **401**     | The request requires user authentication.                         | -                |
| **403**     | The server understood the request, but is refusing to fulfill it. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sleep_goal**

> GetSleepGoalResponse get_sleep_goal()

Get Sleep Goal

Returns the user's sleep goal.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_sleep_goal_response import GetSleepGoalResponse
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
    api_instance = fitbit_web_api.SleepApi(api_client)

    try:
        # Get Sleep Goal
        api_response = await api_instance.get_sleep_goal()
        print("The response of SleepApi->get_sleep_goal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SleepApi->get_sleep_goal: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetSleepGoalResponse**](GetSleepGoalResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                       | Response headers |
| ----------- | ----------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                             | -                |
| **401**     | The request requires user authentication.                         | -                |
| **403**     | The server understood the request, but is refusing to fulfill it. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sleep_list**

> GetSleepLogListResponse get_sleep_list(sort, offset, limit, before_date=before_date, after_date=after_date)

Get Sleep Logs List

The Get Sleep Logs List endpoint returns a list of a user's sleep logs (including naps) before or after a given day with offset, limit, and sort order.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
from fitbit_web_api.models.get_sleep_log_list_response import GetSleepLogListResponse
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
    api_instance = fitbit_web_api.SleepApi(api_client)
    sort = 'sort_example' # str | The sort order of entries by date asc (ascending) or desc (descending).
    offset = 0 # int | The offset number of entries. (default to 0)
    limit = 56 # int | The maximum number of entries returned (maximum;100).
    before_date = '2013-10-20' # date | The date in the format yyyy-MM-ddTHH:mm:ss. Only yyyy-MM-dd is required. Either beforeDate or afterDate should be specified. (optional)
    after_date = '2013-10-20' # date | The date in the format yyyy-MM-ddTHH:mm:ss. (optional)

    try:
        # Get Sleep Logs List
        api_response = await api_instance.get_sleep_list(sort, offset, limit, before_date=before_date, after_date=after_date)
        print("The response of SleepApi->get_sleep_list:\n")
        pprint(api_response)
    except Exception as e:
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

[**GetSleepLogListResponse**](GetSleepLogListResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                       | Response headers |
| ----------- | ----------------------------------------------------------------- | ---------------- |
| **200**     | A successful request.                                             | -                |
| **401**     | The request requires user authentication.                         | -                |
| **403**     | The server understood the request, but is refusing to fulfill it. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sleep_goal**

> update_sleep_goal(min_duration)

Update Sleep Goal

Create or update the user's sleep goal and get a response in the JSON format.

### Example

- OAuth Authentication (oauth2):

```python
import fitbit_web_api
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
    api_instance = fitbit_web_api.SleepApi(api_client)
    min_duration = 'min_duration_example' # str | Duration of sleep goal.

    try:
        # Update Sleep Goal
        await api_instance.update_sleep_goal(min_duration)
    except Exception as e:
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
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                       | Response headers |
| ----------- | ----------------------------------------------------------------- | ---------------- |
| **200**     | Successful request.                                               | -                |
| **401**     | The request requires user authentication.                         | -                |
| **403**     | The server understood the request, but is refusing to fulfill it. | -                |
| **201**     | A successful request.                                             | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
