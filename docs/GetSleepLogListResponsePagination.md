# GetSleepLogListResponsePagination

## Properties

| Name            | Type     | Description                           | Notes      |
| --------------- | -------- | ------------------------------------- | ---------- |
| **after_date**  | **date** | The specified afterDate parameter.    | [optional] |
| **before_date** | **date** | The specified beforeDate parameter.   | [optional] |
| **limit**       | **int**  | The specified limit.                  | [optional] |
| **next**        | **str**  | URL for the next page of results.     | [optional] |
| **offset**      | **int**  | The specified offset.                 | [optional] |
| **previous**    | **str**  | URL for the previous page of results. | [optional] |
| **sort**        | **str**  | The specified sort order.             | [optional] |

## Example

```python
from fitbit_web_api.models.get_sleep_log_list_response_pagination import GetSleepLogListResponsePagination

# TODO update the JSON string below
json = "{}"
# create an instance of GetSleepLogListResponsePagination from a JSON string
get_sleep_log_list_response_pagination_instance = GetSleepLogListResponsePagination.from_json(json)
# print the JSON string representation of the object
print(GetSleepLogListResponsePagination.to_json())

# convert the object into a dict
get_sleep_log_list_response_pagination_dict = get_sleep_log_list_response_pagination_instance.to_dict()
# create an instance of GetSleepLogListResponsePagination from a dict
get_sleep_log_list_response_pagination_from_dict = GetSleepLogListResponsePagination.from_dict(get_sleep_log_list_response_pagination_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
