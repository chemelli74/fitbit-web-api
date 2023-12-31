# fitbit_web_api.CardioFitnessScoreVO2MaxApi

All URIs are relative to *https://api.fitbit.com/*

| Method                                                                                                | HTTP request                                                  | Description                     |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------- |
| [**get_vo2_max_summary_by_date**](CardioFitnessScoreVO2MaxApi.md#get_vo2_max_summary_by_date)         | **GET** /1/user/-/cardioscore/date/{date}.json                | Get VO2 Max Summary by Date     |
| [**get_vo2_max_summary_by_interval**](CardioFitnessScoreVO2MaxApi.md#get_vo2_max_summary_by_interval) | **GET** /1/user/-/cardioscore/date/{startDate}/{endDate}.json | Get VO2 Max Summary by Interval |

# **get_vo2_max_summary_by_date**

> get_vo2_max_summary_by_date(\_date)

Get VO2 Max Summary by Date

This endpoint returns the Cardio Fitness Score (VO2 Max) data for a single date. VO2 Max values will be shown as a range if no run data is available or a single numeric value if the user uses a GPS for runs.

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
api_instance = fitbit_web_api.CardioFitnessScoreVO2MaxApi(fitbit_web_api.ApiClient(configuration))
_date = '2013-10-20' # date | The date in the format of yyyy-MM-dd or today.

try:
    # Get VO2 Max Summary by Date
    api_instance.get_vo2_max_summary_by_date(_date)
except ApiException as e:
    print("Exception when calling CardioFitnessScoreVO2MaxApi->get_vo2_max_summary_by_date: %s\n" % e)
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

# **get_vo2_max_summary_by_interval**

> get_vo2_max_summary_by_interval(start_date, end_date)

Get VO2 Max Summary by Interval

This endpoint returns the Cardio Fitness Score (VO2 Max) data for a date range. VO2 Max values will be shown as a range if no run data is available or a single numeric value if the user uses a GPS for runs.

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
api_instance = fitbit_web_api.CardioFitnessScoreVO2MaxApi(fitbit_web_api.ApiClient(configuration))
start_date = '2013-10-20' # date | The date in the format of yyyy-MM-dd or today.
end_date = '2013-10-20' # date | The date in the format of yyyy-MM-dd or today.

try:
    # Get VO2 Max Summary by Interval
    api_instance.get_vo2_max_summary_by_interval(start_date, end_date)
except ApiException as e:
    print("Exception when calling CardioFitnessScoreVO2MaxApi->get_vo2_max_summary_by_interval: %s\n" % e)
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
