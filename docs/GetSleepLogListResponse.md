# GetSleepLogListResponse

## Properties

| Name           | Type                                                                          | Description                 | Notes      |
| -------------- | ----------------------------------------------------------------------------- | --------------------------- | ---------- |
| **pagination** | [**GetSleepLogListResponsePagination**](GetSleepLogListResponsePagination.md) |                             | [optional] |
| **sleep**      | [**List[SleepLog]**](SleepLog.md)                                             | Array of sleep log entries. | [optional] |
| **summary**    | [**SleepSummary**](SleepSummary.md)                                           |                             | [optional] |

## Example

```python
from fitbit_web_api.models.get_sleep_log_list_response import GetSleepLogListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSleepLogListResponse from a JSON string
get_sleep_log_list_response_instance = GetSleepLogListResponse.from_json(json)
# print the JSON string representation of the object
print(GetSleepLogListResponse.to_json())

# convert the object into a dict
get_sleep_log_list_response_dict = get_sleep_log_list_response_instance.to_dict()
# create an instance of GetSleepLogListResponse from a dict
get_sleep_log_list_response_from_dict = GetSleepLogListResponse.from_dict(get_sleep_log_list_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
