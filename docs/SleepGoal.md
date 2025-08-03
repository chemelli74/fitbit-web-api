# SleepGoal

## Properties

| Name             | Type         | Description                                      | Notes      |
| ---------------- | ------------ | ------------------------------------------------ | ---------- |
| **updated_on**   | **datetime** | The timestamp that the goal was created/updated. | [optional] |
| **min_duration** | **int**      | Length of the sleep goal period in minutes.      | [optional] |
| **bedtime**      | **str**      | The user&#39;s targeted bedtime.                 | [optional] |
| **wakeup_time**  | **str**      | The user&#39;s targeted wake time.               | [optional] |

## Example

```python
from fitbit_web_api.models.sleep_goal import SleepGoal

# TODO update the JSON string below
json = "{}"
# create an instance of SleepGoal from a JSON string
sleep_goal_instance = SleepGoal.from_json(json)
# print the JSON string representation of the object
print(SleepGoal.to_json())

# convert the object into a dict
sleep_goal_dict = sleep_goal_instance.to_dict()
# create an instance of SleepGoal from a dict
sleep_goal_from_dict = SleepGoal.from_dict(sleep_goal_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
