# swagger_client.ActiveZoneMinutesTimeSeriesApi

All URIs are relative to *https://api.fitbit.com/*

| Method                                                                                                   | HTTP request                                                                       | Description                     |
| -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------- |
| [**get_azm_time_series_by_date**](ActiveZoneMinutesTimeSeriesApi.md#get_azm_time_series_by_date)         | **GET** /1/user/-/activities/active-zone-minutes/date/{date}/{period}.json         | Get AZM Time Series by Date     |
| [**get_azm_time_series_by_interval**](ActiveZoneMinutesTimeSeriesApi.md#get_azm_time_series_by_interval) | **GET** /1/user/-/activities/active-zone-minutes/date/{start-date}/{end-date}.json | Get AZM Time Series by Interval |

# **get_azm_time_series_by_date**

> get_azm_time_series_by_date(\_date, period)

Get AZM Time Series by Date

Returns the daily summary values over a period of time by specifying a date and time period.

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
api_instance = swagger_client.ActiveZoneMinutesTimeSeriesApi(swagger_client.ApiClient(configuration))
_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today
period = 'period_example' # str | The range for which data will be returned. **Supported:** 1d | 7d | 30d | 1w | 1m | 3m | 6m | 1y

try:
    # Get AZM Time Series by Date
    api_instance.get_azm_time_series_by_date(_date, period)
except ApiException as e:
    print("Exception when calling ActiveZoneMinutesTimeSeriesApi->get_azm_time_series_by_date: %s\n" % e)
```

### Parameters

| Name       | Type     | Description                                                  | Notes |
| ---------- | -------- | ------------------------------------------------------------ | ----- | --- | --- | --- | --- | --- | --- |
| **\_date** | **date** | The date in the format yyyy-MM-dd or today                   |
| **period** | **str**  | The range for which data will be returned. **Supported:** 1d | 7d    | 30d | 1w  | 1m  | 3m  | 6m  | 1y  |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_azm_time_series_by_interval**

> get_azm_time_series_by_interval(start_date, end_date)

Get AZM Time Series by Interval

Returns the daily summary values over an interval by specifying a date range.

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
api_instance = swagger_client.ActiveZoneMinutesTimeSeriesApi(swagger_client.ApiClient(configuration))
start_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today
end_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today

try:
    # Get AZM Time Series by Interval
    api_instance.get_azm_time_series_by_interval(start_date, end_date)
except ApiException as e:
    print("Exception when calling ActiveZoneMinutesTimeSeriesApi->get_azm_time_series_by_interval: %s\n" % e)
```

### Parameters

| Name           | Type     | Description                                | Notes |
| -------------- | -------- | ------------------------------------------ | ----- |
| **start_date** | **date** | The date in the format yyyy-MM-dd or today |
| **end_date**   | **date** | The date in the format yyyy-MM-dd or today |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
