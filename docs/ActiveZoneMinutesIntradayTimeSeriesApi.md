# fitbit_web_api.ActiveZoneMinutesIntradayTimeSeriesApi

All URIs are relative to *https://api.fitbit.com/*

| Method                                                                                                                           | HTTP request                                                                                                     | Description                  |
| -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| [**get_azmby_date_intraday**](ActiveZoneMinutesIntradayTimeSeriesApi.md#get_azmby_date_intraday)                                 | **GET** /1/user/-/activities/active-zone-minutes/date/{date}/1d/{detail-level}.json                              | Get AZM Intraday by Date     |
| [**get_azmby_date_time_series_intraday**](ActiveZoneMinutesIntradayTimeSeriesApi.md#get_azmby_date_time_series_intraday)         | **GET** /1/user/-/activities/active-zone-minutes/date/{date}/1d/{detail-level}/time/{start-time}/{end-time}.json | Get AZM Intraday by Date     |
| [**get_azmby_interval_intraday**](ActiveZoneMinutesIntradayTimeSeriesApi.md#get_azmby_interval_intraday)                         | **GET** /1/user/-/activities/active-zone-minutes/date/{start-date}/{end-date}/{detail-level}.json                | Get AZM Intraday by Interval |
| [**get_azmby_interval_time_series_intraday**](ActiveZoneMinutesIntradayTimeSeriesApi.md#get_azmby_interval_time_series_intraday) | **GET** /1/user/-/activities/active-zone-minutes/date/{start-date}/{end-date}/time/{start-time}/{end-time}.json  | Get AZM Intraday by Interval |

# **get_azmby_date_intraday**

> get_azmby_date_intraday(\_date, detail_level)

Get AZM Intraday by Date

Returns the active zone minutes intraday data for a 24 hour period by specifying a date and/or time range.

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
api_instance = fitbit_web_api.ActiveZoneMinutesIntradayTimeSeriesApi(fitbit_web_api.ApiClient(configuration))
_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today
detail_level = 'detail_level_example' # str | The detail for which data will be returned. **Supported:** 1min | 5min | 15min

try:
    # Get AZM Intraday by Date
    api_instance.get_azmby_date_intraday(_date, detail_level)
except ApiException as e:
    print("Exception when calling ActiveZoneMinutesIntradayTimeSeriesApi->get_azmby_date_intraday: %s\n" % e)
```

### Parameters

| Name             | Type     | Description                                                     | Notes |
| ---------------- | -------- | --------------------------------------------------------------- | ----- | ----- |
| **\_date**       | **date** | The date in the format yyyy-MM-dd or today                      |
| **detail_level** | **str**  | The detail for which data will be returned. **Supported:** 1min | 5min  | 15min |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_azmby_date_time_series_intraday**

> get_azmby_date_time_series_intraday(\_date, detail_level, start_time, end_time)

Get AZM Intraday by Date

Returns the active zone minutes intraday data for a 24 hour period by specifying a date and/or time range.

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
api_instance = fitbit_web_api.ActiveZoneMinutesIntradayTimeSeriesApi(fitbit_web_api.ApiClient(configuration))
_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today
detail_level = 'detail_level_example' # str | The detail for which data will be returned. **Supported:** 1min | 5min | 15min
start_time = 'start_time_example' # str | The start of the period in the format HH:mm.
end_time = 'end_time_example' # str | The end of the period in the format HH:mm.

try:
    # Get AZM Intraday by Date
    api_instance.get_azmby_date_time_series_intraday(_date, detail_level, start_time, end_time)
except ApiException as e:
    print("Exception when calling ActiveZoneMinutesIntradayTimeSeriesApi->get_azmby_date_time_series_intraday: %s\n" % e)
```

### Parameters

| Name             | Type     | Description                                                     | Notes |
| ---------------- | -------- | --------------------------------------------------------------- | ----- | ----- |
| **\_date**       | **date** | The date in the format yyyy-MM-dd or today                      |
| **detail_level** | **str**  | The detail for which data will be returned. **Supported:** 1min | 5min  | 15min |
| **start_time**   | **str**  | The start of the period in the format HH:mm.                    |
| **end_time**     | **str**  | The end of the period in the format HH:mm.                      |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_azmby_interval_intraday**

> get_azmby_interval_intraday(start_date, end_date, detail_level)

Get AZM Intraday by Interval

Returns the active zone minutes intraday data for a 24 hour period by specifying a date range and/or time range.

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
api_instance = fitbit_web_api.ActiveZoneMinutesIntradayTimeSeriesApi(fitbit_web_api.ApiClient(configuration))
start_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today
end_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today
detail_level = 'detail_level_example' # str | The detail for which data will be returned. **Support:** 1min | 5min | 15min

try:
    # Get AZM Intraday by Interval
    api_instance.get_azmby_interval_intraday(start_date, end_date, detail_level)
except ApiException as e:
    print("Exception when calling ActiveZoneMinutesIntradayTimeSeriesApi->get_azmby_interval_intraday: %s\n" % e)
```

### Parameters

| Name             | Type     | Description                                                   | Notes |
| ---------------- | -------- | ------------------------------------------------------------- | ----- | ----- |
| **start_date**   | **date** | The date in the format yyyy-MM-dd or today                    |
| **end_date**     | **date** | The date in the format yyyy-MM-dd or today                    |
| **detail_level** | **str**  | The detail for which data will be returned. **Support:** 1min | 5min  | 15min |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_azmby_interval_time_series_intraday**

> get_azmby_interval_time_series_intraday(start_date, end_date, detail_level, start_time, end_time)

Get AZM Intraday by Interval

Returns the active zone minutes intraday data for a 24 hour period by specifying a date range and/or time range.

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
api_instance = fitbit_web_api.ActiveZoneMinutesIntradayTimeSeriesApi(fitbit_web_api.ApiClient(configuration))
start_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today
end_date = '2013-10-20' # date | The date in the format yyyy-MM-dd or today
detail_level = 'detail_level_example' # str | The detail for which data will be returned. **Support:** 1min | 5min | 15min
start_time = 'start_time_example' # str | The start of the period in the format HH:mm.
end_time = 'end_time_example' # str | The end of the period in the format HH:mm.

try:
    # Get AZM Intraday by Interval
    api_instance.get_azmby_interval_time_series_intraday(start_date, end_date, detail_level, start_time, end_time)
except ApiException as e:
    print("Exception when calling ActiveZoneMinutesIntradayTimeSeriesApi->get_azmby_interval_time_series_intraday: %s\n" % e)
```

### Parameters

| Name             | Type     | Description                                                   | Notes |
| ---------------- | -------- | ------------------------------------------------------------- | ----- | ----- |
| **start_date**   | **date** | The date in the format yyyy-MM-dd or today                    |
| **end_date**     | **date** | The date in the format yyyy-MM-dd or today                    |
| **detail_level** | **str**  | The detail for which data will be returned. **Support:** 1min | 5min  | 15min |
| **start_time**   | **str**  | The start of the period in the format HH:mm.                  |
| **end_time**     | **str**  | The end of the period in the format HH:mm.                    |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
