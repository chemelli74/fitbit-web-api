# fitbit_web_api.UserApi

All URIs are relative to *https://api.fitbit.com/*

| Method                                          | HTTP request                    | Description    |
| ----------------------------------------------- | ------------------------------- | -------------- |
| [**get_badges**](UserApi.md#get_badges)         | **GET** /1/user/-/badges.json   | Get Badges     |
| [**get_profile**](UserApi.md#get_profile)       | **GET** /1/user/-/profile.json  | Get Profile    |
| [**update_profile**](UserApi.md#update_profile) | **POST** /1/user/-/profile.json | Update Profile |

# **get_badges**

> get_badges()

Get Badges

Retrieves the user's badges in the format requested. Response includes all badges for the user as seen on the Fitbit website badge locker (both activity and weight related.) The endpoint returns weight and distance badges based on the user's unit profile preference as on the website.

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
api_instance = fitbit_web_api.UserApi(fitbit_web_api.ApiClient(configuration))

try:
    # Get Badges
    api_instance.get_badges()
except ApiException as e:
    print("Exception when calling UserApi->get_badges: %s\n" % e)
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

# **get_profile**

> get_profile()

Get Profile

Returns a user's profile. The authenticated owner receives all values. However, the authenticated user's access to other users' data is subject to those users' privacy settings. Numerical values are returned in the unit system specified in the Accept-Language header.

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
api_instance = fitbit_web_api.UserApi(fitbit_web_api.ApiClient(configuration))

try:
    # Get Profile
    api_instance.get_profile()
except ApiException as e:
    print("Exception when calling UserApi->get_profile: %s\n" % e)
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

# **update_profile**

> update_profile(gender=gender, birthday=birthday, height=height, about_me=about_me, fullname=fullname, country=country, state=state, city=city, stride_length_walking=stride_length_walking, stride_length_running=stride_length_running, weight_unit=weight_unit, height_unit=height_unit, water_unit=water_unit, glucose_unit=glucose_unit, timezone=timezone, foods_locale=foods_locale, locale=locale, locale_lang=locale_lang, locale_country=locale_country, start_day_of_week=start_day_of_week)

Update Profile

Updates a user's profile using a form.

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
api_instance = fitbit_web_api.UserApi(fitbit_web_api.ApiClient(configuration))
gender = 'gender_example' # str |  (optional)
birthday = '2013-10-20' # date |  (optional)
height = 'height_example' # str |  (optional)
about_me = 'about_me_example' # str |  (optional)
fullname = 'fullname_example' # str |  (optional)
country = 'country_example' # str |  (optional)
state = 'state_example' # str |  (optional)
city = 'city_example' # str |  (optional)
stride_length_walking = 'stride_length_walking_example' # str |  (optional)
stride_length_running = 'stride_length_running_example' # str |  (optional)
weight_unit = 'weight_unit_example' # str |  (optional)
height_unit = 'height_unit_example' # str |  (optional)
water_unit = 'water_unit_example' # str |  (optional)
glucose_unit = 'glucose_unit_example' # str |  (optional)
timezone = 'timezone_example' # str |  (optional)
foods_locale = 'foods_locale_example' # str |  (optional)
locale = 'locale_example' # str |  (optional)
locale_lang = 'locale_lang_example' # str |  (optional)
locale_country = 'locale_country_example' # str |  (optional)
start_day_of_week = 'start_day_of_week_example' # str |  (optional)

try:
    # Update Profile
    api_instance.update_profile(gender=gender, birthday=birthday, height=height, about_me=about_me, fullname=fullname, country=country, state=state, city=city, stride_length_walking=stride_length_walking, stride_length_running=stride_length_running, weight_unit=weight_unit, height_unit=height_unit, water_unit=water_unit, glucose_unit=glucose_unit, timezone=timezone, foods_locale=foods_locale, locale=locale, locale_lang=locale_lang, locale_country=locale_country, start_day_of_week=start_day_of_week)
except ApiException as e:
    print("Exception when calling UserApi->update_profile: %s\n" % e)
```

### Parameters

| Name                      | Type     | Description | Notes      |
| ------------------------- | -------- | ----------- | ---------- |
| **gender**                | **str**  |             | [optional] |
| **birthday**              | **date** |             | [optional] |
| **height**                | **str**  |             | [optional] |
| **about_me**              | **str**  |             | [optional] |
| **fullname**              | **str**  |             | [optional] |
| **country**               | **str**  |             | [optional] |
| **state**                 | **str**  |             | [optional] |
| **city**                  | **str**  |             | [optional] |
| **stride_length_walking** | **str**  |             | [optional] |
| **stride_length_running** | **str**  |             | [optional] |
| **weight_unit**           | **str**  |             | [optional] |
| **height_unit**           | **str**  |             | [optional] |
| **water_unit**            | **str**  |             | [optional] |
| **glucose_unit**          | **str**  |             | [optional] |
| **timezone**              | **str**  |             | [optional] |
| **foods_locale**          | **str**  |             | [optional] |
| **locale**                | **str**  |             | [optional] |
| **locale_lang**           | **str**  |             | [optional] |
| **locale_country**        | **str**  |             | [optional] |
| **start_day_of_week**     | **str**  |             | [optional] |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
