# swagger_client.BreathingRateIntradayApi

All URIs are relative to *https://api.fitbit.com/*

| Method                                                                                                             | HTTP request                                             | Description                             |
| ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------- | --------------------------------------- |
| [**get_breathing_rate_intraday_by_date**](BreathingRateIntradayApi.md#get_breathing_rate_intraday_by_date)         | **GET** /1/user/-/br/date/{date}/all.json                | Get Breathing Rate Intraday by Date     |
| [**get_breathing_rate_intraday_by_interval**](BreathingRateIntradayApi.md#get_breathing_rate_intraday_by_interval) | **GET** /1/user/-/br/date/{startDate}/{endDate}/all.json | Get Breathing Rate Intraday by Interval |

# **get_breathing_rate_intraday_by_date**

> get_breathing_rate_intraday_by_date(\_date)

Get Breathing Rate Intraday by Date

This endpoint returns intraday breathing rate data for a single date. It measures the average breathing rate throughout the day and categories your breathing rate by sleep stage. Sleep stages vary between light sleep, deep sleep, REM sleep, and full sleep.

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
api_instance = swagger_client.BreathingRateIntradayApi(swagger_client.ApiClient(configuration))
_date = '2013-10-20' # date | The date in the format of yyyy-MM-dd or today.

try:
    # Get Breathing Rate Intraday by Date
    api_instance.get_breathing_rate_intraday_by_date(_date)
except ApiException as e:
    print("Exception when calling BreathingRateIntradayApi->get_breathing_rate_intraday_by_date: %s\n" % e)
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

# **get_breathing_rate_intraday_by_interval**

> get_breathing_rate_intraday_by_interval(start_date, end_date)

Get Breathing Rate Intraday by Interval

This endpoint returns intraday breathing rate data for a date range. It measures the average breathing rate throughout the day and categories your breathing rate by sleep stage. Sleep stages vary between light sleep, deep sleep, REM sleep, and full sleep.

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
api_instance = swagger_client.BreathingRateIntradayApi(swagger_client.ApiClient(configuration))
start_date = '2013-10-20' # date | The date in the format of yyyy-MM-dd or today.
end_date = '2013-10-20' # date | The date in the format of yyyy-MM-dd or today.

try:
    # Get Breathing Rate Intraday by Interval
    api_instance.get_breathing_rate_intraday_by_interval(start_date, end_date)
except ApiException as e:
    print("Exception when calling BreathingRateIntradayApi->get_breathing_rate_intraday_by_interval: %s\n" % e)
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
