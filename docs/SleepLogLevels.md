# SleepLogLevels

## Properties

| Name           | Type                                                                       | Description                                                   | Notes      |
| -------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------- | ---------- |
| **data**       | [**List[SleepLogLevelsDataInner]**](SleepLogLevelsDataInner.md)            |                                                               | [optional] |
| **short_data** | [**List[SleepLogLevelsDataInner]**](SleepLogLevelsDataInner.md)            | Short data periods (3 minutes or less) for stages sleep logs. | [optional] |
| **summary**    | [**Dict[str, SleepLogLevelsSummaryValue]**](SleepLogLevelsSummaryValue.md) |                                                               | [optional] |

## Example

```python
from fitbit_web_api.models.sleep_log_levels import SleepLogLevels

# TODO update the JSON string below
json = "{}"
# create an instance of SleepLogLevels from a JSON string
sleep_log_levels_instance = SleepLogLevels.from_json(json)
# print the JSON string representation of the object
print(SleepLogLevels.to_json())

# convert the object into a dict
sleep_log_levels_dict = sleep_log_levels_instance.to_dict()
# create an instance of SleepLogLevels from a dict
sleep_log_levels_from_dict = SleepLogLevels.from_dict(sleep_log_levels_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
