# fitbit_web_api.HeartRateVariabilityIntradayApi

All URIs are relative to *https://api.fitbit.com/*

| Method                                                                                              | HTTP request                                              | Description                  |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ---------------------------- |
| [**get_hrv_intraday_by_date**](HeartRateVariabilityIntradayApi.md#get_hrv_intraday_by_date)         | **GET** /1/user/-/hrv/date/{date}/all.json                | Get HRV Intraday by Date     |
| [**get_hrv_intraday_by_interval**](HeartRateVariabilityIntradayApi.md#get_hrv_intraday_by_interval) | **GET** /1/user/-/hrv/date/{startDate}/{endDate}/all.json | Get HRV Intraday by Interval |

# **get_hrv_intraday_by_date**

> get_hrv_intraday_by_date(\_date)

Get HRV Intraday by Date

This endpoint returns the Heart Rate Variability (HRV) intraday data for a single date. HRV data applies specifically to a user’s “main sleep,” which is the longest single period of time asleep on a given date.

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
api_instance = fitbit_web_api.HeartRateVariabilityIntradayApi(fitbit_web_api.ApiClient(configuration))
_date = '2013-10-20' # date | The date in the format of yyyy-MM-dd or today.

try:
    # Get HRV Intraday by Date
    api_instance.get_hrv_intraday_by_date(_date)
except ApiException as e:
    print("Exception when calling HeartRateVariabilityIntradayApi->get_hrv_intraday_by_date: %s\n" % e)
```

### Parameters

| Name       | Type     | Description                                    | Notes |
| ---------- | -------- | ---------------------------------------------- | ----- |
| **\_date** | **date** | The date in the format of yyyy-MM-dd or today. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hrv_intraday_by_interval**

> get_hrv_intraday_by_interval(start_date, end_date)

Get HRV Intraday by Interval

This endpoint returns the Heart Rate Variability (HRV) intraday data for a single date. HRV data applies specifically to a user’s “main sleep,” which is the longest single period of time asleep on a given date.

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
api_instance = fitbit_web_api.HeartRateVariabilityIntradayApi(fitbit_web_api.ApiClient(configuration))
start_date = '2013-10-20' # date | The date in the format of yyyy-MM-dd or today.
end_date = '2013-10-20' # date | The date in the format of yyyy-MM-dd or today.

try:
    # Get HRV Intraday by Interval
    api_instance.get_hrv_intraday_by_interval(start_date, end_date)
except ApiException as e:
    print("Exception when calling HeartRateVariabilityIntradayApi->get_hrv_intraday_by_interval: %s\n" % e)
```

### Parameters

| Name           | Type     | Description                                    | Notes |
| -------------- | -------- | ---------------------------------------------- | ----- |
| **start_date** | **date** | The date in the format of yyyy-MM-dd or today. |
| **end_date**   | **date** | The date in the format of yyyy-MM-dd or today. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
