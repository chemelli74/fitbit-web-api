# SleepLogLevelsDataInner

## Properties

| Name          | Type         | Description                                                    | Notes      |
| ------------- | ------------ | -------------------------------------------------------------- | ---------- |
| **date_time** | **datetime** | Timestamp the user started in sleep level.                     | [optional] |
| **level**     | **str**      | The sleep level the user entered.                              | [optional] |
| **seconds**   | **int**      | The length of time the user was in the sleep level in seconds. | [optional] |

## Example

```python
from fitbit_web_api.models.sleep_log_levels_data_inner import SleepLogLevelsDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of SleepLogLevelsDataInner from a JSON string
sleep_log_levels_data_inner_instance = SleepLogLevelsDataInner.from_json(json)
# print the JSON string representation of the object
print(SleepLogLevelsDataInner.to_json())

# convert the object into a dict
sleep_log_levels_data_inner_dict = sleep_log_levels_data_inner_instance.to_dict()
# create an instance of SleepLogLevelsDataInner from a dict
sleep_log_levels_data_inner_from_dict = SleepLogLevelsDataInner.from_dict(sleep_log_levels_data_inner_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
