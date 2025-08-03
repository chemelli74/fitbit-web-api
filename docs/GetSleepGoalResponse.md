# GetSleepGoalResponse

## Properties

| Name     | Type                          | Description | Notes      |
| -------- | ----------------------------- | ----------- | ---------- |
| **goal** | [**SleepGoal**](SleepGoal.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_sleep_goal_response import GetSleepGoalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSleepGoalResponse from a JSON string
get_sleep_goal_response_instance = GetSleepGoalResponse.from_json(json)
# print the JSON string representation of the object
print(GetSleepGoalResponse.to_json())

# convert the object into a dict
get_sleep_goal_response_dict = get_sleep_goal_response_instance.to_dict()
# create an instance of GetSleepGoalResponse from a dict
get_sleep_goal_response_from_dict = GetSleepGoalResponse.from_dict(get_sleep_goal_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
