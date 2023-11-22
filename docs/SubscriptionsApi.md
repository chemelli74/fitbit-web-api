# fitbit_web_api.SubscriptionsApi

All URIs are relative to *https://api.fitbit.com/*

| Method                                                                   | HTTP request                                                                   | Description                 |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | --------------------------- |
| [**add_subscriptions**](SubscriptionsApi.md#add_subscriptions)           | **POST** /1/user/-/{collection-path}/apiSubscriptions/{subscription-id}.json   | Add a Subscription          |
| [**delete_subscriptions**](SubscriptionsApi.md#delete_subscriptions)     | **DELETE** /1/user/-/{collection-path}/apiSubscriptions/{subscription-id}.json | Delete a Subscription       |
| [**get_subscriptions_list**](SubscriptionsApi.md#get_subscriptions_list) | **GET** /1/user/-/{collection-path}/apiSubscriptions.json                      | Get a List of Subscriptions |

# **add_subscriptions**

> add_subscriptions(collection_path, subscription_id)

Add a Subscription

Adds a subscription in your application so that users can get notifications and return a response in the format requested. The subscription-id value provides a way to associate an update with a particular user stream in your application.

### Example

```python
from __future__ import print_function
import time
import fitbit_web_api
from fitbit_web_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = fitbit_web_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = fitbit_web_api.SubscriptionsApi(fitbit_web_api.ApiClient(configuration))
collection_path = 'collection_path_example' # str | This is the resource of the collection to receive notifications from (foods, activities, sleep, or body). If not present, subscription will be created for all collections. If you have both all and specific collection subscriptions, you will get duplicate notifications on that collections' updates. Each subscriber can have only one subscription for a specific user's collection.
subscription_id = 'subscription_id_example' # str | This is the unique ID of the subscription created by the API client application. Each ID must be unique across the entire set of subscribers and collections. The Fitbit servers will pass this ID back along with any notifications about the user indicated by the user parameter in the URL path.

try:
    # Add a Subscription
    api_instance.add_subscriptions(collection_path, subscription_id)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->add_subscriptions: %s\n" % e)
```

### Parameters

| Name                | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                           | Notes |
| ------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| **collection_path** | **str** | This is the resource of the collection to receive notifications from (foods, activities, sleep, or body). If not present, subscription will be created for all collections. If you have both all and specific collection subscriptions, you will get duplicate notifications on that collections&#x27; updates. Each subscriber can have only one subscription for a specific user&#x27;s collection. |
| **subscription_id** | **str** | This is the unique ID of the subscription created by the API client application. Each ID must be unique across the entire set of subscribers and collections. The Fitbit servers will pass this ID back along with any notifications about the user indicated by the user parameter in the URL path.                                                                                                  |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscriptions**

> delete_subscriptions(collection_path, subscription_id)

Delete a Subscription

Deletes a subscription for a user..

### Example

```python
from __future__ import print_function
import time
import fitbit_web_api
from fitbit_web_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = fitbit_web_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = fitbit_web_api.SubscriptionsApi(fitbit_web_api.ApiClient(configuration))
collection_path = 'collection_path_example' # str | This is the resource of the collection to receive notifications from (foods, activities, sleep, or body). If not present, subscription will be created for all collections. If you have both all and specific collection subscriptions, you will get duplicate notifications on that collections' updates. Each subscriber can have only one subscription for a specific user's collection.
subscription_id = 'subscription_id_example' # str | This is the resource of the collection to receive notifications from (foods, activities, sleep, or body). If not present, subscription will be created for all collections. If you have both all and specific collection subscriptions, you will get duplicate notifications on that collections' updates. Each subscriber can have only one subscription for a specific user's collection.

try:
    # Delete a Subscription
    api_instance.delete_subscriptions(collection_path, subscription_id)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->delete_subscriptions: %s\n" % e)
```

### Parameters

| Name                | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                           | Notes |
| ------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| **collection_path** | **str** | This is the resource of the collection to receive notifications from (foods, activities, sleep, or body). If not present, subscription will be created for all collections. If you have both all and specific collection subscriptions, you will get duplicate notifications on that collections&#x27; updates. Each subscriber can have only one subscription for a specific user&#x27;s collection. |
| **subscription_id** | **str** | This is the resource of the collection to receive notifications from (foods, activities, sleep, or body). If not present, subscription will be created for all collections. If you have both all and specific collection subscriptions, you will get duplicate notifications on that collections&#x27; updates. Each subscriber can have only one subscription for a specific user&#x27;s collection. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriptions_list**

> get_subscriptions_list(collection_path)

Get a List of Subscriptions

Retreives a list of a user's subscriptions for your application in the format requested. You can either fetch subscriptions for a specific collection or the entire list of subscriptions for the user. For best practice, make sure that your application maintains this list on your side and use this endpoint only to periodically ensure data consistency.

### Example

```python
from __future__ import print_function
import time
import fitbit_web_api
from fitbit_web_api.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = fitbit_web_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = fitbit_web_api.SubscriptionsApi(fitbit_web_api.ApiClient(configuration))
collection_path = 'collection_path_example' # str | This is the resource of the collection to receive notifications from (foods, activities, sleep, or body). If not present, subscription will be created for all collections. If you have both all and specific collection subscriptions, you will get duplicate notifications on that collections' updates. Each subscriber can have only one subscription for a specific user's collection.

try:
    # Get a List of Subscriptions
    api_instance.get_subscriptions_list(collection_path)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_subscriptions_list: %s\n" % e)
```

### Parameters

| Name                | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                           | Notes |
| ------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| **collection_path** | **str** | This is the resource of the collection to receive notifications from (foods, activities, sleep, or body). If not present, subscription will be created for all collections. If you have both all and specific collection subscriptions, you will get duplicate notifications on that collections&#x27; updates. Each subscriber can have only one subscription for a specific user&#x27;s collection. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
