# swagger_client.ElectrocardiogramApi

All URIs are relative to *https://api.fitbit.com/*

| Method                                                           | HTTP request                    | Description      |
| ---------------------------------------------------------------- | ------------------------------- | ---------------- |
| [**get_ecg_log_list**](ElectrocardiogramApi.md#get_ecg_log_list) | **GET** /1/user/-/ecg/list.json | Get ECG Log List |

# **get_ecg_log_list**

> get_ecg_log_list(sort, offset, limit, before_date=before_date, after_date=after_date)

Get ECG Log List

This endpoint is used for querying the user's on-device ECG readings.

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
api_instance = swagger_client.ElectrocardiogramApi(swagger_client.ApiClient(configuration))
sort = 'sort_example' # str | The sort order of entries by date asc (ascending) or desc (descending).
offset = 0 # int | The offset number of entries. (default to 0)
limit = 56 # int | The maximum number of entries returned (maximum;10).
before_date = '2013-10-20' # date | The date in the format yyyy-MM-ddTHH:mm:ss. Only yyyy-MM-dd is required. Either beforeDate or afterDate should be specified. (optional)
after_date = '2013-10-20' # date | The date in the format yyyy-MM-ddTHH:mm:ss. (optional)

try:
    # Get ECG Log List
    api_instance.get_ecg_log_list(sort, offset, limit, before_date=before_date, after_date=after_date)
except ApiException as e:
    print("Exception when calling ElectrocardiogramApi->get_ecg_log_list: %s\n" % e)
```

### Parameters

| Name            | Type     | Description                                                                                                                  | Notes          |
| --------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------- | -------------- |
| **sort**        | **str**  | The sort order of entries by date asc (ascending) or desc (descending).                                                      |
| **offset**      | **int**  | The offset number of entries.                                                                                                | [default to 0] |
| **limit**       | **int**  | The maximum number of entries returned (maximum;10).                                                                         |
| **before_date** | **date** | The date in the format yyyy-MM-ddTHH:mm:ss. Only yyyy-MM-dd is required. Either beforeDate or afterDate should be specified. | [optional]     |
| **after_date**  | **date** | The date in the format yyyy-MM-ddTHH:mm:ss.                                                                                  | [optional]     |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
