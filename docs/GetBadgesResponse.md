# GetBadgesResponse

## Properties

| Name       | Type                        | Description | Notes      |
| ---------- | --------------------------- | ----------- | ---------- |
| **badges** | [**List[Badge]**](Badge.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_badges_response import GetBadgesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBadgesResponse from a JSON string
get_badges_response_instance = GetBadgesResponse.from_json(json)
# print the JSON string representation of the object
print(GetBadgesResponse.to_json())

# convert the object into a dict
get_badges_response_dict = get_badges_response_instance.to_dict()
# create an instance of GetBadgesResponse from a dict
get_badges_response_from_dict = GetBadgesResponse.from_dict(get_badges_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
