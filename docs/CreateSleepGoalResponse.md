# CreateSleepGoalResponse

## Properties

| Name     | Type                          | Description | Notes      |
| -------- | ----------------------------- | ----------- | ---------- |
| **goal** | [**SleepGoal**](SleepGoal.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.create_sleep_goal_response import CreateSleepGoalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSleepGoalResponse from a JSON string
create_sleep_goal_response_instance = CreateSleepGoalResponse.from_json(json)
# print the JSON string representation of the object
print(CreateSleepGoalResponse.to_json())

# convert the object into a dict
create_sleep_goal_response_dict = create_sleep_goal_response_instance.to_dict()
# create an instance of CreateSleepGoalResponse from a dict
create_sleep_goal_response_from_dict = CreateSleepGoalResponse.from_dict(create_sleep_goal_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
