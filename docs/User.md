# User

## Properties

| Name                            | Type                                | Description | Notes      |
| ------------------------------- | ----------------------------------- | ----------- | ---------- |
| **age**                         | **int**                             |             | [optional] |
| **ambassador**                  | **bool**                            |             | [optional] |
| **auto_stride_enabled**         | **bool**                            |             | [optional] |
| **avatar**                      | **str**                             |             | [optional] |
| **avatar150**                   | **str**                             |             | [optional] |
| **avatar640**                   | **str**                             |             | [optional] |
| **average_daily_steps**         | **int**                             |             | [optional] |
| **challenges_beta**             | **bool**                            |             | [optional] |
| **clock_time_display_format**   | **str**                             |             | [optional] |
| **corporate**                   | **bool**                            |             | [optional] |
| **corporate_admin**             | **bool**                            |             | [optional] |
| **country**                     | **str**                             |             | [optional] |
| **date_of_birth**               | **date**                            |             | [optional] |
| **display_name**                | **str**                             |             | [optional] |
| **display_name_setting**        | **str**                             |             | [optional] |
| **distance_unit**               | **str**                             |             | [optional] |
| **encoded_id**                  | **str**                             |             | [optional] |
| **features**                    | [**UserFeatures**](UserFeatures.md) |             | [optional] |
| **first_name**                  | **str**                             |             | [optional] |
| **foods_locale**                | **str**                             |             | [optional] |
| **full_name**                   | **str**                             |             | [optional] |
| **gender**                      | **str**                             |             | [optional] |
| **glucose_unit**                | **str**                             |             | [optional] |
| **height**                      | **float**                           |             | [optional] |
| **height_unit**                 | **str**                             |             | [optional] |
| **is_bug_report_enabled**       | **bool**                            |             | [optional] |
| **is_child**                    | **bool**                            |             | [optional] |
| **is_coach**                    | **bool**                            |             | [optional] |
| **language_locale**             | **str**                             |             | [optional] |
| **last_name**                   | **str**                             |             | [optional] |
| **legal_terms_accept_required** | **bool**                            |             | [optional] |
| **locale**                      | **str**                             |             | [optional] |
| **member_since**                | **date**                            |             | [optional] |
| **mfa_enabled**                 | **bool**                            |             | [optional] |
| **offset_from_utc_millis**      | **int**                             |             | [optional] |
| **sdk_developer**               | **bool**                            |             | [optional] |
| **sleep_tracking**              | **str**                             |             | [optional] |
| **start_day_of_week**           | **str**                             |             | [optional] |
| **stride_length_running**       | **float**                           |             | [optional] |
| **stride_length_running_type**  | **str**                             |             | [optional] |
| **stride_length_walking**       | **float**                           |             | [optional] |
| **stride_length_walking_type**  | **str**                             |             | [optional] |
| **swim_unit**                   | **str**                             |             | [optional] |
| **timezone**                    | **str**                             |             | [optional] |
| **top_badges**                  | [**List[Badge]**](Badge.md)         |             | [optional] |
| **water_unit**                  | **str**                             |             | [optional] |
| **water_unit_name**             | **str**                             |             | [optional] |
| **weight**                      | **float**                           |             | [optional] |
| **weight_unit**                 | **str**                             |             | [optional] |

## Example

```python
from fitbit_web_api.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
