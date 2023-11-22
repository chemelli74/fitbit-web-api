# swagger_client.SpO2IntradayApi

All URIs are relative to *https://api.fitbit.com/*

| Method                                                                                  | HTTP request                                               | Description                   |
| --------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------- |
| [**get_sp_o2_intraday_by_date**](SpO2IntradayApi.md#get_sp_o2_intraday_by_date)         | **GET** /1/user/-/spo2/date/{date}/all.json                | Get SpO2 Intraday by Date     |
| [**get_sp_o2_intraday_by_interval**](SpO2IntradayApi.md#get_sp_o2_intraday_by_interval) | **GET** /1/user/-/spo2/date/{startDate}/{endDate}/all.json | Get SpO2 Intraday by Interval |

# **get_sp_o2_intraday_by_date**

> get_sp_o2_intraday_by_date(\_date)

Get SpO2 Intraday by Date

This endpoint returns the SpO2 intraday data for a single date. SpO2 applies specifically to a user’s “main sleep”, which is the longest single period of time asleep on a given date.

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
api_instance = swagger_client.SpO2IntradayApi(swagger_client.ApiClient(configuration))
_date = '2013-10-20' # date | The date in the format of yyyy-MM-dd or today.

try:
    # Get SpO2 Intraday by Date
    api_instance.get_sp_o2_intraday_by_date(_date)
except ApiException as e:
    print("Exception when calling SpO2IntradayApi->get_sp_o2_intraday_by_date: %s\n" % e)
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

# **get_sp_o2_intraday_by_interval**

> get_sp_o2_intraday_by_interval(start_date, end_date)

Get SpO2 Intraday by Interval

This endpoint returns the SpO2 intraday data for a specified date range. SpO2 applies specifically to a user’s “main sleep”, which is the longest single period of time asleep on a given date.

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
api_instance = swagger_client.SpO2IntradayApi(swagger_client.ApiClient(configuration))
start_date = '2013-10-20' # date | The date in the format of yyyy-MM-dd or today.
end_date = '2013-10-20' # date | The date in the format of yyyy-MM-dd or today.

try:
    # Get SpO2 Intraday by Interval
    api_instance.get_sp_o2_intraday_by_interval(start_date, end_date)
except ApiException as e:
    print("Exception when calling SpO2IntradayApi->get_sp_o2_intraday_by_interval: %s\n" % e)
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
