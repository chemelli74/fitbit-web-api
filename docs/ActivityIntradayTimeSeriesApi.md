# swagger_client.ActivityIntradayTimeSeriesApi

All URIs are relative to *https://api.fitbit.com/*

| Method                                                                                                                                                        | HTTP request                                                                                                         | Description                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| [**get_activities_resource_by_date_intraday**](ActivityIntradayTimeSeriesApi.md#get_activities_resource_by_date_intraday)                                     | **GET** /1/user/-/activities/{resource-path}/date/{date}/1d/{detail-level}.json                                      | Get Intraday Time Series          |
| [**get_activities_resource_by_date_range_intraday**](ActivityIntradayTimeSeriesApi.md#get_activities_resource_by_date_range_intraday)                         | **GET** /1/user/-/activities/{resource-path}/date/{base-date}/{end-date}/{detail-level}.json                         | Get Activity Intraday Time Series |
| [**get_activities_resource_by_date_range_time_series_intraday**](ActivityIntradayTimeSeriesApi.md#get_activities_resource_by_date_range_time_series_intraday) | **GET** /1/user/-/activities/{resource-path}/date/{date}/{end-date}/{detail-level}/time/{start-time}/{end-time}.json | Get Activity Intraday Time Series |
| [**get_activities_resource_by_date_time_series_intraday**](ActivityIntradayTimeSeriesApi.md#get_activities_resource_by_date_time_series_intraday)             | **GET** /1/user/-/activities/{resource-path}/date/{date}/1d/{detail-level}/time/{start-time}/{end-time}.json         | Get Intraday Time Series          |

# **get_activities_resource_by_date_intraday**

> get_activities_resource_by_date_intraday(\_resource_path, \_date, detail_level)

Get Intraday Time Series

Returns the Intraday Time Series for a given resource in the format requested.

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
api_instance = swagger_client.ActivityIntradayTimeSeriesApi(swagger_client.ApiClient(configuration))
_resource_path = '_resource_path_example' # str | The resource-path; see options in the Resource Path Options section in the full documentation.
_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today.
detail_level = 'detail_level_example' # str | Number of data points to include. Either 1min or 15min. Optional.

try:
    # Get Intraday Time Series
    api_instance.get_activities_resource_by_date_intraday(_resource_path, _date, detail_level)
except ApiException as e:
    print("Exception when calling ActivityIntradayTimeSeriesApi->get_activities_resource_by_date_intraday: %s\n" % e)
```

### Parameters

| Name                | Type     | Description                                                                                    | Notes |
| ------------------- | -------- | ---------------------------------------------------------------------------------------------- | ----- |
| **\_resource_path** | **str**  | The resource-path; see options in the Resource Path Options section in the full documentation. |
| **\_date**          | **date** | The date in the format yyyy-MM-dd or today.                                                    |
| **detail_level**    | **str**  | Number of data points to include. Either 1min or 15min. Optional.                              |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activities_resource_by_date_range_intraday**

> get_activities_resource_by_date_range_intraday(\_resource_path, base_date, end_date, detail_level)

Get Activity Intraday Time Series

Returns the Activity Intraday Time Series for a given resource in the format requested.

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
api_instance = swagger_client.ActivityIntradayTimeSeriesApi(swagger_client.ApiClient(configuration))
_resource_path = '_resource_path_example' # str | The resource-path; see options in the Resource Path Options section in the full documentation.
base_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today.
end_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today.
detail_level = 'detail_level_example' # str | Number of data points to include. Either 1min or 15min. Optional.

try:
    # Get Activity Intraday Time Series
    api_instance.get_activities_resource_by_date_range_intraday(_resource_path, base_date, end_date, detail_level)
except ApiException as e:
    print("Exception when calling ActivityIntradayTimeSeriesApi->get_activities_resource_by_date_range_intraday: %s\n" % e)
```

### Parameters

| Name                | Type     | Description                                                                                    | Notes |
| ------------------- | -------- | ---------------------------------------------------------------------------------------------- | ----- |
| **\_resource_path** | **str**  | The resource-path; see options in the Resource Path Options section in the full documentation. |
| **base_date**       | **date** | The date in the format yyyy-MM-dd or today.                                                    |
| **end_date**        | **date** | The date in the format yyyy-MM-dd or today.                                                    |
| **detail_level**    | **str**  | Number of data points to include. Either 1min or 15min. Optional.                              |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activities_resource_by_date_range_time_series_intraday**

> get_activities_resource_by_date_range_time_series_intraday(\_resource_path, \_date, end_date, detail_level, start_time, end_time)

Get Activity Intraday Time Series

Returns the Intraday Time Series for a given resource in the format requested.

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
api_instance = swagger_client.ActivityIntradayTimeSeriesApi(swagger_client.ApiClient(configuration))
_resource_path = '_resource_path_example' # str | The resource-path; see options in the Resource Path Options section in the full documentation.
_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today.
end_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today.
detail_level = 'detail_level_example' # str | Number of data points to include. Either 1min or 15min.
start_time = 'start_time_example' # str | The start of the period in the format HH:mm.
end_time = 'end_time_example' # str | The end of the period in the format HH:mm.

try:
    # Get Activity Intraday Time Series
    api_instance.get_activities_resource_by_date_range_time_series_intraday(_resource_path, _date, end_date, detail_level, start_time, end_time)
except ApiException as e:
    print("Exception when calling ActivityIntradayTimeSeriesApi->get_activities_resource_by_date_range_time_series_intraday: %s\n" % e)
```

### Parameters

| Name                | Type     | Description                                                                                    | Notes |
| ------------------- | -------- | ---------------------------------------------------------------------------------------------- | ----- |
| **\_resource_path** | **str**  | The resource-path; see options in the Resource Path Options section in the full documentation. |
| **\_date**          | **date** | The date in the format yyyy-MM-dd or today.                                                    |
| **end_date**        | **date** | The date in the format yyyy-MM-dd or today.                                                    |
| **detail_level**    | **str**  | Number of data points to include. Either 1min or 15min.                                        |
| **start_time**      | **str**  | The start of the period in the format HH:mm.                                                   |
| **end_time**        | **str**  | The end of the period in the format HH:mm.                                                     |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activities_resource_by_date_time_series_intraday**

> get_activities_resource_by_date_time_series_intraday(\_resource_path, \_date, detail_level, start_time, end_time)

Get Intraday Time Series

Returns the Intraday Time Series for a given resource in the format requested.

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
api_instance = swagger_client.ActivityIntradayTimeSeriesApi(swagger_client.ApiClient(configuration))
_resource_path = '_resource_path_example' # str | The resource-path; see options in the Resource Path Options section in the full documentation.
_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today.
detail_level = 'detail_level_example' # str | Number of data points to include. Either 1min or 15min.
start_time = 'start_time_example' # str | The start of the period in the format HH:mm.
end_time = 'end_time_example' # str | The end of the period in the format HH:mm.

try:
    # Get Intraday Time Series
    api_instance.get_activities_resource_by_date_time_series_intraday(_resource_path, _date, detail_level, start_time, end_time)
except ApiException as e:
    print("Exception when calling ActivityIntradayTimeSeriesApi->get_activities_resource_by_date_time_series_intraday: %s\n" % e)
```

### Parameters

| Name                | Type     | Description                                                                                    | Notes |
| ------------------- | -------- | ---------------------------------------------------------------------------------------------- | ----- |
| **\_resource_path** | **str**  | The resource-path; see options in the Resource Path Options section in the full documentation. |
| **\_date**          | **date** | The date in the format yyyy-MM-dd or today.                                                    |
| **detail_level**    | **str**  | Number of data points to include. Either 1min or 15min.                                        |
| **start_time**      | **str**  | The start of the period in the format HH:mm.                                                   |
| **end_time**        | **str**  | The end of the period in the format HH:mm.                                                     |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
