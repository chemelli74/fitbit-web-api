# fitbit_web_api.HeartRateIntradayTimeSeriesApi

All URIs are relative to *https://api.fitbit.com/*

| Method                                                                                                                         | HTTP request                                                                                               | Description                         |
| ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| [**get_heart_by_date_intraday**](HeartRateIntradayTimeSeriesApi.md#get_heart_by_date_intraday)                                 | **GET** /1/user/-/activities/heart/date/{date}/1d/{detail-level}.json                                      | Get Heart Rate Intraday Time Series |
| [**get_heart_by_date_range_intraday**](HeartRateIntradayTimeSeriesApi.md#get_heart_by_date_range_intraday)                     | **GET** /1/user/-/activities/heart/date/{date}/{end-date}/{detail-level}.json                              | Get Heart Rate Intraday Time Series |
| [**get_heart_by_date_range_timestamp_intraday**](HeartRateIntradayTimeSeriesApi.md#get_heart_by_date_range_timestamp_intraday) | **GET** /1/user/-/activities/heart/date/{date}/{end-date}/{detail-level}/time/{start-time}/{end-time}.json | Get Heart Rate Intraday Time Series |
| [**get_heart_by_date_timestamp_intraday**](HeartRateIntradayTimeSeriesApi.md#get_heart_by_date_timestamp_intraday)             | **GET** /1/user/-/activities/heart/date/{date}/1d/{detail-level}/time/{start-time}/{end-time}.json         | Get Heart Rate Intraday Time Series |

# **get_heart_by_date_intraday**

> get_heart_by_date_intraday(\_date, detail_level)

Get Heart Rate Intraday Time Series

Returns the intraday time series for a given resource in the format requested. If your application has the appropriate access, your calls to a time series endpoint for a specific day (by using start and end dates on the same day or a period of 1d), the response will include extended intraday values with a one-minute detail level for that day. Unlike other time series calls that allow fetching data of other users, intraday data is available only for and to the authorized user.

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
api_instance = fitbit_web_api.HeartRateIntradayTimeSeriesApi(fitbit_web_api.ApiClient(configuration))
_date = '2013-10-20' # date | The date in the format of yyyy-MM-dd or today.
detail_level = 'detail_level_example' # str | The number of data points to include either 1sec, 1min, 5min or 15min.

try:
    # Get Heart Rate Intraday Time Series
    api_instance.get_heart_by_date_intraday(_date, detail_level)
except ApiException as e:
    print("Exception when calling HeartRateIntradayTimeSeriesApi->get_heart_by_date_intraday: %s\n" % e)
```

### Parameters

| Name             | Type     | Description                                                            | Notes |
| ---------------- | -------- | ---------------------------------------------------------------------- | ----- |
| **\_date**       | **date** | The date in the format of yyyy-MM-dd or today.                         |
| **detail_level** | **str**  | The number of data points to include either 1sec, 1min, 5min or 15min. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heart_by_date_range_intraday**

> get_heart_by_date_range_intraday(\_date, end_date, detail_level)

Get Heart Rate Intraday Time Series

Returns the intraday time series for a given resource in the format requested. If your application has the appropriate access, your calls to a time series endpoint for a specific day (by using start and end dates on the same day or a period of 1d), the response will include extended intraday values with a one-minute detail level for that day. Unlike other time series calls that allow fetching data of other users, intraday data is available only for and to the authorized user.

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
api_instance = fitbit_web_api.HeartRateIntradayTimeSeriesApi(fitbit_web_api.ApiClient(configuration))
_date = '2013-10-20' # date | The date in the format of yyyy-MM-dd or today.
end_date = '2013-10-20' # date | The end date in the format of yyyy-MM-dd or today.
detail_level = 'detail_level_example' # str | The number of data points to include either 1sec, 1min, 5min or 15min.

try:
    # Get Heart Rate Intraday Time Series
    api_instance.get_heart_by_date_range_intraday(_date, end_date, detail_level)
except ApiException as e:
    print("Exception when calling HeartRateIntradayTimeSeriesApi->get_heart_by_date_range_intraday: %s\n" % e)
```

### Parameters

| Name             | Type     | Description                                                            | Notes |
| ---------------- | -------- | ---------------------------------------------------------------------- | ----- |
| **\_date**       | **date** | The date in the format of yyyy-MM-dd or today.                         |
| **end_date**     | **date** | The end date in the format of yyyy-MM-dd or today.                     |
| **detail_level** | **str**  | The number of data points to include either 1sec, 1min, 5min or 15min. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heart_by_date_range_timestamp_intraday**

> get_heart_by_date_range_timestamp_intraday(\_date, end_date, detail_level, start_time, end_time)

Get Heart Rate Intraday Time Series

Returns the intraday time series for a given resource in the format requested. If your application has the appropriate access, your calls to a time series endpoint for a specific day (by using start and end dates on the same day or a period of 1d), the response will include extended intraday values with a one-minute detail level for that day. Unlike other time series calls that allow fetching data of other users, intraday data is available only for and to the authorized user.

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
api_instance = fitbit_web_api.HeartRateIntradayTimeSeriesApi(fitbit_web_api.ApiClient(configuration))
_date = '2013-10-20' # date | The date in the format of yyyy-MM-dd or today.
end_date = '2013-10-20' # date | The end date in the format of yyyy-MM-dd or today.
detail_level = 'detail_level_example' # str | The number of data points to include either 1sec, 1min, 5min or 15min.
start_time = 'start_time_example' # str | The start of the period in the format of HH:mm.
end_time = 'end_time_example' # str | The end time of the period in the format of HH:mm.

try:
    # Get Heart Rate Intraday Time Series
    api_instance.get_heart_by_date_range_timestamp_intraday(_date, end_date, detail_level, start_time, end_time)
except ApiException as e:
    print("Exception when calling HeartRateIntradayTimeSeriesApi->get_heart_by_date_range_timestamp_intraday: %s\n" % e)
```

### Parameters

| Name             | Type     | Description                                                            | Notes |
| ---------------- | -------- | ---------------------------------------------------------------------- | ----- |
| **\_date**       | **date** | The date in the format of yyyy-MM-dd or today.                         |
| **end_date**     | **date** | The end date in the format of yyyy-MM-dd or today.                     |
| **detail_level** | **str**  | The number of data points to include either 1sec, 1min, 5min or 15min. |
| **start_time**   | **str**  | The start of the period in the format of HH:mm.                        |
| **end_time**     | **str**  | The end time of the period in the format of HH:mm.                     |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heart_by_date_timestamp_intraday**

> get_heart_by_date_timestamp_intraday(\_date, detail_level, start_time, end_time)

Get Heart Rate Intraday Time Series

Returns the intraday time series for a given resource in the format requested. If your application has the appropriate access, your calls to a time series endpoint for a specific day (by using start and end dates on the same day or a period of 1d), the response will include extended intraday values with a one-minute detail level for that day. Unlike other time series calls that allow fetching data of other users, intraday data is available only for and to the authorized user.

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
api_instance = fitbit_web_api.HeartRateIntradayTimeSeriesApi(fitbit_web_api.ApiClient(configuration))
_date = '2013-10-20' # date | The date in the format of yyyy-MM-dd or today.
detail_level = 'detail_level_example' # str | The number of data points to include either 1sec, 1min, 5min or 15min.
start_time = 'start_time_example' # str | The start of the period in the format of HH:mm.
end_time = 'end_time_example' # str | The end time of the period in the format of HH:mm.

try:
    # Get Heart Rate Intraday Time Series
    api_instance.get_heart_by_date_timestamp_intraday(_date, detail_level, start_time, end_time)
except ApiException as e:
    print("Exception when calling HeartRateIntradayTimeSeriesApi->get_heart_by_date_timestamp_intraday: %s\n" % e)
```

### Parameters

| Name             | Type     | Description                                                            | Notes |
| ---------------- | -------- | ---------------------------------------------------------------------- | ----- |
| **\_date**       | **date** | The date in the format of yyyy-MM-dd or today.                         |
| **detail_level** | **str**  | The number of data points to include either 1sec, 1min, 5min or 15min. |
| **start_time**   | **str**  | The start of the period in the format of HH:mm.                        |
| **end_time**     | **str**  | The end time of the period in the format of HH:mm.                     |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
