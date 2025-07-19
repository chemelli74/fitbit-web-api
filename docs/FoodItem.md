# FoodItem

## Properties

| Name        | Type    | Description | Notes      |
| ----------- | ------- | ----------- | ---------- |
| **food_id** | **int** |             | [optional] |
| **amount**  | **int** |             | [optional] |
| **unit_id** | **int** |             | [optional] |

## Example

```python
from fitbit_web_api.models.food_item import FoodItem

# TODO update the JSON string below
json = "{}"
# create an instance of FoodItem from a JSON string
food_item_instance = FoodItem.from_json(json)
# print the JSON string representation of the object
print(FoodItem.to_json())

# convert the object into a dict
food_item_dict = food_item_instance.to_dict()
# create an instance of FoodItem from a dict
food_item_from_dict = FoodItem.from_dict(food_item_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
