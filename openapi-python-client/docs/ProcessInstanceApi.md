# openapi_client.ProcessInstanceApi

All URIs are relative to *http://localhost:8080/engine-rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_async_historic_query_based**](ProcessInstanceApi.md#delete_async_historic_query_based) | **POST** /process-instance/delete-historic-query-based | 
[**delete_process_instance**](ProcessInstanceApi.md#delete_process_instance) | **DELETE** /process-instance/{id} | 
[**delete_process_instance_variable**](ProcessInstanceApi.md#delete_process_instance_variable) | **DELETE** /process-instance/{id}/variables/{varName} | 
[**delete_process_instances_async_operation**](ProcessInstanceApi.md#delete_process_instances_async_operation) | **POST** /process-instance/delete | 
[**get_activity_instance_tree**](ProcessInstanceApi.md#get_activity_instance_tree) | **GET** /process-instance/{id}/activity-instances | 
[**get_process_instance_variable**](ProcessInstanceApi.md#get_process_instance_variable) | **GET** /process-instance/{id}/variables/{varName} | 
[**get_process_instance_variable_binary**](ProcessInstanceApi.md#get_process_instance_variable_binary) | **GET** /process-instance/{id}/variables/{varName}/data | 
[**get_process_instance_variables**](ProcessInstanceApi.md#get_process_instance_variables) | **GET** /process-instance/{id}/variables | 
[**get_process_instances**](ProcessInstanceApi.md#get_process_instances) | **GET** /process-instance | 
[**get_process_instances_count**](ProcessInstanceApi.md#get_process_instances_count) | **GET** /process-instance/count | 
[**modify_process_instance**](ProcessInstanceApi.md#modify_process_instance) | **POST** /process-instance/{id}/modification | 
[**modify_process_instance_async_operation**](ProcessInstanceApi.md#modify_process_instance_async_operation) | **POST** /process-instance/{id}/modification-async | 
[**modify_process_instance_variables**](ProcessInstanceApi.md#modify_process_instance_variables) | **POST** /process-instance/{id}/variables | 
[**query_process_instances**](ProcessInstanceApi.md#query_process_instances) | **POST** /process-instance | 
[**query_process_instances_count**](ProcessInstanceApi.md#query_process_instances_count) | **POST** /process-instance/count | 
[**set_process_instance_variable**](ProcessInstanceApi.md#set_process_instance_variable) | **PUT** /process-instance/{id}/variables/{varName} | 
[**set_process_instance_variable_binary**](ProcessInstanceApi.md#set_process_instance_variable_binary) | **POST** /process-instance/{id}/variables/{varName}/data | 
[**set_retries_by_process**](ProcessInstanceApi.md#set_retries_by_process) | **POST** /process-instance/job-retries | 
[**set_retries_by_process_historic_query_based**](ProcessInstanceApi.md#set_retries_by_process_historic_query_based) | **POST** /process-instance/job-retries-historic-query-based | 
[**update_suspension_state**](ProcessInstanceApi.md#update_suspension_state) | **PUT** /process-instance/suspended | 
[**update_suspension_state_async_operation**](ProcessInstanceApi.md#update_suspension_state_async_operation) | **POST** /process-instance/suspended-async | 
[**update_suspension_state_by_id**](ProcessInstanceApi.md#update_suspension_state_by_id) | **PUT** /process-instance/{id}/suspended | 


# **delete_async_historic_query_based**
> BatchDto delete_async_historic_query_based(delete_process_instances_dto=delete_process_instances_dto)



Deletes a set of process instances asynchronously (batch) based on a historic process instance query.

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
    api_instance = openapi_client.ProcessInstanceApi(api_client)
    delete_process_instances_dto = {"deleteReason":"aReason","historicProcessInstanceQuery":{"startedBefore":"2017-04-28T11:24:37.765+0200"},"skipCustomListeners":true,"skipSubprocesses":true} # DeleteProcessInstancesDto | **Unallowed property**: `processInstanceQuery` (optional)

    try:
        api_response = api_instance.delete_async_historic_query_based(delete_process_instances_dto=delete_process_instances_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessInstanceApi->delete_async_historic_query_based: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_process_instances_dto** | [**DeleteProcessInstancesDto**](DeleteProcessInstancesDto.md)| **Unallowed property**: &#x60;processInstanceQuery&#x60; | [optional] 

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
**400** | Bad Request Returned if some of the query parameters are invalid, i.e., neither processInstanceIds, nor historicProcessInstanceQuery is present |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_process_instance**
> delete_process_instance(id, skip_custom_listeners=skip_custom_listeners, skip_io_mappings=skip_io_mappings, skip_subprocesses=skip_subprocesses, fail_if_not_exists=fail_if_not_exists)



Deletes a running process instance by id.

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
    api_instance = openapi_client.ProcessInstanceApi(api_client)
    id = 'id_example' # str | The id of the process instance to be deleted.
skip_custom_listeners = False # bool | If set to true, the custom listeners will be skipped. (optional) (default to False)
skip_io_mappings = False # bool | If set to true, the input/output mappings will be skipped. (optional) (default to False)
skip_subprocesses = False # bool | If set to true, subprocesses related to deleted processes will be skipped. (optional) (default to False)
fail_if_not_exists = True # bool | If set to false, the request will still be successful if the process id is not found. (optional) (default to True)

    try:
        api_instance.delete_process_instance(id, skip_custom_listeners=skip_custom_listeners, skip_io_mappings=skip_io_mappings, skip_subprocesses=skip_subprocesses, fail_if_not_exists=fail_if_not_exists)
    except ApiException as e:
        print("Exception when calling ProcessInstanceApi->delete_process_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process instance to be deleted. | 
 **skip_custom_listeners** | **bool**| If set to true, the custom listeners will be skipped. | [optional] [default to False]
 **skip_io_mappings** | **bool**| If set to true, the input/output mappings will be skipped. | [optional] [default to False]
 **skip_subprocesses** | **bool**| If set to true, subprocesses related to deleted processes will be skipped. | [optional] [default to False]
 **fail_if_not_exists** | **bool**| If set to false, the request will still be successful if the process id is not found. | [optional] [default to True]

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
**404** | Not found Process instance with given id does not exist.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_process_instance_variable**
> delete_process_instance_variable(id, var_name)



Deletes a variable of a process instance by id.

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
    api_instance = openapi_client.ProcessInstanceApi(api_client)
    id = 'id_example' # str | The id of the process instance to delete the variable from.
var_name = 'var_name_example' # str | The name of the variable to delete.

    try:
        api_instance.delete_process_instance_variable(id, var_name)
    except ApiException as e:
        print("Exception when calling ProcessInstanceApi->delete_process_instance_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process instance to delete the variable from. | 
 **var_name** | **str**| The name of the variable to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_process_instances_async_operation**
> BatchDto delete_process_instances_async_operation(delete_process_instances_dto=delete_process_instances_dto)



Deletes multiple process instances asynchronously (batch).

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
    api_instance = openapi_client.ProcessInstanceApi(api_client)
    delete_process_instances_dto = {"deleteReason":"aReason","processInstanceIds":["aProcess","secondProcess"],"skipCustomListeners":true,"skipSubprocesses":true} # DeleteProcessInstancesDto | **Unallowed property**: `historicProcessInstanceQuery` (optional)

    try:
        api_response = api_instance.delete_process_instances_async_operation(delete_process_instances_dto=delete_process_instances_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessInstanceApi->delete_process_instances_async_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_process_instances_dto** | [**DeleteProcessInstancesDto**](DeleteProcessInstancesDto.md)| **Unallowed property**: &#x60;historicProcessInstanceQuery&#x60; | [optional] 

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
**400** | Bad Request Returned if some of the query parameters are invalid, i.e., neither processInstanceIds, nor processInstanceQuery is present |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity_instance_tree**
> ActivityInstanceDto get_activity_instance_tree(id)



Retrieves an Activity Instance (Tree) for a given process instance by id.

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
    api_instance = openapi_client.ProcessInstanceApi(api_client)
    id = 'id_example' # str | The id of the process instance for which the activity instance should be retrieved.

    try:
        api_response = api_instance.get_activity_instance_tree(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessInstanceApi->get_activity_instance_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process instance for which the activity instance should be retrieved. | 

### Return type

[**ActivityInstanceDto**](ActivityInstanceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**500** | Process instance with given id does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_process_instance_variable**
> VariableValueDto get_process_instance_variable(id, var_name, deserialize_value=deserialize_value)



Retrieves a variable of a given process instance by id.

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
    api_instance = openapi_client.ProcessInstanceApi(api_client)
    id = 'id_example' # str | The id of the process instance to retrieve the variable for.
var_name = 'var_name_example' # str | The name of the variable to retrieve.
deserialize_value = True # bool | Determines whether serializable variable values (typically variables that store custom Java objects) should be deserialized on server side (default true).  If set to true, a serializable variable will be deserialized on server side and transformed to JSON using [Jackson's](https://github.com/FasterXML/jackson) POJO/bean property introspection feature. Note that this requires the Java classes of the variable value to be on the REST API's classpath.  If set to false, a serializable variable will be returned in its serialized format. For example, a variable that is serialized as XML will be returned as a JSON string containing XML.  Note: While true is the default value for reasons of backward compatibility, we recommend setting this parameter to false when developing web applications that are independent of the Java process applications deployed to the engine. (optional) (default to True)

    try:
        api_response = api_instance.get_process_instance_variable(id, var_name, deserialize_value=deserialize_value)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessInstanceApi->get_process_instance_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process instance to retrieve the variable for. | 
 **var_name** | **str**| The name of the variable to retrieve. | 
 **deserialize_value** | **bool**| Determines whether serializable variable values (typically variables that store custom Java objects) should be deserialized on server side (default true).  If set to true, a serializable variable will be deserialized on server side and transformed to JSON using [Jackson&#39;s](https://github.com/FasterXML/jackson) POJO/bean property introspection feature. Note that this requires the Java classes of the variable value to be on the REST API&#39;s classpath.  If set to false, a serializable variable will be returned in its serialized format. For example, a variable that is serialized as XML will be returned as a JSON string containing XML.  Note: While true is the default value for reasons of backward compatibility, we recommend setting this parameter to false when developing web applications that are independent of the Java process applications deployed to the engine. | [optional] [default to True]

### Return type

[**VariableValueDto**](VariableValueDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | Bad Request Variable with given id does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_process_instance_variable_binary**
> file get_process_instance_variable_binary(id, var_name)



Retrieves the content of a Process Variable by the Process Instance id and the Process Variable name. Applicable for byte array or file Process Variables.

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
    api_instance = openapi_client.ProcessInstanceApi(api_client)
    id = 'id_example' # str | The id of the process instance to retrieve the variable for.
var_name = 'var_name_example' # str | The name of the variable to retrieve.

    try:
        api_response = api_instance.get_process_instance_variable_binary(id, var_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessInstanceApi->get_process_instance_variable_binary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process instance to retrieve the variable for. | 
 **var_name** | **str**| The name of the variable to retrieve. | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful.         For binary variables or files without any MIME type information, a byte stream is returned.         File variables with MIME type information are returned as the saved type.         Additionally, for file variables the Content-Disposition header will be set. |  -  |
**400** | Bad Request A Process Variable with the given id exists but does not serialize as binary data. |  -  |
**404** | Not Found A Process Variable with the given id does not exist.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_process_instance_variables**
> dict(str, VariableValueDto) get_process_instance_variables(id, deserialize_value=deserialize_value)



Retrieves all variables of a given process instance by id.

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
    api_instance = openapi_client.ProcessInstanceApi(api_client)
    id = 'id_example' # str | The id of the process instance to retrieve the variables from.
deserialize_value = True # bool | Determines whether serializable variable values (typically variables that store custom Java objects) should be deserialized on server side (default true).  If set to true, a serializable variable will be deserialized on server side and transformed to JSON using [Jackson's](https://github.com/FasterXML/jackson) POJO/bean property introspection feature. Note that this requires the Java classes of the variable value to be on the REST API's classpath.  If set to false, a serializable variable will be returned in its serialized format. For example, a variable that is serialized as XML will be returned as a JSON string containing XML.  Note: While true is the default value for reasons of backward compatibility, we recommend setting this parameter to false when developing web applications that are independent of the Java process applications deployed to the engine. (optional) (default to True)

    try:
        api_response = api_instance.get_process_instance_variables(id, deserialize_value=deserialize_value)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessInstanceApi->get_process_instance_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process instance to retrieve the variables from. | 
 **deserialize_value** | **bool**| Determines whether serializable variable values (typically variables that store custom Java objects) should be deserialized on server side (default true).  If set to true, a serializable variable will be deserialized on server side and transformed to JSON using [Jackson&#39;s](https://github.com/FasterXML/jackson) POJO/bean property introspection feature. Note that this requires the Java classes of the variable value to be on the REST API&#39;s classpath.  If set to false, a serializable variable will be returned in its serialized format. For example, a variable that is serialized as XML will be returned as a JSON string containing XML.  Note: While true is the default value for reasons of backward compatibility, we recommend setting this parameter to false when developing web applications that are independent of the Java process applications deployed to the engine. | [optional] [default to True]

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
**200** | Request successful. |  -  |
**500** | Process instance with given id does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_process_instances**
> list[ProcessInstanceDto] get_process_instances(sort_by=sort_by, sort_order=sort_order, first_result=first_result, max_results=max_results, process_instance_ids=process_instance_ids, business_key=business_key, business_key_like=business_key_like, case_instance_id=case_instance_id, process_definition_id=process_definition_id, process_definition_key=process_definition_key, process_definition_key_in=process_definition_key_in, process_definition_key_not_in=process_definition_key_not_in, deployment_id=deployment_id, super_process_instance=super_process_instance, sub_process_instance=sub_process_instance, super_case_instance=super_case_instance, sub_case_instance=sub_case_instance, active=active, suspended=suspended, with_incident=with_incident, incident_id=incident_id, incident_type=incident_type, incident_message=incident_message, incident_message_like=incident_message_like, tenant_id_in=tenant_id_in, without_tenant_id=without_tenant_id, process_definition_without_tenant_id=process_definition_without_tenant_id, activity_id_in=activity_id_in, root_process_instances=root_process_instances, leaf_process_instances=leaf_process_instances, variables=variables, variable_names_ignore_case=variable_names_ignore_case, variable_values_ignore_case=variable_values_ignore_case)



Queries for process instances that fulfill given parameters. Parameters may be static as well as dynamic runtime properties of process instances. The size of the result set can be retrieved by using the Get Instance Count method.

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
    api_instance = openapi_client.ProcessInstanceApi(api_client)
    sort_by = 'sort_by_example' # str | Sort the results lexicographically by a given criterion. Must be used in conjunction with the sortOrder parameter. (optional)
sort_order = 'sort_order_example' # str | Sort the results in a given order. Values may be asc for ascending order or desc for descending order. Must be used in conjunction with the sortBy parameter. (optional)
first_result = 56 # int | Pagination of results. Specifies the index of the first result to return. (optional)
max_results = 56 # int | Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. (optional)
process_instance_ids = 'process_instance_ids_example' # str | Filter by a comma-separated list of process instance ids. (optional)
business_key = 'business_key_example' # str | Filter by process instance business key. (optional)
business_key_like = 'business_key_like_example' # str | Filter by process instance business key that the parameter is a substring of. (optional)
case_instance_id = 'case_instance_id_example' # str | Filter by case instance id. (optional)
process_definition_id = 'process_definition_id_example' # str | Filter by the deployment the id belongs to. (optional)
process_definition_key = 'process_definition_key_example' # str | Filter by the key of the process definition the instances run on. (optional)
process_definition_key_in = 'process_definition_key_in_example' # str | Filter by a comma-separated list of process definition keys. A process instance must have one of the given process definition keys. (optional)
process_definition_key_not_in = 'process_definition_key_not_in_example' # str | Exclude instances by a comma-separated list of process definition keys. A process instance must not have one of the given process definition keys. (optional)
deployment_id = 'deployment_id_example' # str | Filter by the deployment the id belongs to. (optional)
super_process_instance = 'super_process_instance_example' # str | Restrict query to all process instances that are sub process instances of the given process instance. Takes a process instance id. (optional)
sub_process_instance = 'sub_process_instance_example' # str | Restrict query to all process instances that have the given process instance as a sub process instance. Takes a process instance id. (optional)
super_case_instance = 'super_case_instance_example' # str | Restrict query to all process instances that are sub process instances of the given case instance. Takes a case instance id. (optional)
sub_case_instance = 'sub_case_instance_example' # str | Restrict query to all process instances that have the given case instance as a sub case instance. Takes a case instance id. (optional)
active = False # bool | Only include active process instances. Value may only be true, as false is the default behavior. (optional) (default to False)
suspended = False # bool | Only include suspended process instances. Value may only be true, as false is the default behavior. (optional) (default to False)
with_incident = False # bool | Filter by presence of incidents. Selects only process instances that have an incident. (optional) (default to False)
incident_id = 'incident_id_example' # str | Filter by the incident id. (optional)
incident_type = 'incident_type_example' # str | Filter by the incident type. See the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/incidents/#incident-types) for a list of incident types. (optional)
incident_message = 'incident_message_example' # str | Filter by the incident message. Exact match. (optional)
incident_message_like = 'incident_message_like_example' # str | Filter by the incident message that the parameter is a substring of. (optional)
tenant_id_in = 'tenant_id_in_example' # str | Filter by a comma-separated list of tenant ids. A process instance must have one of the given tenant ids. (optional)
without_tenant_id = False # bool | Only include process instances which belong to no tenant. (optional) (default to False)
process_definition_without_tenant_id = False # bool | Only include process instances which process definition has no tenant id. (optional) (default to False)
activity_id_in = 'activity_id_in_example' # str | Filter by a comma-separated list of activity ids. A process instance must currently wait in a leaf activity with one of the given activity ids. (optional)
root_process_instances = False # bool | Restrict the query to all process instances that are top level process instances. (optional) (default to False)
leaf_process_instances = False # bool | Restrict the query to all process instances that are leaf instances. (i.e. don't have any sub instances). (optional) (default to False)
variables = 'variables_example' # str | Only include process instances that have variables with certain values. Variable filtering expressions are comma-separated and are structured as follows:  A valid parameter value has the form `key_operator_value`. `key` is the variable name, `operator` is the comparison operator to be used and `value` the variable value.  **Note**: Values are always treated as String objects on server side.  Valid `operator` values are: `eq` - equal to; `neq` - not equal to; `gt` - greater than; `gteq` - greater than or equal to; `lt` - lower than; `lteq` - lower than or equal to; `like`. `key` and `value` may not contain underscore or comma characters. (optional)
variable_names_ignore_case = False # bool | Match all variable names in this query case-insensitively. If set to true variableName and variablename are treated as equal. (optional) (default to False)
variable_values_ignore_case = False # bool | Match all variable values in this query case-insensitively. If set to true variableValue and variablevalue are treated as equal. (optional) (default to False)

    try:
        api_response = api_instance.get_process_instances(sort_by=sort_by, sort_order=sort_order, first_result=first_result, max_results=max_results, process_instance_ids=process_instance_ids, business_key=business_key, business_key_like=business_key_like, case_instance_id=case_instance_id, process_definition_id=process_definition_id, process_definition_key=process_definition_key, process_definition_key_in=process_definition_key_in, process_definition_key_not_in=process_definition_key_not_in, deployment_id=deployment_id, super_process_instance=super_process_instance, sub_process_instance=sub_process_instance, super_case_instance=super_case_instance, sub_case_instance=sub_case_instance, active=active, suspended=suspended, with_incident=with_incident, incident_id=incident_id, incident_type=incident_type, incident_message=incident_message, incident_message_like=incident_message_like, tenant_id_in=tenant_id_in, without_tenant_id=without_tenant_id, process_definition_without_tenant_id=process_definition_without_tenant_id, activity_id_in=activity_id_in, root_process_instances=root_process_instances, leaf_process_instances=leaf_process_instances, variables=variables, variable_names_ignore_case=variable_names_ignore_case, variable_values_ignore_case=variable_values_ignore_case)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessInstanceApi->get_process_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_by** | **str**| Sort the results lexicographically by a given criterion. Must be used in conjunction with the sortOrder parameter. | [optional] 
 **sort_order** | **str**| Sort the results in a given order. Values may be asc for ascending order or desc for descending order. Must be used in conjunction with the sortBy parameter. | [optional] 
 **first_result** | **int**| Pagination of results. Specifies the index of the first result to return. | [optional] 
 **max_results** | **int**| Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. | [optional] 
 **process_instance_ids** | **str**| Filter by a comma-separated list of process instance ids. | [optional] 
 **business_key** | **str**| Filter by process instance business key. | [optional] 
 **business_key_like** | **str**| Filter by process instance business key that the parameter is a substring of. | [optional] 
 **case_instance_id** | **str**| Filter by case instance id. | [optional] 
 **process_definition_id** | **str**| Filter by the deployment the id belongs to. | [optional] 
 **process_definition_key** | **str**| Filter by the key of the process definition the instances run on. | [optional] 
 **process_definition_key_in** | **str**| Filter by a comma-separated list of process definition keys. A process instance must have one of the given process definition keys. | [optional] 
 **process_definition_key_not_in** | **str**| Exclude instances by a comma-separated list of process definition keys. A process instance must not have one of the given process definition keys. | [optional] 
 **deployment_id** | **str**| Filter by the deployment the id belongs to. | [optional] 
 **super_process_instance** | **str**| Restrict query to all process instances that are sub process instances of the given process instance. Takes a process instance id. | [optional] 
 **sub_process_instance** | **str**| Restrict query to all process instances that have the given process instance as a sub process instance. Takes a process instance id. | [optional] 
 **super_case_instance** | **str**| Restrict query to all process instances that are sub process instances of the given case instance. Takes a case instance id. | [optional] 
 **sub_case_instance** | **str**| Restrict query to all process instances that have the given case instance as a sub case instance. Takes a case instance id. | [optional] 
 **active** | **bool**| Only include active process instances. Value may only be true, as false is the default behavior. | [optional] [default to False]
 **suspended** | **bool**| Only include suspended process instances. Value may only be true, as false is the default behavior. | [optional] [default to False]
 **with_incident** | **bool**| Filter by presence of incidents. Selects only process instances that have an incident. | [optional] [default to False]
 **incident_id** | **str**| Filter by the incident id. | [optional] 
 **incident_type** | **str**| Filter by the incident type. See the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/incidents/#incident-types) for a list of incident types. | [optional] 
 **incident_message** | **str**| Filter by the incident message. Exact match. | [optional] 
 **incident_message_like** | **str**| Filter by the incident message that the parameter is a substring of. | [optional] 
 **tenant_id_in** | **str**| Filter by a comma-separated list of tenant ids. A process instance must have one of the given tenant ids. | [optional] 
 **without_tenant_id** | **bool**| Only include process instances which belong to no tenant. | [optional] [default to False]
 **process_definition_without_tenant_id** | **bool**| Only include process instances which process definition has no tenant id. | [optional] [default to False]
 **activity_id_in** | **str**| Filter by a comma-separated list of activity ids. A process instance must currently wait in a leaf activity with one of the given activity ids. | [optional] 
 **root_process_instances** | **bool**| Restrict the query to all process instances that are top level process instances. | [optional] [default to False]
 **leaf_process_instances** | **bool**| Restrict the query to all process instances that are leaf instances. (i.e. don&#39;t have any sub instances). | [optional] [default to False]
 **variables** | **str**| Only include process instances that have variables with certain values. Variable filtering expressions are comma-separated and are structured as follows:  A valid parameter value has the form &#x60;key_operator_value&#x60;. &#x60;key&#x60; is the variable name, &#x60;operator&#x60; is the comparison operator to be used and &#x60;value&#x60; the variable value.  **Note**: Values are always treated as String objects on server side.  Valid &#x60;operator&#x60; values are: &#x60;eq&#x60; - equal to; &#x60;neq&#x60; - not equal to; &#x60;gt&#x60; - greater than; &#x60;gteq&#x60; - greater than or equal to; &#x60;lt&#x60; - lower than; &#x60;lteq&#x60; - lower than or equal to; &#x60;like&#x60;. &#x60;key&#x60; and &#x60;value&#x60; may not contain underscore or comma characters. | [optional] 
 **variable_names_ignore_case** | **bool**| Match all variable names in this query case-insensitively. If set to true variableName and variablename are treated as equal. | [optional] [default to False]
 **variable_values_ignore_case** | **bool**| Match all variable values in this query case-insensitively. If set to true variableValue and variablevalue are treated as equal. | [optional] [default to False]

### Return type

[**list[ProcessInstanceDto]**](ProcessInstanceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | Bad Request Returned if some of the query parameters are invalid, for example if a sortOrder parameter is supplied, but no sortBy, or if an invalid operator for variable comparison is used. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_process_instances_count**
> CountResultDto get_process_instances_count(process_instance_ids=process_instance_ids, business_key=business_key, business_key_like=business_key_like, case_instance_id=case_instance_id, process_definition_id=process_definition_id, process_definition_key=process_definition_key, process_definition_key_in=process_definition_key_in, process_definition_key_not_in=process_definition_key_not_in, deployment_id=deployment_id, super_process_instance=super_process_instance, sub_process_instance=sub_process_instance, super_case_instance=super_case_instance, sub_case_instance=sub_case_instance, active=active, suspended=suspended, with_incident=with_incident, incident_id=incident_id, incident_type=incident_type, incident_message=incident_message, incident_message_like=incident_message_like, tenant_id_in=tenant_id_in, without_tenant_id=without_tenant_id, process_definition_without_tenant_id=process_definition_without_tenant_id, activity_id_in=activity_id_in, root_process_instances=root_process_instances, leaf_process_instances=leaf_process_instances, variables=variables, variable_names_ignore_case=variable_names_ignore_case, variable_values_ignore_case=variable_values_ignore_case)



Queries for the number of process instances that fulfill given parameters.

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
    api_instance = openapi_client.ProcessInstanceApi(api_client)
    process_instance_ids = 'process_instance_ids_example' # str | Filter by a comma-separated list of process instance ids. (optional)
business_key = 'business_key_example' # str | Filter by process instance business key. (optional)
business_key_like = 'business_key_like_example' # str | Filter by process instance business key that the parameter is a substring of. (optional)
case_instance_id = 'case_instance_id_example' # str | Filter by case instance id. (optional)
process_definition_id = 'process_definition_id_example' # str | Filter by the deployment the id belongs to. (optional)
process_definition_key = 'process_definition_key_example' # str | Filter by the key of the process definition the instances run on. (optional)
process_definition_key_in = 'process_definition_key_in_example' # str | Filter by a comma-separated list of process definition keys. A process instance must have one of the given process definition keys. (optional)
process_definition_key_not_in = 'process_definition_key_not_in_example' # str | Exclude instances by a comma-separated list of process definition keys. A process instance must not have one of the given process definition keys. (optional)
deployment_id = 'deployment_id_example' # str | Filter by the deployment the id belongs to. (optional)
super_process_instance = 'super_process_instance_example' # str | Restrict query to all process instances that are sub process instances of the given process instance. Takes a process instance id. (optional)
sub_process_instance = 'sub_process_instance_example' # str | Restrict query to all process instances that have the given process instance as a sub process instance. Takes a process instance id. (optional)
super_case_instance = 'super_case_instance_example' # str | Restrict query to all process instances that are sub process instances of the given case instance. Takes a case instance id. (optional)
sub_case_instance = 'sub_case_instance_example' # str | Restrict query to all process instances that have the given case instance as a sub case instance. Takes a case instance id. (optional)
active = False # bool | Only include active process instances. Value may only be true, as false is the default behavior. (optional) (default to False)
suspended = False # bool | Only include suspended process instances. Value may only be true, as false is the default behavior. (optional) (default to False)
with_incident = False # bool | Filter by presence of incidents. Selects only process instances that have an incident. (optional) (default to False)
incident_id = 'incident_id_example' # str | Filter by the incident id. (optional)
incident_type = 'incident_type_example' # str | Filter by the incident type. See the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/incidents/#incident-types) for a list of incident types. (optional)
incident_message = 'incident_message_example' # str | Filter by the incident message. Exact match. (optional)
incident_message_like = 'incident_message_like_example' # str | Filter by the incident message that the parameter is a substring of. (optional)
tenant_id_in = 'tenant_id_in_example' # str | Filter by a comma-separated list of tenant ids. A process instance must have one of the given tenant ids. (optional)
without_tenant_id = False # bool | Only include process instances which belong to no tenant. (optional) (default to False)
process_definition_without_tenant_id = False # bool | Only include process instances which process definition has no tenant id. (optional) (default to False)
activity_id_in = 'activity_id_in_example' # str | Filter by a comma-separated list of activity ids. A process instance must currently wait in a leaf activity with one of the given activity ids. (optional)
root_process_instances = False # bool | Restrict the query to all process instances that are top level process instances. (optional) (default to False)
leaf_process_instances = False # bool | Restrict the query to all process instances that are leaf instances. (i.e. don't have any sub instances). (optional) (default to False)
variables = 'variables_example' # str | Only include process instances that have variables with certain values. Variable filtering expressions are comma-separated and are structured as follows:  A valid parameter value has the form `key_operator_value`. `key` is the variable name, `operator` is the comparison operator to be used and `value` the variable value.  **Note**: Values are always treated as String objects on server side.  Valid `operator` values are: `eq` - equal to; `neq` - not equal to; `gt` - greater than; `gteq` - greater than or equal to; `lt` - lower than; `lteq` - lower than or equal to; `like`. `key` and `value` may not contain underscore or comma characters. (optional)
variable_names_ignore_case = False # bool | Match all variable names in this query case-insensitively. If set to true variableName and variablename are treated as equal. (optional) (default to False)
variable_values_ignore_case = False # bool | Match all variable values in this query case-insensitively. If set to true variableValue and variablevalue are treated as equal. (optional) (default to False)

    try:
        api_response = api_instance.get_process_instances_count(process_instance_ids=process_instance_ids, business_key=business_key, business_key_like=business_key_like, case_instance_id=case_instance_id, process_definition_id=process_definition_id, process_definition_key=process_definition_key, process_definition_key_in=process_definition_key_in, process_definition_key_not_in=process_definition_key_not_in, deployment_id=deployment_id, super_process_instance=super_process_instance, sub_process_instance=sub_process_instance, super_case_instance=super_case_instance, sub_case_instance=sub_case_instance, active=active, suspended=suspended, with_incident=with_incident, incident_id=incident_id, incident_type=incident_type, incident_message=incident_message, incident_message_like=incident_message_like, tenant_id_in=tenant_id_in, without_tenant_id=without_tenant_id, process_definition_without_tenant_id=process_definition_without_tenant_id, activity_id_in=activity_id_in, root_process_instances=root_process_instances, leaf_process_instances=leaf_process_instances, variables=variables, variable_names_ignore_case=variable_names_ignore_case, variable_values_ignore_case=variable_values_ignore_case)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessInstanceApi->get_process_instances_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_instance_ids** | **str**| Filter by a comma-separated list of process instance ids. | [optional] 
 **business_key** | **str**| Filter by process instance business key. | [optional] 
 **business_key_like** | **str**| Filter by process instance business key that the parameter is a substring of. | [optional] 
 **case_instance_id** | **str**| Filter by case instance id. | [optional] 
 **process_definition_id** | **str**| Filter by the deployment the id belongs to. | [optional] 
 **process_definition_key** | **str**| Filter by the key of the process definition the instances run on. | [optional] 
 **process_definition_key_in** | **str**| Filter by a comma-separated list of process definition keys. A process instance must have one of the given process definition keys. | [optional] 
 **process_definition_key_not_in** | **str**| Exclude instances by a comma-separated list of process definition keys. A process instance must not have one of the given process definition keys. | [optional] 
 **deployment_id** | **str**| Filter by the deployment the id belongs to. | [optional] 
 **super_process_instance** | **str**| Restrict query to all process instances that are sub process instances of the given process instance. Takes a process instance id. | [optional] 
 **sub_process_instance** | **str**| Restrict query to all process instances that have the given process instance as a sub process instance. Takes a process instance id. | [optional] 
 **super_case_instance** | **str**| Restrict query to all process instances that are sub process instances of the given case instance. Takes a case instance id. | [optional] 
 **sub_case_instance** | **str**| Restrict query to all process instances that have the given case instance as a sub case instance. Takes a case instance id. | [optional] 
 **active** | **bool**| Only include active process instances. Value may only be true, as false is the default behavior. | [optional] [default to False]
 **suspended** | **bool**| Only include suspended process instances. Value may only be true, as false is the default behavior. | [optional] [default to False]
 **with_incident** | **bool**| Filter by presence of incidents. Selects only process instances that have an incident. | [optional] [default to False]
 **incident_id** | **str**| Filter by the incident id. | [optional] 
 **incident_type** | **str**| Filter by the incident type. See the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/incidents/#incident-types) for a list of incident types. | [optional] 
 **incident_message** | **str**| Filter by the incident message. Exact match. | [optional] 
 **incident_message_like** | **str**| Filter by the incident message that the parameter is a substring of. | [optional] 
 **tenant_id_in** | **str**| Filter by a comma-separated list of tenant ids. A process instance must have one of the given tenant ids. | [optional] 
 **without_tenant_id** | **bool**| Only include process instances which belong to no tenant. | [optional] [default to False]
 **process_definition_without_tenant_id** | **bool**| Only include process instances which process definition has no tenant id. | [optional] [default to False]
 **activity_id_in** | **str**| Filter by a comma-separated list of activity ids. A process instance must currently wait in a leaf activity with one of the given activity ids. | [optional] 
 **root_process_instances** | **bool**| Restrict the query to all process instances that are top level process instances. | [optional] [default to False]
 **leaf_process_instances** | **bool**| Restrict the query to all process instances that are leaf instances. (i.e. don&#39;t have any sub instances). | [optional] [default to False]
 **variables** | **str**| Only include process instances that have variables with certain values. Variable filtering expressions are comma-separated and are structured as follows:  A valid parameter value has the form &#x60;key_operator_value&#x60;. &#x60;key&#x60; is the variable name, &#x60;operator&#x60; is the comparison operator to be used and &#x60;value&#x60; the variable value.  **Note**: Values are always treated as String objects on server side.  Valid &#x60;operator&#x60; values are: &#x60;eq&#x60; - equal to; &#x60;neq&#x60; - not equal to; &#x60;gt&#x60; - greater than; &#x60;gteq&#x60; - greater than or equal to; &#x60;lt&#x60; - lower than; &#x60;lteq&#x60; - lower than or equal to; &#x60;like&#x60;. &#x60;key&#x60; and &#x60;value&#x60; may not contain underscore or comma characters. | [optional] 
 **variable_names_ignore_case** | **bool**| Match all variable names in this query case-insensitively. If set to true variableName and variablename are treated as equal. | [optional] [default to False]
 **variable_values_ignore_case** | **bool**| Match all variable values in this query case-insensitively. If set to true variableValue and variablevalue are treated as equal. | [optional] [default to False]

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
**400** | Bad Request Returned if some of the query parameters are invalid, for example an invalid operator for variable comparison is used. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_process_instance**
> modify_process_instance(id, process_instance_modification_dto=process_instance_modification_dto)



Submits a list of modification instructions to change a process instance's execution state. A modification instruction is one of the following:  * Starting execution before an activity * Starting execution after an activity on its single outgoing sequence flow * Starting execution on a specific sequence flow * Canceling an activity instance, transition instance, or all instances (activity or transition) for an activity  Instructions are executed immediately and in the order they are provided in this request's body. Variables can be provided with every starting instruction.  The exact semantics of modification can be read about in the [User guide](https://docs.camunda.org/manual/develop/user-guide/process-engine/process-instance-modification/).

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
    api_instance = openapi_client.ProcessInstanceApi(api_client)
    id = 'id_example' # str | The id of the process instance to modify.
process_instance_modification_dto = {"skipCustomListeners":true,"skipIoMappings":true,"instructions":[{"type":"startBeforeActivity","activityId":"activityId","variables":{"var":{"value":"aVariableValue","local":false,"type":"String"},"varLocal":{"value":"anotherVariableValue","local":true,"type":"String"}}},{"type":"cancel","activityInstanceId":"anActivityInstanceId"}],"annotation":"Modified to resolve an error."} # ProcessInstanceModificationDto |  (optional)

    try:
        api_instance.modify_process_instance(id, process_instance_modification_dto=process_instance_modification_dto)
    except ApiException as e:
        print("Exception when calling ProcessInstanceApi->modify_process_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process instance to modify. | 
 **process_instance_modification_dto** | [**ProcessInstanceModificationDto**](ProcessInstanceModificationDto.md)|  | [optional] 

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
**400** | At least one modification instruction misses required parameters. |  -  |
**500** | The modification cannot be performed, for example because it starts a failing activity. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_process_instance_async_operation**
> BatchDto modify_process_instance_async_operation(id, process_instance_modification_dto=process_instance_modification_dto)



Submits a list of modification instructions to change a process instance's execution state async. A modification instruction is one of the following:  * Starting execution before an activity * Starting execution after an activity on its single outgoing sequence flow * Starting execution on a specific sequence flow * Cancelling an activity instance, transition instance, or all instances (activity or transition) for an activity  Instructions are executed asynchronous and in the order they are provided in this request's body. Variables can be provided with every starting instruction.  The exact semantics of modification can be read about in the [User guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/process-instance-modification/).

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
    api_instance = openapi_client.ProcessInstanceApi(api_client)
    id = 'id_example' # str | The id of the process instance to modify.
process_instance_modification_dto = {"skipCustomListeners":true,"skipIoMappings":true,"instructions":[{"type":"startBeforeActivity","activityId":"activityId"},{"type":"cancel","activityInstanceId":"anActivityInstanceId"}],"annotation":"Modified to resolve an error."} # ProcessInstanceModificationDto |  (optional)

    try:
        api_response = api_instance.modify_process_instance_async_operation(id, process_instance_modification_dto=process_instance_modification_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessInstanceApi->modify_process_instance_async_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process instance to modify. | 
 **process_instance_modification_dto** | [**ProcessInstanceModificationDto**](ProcessInstanceModificationDto.md)|  | [optional] 

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
**400** | Bad Request At least one modification instruction misses required parameters. |  -  |
**403** | Forbidden If the user is not allowed to execute batches. See the Introduction for the error response format. |  -  |
**500** | The modification cannot be performed, for example because it starts a failing activity. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_process_instance_variables**
> modify_process_instance_variables(id, patch_variables_dto=patch_variables_dto)



Updates or deletes the variables of a process instance by id. Updates precede deletions. So, if a variable is updated AND deleted, the deletion overrides the update.

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
    api_instance = openapi_client.ProcessInstanceApi(api_client)
    id = 'id_example' # str | The id of the process instance to set variables for.
patch_variables_dto = {"modifications":{"aVariable":{"value":"aValue","type":"String"},"anotherVariable":{"value":42,"type":"Integer"}},"deletions":["aThirdVariable","FourthVariable"]} # PatchVariablesDto |  (optional)

    try:
        api_instance.modify_process_instance_variables(id, patch_variables_dto=patch_variables_dto)
    except ApiException as e:
        print("Exception when calling ProcessInstanceApi->modify_process_instance_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process instance to set variables for. | 
 **patch_variables_dto** | [**PatchVariablesDto**](PatchVariablesDto.md)|  | [optional] 

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
**400** | Bad Request The variable value or type is invalid, for example if the value could not be parsed to an Integer value or the passed variable type is not supported. |  -  |
**500** | Update or delete could not be executed, for example because the process instance does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_process_instances**
> list[ProcessInstanceDto] query_process_instances(first_result=first_result, max_results=max_results, process_instance_query_dto=process_instance_query_dto)



Queries for process instances that fulfill given parameters through a JSON object. This method is slightly more powerful than the Get Instances method because it allows filtering by multiple process variables of types `string`, `number` or `boolean`.

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
    api_instance = openapi_client.ProcessInstanceApi(api_client)
    first_result = 56 # int | Pagination of results. Specifies the index of the first result to return. (optional)
max_results = 56 # int | Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. (optional)
process_instance_query_dto = {"variables":[{"name":"myVariable","operator":"eq","value":"camunda"},{"name":"mySecondVariable","operator":"neq","value":124}],"processDefinitionId":"aProcessDefinitionId","sorting":[{"sortBy":"definitionKey","sortOrder":"asc"},{"sortBy":"instanceId","sortOrder":"desc"}]} # ProcessInstanceQueryDto |  (optional)

    try:
        api_response = api_instance.query_process_instances(first_result=first_result, max_results=max_results, process_instance_query_dto=process_instance_query_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessInstanceApi->query_process_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_result** | **int**| Pagination of results. Specifies the index of the first result to return. | [optional] 
 **max_results** | **int**| Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. | [optional] 
 **process_instance_query_dto** | [**ProcessInstanceQueryDto**](ProcessInstanceQueryDto.md)|  | [optional] 

### Return type

[**list[ProcessInstanceDto]**](ProcessInstanceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | Bad Request Returned if some of the query parameters are invalid, for example if a sortOrder parameter is supplied, but no sortBy, or if an invalid operator for variable comparison is used. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_process_instances_count**
> CountResultDto query_process_instances_count(process_instance_query_dto=process_instance_query_dto)



Queries for the number of process instances that fulfill the given parameters. This method takes the same message body as the Get Instances (POST) method and therefore it is slightly more powerful than the Get Instance Count method.

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
    api_instance = openapi_client.ProcessInstanceApi(api_client)
    process_instance_query_dto = {"variables":[{"name":"myVariable","operator":"eq","value":"camunda"},{"name":"mySecondVariable","operator":"neq","value":124}],"processDefinitionId":"aProcessDefinitionId"} # ProcessInstanceQueryDto |  (optional)

    try:
        api_response = api_instance.query_process_instances_count(process_instance_query_dto=process_instance_query_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessInstanceApi->query_process_instances_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_instance_query_dto** | [**ProcessInstanceQueryDto**](ProcessInstanceQueryDto.md)|  | [optional] 

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
**400** | Bad Request Returned if some of the query parameters are invalid, for example if an invalid operator for variable comparison is used. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_process_instance_variable**
> set_process_instance_variable(id, var_name, variable_value_dto=variable_value_dto)



Sets a variable of a given process instance by id.

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
    api_instance = openapi_client.ProcessInstanceApi(api_client)
    id = 'id_example' # str | The id of the process instance to set the variable for.
var_name = 'var_name_example' # str | The name of the variable to set.
variable_value_dto = {"value":"someValue","type":"String"} # VariableValueDto |  (optional)

    try:
        api_instance.set_process_instance_variable(id, var_name, variable_value_dto=variable_value_dto)
    except ApiException as e:
        print("Exception when calling ProcessInstanceApi->set_process_instance_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process instance to set the variable for. | 
 **var_name** | **str**| The name of the variable to set. | 
 **variable_value_dto** | [**VariableValueDto**](VariableValueDto.md)|  | [optional] 

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
**400** | Bad Request The variable value or type is invalid, for example if the value could not be parsed to an Integer value or the passed variable type is not supported. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_process_instance_variable_binary**
> set_process_instance_variable_binary(id, var_name, data=data, value_type=value_type)



Sets the serialized value for a binary variable or the binary value for a file variable.

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
    api_instance = openapi_client.ProcessInstanceApi(api_client)
    id = 'id_example' # str | The id of the process instance to retrieve the variable for.
var_name = 'var_name_example' # str | The name of the variable to retrieve.
data = '/path/to/file' # file | The binary data to be set. For File variables, this multipart can contain the filename, binary value and MIME type of the file variable to be set Only the filename is mandatory. (optional)
value_type = 'value_type_example' # str | The name of the variable type. Either Bytes for a byte array variable or File for a file variable. (optional)

    try:
        api_instance.set_process_instance_variable_binary(id, var_name, data=data, value_type=value_type)
    except ApiException as e:
        print("Exception when calling ProcessInstanceApi->set_process_instance_variable_binary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process instance to retrieve the variable for. | 
 **var_name** | **str**| The name of the variable to retrieve. | 
 **data** | **file**| The binary data to be set. For File variables, this multipart can contain the filename, binary value and MIME type of the file variable to be set Only the filename is mandatory. | [optional] 
 **value_type** | **str**| The name of the variable type. Either Bytes for a byte array variable or File for a file variable. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request successful. |  -  |
**400** | Bad Request The variable value or type is invalid, for example if no filename is set. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_retries_by_process**
> BatchDto set_retries_by_process(set_job_retries_by_process_dto=set_job_retries_by_process_dto)



Create a batch to set retries of jobs associated with given processes asynchronously.

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
    api_instance = openapi_client.ProcessInstanceApi(api_client)
    set_job_retries_by_process_dto = {"retries":5,"processInstances":["aProcess","secondProcess"],"processInstanceQuery":{"processDefinitionId":"aProcessDefinitionId"}} # SetJobRetriesByProcessDto | Please note that if both processInstances and processInstanceQuery are provided, then the resulting execution will be performed on the union of these sets. **Unallowed property**: `historicProcessInstanceQuery` (optional)

    try:
        api_response = api_instance.set_retries_by_process(set_job_retries_by_process_dto=set_job_retries_by_process_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessInstanceApi->set_retries_by_process: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_job_retries_by_process_dto** | [**SetJobRetriesByProcessDto**](SetJobRetriesByProcessDto.md)| Please note that if both processInstances and processInstanceQuery are provided, then the resulting execution will be performed on the union of these sets. **Unallowed property**: &#x60;historicProcessInstanceQuery&#x60; | [optional] 

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
**400** | Bad Request Returned if some of the query parameters are invalid, for example if neither processInstanceIds, nor processInstanceQuery is present. Or if the retry count is not specified. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_retries_by_process_historic_query_based**
> BatchDto set_retries_by_process_historic_query_based(set_job_retries_by_process_dto=set_job_retries_by_process_dto)



Create a batch to set retries of jobs asynchronously based on a historic process instance query.

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
    api_instance = openapi_client.ProcessInstanceApi(api_client)
    set_job_retries_by_process_dto = {"retries":5,"historicProcessInstanceQuery":{"startedBefore":"2017-04-28T11:24:37.769+0200"},"processInstances":["aProcess","secondProcess"]} # SetJobRetriesByProcessDto | Please note that if both processInstances and historicProcessInstanceQuery are provided, then the resulting execution will be performed on the union of these sets. **Unallowed property**: `processInstanceQuery` (optional)

    try:
        api_response = api_instance.set_retries_by_process_historic_query_based(set_job_retries_by_process_dto=set_job_retries_by_process_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessInstanceApi->set_retries_by_process_historic_query_based: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_job_retries_by_process_dto** | [**SetJobRetriesByProcessDto**](SetJobRetriesByProcessDto.md)| Please note that if both processInstances and historicProcessInstanceQuery are provided, then the resulting execution will be performed on the union of these sets. **Unallowed property**: &#x60;processInstanceQuery&#x60; | [optional] 

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
**400** | Bad Request Returned if some of the query parameters are invalid, for example if neither processInstanceIds, nor historicProcessInstanceQuery is present. Or if the retry count is not specified. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_suspension_state**
> update_suspension_state(process_instance_suspension_state_dto=process_instance_suspension_state_dto)



Activates or suspends process instances by providing certain criteria:  # Activate/Suspend Process Instance By Process Definition Id * `suspend` * `processDefinitionId`  # Activate/Suspend Process Instance By Process Definition Key  * `suspend` * `processDefinitionKey` * `processDefinitionTenantId` * `processDefinitionWithoutTenantId`  # Activate/Suspend Process Instance In Group * `suspend` * `processInstanceIds` * `processInstanceQuery` * `historicProcessInstanceQuery`

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
    api_instance = openapi_client.ProcessInstanceApi(api_client)
    process_instance_suspension_state_dto = {"processDefinitionId":"aProcDefId","suspended":true} # ProcessInstanceSuspensionStateDto |  (optional)

    try:
        api_instance.update_suspension_state(process_instance_suspension_state_dto=process_instance_suspension_state_dto)
    except ApiException as e:
        print("Exception when calling ProcessInstanceApi->update_suspension_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_instance_suspension_state_dto** | [**ProcessInstanceSuspensionStateDto**](ProcessInstanceSuspensionStateDto.md)|  | [optional] 

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
**400** | Bad Request Returned if some of the request parameters are invalid, for example if the provided processDefinitionId or processDefinitionKey parameter is null. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_suspension_state_async_operation**
> BatchDto update_suspension_state_async_operation(process_instance_suspension_state_async_dto=process_instance_suspension_state_async_dto)



Activates or suspends process instances asynchronously with a list of process instance ids, a process instance query, and/or a historical process instance query.

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
    api_instance = openapi_client.ProcessInstanceApi(api_client)
    process_instance_suspension_state_async_dto = {"processInstanceIds":["processInstanceId1","processInstanceIdN"],"suspended":true} # ProcessInstanceSuspensionStateAsyncDto |  (optional)

    try:
        api_response = api_instance.update_suspension_state_async_operation(process_instance_suspension_state_async_dto=process_instance_suspension_state_async_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessInstanceApi->update_suspension_state_async_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_instance_suspension_state_async_dto** | [**ProcessInstanceSuspensionStateAsyncDto**](ProcessInstanceSuspensionStateAsyncDto.md)|  | [optional] 

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
**400** | Bad Request Returned if some of the request parameters are invalid, for example if the provided processDefinitionId or processDefinitionKey parameter is null. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_suspension_state_by_id**
> update_suspension_state_by_id(id, suspension_state_dto=suspension_state_dto)



Activates or suspends a given process instance by id.

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
    api_instance = openapi_client.ProcessInstanceApi(api_client)
    id = 'id_example' # str | The id of the process instance to activate or suspend.
suspension_state_dto = {"suspended":true} # SuspensionStateDto |  (optional)

    try:
        api_instance.update_suspension_state_by_id(id, suspension_state_dto=suspension_state_dto)
    except ApiException as e:
        print("Exception when calling ProcessInstanceApi->update_suspension_state_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process instance to activate or suspend. | 
 **suspension_state_dto** | [**SuspensionStateDto**](SuspensionStateDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

