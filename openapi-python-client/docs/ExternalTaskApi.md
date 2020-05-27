# openapi_client.ExternalTaskApi

All URIs are relative to *http://localhost:8080/engine-rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**complete_external_task_resource**](ExternalTaskApi.md#complete_external_task_resource) | **POST** /external-task/{id}/complete | 
[**extend_lock**](ExternalTaskApi.md#extend_lock) | **POST** /external-task/{id}/extendLock | 
[**fetch_and_lock**](ExternalTaskApi.md#fetch_and_lock) | **POST** /external-task/fetchAndLock | 
[**get_external_task**](ExternalTaskApi.md#get_external_task) | **GET** /external-task/{id} | 
[**get_external_task_error_details**](ExternalTaskApi.md#get_external_task_error_details) | **GET** /external-task/{id}/errorDetails | 
[**get_external_tasks**](ExternalTaskApi.md#get_external_tasks) | **GET** /external-task | 
[**get_external_tasks_count**](ExternalTaskApi.md#get_external_tasks_count) | **GET** /external-task/count | 
[**get_topic_names**](ExternalTaskApi.md#get_topic_names) | **GET** /external-task/topic-names | 
[**handle_external_task_bpmn_error**](ExternalTaskApi.md#handle_external_task_bpmn_error) | **POST** /external-task/{id}/bpmnError | 
[**handle_failure**](ExternalTaskApi.md#handle_failure) | **POST** /external-task/{id}/failure | 
[**query_external_tasks**](ExternalTaskApi.md#query_external_tasks) | **POST** /external-task | 
[**query_external_tasks_count**](ExternalTaskApi.md#query_external_tasks_count) | **POST** /external-task/count | 
[**set_external_task_resource_priority**](ExternalTaskApi.md#set_external_task_resource_priority) | **PUT** /external-task/{id}/priority | 
[**set_external_task_resource_retries**](ExternalTaskApi.md#set_external_task_resource_retries) | **PUT** /external-task/{id}/retries | 
[**set_external_task_retries**](ExternalTaskApi.md#set_external_task_retries) | **PUT** /external-task/retries | 
[**set_external_task_retries_async_operation**](ExternalTaskApi.md#set_external_task_retries_async_operation) | **POST** /external-task/retries-async | 
[**unlock**](ExternalTaskApi.md#unlock) | **POST** /external-task/{id}/unlock | 


# **complete_external_task_resource**
> complete_external_task_resource(id, complete_external_task_dto=complete_external_task_dto)



Completes an external task by id and updates process variables.

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
    api_instance = openapi_client.ExternalTaskApi(api_client)
    id = 'id_example' # str | The id of the task to complete.
complete_external_task_dto = {"workerId":"brick-layer","maxTasks":1,"topics":[{"topicName":"commit","lockDuration":10000}]} # CompleteExternalTaskDto |  (optional)

    try:
        api_instance.complete_external_task_resource(id, complete_external_task_dto=complete_external_task_dto)
    except ApiException as e:
        print("Exception when calling ExternalTaskApi->complete_external_task_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to complete. | 
 **complete_external_task_dto** | [**CompleteExternalTaskDto**](CompleteExternalTaskDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request successful. |  -  |
**400** | Returned if the task&#39;s most recent lock was not acquired by the provided worker. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Returned if the task does not exist. This could indicate a wrong task id as well as a cancelled task, e.g., due to a caught BPMN boundary event. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**500** | Returned if the corresponding process instance could not be resumed successfully. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extend_lock**
> extend_lock(id, extend_lock_on_external_task_dto=extend_lock_on_external_task_dto)



Extends the timeout of the lock by a given amount of time.

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
    api_instance = openapi_client.ExternalTaskApi(api_client)
    id = 'id_example' # str | The id of the external task.
extend_lock_on_external_task_dto = {"workerId":"anId","newDuration":100000} # ExtendLockOnExternalTaskDto |  (optional)

    try:
        api_instance.extend_lock(id, extend_lock_on_external_task_dto=extend_lock_on_external_task_dto)
    except ApiException as e:
        print("Exception when calling ExternalTaskApi->extend_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the external task. | 
 **extend_lock_on_external_task_dto** | [**ExtendLockOnExternalTaskDto**](ExtendLockOnExternalTaskDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request successful. |  -  |
**400** | In case the new lock duration is negative or the external task is not locked by the given worker or not  locked at all, an exception of type &#x60;InvalidRequestException&#x60; is returned. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Returned if the task does not exist. This could indicate a wrong task id as well as a cancelled task, e.g., due to a caught BPMN boundary event. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_and_lock**
> list[LockedExternalTaskDto] fetch_and_lock(fetch_external_tasks_dto=fetch_external_tasks_dto)



Fetches and locks a specific number of external tasks for execution by a worker. Query can be restricted to specific task topics and for each task topic an individual lock time can be provided.

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
    api_instance = openapi_client.ExternalTaskApi(api_client)
    fetch_external_tasks_dto = {"workerId":"brick-layer","maxTasks":1,"topics":[{"topicName":"commit","lockDuration":10000}]} # FetchExternalTasksDto |  (optional)

    try:
        api_response = api_instance.fetch_and_lock(fetch_external_tasks_dto=fetch_external_tasks_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExternalTaskApi->fetch_and_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fetch_external_tasks_dto** | [**FetchExternalTasksDto**](FetchExternalTasksDto.md)|  | [optional] 

### Return type

[**list[LockedExternalTaskDto]**](LockedExternalTaskDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | Bad Request. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_task**
> ExternalTaskDto get_external_task(id)



Retrieves an external task by id, corresponding to the `ExternalTask` interface in the engine.

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
    api_instance = openapi_client.ExternalTaskApi(api_client)
    id = 'id_example' # str | The id of the external task to be retrieved.

    try:
        api_response = api_instance.get_external_task(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExternalTaskApi->get_external_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the external task to be retrieved. | 

### Return type

[**ExternalTaskDto**](ExternalTaskDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**404** | External task with the given id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_task_error_details**
> str get_external_task_error_details(id)



Retrieves the error details in the context of a running external task by id.

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
    api_instance = openapi_client.ExternalTaskApi(api_client)
    id = 'id_example' # str | The id of the external task for which the error details should be retrieved.

    try:
        api_response = api_instance.get_external_task_error_details(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExternalTaskApi->get_external_task_error_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the external task for which the error details should be retrieved. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**204** | Request successful. In case the external task has no error details. |  -  |
**500** | An external task with the given id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_tasks**
> list[ExternalTaskDto] get_external_tasks(external_task_id=external_task_id, external_task_id_in=external_task_id_in, topic_name=topic_name, worker_id=worker_id, locked=locked, not_locked=not_locked, with_retries_left=with_retries_left, no_retries_left=no_retries_left, lock_expiration_after=lock_expiration_after, lock_expiration_before=lock_expiration_before, activity_id=activity_id, activity_id_in=activity_id_in, execution_id=execution_id, process_instance_id=process_instance_id, process_instance_id_in=process_instance_id_in, process_definition_id=process_definition_id, tenant_id_in=tenant_id_in, active=active, suspended=suspended, priority_higher_than_or_equals=priority_higher_than_or_equals, priority_lower_than_or_equals=priority_lower_than_or_equals, sort_by=sort_by, sort_order=sort_order, first_result=first_result, max_results=max_results)



Queries for the external tasks that fulfill given parameters. Parameters may be static as well as dynamic runtime properties of executions. The size of the result set can be retrieved by using the [Get External Task Count](https://docs.camunda.org/manual/7.13/reference/rest/external-task/get-query-count/) method.

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
    api_instance = openapi_client.ExternalTaskApi(api_client)
    external_task_id = 'external_task_id_example' # str | Filter by an external task's id. (optional)
external_task_id_in = 'external_task_id_in_example' # str | Filter by the comma-separated list of external task ids. (optional)
topic_name = 'topic_name_example' # str | Filter by an external task topic. (optional)
worker_id = 'worker_id_example' # str | Filter by the id of the worker that the task was most recently locked by. (optional)
locked = True # bool | Only include external tasks that are currently locked (i.e., they have a lock time and it has not expired). Value may only be `true`, as `false` matches any external task. (optional)
not_locked = True # bool | Only include external tasks that are currently not locked (i.e., they have no lock or it has expired). Value may only be `true`, as `false` matches any external task. (optional)
with_retries_left = True # bool | Only include external tasks that have a positive (&gt; 0) number of retries (or `null`). Value may only be `true`, as `false` matches any external task. (optional)
no_retries_left = True # bool | Only include external tasks that have 0 retries. Value may only be `true`, as `false` matches any external task. (optional)
lock_expiration_after = '2013-10-20T19:20:30+01:00' # datetime | Restrict to external tasks that have a lock that expires after a given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.000+0200`. (optional)
lock_expiration_before = '2013-10-20T19:20:30+01:00' # datetime | Restrict to external tasks that have a lock that expires before a given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.000+0200`. (optional)
activity_id = 'activity_id_example' # str | Filter by the id of the activity that an external task is created for. (optional)
activity_id_in = 'activity_id_in_example' # str | Filter by the comma-separated list of ids of the activities that an external task is created for. (optional)
execution_id = 'execution_id_example' # str | Filter by the id of the execution that an external task belongs to. (optional)
process_instance_id = 'process_instance_id_example' # str | Filter by the id of the process instance that an external task belongs to. (optional)
process_instance_id_in = 'process_instance_id_in_example' # str | Filter by a comma-separated list of process instance ids that an external task may belong to. (optional)
process_definition_id = 'process_definition_id_example' # str | Filter by the id of the process definition that an external task belongs to. (optional)
tenant_id_in = 'tenant_id_in_example' # str | Filter by a comma-separated list of tenant ids. An external task must have one of the given tenant ids. (optional)
active = True # bool | Only include active tasks. Value may only be `true`, as `false` matches any external task. (optional)
suspended = True # bool | Only include suspended tasks. Value may only be `true`, as `false` matches any external task. (optional)
priority_higher_than_or_equals = 56 # int | Only include jobs with a priority higher than or equal to the given value. Value must be a valid `long` value. (optional)
priority_lower_than_or_equals = 56 # int | Only include jobs with a priority lower than or equal to the given value. Value must be a valid `long` value. (optional)
sort_by = 'sort_by_example' # str | Sort the results lexicographically by a given criterion. Must be used in conjunction with the sortOrder parameter. (optional)
sort_order = 'sort_order_example' # str | Sort the results in a given order. Values may be asc for ascending order or desc for descending order. Must be used in conjunction with the sortBy parameter. (optional)
first_result = 56 # int | Pagination of results. Specifies the index of the first result to return. (optional)
max_results = 56 # int | Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. (optional)

    try:
        api_response = api_instance.get_external_tasks(external_task_id=external_task_id, external_task_id_in=external_task_id_in, topic_name=topic_name, worker_id=worker_id, locked=locked, not_locked=not_locked, with_retries_left=with_retries_left, no_retries_left=no_retries_left, lock_expiration_after=lock_expiration_after, lock_expiration_before=lock_expiration_before, activity_id=activity_id, activity_id_in=activity_id_in, execution_id=execution_id, process_instance_id=process_instance_id, process_instance_id_in=process_instance_id_in, process_definition_id=process_definition_id, tenant_id_in=tenant_id_in, active=active, suspended=suspended, priority_higher_than_or_equals=priority_higher_than_or_equals, priority_lower_than_or_equals=priority_lower_than_or_equals, sort_by=sort_by, sort_order=sort_order, first_result=first_result, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExternalTaskApi->get_external_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_task_id** | **str**| Filter by an external task&#39;s id. | [optional] 
 **external_task_id_in** | **str**| Filter by the comma-separated list of external task ids. | [optional] 
 **topic_name** | **str**| Filter by an external task topic. | [optional] 
 **worker_id** | **str**| Filter by the id of the worker that the task was most recently locked by. | [optional] 
 **locked** | **bool**| Only include external tasks that are currently locked (i.e., they have a lock time and it has not expired). Value may only be &#x60;true&#x60;, as &#x60;false&#x60; matches any external task. | [optional] 
 **not_locked** | **bool**| Only include external tasks that are currently not locked (i.e., they have no lock or it has expired). Value may only be &#x60;true&#x60;, as &#x60;false&#x60; matches any external task. | [optional] 
 **with_retries_left** | **bool**| Only include external tasks that have a positive (&amp;gt; 0) number of retries (or &#x60;null&#x60;). Value may only be &#x60;true&#x60;, as &#x60;false&#x60; matches any external task. | [optional] 
 **no_retries_left** | **bool**| Only include external tasks that have 0 retries. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; matches any external task. | [optional] 
 **lock_expiration_after** | **datetime**| Restrict to external tasks that have a lock that expires after a given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.000+0200&#x60;. | [optional] 
 **lock_expiration_before** | **datetime**| Restrict to external tasks that have a lock that expires before a given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.000+0200&#x60;. | [optional] 
 **activity_id** | **str**| Filter by the id of the activity that an external task is created for. | [optional] 
 **activity_id_in** | **str**| Filter by the comma-separated list of ids of the activities that an external task is created for. | [optional] 
 **execution_id** | **str**| Filter by the id of the execution that an external task belongs to. | [optional] 
 **process_instance_id** | **str**| Filter by the id of the process instance that an external task belongs to. | [optional] 
 **process_instance_id_in** | **str**| Filter by a comma-separated list of process instance ids that an external task may belong to. | [optional] 
 **process_definition_id** | **str**| Filter by the id of the process definition that an external task belongs to. | [optional] 
 **tenant_id_in** | **str**| Filter by a comma-separated list of tenant ids. An external task must have one of the given tenant ids. | [optional] 
 **active** | **bool**| Only include active tasks. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; matches any external task. | [optional] 
 **suspended** | **bool**| Only include suspended tasks. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; matches any external task. | [optional] 
 **priority_higher_than_or_equals** | **int**| Only include jobs with a priority higher than or equal to the given value. Value must be a valid &#x60;long&#x60; value. | [optional] 
 **priority_lower_than_or_equals** | **int**| Only include jobs with a priority lower than or equal to the given value. Value must be a valid &#x60;long&#x60; value. | [optional] 
 **sort_by** | **str**| Sort the results lexicographically by a given criterion. Must be used in conjunction with the sortOrder parameter. | [optional] 
 **sort_order** | **str**| Sort the results in a given order. Values may be asc for ascending order or desc for descending order. Must be used in conjunction with the sortBy parameter. | [optional] 
 **first_result** | **int**| Pagination of results. Specifies the index of the first result to return. | [optional] 
 **max_results** | **int**| Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. | [optional] 

### Return type

[**list[ExternalTaskDto]**](ExternalTaskDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | Returned if some of the query parameters are invalid, for example if a &#x60;sortOrder&#x60; parameter is supplied, but no &#x60;sortBy&#x60;. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_tasks_count**
> CountResultDto get_external_tasks_count(external_task_id=external_task_id, external_task_id_in=external_task_id_in, topic_name=topic_name, worker_id=worker_id, locked=locked, not_locked=not_locked, with_retries_left=with_retries_left, no_retries_left=no_retries_left, lock_expiration_after=lock_expiration_after, lock_expiration_before=lock_expiration_before, activity_id=activity_id, activity_id_in=activity_id_in, execution_id=execution_id, process_instance_id=process_instance_id, process_instance_id_in=process_instance_id_in, process_definition_id=process_definition_id, tenant_id_in=tenant_id_in, active=active, suspended=suspended, priority_higher_than_or_equals=priority_higher_than_or_equals, priority_lower_than_or_equals=priority_lower_than_or_equals)



Queries for the number of external tasks that fulfill given parameters. Takes the same parameters as the [Get External Tasks](https://docs.camunda.org/manual/7.13/reference/rest/external-task/get-query/) method.

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
    api_instance = openapi_client.ExternalTaskApi(api_client)
    external_task_id = 'external_task_id_example' # str | Filter by an external task's id. (optional)
external_task_id_in = 'external_task_id_in_example' # str | Filter by the comma-separated list of external task ids. (optional)
topic_name = 'topic_name_example' # str | Filter by an external task topic. (optional)
worker_id = 'worker_id_example' # str | Filter by the id of the worker that the task was most recently locked by. (optional)
locked = True # bool | Only include external tasks that are currently locked (i.e., they have a lock time and it has not expired). Value may only be `true`, as `false` matches any external task. (optional)
not_locked = True # bool | Only include external tasks that are currently not locked (i.e., they have no lock or it has expired). Value may only be `true`, as `false` matches any external task. (optional)
with_retries_left = True # bool | Only include external tasks that have a positive (&gt; 0) number of retries (or `null`). Value may only be `true`, as `false` matches any external task. (optional)
no_retries_left = True # bool | Only include external tasks that have 0 retries. Value may only be `true`, as `false` matches any external task. (optional)
lock_expiration_after = '2013-10-20T19:20:30+01:00' # datetime | Restrict to external tasks that have a lock that expires after a given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.000+0200`. (optional)
lock_expiration_before = '2013-10-20T19:20:30+01:00' # datetime | Restrict to external tasks that have a lock that expires before a given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.000+0200`. (optional)
activity_id = 'activity_id_example' # str | Filter by the id of the activity that an external task is created for. (optional)
activity_id_in = 'activity_id_in_example' # str | Filter by the comma-separated list of ids of the activities that an external task is created for. (optional)
execution_id = 'execution_id_example' # str | Filter by the id of the execution that an external task belongs to. (optional)
process_instance_id = 'process_instance_id_example' # str | Filter by the id of the process instance that an external task belongs to. (optional)
process_instance_id_in = 'process_instance_id_in_example' # str | Filter by a comma-separated list of process instance ids that an external task may belong to. (optional)
process_definition_id = 'process_definition_id_example' # str | Filter by the id of the process definition that an external task belongs to. (optional)
tenant_id_in = 'tenant_id_in_example' # str | Filter by a comma-separated list of tenant ids. An external task must have one of the given tenant ids. (optional)
active = True # bool | Only include active tasks. Value may only be `true`, as `false` matches any external task. (optional)
suspended = True # bool | Only include suspended tasks. Value may only be `true`, as `false` matches any external task. (optional)
priority_higher_than_or_equals = 56 # int | Only include jobs with a priority higher than or equal to the given value. Value must be a valid `long` value. (optional)
priority_lower_than_or_equals = 56 # int | Only include jobs with a priority lower than or equal to the given value. Value must be a valid `long` value. (optional)

    try:
        api_response = api_instance.get_external_tasks_count(external_task_id=external_task_id, external_task_id_in=external_task_id_in, topic_name=topic_name, worker_id=worker_id, locked=locked, not_locked=not_locked, with_retries_left=with_retries_left, no_retries_left=no_retries_left, lock_expiration_after=lock_expiration_after, lock_expiration_before=lock_expiration_before, activity_id=activity_id, activity_id_in=activity_id_in, execution_id=execution_id, process_instance_id=process_instance_id, process_instance_id_in=process_instance_id_in, process_definition_id=process_definition_id, tenant_id_in=tenant_id_in, active=active, suspended=suspended, priority_higher_than_or_equals=priority_higher_than_or_equals, priority_lower_than_or_equals=priority_lower_than_or_equals)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExternalTaskApi->get_external_tasks_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_task_id** | **str**| Filter by an external task&#39;s id. | [optional] 
 **external_task_id_in** | **str**| Filter by the comma-separated list of external task ids. | [optional] 
 **topic_name** | **str**| Filter by an external task topic. | [optional] 
 **worker_id** | **str**| Filter by the id of the worker that the task was most recently locked by. | [optional] 
 **locked** | **bool**| Only include external tasks that are currently locked (i.e., they have a lock time and it has not expired). Value may only be &#x60;true&#x60;, as &#x60;false&#x60; matches any external task. | [optional] 
 **not_locked** | **bool**| Only include external tasks that are currently not locked (i.e., they have no lock or it has expired). Value may only be &#x60;true&#x60;, as &#x60;false&#x60; matches any external task. | [optional] 
 **with_retries_left** | **bool**| Only include external tasks that have a positive (&amp;gt; 0) number of retries (or &#x60;null&#x60;). Value may only be &#x60;true&#x60;, as &#x60;false&#x60; matches any external task. | [optional] 
 **no_retries_left** | **bool**| Only include external tasks that have 0 retries. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; matches any external task. | [optional] 
 **lock_expiration_after** | **datetime**| Restrict to external tasks that have a lock that expires after a given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.000+0200&#x60;. | [optional] 
 **lock_expiration_before** | **datetime**| Restrict to external tasks that have a lock that expires before a given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.000+0200&#x60;. | [optional] 
 **activity_id** | **str**| Filter by the id of the activity that an external task is created for. | [optional] 
 **activity_id_in** | **str**| Filter by the comma-separated list of ids of the activities that an external task is created for. | [optional] 
 **execution_id** | **str**| Filter by the id of the execution that an external task belongs to. | [optional] 
 **process_instance_id** | **str**| Filter by the id of the process instance that an external task belongs to. | [optional] 
 **process_instance_id_in** | **str**| Filter by a comma-separated list of process instance ids that an external task may belong to. | [optional] 
 **process_definition_id** | **str**| Filter by the id of the process definition that an external task belongs to. | [optional] 
 **tenant_id_in** | **str**| Filter by a comma-separated list of tenant ids. An external task must have one of the given tenant ids. | [optional] 
 **active** | **bool**| Only include active tasks. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; matches any external task. | [optional] 
 **suspended** | **bool**| Only include suspended tasks. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; matches any external task. | [optional] 
 **priority_higher_than_or_equals** | **int**| Only include jobs with a priority higher than or equal to the given value. Value must be a valid &#x60;long&#x60; value. | [optional] 
 **priority_lower_than_or_equals** | **int**| Only include jobs with a priority lower than or equal to the given value. Value must be a valid &#x60;long&#x60; value. | [optional] 

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

# **get_topic_names**
> list[str] get_topic_names(with_locked_tasks=with_locked_tasks, with_unlocked_tasks=with_unlocked_tasks, with_retries_left=with_retries_left)



Queries for distinct topic names of external tasks that fulfill given parameters. Query can be restricted to only tasks with retries left, tasks that are locked, or tasks that are unlocked. The parameters withLockedTasks and withUnlockedTasks are exclusive. Setting them both to true will return an empty list. Providing no parameters will return a list of all distinct topic names with external tasks.

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
    api_instance = openapi_client.ExternalTaskApi(api_client)
    with_locked_tasks = True # bool | Only include external tasks that are currently locked (i.e., they have a lock time and it has not expired). Value may only be `true`, as `false` matches any external task. (optional)
with_unlocked_tasks = True # bool | Only include external tasks that are currently not locked (i.e., they have no lock or it has expired). Value may only be `true`, as `false` matches any external task. (optional)
with_retries_left = True # bool | Only include external tasks that have a positive (&gt; 0) number of retries (or `null`). Value may only be `true`, as `false` matches any external task. (optional)

    try:
        api_response = api_instance.get_topic_names(with_locked_tasks=with_locked_tasks, with_unlocked_tasks=with_unlocked_tasks, with_retries_left=with_retries_left)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExternalTaskApi->get_topic_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **with_locked_tasks** | **bool**| Only include external tasks that are currently locked (i.e., they have a lock time and it has not expired). Value may only be &#x60;true&#x60;, as &#x60;false&#x60; matches any external task. | [optional] 
 **with_unlocked_tasks** | **bool**| Only include external tasks that are currently not locked (i.e., they have no lock or it has expired). Value may only be &#x60;true&#x60;, as &#x60;false&#x60; matches any external task. | [optional] 
 **with_retries_left** | **bool**| Only include external tasks that have a positive (&amp;gt; 0) number of retries (or &#x60;null&#x60;). Value may only be &#x60;true&#x60;, as &#x60;false&#x60; matches any external task. | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | Returned if some of the query parameters are invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_external_task_bpmn_error**
> handle_external_task_bpmn_error(id, external_task_bpmn_error=external_task_bpmn_error)



Reports a business error in the context of a running external task by id. The error code must be specified to identify the BPMN error handler.

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
    api_instance = openapi_client.ExternalTaskApi(api_client)
    id = 'id_example' # str | The id of the external task in which context a BPMN error is reported.
external_task_bpmn_error = {"workerId":"aWorker","errorCode":"bpmn-error","errorMessage":"anErrorMessage","variables":{"aVariable":{"value":"aStringValue","type":"String"},"anotherVariable":{"value":true,"type":"Boolean"}}} # ExternalTaskBpmnError |  (optional)

    try:
        api_instance.handle_external_task_bpmn_error(id, external_task_bpmn_error=external_task_bpmn_error)
    except ApiException as e:
        print("Exception when calling ExternalTaskApi->handle_external_task_bpmn_error: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the external task in which context a BPMN error is reported. | 
 **external_task_bpmn_error** | [**ExternalTaskBpmnError**](ExternalTaskBpmnError.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request successful. |  -  |
**400** | Returned if the task&#39;s most recent lock was not acquired by the provided worker.  See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Returned if the task does not exist. This could indicate a wrong task id as well as a cancelled task, e.g., due to a caught BPMN boundary event.  See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**500** | Returned if the corresponding process instance could not be resumed successfully.  See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_failure**
> handle_failure(id, external_task_failure_dto=external_task_failure_dto)



Reports a failure to execute an external task by id. A number of retries and a timeout until the task can be retried can be specified. If retries are set to 0, an incident for this task is created.

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
    api_instance = openapi_client.ExternalTaskApi(api_client)
    id = 'id_example' # str | The id of the external task to report a failure for.
external_task_failure_dto = {"workerId":"aWorker","errorMessage":"Does not compute","retries":3,"retryTimeout":60000} # ExternalTaskFailureDto |  (optional)

    try:
        api_instance.handle_failure(id, external_task_failure_dto=external_task_failure_dto)
    except ApiException as e:
        print("Exception when calling ExternalTaskApi->handle_failure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the external task to report a failure for. | 
 **external_task_failure_dto** | [**ExternalTaskFailureDto**](ExternalTaskFailureDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request successful. |  -  |
**400** | Returned if the task&#39;s most recent lock was not acquired by the provided worker. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Returned if the task does not exist. This could indicate a wrong task id as well as a cancelled task, e.g., due to a caught BPMN boundary event. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**500** | Returned if the corresponding process instance could not be resumed successfully. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_external_tasks**
> list[ExternalTaskDto] query_external_tasks(first_result=first_result, max_results=max_results, external_task_query_dto=external_task_query_dto)



Queries for external tasks that fulfill given parameters in the form of a JSON object.  This method is slightly more powerful than the [Get External Tasks](https://docs.camunda.org/manual/7.13/reference/rest/external-task/get-query/) method because it allows to specify a hierarchical result sorting.

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
    api_instance = openapi_client.ExternalTaskApi(api_client)
    first_result = 56 # int | Pagination of results. Specifies the index of the first result to return. (optional)
max_results = 56 # int | Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. (optional)
external_task_query_dto = {"processDefinitionId":"aProcessDefinitionId","sorting":[{"sortBy":"processDefinitionKey","sortOrder":"asc"},{"sortBy":"lockExpirationTime","sortOrder":"desc"}]} # ExternalTaskQueryDto |  (optional)

    try:
        api_response = api_instance.query_external_tasks(first_result=first_result, max_results=max_results, external_task_query_dto=external_task_query_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExternalTaskApi->query_external_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_result** | **int**| Pagination of results. Specifies the index of the first result to return. | [optional] 
 **max_results** | **int**| Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. | [optional] 
 **external_task_query_dto** | [**ExternalTaskQueryDto**](ExternalTaskQueryDto.md)|  | [optional] 

### Return type

[**list[ExternalTaskDto]**](ExternalTaskDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. The Response is a JSON array of external task objects. |  -  |
**400** | Returned if some of the query parameters are invalid, for example if a &#x60;sortOrder&#x60; parameter is supplied, but no &#x60;sortBy&#x60;. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_external_tasks_count**
> CountResultDto query_external_tasks_count(external_task_query_dto=external_task_query_dto)



Queries for the number of external tasks that fulfill given parameters. This method takes the same message body as the [Get External Tasks (POST)](https://docs.camunda.org/manual/7.13/reference/rest/external-task/post-query/) method.

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
    api_instance = openapi_client.ExternalTaskApi(api_client)
    external_task_query_dto = {"topicName":"aTopicName","withRetriesLeft":true} # ExternalTaskQueryDto |  (optional)

    try:
        api_response = api_instance.query_external_tasks_count(external_task_query_dto=external_task_query_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExternalTaskApi->query_external_tasks_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_task_query_dto** | [**ExternalTaskQueryDto**](ExternalTaskQueryDto.md)|  | [optional] 

### Return type

[**CountResultDto**](CountResultDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | Returned if some of the query parameters are invalid. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_external_task_resource_priority**
> set_external_task_resource_priority(id, priority_dto=priority_dto)



Sets the priority of an existing external task by id. The default value of a priority is 0.

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
    api_instance = openapi_client.ExternalTaskApi(api_client)
    id = 'id_example' # str | The id of the external task to set the priority for.
priority_dto = {"priority":5} # PriorityDto |  (optional)

    try:
        api_instance.set_external_task_resource_priority(id, priority_dto=priority_dto)
    except ApiException as e:
        print("Exception when calling ExternalTaskApi->set_external_task_resource_priority: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the external task to set the priority for. | 
 **priority_dto** | [**PriorityDto**](PriorityDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request successful. |  -  |
**404** | Returned if the task does not exist. This could indicate a wrong task id as well as a cancelled task, e.g., due to a caught BPMN boundary event. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_external_task_resource_retries**
> set_external_task_resource_retries(id, retries_dto=retries_dto)



Sets the number of retries left to execute an external task by id. If retries are set to 0, an  incident is created.

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
    api_instance = openapi_client.ExternalTaskApi(api_client)
    id = 'id_example' # str | The id of the external task to set the number of retries for.
retries_dto = {"retries":123} # RetriesDto |  (optional)

    try:
        api_instance.set_external_task_resource_retries(id, retries_dto=retries_dto)
    except ApiException as e:
        print("Exception when calling ExternalTaskApi->set_external_task_resource_retries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the external task to set the number of retries for. | 
 **retries_dto** | [**RetriesDto**](RetriesDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request successful. |  -  |
**400** | Returned if the task does not exist. This could indicate a wrong task id as well as a cancelled task, e.g., due to a caught BPMN boundary event. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | In case the number of retries is negative or null, an exception of type &#x60;InvalidRequestException&#x60; is returned. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_external_task_retries**
> set_external_task_retries(set_retries_for_external_tasks_dto=set_retries_for_external_tasks_dto)



Sets the number of retries left to execute external tasks by id synchronously. If retries are set to 0,  an incident is created.

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
    api_instance = openapi_client.ExternalTaskApi(api_client)
    set_retries_for_external_tasks_dto = {"retries":123,"externalTaskIds":["anExternalTask","anotherExternalTask"]} # SetRetriesForExternalTasksDto |  (optional)

    try:
        api_instance.set_external_task_retries(set_retries_for_external_tasks_dto=set_retries_for_external_tasks_dto)
    except ApiException as e:
        print("Exception when calling ExternalTaskApi->set_external_task_retries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_retries_for_external_tasks_dto** | [**SetRetriesForExternalTasksDto**](SetRetriesForExternalTasksDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request successful. |  -  |
**400** | In case the number of retries is negative or null, an exception of type &#x60;InvalidRequestException&#x60; is returned. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Returned if the task does not exist. This could indicate a wrong task id as well as a cancelled task,  e.g., due to a caught BPMN boundary event. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_external_task_retries_async_operation**
> BatchDto set_external_task_retries_async_operation(set_retries_for_external_tasks_dto=set_retries_for_external_tasks_dto)



Sets the number of retries left to execute external tasks by id asynchronously. If retries are set to 0, an incident is created.

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
    api_instance = openapi_client.ExternalTaskApi(api_client)
    set_retries_for_external_tasks_dto = {"retries":123,"externalTaskIds":["anExternalTask","anotherExternalTask"]} # SetRetriesForExternalTasksDto |  (optional)

    try:
        api_response = api_instance.set_external_task_retries_async_operation(set_retries_for_external_tasks_dto=set_retries_for_external_tasks_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExternalTaskApi->set_external_task_retries_async_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_retries_for_external_tasks_dto** | [**SetRetriesForExternalTasksDto**](SetRetriesForExternalTasksDto.md)|  | [optional] 

### Return type

[**BatchDto**](BatchDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | If neither externalTaskIds nor externalTaskQuery are present or externalTaskIds contains null value or  the number of retries is negative or null, an exception of type &#x60;InvalidRequestException&#x60; is returned. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Returned if the task does not exist. This could indicate a wrong task id as well as a cancelled task,  e.g., due to a caught BPMN boundary event. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlock**
> unlock(id)



Unlocks an external task by id. Clears the task's lock expiration time and worker id.

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
    api_instance = openapi_client.ExternalTaskApi(api_client)
    id = 'id_example' # str | The id of the external task to unlock.

    try:
        api_instance.unlock(id)
    except ApiException as e:
        print("Exception when calling ExternalTaskApi->unlock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the external task to unlock. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request successful. |  -  |
**404** | Returned if the task does not exist. This could indicate a wrong task id as well as a cancelled task, e.g., due to a caught BPMN boundary event. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

