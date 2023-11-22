# swagger_client.DevicesApi

All URIs are relative to *https://api.fitbit.com/*

| Method                                           | HTTP request                                                             | Description  |
| ------------------------------------------------ | ------------------------------------------------------------------------ | ------------ |
| [**add_alarms**](DevicesApi.md#add_alarms)       | **POST** /1/user/-/devices/tracker/{tracker-id}/alarms.json              | Add Alarm    |
| [**delete_alarms**](DevicesApi.md#delete_alarms) | **DELETE** /1/user/-/devices/tracker/{tracker-id}/alarms/{alarm-id}.json | Delete Alarm |
| [**get_alarms**](DevicesApi.md#get_alarms)       | **GET** /1/user/-/devices/tracker/{tracker-id}/alarms.json               | Get Alarms   |
| [**get_devices**](DevicesApi.md#get_devices)     | **GET** /1/user/-/devices.json                                           | Get Devices  |
| [**update_alarms**](DevicesApi.md#update_alarms) | **POST** /1/user/-/devices/tracker/{tracker-id}/alarms/{alarm-id}.json   | Update Alarm |

# **add_alarms**

> add_alarms(tracker_id, time, enabled, recurring, week_days)

Add Alarm

Adds the alarm settings to a given ID for a given device.

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
tracker_id = 56 # int | The ID of the tracker for which data is returned. The tracker-id value is found via the Get Devices endpoint.
time = 'time_example' # str | Time of day that the alarm vibrates with a UTC timezone offset, e.g. 07:15-08:00.
enabled = true # bool | true or false. If false, alarm does not vibrate until enabled is set to true.
recurring = 'recurring_example' # str | true or false. If false, the alarm is a single event.
week_days = 'week_days_example' # str | Comma separated list of days of the week on which the alarm vibrates, e.g. MONDAY, TUESDAY.

try:
    # Add Alarm
    api_instance.add_alarms(tracker_id, time, enabled, recurring, week_days)
except ApiException as e:
    print("Exception when calling DevicesApi->add_alarms: %s\n" % e)
```

### Parameters

| Name           | Type     | Description                                                                                                   | Notes |
| -------------- | -------- | ------------------------------------------------------------------------------------------------------------- | ----- |
| **tracker_id** | **int**  | The ID of the tracker for which data is returned. The tracker-id value is found via the Get Devices endpoint. |
| **time**       | **str**  | Time of day that the alarm vibrates with a UTC timezone offset, e.g. 07:15-08:00.                             |
| **enabled**    | **bool** | true or false. If false, alarm does not vibrate until enabled is set to true.                                 |
| **recurring**  | **str**  | true or false. If false, the alarm is a single event.                                                         |
| **week_days**  | **str**  | Comma separated list of days of the week on which the alarm vibrates, e.g. MONDAY, TUESDAY.                   |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alarms**

> delete_alarms(tracker_id, alarm_id)

Delete Alarm

Deletes the user's device alarm entry with the given ID for a given device.

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
tracker_id = 56 # int | The ID of the tracker whose alarms is managed. The tracker-id value is found via the Get Devices endpoint.
alarm_id = 56 # int | The ID of the alarm to be updated. The alarm-id value is found via the Get Alarms endpoint.

try:
    # Delete Alarm
    api_instance.delete_alarms(tracker_id, alarm_id)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_alarms: %s\n" % e)
```

### Parameters

| Name           | Type    | Description                                                                                                | Notes |
| -------------- | ------- | ---------------------------------------------------------------------------------------------------------- | ----- |
| **tracker_id** | **int** | The ID of the tracker whose alarms is managed. The tracker-id value is found via the Get Devices endpoint. |
| **alarm_id**   | **int** | The ID of the alarm to be updated. The alarm-id value is found via the Get Alarms endpoint.                |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alarms**

> get_alarms(tracker_id)

Get Alarms

Returns alarms for a device

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
tracker_id = 56 # int | The ID of the tracker for which data is returned. The tracker-id value is found via the Get Devices endpoint.

try:
    # Get Alarms
    api_instance.get_alarms(tracker_id)
except ApiException as e:
    print("Exception when calling DevicesApi->get_alarms: %s\n" % e)
```

### Parameters

| Name           | Type    | Description                                                                                                   | Notes |
| -------------- | ------- | ------------------------------------------------------------------------------------------------------------- | ----- |
| **tracker_id** | **int** | The ID of the tracker for which data is returned. The tracker-id value is found via the Get Devices endpoint. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices**

> get_devices()

Get Devices

Returns a list of the Fitbit devices connected to a user's account.

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))

try:
    # Get Devices
    api_instance.get_devices()
except ApiException as e:
    print("Exception when calling DevicesApi->get_devices: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_alarms**

> update_alarms(tracker_id, alarm_id, time, enabled, recurring, week_days, snooze_length, snooze_count)

Update Alarm

Updates the alarm entry with a given ID for a given device. It also gets a response in the format requested.

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
tracker_id = 56 # int | The ID of the tracker for which data is returned. The tracker-id value is found via the Get Devices endpoint.
alarm_id = 56 # int | The ID of the alarm to be updated. The alarm-id value is found in the response of the Get Activity endpoint.
time = 'time_example' # str | Time of day that the alarm vibrates with a UTC timezone offset, e.g. 07:15-08:00.
enabled = true # bool | true or false. If false, the alarm does not vibrate until enabled is set to true.
recurring = 'recurring_example' # str | true or false. If false, the alarm is a single event.
week_days = 'week_days_example' # str | Comma seperated list of days of the week on which the alarm vibrates, e.g. MONDAY, TUESDAY.
snooze_length = 56 # int | Minutes between alarms.
snooze_count = 56 # int | Maximum snooze count.

try:
    # Update Alarm
    api_instance.update_alarms(tracker_id, alarm_id, time, enabled, recurring, week_days, snooze_length, snooze_count)
except ApiException as e:
    print("Exception when calling DevicesApi->update_alarms: %s\n" % e)
```

### Parameters

| Name              | Type     | Description                                                                                                   | Notes |
| ----------------- | -------- | ------------------------------------------------------------------------------------------------------------- | ----- |
| **tracker_id**    | **int**  | The ID of the tracker for which data is returned. The tracker-id value is found via the Get Devices endpoint. |
| **alarm_id**      | **int**  | The ID of the alarm to be updated. The alarm-id value is found in the response of the Get Activity endpoint.  |
| **time**          | **str**  | Time of day that the alarm vibrates with a UTC timezone offset, e.g. 07:15-08:00.                             |
| **enabled**       | **bool** | true or false. If false, the alarm does not vibrate until enabled is set to true.                             |
| **recurring**     | **str**  | true or false. If false, the alarm is a single event.                                                         |
| **week_days**     | **str**  | Comma seperated list of days of the week on which the alarm vibrates, e.g. MONDAY, TUESDAY.                   |
| **snooze_length** | **int**  | Minutes between alarms.                                                                                       |
| **snooze_count**  | **int**  | Maximum snooze count.                                                                                         |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
