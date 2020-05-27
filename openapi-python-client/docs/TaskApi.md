# openapi_client.TaskApi

All URIs are relative to *http://localhost:8080/engine-rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**claim**](TaskApi.md#claim) | **POST** /task/{id}/claim | 
[**complete**](TaskApi.md#complete) | **POST** /task/{id}/complete | 
[**create_task**](TaskApi.md#create_task) | **POST** /task/create | 
[**delegate_task**](TaskApi.md#delegate_task) | **POST** /task/{id}/delegate | 
[**delete_task**](TaskApi.md#delete_task) | **DELETE** /task/{id} | 
[**get_deployed_form**](TaskApi.md#get_deployed_form) | **GET** /task/{id}/deployed-form | 
[**get_form**](TaskApi.md#get_form) | **GET** /task/{id}/form | 
[**get_form_variables**](TaskApi.md#get_form_variables) | **GET** /task/{id}/form-variables | 
[**get_rendered_form**](TaskApi.md#get_rendered_form) | **GET** /task/{id}/rendered-form | 
[**get_task**](TaskApi.md#get_task) | **GET** /task/{id} | 
[**get_tasks**](TaskApi.md#get_tasks) | **GET** /task | 
[**get_tasks_count**](TaskApi.md#get_tasks_count) | **GET** /task/count | 
[**handle_bpmn_error**](TaskApi.md#handle_bpmn_error) | **POST** /task/{id}/bpmnError | 
[**handle_escalation**](TaskApi.md#handle_escalation) | **POST** /task/{id}/bpmnEscalation | 
[**query_tasks**](TaskApi.md#query_tasks) | **POST** /task | 
[**query_tasks_count**](TaskApi.md#query_tasks_count) | **POST** /task/count | 
[**resolve**](TaskApi.md#resolve) | **POST** /task/{id}/resolve | 
[**set_assignee**](TaskApi.md#set_assignee) | **POST** /task/{id}/assignee | 
[**submit**](TaskApi.md#submit) | **POST** /task/{id}/submit-form | 
[**unclaim**](TaskApi.md#unclaim) | **POST** /task/{id}/unclaim | 
[**update_task**](TaskApi.md#update_task) | **PUT** /task/{id} | 


# **claim**
> claim(id, user_id_dto=user_id_dto)



Claims a task for a specific user.  **Note:** The difference with the [Set Assignee](https://docs.camunda.org/manual/7.13/reference/rest/task/post-assignee/) method is that here a check is performed to see if the task already has a user assigned to it.

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
    api_instance = openapi_client.TaskApi(api_client)
    id = 'id_example' # str | The id of the task to claim.
user_id_dto = {"userId":"aUserId"} # UserIdDto | Provide the id of the user that claims the task. (optional)

    try:
        api_instance.claim(id, user_id_dto=user_id_dto)
    except ApiException as e:
        print("Exception when calling TaskApi->claim: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to claim. | 
 **user_id_dto** | [**UserIdDto**](UserIdDto.md)| Provide the id of the user that claims the task. | [optional] 

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
**500** | Task with given id does not exist or claiming was not successful. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete**
> dict(str, VariableValueDto) complete(id, complete_task_dto=complete_task_dto)



Completes a task and updates process variables.

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
    api_instance = openapi_client.TaskApi(api_client)
    id = 'id_example' # str | The id of the task to complete.
complete_task_dto = {"variables":{"aVariable":{"value":"aStringValue"},"anotherVariable":{"value":42},"aThirdVariable":{"value":true}},"withVariablesInReturn":true} # CompleteTaskDto |  (optional)

    try:
        api_response = api_instance.complete(id, complete_task_dto=complete_task_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskApi->complete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to complete. | 
 **complete_task_dto** | [**CompleteTaskDto**](CompleteTaskDto.md)|  | [optional] 

### Return type

[**dict(str, VariableValueDto)**](VariableValueDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. The response contains the process variables. |  -  |
**204** | Request successful. The response contains no variables. |  -  |
**400** | The variable value or type is invalid, for example if the value could not be parsed to an Integer value or the passed variable type is not supported. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**500** | If the task does not exist or the corresponding process instance could not be resumed successfully. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_task**
> create_task(task_dto=task_dto)



Creates a new task.

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
    api_instance = openapi_client.TaskApi(api_client)
    task_dto = {"id":"aTaskId","name":"My Task","description":"This have to be done very urgent","priority":30,"assignee":"peter","owner":"mary","delegationState":"PENDING","due":"2014-08-30T10:00:00.000+0200","followUp":"2014-08-25T10:00:00.000+0200","parentTaskId":"aParentTaskId","caseInstanceId":"aCaseInstanceId","tenantId":null} # TaskDto |  (optional)

    try:
        api_instance.create_task(task_dto=task_dto)
    except ApiException as e:
        print("Exception when calling TaskApi->create_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_dto** | [**TaskDto**](TaskDto.md)|  | [optional] 

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
**400** | Returned if a not valid &#x60;delegationState&#x60; is supplied. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delegate_task**
> delegate_task(id, user_id_dto=user_id_dto)



Delegates a task to another user.

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
    api_instance = openapi_client.TaskApi(api_client)
    id = 'id_example' # str | The id of the task to delegate.
user_id_dto = {"userId":"aUserId"} # UserIdDto | Provide the id of the user that the task should be delegated to. (optional)

    try:
        api_instance.delegate_task(id, user_id_dto=user_id_dto)
    except ApiException as e:
        print("Exception when calling TaskApi->delegate_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to delegate. | 
 **user_id_dto** | [**UserIdDto**](UserIdDto.md)| Provide the id of the user that the task should be delegated to. | [optional] 

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
**500** | If the task does not exist or delegation was not successful. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_task**
> delete_task(id)



Removes a task by id.

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
    api_instance = openapi_client.TaskApi(api_client)
    id = 'id_example' # str | The id of the task to be removed.

    try:
        api_instance.delete_task(id)
    except ApiException as e:
        print("Exception when calling TaskApi->delete_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to be removed. | 

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
**400** | Bad Request. The Task with the given id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**500** | The Task with the given id cannot be deleted because it is part of a running process or case instance. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployed_form**
> file get_deployed_form(id)



Retrieves the deployed form that is referenced from a given task. For further information please refer to the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/task-forms/#embedded-task-forms).

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
    api_instance = openapi_client.TaskApi(api_client)
    id = 'id_example' # str | The id of the task to get the deployed form for.

    try:
        api_response = api_instance.get_deployed_form(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskApi->get_deployed_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to get the deployed form for. | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xhtml+xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | The form key has wrong format. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**403** | The deployed form cannot be retrieved due to missing permissions on task resource. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | No deployed form for a given task exists. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_form**
> FormDto get_form(id)



Retrieves the form key for a task. The form key corresponds to the `FormData#formKey` property in the engine. This key can be used to do task-specific form rendering in client applications. Additionally, the context path of the containing process application is returned.

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
    api_instance = openapi_client.TaskApi(api_client)
    id = 'id_example' # str | The id of the task to retrieve the form for.

    try:
        api_response = api_instance.get_form(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskApi->get_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to retrieve the form for. | 

### Return type

[**FormDto**](FormDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | Task with given id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_form_variables**
> dict(str, VariableValueDto) get_form_variables(id, variable_names=variable_names, deserialize_values=deserialize_values)



Retrieves the form variables for a task. The form variables take form data specified on the task into account. If form fields are defined, the variable types and default values of the form fields are taken into account.

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
    api_instance = openapi_client.TaskApi(api_client)
    id = 'id_example' # str | The id of the task to retrieve the variables for.
variable_names = 'variable_names_example' # str | A comma-separated list of variable names. Allows restricting the list of requested variables to the variable names in the list. It is best practice to restrict the list of variables to the variables actually required by the form in order to minimize fetching of data. If the query parameter is ommitted all variables are fetched. If the query parameter contains non-existent variable names, the variable names are ignored. (optional)
deserialize_values = True # bool | Determines whether serializable variable values (typically variables that store custom Java objects) should be deserialized on server side (default true).  If set to true, a serializable variable will be deserialized on server side and transformed to JSON using [Jackson's](http://jackson.codehaus.org/) POJO/bean property introspection feature. Note that this requires the Java classes of the variable value to be on the REST API's classpath.  If set to false, a serializable variable will be returned in its serialized format. For example, a variable that is serialized as XML will be returned as a JSON string containing XML.  Note: While true is the default value for reasons of backward compatibility, we recommend setting this parameter to false when developing web applications that are independent of the Java process applications deployed to the engine. (optional) (default to True)

    try:
        api_response = api_instance.get_form_variables(id, variable_names=variable_names, deserialize_values=deserialize_values)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskApi->get_form_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to retrieve the variables for. | 
 **variable_names** | **str**| A comma-separated list of variable names. Allows restricting the list of requested variables to the variable names in the list. It is best practice to restrict the list of variables to the variables actually required by the form in order to minimize fetching of data. If the query parameter is ommitted all variables are fetched. If the query parameter contains non-existent variable names, the variable names are ignored. | [optional] 
 **deserialize_values** | **bool**| Determines whether serializable variable values (typically variables that store custom Java objects) should be deserialized on server side (default true).  If set to true, a serializable variable will be deserialized on server side and transformed to JSON using [Jackson&#39;s](http://jackson.codehaus.org/) POJO/bean property introspection feature. Note that this requires the Java classes of the variable value to be on the REST API&#39;s classpath.  If set to false, a serializable variable will be returned in its serialized format. For example, a variable that is serialized as XML will be returned as a JSON string containing XML.  Note: While true is the default value for reasons of backward compatibility, we recommend setting this parameter to false when developing web applications that are independent of the Java process applications deployed to the engine. | [optional] [default to True]

### Return type

[**dict(str, VariableValueDto)**](VariableValueDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. A JSON object containing a property for each variable returned. |  -  |
**404** |  id is null or does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rendered_form**
> file get_rendered_form(id)



Retrieves the rendered form for a task. This method can be used to get the HTML rendering of a [Generated Task Form](https://docs.camunda.org/manual/7.13/user-guide/task-forms/#generated-task-forms).

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
    api_instance = openapi_client.TaskApi(api_client)
    id = 'id_example' # str | The id of the task to get the rendered form for.

    try:
        api_response = api_instance.get_rendered_form(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskApi->get_rendered_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to get the rendered form for. | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xhtml+xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | The task with the given id does not exist or has no form field metadata defined for this task. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> TaskDto get_task(id)



Retrieves a task by id.

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
    api_instance = openapi_client.TaskApi(api_client)
    id = 'id_example' # str | The id of the task to be retrieved.

    try:
        api_response = api_instance.get_task(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskApi->get_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to be retrieved. | 

### Return type

[**TaskDto**](TaskDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**404** | Task with given id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks**
> list[TaskDto] get_tasks(process_instance_id=process_instance_id, process_instance_id_in=process_instance_id_in, process_instance_business_key=process_instance_business_key, process_instance_business_key_expression=process_instance_business_key_expression, process_instance_business_key_in=process_instance_business_key_in, process_instance_business_key_like=process_instance_business_key_like, process_instance_business_key_like_expression=process_instance_business_key_like_expression, process_definition_id=process_definition_id, process_definition_key=process_definition_key, process_definition_key_in=process_definition_key_in, process_definition_name=process_definition_name, process_definition_name_like=process_definition_name_like, execution_id=execution_id, case_instance_id=case_instance_id, case_instance_business_key=case_instance_business_key, case_instance_business_key_like=case_instance_business_key_like, case_definition_id=case_definition_id, case_definition_key=case_definition_key, case_definition_name=case_definition_name, case_definition_name_like=case_definition_name_like, case_execution_id=case_execution_id, activity_instance_id_in=activity_instance_id_in, tenant_id_in=tenant_id_in, without_tenant_id=without_tenant_id, assignee=assignee, assignee_expression=assignee_expression, assignee_like=assignee_like, assignee_like_expression=assignee_like_expression, assignee_in=assignee_in, owner=owner, owner_expression=owner_expression, candidate_group=candidate_group, candidate_group_expression=candidate_group_expression, candidate_user=candidate_user, candidate_user_expression=candidate_user_expression, include_assigned_tasks=include_assigned_tasks, involved_user=involved_user, involved_user_expression=involved_user_expression, assigned=assigned, unassigned=unassigned, task_definition_key=task_definition_key, task_definition_key_in=task_definition_key_in, task_definition_key_like=task_definition_key_like, name=name, name_not_equal=name_not_equal, name_like=name_like, name_not_like=name_not_like, description=description, description_like=description_like, priority=priority, max_priority=max_priority, min_priority=min_priority, due_date=due_date, due_date_expression=due_date_expression, due_after=due_after, due_after_expression=due_after_expression, due_before=due_before, due_before_expression=due_before_expression, follow_up_date=follow_up_date, follow_up_date_expression=follow_up_date_expression, follow_up_after=follow_up_after, follow_up_after_expression=follow_up_after_expression, follow_up_before=follow_up_before, follow_up_before_expression=follow_up_before_expression, follow_up_before_or_not_existent=follow_up_before_or_not_existent, follow_up_before_or_not_existent_expression=follow_up_before_or_not_existent_expression, created_on=created_on, created_on_expression=created_on_expression, created_after=created_after, created_after_expression=created_after_expression, created_before=created_before, created_before_expression=created_before_expression, delegation_state=delegation_state, candidate_groups=candidate_groups, candidate_groups_expression=candidate_groups_expression, with_candidate_groups=with_candidate_groups, without_candidate_groups=without_candidate_groups, with_candidate_users=with_candidate_users, without_candidate_users=without_candidate_users, active=active, suspended=suspended, task_variables=task_variables, process_variables=process_variables, case_instance_variables=case_instance_variables, variable_names_ignore_case=variable_names_ignore_case, variable_values_ignore_case=variable_values_ignore_case, parent_task_id=parent_task_id, sort_by=sort_by, sort_order=sort_order, first_result=first_result, max_results=max_results)



Queries for tasks that fulfill a given filter. The size of the result set can be retrieved by using the Get Task Count method.  **Security Consideration:** There are several query parameters (such as assigneeExpression) for specifying an EL expression. These are disabled by default to prevent remote code execution. See the section on [security considerations](https://docs.camunda.org/manual/7.13/user-guide/process-engine/securing-custom-code/) for custom code in the user guide for details.

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
    api_instance = openapi_client.TaskApi(api_client)
    process_instance_id = 'process_instance_id_example' # str | Restrict to tasks that belong to process instances with the given id. (optional)
process_instance_id_in = 'process_instance_id_in_example' # str | Restrict to tasks that belong to process instances with the given ids. (optional)
process_instance_business_key = 'process_instance_business_key_example' # str | Restrict to tasks that belong to process instances with the given business key. (optional)
process_instance_business_key_expression = 'process_instance_business_key_expression_example' # str | Restrict to tasks that belong to process instances with the given business key which  is described by an expression. See the  [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. (optional)
process_instance_business_key_in = 'process_instance_business_key_in_example' # str | Restrict to tasks that belong to process instances with one of the give business keys.  The keys need to be in a comma-separated list. (optional)
process_instance_business_key_like = 'process_instance_business_key_like_example' # str | Restrict to tasks that have a process instance business key that has the parameter  value as a substring. (optional)
process_instance_business_key_like_expression = 'process_instance_business_key_like_expression_example' # str | Restrict to tasks that have a process instance business key that has the parameter  value as a substring and is described by an expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions)  for more information on available functions. (optional)
process_definition_id = 'process_definition_id_example' # str | Restrict to tasks that belong to a process definition with the given id. (optional)
process_definition_key = 'process_definition_key_example' # str | Restrict to tasks that belong to a process definition with the given key. (optional)
process_definition_key_in = 'process_definition_key_in_example' # str | Restrict to tasks that belong to a process definition with one of the given keys. The  keys need to be in a comma-separated list. (optional)
process_definition_name = 'process_definition_name_example' # str | Restrict to tasks that belong to a process definition with the given name. (optional)
process_definition_name_like = 'process_definition_name_like_example' # str | Restrict to tasks that have a process definition name that has the parameter value as  a substring. (optional)
execution_id = 'execution_id_example' # str | Restrict to tasks that belong to an execution with the given id. (optional)
case_instance_id = 'case_instance_id_example' # str | Restrict to tasks that belong to case instances with the given id. (optional)
case_instance_business_key = 'case_instance_business_key_example' # str | Restrict to tasks that belong to case instances with the given business key. (optional)
case_instance_business_key_like = 'case_instance_business_key_like_example' # str | Restrict to tasks that have a case instance business key that has the parameter value  as a substring. (optional)
case_definition_id = 'case_definition_id_example' # str | Restrict to tasks that belong to a case definition with the given id. (optional)
case_definition_key = 'case_definition_key_example' # str | Restrict to tasks that belong to a case definition with the given key. (optional)
case_definition_name = 'case_definition_name_example' # str | Restrict to tasks that belong to a case definition with the given name. (optional)
case_definition_name_like = 'case_definition_name_like_example' # str | Restrict to tasks that have a case definition name that has the parameter value as a  substring. (optional)
case_execution_id = 'case_execution_id_example' # str | Restrict to tasks that belong to a case execution with the given id. (optional)
activity_instance_id_in = 'activity_instance_id_in_example' # str | Only include tasks which belong to one of the passed and comma-separated activity  instance ids. (optional)
tenant_id_in = 'tenant_id_in_example' # str | Only include tasks which belong to one of the passed and comma-separated  tenant ids. (optional)
without_tenant_id = False # bool | Only include tasks which belong to no tenant. Value may only be `true`,  as `false` is the default behavior. (optional) (default to False)
assignee = 'assignee_example' # str | Restrict to tasks that the given user is assigned to. (optional)
assignee_expression = 'assignee_expression_example' # str | Restrict to tasks that the user described by the given expression is assigned to.  See the  [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions)  for more information on available functions. (optional)
assignee_like = 'assignee_like_example' # str | Restrict to tasks that have an assignee that has the parameter  value as a substring. (optional)
assignee_like_expression = 'assignee_like_expression_example' # str | Restrict to tasks that have an assignee that has the parameter value described by the  given expression as a substring. See the  [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions)  for more information on available functions. (optional)
assignee_in = 'assignee_in_example' # str | Only include tasks which are assigned to one of the passed and  comma-separated user ids. (optional)
owner = 'owner_example' # str | Restrict to tasks that the given user owns. (optional)
owner_expression = 'owner_expression_example' # str | Restrict to tasks that the user described by the given expression owns. See the  [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions)  for more information on available functions. (optional)
candidate_group = 'candidate_group_example' # str | Only include tasks that are offered to the given group. (optional)
candidate_group_expression = 'candidate_group_expression_example' # str | Only include tasks that are offered to the group described by the given expression.  See the  [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions)  for more information on available functions. (optional)
candidate_user = 'candidate_user_example' # str | Only include tasks that are offered to the given user or to one of his groups. (optional)
candidate_user_expression = 'candidate_user_expression_example' # str | Only include tasks that are offered to the user described by the given expression.  See the  [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions)  for more information on available functions. (optional)
include_assigned_tasks = False # bool | Also include tasks that are assigned to users in candidate queries. Default is to only  include tasks that are not assigned to any user if you query by candidate user or group(s). (optional) (default to False)
involved_user = 'involved_user_example' # str | Only include tasks that the given user is involved in. A user is involved in a task if  an identity link exists between task and user (e.g., the user is the assignee). (optional)
involved_user_expression = 'involved_user_expression_example' # str | Only include tasks that the user described by the given expression is involved in. A user is involved in a task if an identity link exists between task and user (e.g., the user is the assignee). See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. (optional)
assigned = False # bool | If set to `true`, restricts the query to all tasks that are assigned. (optional) (default to False)
unassigned = False # bool | If set to `true`, restricts the query to all tasks that are unassigned. (optional) (default to False)
task_definition_key = 'task_definition_key_example' # str | Restrict to tasks that have the given key. (optional)
task_definition_key_in = 'task_definition_key_in_example' # str | Restrict to tasks that have one of the given keys. The keys need to be in a comma-separated list. (optional)
task_definition_key_like = 'task_definition_key_like_example' # str | Restrict to tasks that have a key that has the parameter value as a substring. (optional)
name = 'name_example' # str | Restrict to tasks that have the given name. (optional)
name_not_equal = 'name_not_equal_example' # str | Restrict to tasks that do not have the given name. (optional)
name_like = 'name_like_example' # str | Restrict to tasks that have a name with the given parameter value as substring. (optional)
name_not_like = 'name_not_like_example' # str | Restrict to tasks that do not have a name with the given parameter value as substring. (optional)
description = 'description_example' # str | Restrict to tasks that have the given description. (optional)
description_like = 'description_like_example' # str | Restrict to tasks that have a description that has the parameter value as a substring. (optional)
priority = 56 # int | Restrict to tasks that have the given priority. (optional)
max_priority = 56 # int | Restrict to tasks that have a lower or equal priority. (optional)
min_priority = 56 # int | Restrict to tasks that have a higher or equal priority. (optional)
due_date = 'due_date_example' # str | Restrict to tasks that are due on the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.546+0200`. (optional)
due_date_expression = 'due_date_expression_example' # str | Restrict to tasks that are due on the date described by the given expression. See the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a `java.util.Date` or `org.joda.time.DateTime` object. (optional)
due_after = 'due_after_example' # str | Restrict to tasks that are due after the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.435+0200`. (optional)
due_after_expression = 'due_after_expression_example' # str | Restrict to tasks that are due after the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a `java.util.Date` or `org.joda.time.DateTime` object. (optional)
due_before = 'due_before_example' # str | Restrict to tasks that are due before the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.243+0200`. (optional)
due_before_expression = 'due_before_expression_example' # str | Restrict to tasks that are due before the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a `java.util.Date` or `org.joda.time.DateTime` object. (optional)
follow_up_date = 'follow_up_date_example' # str | Restrict to tasks that have a followUp date on the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.342+0200`. (optional)
follow_up_date_expression = 'follow_up_date_expression_example' # str | Restrict to tasks that have a followUp date on the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a `java.util.Date` or `org.joda.time.DateTime` object. (optional)
follow_up_after = 'follow_up_after_example' # str | Restrict to tasks that have a followUp date after the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.542+0200`. (optional)
follow_up_after_expression = 'follow_up_after_expression_example' # str | Restrict to tasks that have a followUp date after the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a `java.util.Date` or `org.joda.time.DateTime` object. (optional)
follow_up_before = 'follow_up_before_example' # str | Restrict to tasks that have a followUp date before the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.234+0200`. (optional)
follow_up_before_expression = 'follow_up_before_expression_example' # str | Restrict to tasks that have a followUp date before the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a `java.util.Date` or `org.joda.time.DateTime` object. (optional)
follow_up_before_or_not_existent = 'follow_up_before_or_not_existent_example' # str | Restrict to tasks that have no followUp date or a followUp date before the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.432+0200`. The typical use case is to query all `active` tasks for a user for a given date. (optional)
follow_up_before_or_not_existent_expression = 'follow_up_before_or_not_existent_expression_example' # str | Restrict to tasks that have no followUp date or a followUp date before the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a `java.util.Date` or `org.joda.time.DateTime` object. (optional)
created_on = 'created_on_example' # str | Restrict to tasks that were created on the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.324+0200`. (optional)
created_on_expression = 'created_on_expression_example' # str | Restrict to tasks that were created on the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a `java.util.Date` or `org.joda.time.DateTime` object. (optional)
created_after = 'created_after_example' # str | Restrict to tasks that were created after the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.342+0200`. (optional)
created_after_expression = 'created_after_expression_example' # str | Restrict to tasks that were created after the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a `java.util.Date` or `org.joda.time.DateTime` object. (optional)
created_before = 'created_before_example' # str | Restrict to tasks that were created before the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.332+0200`. (optional)
created_before_expression = 'created_before_expression_example' # str | Restrict to tasks that were created before the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a `java.util.Date` or `org.joda.time.DateTime` object. (optional)
delegation_state = 'delegation_state_example' # str | Restrict to tasks that are in the given delegation state. Valid values are `PENDING` and `RESOLVED`. (optional)
candidate_groups = 'candidate_groups_example' # str | Restrict to tasks that are offered to any of the given candidate groups. Takes a comma-separated list of group names, so for example `developers,support,sales`. (optional)
candidate_groups_expression = 'candidate_groups_expression_example' # str | Restrict to tasks that are offered to any of the candidate groups described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to `java.util.List` of Strings. (optional)
with_candidate_groups = False # bool | Only include tasks which have a candidate group. Value may only be `true`, as `false` is the default behavior. (optional) (default to False)
without_candidate_groups = False # bool | Only include tasks which have no candidate group. Value may only be `true`, as `false` is the default behavior. (optional) (default to False)
with_candidate_users = False # bool | Only include tasks which have a candidate user. Value may only be `true`, as `false` is the default behavior. (optional) (default to False)
without_candidate_users = False # bool | Only include tasks which have no candidate users. Value may only be `true`, as `false` is the default behavior. (optional) (default to False)
active = False # bool | Only include active tasks. Value may only be `true`, as `false` is the default behavior. (optional) (default to False)
suspended = False # bool | Only include suspended tasks. Value may only be `true`, as `false` is the default behavior. (optional) (default to False)
task_variables = 'task_variables_example' # str | Only include tasks that have variables with certain values. Variable filtering expressions are comma-separated and are structured as follows:  A valid parameter value has the form `key_operator_value`. `key` is the variable name, `operator` is the comparison operator to be used and `value` the variable value.  **Note**: Values are always treated as String objects on server side.  Valid `operator` values are: `eq` - equal to; `neq` - not equal to; `gt` - greater than; `gteq` - greater than or equal to; `lt` - lower than; `lteq` - lower than or equal to; `like`. `key` and `value` may not contain underscore or comma characters. (optional)
process_variables = 'process_variables_example' # str | Only include tasks that belong to process instances that have variables with certain  values. Variable filtering expressions are comma-separated and are structured as follows:  A valid parameter value has the form `key_operator_value`. `key` is the variable name, `operator` is the comparison operator to be used and `value` the variable value.  **Note**: Values are always treated as String objects on server side.  Valid `operator` values are: `eq` - equal to; `neq` - not equal to; `gt` - greater than; `gteq` - greater than or equal to; `lt` - lower than; `lteq` - lower than or equal to; `like`. `key` and `value` may not contain underscore or comma characters. (optional)
case_instance_variables = 'case_instance_variables_example' # str | Only include tasks that belong to case instances that have variables with certain values. Variable filtering expressions are comma-separated and are structured as follows:  A valid parameter value has the form `key_operator_value`. `key` is the variable name, `operator` is the comparison operator to be used and `value` the variable value.  **Note**: Values are always treated as String objects on server side.  Valid `operator` values are: `eq` - equal to; `neq` - not equal to; `gt` - greater than; `gteq` - greater than or equal to; `lt` - lower than; `lteq` - lower than or equal to; `like`. `key` and `value` may not contain underscore or comma characters. (optional)
variable_names_ignore_case = False # bool | Match all variable names in this query case-insensitively. If set `variableName` and `variablename` are treated as equal. (optional) (default to False)
variable_values_ignore_case = False # bool | Match all variable values in this query case-insensitively. If set `variableValue` and `variablevalue` are treated as equal. (optional) (default to False)
parent_task_id = 'parent_task_id_example' # str | Restrict query to all tasks that are sub tasks of the given task. Takes a task id. (optional)
sort_by = 'sort_by_example' # str | Sort the results lexicographically by a given criterion. Must be used in conjunction with the sortOrder parameter. (optional)
sort_order = 'sort_order_example' # str | Sort the results in a given order. Values may be asc for ascending order or desc for descending order. Must be used in conjunction with the sortBy parameter. (optional)
first_result = 56 # int | Pagination of results. Specifies the index of the first result to return. (optional)
max_results = 56 # int | Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. (optional)

    try:
        api_response = api_instance.get_tasks(process_instance_id=process_instance_id, process_instance_id_in=process_instance_id_in, process_instance_business_key=process_instance_business_key, process_instance_business_key_expression=process_instance_business_key_expression, process_instance_business_key_in=process_instance_business_key_in, process_instance_business_key_like=process_instance_business_key_like, process_instance_business_key_like_expression=process_instance_business_key_like_expression, process_definition_id=process_definition_id, process_definition_key=process_definition_key, process_definition_key_in=process_definition_key_in, process_definition_name=process_definition_name, process_definition_name_like=process_definition_name_like, execution_id=execution_id, case_instance_id=case_instance_id, case_instance_business_key=case_instance_business_key, case_instance_business_key_like=case_instance_business_key_like, case_definition_id=case_definition_id, case_definition_key=case_definition_key, case_definition_name=case_definition_name, case_definition_name_like=case_definition_name_like, case_execution_id=case_execution_id, activity_instance_id_in=activity_instance_id_in, tenant_id_in=tenant_id_in, without_tenant_id=without_tenant_id, assignee=assignee, assignee_expression=assignee_expression, assignee_like=assignee_like, assignee_like_expression=assignee_like_expression, assignee_in=assignee_in, owner=owner, owner_expression=owner_expression, candidate_group=candidate_group, candidate_group_expression=candidate_group_expression, candidate_user=candidate_user, candidate_user_expression=candidate_user_expression, include_assigned_tasks=include_assigned_tasks, involved_user=involved_user, involved_user_expression=involved_user_expression, assigned=assigned, unassigned=unassigned, task_definition_key=task_definition_key, task_definition_key_in=task_definition_key_in, task_definition_key_like=task_definition_key_like, name=name, name_not_equal=name_not_equal, name_like=name_like, name_not_like=name_not_like, description=description, description_like=description_like, priority=priority, max_priority=max_priority, min_priority=min_priority, due_date=due_date, due_date_expression=due_date_expression, due_after=due_after, due_after_expression=due_after_expression, due_before=due_before, due_before_expression=due_before_expression, follow_up_date=follow_up_date, follow_up_date_expression=follow_up_date_expression, follow_up_after=follow_up_after, follow_up_after_expression=follow_up_after_expression, follow_up_before=follow_up_before, follow_up_before_expression=follow_up_before_expression, follow_up_before_or_not_existent=follow_up_before_or_not_existent, follow_up_before_or_not_existent_expression=follow_up_before_or_not_existent_expression, created_on=created_on, created_on_expression=created_on_expression, created_after=created_after, created_after_expression=created_after_expression, created_before=created_before, created_before_expression=created_before_expression, delegation_state=delegation_state, candidate_groups=candidate_groups, candidate_groups_expression=candidate_groups_expression, with_candidate_groups=with_candidate_groups, without_candidate_groups=without_candidate_groups, with_candidate_users=with_candidate_users, without_candidate_users=without_candidate_users, active=active, suspended=suspended, task_variables=task_variables, process_variables=process_variables, case_instance_variables=case_instance_variables, variable_names_ignore_case=variable_names_ignore_case, variable_values_ignore_case=variable_values_ignore_case, parent_task_id=parent_task_id, sort_by=sort_by, sort_order=sort_order, first_result=first_result, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskApi->get_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_instance_id** | **str**| Restrict to tasks that belong to process instances with the given id. | [optional] 
 **process_instance_id_in** | **str**| Restrict to tasks that belong to process instances with the given ids. | [optional] 
 **process_instance_business_key** | **str**| Restrict to tasks that belong to process instances with the given business key. | [optional] 
 **process_instance_business_key_expression** | **str**| Restrict to tasks that belong to process instances with the given business key which  is described by an expression. See the  [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. | [optional] 
 **process_instance_business_key_in** | **str**| Restrict to tasks that belong to process instances with one of the give business keys.  The keys need to be in a comma-separated list. | [optional] 
 **process_instance_business_key_like** | **str**| Restrict to tasks that have a process instance business key that has the parameter  value as a substring. | [optional] 
 **process_instance_business_key_like_expression** | **str**| Restrict to tasks that have a process instance business key that has the parameter  value as a substring and is described by an expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions)  for more information on available functions. | [optional] 
 **process_definition_id** | **str**| Restrict to tasks that belong to a process definition with the given id. | [optional] 
 **process_definition_key** | **str**| Restrict to tasks that belong to a process definition with the given key. | [optional] 
 **process_definition_key_in** | **str**| Restrict to tasks that belong to a process definition with one of the given keys. The  keys need to be in a comma-separated list. | [optional] 
 **process_definition_name** | **str**| Restrict to tasks that belong to a process definition with the given name. | [optional] 
 **process_definition_name_like** | **str**| Restrict to tasks that have a process definition name that has the parameter value as  a substring. | [optional] 
 **execution_id** | **str**| Restrict to tasks that belong to an execution with the given id. | [optional] 
 **case_instance_id** | **str**| Restrict to tasks that belong to case instances with the given id. | [optional] 
 **case_instance_business_key** | **str**| Restrict to tasks that belong to case instances with the given business key. | [optional] 
 **case_instance_business_key_like** | **str**| Restrict to tasks that have a case instance business key that has the parameter value  as a substring. | [optional] 
 **case_definition_id** | **str**| Restrict to tasks that belong to a case definition with the given id. | [optional] 
 **case_definition_key** | **str**| Restrict to tasks that belong to a case definition with the given key. | [optional] 
 **case_definition_name** | **str**| Restrict to tasks that belong to a case definition with the given name. | [optional] 
 **case_definition_name_like** | **str**| Restrict to tasks that have a case definition name that has the parameter value as a  substring. | [optional] 
 **case_execution_id** | **str**| Restrict to tasks that belong to a case execution with the given id. | [optional] 
 **activity_instance_id_in** | **str**| Only include tasks which belong to one of the passed and comma-separated activity  instance ids. | [optional] 
 **tenant_id_in** | **str**| Only include tasks which belong to one of the passed and comma-separated  tenant ids. | [optional] 
 **without_tenant_id** | **bool**| Only include tasks which belong to no tenant. Value may only be &#x60;true&#x60;,  as &#x60;false&#x60; is the default behavior. | [optional] [default to False]
 **assignee** | **str**| Restrict to tasks that the given user is assigned to. | [optional] 
 **assignee_expression** | **str**| Restrict to tasks that the user described by the given expression is assigned to.  See the  [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions)  for more information on available functions. | [optional] 
 **assignee_like** | **str**| Restrict to tasks that have an assignee that has the parameter  value as a substring. | [optional] 
 **assignee_like_expression** | **str**| Restrict to tasks that have an assignee that has the parameter value described by the  given expression as a substring. See the  [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions)  for more information on available functions. | [optional] 
 **assignee_in** | **str**| Only include tasks which are assigned to one of the passed and  comma-separated user ids. | [optional] 
 **owner** | **str**| Restrict to tasks that the given user owns. | [optional] 
 **owner_expression** | **str**| Restrict to tasks that the user described by the given expression owns. See the  [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions)  for more information on available functions. | [optional] 
 **candidate_group** | **str**| Only include tasks that are offered to the given group. | [optional] 
 **candidate_group_expression** | **str**| Only include tasks that are offered to the group described by the given expression.  See the  [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions)  for more information on available functions. | [optional] 
 **candidate_user** | **str**| Only include tasks that are offered to the given user or to one of his groups. | [optional] 
 **candidate_user_expression** | **str**| Only include tasks that are offered to the user described by the given expression.  See the  [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions)  for more information on available functions. | [optional] 
 **include_assigned_tasks** | **bool**| Also include tasks that are assigned to users in candidate queries. Default is to only  include tasks that are not assigned to any user if you query by candidate user or group(s). | [optional] [default to False]
 **involved_user** | **str**| Only include tasks that the given user is involved in. A user is involved in a task if  an identity link exists between task and user (e.g., the user is the assignee). | [optional] 
 **involved_user_expression** | **str**| Only include tasks that the user described by the given expression is involved in. A user is involved in a task if an identity link exists between task and user (e.g., the user is the assignee). See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. | [optional] 
 **assigned** | **bool**| If set to &#x60;true&#x60;, restricts the query to all tasks that are assigned. | [optional] [default to False]
 **unassigned** | **bool**| If set to &#x60;true&#x60;, restricts the query to all tasks that are unassigned. | [optional] [default to False]
 **task_definition_key** | **str**| Restrict to tasks that have the given key. | [optional] 
 **task_definition_key_in** | **str**| Restrict to tasks that have one of the given keys. The keys need to be in a comma-separated list. | [optional] 
 **task_definition_key_like** | **str**| Restrict to tasks that have a key that has the parameter value as a substring. | [optional] 
 **name** | **str**| Restrict to tasks that have the given name. | [optional] 
 **name_not_equal** | **str**| Restrict to tasks that do not have the given name. | [optional] 
 **name_like** | **str**| Restrict to tasks that have a name with the given parameter value as substring. | [optional] 
 **name_not_like** | **str**| Restrict to tasks that do not have a name with the given parameter value as substring. | [optional] 
 **description** | **str**| Restrict to tasks that have the given description. | [optional] 
 **description_like** | **str**| Restrict to tasks that have a description that has the parameter value as a substring. | [optional] 
 **priority** | **int**| Restrict to tasks that have the given priority. | [optional] 
 **max_priority** | **int**| Restrict to tasks that have a lower or equal priority. | [optional] 
 **min_priority** | **int**| Restrict to tasks that have a higher or equal priority. | [optional] 
 **due_date** | **str**| Restrict to tasks that are due on the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.546+0200&#x60;. | [optional] 
 **due_date_expression** | **str**| Restrict to tasks that are due on the date described by the given expression. See the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a &#x60;java.util.Date&#x60; or &#x60;org.joda.time.DateTime&#x60; object. | [optional] 
 **due_after** | **str**| Restrict to tasks that are due after the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.435+0200&#x60;. | [optional] 
 **due_after_expression** | **str**| Restrict to tasks that are due after the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a &#x60;java.util.Date&#x60; or &#x60;org.joda.time.DateTime&#x60; object. | [optional] 
 **due_before** | **str**| Restrict to tasks that are due before the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.243+0200&#x60;. | [optional] 
 **due_before_expression** | **str**| Restrict to tasks that are due before the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a &#x60;java.util.Date&#x60; or &#x60;org.joda.time.DateTime&#x60; object. | [optional] 
 **follow_up_date** | **str**| Restrict to tasks that have a followUp date on the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.342+0200&#x60;. | [optional] 
 **follow_up_date_expression** | **str**| Restrict to tasks that have a followUp date on the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a &#x60;java.util.Date&#x60; or &#x60;org.joda.time.DateTime&#x60; object. | [optional] 
 **follow_up_after** | **str**| Restrict to tasks that have a followUp date after the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.542+0200&#x60;. | [optional] 
 **follow_up_after_expression** | **str**| Restrict to tasks that have a followUp date after the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a &#x60;java.util.Date&#x60; or &#x60;org.joda.time.DateTime&#x60; object. | [optional] 
 **follow_up_before** | **str**| Restrict to tasks that have a followUp date before the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.234+0200&#x60;. | [optional] 
 **follow_up_before_expression** | **str**| Restrict to tasks that have a followUp date before the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a &#x60;java.util.Date&#x60; or &#x60;org.joda.time.DateTime&#x60; object. | [optional] 
 **follow_up_before_or_not_existent** | **str**| Restrict to tasks that have no followUp date or a followUp date before the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.432+0200&#x60;. The typical use case is to query all &#x60;active&#x60; tasks for a user for a given date. | [optional] 
 **follow_up_before_or_not_existent_expression** | **str**| Restrict to tasks that have no followUp date or a followUp date before the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a &#x60;java.util.Date&#x60; or &#x60;org.joda.time.DateTime&#x60; object. | [optional] 
 **created_on** | **str**| Restrict to tasks that were created on the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.324+0200&#x60;. | [optional] 
 **created_on_expression** | **str**| Restrict to tasks that were created on the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a &#x60;java.util.Date&#x60; or &#x60;org.joda.time.DateTime&#x60; object. | [optional] 
 **created_after** | **str**| Restrict to tasks that were created after the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.342+0200&#x60;. | [optional] 
 **created_after_expression** | **str**| Restrict to tasks that were created after the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a &#x60;java.util.Date&#x60; or &#x60;org.joda.time.DateTime&#x60; object. | [optional] 
 **created_before** | **str**| Restrict to tasks that were created before the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.332+0200&#x60;. | [optional] 
 **created_before_expression** | **str**| Restrict to tasks that were created before the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a &#x60;java.util.Date&#x60; or &#x60;org.joda.time.DateTime&#x60; object. | [optional] 
 **delegation_state** | **str**| Restrict to tasks that are in the given delegation state. Valid values are &#x60;PENDING&#x60; and &#x60;RESOLVED&#x60;. | [optional] 
 **candidate_groups** | **str**| Restrict to tasks that are offered to any of the given candidate groups. Takes a comma-separated list of group names, so for example &#x60;developers,support,sales&#x60;. | [optional] 
 **candidate_groups_expression** | **str**| Restrict to tasks that are offered to any of the candidate groups described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to &#x60;java.util.List&#x60; of Strings. | [optional] 
 **with_candidate_groups** | **bool**| Only include tasks which have a candidate group. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] [default to False]
 **without_candidate_groups** | **bool**| Only include tasks which have no candidate group. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] [default to False]
 **with_candidate_users** | **bool**| Only include tasks which have a candidate user. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] [default to False]
 **without_candidate_users** | **bool**| Only include tasks which have no candidate users. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] [default to False]
 **active** | **bool**| Only include active tasks. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] [default to False]
 **suspended** | **bool**| Only include suspended tasks. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] [default to False]
 **task_variables** | **str**| Only include tasks that have variables with certain values. Variable filtering expressions are comma-separated and are structured as follows:  A valid parameter value has the form &#x60;key_operator_value&#x60;. &#x60;key&#x60; is the variable name, &#x60;operator&#x60; is the comparison operator to be used and &#x60;value&#x60; the variable value.  **Note**: Values are always treated as String objects on server side.  Valid &#x60;operator&#x60; values are: &#x60;eq&#x60; - equal to; &#x60;neq&#x60; - not equal to; &#x60;gt&#x60; - greater than; &#x60;gteq&#x60; - greater than or equal to; &#x60;lt&#x60; - lower than; &#x60;lteq&#x60; - lower than or equal to; &#x60;like&#x60;. &#x60;key&#x60; and &#x60;value&#x60; may not contain underscore or comma characters. | [optional] 
 **process_variables** | **str**| Only include tasks that belong to process instances that have variables with certain  values. Variable filtering expressions are comma-separated and are structured as follows:  A valid parameter value has the form &#x60;key_operator_value&#x60;. &#x60;key&#x60; is the variable name, &#x60;operator&#x60; is the comparison operator to be used and &#x60;value&#x60; the variable value.  **Note**: Values are always treated as String objects on server side.  Valid &#x60;operator&#x60; values are: &#x60;eq&#x60; - equal to; &#x60;neq&#x60; - not equal to; &#x60;gt&#x60; - greater than; &#x60;gteq&#x60; - greater than or equal to; &#x60;lt&#x60; - lower than; &#x60;lteq&#x60; - lower than or equal to; &#x60;like&#x60;. &#x60;key&#x60; and &#x60;value&#x60; may not contain underscore or comma characters. | [optional] 
 **case_instance_variables** | **str**| Only include tasks that belong to case instances that have variables with certain values. Variable filtering expressions are comma-separated and are structured as follows:  A valid parameter value has the form &#x60;key_operator_value&#x60;. &#x60;key&#x60; is the variable name, &#x60;operator&#x60; is the comparison operator to be used and &#x60;value&#x60; the variable value.  **Note**: Values are always treated as String objects on server side.  Valid &#x60;operator&#x60; values are: &#x60;eq&#x60; - equal to; &#x60;neq&#x60; - not equal to; &#x60;gt&#x60; - greater than; &#x60;gteq&#x60; - greater than or equal to; &#x60;lt&#x60; - lower than; &#x60;lteq&#x60; - lower than or equal to; &#x60;like&#x60;. &#x60;key&#x60; and &#x60;value&#x60; may not contain underscore or comma characters. | [optional] 
 **variable_names_ignore_case** | **bool**| Match all variable names in this query case-insensitively. If set &#x60;variableName&#x60; and &#x60;variablename&#x60; are treated as equal. | [optional] [default to False]
 **variable_values_ignore_case** | **bool**| Match all variable values in this query case-insensitively. If set &#x60;variableValue&#x60; and &#x60;variablevalue&#x60; are treated as equal. | [optional] [default to False]
 **parent_task_id** | **str**| Restrict query to all tasks that are sub tasks of the given task. Takes a task id. | [optional] 
 **sort_by** | **str**| Sort the results lexicographically by a given criterion. Must be used in conjunction with the sortOrder parameter. | [optional] 
 **sort_order** | **str**| Sort the results in a given order. Values may be asc for ascending order or desc for descending order. Must be used in conjunction with the sortBy parameter. | [optional] 
 **first_result** | **int**| Pagination of results. Specifies the index of the first result to return. | [optional] 
 **max_results** | **int**| Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. | [optional] 

### Return type

[**list[TaskDto]**](TaskDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | Returned if some of the query parameters are invalid, for example if a &#x60;sortOrder&#x60; parameter is supplied, but no &#x60;sortBy&#x60;, or if an invalid operator for variable comparison is used. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_count**
> CountResultDto get_tasks_count(process_instance_id=process_instance_id, process_instance_id_in=process_instance_id_in, process_instance_business_key=process_instance_business_key, process_instance_business_key_expression=process_instance_business_key_expression, process_instance_business_key_in=process_instance_business_key_in, process_instance_business_key_like=process_instance_business_key_like, process_instance_business_key_like_expression=process_instance_business_key_like_expression, process_definition_id=process_definition_id, process_definition_key=process_definition_key, process_definition_key_in=process_definition_key_in, process_definition_name=process_definition_name, process_definition_name_like=process_definition_name_like, execution_id=execution_id, case_instance_id=case_instance_id, case_instance_business_key=case_instance_business_key, case_instance_business_key_like=case_instance_business_key_like, case_definition_id=case_definition_id, case_definition_key=case_definition_key, case_definition_name=case_definition_name, case_definition_name_like=case_definition_name_like, case_execution_id=case_execution_id, activity_instance_id_in=activity_instance_id_in, tenant_id_in=tenant_id_in, without_tenant_id=without_tenant_id, assignee=assignee, assignee_expression=assignee_expression, assignee_like=assignee_like, assignee_like_expression=assignee_like_expression, assignee_in=assignee_in, owner=owner, owner_expression=owner_expression, candidate_group=candidate_group, candidate_group_expression=candidate_group_expression, candidate_user=candidate_user, candidate_user_expression=candidate_user_expression, include_assigned_tasks=include_assigned_tasks, involved_user=involved_user, involved_user_expression=involved_user_expression, assigned=assigned, unassigned=unassigned, task_definition_key=task_definition_key, task_definition_key_in=task_definition_key_in, task_definition_key_like=task_definition_key_like, name=name, name_not_equal=name_not_equal, name_like=name_like, name_not_like=name_not_like, description=description, description_like=description_like, priority=priority, max_priority=max_priority, min_priority=min_priority, due_date=due_date, due_date_expression=due_date_expression, due_after=due_after, due_after_expression=due_after_expression, due_before=due_before, due_before_expression=due_before_expression, follow_up_date=follow_up_date, follow_up_date_expression=follow_up_date_expression, follow_up_after=follow_up_after, follow_up_after_expression=follow_up_after_expression, follow_up_before=follow_up_before, follow_up_before_expression=follow_up_before_expression, follow_up_before_or_not_existent=follow_up_before_or_not_existent, follow_up_before_or_not_existent_expression=follow_up_before_or_not_existent_expression, created_on=created_on, created_on_expression=created_on_expression, created_after=created_after, created_after_expression=created_after_expression, created_before=created_before, created_before_expression=created_before_expression, delegation_state=delegation_state, candidate_groups=candidate_groups, candidate_groups_expression=candidate_groups_expression, with_candidate_groups=with_candidate_groups, without_candidate_groups=without_candidate_groups, with_candidate_users=with_candidate_users, without_candidate_users=without_candidate_users, active=active, suspended=suspended, task_variables=task_variables, process_variables=process_variables, case_instance_variables=case_instance_variables, variable_names_ignore_case=variable_names_ignore_case, variable_values_ignore_case=variable_values_ignore_case, parent_task_id=parent_task_id)



Retrieves the number of tasks that fulfill a provided filter. Corresponds to the size of the result set when using the [Get Tasks](https://docs.camunda.org/manual/7.13/reference/rest/task/) method.  **Security Consideration:** There are several query parameters (such as assigneeExpression) for specifying an EL expression. These are disabled by default to prevent remote code execution. See the section on [security considerations](https://docs.camunda.org/manual/7.13/user-guide/process-engine/securing-custom-code/) for custom code in the user guide for details.

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
    api_instance = openapi_client.TaskApi(api_client)
    process_instance_id = 'process_instance_id_example' # str | Restrict to tasks that belong to process instances with the given id. (optional)
process_instance_id_in = 'process_instance_id_in_example' # str | Restrict to tasks that belong to process instances with the given ids. (optional)
process_instance_business_key = 'process_instance_business_key_example' # str | Restrict to tasks that belong to process instances with the given business key. (optional)
process_instance_business_key_expression = 'process_instance_business_key_expression_example' # str | Restrict to tasks that belong to process instances with the given business key which  is described by an expression. See the  [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. (optional)
process_instance_business_key_in = 'process_instance_business_key_in_example' # str | Restrict to tasks that belong to process instances with one of the give business keys.  The keys need to be in a comma-separated list. (optional)
process_instance_business_key_like = 'process_instance_business_key_like_example' # str | Restrict to tasks that have a process instance business key that has the parameter  value as a substring. (optional)
process_instance_business_key_like_expression = 'process_instance_business_key_like_expression_example' # str | Restrict to tasks that have a process instance business key that has the parameter  value as a substring and is described by an expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions)  for more information on available functions. (optional)
process_definition_id = 'process_definition_id_example' # str | Restrict to tasks that belong to a process definition with the given id. (optional)
process_definition_key = 'process_definition_key_example' # str | Restrict to tasks that belong to a process definition with the given key. (optional)
process_definition_key_in = 'process_definition_key_in_example' # str | Restrict to tasks that belong to a process definition with one of the given keys. The  keys need to be in a comma-separated list. (optional)
process_definition_name = 'process_definition_name_example' # str | Restrict to tasks that belong to a process definition with the given name. (optional)
process_definition_name_like = 'process_definition_name_like_example' # str | Restrict to tasks that have a process definition name that has the parameter value as  a substring. (optional)
execution_id = 'execution_id_example' # str | Restrict to tasks that belong to an execution with the given id. (optional)
case_instance_id = 'case_instance_id_example' # str | Restrict to tasks that belong to case instances with the given id. (optional)
case_instance_business_key = 'case_instance_business_key_example' # str | Restrict to tasks that belong to case instances with the given business key. (optional)
case_instance_business_key_like = 'case_instance_business_key_like_example' # str | Restrict to tasks that have a case instance business key that has the parameter value  as a substring. (optional)
case_definition_id = 'case_definition_id_example' # str | Restrict to tasks that belong to a case definition with the given id. (optional)
case_definition_key = 'case_definition_key_example' # str | Restrict to tasks that belong to a case definition with the given key. (optional)
case_definition_name = 'case_definition_name_example' # str | Restrict to tasks that belong to a case definition with the given name. (optional)
case_definition_name_like = 'case_definition_name_like_example' # str | Restrict to tasks that have a case definition name that has the parameter value as a  substring. (optional)
case_execution_id = 'case_execution_id_example' # str | Restrict to tasks that belong to a case execution with the given id. (optional)
activity_instance_id_in = 'activity_instance_id_in_example' # str | Only include tasks which belong to one of the passed and comma-separated activity  instance ids. (optional)
tenant_id_in = 'tenant_id_in_example' # str | Only include tasks which belong to one of the passed and comma-separated  tenant ids. (optional)
without_tenant_id = False # bool | Only include tasks which belong to no tenant. Value may only be `true`,  as `false` is the default behavior. (optional) (default to False)
assignee = 'assignee_example' # str | Restrict to tasks that the given user is assigned to. (optional)
assignee_expression = 'assignee_expression_example' # str | Restrict to tasks that the user described by the given expression is assigned to.  See the  [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions)  for more information on available functions. (optional)
assignee_like = 'assignee_like_example' # str | Restrict to tasks that have an assignee that has the parameter  value as a substring. (optional)
assignee_like_expression = 'assignee_like_expression_example' # str | Restrict to tasks that have an assignee that has the parameter value described by the  given expression as a substring. See the  [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions)  for more information on available functions. (optional)
assignee_in = 'assignee_in_example' # str | Only include tasks which are assigned to one of the passed and  comma-separated user ids. (optional)
owner = 'owner_example' # str | Restrict to tasks that the given user owns. (optional)
owner_expression = 'owner_expression_example' # str | Restrict to tasks that the user described by the given expression owns. See the  [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions)  for more information on available functions. (optional)
candidate_group = 'candidate_group_example' # str | Only include tasks that are offered to the given group. (optional)
candidate_group_expression = 'candidate_group_expression_example' # str | Only include tasks that are offered to the group described by the given expression.  See the  [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions)  for more information on available functions. (optional)
candidate_user = 'candidate_user_example' # str | Only include tasks that are offered to the given user or to one of his groups. (optional)
candidate_user_expression = 'candidate_user_expression_example' # str | Only include tasks that are offered to the user described by the given expression.  See the  [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions)  for more information on available functions. (optional)
include_assigned_tasks = False # bool | Also include tasks that are assigned to users in candidate queries. Default is to only  include tasks that are not assigned to any user if you query by candidate user or group(s). (optional) (default to False)
involved_user = 'involved_user_example' # str | Only include tasks that the given user is involved in. A user is involved in a task if  an identity link exists between task and user (e.g., the user is the assignee). (optional)
involved_user_expression = 'involved_user_expression_example' # str | Only include tasks that the user described by the given expression is involved in. A user is involved in a task if an identity link exists between task and user (e.g., the user is the assignee). See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. (optional)
assigned = False # bool | If set to `true`, restricts the query to all tasks that are assigned. (optional) (default to False)
unassigned = False # bool | If set to `true`, restricts the query to all tasks that are unassigned. (optional) (default to False)
task_definition_key = 'task_definition_key_example' # str | Restrict to tasks that have the given key. (optional)
task_definition_key_in = 'task_definition_key_in_example' # str | Restrict to tasks that have one of the given keys. The keys need to be in a comma-separated list. (optional)
task_definition_key_like = 'task_definition_key_like_example' # str | Restrict to tasks that have a key that has the parameter value as a substring. (optional)
name = 'name_example' # str | Restrict to tasks that have the given name. (optional)
name_not_equal = 'name_not_equal_example' # str | Restrict to tasks that do not have the given name. (optional)
name_like = 'name_like_example' # str | Restrict to tasks that have a name with the given parameter value as substring. (optional)
name_not_like = 'name_not_like_example' # str | Restrict to tasks that do not have a name with the given parameter value as substring. (optional)
description = 'description_example' # str | Restrict to tasks that have the given description. (optional)
description_like = 'description_like_example' # str | Restrict to tasks that have a description that has the parameter value as a substring. (optional)
priority = 56 # int | Restrict to tasks that have the given priority. (optional)
max_priority = 56 # int | Restrict to tasks that have a lower or equal priority. (optional)
min_priority = 56 # int | Restrict to tasks that have a higher or equal priority. (optional)
due_date = 'due_date_example' # str | Restrict to tasks that are due on the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.546+0200`. (optional)
due_date_expression = 'due_date_expression_example' # str | Restrict to tasks that are due on the date described by the given expression. See the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a `java.util.Date` or `org.joda.time.DateTime` object. (optional)
due_after = 'due_after_example' # str | Restrict to tasks that are due after the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.435+0200`. (optional)
due_after_expression = 'due_after_expression_example' # str | Restrict to tasks that are due after the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a `java.util.Date` or `org.joda.time.DateTime` object. (optional)
due_before = 'due_before_example' # str | Restrict to tasks that are due before the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.243+0200`. (optional)
due_before_expression = 'due_before_expression_example' # str | Restrict to tasks that are due before the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a `java.util.Date` or `org.joda.time.DateTime` object. (optional)
follow_up_date = 'follow_up_date_example' # str | Restrict to tasks that have a followUp date on the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.342+0200`. (optional)
follow_up_date_expression = 'follow_up_date_expression_example' # str | Restrict to tasks that have a followUp date on the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a `java.util.Date` or `org.joda.time.DateTime` object. (optional)
follow_up_after = 'follow_up_after_example' # str | Restrict to tasks that have a followUp date after the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.542+0200`. (optional)
follow_up_after_expression = 'follow_up_after_expression_example' # str | Restrict to tasks that have a followUp date after the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a `java.util.Date` or `org.joda.time.DateTime` object. (optional)
follow_up_before = 'follow_up_before_example' # str | Restrict to tasks that have a followUp date before the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.234+0200`. (optional)
follow_up_before_expression = 'follow_up_before_expression_example' # str | Restrict to tasks that have a followUp date before the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a `java.util.Date` or `org.joda.time.DateTime` object. (optional)
follow_up_before_or_not_existent = 'follow_up_before_or_not_existent_example' # str | Restrict to tasks that have no followUp date or a followUp date before the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.432+0200`. The typical use case is to query all `active` tasks for a user for a given date. (optional)
follow_up_before_or_not_existent_expression = 'follow_up_before_or_not_existent_expression_example' # str | Restrict to tasks that have no followUp date or a followUp date before the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a `java.util.Date` or `org.joda.time.DateTime` object. (optional)
created_on = 'created_on_example' # str | Restrict to tasks that were created on the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.324+0200`. (optional)
created_on_expression = 'created_on_expression_example' # str | Restrict to tasks that were created on the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a `java.util.Date` or `org.joda.time.DateTime` object. (optional)
created_after = 'created_after_example' # str | Restrict to tasks that were created after the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.342+0200`. (optional)
created_after_expression = 'created_after_expression_example' # str | Restrict to tasks that were created after the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a `java.util.Date` or `org.joda.time.DateTime` object. (optional)
created_before = 'created_before_example' # str | Restrict to tasks that were created before the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.332+0200`. (optional)
created_before_expression = 'created_before_expression_example' # str | Restrict to tasks that were created before the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a `java.util.Date` or `org.joda.time.DateTime` object. (optional)
delegation_state = 'delegation_state_example' # str | Restrict to tasks that are in the given delegation state. Valid values are `PENDING` and `RESOLVED`. (optional)
candidate_groups = 'candidate_groups_example' # str | Restrict to tasks that are offered to any of the given candidate groups. Takes a comma-separated list of group names, so for example `developers,support,sales`. (optional)
candidate_groups_expression = 'candidate_groups_expression_example' # str | Restrict to tasks that are offered to any of the candidate groups described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to `java.util.List` of Strings. (optional)
with_candidate_groups = False # bool | Only include tasks which have a candidate group. Value may only be `true`, as `false` is the default behavior. (optional) (default to False)
without_candidate_groups = False # bool | Only include tasks which have no candidate group. Value may only be `true`, as `false` is the default behavior. (optional) (default to False)
with_candidate_users = False # bool | Only include tasks which have a candidate user. Value may only be `true`, as `false` is the default behavior. (optional) (default to False)
without_candidate_users = False # bool | Only include tasks which have no candidate users. Value may only be `true`, as `false` is the default behavior. (optional) (default to False)
active = False # bool | Only include active tasks. Value may only be `true`, as `false` is the default behavior. (optional) (default to False)
suspended = False # bool | Only include suspended tasks. Value may only be `true`, as `false` is the default behavior. (optional) (default to False)
task_variables = 'task_variables_example' # str | Only include tasks that have variables with certain values. Variable filtering expressions are comma-separated and are structured as follows:  A valid parameter value has the form `key_operator_value`. `key` is the variable name, `operator` is the comparison operator to be used and `value` the variable value.  **Note**: Values are always treated as String objects on server side.  Valid `operator` values are: `eq` - equal to; `neq` - not equal to; `gt` - greater than; `gteq` - greater than or equal to; `lt` - lower than; `lteq` - lower than or equal to; `like`. `key` and `value` may not contain underscore or comma characters. (optional)
process_variables = 'process_variables_example' # str | Only include tasks that belong to process instances that have variables with certain  values. Variable filtering expressions are comma-separated and are structured as follows:  A valid parameter value has the form `key_operator_value`. `key` is the variable name, `operator` is the comparison operator to be used and `value` the variable value.  **Note**: Values are always treated as String objects on server side.  Valid `operator` values are: `eq` - equal to; `neq` - not equal to; `gt` - greater than; `gteq` - greater than or equal to; `lt` - lower than; `lteq` - lower than or equal to; `like`. `key` and `value` may not contain underscore or comma characters. (optional)
case_instance_variables = 'case_instance_variables_example' # str | Only include tasks that belong to case instances that have variables with certain values. Variable filtering expressions are comma-separated and are structured as follows:  A valid parameter value has the form `key_operator_value`. `key` is the variable name, `operator` is the comparison operator to be used and `value` the variable value.  **Note**: Values are always treated as String objects on server side.  Valid `operator` values are: `eq` - equal to; `neq` - not equal to; `gt` - greater than; `gteq` - greater than or equal to; `lt` - lower than; `lteq` - lower than or equal to; `like`. `key` and `value` may not contain underscore or comma characters. (optional)
variable_names_ignore_case = False # bool | Match all variable names in this query case-insensitively. If set `variableName` and `variablename` are treated as equal. (optional) (default to False)
variable_values_ignore_case = False # bool | Match all variable values in this query case-insensitively. If set `variableValue` and `variablevalue` are treated as equal. (optional) (default to False)
parent_task_id = 'parent_task_id_example' # str | Restrict query to all tasks that are sub tasks of the given task. Takes a task id. (optional)

    try:
        api_response = api_instance.get_tasks_count(process_instance_id=process_instance_id, process_instance_id_in=process_instance_id_in, process_instance_business_key=process_instance_business_key, process_instance_business_key_expression=process_instance_business_key_expression, process_instance_business_key_in=process_instance_business_key_in, process_instance_business_key_like=process_instance_business_key_like, process_instance_business_key_like_expression=process_instance_business_key_like_expression, process_definition_id=process_definition_id, process_definition_key=process_definition_key, process_definition_key_in=process_definition_key_in, process_definition_name=process_definition_name, process_definition_name_like=process_definition_name_like, execution_id=execution_id, case_instance_id=case_instance_id, case_instance_business_key=case_instance_business_key, case_instance_business_key_like=case_instance_business_key_like, case_definition_id=case_definition_id, case_definition_key=case_definition_key, case_definition_name=case_definition_name, case_definition_name_like=case_definition_name_like, case_execution_id=case_execution_id, activity_instance_id_in=activity_instance_id_in, tenant_id_in=tenant_id_in, without_tenant_id=without_tenant_id, assignee=assignee, assignee_expression=assignee_expression, assignee_like=assignee_like, assignee_like_expression=assignee_like_expression, assignee_in=assignee_in, owner=owner, owner_expression=owner_expression, candidate_group=candidate_group, candidate_group_expression=candidate_group_expression, candidate_user=candidate_user, candidate_user_expression=candidate_user_expression, include_assigned_tasks=include_assigned_tasks, involved_user=involved_user, involved_user_expression=involved_user_expression, assigned=assigned, unassigned=unassigned, task_definition_key=task_definition_key, task_definition_key_in=task_definition_key_in, task_definition_key_like=task_definition_key_like, name=name, name_not_equal=name_not_equal, name_like=name_like, name_not_like=name_not_like, description=description, description_like=description_like, priority=priority, max_priority=max_priority, min_priority=min_priority, due_date=due_date, due_date_expression=due_date_expression, due_after=due_after, due_after_expression=due_after_expression, due_before=due_before, due_before_expression=due_before_expression, follow_up_date=follow_up_date, follow_up_date_expression=follow_up_date_expression, follow_up_after=follow_up_after, follow_up_after_expression=follow_up_after_expression, follow_up_before=follow_up_before, follow_up_before_expression=follow_up_before_expression, follow_up_before_or_not_existent=follow_up_before_or_not_existent, follow_up_before_or_not_existent_expression=follow_up_before_or_not_existent_expression, created_on=created_on, created_on_expression=created_on_expression, created_after=created_after, created_after_expression=created_after_expression, created_before=created_before, created_before_expression=created_before_expression, delegation_state=delegation_state, candidate_groups=candidate_groups, candidate_groups_expression=candidate_groups_expression, with_candidate_groups=with_candidate_groups, without_candidate_groups=without_candidate_groups, with_candidate_users=with_candidate_users, without_candidate_users=without_candidate_users, active=active, suspended=suspended, task_variables=task_variables, process_variables=process_variables, case_instance_variables=case_instance_variables, variable_names_ignore_case=variable_names_ignore_case, variable_values_ignore_case=variable_values_ignore_case, parent_task_id=parent_task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskApi->get_tasks_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_instance_id** | **str**| Restrict to tasks that belong to process instances with the given id. | [optional] 
 **process_instance_id_in** | **str**| Restrict to tasks that belong to process instances with the given ids. | [optional] 
 **process_instance_business_key** | **str**| Restrict to tasks that belong to process instances with the given business key. | [optional] 
 **process_instance_business_key_expression** | **str**| Restrict to tasks that belong to process instances with the given business key which  is described by an expression. See the  [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. | [optional] 
 **process_instance_business_key_in** | **str**| Restrict to tasks that belong to process instances with one of the give business keys.  The keys need to be in a comma-separated list. | [optional] 
 **process_instance_business_key_like** | **str**| Restrict to tasks that have a process instance business key that has the parameter  value as a substring. | [optional] 
 **process_instance_business_key_like_expression** | **str**| Restrict to tasks that have a process instance business key that has the parameter  value as a substring and is described by an expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions)  for more information on available functions. | [optional] 
 **process_definition_id** | **str**| Restrict to tasks that belong to a process definition with the given id. | [optional] 
 **process_definition_key** | **str**| Restrict to tasks that belong to a process definition with the given key. | [optional] 
 **process_definition_key_in** | **str**| Restrict to tasks that belong to a process definition with one of the given keys. The  keys need to be in a comma-separated list. | [optional] 
 **process_definition_name** | **str**| Restrict to tasks that belong to a process definition with the given name. | [optional] 
 **process_definition_name_like** | **str**| Restrict to tasks that have a process definition name that has the parameter value as  a substring. | [optional] 
 **execution_id** | **str**| Restrict to tasks that belong to an execution with the given id. | [optional] 
 **case_instance_id** | **str**| Restrict to tasks that belong to case instances with the given id. | [optional] 
 **case_instance_business_key** | **str**| Restrict to tasks that belong to case instances with the given business key. | [optional] 
 **case_instance_business_key_like** | **str**| Restrict to tasks that have a case instance business key that has the parameter value  as a substring. | [optional] 
 **case_definition_id** | **str**| Restrict to tasks that belong to a case definition with the given id. | [optional] 
 **case_definition_key** | **str**| Restrict to tasks that belong to a case definition with the given key. | [optional] 
 **case_definition_name** | **str**| Restrict to tasks that belong to a case definition with the given name. | [optional] 
 **case_definition_name_like** | **str**| Restrict to tasks that have a case definition name that has the parameter value as a  substring. | [optional] 
 **case_execution_id** | **str**| Restrict to tasks that belong to a case execution with the given id. | [optional] 
 **activity_instance_id_in** | **str**| Only include tasks which belong to one of the passed and comma-separated activity  instance ids. | [optional] 
 **tenant_id_in** | **str**| Only include tasks which belong to one of the passed and comma-separated  tenant ids. | [optional] 
 **without_tenant_id** | **bool**| Only include tasks which belong to no tenant. Value may only be &#x60;true&#x60;,  as &#x60;false&#x60; is the default behavior. | [optional] [default to False]
 **assignee** | **str**| Restrict to tasks that the given user is assigned to. | [optional] 
 **assignee_expression** | **str**| Restrict to tasks that the user described by the given expression is assigned to.  See the  [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions)  for more information on available functions. | [optional] 
 **assignee_like** | **str**| Restrict to tasks that have an assignee that has the parameter  value as a substring. | [optional] 
 **assignee_like_expression** | **str**| Restrict to tasks that have an assignee that has the parameter value described by the  given expression as a substring. See the  [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions)  for more information on available functions. | [optional] 
 **assignee_in** | **str**| Only include tasks which are assigned to one of the passed and  comma-separated user ids. | [optional] 
 **owner** | **str**| Restrict to tasks that the given user owns. | [optional] 
 **owner_expression** | **str**| Restrict to tasks that the user described by the given expression owns. See the  [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions)  for more information on available functions. | [optional] 
 **candidate_group** | **str**| Only include tasks that are offered to the given group. | [optional] 
 **candidate_group_expression** | **str**| Only include tasks that are offered to the group described by the given expression.  See the  [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions)  for more information on available functions. | [optional] 
 **candidate_user** | **str**| Only include tasks that are offered to the given user or to one of his groups. | [optional] 
 **candidate_user_expression** | **str**| Only include tasks that are offered to the user described by the given expression.  See the  [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions)  for more information on available functions. | [optional] 
 **include_assigned_tasks** | **bool**| Also include tasks that are assigned to users in candidate queries. Default is to only  include tasks that are not assigned to any user if you query by candidate user or group(s). | [optional] [default to False]
 **involved_user** | **str**| Only include tasks that the given user is involved in. A user is involved in a task if  an identity link exists between task and user (e.g., the user is the assignee). | [optional] 
 **involved_user_expression** | **str**| Only include tasks that the user described by the given expression is involved in. A user is involved in a task if an identity link exists between task and user (e.g., the user is the assignee). See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. | [optional] 
 **assigned** | **bool**| If set to &#x60;true&#x60;, restricts the query to all tasks that are assigned. | [optional] [default to False]
 **unassigned** | **bool**| If set to &#x60;true&#x60;, restricts the query to all tasks that are unassigned. | [optional] [default to False]
 **task_definition_key** | **str**| Restrict to tasks that have the given key. | [optional] 
 **task_definition_key_in** | **str**| Restrict to tasks that have one of the given keys. The keys need to be in a comma-separated list. | [optional] 
 **task_definition_key_like** | **str**| Restrict to tasks that have a key that has the parameter value as a substring. | [optional] 
 **name** | **str**| Restrict to tasks that have the given name. | [optional] 
 **name_not_equal** | **str**| Restrict to tasks that do not have the given name. | [optional] 
 **name_like** | **str**| Restrict to tasks that have a name with the given parameter value as substring. | [optional] 
 **name_not_like** | **str**| Restrict to tasks that do not have a name with the given parameter value as substring. | [optional] 
 **description** | **str**| Restrict to tasks that have the given description. | [optional] 
 **description_like** | **str**| Restrict to tasks that have a description that has the parameter value as a substring. | [optional] 
 **priority** | **int**| Restrict to tasks that have the given priority. | [optional] 
 **max_priority** | **int**| Restrict to tasks that have a lower or equal priority. | [optional] 
 **min_priority** | **int**| Restrict to tasks that have a higher or equal priority. | [optional] 
 **due_date** | **str**| Restrict to tasks that are due on the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.546+0200&#x60;. | [optional] 
 **due_date_expression** | **str**| Restrict to tasks that are due on the date described by the given expression. See the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a &#x60;java.util.Date&#x60; or &#x60;org.joda.time.DateTime&#x60; object. | [optional] 
 **due_after** | **str**| Restrict to tasks that are due after the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.435+0200&#x60;. | [optional] 
 **due_after_expression** | **str**| Restrict to tasks that are due after the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a &#x60;java.util.Date&#x60; or &#x60;org.joda.time.DateTime&#x60; object. | [optional] 
 **due_before** | **str**| Restrict to tasks that are due before the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.243+0200&#x60;. | [optional] 
 **due_before_expression** | **str**| Restrict to tasks that are due before the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a &#x60;java.util.Date&#x60; or &#x60;org.joda.time.DateTime&#x60; object. | [optional] 
 **follow_up_date** | **str**| Restrict to tasks that have a followUp date on the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.342+0200&#x60;. | [optional] 
 **follow_up_date_expression** | **str**| Restrict to tasks that have a followUp date on the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a &#x60;java.util.Date&#x60; or &#x60;org.joda.time.DateTime&#x60; object. | [optional] 
 **follow_up_after** | **str**| Restrict to tasks that have a followUp date after the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.542+0200&#x60;. | [optional] 
 **follow_up_after_expression** | **str**| Restrict to tasks that have a followUp date after the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a &#x60;java.util.Date&#x60; or &#x60;org.joda.time.DateTime&#x60; object. | [optional] 
 **follow_up_before** | **str**| Restrict to tasks that have a followUp date before the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.234+0200&#x60;. | [optional] 
 **follow_up_before_expression** | **str**| Restrict to tasks that have a followUp date before the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a &#x60;java.util.Date&#x60; or &#x60;org.joda.time.DateTime&#x60; object. | [optional] 
 **follow_up_before_or_not_existent** | **str**| Restrict to tasks that have no followUp date or a followUp date before the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.432+0200&#x60;. The typical use case is to query all &#x60;active&#x60; tasks for a user for a given date. | [optional] 
 **follow_up_before_or_not_existent_expression** | **str**| Restrict to tasks that have no followUp date or a followUp date before the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a &#x60;java.util.Date&#x60; or &#x60;org.joda.time.DateTime&#x60; object. | [optional] 
 **created_on** | **str**| Restrict to tasks that were created on the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.324+0200&#x60;. | [optional] 
 **created_on_expression** | **str**| Restrict to tasks that were created on the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a &#x60;java.util.Date&#x60; or &#x60;org.joda.time.DateTime&#x60; object. | [optional] 
 **created_after** | **str**| Restrict to tasks that were created after the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.342+0200&#x60;. | [optional] 
 **created_after_expression** | **str**| Restrict to tasks that were created after the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a &#x60;java.util.Date&#x60; or &#x60;org.joda.time.DateTime&#x60; object. | [optional] 
 **created_before** | **str**| Restrict to tasks that were created before the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.332+0200&#x60;. | [optional] 
 **created_before_expression** | **str**| Restrict to tasks that were created before the date described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to a &#x60;java.util.Date&#x60; or &#x60;org.joda.time.DateTime&#x60; object. | [optional] 
 **delegation_state** | **str**| Restrict to tasks that are in the given delegation state. Valid values are &#x60;PENDING&#x60; and &#x60;RESOLVED&#x60;. | [optional] 
 **candidate_groups** | **str**| Restrict to tasks that are offered to any of the given candidate groups. Takes a comma-separated list of group names, so for example &#x60;developers,support,sales&#x60;. | [optional] 
 **candidate_groups_expression** | **str**| Restrict to tasks that are offered to any of the candidate groups described by the given expression. See the [user guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/expression-language/#internal-context-functions) for more information on available functions. The expression must evaluate to &#x60;java.util.List&#x60; of Strings. | [optional] 
 **with_candidate_groups** | **bool**| Only include tasks which have a candidate group. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] [default to False]
 **without_candidate_groups** | **bool**| Only include tasks which have no candidate group. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] [default to False]
 **with_candidate_users** | **bool**| Only include tasks which have a candidate user. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] [default to False]
 **without_candidate_users** | **bool**| Only include tasks which have no candidate users. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] [default to False]
 **active** | **bool**| Only include active tasks. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] [default to False]
 **suspended** | **bool**| Only include suspended tasks. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] [default to False]
 **task_variables** | **str**| Only include tasks that have variables with certain values. Variable filtering expressions are comma-separated and are structured as follows:  A valid parameter value has the form &#x60;key_operator_value&#x60;. &#x60;key&#x60; is the variable name, &#x60;operator&#x60; is the comparison operator to be used and &#x60;value&#x60; the variable value.  **Note**: Values are always treated as String objects on server side.  Valid &#x60;operator&#x60; values are: &#x60;eq&#x60; - equal to; &#x60;neq&#x60; - not equal to; &#x60;gt&#x60; - greater than; &#x60;gteq&#x60; - greater than or equal to; &#x60;lt&#x60; - lower than; &#x60;lteq&#x60; - lower than or equal to; &#x60;like&#x60;. &#x60;key&#x60; and &#x60;value&#x60; may not contain underscore or comma characters. | [optional] 
 **process_variables** | **str**| Only include tasks that belong to process instances that have variables with certain  values. Variable filtering expressions are comma-separated and are structured as follows:  A valid parameter value has the form &#x60;key_operator_value&#x60;. &#x60;key&#x60; is the variable name, &#x60;operator&#x60; is the comparison operator to be used and &#x60;value&#x60; the variable value.  **Note**: Values are always treated as String objects on server side.  Valid &#x60;operator&#x60; values are: &#x60;eq&#x60; - equal to; &#x60;neq&#x60; - not equal to; &#x60;gt&#x60; - greater than; &#x60;gteq&#x60; - greater than or equal to; &#x60;lt&#x60; - lower than; &#x60;lteq&#x60; - lower than or equal to; &#x60;like&#x60;. &#x60;key&#x60; and &#x60;value&#x60; may not contain underscore or comma characters. | [optional] 
 **case_instance_variables** | **str**| Only include tasks that belong to case instances that have variables with certain values. Variable filtering expressions are comma-separated and are structured as follows:  A valid parameter value has the form &#x60;key_operator_value&#x60;. &#x60;key&#x60; is the variable name, &#x60;operator&#x60; is the comparison operator to be used and &#x60;value&#x60; the variable value.  **Note**: Values are always treated as String objects on server side.  Valid &#x60;operator&#x60; values are: &#x60;eq&#x60; - equal to; &#x60;neq&#x60; - not equal to; &#x60;gt&#x60; - greater than; &#x60;gteq&#x60; - greater than or equal to; &#x60;lt&#x60; - lower than; &#x60;lteq&#x60; - lower than or equal to; &#x60;like&#x60;. &#x60;key&#x60; and &#x60;value&#x60; may not contain underscore or comma characters. | [optional] 
 **variable_names_ignore_case** | **bool**| Match all variable names in this query case-insensitively. If set &#x60;variableName&#x60; and &#x60;variablename&#x60; are treated as equal. | [optional] [default to False]
 **variable_values_ignore_case** | **bool**| Match all variable values in this query case-insensitively. If set &#x60;variableValue&#x60; and &#x60;variablevalue&#x60; are treated as equal. | [optional] [default to False]
 **parent_task_id** | **str**| Restrict query to all tasks that are sub tasks of the given task. Takes a task id. | [optional] 

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

# **handle_bpmn_error**
> handle_bpmn_error(id, task_bpmn_error_dto=task_bpmn_error_dto)



Reports a business error in the context of a running task by id. The error code must be specified to identify the BPMN error handler. See the documentation for [Reporting Bpmn Error](https://docs.camunda.org/manual/7.13/reference/bpmn20/tasks/user-task/#reporting-bpmn-error) in User Tasks.

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
    api_instance = openapi_client.TaskApi(api_client)
    id = 'id_example' # str | The id of the task a BPMN error is reported for.
task_bpmn_error_dto = {"errorCode":"bpmn-error-543","errorMessage":"anErrorMessage","variables":{"aVariable":{"value":"aStringValue","type":"String"},"anotherVariable":{"value":true,"type":"Boolean"}}} # TaskBpmnErrorDto |  (optional)

    try:
        api_instance.handle_bpmn_error(id, task_bpmn_error_dto=task_bpmn_error_dto)
    except ApiException as e:
        print("Exception when calling TaskApi->handle_bpmn_error: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task a BPMN error is reported for. | 
 **task_bpmn_error_dto** | [**TaskBpmnErrorDto**](TaskBpmnErrorDto.md)|  | [optional] 

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
**403** | If the authenticated user is unauthorized to update the process instance. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Returned if the task does not exist or &lt;code&gt;errorCode&lt;/code&gt; is not presented in the request. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **handle_escalation**
> handle_escalation(id, task_escalation_dto=task_escalation_dto)



Reports an escalation in the context of a running task by id. The escalation code must be specified to identify the escalation handler. See the documentation for [Reporting Bpmn Escalation](https://docs.camunda.org/manual/7.13/reference/bpmn20/tasks/user-task/#reporting-bpmn-escalation) in User Tasks.

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
    api_instance = openapi_client.TaskApi(api_client)
    id = 'id_example' # str | The id of the task in which context a BPMN escalation is reported.
task_escalation_dto = {"escalationCode":"bpmn-escalation-432","variables":{"aVariable":{"value":"aStringValue","type":"String"},"anotherVariable":{"value":true,"type":"Boolean"}}} # TaskEscalationDto |  (optional)

    try:
        api_instance.handle_escalation(id, task_escalation_dto=task_escalation_dto)
    except ApiException as e:
        print("Exception when calling TaskApi->handle_escalation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task in which context a BPMN escalation is reported. | 
 **task_escalation_dto** | [**TaskEscalationDto**](TaskEscalationDto.md)|  | [optional] 

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
**403** | If the authenticated user is unauthorized to update the process instance. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Returned if the task does not exist or &lt;code&gt;errorCode&lt;/code&gt; is not presented in the request. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_tasks**
> list[TaskDto] query_tasks(first_result=first_result, max_results=max_results, task_query_dto=task_query_dto)



Queries for tasks that fulfill a given filter. This method is slightly more powerful than the [Get Tasks](https://docs.camunda.org/manual/7.13/reference/rest/task/get-query/) method because it allows filtering by multiple process or task variables of types `String`, `Number` or `Boolean`. The size of the result set can be retrieved by using the [Get Task Count (POST)](https://docs.camunda.org/manual/7.13/reference/rest/task/post-query-count/) method.  **Security Consideration**: There are several parameters (such as `assigneeExpression`) for specifying an EL expression. These are disabled by default to prevent remote code execution. See the section on [security considerations for custom code](https://docs.camunda.org/manual/7.13/user-guide/process-engine/securing-custom-code/) in the user guide for details.

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
    api_instance = openapi_client.TaskApi(api_client)
    first_result = 56 # int | Pagination of results. Specifies the index of the first result to return. (optional)
max_results = 56 # int | Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. (optional)
task_query_dto = {"taskVariables":[{"name":"varName","value":"varValue","operator":"eq"},{"name":"anotherVarName","value":30,"operator":"neq"}],"processInstanceBusinessKeyIn":"aBusinessKey,anotherBusinessKey","assigneeIn":"anAssignee,anotherAssignee","priority":10,"sorting":[{"sortBy":"dueDate","sortOrder":"asc"},{"sortBy":"processVariable","sortOrder":"desc","parameters":{"variable":"orderId","type":"String"}}]} # TaskQueryDto |  (optional)

    try:
        api_response = api_instance.query_tasks(first_result=first_result, max_results=max_results, task_query_dto=task_query_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskApi->query_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_result** | **int**| Pagination of results. Specifies the index of the first result to return. | [optional] 
 **max_results** | **int**| Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. | [optional] 
 **task_query_dto** | [**TaskQueryDto**](TaskQueryDto.md)|  | [optional] 

### Return type

[**list[TaskDto]**](TaskDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | Returned if some of the query parameters are invalid, for example if a &#x60;sortOrder&#x60; parameter is supplied, but no &#x60;sortBy&#x60;, or if an invalid operator for variable comparison is used. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_tasks_count**
> CountResultDto query_tasks_count(task_query_dto=task_query_dto)



Retrieves the number of tasks that fulfill the given filter. Corresponds to the size of the result set of the [Get Tasks (POST)](https://docs.camunda.org/manual/7.13/reference/rest/task/post-query/) method and takes the same parameters.  **Security Consideration**: There are several parameters (such as `assigneeExpression`) for specifying an EL expression. These are disabled by default to prevent remote code execution. See the section on [security considerations for custom code](https://docs.camunda.org/manual/7.13/user-guide/process-engine/securing-custom-code/) in the user guide for details.

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
    api_instance = openapi_client.TaskApi(api_client)
    task_query_dto = {"taskVariables":[{"name":"varName","value":"varValue","operator":"eq"},{"name":"anotherVarName","value":30,"operator":"neq"}],"processInstanceBusinessKeyIn":"aBusinessKey,anotherBusinessKey","assigneeIn":"anAssignee,anotherAssignee","priority":10,"sorting":[{"sortBy":"dueDate","sortOrder":"asc"},{"sortBy":"processVariable","sortOrder":"desc","parameters":{"variable":"orderId","type":"String"}}]} # TaskQueryDto |  (optional)

    try:
        api_response = api_instance.query_tasks_count(task_query_dto=task_query_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskApi->query_tasks_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_query_dto** | [**TaskQueryDto**](TaskQueryDto.md)|  | [optional] 

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

# **resolve**
> resolve(id, complete_task_dto=complete_task_dto)



Resolves a task and updates execution variables.  Resolving a task marks that the assignee is done with the task delegated to them, and that it can be sent back to the owner. Can only be executed when the task has been delegated. The assignee will be set to the owner, who performed the delegation.

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
    api_instance = openapi_client.TaskApi(api_client)
    id = 'id_example' # str | The id of the task to resolve.
complete_task_dto = {"variables":{"aVariable":{"value":"aStringValue"},"anotherVariable":{"value":42},"aThirdVariable":{"value":true}}} # CompleteTaskDto |  (optional)

    try:
        api_instance.resolve(id, complete_task_dto=complete_task_dto)
    except ApiException as e:
        print("Exception when calling TaskApi->resolve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to resolve. | 
 **complete_task_dto** | [**CompleteTaskDto**](CompleteTaskDto.md)|  | [optional] 

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
**400** | The variable value or type is invalid, for example if the value could not be parsed to an Integer value or the passed variable type is not supported. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**500** | If the task does not exist or the corresponding process instance could not be resumed successfully. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_assignee**
> set_assignee(id, user_id_dto=user_id_dto)



Changes the assignee of a task to a specific user.  **Note:** The difference with the [Claim Task](https://docs.camunda.org/manual/7.13/reference/rest/task/post-claim/) method is that this method does not check if the task already has a user assigned to it.

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
    api_instance = openapi_client.TaskApi(api_client)
    id = 'id_example' # str | The id of the task to set the assignee for.
user_id_dto = {"userId":"aUserId"} # UserIdDto | Provide the id of the user that will be the assignee of the task. (optional)

    try:
        api_instance.set_assignee(id, user_id_dto=user_id_dto)
    except ApiException as e:
        print("Exception when calling TaskApi->set_assignee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to set the assignee for. | 
 **user_id_dto** | [**UserIdDto**](UserIdDto.md)| Provide the id of the user that will be the assignee of the task. | [optional] 

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
**500** | Task with given id does not exist or setting the assignee was not successful. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit**
> dict(str, VariableValueDto) submit(id, complete_task_dto=complete_task_dto)



Completes a task and updates process variables using a form submit. There are two difference between this method and the `complete` method:  * If the task is in state `PENDING` - i.e., has been delegated before, it is not completed but resolved. Otherwise it will be completed. * If the task has Form Field Metadata defined, the process engine will perform backend validation for any form fields which have validators defined. See the [Generated Task Forms](https://docs.camunda.org/manual/7.13/user-guide/task-forms/_index/#generated-task-forms) section of the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/) for more information.

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
    api_instance = openapi_client.TaskApi(api_client)
    id = 'id_example' # str | The id of the task to submit the form for.
complete_task_dto = {"variables":{"aVariable":{"value":"aStringValue"},"anotherVariable":{"value":42},"aThirdVariable":{"value":true},"aFileVariable":{"value":"TG9yZW0gaXBzdW0=","type":"File","valueInfo":{"filename":"myFile.txt"}}}} # CompleteTaskDto |  (optional)

    try:
        api_response = api_instance.submit(id, complete_task_dto=complete_task_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskApi->submit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to submit the form for. | 
 **complete_task_dto** | [**CompleteTaskDto**](CompleteTaskDto.md)|  | [optional] 

### Return type

[**dict(str, VariableValueDto)**](VariableValueDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. The response contains the process variables. |  -  |
**204** | Request successful. The response contains no variables. |  -  |
**400** | The variable value or type is invalid, for example if the value could not be parsed to an Integer value or the passed variable type is not supported.  See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**500** | If the task does not exist or the corresponding process instance could not be resumed successfully.  See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unclaim**
> unclaim(id)



Resets a task's assignee. If successful, the task is not assigned to a user.

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
    api_instance = openapi_client.TaskApi(api_client)
    id = 'id_example' # str | The id of the task to unclaim.

    try:
        api_instance.unclaim(id)
    except ApiException as e:
        print("Exception when calling TaskApi->unclaim: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to unclaim. | 

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
**500** | The Task with the given id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task**
> update_task(id, task_dto=task_dto)



Updates a task.

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
    api_instance = openapi_client.TaskApi(api_client)
    id = 'id_example' # str | The id of the task to be updated.
task_dto = {"name":"My Task","description":"This have to be done very urgent","priority":30,"assignee":"peter","owner":"mary","delegationState":"PENDING","due":"2014-08-30T10:00:00.000+0200","followUp":"2014-08-25T10:00:00.000+0200","parentTaskId":"aParentTaskId","caseInstanceId":"aCaseInstanceId","tenantId":"tenantId"} # TaskDto |  (optional)

    try:
        api_instance.update_task(id, task_dto=task_dto)
    except ApiException as e:
        print("Exception when calling TaskApi->update_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to be updated. | 
 **task_dto** | [**TaskDto**](TaskDto.md)|  | [optional] 

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
**400** | Returned if a not valid &#x60;delegationState&#x60; is supplied. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | If the corresponding task cannot be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

