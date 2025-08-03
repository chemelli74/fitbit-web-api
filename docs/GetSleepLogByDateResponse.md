# GetSleepLogByDateResponse

## Properties

| Name        | Type                                | Description                 | Notes      |
| ----------- | ----------------------------------- | --------------------------- | ---------- |
| **sleep**   | [**List[SleepLog]**](SleepLog.md)   | Array of sleep log entries. | [optional] |
| **summary** | [**SleepSummary**](SleepSummary.md) |                             | [optional] |
| **meta**    | [**SleepMeta**](SleepMeta.md)       |                             | [optional] |

## Example

```python
from fitbit_web_api.models.get_sleep_log_by_date_response import GetSleepLogByDateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSleepLogByDateResponse from a JSON string
get_sleep_log_by_date_response_instance = GetSleepLogByDateResponse.from_json(json)
# print the JSON string representation of the object
print(GetSleepLogByDateResponse.to_json())

# convert the object into a dict
get_sleep_log_by_date_response_dict = get_sleep_log_by_date_response_instance.to_dict()
# create an instance of GetSleepLogByDateResponse from a dict
get_sleep_log_by_date_response_from_dict = GetSleepLogByDateResponse.from_dict(get_sleep_log_by_date_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
