# SleepLog

## Properties

| Name                       | Type                                    | Description                                                                                                                                                                                                     | Notes      |
| -------------------------- | --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **date_of_sleep**          | **date**                                | The date the sleep log ended.                                                                                                                                                                                   | [optional] |
| **duration**               | **int**                                 | Length of the sleep in milliseconds.                                                                                                                                                                            | [optional] |
| **efficiency**             | **float**                               | Calculated sleep efficiency score.                                                                                                                                                                              | [optional] |
| **end_time**               | **str**                                 | Time the sleep log ended.                                                                                                                                                                                       | [optional] |
| **info_code**              | **int**                                 | An integer value representing the quality of data collected within the sleep log. 0 &#x3D; Sufficient data, 1 &#x3D; Insufficient heart rate data, 2 &#x3D; Sleep period too short, 3 &#x3D; Server-side issue. | [optional] |
| **is_main_sleep**          | **bool**                                | Boolean value indicating if this is the main sleep period.                                                                                                                                                      | [optional] |
| **levels**                 | [**SleepLogLevels**](SleepLogLevels.md) |                                                                                                                                                                                                                 | [optional] |
| **log_id**                 | **int**                                 | Sleep log ID.                                                                                                                                                                                                   | [optional] |
| **minutes_after_wakeup**   | **int**                                 | The total number of minutes after the user woke up.                                                                                                                                                             | [optional] |
| **minutes_asleep**         | **int**                                 | The total number of minutes the user was asleep.                                                                                                                                                                | [optional] |
| **minutes_awake**          | **int**                                 | The total sum of wake minutes only.                                                                                                                                                                             | [optional] |
| **minutes_to_fall_asleep** | **int**                                 | The total number of minutes before the user falls asleep.                                                                                                                                                       | [optional] |
| **log_type**               | **str**                                 | The type of sleep in terms of how it was logged.                                                                                                                                                                | [optional] |
| **start_time**             | **str**                                 | Time the sleep log begins.                                                                                                                                                                                      | [optional] |
| **time_in_bed**            | **int**                                 | Total number of minutes the user was in bed.                                                                                                                                                                    | [optional] |
| **type**                   | **str**                                 | The type of sleep log.                                                                                                                                                                                          | [optional] |

## Example

```python
from fitbit_web_api.models.sleep_log import SleepLog

# TODO update the JSON string below
json = "{}"
# create an instance of SleepLog from a JSON string
sleep_log_instance = SleepLog.from_json(json)
# print the JSON string representation of the object
print(SleepLog.to_json())

# convert the object into a dict
sleep_log_dict = sleep_log_instance.to_dict()
# create an instance of SleepLog from a dict
sleep_log_from_dict = SleepLog.from_dict(sleep_log_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
