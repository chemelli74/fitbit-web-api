# fitbit_web_api.NutritionTimeSeriesApi

All URIs are relative to *https://api.fitbit.com/*

| Method                                                                                               | HTTP request                                                                 | Description                   |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ----------------------------- |
| [**get_foods_by_date_range**](NutritionTimeSeriesApi.md#get_foods_by_date_range)                     | **GET** /1/user/-/foods/log/{resource-path}/date/{base-date}/{end-date}.json | Get Food or Water Time Series |
| [**get_foods_resource_by_date_period**](NutritionTimeSeriesApi.md#get_foods_resource_by_date_period) | **GET** /1/user/-/foods/log/{resource-path}/date/{date}/{period}.json        | Get Food or Water Time Series |

# **get_foods_by_date_range**

> get_foods_by_date_range(\_resource_path, base_date, end_date)

Get Food or Water Time Series

Updates a user's daily activity goals and returns a response using units in the unit system which corresponds to the Accept-Language header provided.

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
api_instance = fitbit_web_api.NutritionTimeSeriesApi(fitbit_web_api.ApiClient(configuration))
_resource_path = '_resource_path_example' # str | The resouce path. See options in the Resouce Path Options section in the full documentation.
base_date = '2013-10-20' # date | The range start date in the format yyyy-MM-dd or today.
end_date = '2013-10-20' # date | The end date of the range.

try:
    # Get Food or Water Time Series
    api_instance.get_foods_by_date_range(_resource_path, base_date, end_date)
except ApiException as e:
    print("Exception when calling NutritionTimeSeriesApi->get_foods_by_date_range: %s\n" % e)
```

### Parameters

| Name                | Type     | Description                                                                                  | Notes |
| ------------------- | -------- | -------------------------------------------------------------------------------------------- | ----- |
| **\_resource_path** | **str**  | The resouce path. See options in the Resouce Path Options section in the full documentation. |
| **base_date**       | **date** | The range start date in the format yyyy-MM-dd or today.                                      |
| **end_date**        | **date** | The end date of the range.                                                                   |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_foods_resource_by_date_period**

> get_foods_resource_by_date_period(\_resource_path, \_date, period)

Get Food or Water Time Series

Updates a user's daily activity goals and returns a response using units in the unit system which corresponds to the Accept-Language header provided.

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
api_instance = fitbit_web_api.NutritionTimeSeriesApi(fitbit_web_api.ApiClient(configuration))
_resource_path = '_resource_path_example' # str | The resouce path. See options in the Resouce Path Options section in the full documentation.
_date = '2013-10-20' # date | The end date of the period specified in the format yyyy-MM-dd or today.
period = 'period_example' # str | The range for which data will be returned. Options are 1d, 7d, 30d, 1w, 3m, 6m, 1y, or max.

try:
    # Get Food or Water Time Series
    api_instance.get_foods_resource_by_date_period(_resource_path, _date, period)
except ApiException as e:
    print("Exception when calling NutritionTimeSeriesApi->get_foods_resource_by_date_period: %s\n" % e)
```

### Parameters

| Name                | Type     | Description                                                                                  | Notes |
| ------------------- | -------- | -------------------------------------------------------------------------------------------- | ----- |
| **\_resource_path** | **str**  | The resouce path. See options in the Resouce Path Options section in the full documentation. |
| **\_date**          | **date** | The end date of the period specified in the format yyyy-MM-dd or today.                      |
| **period**          | **str**  | The range for which data will be returned. Options are 1d, 7d, 30d, 1w, 3m, 6m, 1y, or max.  |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
