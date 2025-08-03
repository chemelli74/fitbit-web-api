# SleepLogLevelsSummaryValue

## Properties

| Name                       | Type    | Description                                                   | Notes      |
| -------------------------- | ------- | ------------------------------------------------------------- | ---------- |
| **count**                  | **int** | Total number of times the user entered the sleep level.       | [optional] |
| **minutes**                | **int** | Total number of minutes the user appeared in the sleep level. | [optional] |
| **thirty_day_avg_minutes** | **int** | The average sleep stage time over the past 30 days.           | [optional] |

## Example

```python
from fitbit_web_api.models.sleep_log_levels_summary_value import SleepLogLevelsSummaryValue

# TODO update the JSON string below
json = "{}"
# create an instance of SleepLogLevelsSummaryValue from a JSON string
sleep_log_levels_summary_value_instance = SleepLogLevelsSummaryValue.from_json(json)
# print the JSON string representation of the object
print(SleepLogLevelsSummaryValue.to_json())

# convert the object into a dict
sleep_log_levels_summary_value_dict = sleep_log_levels_summary_value_instance.to_dict()
# create an instance of SleepLogLevelsSummaryValue from a dict
sleep_log_levels_summary_value_from_dict = SleepLogLevelsSummaryValue.from_dict(sleep_log_levels_summary_value_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
