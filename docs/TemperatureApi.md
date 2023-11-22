# fitbit_web_api.TemperatureApi

All URIs are relative to *https://api.fitbit.com/*

| Method                                                                                       | HTTP request                                                | Description                                |
| -------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------ |
| [**get_temp_core_summary_by_date**](TemperatureApi.md#get_temp_core_summary_by_date)         | **GET** /1/user/-/temp/core/date/{date}.json                | Get Temperature (Core) Summary by Date     |
| [**get_temp_core_summary_by_interval**](TemperatureApi.md#get_temp_core_summary_by_interval) | **GET** /1/user/-/temp/core/date/{startDate}/{endDate}.json | Get Temperature (Core) Summary by Interval |
| [**get_temp_skin_summary_by_interval**](TemperatureApi.md#get_temp_skin_summary_by_interval) | **GET** /1/user/-/temp/skin/date/{startDate}/{endDate}.json | Get Temperature (Skin) Summary by Interval |
| [**get_temp_skin_summary_date**](TemperatureApi.md#get_temp_skin_summary_date)               | **GET** /1/user/-/temp/skin/date/{date}.json                | Get Temperature (Skin) Summary by Date     |

# **get_temp_core_summary_by_date**

> get_temp_core_summary_by_date(\_date)

Get Temperature (Core) Summary by Date

Returns the Temperature (Core) data for a single date. Temperature (Core) data applies specifically to data logged manually by the user throughout the day.

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
api_instance = fitbit_web_api.TemperatureApi(fitbit_web_api.ApiClient(configuration))
_date = '2013-10-20' # date | The date in the format of yyyy-MM-dd or today.

try:
    # Get Temperature (Core) Summary by Date
    api_instance.get_temp_core_summary_by_date(_date)
except ApiException as e:
    print("Exception when calling TemperatureApi->get_temp_core_summary_by_date: %s\n" % e)
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

# **get_temp_core_summary_by_interval**

> get_temp_core_summary_by_interval(start_date, end_date)

Get Temperature (Core) Summary by Interval

Returns Temperature (Core) data for a date range. Temperature (Core) data applies specifically to data logged manually by the user throughout the day and the maximum date range cannot exceed 30 days.

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
api_instance = fitbit_web_api.TemperatureApi(fitbit_web_api.ApiClient(configuration))
start_date = '2013-10-20' # date | The date in the format of yyyy-MM-dd or today.
end_date = '2013-10-20' # date | The date in the format of yyyy-MM-dd or today.

try:
    # Get Temperature (Core) Summary by Interval
    api_instance.get_temp_core_summary_by_interval(start_date, end_date)
except ApiException as e:
    print("Exception when calling TemperatureApi->get_temp_core_summary_by_interval: %s\n" % e)
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

# **get_temp_skin_summary_by_interval**

> get_temp_skin_summary_by_interval(start_date, end_date)

Get Temperature (Skin) Summary by Interval

Returns Temperature (Skin) data for a date range. It only returns a value for dates on which the Fitbit device was able to record Temperature (skin) data and the maximum date range cannot exceed 30 days.

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
api_instance = fitbit_web_api.TemperatureApi(fitbit_web_api.ApiClient(configuration))
start_date = '2013-10-20' # date | The date in the format of yyyy-MM-dd or today.
end_date = '2013-10-20' # date | The date in the format of yyyy-MM-dd or today.

try:
    # Get Temperature (Skin) Summary by Interval
    api_instance.get_temp_skin_summary_by_interval(start_date, end_date)
except ApiException as e:
    print("Exception when calling TemperatureApi->get_temp_skin_summary_by_interval: %s\n" % e)
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

# **get_temp_skin_summary_date**

> get_temp_skin_summary_date(\_date)

Get Temperature (Skin) Summary by Date

Returns the Temperature (Skin) data for a single date. Temperature (Skin) data applies specifically to a user’s “main sleep”, which is the longest single period of time asleep on a given date.

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
api_instance = fitbit_web_api.TemperatureApi(fitbit_web_api.ApiClient(configuration))
_date = '2013-10-20' # date | The date in the format of yyyy-MM-dd or today.

try:
    # Get Temperature (Skin) Summary by Date
    api_instance.get_temp_skin_summary_date(_date)
except ApiException as e:
    print("Exception when calling TemperatureApi->get_temp_skin_summary_date: %s\n" % e)
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
