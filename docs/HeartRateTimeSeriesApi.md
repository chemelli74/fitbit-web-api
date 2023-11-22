# fitbit_web_api.HeartRateTimeSeriesApi

All URIs are relative to *https://api.fitbit.com/*

| Method                                                                             | HTTP request                                                        | Description                |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------- | -------------------------- |
| [**get_heart_by_date_period**](HeartRateTimeSeriesApi.md#get_heart_by_date_period) | **GET** /1/user/-/activities/heart/date/{date}/{period}.json        | Get Heart Rate Time Series |
| [**get_heart_by_date_range**](HeartRateTimeSeriesApi.md#get_heart_by_date_range)   | **GET** /1/user/-/activities/heart/date/{base-date}/{end-date}.json | Get Heart Rate Time Series |

# **get_heart_by_date_period**

> get_heart_by_date_period(\_date, period)

Get Heart Rate Time Series

Returns the time series data in the specified range for a given resource in the format requested using units in the unit systems that corresponds to the Accept-Language header provided.

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
api_instance = fitbit_web_api.HeartRateTimeSeriesApi(fitbit_web_api.ApiClient(configuration))
_date = '2013-10-20' # date | The end date of the period specified in the format yyyy-MM-dd or today.
period = 'period_example' # str | The range of which data will be returned. Options are 1d, 7d, 30d, 1w, and 1m.

try:
    # Get Heart Rate Time Series
    api_instance.get_heart_by_date_period(_date, period)
except ApiException as e:
    print("Exception when calling HeartRateTimeSeriesApi->get_heart_by_date_period: %s\n" % e)
```

### Parameters

| Name       | Type     | Description                                                                    | Notes |
| ---------- | -------- | ------------------------------------------------------------------------------ | ----- |
| **\_date** | **date** | The end date of the period specified in the format yyyy-MM-dd or today.        |
| **period** | **str**  | The range of which data will be returned. Options are 1d, 7d, 30d, 1w, and 1m. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heart_by_date_range**

> get_heart_by_date_range(base_date, end_date)

Get Heart Rate Time Series

Returns the time series data in the specified range for a given resource in the format requested using units in the unit systems that corresponds to the Accept-Language header provided.

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
api_instance = fitbit_web_api.HeartRateTimeSeriesApi(fitbit_web_api.ApiClient(configuration))
base_date = 'base_date_example' # str | The range start date in  the format yyyy-MM-dd or today.
end_date = '2013-10-20' # date | The end date of the range.

try:
    # Get Heart Rate Time Series
    api_instance.get_heart_by_date_range(base_date, end_date)
except ApiException as e:
    print("Exception when calling HeartRateTimeSeriesApi->get_heart_by_date_range: %s\n" % e)
```

### Parameters

| Name          | Type     | Description                                             | Notes |
| ------------- | -------- | ------------------------------------------------------- | ----- |
| **base_date** | **str**  | The range start date in the format yyyy-MM-dd or today. |
| **end_date**  | **date** | The end date of the range.                              |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
