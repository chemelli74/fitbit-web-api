# SleepMeta

## Properties

| Name               | Type    | Description                            | Notes      |
| ------------------ | ------- | -------------------------------------- | ---------- |
| **retry_duration** | **int** | The retry duration in milliseconds.    | [optional] |
| **state**          | **str** | The processing state of the sleep log. | [optional] |

## Example

```python
from fitbit_web_api.models.sleep_meta import SleepMeta

# TODO update the JSON string below
json = "{}"
# create an instance of SleepMeta from a JSON string
sleep_meta_instance = SleepMeta.from_json(json)
# print the JSON string representation of the object
print(SleepMeta.to_json())

# convert the object into a dict
sleep_meta_dict = sleep_meta_instance.to_dict()
# create an instance of SleepMeta from a dict
sleep_meta_from_dict = SleepMeta.from_dict(sleep_meta_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
