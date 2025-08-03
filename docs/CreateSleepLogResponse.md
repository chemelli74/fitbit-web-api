# CreateSleepLogResponse

## Properties

| Name      | Type                              | Description                 | Notes      |
| --------- | --------------------------------- | --------------------------- | ---------- |
| **sleep** | [**List[SleepLog]**](SleepLog.md) | Array of sleep log entries. | [optional] |

## Example

```python
from fitbit_web_api.models.create_sleep_log_response import CreateSleepLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSleepLogResponse from a JSON string
create_sleep_log_response_instance = CreateSleepLogResponse.from_json(json)
# print the JSON string representation of the object
print(CreateSleepLogResponse.to_json())

# convert the object into a dict
create_sleep_log_response_dict = create_sleep_log_response_instance.to_dict()
# create an instance of CreateSleepLogResponse from a dict
create_sleep_log_response_from_dict = CreateSleepLogResponse.from_dict(create_sleep_log_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
