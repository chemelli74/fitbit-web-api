# swagger_client.ActivityTimeSeriesApi

All URIs are relative to *https://api.fitbit.com/*

| Method                                                                                                                        | HTTP request                                                                          | Description                                             |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| [**get_activities_resource_by_date_period**](ActivityTimeSeriesApi.md#get_activities_resource_by_date_period)                 | **GET** /1/user/-/activities/{resource-path}/date/{date}/{period}.json                | Get Activity Time Series                                |
| [**get_activities_resource_by_date_range**](ActivityTimeSeriesApi.md#get_activities_resource_by_date_range)                   | **GET** /1/user/-/activities/{resource-path}/date/{base-date}/{end-date}.json         | Get Activity Resource by Date Range                     |
| [**get_activities_tracker_resource_by_date_period**](ActivityTimeSeriesApi.md#get_activities_tracker_resource_by_date_period) | **GET** /1/user/-/activities/tracker/{resource-path}/date/{date}/{period}.json        | Get Activity Time Series                                |
| [**get_activities_tracker_resource_by_date_range**](ActivityTimeSeriesApi.md#get_activities_tracker_resource_by_date_range)   | **GET** /1/user/-/activities/tracker/{resource-path}/date/{base-date}/{end-date}.json | Get Activity Tracker Resource by Date Range Time Series |

# **get_activities_resource_by_date_period**

> get_activities_resource_by_date_period(\_resource_path, \_date, period)

Get Activity Time Series

Returns time series data in the specified range for a given resource in the format requested using units in the unit system that corresponds to the Accept-Language header provided.

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
api_instance = swagger_client.ActivityTimeSeriesApi(swagger_client.ApiClient(configuration))
_resource_path = '_resource_path_example' # str | The resource-path; see options in the Resource Path Options section in the full documentation.
_date = '2013-10-20' # date | The end date of the period specified in the format yyyy-MM-dd or today.
period = 'period_example' # str | The range for which data will be returned. Options are 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, or max.

try:
    # Get Activity Time Series
    api_instance.get_activities_resource_by_date_period(_resource_path, _date, period)
except ApiException as e:
    print("Exception when calling ActivityTimeSeriesApi->get_activities_resource_by_date_period: %s\n" % e)
```

### Parameters

| Name                | Type     | Description                                                                                     | Notes |
| ------------------- | -------- | ----------------------------------------------------------------------------------------------- | ----- |
| **\_resource_path** | **str**  | The resource-path; see options in the Resource Path Options section in the full documentation.  |
| **\_date**          | **date** | The end date of the period specified in the format yyyy-MM-dd or today.                         |
| **period**          | **str**  | The range for which data will be returned. Options are 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, or max. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activities_resource_by_date_range**

> get_activities_resource_by_date_range(\_resource_path, base_date, end_date)

Get Activity Resource by Date Range

Returns activities time series data in the specified range for a given resource.

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
api_instance = swagger_client.ActivityTimeSeriesApi(swagger_client.ApiClient(configuration))
_resource_path = '_resource_path_example' # str | The resource-path; see options in the Resource Path Options section in the full documentation.
base_date = '2013-10-20' # date | The range start date in the format yyyy-MM-dd or today.
end_date = '2013-10-20' # date | The end date of the range.

try:
    # Get Activity Resource by Date Range
    api_instance.get_activities_resource_by_date_range(_resource_path, base_date, end_date)
except ApiException as e:
    print("Exception when calling ActivityTimeSeriesApi->get_activities_resource_by_date_range: %s\n" % e)
```

### Parameters

| Name                | Type     | Description                                                                                    | Notes |
| ------------------- | -------- | ---------------------------------------------------------------------------------------------- | ----- |
| **\_resource_path** | **str**  | The resource-path; see options in the Resource Path Options section in the full documentation. |
| **base_date**       | **date** | The range start date in the format yyyy-MM-dd or today.                                        |
| **end_date**        | **date** | The end date of the range.                                                                     |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activities_tracker_resource_by_date_period**

> get_activities_tracker_resource_by_date_period(\_resource_path, \_date, period)

Get Activity Time Series

Returns time series data in the specified range for a given resource in the format requested using units in the unit system that corresponds to the Accept-Language header provided.

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
api_instance = swagger_client.ActivityTimeSeriesApi(swagger_client.ApiClient(configuration))
_resource_path = '_resource_path_example' # str | The resource-path; see options in the Resource Path Options section in the full documentation.
_date = '2013-10-20' # date | The end date of the period specified in the format yyyy-MM-dd or today.
period = 'period_example' # str | The range for which data will be returned. Options are 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, or max.

try:
    # Get Activity Time Series
    api_instance.get_activities_tracker_resource_by_date_period(_resource_path, _date, period)
except ApiException as e:
    print("Exception when calling ActivityTimeSeriesApi->get_activities_tracker_resource_by_date_period: %s\n" % e)
```

### Parameters

| Name                | Type     | Description                                                                                     | Notes |
| ------------------- | -------- | ----------------------------------------------------------------------------------------------- | ----- |
| **\_resource_path** | **str**  | The resource-path; see options in the Resource Path Options section in the full documentation.  |
| **\_date**          | **date** | The end date of the period specified in the format yyyy-MM-dd or today.                         |
| **period**          | **str**  | The range for which data will be returned. Options are 1d, 7d, 30d, 1w, 1m, 3m, 6m, 1y, or max. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activities_tracker_resource_by_date_range**

> get_activities_tracker_resource_by_date_range(\_resource_path, base_date, end_date)

Get Activity Tracker Resource by Date Range Time Series

Returns time series data in the specified range for a given resource.

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
api_instance = swagger_client.ActivityTimeSeriesApi(swagger_client.ApiClient(configuration))
_resource_path = '_resource_path_example' # str | The resource-path; see options in the Resource Path Options section in the full documentation.
base_date = '2013-10-20' # date | The range start date in the format yyyy-MM-dd or today.
end_date = '2013-10-20' # date | The end date of the range.

try:
    # Get Activity Tracker Resource by Date Range Time Series
    api_instance.get_activities_tracker_resource_by_date_range(_resource_path, base_date, end_date)
except ApiException as e:
    print("Exception when calling ActivityTimeSeriesApi->get_activities_tracker_resource_by_date_range: %s\n" % e)
```

### Parameters

| Name                | Type     | Description                                                                                    | Notes |
| ------------------- | -------- | ---------------------------------------------------------------------------------------------- | ----- |
| **\_resource_path** | **str**  | The resource-path; see options in the Resource Path Options section in the full documentation. |
| **base_date**       | **date** | The range start date in the format yyyy-MM-dd or today.                                        |
| **end_date**        | **date** | The end date of the range.                                                                     |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
