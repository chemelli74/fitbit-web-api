# Badge

## Properties

| Name                           | Type             | Description | Notes      |
| ------------------------------ | ---------------- | ----------- | ---------- |
| **badge_gradient_end_color**   | **str**          |             | [optional] |
| **badge_gradient_start_color** | **str**          |             | [optional] |
| **badge_type**                 | **str**          |             | [optional] |
| **category**                   | **str**          |             | [optional] |
| **cheers**                     | **List[object]** |             | [optional] |
| **date_time**                  | **datetime**     |             | [optional] |
| **description**                | **str**          |             | [optional] |
| **earned_message**             | **str**          |             | [optional] |
| **encoded_id**                 | **str**          |             | [optional] |
| **image100px**                 | **str**          |             | [optional] |
| **image125px**                 | **str**          |             | [optional] |
| **image300px**                 | **str**          |             | [optional] |
| **image50px**                  | **str**          |             | [optional] |
| **image75px**                  | **str**          |             | [optional] |
| **marketing_description**      | **str**          |             | [optional] |
| **mobile_description**         | **str**          |             | [optional] |
| **name**                       | **str**          |             | [optional] |
| **share_image640px**           | **str**          |             | [optional] |
| **share_text**                 | **str**          |             | [optional] |
| **short_description**          | **str**          |             | [optional] |
| **short_name**                 | **str**          |             | [optional] |
| **times_achieved**             | **int**          |             | [optional] |
| **value**                      | **int**          |             | [optional] |
| **unit**                       | **str**          |             | [optional] |

## Example

```python
from fitbit_web_api.models.badge import Badge

# TODO update the JSON string below
json = "{}"
# create an instance of Badge from a JSON string
badge_instance = Badge.from_json(json)
# print the JSON string representation of the object
print(Badge.to_json())

# convert the object into a dict
badge_dict = badge_instance.to_dict()
# create an instance of Badge from a dict
badge_from_dict = Badge.from_dict(badge_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
