# swagger_client.ActivityApi

All URIs are relative to *https://api.fitbit.com/*

| Method                                                                        | HTTP request                                                | Description                  |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------- | ---------------------------- |
| [**add_activities_log**](ActivityApi.md#add_activities_log)                   | **POST** /1/user/-/activities.json                          | Log Activity                 |
| [**add_favorite_activities**](ActivityApi.md#add_favorite_activities)         | **POST** /1/user/-/activities/favorite/{activity-id}.json   | Add Favorite Activity        |
| [**add_update_activities_goals**](ActivityApi.md#add_update_activities_goals) | **POST** /1/user/-/activities/goals/{period}.json           | Update Activity Goals        |
| [**delete_activities_log**](ActivityApi.md#delete_activities_log)             | **DELETE** /1/user/-/activities/{activity-log-id}.json      | Delete Activity Log          |
| [**delete_favorite_activities**](ActivityApi.md#delete_favorite_activities)   | **DELETE** /1/user/-/activities/favorite/{activity-id}.json | Delete Favorite Activity     |
| [**get_activities_by_date**](ActivityApi.md#get_activities_by_date)           | **GET** /1/user/-/activities/date/{date}.json               | Get Activity Summary by Date |
| [**get_activities_goals**](ActivityApi.md#get_activities_goals)               | **GET** /1/user/-/activities/goals/{period}.json            | Get Activity Goals           |
| [**get_activities_log**](ActivityApi.md#get_activities_log)                   | **GET** /1/user/-/activities.json                           | Get Lifetime Stats           |
| [**get_activities_log_list**](ActivityApi.md#get_activities_log_list)         | **GET** /1/user/-/activities/list.json                      | Get Activity Log List        |
| [**get_activities_tcx**](ActivityApi.md#get_activities_tcx)                   | **GET** /1/user/-/activities/{log-id}.tcx                   | Get Activity TCX             |
| [**get_activities_type_detail**](ActivityApi.md#get_activities_type_detail)   | **GET** /1/activities/{activity-id}.json                    | Get Activity Type            |
| [**get_activities_types**](ActivityApi.md#get_activities_types)               | **GET** /1/activities.json                                  | Browse Activity Types        |
| [**get_favorite_activities**](ActivityApi.md#get_favorite_activities)         | **GET** /1/user/-/activities/favorite.json                  | Get Favorite Activities      |
| [**get_frequent_activities**](ActivityApi.md#get_frequent_activities)         | **GET** /1/user/-/activities/frequent.json                  | Get Frequent Activities      |
| [**get_recent_activities**](ActivityApi.md#get_recent_activities)             | **GET** /1/user/-/activities/recent.json                    | Get Recent Activity Types    |

# **add_activities_log**

> add_activities_log(activity_id, manual_calories, start_time, duration_millis, \_date, distance, activity_name=activity_name, distance_unit=distance_unit)

Log Activity

The Log Activity endpoint creates log entry for an activity or user's private custom activity using units in the unit system which corresponds to the Accept-Language header provided (or using optional custom distanceUnit) and get a response in the format requested.

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
api_instance = swagger_client.ActivityApi(swagger_client.ApiClient(configuration))
activity_id = 56 # int | The ID of the activity, directory activity or intensity level activity.
manual_calories = 56 # int | Calories burned that are manaully specified. Required with activityName must be provided.
start_time = 'start_time_example' # str | Activity start time. Hours and minutes in the format HH:mm:ss.
duration_millis = 56 # int | Duration in milliseconds.
_date = '2013-10-20' # date | Log entry date in the format yyyy-MM-dd.
distance = 56 # int | Distance is required for logging directory activity in the format X.XX and in the selected distanceUnit.
activity_name = 'activity_name_example' # str | Custom activity name. Either activityId or activityName must be provided. (optional)
distance_unit = 56 # int | Distance measurement unit. Steps units are available only for Walking (activityId=90013) and Running (activityId=90009) directory activities and their intensity levels. (optional)

try:
    # Log Activity
    api_instance.add_activities_log(activity_id, manual_calories, start_time, duration_millis, _date, distance, activity_name=activity_name, distance_unit=distance_unit)
except ApiException as e:
    print("Exception when calling ActivityApi->add_activities_log: %s\n" % e)
```

### Parameters

| Name                | Type     | Description                                                                                                                                                                        | Notes      |
| ------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **activity_id**     | **int**  | The ID of the activity, directory activity or intensity level activity.                                                                                                            |
| **manual_calories** | **int**  | Calories burned that are manaully specified. Required with activityName must be provided.                                                                                          |
| **start_time**      | **str**  | Activity start time. Hours and minutes in the format HH:mm:ss.                                                                                                                     |
| **duration_millis** | **int**  | Duration in milliseconds.                                                                                                                                                          |
| **\_date**          | **date** | Log entry date in the format yyyy-MM-dd.                                                                                                                                           |
| **distance**        | **int**  | Distance is required for logging directory activity in the format X.XX and in the selected distanceUnit.                                                                           |
| **activity_name**   | **str**  | Custom activity name. Either activityId or activityName must be provided.                                                                                                          | [optional] |
| **distance_unit**   | **int**  | Distance measurement unit. Steps units are available only for Walking (activityId&#x3D;90013) and Running (activityId&#x3D;90009) directory activities and their intensity levels. | [optional] |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_favorite_activities**

> add_favorite_activities(activity_id)

Add Favorite Activity

Adds the activity with the given ID to user's list of favorite activities.

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
api_instance = swagger_client.ActivityApi(swagger_client.ApiClient(configuration))
activity_id = 'activity_id_example' # str | The encoded ID of the activity.

try:
    # Add Favorite Activity
    api_instance.add_favorite_activities(activity_id)
except ApiException as e:
    print("Exception when calling ActivityApi->add_favorite_activities: %s\n" % e)
```

### Parameters

| Name            | Type    | Description                     | Notes |
| --------------- | ------- | ------------------------------- | ----- |
| **activity_id** | **str** | The encoded ID of the activity. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_update_activities_goals**

> add_update_activities_goals(period, type, value)

Update Activity Goals

Updates a user's daily or weekly activity goals and returns a response using units in the unit system which corresponds to the Accept-Language header provided.

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
api_instance = swagger_client.ActivityApi(swagger_client.ApiClient(configuration))
period = 'period_example' # str | daily or weekly.
type = 'type_example' # str | goal type
value = 'value_example' # str | goal value

try:
    # Update Activity Goals
    api_instance.add_update_activities_goals(period, type, value)
except ApiException as e:
    print("Exception when calling ActivityApi->add_update_activities_goals: %s\n" % e)
```

### Parameters

| Name       | Type    | Description      | Notes |
| ---------- | ------- | ---------------- | ----- |
| **period** | **str** | daily or weekly. |
| **type**   | **str** | goal type        |
| **value**  | **str** | goal value       |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_activities_log**

> delete_activities_log(activity_log_id)

Delete Activity Log

Deletes a user's activity log entry with the given ID.

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
api_instance = swagger_client.ActivityApi(swagger_client.ApiClient(configuration))
activity_log_id = 56 # int | The id of the activity log entry.

try:
    # Delete Activity Log
    api_instance.delete_activities_log(activity_log_id)
except ApiException as e:
    print("Exception when calling ActivityApi->delete_activities_log: %s\n" % e)
```

### Parameters

| Name                | Type    | Description                       | Notes |
| ------------------- | ------- | --------------------------------- | ----- |
| **activity_log_id** | **int** | The id of the activity log entry. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_favorite_activities**

> delete_favorite_activities(activity_id)

Delete Favorite Activity

Removes the activity with the given ID from a user's list of favorite activities.

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
api_instance = swagger_client.ActivityApi(swagger_client.ApiClient(configuration))
activity_id = 'activity_id_example' # str | The ID of the activity to be removed.

try:
    # Delete Favorite Activity
    api_instance.delete_favorite_activities(activity_id)
except ApiException as e:
    print("Exception when calling ActivityApi->delete_favorite_activities: %s\n" % e)
```

### Parameters

| Name            | Type    | Description                           | Notes |
| --------------- | ------- | ------------------------------------- | ----- |
| **activity_id** | **str** | The ID of the activity to be removed. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activities_by_date**

> get_activities_by_date(\_date)

Get Activity Summary by Date

Retrieves a summary and list of a user's activities and activity log entries for a given day.

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
api_instance = swagger_client.ActivityApi(swagger_client.ApiClient(configuration))
_date = '2013-10-20' # date | The date in the format yyyy-MM-dd

try:
    # Get Activity Summary by Date
    api_instance.get_activities_by_date(_date)
except ApiException as e:
    print("Exception when calling ActivityApi->get_activities_by_date: %s\n" % e)
```

### Parameters

| Name       | Type     | Description                       | Notes |
| ---------- | -------- | --------------------------------- | ----- |
| **\_date** | **date** | The date in the format yyyy-MM-dd |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activities_goals**

> get_activities_goals(period)

Get Activity Goals

Retreives a user's current daily or weekly activity goals using measurement units as defined in the unit system, which corresponds to the Accept-Language header provided.

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
api_instance = swagger_client.ActivityApi(swagger_client.ApiClient(configuration))
period = 'period_example' # str | daily or weekly.

try:
    # Get Activity Goals
    api_instance.get_activities_goals(period)
except ApiException as e:
    print("Exception when calling ActivityApi->get_activities_goals: %s\n" % e)
```

### Parameters

| Name       | Type    | Description      | Notes |
| ---------- | ------- | ---------------- | ----- |
| **period** | **str** | daily or weekly. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activities_log**

> get_activities_log()

Get Lifetime Stats

Updates a user's daily activity goals and returns a response using units in the unit system which corresponds to the Accept-Language header provided.

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
api_instance = swagger_client.ActivityApi(swagger_client.ApiClient(configuration))

try:
    # Get Lifetime Stats
    api_instance.get_activities_log()
except ApiException as e:
    print("Exception when calling ActivityApi->get_activities_log: %s\n" % e)
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

# **get_activities_log_list**

> get_activities_log_list(sort, offset, limit, before_date=before_date, after_date=after_date)

Get Activity Log List

Retreives a list of user's activity log entries before or after a given day with offset and limit using units in the unit system which corresponds to the Accept-Language header provided.

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
api_instance = swagger_client.ActivityApi(swagger_client.ApiClient(configuration))
sort = 'sort_example' # str | The sort order of entries by date asc (ascending) or desc (descending).
offset = 0 # int | The offset number of entries. (default to 0)
limit = 56 # int | The maximum number of entries returned (maximum;100).
before_date = '2013-10-20' # date | The date in the format yyyy-MM-ddTHH:mm:ss. Only yyyy-MM-dd is required. Either beforeDate or afterDate should be specified. (optional)
after_date = '2013-10-20' # date | The date in the format yyyy-MM-ddTHH:mm:ss. (optional)

try:
    # Get Activity Log List
    api_instance.get_activities_log_list(sort, offset, limit, before_date=before_date, after_date=after_date)
except ApiException as e:
    print("Exception when calling ActivityApi->get_activities_log_list: %s\n" % e)
```

### Parameters

| Name            | Type     | Description                                                                                                                  | Notes          |
| --------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------- | -------------- |
| **sort**        | **str**  | The sort order of entries by date asc (ascending) or desc (descending).                                                      |
| **offset**      | **int**  | The offset number of entries.                                                                                                | [default to 0] |
| **limit**       | **int**  | The maximum number of entries returned (maximum;100).                                                                        |
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

# **get_activities_tcx**

> get_activities_tcx(log_id, include_partial_tcx=include_partial_tcx)

Get Activity TCX

Retreives the details of a user's location and heart rate data during a logged exercise activity.

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
api_instance = swagger_client.ActivityApi(swagger_client.ApiClient(configuration))
log_id = 'log_id_example' # str | The activity's log ID.
include_partial_tcx = true # bool | Include TCX points regardless of GPS data being present (optional)

try:
    # Get Activity TCX
    api_instance.get_activities_tcx(log_id, include_partial_tcx=include_partial_tcx)
except ApiException as e:
    print("Exception when calling ActivityApi->get_activities_tcx: %s\n" % e)
```

### Parameters

| Name                    | Type     | Description                                             | Notes      |
| ----------------------- | -------- | ------------------------------------------------------- | ---------- |
| **log_id**              | **str**  | The activity&#x27;s log ID.                             |
| **include_partial_tcx** | **bool** | Include TCX points regardless of GPS data being present | [optional] |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activities_type_detail**

> get_activities_type_detail(activity_id)

Get Activity Type

Returns the detail of a specific activity in the Fitbit activities database in the format requested. If activity has levels, it also returns a list of activity level details.

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
api_instance = swagger_client.ActivityApi(swagger_client.ApiClient(configuration))
activity_id = 'activity_id_example' # str | The activity ID.

try:
    # Get Activity Type
    api_instance.get_activities_type_detail(activity_id)
except ApiException as e:
    print("Exception when calling ActivityApi->get_activities_type_detail: %s\n" % e)
```

### Parameters

| Name            | Type    | Description      | Notes |
| --------------- | ------- | ---------------- | ----- |
| **activity_id** | **str** | The activity ID. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activities_types**

> get_activities_types()

Browse Activity Types

Retreives a tree of all valid Fitbit public activities from the activities catelog as well as private custom activities the user created in the format requested.

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
api_instance = swagger_client.ActivityApi(swagger_client.ApiClient(configuration))

try:
    # Browse Activity Types
    api_instance.get_activities_types()
except ApiException as e:
    print("Exception when calling ActivityApi->get_activities_types: %s\n" % e)
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

# **get_favorite_activities**

> get_favorite_activities()

Get Favorite Activities

Returns a list of a user's favorite activities.

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
api_instance = swagger_client.ActivityApi(swagger_client.ApiClient(configuration))

try:
    # Get Favorite Activities
    api_instance.get_favorite_activities()
except ApiException as e:
    print("Exception when calling ActivityApi->get_favorite_activities: %s\n" % e)
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

# **get_frequent_activities**

> get_frequent_activities()

Get Frequent Activities

Retreives a list of a user's frequent activities in the format requested using units in the unit system which corresponds to the Accept-Language header provided.

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
api_instance = swagger_client.ActivityApi(swagger_client.ApiClient(configuration))

try:
    # Get Frequent Activities
    api_instance.get_frequent_activities()
except ApiException as e:
    print("Exception when calling ActivityApi->get_frequent_activities: %s\n" % e)
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

# **get_recent_activities**

> get_recent_activities()

Get Recent Activity Types

Retreives a list of a user's recent activities types logged with some details of the last activity log of that type using units in the unit system which corresponds to the Accept-Language header provided.

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
api_instance = swagger_client.ActivityApi(swagger_client.ApiClient(configuration))

try:
    # Get Recent Activity Types
    api_instance.get_recent_activities()
except ApiException as e:
    print("Exception when calling ActivityApi->get_recent_activities: %s\n" % e)
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
