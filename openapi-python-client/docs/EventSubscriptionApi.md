# openapi_client.EventSubscriptionApi

All URIs are relative to *http://localhost:8080/engine-rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event_subscriptions**](EventSubscriptionApi.md#get_event_subscriptions) | **GET** /event-subscription | 
[**get_event_subscriptions_count**](EventSubscriptionApi.md#get_event_subscriptions_count) | **GET** /event-subscription/count | 


# **get_event_subscriptions**
> list[EventSubscriptionDto] get_event_subscriptions(event_subscription_id=event_subscription_id, event_name=event_name, event_type=event_type, execution_id=execution_id, process_instance_id=process_instance_id, activity_id=activity_id, tenant_id_in=tenant_id_in, without_tenant_id=without_tenant_id, include_event_subscriptions_without_tenant_id=include_event_subscriptions_without_tenant_id, sort_by=sort_by, sort_order=sort_order, first_result=first_result, max_results=max_results)



Queries for event subscriptions that fulfill given parameters. The size of the result set can be retrieved by using the [Get Event Subscriptions count](https://docs.camunda.org/manual/7.13/reference/rest/event-subscription/get-query-count/) method.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/engine-rest
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080/engine-rest"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EventSubscriptionApi(api_client)
    event_subscription_id = 'event_subscription_id_example' # str | Only select subscription with the given id. (optional)
event_name = 'event_name_example' # str | Only select subscriptions for events with the given name. (optional)
event_type = 'event_type_example' # str | Only select subscriptions for events with the given type. Valid values: `message`, `signal`, `compensate` and `conditional`. (optional)
execution_id = 'execution_id_example' # str | Only select subscriptions that belong to an execution with the given id. (optional)
process_instance_id = 'process_instance_id_example' # str | Only select subscriptions that belong to a process instance with the given id. (optional)
activity_id = 'activity_id_example' # str | Only select subscriptions that belong to an activity with the given id. (optional)
tenant_id_in = 'tenant_id_in_example' # str | Filter by a comma-separated list of tenant ids. Only select subscriptions that belong to one of the given tenant ids. (optional)
without_tenant_id = True # bool | Only select subscriptions which have no tenant id. Value may only be `true`, as `false` is the default behavior. (optional)
include_event_subscriptions_without_tenant_id = True # bool | Select event subscriptions which have no tenant id. Can be used in combination with tenantIdIn parameter. Value may only be `true`, as `false` is the default behavior. (optional)
sort_by = 'sort_by_example' # str | Sort the results lexicographically by a given criterion. Must be used in conjunction with the sortOrder parameter. (optional)
sort_order = 'sort_order_example' # str | Sort the results in a given order. Values may be asc for ascending order or desc for descending order. Must be used in conjunction with the sortBy parameter. (optional)
first_result = 56 # int | Pagination of results. Specifies the index of the first result to return. (optional)
max_results = 56 # int | Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. (optional)

    try:
        api_response = api_instance.get_event_subscriptions(event_subscription_id=event_subscription_id, event_name=event_name, event_type=event_type, execution_id=execution_id, process_instance_id=process_instance_id, activity_id=activity_id, tenant_id_in=tenant_id_in, without_tenant_id=without_tenant_id, include_event_subscriptions_without_tenant_id=include_event_subscriptions_without_tenant_id, sort_by=sort_by, sort_order=sort_order, first_result=first_result, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventSubscriptionApi->get_event_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_subscription_id** | **str**| Only select subscription with the given id. | [optional] 
 **event_name** | **str**| Only select subscriptions for events with the given name. | [optional] 
 **event_type** | **str**| Only select subscriptions for events with the given type. Valid values: &#x60;message&#x60;, &#x60;signal&#x60;, &#x60;compensate&#x60; and &#x60;conditional&#x60;. | [optional] 
 **execution_id** | **str**| Only select subscriptions that belong to an execution with the given id. | [optional] 
 **process_instance_id** | **str**| Only select subscriptions that belong to a process instance with the given id. | [optional] 
 **activity_id** | **str**| Only select subscriptions that belong to an activity with the given id. | [optional] 
 **tenant_id_in** | **str**| Filter by a comma-separated list of tenant ids. Only select subscriptions that belong to one of the given tenant ids. | [optional] 
 **without_tenant_id** | **bool**| Only select subscriptions which have no tenant id. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] 
 **include_event_subscriptions_without_tenant_id** | **bool**| Select event subscriptions which have no tenant id. Can be used in combination with tenantIdIn parameter. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] 
 **sort_by** | **str**| Sort the results lexicographically by a given criterion. Must be used in conjunction with the sortOrder parameter. | [optional] 
 **sort_order** | **str**| Sort the results in a given order. Values may be asc for ascending order or desc for descending order. Must be used in conjunction with the sortBy parameter. | [optional] 
 **first_result** | **int**| Pagination of results. Specifies the index of the first result to return. | [optional] 
 **max_results** | **int**| Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. | [optional] 

### Return type

[**list[EventSubscriptionDto]**](EventSubscriptionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | Bad Request Returned if some of the query parameters are invalid, for example if a &#x60;sortOrder&#x60; parameter is supplied, but no &#x60;sortBy&#x60;. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_subscriptions_count**
> CountResultDto get_event_subscriptions_count(event_subscription_id=event_subscription_id, event_name=event_name, event_type=event_type, execution_id=execution_id, process_instance_id=process_instance_id, activity_id=activity_id, tenant_id_in=tenant_id_in, without_tenant_id=without_tenant_id, include_event_subscriptions_without_tenant_id=include_event_subscriptions_without_tenant_id)



Queries for the number of event subscriptions that fulfill given parameters. Takes the same parameters as the [Get Event Subscriptions](https://docs.camunda.org/manual/7.13/reference/rest/event-subscription/get-query/) method.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/engine-rest
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080/engine-rest"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EventSubscriptionApi(api_client)
    event_subscription_id = 'event_subscription_id_example' # str | Only select subscription with the given id. (optional)
event_name = 'event_name_example' # str | Only select subscriptions for events with the given name. (optional)
event_type = 'event_type_example' # str | Only select subscriptions for events with the given type. Valid values: `message`, `signal`, `compensate` and `conditional`. (optional)
execution_id = 'execution_id_example' # str | Only select subscriptions that belong to an execution with the given id. (optional)
process_instance_id = 'process_instance_id_example' # str | Only select subscriptions that belong to a process instance with the given id. (optional)
activity_id = 'activity_id_example' # str | Only select subscriptions that belong to an activity with the given id. (optional)
tenant_id_in = 'tenant_id_in_example' # str | Filter by a comma-separated list of tenant ids. Only select subscriptions that belong to one of the given tenant ids. (optional)
without_tenant_id = True # bool | Only select subscriptions which have no tenant id. Value may only be `true`, as `false` is the default behavior. (optional)
include_event_subscriptions_without_tenant_id = True # bool | Select event subscriptions which have no tenant id. Can be used in combination with tenantIdIn parameter. Value may only be `true`, as `false` is the default behavior. (optional)

    try:
        api_response = api_instance.get_event_subscriptions_count(event_subscription_id=event_subscription_id, event_name=event_name, event_type=event_type, execution_id=execution_id, process_instance_id=process_instance_id, activity_id=activity_id, tenant_id_in=tenant_id_in, without_tenant_id=without_tenant_id, include_event_subscriptions_without_tenant_id=include_event_subscriptions_without_tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventSubscriptionApi->get_event_subscriptions_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_subscription_id** | **str**| Only select subscription with the given id. | [optional] 
 **event_name** | **str**| Only select subscriptions for events with the given name. | [optional] 
 **event_type** | **str**| Only select subscriptions for events with the given type. Valid values: &#x60;message&#x60;, &#x60;signal&#x60;, &#x60;compensate&#x60; and &#x60;conditional&#x60;. | [optional] 
 **execution_id** | **str**| Only select subscriptions that belong to an execution with the given id. | [optional] 
 **process_instance_id** | **str**| Only select subscriptions that belong to a process instance with the given id. | [optional] 
 **activity_id** | **str**| Only select subscriptions that belong to an activity with the given id. | [optional] 
 **tenant_id_in** | **str**| Filter by a comma-separated list of tenant ids. Only select subscriptions that belong to one of the given tenant ids. | [optional] 
 **without_tenant_id** | **bool**| Only select subscriptions which have no tenant id. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] 
 **include_event_subscriptions_without_tenant_id** | **bool**| Select event subscriptions which have no tenant id. Can be used in combination with tenantIdIn parameter. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] 

### Return type

[**CountResultDto**](CountResultDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | Returned if some of the query parameters are invalid. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

