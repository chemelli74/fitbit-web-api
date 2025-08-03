# SleepSummary

## Properties

| Name                     | Type               | Description                                                           | Notes      |
| ------------------------ | ------------------ | --------------------------------------------------------------------- | ---------- |
| **stages**               | **Dict[str, int]** | Summary of sleep stages with minutes for each stage.                  | [optional] |
| **total_minutes_asleep** | **int**            | Total number of minutes the user was asleep across all sleep records. | [optional] |
| **total_sleep_records**  | **int**            | The number of sleep records within the sleep log.                     | [optional] |
| **total_time_in_bed**    | **int**            | Total number of minutes the user was in bed across all records.       | [optional] |

## Example

```python
from fitbit_web_api.models.sleep_summary import SleepSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SleepSummary from a JSON string
sleep_summary_instance = SleepSummary.from_json(json)
# print the JSON string representation of the object
print(SleepSummary.to_json())

# convert the object into a dict
sleep_summary_dict = sleep_summary_instance.to_dict()
# create an instance of SleepSummary from a dict
sleep_summary_from_dict = SleepSummary.from_dict(sleep_summary_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
