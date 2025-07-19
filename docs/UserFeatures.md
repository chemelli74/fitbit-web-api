# UserFeatures

## Properties

| Name              | Type     | Description | Notes      |
| ----------------- | -------- | ----------- | ---------- |
| **exercise_goal** | **bool** |             | [optional] |

## Example

```python
from fitbit_web_api.models.user_features import UserFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of UserFeatures from a JSON string
user_features_instance = UserFeatures.from_json(json)
# print the JSON string representation of the object
print(UserFeatures.to_json())

# convert the object into a dict
user_features_dict = user_features_instance.to_dict()
# create an instance of UserFeatures from a dict
user_features_from_dict = UserFeatures.from_dict(user_features_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
