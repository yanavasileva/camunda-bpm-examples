# openapi_client.TaskVariableApi

All URIs are relative to *http://localhost:8080/engine-rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_task_variable**](TaskVariableApi.md#delete_task_variable) | **DELETE** /task/{id}/variables/{varName} | 
[**get_task_variable**](TaskVariableApi.md#get_task_variable) | **GET** /task/{id}/variables/{varName} | 
[**get_task_variable_binary**](TaskVariableApi.md#get_task_variable_binary) | **GET** /task/{id}/variables/{varName}/data | 
[**get_task_variables**](TaskVariableApi.md#get_task_variables) | **GET** /task/{id}/variables | 
[**modify_task_variables**](TaskVariableApi.md#modify_task_variables) | **POST** /task/{id}/variables | 
[**put_task_variable**](TaskVariableApi.md#put_task_variable) | **PUT** /task/{id}/variables/{varName} | 
[**set_binary_task_variable**](TaskVariableApi.md#set_binary_task_variable) | **POST** /task/{id}/variables/{varName}/data | 


# **delete_task_variable**
> delete_task_variable(id, var_name)



Removes a variable that is visible to a task. A variable is visible to a task if it is a local task variable or declared in a parent scope of the task. See documentation on [visiblity of variables](https://docs.camunda.org/manual/7.13/user-guide/process-engine/variables/).

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
    api_instance = openapi_client.TaskVariableApi(api_client)
    id = 'id_example' # str | The id of the task to delete the variable from.
var_name = 'var_name_example' # str | The name of the variable to be removed.

    try:
        api_instance.delete_task_variable(id, var_name)
    except ApiException as e:
        print("Exception when calling TaskVariableApi->delete_task_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to delete the variable from. | 
 **var_name** | **str**| The name of the variable to be removed. | 

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
**500** | Task id is null or does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_variable**
> VariableValueDto get_task_variable(id, var_name, deserialize_value=deserialize_value)



Retrieves a variable from the context of a given task. The variable must be visible from the task. It is visible from the task if it is a local task variable or declared in a parent scope of the task. See documentation on [visiblity of variables](https://docs.camunda.org/manual/7.13/user-guide/process-engine/variables/).

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
    api_instance = openapi_client.TaskVariableApi(api_client)
    id = 'id_example' # str | The id of the task to retrieve the variable from.
var_name = 'var_name_example' # str | The name of the variable to get.
deserialize_value = True # bool | Determines whether serializable variable values (typically variables that store custom Java objects) should be deserialized on the server side (default `true`).  If set to `true`, a serializable variable will be deserialized on server side and transformed to JSON using [Jackson's](https://github.com/FasterXML/jackson) POJO/bean property introspection feature. Note that this requires the Java classes of the variable value to be on the REST API's classpath.  If set to `false`, a serializable variable will be returned in its serialized format. For example, a variable that is serialized as XML will be returned as a JSON string containing XML.  Note: While `true` is the default value for reasons of backward compatibility, we recommend setting this parameter to `false` when developing web applications that are independent of the Java process applications deployed to the engine. (optional) (default to True)

    try:
        api_response = api_instance.get_task_variable(id, var_name, deserialize_value=deserialize_value)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskVariableApi->get_task_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to retrieve the variable from. | 
 **var_name** | **str**| The name of the variable to get. | 
 **deserialize_value** | **bool**| Determines whether serializable variable values (typically variables that store custom Java objects) should be deserialized on the server side (default &#x60;true&#x60;).  If set to &#x60;true&#x60;, a serializable variable will be deserialized on server side and transformed to JSON using [Jackson&#39;s](https://github.com/FasterXML/jackson) POJO/bean property introspection feature. Note that this requires the Java classes of the variable value to be on the REST API&#39;s classpath.  If set to &#x60;false&#x60;, a serializable variable will be returned in its serialized format. For example, a variable that is serialized as XML will be returned as a JSON string containing XML.  Note: While &#x60;true&#x60; is the default value for reasons of backward compatibility, we recommend setting this parameter to &#x60;false&#x60; when developing web applications that are independent of the Java process applications deployed to the engine. | [optional] [default to True]

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
**404** | Variable with given id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**500** | Task id is &#x60;null&#x60; or does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_variable_binary**
> file get_task_variable_binary(id, var_name)



Retrieves a binary variable from the context of a given task. Applicable for byte array and file variables. The variable must be visible from the task. It is visible from the task if it is a local task variable or declared in a parent scope of the task. See documentation on [visiblity of variables](https://docs.camunda.org/manual/7.13/user-guide/process-engine/variables/).

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
    api_instance = openapi_client.TaskVariableApi(api_client)
    id = 'id_example' # str | The id of the task to retrieve the variable for.
var_name = 'var_name_example' # str | The name of the variable to retrieve.

    try:
        api_response = api_instance.get_task_variable_binary(id, var_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskVariableApi->get_task_variable_binary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to retrieve the variable for. | 
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
**400** | Variable with given id exists but is not a binary variable.See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Variable with given id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_variables**
> dict(str, VariableValueDto) get_task_variables(id, deserialize_value=deserialize_value)



Retrieves all variables visible from the task. A variable is visible from the task if it is a local task variable or declared in a parent scope of the task. See documentation on [visiblity of variables](https://docs.camunda.org/manual/7.13/user-guide/process-engine/variables/).

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
    api_instance = openapi_client.TaskVariableApi(api_client)
    id = 'id_example' # str | The id of the task to retrieve the variables from.
deserialize_value = True # bool | Determines whether serializable variable values (typically variables that store custom Java objects) should be deserialized on the server side (default `true`). If set to `true`, a serializable variable will be deserialized on server side and transformed to JSON using [Jackson's](https://github.com/FasterXML/jackson) POJO/bean property introspection feature. Note that this requires the Java classes of the variable value to be on the REST API's classpath.  If set to `false`, a serializable variable will be returned in its serialized format. For example, a variable that is serialized as XML will be returned as a JSON string containing XML.  Note: While `true` is the default value for reasons of backward compatibility, we recommend setting this parameter to `false` when developing web applications that are independent of the Java process applications deployed to the engine. (optional) (default to True)

    try:
        api_response = api_instance.get_task_variables(id, deserialize_value=deserialize_value)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskVariableApi->get_task_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to retrieve the variables from. | 
 **deserialize_value** | **bool**| Determines whether serializable variable values (typically variables that store custom Java objects) should be deserialized on the server side (default &#x60;true&#x60;). If set to &#x60;true&#x60;, a serializable variable will be deserialized on server side and transformed to JSON using [Jackson&#39;s](https://github.com/FasterXML/jackson) POJO/bean property introspection feature. Note that this requires the Java classes of the variable value to be on the REST API&#39;s classpath.  If set to &#x60;false&#x60;, a serializable variable will be returned in its serialized format. For example, a variable that is serialized as XML will be returned as a JSON string containing XML.  Note: While &#x60;true&#x60; is the default value for reasons of backward compatibility, we recommend setting this parameter to &#x60;false&#x60; when developing web applications that are independent of the Java process applications deployed to the engine. | [optional] [default to True]

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
**500** | Task id is &#x60;null&#x60; or does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_task_variables**
> modify_task_variables(id, patch_variables_dto=patch_variables_dto)



Updates or deletes the variables visible from the task. Updates precede deletions. So, if a variable is updated AND deleted, the deletion overrides the update. A variable is visible from the task if it is a local task variable or declared in a parent scope of the task. See documentation on [visiblity of variables](https://docs.camunda.org/manual/7.13/user-guide/process-engine/variables/).

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
    api_instance = openapi_client.TaskVariableApi(api_client)
    id = 'id_example' # str | The id of the task to set variables for.
patch_variables_dto = {"modifications":{"aVariable":{"value":"aValue","type":"String"},"anotherVariable":{"value":42,"type":"Integer"}},"deletions":["aThirdVariable","FourthVariable"]} # PatchVariablesDto |  (optional)

    try:
        api_instance.modify_task_variables(id, patch_variables_dto=patch_variables_dto)
    except ApiException as e:
        print("Exception when calling TaskVariableApi->modify_task_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to set variables for. | 
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
**400** | The variable value or type is invalid. For example the value could not be parsed to an &#x60;Integer&#x60; value or the passed variable type is not supported. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**500** | Update or delete could not be executed because the task is &#x60;null&#x60; or does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_task_variable**
> put_task_variable(id, var_name, variable_value_dto=variable_value_dto)



Updates a process variable that is visible from the Task scope. A variable is visible from the task if it is a local task variable, or declared in a parent scope of the task. See the documentation on [variable scopes and visibility](https://docs.camunda.org/manual/7.13/user-guide/process-engine/variables#variable-scopes-and-variable-visibility).  **Note**: If a variable doesn't exist, the variable is created in the top-most scope visible from the task.

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
    api_instance = openapi_client.TaskVariableApi(api_client)
    id = 'id_example' # str | The id of the task to set the variable for.
var_name = 'var_name_example' # str | The name of the variable to set.
variable_value_dto = {"value":"someValue","type":"String"} # VariableValueDto |  (optional)

    try:
        api_instance.put_task_variable(id, var_name, variable_value_dto=variable_value_dto)
    except ApiException as e:
        print("Exception when calling TaskVariableApi->put_task_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to set the variable for. | 
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
**400** | The variable name, value or type is invalid, for example if the value could not be parsed to an &#x60;Integer&#x60; value or the passed variable type is not supported or a new transient variable has the name that is already persisted. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**500** | The variable name is &#x60;null&#x60;, or the Task id is &#x60;null&#x60; or does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_binary_task_variable**
> set_binary_task_variable(id, var_name, data=data, value_type=value_type)



Sets the serialized value for a binary variable or the binary value for a file variable visible from the task. A variable is visible from the task if it is a local task variable or declared in a parent scope of the task. See documentation on [visiblity of variables](https://docs.camunda.org/manual/7.13/user-guide/process-engine/variables/).

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
    api_instance = openapi_client.TaskVariableApi(api_client)
    id = 'id_example' # str | The id of the task to retrieve the variable for.
var_name = 'var_name_example' # str | The name of the variable to retrieve.
data = '/path/to/file' # file | The binary data to be set. For File variables, this multipart can contain the filename, binary value and MIME type of the file variable to be set Only the filename is mandatory. (optional)
value_type = 'value_type_example' # str | The name of the variable type. Either Bytes for a byte array variable or File for a file variable. (optional)

    try:
        api_instance.set_binary_task_variable(id, var_name, data=data, value_type=value_type)
    except ApiException as e:
        print("Exception when calling TaskVariableApi->set_binary_task_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to retrieve the variable for. | 
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
**400** | The variable value or type is invalid, for example if no filename is set. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**500** | Variable name is &#x60;null&#x60;, or the Task id is &#x60;null&#x60; or does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

