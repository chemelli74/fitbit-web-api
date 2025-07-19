# GetProfileResponse

## Properties

| Name     | Type                | Description | Notes      |
| -------- | ------------------- | ----------- | ---------- |
| **user** | [**User**](User.md) |             | [optional] |

## Example

```python
from fitbit_web_api.models.get_profile_response import GetProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetProfileResponse from a JSON string
get_profile_response_instance = GetProfileResponse.from_json(json)
# print the JSON string representation of the object
print(GetProfileResponse.to_json())

# convert the object into a dict
get_profile_response_dict = get_profile_response_instance.to_dict()
# create an instance of GetProfileResponse from a dict
get_profile_response_from_dict = GetProfileResponse.from_dict(get_profile_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
