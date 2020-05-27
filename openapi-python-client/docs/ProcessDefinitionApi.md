# openapi_client.ProcessDefinitionApi

All URIs are relative to *http://localhost:8080/engine-rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_process_definition**](ProcessDefinitionApi.md#delete_process_definition) | **DELETE** /process-definition/{id} | Delete
[**delete_process_definitions_by_key**](ProcessDefinitionApi.md#delete_process_definitions_by_key) | **DELETE** /process-definition/key/{key} | Delete By Key
[**delete_process_definitions_by_key_and_tenant_id**](ProcessDefinitionApi.md#delete_process_definitions_by_key_and_tenant_id) | **DELETE** /process-definition/key/{key}/tenant/{tenant-id} | Delete By Key
[**get_activity_statistics**](ProcessDefinitionApi.md#get_activity_statistics) | **GET** /process-definition/{id}/statistics | Get Activity Instance Statistics
[**get_activity_statistics_by_process_definition_key**](ProcessDefinitionApi.md#get_activity_statistics_by_process_definition_key) | **GET** /process-definition/key/{key}/statistics | Get Activity Instance Statistics
[**get_activity_statistics_by_process_definition_key_and_tenant_id**](ProcessDefinitionApi.md#get_activity_statistics_by_process_definition_key_and_tenant_id) | **GET** /process-definition/key/{key}/tenant/{tenant-id}/statistics | Get Activity Instance Statistics
[**get_deployed_start_form**](ProcessDefinitionApi.md#get_deployed_start_form) | **GET** /process-definition/{id}/deployed-start-form | Get Deployed Start Form
[**get_deployed_start_form_by_key**](ProcessDefinitionApi.md#get_deployed_start_form_by_key) | **GET** /process-definition/key/{key}/deployed-start-form | Get Deployed Start Form
[**get_deployed_start_form_by_key_and_tenant_id**](ProcessDefinitionApi.md#get_deployed_start_form_by_key_and_tenant_id) | **GET** /process-definition/key/{key}/tenant/{tenant-id}/deployed-start-form | Get Deployed Start Form
[**get_latest_process_definition_by_tenant_id**](ProcessDefinitionApi.md#get_latest_process_definition_by_tenant_id) | **GET** /process-definition/key/{key}/tenant/{tenant-id} | Get
[**get_process_definition**](ProcessDefinitionApi.md#get_process_definition) | **GET** /process-definition/{id} | Get
[**get_process_definition_bpmn20_xml**](ProcessDefinitionApi.md#get_process_definition_bpmn20_xml) | **GET** /process-definition/{id}/xml | Get XML
[**get_process_definition_bpmn20_xml_by_key**](ProcessDefinitionApi.md#get_process_definition_bpmn20_xml_by_key) | **GET** /process-definition/key/{key}/xml | Get XML
[**get_process_definition_bpmn20_xml_by_key_and_tenant_id**](ProcessDefinitionApi.md#get_process_definition_bpmn20_xml_by_key_and_tenant_id) | **GET** /process-definition/key/{key}/tenant/{tenant-id}/xml | Get XML
[**get_process_definition_by_key**](ProcessDefinitionApi.md#get_process_definition_by_key) | **GET** /process-definition/key/{key} | Get
[**get_process_definition_diagram**](ProcessDefinitionApi.md#get_process_definition_diagram) | **GET** /process-definition/{id}/diagram | Get Diagram
[**get_process_definition_diagram_by_key**](ProcessDefinitionApi.md#get_process_definition_diagram_by_key) | **GET** /process-definition/key/{key}/diagram | Get Diagram
[**get_process_definition_diagram_by_key_and_tenant_id**](ProcessDefinitionApi.md#get_process_definition_diagram_by_key_and_tenant_id) | **GET** /process-definition/key/{key}/tenant/{tenant-id}/diagram | Get Diagram
[**get_process_definition_statistics**](ProcessDefinitionApi.md#get_process_definition_statistics) | **GET** /process-definition/statistics | Get Process Instance Statistics
[**get_process_definitions**](ProcessDefinitionApi.md#get_process_definitions) | **GET** /process-definition | Get List
[**get_process_definitions_count**](ProcessDefinitionApi.md#get_process_definitions_count) | **GET** /process-definition/count | Get List Count
[**get_rendered_start_form**](ProcessDefinitionApi.md#get_rendered_start_form) | **GET** /process-definition/{id}/rendered-form | Get Rendered Start Form
[**get_rendered_start_form_by_key**](ProcessDefinitionApi.md#get_rendered_start_form_by_key) | **GET** /process-definition/key/{key}/rendered-form | Get Rendered Start Form
[**get_rendered_start_form_by_key_and_tenant_id**](ProcessDefinitionApi.md#get_rendered_start_form_by_key_and_tenant_id) | **GET** /process-definition/key/{key}/tenant/{tenant-id}/rendered-form | Get Rendered Start Form
[**get_start_form**](ProcessDefinitionApi.md#get_start_form) | **GET** /process-definition/{id}/startForm | Get Start Form Key
[**get_start_form_by_key**](ProcessDefinitionApi.md#get_start_form_by_key) | **GET** /process-definition/key/{key}/startForm | Get Start Form Key
[**get_start_form_by_key_and_tenant_id**](ProcessDefinitionApi.md#get_start_form_by_key_and_tenant_id) | **GET** /process-definition/key/{key}/tenant/{tenant-id}/startForm | Get Start Form Key
[**get_start_form_variables**](ProcessDefinitionApi.md#get_start_form_variables) | **GET** /process-definition/{id}/form-variables | Get Start Form Variables
[**get_start_form_variables_by_key**](ProcessDefinitionApi.md#get_start_form_variables_by_key) | **GET** /process-definition/key/{key}/form-variables | Get Start Form Variables
[**get_start_form_variables_by_key_and_tenant_id**](ProcessDefinitionApi.md#get_start_form_variables_by_key_and_tenant_id) | **GET** /process-definition/key/{key}/tenant/{tenant-id}/form-variables | Get Start Form Variables
[**restart_process_instance**](ProcessDefinitionApi.md#restart_process_instance) | **POST** /process-definition/{id}/restart | Restart Process Instance
[**restart_process_instance_async_operation**](ProcessDefinitionApi.md#restart_process_instance_async_operation) | **POST** /process-definition/{id}/restart-async | Restart Process Instance Async
[**start_process_instance**](ProcessDefinitionApi.md#start_process_instance) | **POST** /process-definition/{id}/start | Start Instance
[**start_process_instance_by_key**](ProcessDefinitionApi.md#start_process_instance_by_key) | **POST** /process-definition/key/{key}/start | Start Instance
[**start_process_instance_by_key_and_tenant_id**](ProcessDefinitionApi.md#start_process_instance_by_key_and_tenant_id) | **POST** /process-definition/key/{key}/tenant/{tenant-id}/start | Start Instance
[**submit_form**](ProcessDefinitionApi.md#submit_form) | **POST** /process-definition/{id}/submit-form | Submit Start Form
[**submit_form_by_key**](ProcessDefinitionApi.md#submit_form_by_key) | **POST** /process-definition/key/{key}/submit-form | Submit Start Form
[**submit_form_by_key_and_tenant_id**](ProcessDefinitionApi.md#submit_form_by_key_and_tenant_id) | **POST** /process-definition/key/{key}/tenant/{tenant-id}/submit-form | Submit Start Form
[**update_history_time_to_live_by_process_definition_id**](ProcessDefinitionApi.md#update_history_time_to_live_by_process_definition_id) | **PUT** /process-definition/{id}/history-time-to-live | Update History Time to Live
[**update_history_time_to_live_by_process_definition_key**](ProcessDefinitionApi.md#update_history_time_to_live_by_process_definition_key) | **PUT** /process-definition/key/{key}/history-time-to-live | Update History Time to Live
[**update_history_time_to_live_by_process_definition_key_and_tenant_id**](ProcessDefinitionApi.md#update_history_time_to_live_by_process_definition_key_and_tenant_id) | **PUT** /process-definition/key/{key}/tenant/{tenant-id}/history-time-to-live | Update History Time to Live
[**update_process_definition_suspension_state**](ProcessDefinitionApi.md#update_process_definition_suspension_state) | **PUT** /process-definition/suspended | Activate/Suspend By Key
[**update_process_definition_suspension_state_by_id**](ProcessDefinitionApi.md#update_process_definition_suspension_state_by_id) | **PUT** /process-definition/{id}/suspended | Activate/Suspend By Id
[**update_process_definition_suspension_state_by_key**](ProcessDefinitionApi.md#update_process_definition_suspension_state_by_key) | **PUT** /process-definition/key/{key}/suspended | Activate/Suspend by Id
[**update_process_definition_suspension_state_by_key_and_tenant_id**](ProcessDefinitionApi.md#update_process_definition_suspension_state_by_key_and_tenant_id) | **PUT** /process-definition/key/{key}/tenant/{tenant-id}/suspended | Activate/Suspend by Id


# **delete_process_definition**
> delete_process_definition(id, cascade=cascade, skip_custom_listeners=skip_custom_listeners, skip_io_mappings=skip_io_mappings)

Delete

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    id = 'id_example' # str | The id of the process definition to be deleted.
cascade = True # bool | `true`, if all process instances, historic process instances and jobs for this process definition should be deleted. (optional)
skip_custom_listeners = False # bool | `true`, if only the built-in ExecutionListeners should be notified with the end event. (optional) (default to False)
skip_io_mappings = False # bool | A boolean value to control whether input/output mappings should be executed during deletion. `true`, if input/output mappings should not be invoked. (optional) (default to False)

    try:
        # Delete
        api_instance.delete_process_definition(id, cascade=cascade, skip_custom_listeners=skip_custom_listeners, skip_io_mappings=skip_io_mappings)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->delete_process_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process definition to be deleted. | 
 **cascade** | **bool**| &#x60;true&#x60;, if all process instances, historic process instances and jobs for this process definition should be deleted. | [optional] 
 **skip_custom_listeners** | **bool**| &#x60;true&#x60;, if only the built-in ExecutionListeners should be notified with the end event. | [optional] [default to False]
 **skip_io_mappings** | **bool**| A boolean value to control whether input/output mappings should be executed during deletion. &#x60;true&#x60;, if input/output mappings should not be invoked. | [optional] [default to False]

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
**404** | Not found Process definition with given id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_process_definitions_by_key**
> delete_process_definitions_by_key(key, cascade=cascade, skip_custom_listeners=skip_custom_listeners, skip_io_mappings=skip_io_mappings)

Delete By Key

Deletes process definitions by a given key which belong to no tenant id.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    key = 'key_example' # str | The key of the process definitions to be deleted.
cascade = True # bool | `true`, if all process instances, historic process instances and jobs for this process definition should be deleted. (optional)
skip_custom_listeners = False # bool | `true`, if only the built-in ExecutionListeners should be notified with the end event. (optional) (default to False)
skip_io_mappings = False # bool | A boolean value to control whether input/output mappings should be executed during deletion. `true`, if input/output mappings should not be invoked. (optional) (default to False)

    try:
        # Delete By Key
        api_instance.delete_process_definitions_by_key(key, cascade=cascade, skip_custom_listeners=skip_custom_listeners, skip_io_mappings=skip_io_mappings)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->delete_process_definitions_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the process definitions to be deleted. | 
 **cascade** | **bool**| &#x60;true&#x60;, if all process instances, historic process instances and jobs for this process definition should be deleted. | [optional] 
 **skip_custom_listeners** | **bool**| &#x60;true&#x60;, if only the built-in ExecutionListeners should be notified with the end event. | [optional] [default to False]
 **skip_io_mappings** | **bool**| A boolean value to control whether input/output mappings should be executed during deletion. &#x60;true&#x60;, if input/output mappings should not be invoked. | [optional] [default to False]

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
**403** | Forbidden The process definitions with the given &#x60;key&#x60; cannot be deleted due to missing permissions. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Not found Process definition with given &#x60;key&#x60; does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_process_definitions_by_key_and_tenant_id**
> delete_process_definitions_by_key_and_tenant_id(key, tenant_id, cascade=cascade, skip_custom_listeners=skip_custom_listeners, skip_io_mappings=skip_io_mappings)

Delete By Key

Deletes process definitions by a given key and which belong to a tenant id.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    key = 'key_example' # str | The key of the process definitions to be deleted.
tenant_id = 'tenant_id_example' # str | The id of the tenant the process definitions belong to.
cascade = True # bool | `true`, if all process instances, historic process instances and jobs for this process definition should be deleted. (optional)
skip_custom_listeners = False # bool | `true`, if only the built-in ExecutionListeners should be notified with the end event. (optional) (default to False)
skip_io_mappings = False # bool | A boolean value to control whether input/output mappings should be executed during deletion. `true`, if input/output mappings should not be invoked. (optional) (default to False)

    try:
        # Delete By Key
        api_instance.delete_process_definitions_by_key_and_tenant_id(key, tenant_id, cascade=cascade, skip_custom_listeners=skip_custom_listeners, skip_io_mappings=skip_io_mappings)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->delete_process_definitions_by_key_and_tenant_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the process definitions to be deleted. | 
 **tenant_id** | **str**| The id of the tenant the process definitions belong to. | 
 **cascade** | **bool**| &#x60;true&#x60;, if all process instances, historic process instances and jobs for this process definition should be deleted. | [optional] 
 **skip_custom_listeners** | **bool**| &#x60;true&#x60;, if only the built-in ExecutionListeners should be notified with the end event. | [optional] [default to False]
 **skip_io_mappings** | **bool**| A boolean value to control whether input/output mappings should be executed during deletion. &#x60;true&#x60;, if input/output mappings should not be invoked. | [optional] [default to False]

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
**403** | Forbidden The process definitions with the given &#x60;key&#x60; cannot be deleted due to missing permissions. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Not found Process definition with given key does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity_statistics**
> list[ActivityStatisticsResultDto] get_activity_statistics(id, failed_jobs=failed_jobs, incidents=incidents, incidents_for_type=incidents_for_type)

Get Activity Instance Statistics

Retrieves runtime statistics of a given process definition, grouped by activities. These statistics include the number of running activity instances, optionally the number of failed jobs and also optionally the number of incidents either grouped by incident types or for a specific incident type. **Note**: This does not include historic data.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    id = 'id_example' # str | The id of the process definition.
failed_jobs = True # bool | Whether to include the number of failed jobs in the result or not. Valid values are `true` or `false`. (optional)
incidents = True # bool | Valid values for this property are `true` or `false`. If this property has been set to `true` the result will include the corresponding number of incidents for each occurred incident type. If it is set to `false`, the incidents will not be included in the result. Cannot be used in combination with `incidentsForType`. (optional)
incidents_for_type = 'incidents_for_type_example' # str | If this property has been set with any incident type (i.e., a string value) the result will only include the number of incidents for the assigned incident type. Cannot be used in combination with `incidents`. See the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/incidents/#incident-types) for a list of incident types. (optional)

    try:
        # Get Activity Instance Statistics
        api_response = api_instance.get_activity_statistics(id, failed_jobs=failed_jobs, incidents=incidents, incidents_for_type=incidents_for_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_activity_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process definition. | 
 **failed_jobs** | **bool**| Whether to include the number of failed jobs in the result or not. Valid values are &#x60;true&#x60; or &#x60;false&#x60;. | [optional] 
 **incidents** | **bool**| Valid values for this property are &#x60;true&#x60; or &#x60;false&#x60;. If this property has been set to &#x60;true&#x60; the result will include the corresponding number of incidents for each occurred incident type. If it is set to &#x60;false&#x60;, the incidents will not be included in the result. Cannot be used in combination with &#x60;incidentsForType&#x60;. | [optional] 
 **incidents_for_type** | **str**| If this property has been set with any incident type (i.e., a string value) the result will only include the number of incidents for the assigned incident type. Cannot be used in combination with &#x60;incidents&#x60;. See the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/incidents/#incident-types) for a list of incident types. | [optional] 

### Return type

[**list[ActivityStatisticsResultDto]**](ActivityStatisticsResultDto.md)

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
**404** | Process definition with given key does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity_statistics_by_process_definition_key**
> list[ActivityStatisticsResultDto] get_activity_statistics_by_process_definition_key(key, failed_jobs=failed_jobs, incidents=incidents, incidents_for_type=incidents_for_type)

Get Activity Instance Statistics

Retrieves runtime statistics of the latest version of the given process definition which belongs to no tenant, grouped by activities. These statistics include the number of running activity instances, optionally the number of failed jobs and also optionally the number of incidents either grouped by incident types or for a specific incident type. **Note**: This does not include historic data.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    key = 'key_example' # str | The key of the process definition (the latest version thereof) to be retrieved.
failed_jobs = True # bool | Whether to include the number of failed jobs in the result or not. Valid values are `true` or `false`. (optional)
incidents = True # bool | Valid values for this property are `true` or `false`. If this property has been set to `true` the result will include the corresponding number of incidents for each occurred incident type. If it is set to `false`, the incidents will not be included in the result. Cannot be used in combination with `incidentsForType`. (optional)
incidents_for_type = 'incidents_for_type_example' # str | If this property has been set with any incident type (i.e., a string value) the result will only include the number of incidents for the assigned incident type. Cannot be used in combination with `incidents`. See the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/incidents/#incident-types) for a list of incident types. (optional)

    try:
        # Get Activity Instance Statistics
        api_response = api_instance.get_activity_statistics_by_process_definition_key(key, failed_jobs=failed_jobs, incidents=incidents, incidents_for_type=incidents_for_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_activity_statistics_by_process_definition_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the process definition (the latest version thereof) to be retrieved. | 
 **failed_jobs** | **bool**| Whether to include the number of failed jobs in the result or not. Valid values are &#x60;true&#x60; or &#x60;false&#x60;. | [optional] 
 **incidents** | **bool**| Valid values for this property are &#x60;true&#x60; or &#x60;false&#x60;. If this property has been set to &#x60;true&#x60; the result will include the corresponding number of incidents for each occurred incident type. If it is set to &#x60;false&#x60;, the incidents will not be included in the result. Cannot be used in combination with &#x60;incidentsForType&#x60;. | [optional] 
 **incidents_for_type** | **str**| If this property has been set with any incident type (i.e., a string value) the result will only include the number of incidents for the assigned incident type. Cannot be used in combination with &#x60;incidents&#x60;. See the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/incidents/#incident-types) for a list of incident types. | [optional] 

### Return type

[**list[ActivityStatisticsResultDto]**](ActivityStatisticsResultDto.md)

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
**404** | Process definition with given key does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity_statistics_by_process_definition_key_and_tenant_id**
> list[ActivityStatisticsResultDto] get_activity_statistics_by_process_definition_key_and_tenant_id(key, tenant_id, failed_jobs=failed_jobs, incidents=incidents, incidents_for_type=incidents_for_type)

Get Activity Instance Statistics

Retrieves runtime statistics of the latest version of the given process definition for a tenant, grouped by activities. These statistics include the number of running activity instances, optionally the number of failed jobs and also optionally the number of incidents either grouped by incident types or for a specific incident type. **Note**: This does not include historic data.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    key = 'key_example' # str | The key of the process definition (the latest version thereof) to be retrieved.
tenant_id = 'tenant_id_example' # str | The id of the tenant the process definition belongs to.
failed_jobs = True # bool | Whether to include the number of failed jobs in the result or not. Valid values are `true` or `false`. (optional)
incidents = True # bool | Valid values for this property are `true` or `false`. If this property has been set to `true` the result will include the corresponding number of incidents for each occurred incident type. If it is set to `false`, the incidents will not be included in the result. Cannot be used in combination with `incidentsForType`. (optional)
incidents_for_type = 'incidents_for_type_example' # str | If this property has been set with any incident type (i.e., a string value) the result will only include the number of incidents for the assigned incident type. Cannot be used in combination with `incidents`. See the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/incidents/#incident-types) for a list of incident types. (optional)

    try:
        # Get Activity Instance Statistics
        api_response = api_instance.get_activity_statistics_by_process_definition_key_and_tenant_id(key, tenant_id, failed_jobs=failed_jobs, incidents=incidents, incidents_for_type=incidents_for_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_activity_statistics_by_process_definition_key_and_tenant_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the process definition (the latest version thereof) to be retrieved. | 
 **tenant_id** | **str**| The id of the tenant the process definition belongs to. | 
 **failed_jobs** | **bool**| Whether to include the number of failed jobs in the result or not. Valid values are &#x60;true&#x60; or &#x60;false&#x60;. | [optional] 
 **incidents** | **bool**| Valid values for this property are &#x60;true&#x60; or &#x60;false&#x60;. If this property has been set to &#x60;true&#x60; the result will include the corresponding number of incidents for each occurred incident type. If it is set to &#x60;false&#x60;, the incidents will not be included in the result. Cannot be used in combination with &#x60;incidentsForType&#x60;. | [optional] 
 **incidents_for_type** | **str**| If this property has been set with any incident type (i.e., a string value) the result will only include the number of incidents for the assigned incident type. Cannot be used in combination with &#x60;incidents&#x60;. See the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/incidents/#incident-types) for a list of incident types. | [optional] 

### Return type

[**list[ActivityStatisticsResultDto]**](ActivityStatisticsResultDto.md)

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
**404** | Process definition with given key does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployed_start_form**
> file get_deployed_start_form(id)

Get Deployed Start Form

Retrieves the deployed form that can be referenced from a start event. For further information please refer to [User Guide](https://docs.camunda.org/manual/7.13/user-guide/task-forms/#embedded-task-forms).

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    id = 'id_example' # str | The id of the process definition to get the deployed start form for.

    try:
        # Get Deployed Start Form
        api_response = api_instance.get_deployed_start_form(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_deployed_start_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process definition to get the deployed start form for. | 

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
**400** | The form key has wrong format.  See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**403** | The deployed start form cannot be retrieved due to missing permissions on process definition resource. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | No deployed start form for a given process definition exists. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployed_start_form_by_key**
> file get_deployed_start_form_by_key(key)

Get Deployed Start Form

Retrieves the deployed form that can be referenced from a start event. For further information please refer to [User Guide](https://docs.camunda.org/manual/7.13/user-guide/task-forms/#embedded-task-forms).

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    key = 'key_example' # str | The key of the process definition (the latest version thereof) to be retrieved.

    try:
        # Get Deployed Start Form
        api_response = api_instance.get_deployed_start_form_by_key(key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_deployed_start_form_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the process definition (the latest version thereof) to be retrieved. | 

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
**400** | The form key has wrong format.  See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**403** | The deployed start form cannot be retrieved due to missing permissions on process definition resource. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | No deployed start form for a given process definition exists. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployed_start_form_by_key_and_tenant_id**
> file get_deployed_start_form_by_key_and_tenant_id(key, tenant_id)

Get Deployed Start Form

Retrieves the deployed form that can be referenced from a start event. For further information please refer to [User Guide](https://docs.camunda.org/manual/7.13/user-guide/task-forms/#embedded-task-forms).

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    key = 'key_example' # str | The key of the process definition (the latest version thereof) to be retrieved.
tenant_id = 'tenant_id_example' # str | The id of the tenant the process definitions belong to.

    try:
        # Get Deployed Start Form
        api_response = api_instance.get_deployed_start_form_by_key_and_tenant_id(key, tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_deployed_start_form_by_key_and_tenant_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the process definition (the latest version thereof) to be retrieved. | 
 **tenant_id** | **str**| The id of the tenant the process definitions belong to. | 

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
**400** | The form key has wrong format.  See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**403** | The deployed start form cannot be retrieved due to missing permissions on process definition resource. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | No deployed start form for a given process definition exists. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_process_definition_by_tenant_id**
> ProcessDefinitionDto get_latest_process_definition_by_tenant_id(key, tenant_id)

Get

Retrieves the latest version of the process definition for tenant according to the `ProcessDefinition` interface in the engine.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    key = 'key_example' # str | The key of the process definition (the latest version thereof) to be retrieved.
tenant_id = 'tenant_id_example' # str | The id of the tenant the process definition belongs to.

    try:
        # Get
        api_response = api_instance.get_latest_process_definition_by_tenant_id(key, tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_latest_process_definition_by_tenant_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the process definition (the latest version thereof) to be retrieved. | 
 **tenant_id** | **str**| The id of the tenant the process definition belongs to. | 

### Return type

[**ProcessDefinitionDto**](ProcessDefinitionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | Process definition with given &#x60;key&#x60; does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_process_definition**
> ProcessDefinitionDto get_process_definition(id)

Get

Retrieves a process definition according to the `ProcessDefinition` interface in the engine.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    id = 'id_example' # str | The id of the process definition to be retrieved.

    try:
        # Get
        api_response = api_instance.get_process_definition(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_process_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process definition to be retrieved. | 

### Return type

[**ProcessDefinitionDto**](ProcessDefinitionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | Process definition with given &#x60;id&#x60; does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_process_definition_bpmn20_xml**
> ProcessDefinitionDiagramDto get_process_definition_bpmn20_xml(id)

Get XML

Retrieves the BPMN 2.0 XML of a process definition.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    id = 'id_example' # str | The id of the process definition.

    try:
        # Get XML
        api_response = api_instance.get_process_definition_bpmn20_xml(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_process_definition_bpmn20_xml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process definition. | 

### Return type

[**ProcessDefinitionDiagramDto**](ProcessDefinitionDiagramDto.md)

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
**403** | The Process Definition xml cannot be retrieved due to missing permissions on the Process Definition resource. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Process definition with given id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_process_definition_bpmn20_xml_by_key**
> ProcessDefinitionDiagramDto get_process_definition_bpmn20_xml_by_key(key)

Get XML

Retrieves latest version the BPMN 2.0 XML of a process definition.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    key = 'key_example' # str | The key of the process definition (the latest version thereof) whose XML should be retrieved.

    try:
        # Get XML
        api_response = api_instance.get_process_definition_bpmn20_xml_by_key(key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_process_definition_bpmn20_xml_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the process definition (the latest version thereof) whose XML should be retrieved. | 

### Return type

[**ProcessDefinitionDiagramDto**](ProcessDefinitionDiagramDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**403** | The Process Definition xml cannot be retrieved due to missing permissions on the Process Definition resource. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Process definition with given id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_process_definition_bpmn20_xml_by_key_and_tenant_id**
> ProcessDefinitionDiagramDto get_process_definition_bpmn20_xml_by_key_and_tenant_id(key, tenant_id)

Get XML

Retrieves latest version the BPMN 2.0 XML of a process definition. Returns the XML for the latest version of the process definition for tenant.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    key = 'key_example' # str | The key of the process definition (the latest version thereof) whose XML should be retrieved.
tenant_id = 'tenant_id_example' # str | The id of the tenant the process definition belongs to.

    try:
        # Get XML
        api_response = api_instance.get_process_definition_bpmn20_xml_by_key_and_tenant_id(key, tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_process_definition_bpmn20_xml_by_key_and_tenant_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the process definition (the latest version thereof) whose XML should be retrieved. | 
 **tenant_id** | **str**| The id of the tenant the process definition belongs to. | 

### Return type

[**ProcessDefinitionDiagramDto**](ProcessDefinitionDiagramDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**403** | The Process Definition xml cannot be retrieved due to missing permissions on the Process Definition resource. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Process definition with given id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_process_definition_by_key**
> ProcessDefinitionDto get_process_definition_by_key(key)

Get

Retrieves the latest version of the process definition which belongs to no tenant according to the `ProcessDefinition` interface in the engine.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    key = 'key_example' # str | The key of the process definition (the latest version thereof) to be retrieved.

    try:
        # Get
        api_response = api_instance.get_process_definition_by_key(key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_process_definition_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the process definition (the latest version thereof) to be retrieved. | 

### Return type

[**ProcessDefinitionDto**](ProcessDefinitionDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | Process definition with given &#x60;key&#x60; does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_process_definition_diagram**
> file get_process_definition_diagram(id)

Get Diagram

Retrieves the diagram of a process definition.  If the process definition's deployment contains an image resource with the same file name as the process definition, the deployed image will be returned by the Get Diagram endpoint. Example: `someProcess.bpmn` and `someProcess.png`. Supported file extentions for the image are: `svg`, `png`, `jpg`, and `gif`.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    id = 'id_example' # str | The id of the process definition.

    try:
        # Get Diagram
        api_response = api_instance.get_process_definition_diagram(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_process_definition_diagram: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process definition. | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. The image diagram of this process. |  -  |
**204** | The process definition doesn&#39;t have an associated diagram. |  -  |
**404** | Process definition with given id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_process_definition_diagram_by_key**
> file get_process_definition_diagram_by_key(key)

Get Diagram

Retrieves the diagram for the latest version of the process definition which belongs to no tenant.  If the process definition's deployment contains an image resource with the same file name as the process definition, the deployed image will be returned by the Get Diagram endpoint. Example: `someProcess.bpmn` and `someProcess.png`. Supported file extentions for the image are: `svg`, `png`, `jpg`, and `gif`.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    key = 'key_example' # str | The key of the process definition.

    try:
        # Get Diagram
        api_response = api_instance.get_process_definition_diagram_by_key(key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_process_definition_diagram_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the process definition. | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. The image diagram of this process. |  -  |
**204** | The process definition doesn&#39;t have an associated diagram. |  -  |
**404** | Process definition with given id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_process_definition_diagram_by_key_and_tenant_id**
> file get_process_definition_diagram_by_key_and_tenant_id(key, tenant_id)

Get Diagram

Retrieves the diagram for the latest version of the process definition for tenant.  If the process definition's deployment contains an image resource with the same file name as the process definition, the deployed image will be returned by the Get Diagram endpoint. Example: `someProcess.bpmn` and `someProcess.png`. Supported file extentions for the image are: `svg`, `png`, `jpg`, and `gif`.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    key = 'key_example' # str | The key of the process definition.
tenant_id = 'tenant_id_example' # str | The id of the tenant the process definition belongs to.

    try:
        # Get Diagram
        api_response = api_instance.get_process_definition_diagram_by_key_and_tenant_id(key, tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_process_definition_diagram_by_key_and_tenant_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the process definition. | 
 **tenant_id** | **str**| The id of the tenant the process definition belongs to. | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. The image diagram of this process. |  -  |
**204** | The process definition doesn&#39;t have an associated diagram. |  -  |
**404** | Process definition with given id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_process_definition_statistics**
> list[ProcessDefinitionStatisticsResultDto] get_process_definition_statistics(failed_jobs=failed_jobs, incidents=incidents, incidents_for_type=incidents_for_type, root_incidents=root_incidents)

Get Process Instance Statistics

Retrieves runtime statistics of the process engine, grouped by process definitions. These statistics include the number of running process instances, optionally the number of failed jobs and also optionally the number of incidents either grouped by incident types or for a specific incident type. **Note**: This does not include historic data.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    failed_jobs = True # bool | Whether to include the number of failed jobs in the result or not. Valid values are `true` or `false`. (optional)
incidents = True # bool | Valid values for this property are `true` or `false`. If this property has been set to `true` the result will include the corresponding number of incidents for each occurred incident type. If it is set to `false`, the incidents will not be included in the result. Cannot be used in combination with `incidentsForType`. (optional)
incidents_for_type = 'incidents_for_type_example' # str | If this property has been set with any incident type (i.e., a string value) the result will only include the number of incidents for the assigned incident type. Cannot be used in combination with `incidents`. See the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/incidents/#incident-types) for a list of incident types. (optional)
root_incidents = True # bool | Valid values for this property are `true` or `false`. If this property has been set to `true` the result will include the corresponding number of root incidents for each occurred incident type. If it is set to `false`, the incidents will not be included in the result. Cannot be used in combination with `incidentsForType` or `incidents`. (optional)

    try:
        # Get Process Instance Statistics
        api_response = api_instance.get_process_definition_statistics(failed_jobs=failed_jobs, incidents=incidents, incidents_for_type=incidents_for_type, root_incidents=root_incidents)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_process_definition_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **failed_jobs** | **bool**| Whether to include the number of failed jobs in the result or not. Valid values are &#x60;true&#x60; or &#x60;false&#x60;. | [optional] 
 **incidents** | **bool**| Valid values for this property are &#x60;true&#x60; or &#x60;false&#x60;. If this property has been set to &#x60;true&#x60; the result will include the corresponding number of incidents for each occurred incident type. If it is set to &#x60;false&#x60;, the incidents will not be included in the result. Cannot be used in combination with &#x60;incidentsForType&#x60;. | [optional] 
 **incidents_for_type** | **str**| If this property has been set with any incident type (i.e., a string value) the result will only include the number of incidents for the assigned incident type. Cannot be used in combination with &#x60;incidents&#x60;. See the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/incidents/#incident-types) for a list of incident types. | [optional] 
 **root_incidents** | **bool**| Valid values for this property are &#x60;true&#x60; or &#x60;false&#x60;. If this property has been set to &#x60;true&#x60; the result will include the corresponding number of root incidents for each occurred incident type. If it is set to &#x60;false&#x60;, the incidents will not be included in the result. Cannot be used in combination with &#x60;incidentsForType&#x60; or &#x60;incidents&#x60;. | [optional] 

### Return type

[**list[ProcessDefinitionStatisticsResultDto]**](ProcessDefinitionStatisticsResultDto.md)

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

# **get_process_definitions**
> list[ProcessDefinitionDto] get_process_definitions(process_definition_id=process_definition_id, process_definition_id_in=process_definition_id_in, name=name, name_like=name_like, deployment_id=deployment_id, deployed_after=deployed_after, deployed_at=deployed_at, key=key, keys_in=keys_in, key_like=key_like, category=category, category_like=category_like, version=version, latest_version=latest_version, resource_name=resource_name, resource_name_like=resource_name_like, startable_by=startable_by, active=active, suspended=suspended, incident_id=incident_id, incident_type=incident_type, incident_message=incident_message, incident_message_like=incident_message_like, tenant_id_in=tenant_id_in, without_tenant_id=without_tenant_id, include_process_definitions_without_tenant_id=include_process_definitions_without_tenant_id, version_tag=version_tag, version_tag_like=version_tag_like, without_version_tag=without_version_tag, startable_in_tasklist=startable_in_tasklist, not_startable_in_tasklist=not_startable_in_tasklist, startable_permission_check=startable_permission_check, sort_by=sort_by, sort_order=sort_order, first_result=first_result, max_results=max_results)

Get List

Queries for process definitions that fulfill given parameters. Parameters may be the properties of  process definitions, such as the name, key or version. The size of the result set can be retrieved by using the [Get Definition Count](https://docs.camunda.org/manual/7.13/reference/rest/process-definition/get-query-count/) method.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    process_definition_id = 'process_definition_id_example' # str | Filter by process definition id. (optional)
process_definition_id_in = 'process_definition_id_in_example' # str | Filter by a comma-separated list of process definition ids. (optional)
name = 'name_example' # str | Filter by process definition name. (optional)
name_like = 'name_like_example' # str | Filter by process definition names that the parameter is a substring of. (optional)
deployment_id = 'deployment_id_example' # str | Filter by the deployment the id belongs to. (optional)
deployed_after = '2013-10-20T19:20:30+01:00' # datetime | Filter by the deploy time of the deployment the process definition belongs to. Only selects process definitions that have been deployed after (exclusive) a specific time. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.546+0200`. (optional)
deployed_at = '2013-10-20T19:20:30+01:00' # datetime | Filter by the deploy time of the deployment the process definition belongs to. Only selects process definitions that have been deployed at a specific time (exact match). By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.546+0200`. (optional)
key = 'key_example' # str | Filter by process definition key, i.e., the id in the BPMN 2.0 XML. Exact match. (optional)
keys_in = 'keys_in_example' # str | Filter by a comma-separated list of process definition keys. (optional)
key_like = 'key_like_example' # str | Filter by process definition keys that the parameter is a substring of. (optional)
category = 'category_example' # str | Filter by process definition category. Exact match. (optional)
category_like = 'category_like_example' # str | Filter by process definition categories that the parameter is a substring of. (optional)
version = 56 # int | Filter by process definition version. (optional)
latest_version = True # bool | Only include those process definitions that are latest versions. Value may only be `true`, as `false` is the default behavior. (optional)
resource_name = 'resource_name_example' # str | Filter by the name of the process definition resource. Exact match. (optional)
resource_name_like = 'resource_name_like_example' # str | Filter by names of those process definition resources that the parameter is a substring of. (optional)
startable_by = 'startable_by_example' # str | Filter by a user name who is allowed to start the process. (optional)
active = True # bool | Only include active process definitions. Value may only be `true`, as `false` is the default behavior. (optional)
suspended = True # bool | Only include suspended process definitions. Value may only be `true`, as `false` is the default behavior. (optional)
incident_id = 'incident_id_example' # str | Filter by the incident id. (optional)
incident_type = 'incident_type_example' # str | Filter by the incident type. See the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/incidents/#incident-types) for a list of incident types. (optional)
incident_message = 'incident_message_example' # str | Filter by the incident message. Exact match. (optional)
incident_message_like = 'incident_message_like_example' # str | Filter by the incident message that the parameter is a substring of. (optional)
tenant_id_in = 'tenant_id_in_example' # str | Filter by a comma-separated list of tenant ids. A process definition must have one of the given tenant ids. (optional)
without_tenant_id = True # bool | Only include process definitions which belong to no tenant. Value may only be true, as false is the default behavior. (optional)
include_process_definitions_without_tenant_id = True # bool | Include process definitions which belong to no tenant. Can be used in combination with `tenantIdIn`. Value may only be `true`, as `false` is the default behavior. (optional)
version_tag = 'version_tag_example' # str | Filter by the version tag. (optional)
version_tag_like = 'version_tag_like_example' # str | Filter by the version tag that the parameter is a substring of. (optional)
without_version_tag = True # bool | Only include process definitions without a `versionTag`. (optional)
startable_in_tasklist = True # bool | Filter by process definitions which are startable in Tasklist.. (optional)
not_startable_in_tasklist = True # bool | Filter by process definitions which are not startable in Tasklist. (optional)
startable_permission_check = True # bool | Filter by process definitions which the user is allowed to start in Tasklist. If the user doesn't have these permissions the result will be empty list. The permissions are: * `CREATE` permission for all Process instances * `CREATE_INSTANCE` and `READ` permission on Process definition level (optional)
sort_by = 'sort_by_example' # str | Sort the results lexicographically by a given criterion. Must be used in conjunction with the sortOrder parameter. (optional)
sort_order = 'sort_order_example' # str | Sort the results in a given order. Values may be asc for ascending order or desc for descending order. Must be used in conjunction with the sortBy parameter. (optional)
first_result = 56 # int | Pagination of results. Specifies the index of the first result to return. (optional)
max_results = 56 # int | Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. (optional)

    try:
        # Get List
        api_response = api_instance.get_process_definitions(process_definition_id=process_definition_id, process_definition_id_in=process_definition_id_in, name=name, name_like=name_like, deployment_id=deployment_id, deployed_after=deployed_after, deployed_at=deployed_at, key=key, keys_in=keys_in, key_like=key_like, category=category, category_like=category_like, version=version, latest_version=latest_version, resource_name=resource_name, resource_name_like=resource_name_like, startable_by=startable_by, active=active, suspended=suspended, incident_id=incident_id, incident_type=incident_type, incident_message=incident_message, incident_message_like=incident_message_like, tenant_id_in=tenant_id_in, without_tenant_id=without_tenant_id, include_process_definitions_without_tenant_id=include_process_definitions_without_tenant_id, version_tag=version_tag, version_tag_like=version_tag_like, without_version_tag=without_version_tag, startable_in_tasklist=startable_in_tasklist, not_startable_in_tasklist=not_startable_in_tasklist, startable_permission_check=startable_permission_check, sort_by=sort_by, sort_order=sort_order, first_result=first_result, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_process_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_definition_id** | **str**| Filter by process definition id. | [optional] 
 **process_definition_id_in** | **str**| Filter by a comma-separated list of process definition ids. | [optional] 
 **name** | **str**| Filter by process definition name. | [optional] 
 **name_like** | **str**| Filter by process definition names that the parameter is a substring of. | [optional] 
 **deployment_id** | **str**| Filter by the deployment the id belongs to. | [optional] 
 **deployed_after** | **datetime**| Filter by the deploy time of the deployment the process definition belongs to. Only selects process definitions that have been deployed after (exclusive) a specific time. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.546+0200&#x60;. | [optional] 
 **deployed_at** | **datetime**| Filter by the deploy time of the deployment the process definition belongs to. Only selects process definitions that have been deployed at a specific time (exact match). By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.546+0200&#x60;. | [optional] 
 **key** | **str**| Filter by process definition key, i.e., the id in the BPMN 2.0 XML. Exact match. | [optional] 
 **keys_in** | **str**| Filter by a comma-separated list of process definition keys. | [optional] 
 **key_like** | **str**| Filter by process definition keys that the parameter is a substring of. | [optional] 
 **category** | **str**| Filter by process definition category. Exact match. | [optional] 
 **category_like** | **str**| Filter by process definition categories that the parameter is a substring of. | [optional] 
 **version** | **int**| Filter by process definition version. | [optional] 
 **latest_version** | **bool**| Only include those process definitions that are latest versions. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] 
 **resource_name** | **str**| Filter by the name of the process definition resource. Exact match. | [optional] 
 **resource_name_like** | **str**| Filter by names of those process definition resources that the parameter is a substring of. | [optional] 
 **startable_by** | **str**| Filter by a user name who is allowed to start the process. | [optional] 
 **active** | **bool**| Only include active process definitions. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] 
 **suspended** | **bool**| Only include suspended process definitions. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] 
 **incident_id** | **str**| Filter by the incident id. | [optional] 
 **incident_type** | **str**| Filter by the incident type. See the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/incidents/#incident-types) for a list of incident types. | [optional] 
 **incident_message** | **str**| Filter by the incident message. Exact match. | [optional] 
 **incident_message_like** | **str**| Filter by the incident message that the parameter is a substring of. | [optional] 
 **tenant_id_in** | **str**| Filter by a comma-separated list of tenant ids. A process definition must have one of the given tenant ids. | [optional] 
 **without_tenant_id** | **bool**| Only include process definitions which belong to no tenant. Value may only be true, as false is the default behavior. | [optional] 
 **include_process_definitions_without_tenant_id** | **bool**| Include process definitions which belong to no tenant. Can be used in combination with &#x60;tenantIdIn&#x60;. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] 
 **version_tag** | **str**| Filter by the version tag. | [optional] 
 **version_tag_like** | **str**| Filter by the version tag that the parameter is a substring of. | [optional] 
 **without_version_tag** | **bool**| Only include process definitions without a &#x60;versionTag&#x60;. | [optional] 
 **startable_in_tasklist** | **bool**| Filter by process definitions which are startable in Tasklist.. | [optional] 
 **not_startable_in_tasklist** | **bool**| Filter by process definitions which are not startable in Tasklist. | [optional] 
 **startable_permission_check** | **bool**| Filter by process definitions which the user is allowed to start in Tasklist. If the user doesn&#39;t have these permissions the result will be empty list. The permissions are: * &#x60;CREATE&#x60; permission for all Process instances * &#x60;CREATE_INSTANCE&#x60; and &#x60;READ&#x60; permission on Process definition level | [optional] 
 **sort_by** | **str**| Sort the results lexicographically by a given criterion. Must be used in conjunction with the sortOrder parameter. | [optional] 
 **sort_order** | **str**| Sort the results in a given order. Values may be asc for ascending order or desc for descending order. Must be used in conjunction with the sortBy parameter. | [optional] 
 **first_result** | **int**| Pagination of results. Specifies the index of the first result to return. | [optional] 
 **max_results** | **int**| Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. | [optional] 

### Return type

[**list[ProcessDefinitionDto]**](ProcessDefinitionDto.md)

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

# **get_process_definitions_count**
> CountResultDto get_process_definitions_count(process_definition_id=process_definition_id, process_definition_id_in=process_definition_id_in, name=name, name_like=name_like, deployment_id=deployment_id, deployed_after=deployed_after, deployed_at=deployed_at, key=key, keys_in=keys_in, key_like=key_like, category=category, category_like=category_like, version=version, latest_version=latest_version, resource_name=resource_name, resource_name_like=resource_name_like, startable_by=startable_by, active=active, suspended=suspended, incident_id=incident_id, incident_type=incident_type, incident_message=incident_message, incident_message_like=incident_message_like, tenant_id_in=tenant_id_in, without_tenant_id=without_tenant_id, include_process_definitions_without_tenant_id=include_process_definitions_without_tenant_id, version_tag=version_tag, version_tag_like=version_tag_like, without_version_tag=without_version_tag, startable_in_tasklist=startable_in_tasklist, not_startable_in_tasklist=not_startable_in_tasklist, startable_permission_check=startable_permission_check)

Get List Count

Requests the number of process definitions that fulfill the query criteria. Takes the same filtering parameters as the [Get Definitions](https://docs.camunda.org/manual/7.13/reference/rest/process-definition/get-query/) method.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    process_definition_id = 'process_definition_id_example' # str | Filter by process definition id. (optional)
process_definition_id_in = 'process_definition_id_in_example' # str | Filter by a comma-separated list of process definition ids. (optional)
name = 'name_example' # str | Filter by process definition name. (optional)
name_like = 'name_like_example' # str | Filter by process definition names that the parameter is a substring of. (optional)
deployment_id = 'deployment_id_example' # str | Filter by the deployment the id belongs to. (optional)
deployed_after = '2013-10-20T19:20:30+01:00' # datetime | Filter by the deploy time of the deployment the process definition belongs to. Only selects process definitions that have been deployed after (exclusive) a specific time. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.546+0200`. (optional)
deployed_at = '2013-10-20T19:20:30+01:00' # datetime | Filter by the deploy time of the deployment the process definition belongs to. Only selects process definitions that have been deployed at a specific time (exact match). By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.546+0200`. (optional)
key = 'key_example' # str | Filter by process definition key, i.e., the id in the BPMN 2.0 XML. Exact match. (optional)
keys_in = 'keys_in_example' # str | Filter by a comma-separated list of process definition keys. (optional)
key_like = 'key_like_example' # str | Filter by process definition keys that the parameter is a substring of. (optional)
category = 'category_example' # str | Filter by process definition category. Exact match. (optional)
category_like = 'category_like_example' # str | Filter by process definition categories that the parameter is a substring of. (optional)
version = 56 # int | Filter by process definition version. (optional)
latest_version = True # bool | Only include those process definitions that are latest versions. Value may only be `true`, as `false` is the default behavior. (optional)
resource_name = 'resource_name_example' # str | Filter by the name of the process definition resource. Exact match. (optional)
resource_name_like = 'resource_name_like_example' # str | Filter by names of those process definition resources that the parameter is a substring of. (optional)
startable_by = 'startable_by_example' # str | Filter by a user name who is allowed to start the process. (optional)
active = True # bool | Only include active process definitions. Value may only be `true`, as `false` is the default behavior. (optional)
suspended = True # bool | Only include suspended process definitions. Value may only be `true`, as `false` is the default behavior. (optional)
incident_id = 'incident_id_example' # str | Filter by the incident id. (optional)
incident_type = 'incident_type_example' # str | Filter by the incident type. See the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/incidents/#incident-types) for a list of incident types. (optional)
incident_message = 'incident_message_example' # str | Filter by the incident message. Exact match. (optional)
incident_message_like = 'incident_message_like_example' # str | Filter by the incident message that the parameter is a substring of. (optional)
tenant_id_in = 'tenant_id_in_example' # str | Filter by a comma-separated list of tenant ids. A process definition must have one of the given tenant ids. (optional)
without_tenant_id = True # bool | Only include process definitions which belong to no tenant. Value may only be true, as false is the default behavior. (optional)
include_process_definitions_without_tenant_id = True # bool | Include process definitions which belong to no tenant. Can be used in combination with `tenantIdIn`. Value may only be `true`, as `false` is the default behavior. (optional)
version_tag = 'version_tag_example' # str | Filter by the version tag. (optional)
version_tag_like = 'version_tag_like_example' # str | Filter by the version tag that the parameter is a substring of. (optional)
without_version_tag = True # bool | Only include process definitions without a `versionTag`. (optional)
startable_in_tasklist = True # bool | Filter by process definitions which are startable in Tasklist.. (optional)
not_startable_in_tasklist = True # bool | Filter by process definitions which are not startable in Tasklist. (optional)
startable_permission_check = True # bool | Filter by process definitions which the user is allowed to start in Tasklist. If the user doesn't have these permissions the result will be empty list. The permissions are: * `CREATE` permission for all Process instances * `CREATE_INSTANCE` and `READ` permission on Process definition level (optional)

    try:
        # Get List Count
        api_response = api_instance.get_process_definitions_count(process_definition_id=process_definition_id, process_definition_id_in=process_definition_id_in, name=name, name_like=name_like, deployment_id=deployment_id, deployed_after=deployed_after, deployed_at=deployed_at, key=key, keys_in=keys_in, key_like=key_like, category=category, category_like=category_like, version=version, latest_version=latest_version, resource_name=resource_name, resource_name_like=resource_name_like, startable_by=startable_by, active=active, suspended=suspended, incident_id=incident_id, incident_type=incident_type, incident_message=incident_message, incident_message_like=incident_message_like, tenant_id_in=tenant_id_in, without_tenant_id=without_tenant_id, include_process_definitions_without_tenant_id=include_process_definitions_without_tenant_id, version_tag=version_tag, version_tag_like=version_tag_like, without_version_tag=without_version_tag, startable_in_tasklist=startable_in_tasklist, not_startable_in_tasklist=not_startable_in_tasklist, startable_permission_check=startable_permission_check)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_process_definitions_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_definition_id** | **str**| Filter by process definition id. | [optional] 
 **process_definition_id_in** | **str**| Filter by a comma-separated list of process definition ids. | [optional] 
 **name** | **str**| Filter by process definition name. | [optional] 
 **name_like** | **str**| Filter by process definition names that the parameter is a substring of. | [optional] 
 **deployment_id** | **str**| Filter by the deployment the id belongs to. | [optional] 
 **deployed_after** | **datetime**| Filter by the deploy time of the deployment the process definition belongs to. Only selects process definitions that have been deployed after (exclusive) a specific time. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.546+0200&#x60;. | [optional] 
 **deployed_at** | **datetime**| Filter by the deploy time of the deployment the process definition belongs to. Only selects process definitions that have been deployed at a specific time (exact match). By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.546+0200&#x60;. | [optional] 
 **key** | **str**| Filter by process definition key, i.e., the id in the BPMN 2.0 XML. Exact match. | [optional] 
 **keys_in** | **str**| Filter by a comma-separated list of process definition keys. | [optional] 
 **key_like** | **str**| Filter by process definition keys that the parameter is a substring of. | [optional] 
 **category** | **str**| Filter by process definition category. Exact match. | [optional] 
 **category_like** | **str**| Filter by process definition categories that the parameter is a substring of. | [optional] 
 **version** | **int**| Filter by process definition version. | [optional] 
 **latest_version** | **bool**| Only include those process definitions that are latest versions. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] 
 **resource_name** | **str**| Filter by the name of the process definition resource. Exact match. | [optional] 
 **resource_name_like** | **str**| Filter by names of those process definition resources that the parameter is a substring of. | [optional] 
 **startable_by** | **str**| Filter by a user name who is allowed to start the process. | [optional] 
 **active** | **bool**| Only include active process definitions. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] 
 **suspended** | **bool**| Only include suspended process definitions. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] 
 **incident_id** | **str**| Filter by the incident id. | [optional] 
 **incident_type** | **str**| Filter by the incident type. See the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/incidents/#incident-types) for a list of incident types. | [optional] 
 **incident_message** | **str**| Filter by the incident message. Exact match. | [optional] 
 **incident_message_like** | **str**| Filter by the incident message that the parameter is a substring of. | [optional] 
 **tenant_id_in** | **str**| Filter by a comma-separated list of tenant ids. A process definition must have one of the given tenant ids. | [optional] 
 **without_tenant_id** | **bool**| Only include process definitions which belong to no tenant. Value may only be true, as false is the default behavior. | [optional] 
 **include_process_definitions_without_tenant_id** | **bool**| Include process definitions which belong to no tenant. Can be used in combination with &#x60;tenantIdIn&#x60;. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] 
 **version_tag** | **str**| Filter by the version tag. | [optional] 
 **version_tag_like** | **str**| Filter by the version tag that the parameter is a substring of. | [optional] 
 **without_version_tag** | **bool**| Only include process definitions without a &#x60;versionTag&#x60;. | [optional] 
 **startable_in_tasklist** | **bool**| Filter by process definitions which are startable in Tasklist.. | [optional] 
 **not_startable_in_tasklist** | **bool**| Filter by process definitions which are not startable in Tasklist. | [optional] 
 **startable_permission_check** | **bool**| Filter by process definitions which the user is allowed to start in Tasklist. If the user doesn&#39;t have these permissions the result will be empty list. The permissions are: * &#x60;CREATE&#x60; permission for all Process instances * &#x60;CREATE_INSTANCE&#x60; and &#x60;READ&#x60; permission on Process definition level | [optional] 

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

# **get_rendered_start_form**
> file get_rendered_start_form(id)

Get Rendered Start Form

Retrieves the rendered form for a process definition. This method can be used to get the HTML rendering of a [Generated Task Form](https://docs.camunda.org/manual/7.13/user-guide/task-forms/#generated-task-forms).

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    id = 'id_example' # str | The id of the process definition to get the rendered start form for.

    try:
        # Get Rendered Start Form
        api_response = api_instance.get_rendered_start_form(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_rendered_start_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process definition to get the rendered start form for. | 

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
**400** | Process definition has no form field metadata defined. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Process definition with given id does not exist.  See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rendered_start_form_by_key**
> file get_rendered_start_form_by_key(key)

Get Rendered Start Form

Retrieves  the rendered form for the latest version of the process definition which belongs to no tenant. This method can be used to get the HTML rendering of a [Generated Task Form](https://docs.camunda.org/manual/7.13/user-guide/task-forms/#generated-task-forms).

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    key = 'key_example' # str | The key of the process definition (the latest version thereof) to be retrieved.

    try:
        # Get Rendered Start Form
        api_response = api_instance.get_rendered_start_form_by_key(key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_rendered_start_form_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the process definition (the latest version thereof) to be retrieved. | 

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
**400** | Process definition has no form field metadata defined. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Process definition with given key does not exist.  See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rendered_start_form_by_key_and_tenant_id**
> file get_rendered_start_form_by_key_and_tenant_id(key, tenant_id)

Get Rendered Start Form

Retrieves  the rendered form for the latest version of the process definition for a tenant. This method can be used to get the HTML rendering of a [Generated Task Form](https://docs.camunda.org/manual/7.13/user-guide/task-forms/#generated-task-forms).

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    key = 'key_example' # str | The key of the process definition (the latest version thereof) to be retrieved.
tenant_id = 'tenant_id_example' # str | The id of the tenant the process definition belongs to.

    try:
        # Get Rendered Start Form
        api_response = api_instance.get_rendered_start_form_by_key_and_tenant_id(key, tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_rendered_start_form_by_key_and_tenant_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the process definition (the latest version thereof) to be retrieved. | 
 **tenant_id** | **str**| The id of the tenant the process definition belongs to. | 

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
**400** | Process definition has no form field metadata defined. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Process definition with given key does not exist.  See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_start_form**
> FormDto get_start_form(id)

Get Start Form Key

Retrieves the key of the start form for a process definition. The form key corresponds to the `FormData#formKey` property in the engine.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    id = 'id_example' # str | The id of the process definition to get the start form key for.

    try:
        # Get Start Form Key
        api_response = api_instance.get_start_form(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_start_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process definition to get the start form key for. | 

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
**400** | Process definition has no start form defined. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Process definition with given id does not exist.  See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_start_form_by_key**
> FormDto get_start_form_by_key(key)

Get Start Form Key

Retrieves the key of the start form for the latest version of the process definition which belongs to no tenant. The form key corresponds to the `FormData#formKey` property in the engine.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    key = 'key_example' # str | The key of the process definition (the latest version thereof) for which the form key is to be retrieved.

    try:
        # Get Start Form Key
        api_response = api_instance.get_start_form_by_key(key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_start_form_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the process definition (the latest version thereof) for which the form key is to be retrieved. | 

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
**400** | Process definition has no start form defined. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Process definition with given key does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_start_form_by_key_and_tenant_id**
> FormDto get_start_form_by_key_and_tenant_id(key, tenant_id)

Get Start Form Key

Retrieves the key of the start form for the latest version of the process definition for a tenant. The form key corresponds to the `FormData#formKey` property in the engine.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    key = 'key_example' # str | The key of the process definition (the latest version thereof) for which the form key is to be retrieved.
tenant_id = 'tenant_id_example' # str | The id of the tenant the process definition belongs to.

    try:
        # Get Start Form Key
        api_response = api_instance.get_start_form_by_key_and_tenant_id(key, tenant_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_start_form_by_key_and_tenant_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the process definition (the latest version thereof) for which the form key is to be retrieved. | 
 **tenant_id** | **str**| The id of the tenant the process definition belongs to. | 

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
**400** | Process definition has no start form defined. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Process definition with given key does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_start_form_variables**
> dict(str, VariableValueDto) get_start_form_variables(id, variable_names=variable_names, deserialize_values=deserialize_values)

Get Start Form Variables

Retrieves the start form variables for a process definition (only if they are defined via the  [Generated Task Form](https://docs.camunda.org/manual/7.13/user-guide/task-forms/#generated-task-forms) approach). The start form variables take form data specified on the start event into account. If form fields are defined, the variable types and default values of the form fields are taken into account.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    id = 'id_example' # str | The id of the process definition to retrieve the variables for.
variable_names = 'variable_names_example' # str | A comma-separated list of variable names. Allows restricting the list of requested variables to the variable names in the list. It is best practice to restrict the list of variables to the variables actually required by the form in order to minimize fetching of data. If the query parameter is ommitted all variables are fetched. If the query parameter contains non-existent variable names, the variable names are ignored. (optional)
deserialize_values = True # bool | Determines whether serializable variable values (typically variables that store custom Java objects) should be deserialized on server side (default true).  If set to true, a serializable variable will be deserialized on server side and transformed to JSON using [Jackson's](http://jackson.codehaus.org/) POJO/bean property introspection feature. Note that this requires the Java classes of the variable value to be on the REST API's classpath.  If set to false, a serializable variable will be returned in its serialized format. For example, a variable that is serialized as XML will be returned as a JSON string containing XML.  **Note**: While true is the default value for reasons of backward compatibility, we recommend setting this parameter to false when developing web applications that are independent of the Java process applications deployed to the engine. (optional) (default to True)

    try:
        # Get Start Form Variables
        api_response = api_instance.get_start_form_variables(id, variable_names=variable_names, deserialize_values=deserialize_values)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_start_form_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process definition to retrieve the variables for. | 
 **variable_names** | **str**| A comma-separated list of variable names. Allows restricting the list of requested variables to the variable names in the list. It is best practice to restrict the list of variables to the variables actually required by the form in order to minimize fetching of data. If the query parameter is ommitted all variables are fetched. If the query parameter contains non-existent variable names, the variable names are ignored. | [optional] 
 **deserialize_values** | **bool**| Determines whether serializable variable values (typically variables that store custom Java objects) should be deserialized on server side (default true).  If set to true, a serializable variable will be deserialized on server side and transformed to JSON using [Jackson&#39;s](http://jackson.codehaus.org/) POJO/bean property introspection feature. Note that this requires the Java classes of the variable value to be on the REST API&#39;s classpath.  If set to false, a serializable variable will be returned in its serialized format. For example, a variable that is serialized as XML will be returned as a JSON string containing XML.  **Note**: While true is the default value for reasons of backward compatibility, we recommend setting this parameter to false when developing web applications that are independent of the Java process applications deployed to the engine. | [optional] [default to True]

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
**404** | The id is null or does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_start_form_variables_by_key**
> dict(str, VariableValueDto) get_start_form_variables_by_key(key, variable_names=variable_names, deserialize_values=deserialize_values)

Get Start Form Variables

Retrieves the start form variables for the latest process definition which belongs to no tenant (only if they are defined via the  [Generated Task Form](https://docs.camunda.org/manual/7.13/user-guide/task-forms/#generated-task-forms) approach). The start form variables take form data specified on the start event into account. If form fields are defined, the variable types and default values of the form fields are taken into account.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    key = 'key_example' # str | The key of the process definition (the latest version thereof) to be retrieved.
variable_names = 'variable_names_example' # str | A comma-separated list of variable names. Allows restricting the list of requested variables to the variable names in the list. It is best practice to restrict the list of variables to the variables actually required by the form in order to minimize fetching of data. If the query parameter is ommitted all variables are fetched. If the query parameter contains non-existent variable names, the variable names are ignored. (optional)
deserialize_values = True # bool | Determines whether serializable variable values (typically variables that store custom Java objects) should be deserialized on server side (default true).  If set to true, a serializable variable will be deserialized on server side and transformed to JSON using [Jackson's](http://jackson.codehaus.org/) POJO/bean property introspection feature. Note that this requires the Java classes of the variable value to be on the REST API's classpath.  If set to false, a serializable variable will be returned in its serialized format. For example, a variable that is serialized as XML will be returned as a JSON string containing XML.  **Note**: While true is the default value for reasons of backward compatibility, we recommend setting this parameter to false when developing web applications that are independent of the Java process applications deployed to the engine. (optional) (default to True)

    try:
        # Get Start Form Variables
        api_response = api_instance.get_start_form_variables_by_key(key, variable_names=variable_names, deserialize_values=deserialize_values)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_start_form_variables_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the process definition (the latest version thereof) to be retrieved. | 
 **variable_names** | **str**| A comma-separated list of variable names. Allows restricting the list of requested variables to the variable names in the list. It is best practice to restrict the list of variables to the variables actually required by the form in order to minimize fetching of data. If the query parameter is ommitted all variables are fetched. If the query parameter contains non-existent variable names, the variable names are ignored. | [optional] 
 **deserialize_values** | **bool**| Determines whether serializable variable values (typically variables that store custom Java objects) should be deserialized on server side (default true).  If set to true, a serializable variable will be deserialized on server side and transformed to JSON using [Jackson&#39;s](http://jackson.codehaus.org/) POJO/bean property introspection feature. Note that this requires the Java classes of the variable value to be on the REST API&#39;s classpath.  If set to false, a serializable variable will be returned in its serialized format. For example, a variable that is serialized as XML will be returned as a JSON string containing XML.  **Note**: While true is the default value for reasons of backward compatibility, we recommend setting this parameter to false when developing web applications that are independent of the Java process applications deployed to the engine. | [optional] [default to True]

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
**404** | The key is null or does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_start_form_variables_by_key_and_tenant_id**
> dict(str, VariableValueDto) get_start_form_variables_by_key_and_tenant_id(key, tenant_id, variable_names=variable_names, deserialize_values=deserialize_values)

Get Start Form Variables

Retrieves the start form variables for the latest process definition for a tenant (only if they are defined via the  [Generated Task Form](https://docs.camunda.org/manual/7.13/user-guide/task-forms/#generated-task-forms) approach). The start form variables take form data specified on the start event into account. If form fields are defined, the variable types and default values of the form fields are taken into account.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    key = 'key_example' # str | The key of the process definition (the latest version thereof) to be retrieved.
tenant_id = 'tenant_id_example' # str | The id of the tenant the process definition belongs to.
variable_names = 'variable_names_example' # str | A comma-separated list of variable names. Allows restricting the list of requested variables to the variable names in the list. It is best practice to restrict the list of variables to the variables actually required by the form in order to minimize fetching of data. If the query parameter is ommitted all variables are fetched. If the query parameter contains non-existent variable names, the variable names are ignored. (optional)
deserialize_values = True # bool | Determines whether serializable variable values (typically variables that store custom Java objects) should be deserialized on server side (default true).  If set to true, a serializable variable will be deserialized on server side and transformed to JSON using [Jackson's](http://jackson.codehaus.org/) POJO/bean property introspection feature. Note that this requires the Java classes of the variable value to be on the REST API's classpath.  If set to false, a serializable variable will be returned in its serialized format. For example, a variable that is serialized as XML will be returned as a JSON string containing XML.  **Note**: While true is the default value for reasons of backward compatibility, we recommend setting this parameter to false when developing web applications that are independent of the Java process applications deployed to the engine. (optional) (default to True)

    try:
        # Get Start Form Variables
        api_response = api_instance.get_start_form_variables_by_key_and_tenant_id(key, tenant_id, variable_names=variable_names, deserialize_values=deserialize_values)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->get_start_form_variables_by_key_and_tenant_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the process definition (the latest version thereof) to be retrieved. | 
 **tenant_id** | **str**| The id of the tenant the process definition belongs to. | 
 **variable_names** | **str**| A comma-separated list of variable names. Allows restricting the list of requested variables to the variable names in the list. It is best practice to restrict the list of variables to the variables actually required by the form in order to minimize fetching of data. If the query parameter is ommitted all variables are fetched. If the query parameter contains non-existent variable names, the variable names are ignored. | [optional] 
 **deserialize_values** | **bool**| Determines whether serializable variable values (typically variables that store custom Java objects) should be deserialized on server side (default true).  If set to true, a serializable variable will be deserialized on server side and transformed to JSON using [Jackson&#39;s](http://jackson.codehaus.org/) POJO/bean property introspection feature. Note that this requires the Java classes of the variable value to be on the REST API&#39;s classpath.  If set to false, a serializable variable will be returned in its serialized format. For example, a variable that is serialized as XML will be returned as a JSON string containing XML.  **Note**: While true is the default value for reasons of backward compatibility, we recommend setting this parameter to false when developing web applications that are independent of the Java process applications deployed to the engine. | [optional] [default to True]

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
**404** | The key is null or does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart_process_instance**
> restart_process_instance(id, restart_process_instance_dto=restart_process_instance_dto)

Restart Process Instance

Restarts process instances that were canceled or terminated synchronously. Can also restart completed process instances. It will create a new instance using the original instance information. To execute the restart asynchronously, use the [Restart Process Instance Async](https://docs.camunda.org/manual/7.13/reference/rest/process-definition/post-restart-process-instance-async/) method.  For more information about the difference between synchronous and asynchronous execution, please refer to the related section of the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/process-instance-restart/#execution).

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    id = 'id_example' # str | The id of the process definition of the process instances to restart.
restart_process_instance_dto = {"instructions":[{"type":"startAfterActivity","activityId":"aUserTask"}],"processInstanceIds":["aProcessInstance","anotherProcessInstance"],"initialVariables":true,"skipCustomListeners":true,"withoutBusinessKey":true} # RestartProcessInstanceDto |  (optional)

    try:
        # Restart Process Instance
        api_instance.restart_process_instance(id, restart_process_instance_dto=restart_process_instance_dto)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->restart_process_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process definition of the process instances to restart. | 
 **restart_process_instance_dto** | [**RestartProcessInstanceDto**](RestartProcessInstanceDto.md)|  | [optional] 

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
**400** | In case following parameters are missing: &#x60;instructions&#x60;, &#x60;activityId&#x60; or &#x60;transitionId&#x60;, &#x60;processInstanceIds&#x60; or &#x60;historicProcessInstanceQuery&#x60;, an exception of type &#x60;InvalidRequestException&#x60; is returned.  See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Process definition with given id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart_process_instance_async_operation**
> BatchDto restart_process_instance_async_operation(id, restart_process_instance_dto=restart_process_instance_dto)

Restart Process Instance Async

Restarts process instances that were canceled or terminated asynchronously. Can also restart completed process instances. It will create a new instance using the original instance information. To execute the restart asynchronously, use the [Restart Process Instance](https://docs.camunda.org/manual/7.13/reference/rest/process-definition/post-restart-process-instance-sync/) method.  For more information about the difference between synchronous and asynchronous execution, please refer to the related section of the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/process-instance-restart/#execution).

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    id = 'id_example' # str | The id of the process definition of the process instances to restart.
restart_process_instance_dto = {"instructions":[{"type":"startAfterActivity","activityId":"aUserTask"}],"processInstanceIds":["aProcessInstance","anotherProcessInstance"],"initialVariables":true,"skipCustomListeners":true,"withoutBusinessKey":true} # RestartProcessInstanceDto |  (optional)

    try:
        # Restart Process Instance Async
        api_response = api_instance.restart_process_instance_async_operation(id, restart_process_instance_dto=restart_process_instance_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->restart_process_instance_async_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process definition of the process instances to restart. | 
 **restart_process_instance_dto** | [**RestartProcessInstanceDto**](RestartProcessInstanceDto.md)|  | [optional] 

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
**400** | In case following parameters are missing: &#x60;instructions&#x60;, &#x60;activityId&#x60; or &#x60;transitionId&#x60;, &#x60;processInstanceIds&#x60; or &#x60;historicProcessInstanceQuery&#x60;, an exception of type &#x60;InvalidRequestException&#x60; is returned.  See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Process definition with given id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_process_instance**
> ProcessInstanceWithVariablesDto start_process_instance(id, start_process_instance_dto=start_process_instance_dto)

Start Instance

Instantiates a given process definition. Process variables and business key may be supplied in the request body.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    id = 'id_example' # str | The id of the process definition to be retrieved.
start_process_instance_dto = {"variables":{"aVariable":{"value":"aStringValue","type":"String"},"anotherVariable":{"value":true,"type":"Boolean"}},"businessKey":"myBusinessKey"} # StartProcessInstanceDto |  (optional)

    try:
        # Start Instance
        api_response = api_instance.start_process_instance(id, start_process_instance_dto=start_process_instance_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->start_process_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process definition to be retrieved. | 
 **start_process_instance_dto** | [**StartProcessInstanceDto**](StartProcessInstanceDto.md)|  | [optional] 

### Return type

[**ProcessInstanceWithVariablesDto**](ProcessInstanceWithVariablesDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | The instance could not be created due to an invalid variable value, for example if the value could not be parsed to an &#x60;Integer&#x60; value or the passed variable type is not supported. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**500** | The instance could not be created successfully. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_process_instance_by_key**
> ProcessInstanceWithVariablesDto start_process_instance_by_key(key, start_process_instance_dto=start_process_instance_dto)

Start Instance

Instantiates a given process definition, starts the latest version of the process definition which belongs to no tenant. Process variables and business key may be supplied in the request body.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    key = 'key_example' # str | The key of the process definition (the latest version thereof) to be retrieved.
start_process_instance_dto = {"variables":{"aVariable":{"value":"aStringValue","type":"String"},"anotherVariable":{"value":true,"type":"Boolean"}},"businessKey":"myBusinessKey"} # StartProcessInstanceDto |  (optional)

    try:
        # Start Instance
        api_response = api_instance.start_process_instance_by_key(key, start_process_instance_dto=start_process_instance_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->start_process_instance_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the process definition (the latest version thereof) to be retrieved. | 
 **start_process_instance_dto** | [**StartProcessInstanceDto**](StartProcessInstanceDto.md)|  | [optional] 

### Return type

[**ProcessInstanceWithVariablesDto**](ProcessInstanceWithVariablesDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | The instance could not be created due to an invalid variable value, for example if the value could not be parsed to an &#x60;Integer&#x60; value or the passed variable type is not supported. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**500** | The instance could not be created successfully. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_process_instance_by_key_and_tenant_id**
> ProcessInstanceWithVariablesDto start_process_instance_by_key_and_tenant_id(key, tenant_id, start_process_instance_dto=start_process_instance_dto)

Start Instance

Instantiates a given process definition, starts the latest version of the process definition for tenant. Process variables and business key may be supplied in the request body.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    key = 'key_example' # str | The key of the process definition (the latest version thereof) to be retrieved.
tenant_id = 'tenant_id_example' # str | The id of the tenant the process definition belongs to.
start_process_instance_dto = {"variables":{"aVariable":{"value":"aStringValue","type":"String"},"anotherVariable":{"value":true,"type":"Boolean"}},"businessKey":"myBusinessKey"} # StartProcessInstanceDto |  (optional)

    try:
        # Start Instance
        api_response = api_instance.start_process_instance_by_key_and_tenant_id(key, tenant_id, start_process_instance_dto=start_process_instance_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->start_process_instance_by_key_and_tenant_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the process definition (the latest version thereof) to be retrieved. | 
 **tenant_id** | **str**| The id of the tenant the process definition belongs to. | 
 **start_process_instance_dto** | [**StartProcessInstanceDto**](StartProcessInstanceDto.md)|  | [optional] 

### Return type

[**ProcessInstanceWithVariablesDto**](ProcessInstanceWithVariablesDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | The instance could not be created due to an invalid variable value, for example if the value could not be parsed to an &#x60;Integer&#x60; value or the passed variable type is not supported. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**500** | The instance could not be created successfully. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_form**
> ProcessInstanceDto submit_form(id, start_process_instance_form_dto=start_process_instance_form_dto)

Submit Start Form

Starts a process instance using a set of process variables and the business key. If the start event has Form Field Metadata defined, the process engine will perform backend validation for any form fields which have validators defined. See [Documentation on Generated Task Forms](https://docs.camunda.org/manual/7.13/user-guide/task-forms/#generated-task-forms).

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    id = 'id_example' # str | The id of the process definition to submit the form for.
start_process_instance_form_dto = {"variables":{"aVariable":{"value":"aStringValue","type":"String"},"anotherVariable":{"value":true,"type":"Boolean"}},"businessKey":"myBusinessKey"} # StartProcessInstanceFormDto |  (optional)

    try:
        # Submit Start Form
        api_response = api_instance.submit_form(id, start_process_instance_form_dto=start_process_instance_form_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->submit_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process definition to submit the form for. | 
 **start_process_instance_form_dto** | [**StartProcessInstanceFormDto**](StartProcessInstanceFormDto.md)|  | [optional] 

### Return type

[**ProcessInstanceDto**](ProcessInstanceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | The instance could not be created due to an invalid variable value, for example if the value could not be parsed to an &#x60;Integer&#x60; value or the passed variable type is not supported. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Process definition with given id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**500** | The instance could not be created successfully. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_form_by_key**
> ProcessInstanceDto submit_form_by_key(key, start_process_instance_form_dto=start_process_instance_form_dto)

Submit Start Form

Starts the latest version of the process definition which belongs to no tenant using a set of process variables and the business key. If the start event has Form Field Metadata defined, the process engine will perform backend validation for any form fields which have validators defined. See [Documentation on Generated Task Forms](https://docs.camunda.org/manual/7.13/user-guide/task-forms/#generated-task-forms).

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    key = 'key_example' # str | The key of the process definition to submit the form for.
start_process_instance_form_dto = {"variables":{"aVariable":{"value":"aStringValue","type":"String"},"anotherVariable":{"value":true,"type":"Boolean"}},"businessKey":"myBusinessKey"} # StartProcessInstanceFormDto |  (optional)

    try:
        # Submit Start Form
        api_response = api_instance.submit_form_by_key(key, start_process_instance_form_dto=start_process_instance_form_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->submit_form_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the process definition to submit the form for. | 
 **start_process_instance_form_dto** | [**StartProcessInstanceFormDto**](StartProcessInstanceFormDto.md)|  | [optional] 

### Return type

[**ProcessInstanceDto**](ProcessInstanceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | The instance could not be created due to an invalid variable value, for example if the value could not be parsed to an &#x60;Integer&#x60; value or the passed variable type is not supported. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Process definition with given key does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**500** | The instance could not be created successfully. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_form_by_key_and_tenant_id**
> ProcessInstanceDto submit_form_by_key_and_tenant_id(key, tenant_id, start_process_instance_form_dto=start_process_instance_form_dto)

Submit Start Form

Starts the latest version of the process definition for a tenant using a set of process variables and the business key. If the start event has Form Field Metadata defined, the process engine will perform backend validation for any form fields which have validators defined. See [Documentation on Generated Task Forms](https://docs.camunda.org/manual/7.13/user-guide/task-forms/#generated-task-forms).

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    key = 'key_example' # str | The key of the process definition to submit the form for.
tenant_id = 'tenant_id_example' # str | The id of the tenant the process definition belongs to.
start_process_instance_form_dto = {"variables":{"aVariable":{"value":"aStringValue","type":"String"},"anotherVariable":{"value":true,"type":"Boolean"}},"businessKey":"myBusinessKey"} # StartProcessInstanceFormDto |  (optional)

    try:
        # Submit Start Form
        api_response = api_instance.submit_form_by_key_and_tenant_id(key, tenant_id, start_process_instance_form_dto=start_process_instance_form_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->submit_form_by_key_and_tenant_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the process definition to submit the form for. | 
 **tenant_id** | **str**| The id of the tenant the process definition belongs to. | 
 **start_process_instance_form_dto** | [**StartProcessInstanceFormDto**](StartProcessInstanceFormDto.md)|  | [optional] 

### Return type

[**ProcessInstanceDto**](ProcessInstanceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | The instance could not be created due to an invalid variable value, for example if the value could not be parsed to an &#x60;Integer&#x60; value or the passed variable type is not supported. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Process definition with given key does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**500** | The instance could not be created successfully. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_history_time_to_live_by_process_definition_id**
> update_history_time_to_live_by_process_definition_id(id, history_time_to_live_dto=history_time_to_live_dto)

Update History Time to Live

Updates history time to live for process definition. The field is used within [History cleanup](https://docs.camunda.org/manual/7.13/user-guide/process-engine/history/#history-cleanup).

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    id = 'id_example' # str | The id of the process definition to change history time to live.
history_time_to_live_dto = {"historyTimeToLive":5} # HistoryTimeToLiveDto |  (optional)

    try:
        # Update History Time to Live
        api_instance.update_history_time_to_live_by_process_definition_id(id, history_time_to_live_dto=history_time_to_live_dto)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->update_history_time_to_live_by_process_definition_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process definition to change history time to live. | 
 **history_time_to_live_dto** | [**HistoryTimeToLiveDto**](HistoryTimeToLiveDto.md)|  | [optional] 

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
**400** | Returned if some of the request parameters are invalid. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Process definition with given id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_history_time_to_live_by_process_definition_key**
> update_history_time_to_live_by_process_definition_key(key, history_time_to_live_dto=history_time_to_live_dto)

Update History Time to Live

Updates history time to live for the latest version of the process definition which belongs to no tenant. The field is used within [History cleanup](https://docs.camunda.org/manual/7.13/user-guide/process-engine/history/#history-cleanup).

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    key = 'key_example' # str | The key of the process definition to change history time to live.
history_time_to_live_dto = {"historyTimeToLive":5} # HistoryTimeToLiveDto |  (optional)

    try:
        # Update History Time to Live
        api_instance.update_history_time_to_live_by_process_definition_key(key, history_time_to_live_dto=history_time_to_live_dto)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->update_history_time_to_live_by_process_definition_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the process definition to change history time to live. | 
 **history_time_to_live_dto** | [**HistoryTimeToLiveDto**](HistoryTimeToLiveDto.md)|  | [optional] 

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
**400** | Returned if some of the request parameters are invalid. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Process definition with given id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_history_time_to_live_by_process_definition_key_and_tenant_id**
> update_history_time_to_live_by_process_definition_key_and_tenant_id(key, tenant_id, history_time_to_live_dto=history_time_to_live_dto)

Update History Time to Live

Updates history time to live for the latest version of the process definition for a tenant. The field is used within [History cleanup](https://docs.camunda.org/manual/7.13/user-guide/process-engine/history/#history-cleanup).

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    key = 'key_example' # str | The key of the process definition to change history time to live.
tenant_id = 'tenant_id_example' # str | The id of the tenant the process definition belongs to.
history_time_to_live_dto = {"historyTimeToLive":5} # HistoryTimeToLiveDto |  (optional)

    try:
        # Update History Time to Live
        api_instance.update_history_time_to_live_by_process_definition_key_and_tenant_id(key, tenant_id, history_time_to_live_dto=history_time_to_live_dto)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->update_history_time_to_live_by_process_definition_key_and_tenant_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the process definition to change history time to live. | 
 **tenant_id** | **str**| The id of the tenant the process definition belongs to. | 
 **history_time_to_live_dto** | [**HistoryTimeToLiveDto**](HistoryTimeToLiveDto.md)|  | [optional] 

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
**400** | Returned if some of the request parameters are invalid. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Process definition with given id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_process_definition_suspension_state**
> update_process_definition_suspension_state(process_definition_suspension_state_dto=process_definition_suspension_state_dto)

Activate/Suspend By Key

Activates or suspends process definitions with the given process definition key.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    process_definition_suspension_state_dto = {"processDefinitionKey":"aProcessDefinitionKey","suspended":true,"includeProcessInstances":true,"executionDate":"2013-11-21T10:49:45T14:42:45"} # ProcessDefinitionSuspensionStateDto | **Note**: Unallowed property is `processDefinitionId`. (optional)

    try:
        # Activate/Suspend By Key
        api_instance.update_process_definition_suspension_state(process_definition_suspension_state_dto=process_definition_suspension_state_dto)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->update_process_definition_suspension_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_definition_suspension_state_dto** | [**ProcessDefinitionSuspensionStateDto**](ProcessDefinitionSuspensionStateDto.md)| **Note**: Unallowed property is &#x60;processDefinitionId&#x60;. | [optional] 

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
**400** | Returned if some of the query parameters are invalid, for example if the provided &#x60;executionDate&#x60; parameter doesn&#39;t have the expected format or if the &#x60;processDefinitionKey&#x60; parameter is &#x60;null&#x60;. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Process definition with given key does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_process_definition_suspension_state_by_id**
> update_process_definition_suspension_state_by_id(id, process_definition_suspension_state_dto=process_definition_suspension_state_dto)

Activate/Suspend By Id

Activates or suspends a given process definition by id.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    id = 'id_example' # str | The id of the process definition to activate or suspend.
process_definition_suspension_state_dto = {"suspended":true,"includeProcessInstances":true,"executionDate":"2013-11-21T10:49:45T14:42:45"} # ProcessDefinitionSuspensionStateDto | **Note**: Unallowed properties are `processDefinitionId` and `processDefinitionKey`. (optional)

    try:
        # Activate/Suspend By Id
        api_instance.update_process_definition_suspension_state_by_id(id, process_definition_suspension_state_dto=process_definition_suspension_state_dto)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->update_process_definition_suspension_state_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the process definition to activate or suspend. | 
 **process_definition_suspension_state_dto** | [**ProcessDefinitionSuspensionStateDto**](ProcessDefinitionSuspensionStateDto.md)| **Note**: Unallowed properties are &#x60;processDefinitionId&#x60; and &#x60;processDefinitionKey&#x60;. | [optional] 

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
**400** | Returned if some of the query parameters are invalid, for example if the provided &#x60;executionDate&#x60; parameter doesn&#39;t have the expected format or if the &#x60;processDefinitionKey&#x60; parameter is &#x60;null&#x60;. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Process definition with given key does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_process_definition_suspension_state_by_key**
> update_process_definition_suspension_state_by_key(key, process_definition_suspension_state_dto=process_definition_suspension_state_dto)

Activate/Suspend by Id

Activates or suspends a given process definition by latest version of process definition key which belongs to no tenant.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    key = 'key_example' # str | The key of the process definition (the latest version thereof) to be activated/suspended.
process_definition_suspension_state_dto = {"suspended":true,"includeProcessInstances":true,"executionDate":"2013-11-21T10:49:45T14:42:45"} # ProcessDefinitionSuspensionStateDto | **Note**: Unallowed properties are `processDefinitionId` and `processDefinitionKey`. (optional)

    try:
        # Activate/Suspend by Id
        api_instance.update_process_definition_suspension_state_by_key(key, process_definition_suspension_state_dto=process_definition_suspension_state_dto)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->update_process_definition_suspension_state_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the process definition (the latest version thereof) to be activated/suspended. | 
 **process_definition_suspension_state_dto** | [**ProcessDefinitionSuspensionStateDto**](ProcessDefinitionSuspensionStateDto.md)| **Note**: Unallowed properties are &#x60;processDefinitionId&#x60; and &#x60;processDefinitionKey&#x60;. | [optional] 

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
**400** | Returned if some of the query parameters are invalid, for example if the provided &#x60;executionDate&#x60; parameter doesn&#39;t have the expected format or if the &#x60;processDefinitionKey&#x60; parameter is &#x60;null&#x60;. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Process definition with given key does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_process_definition_suspension_state_by_key_and_tenant_id**
> update_process_definition_suspension_state_by_key_and_tenant_id(key, tenant_id, process_definition_suspension_state_dto=process_definition_suspension_state_dto)

Activate/Suspend by Id

Activates or suspends a given process definition by the latest version of the process definition for tenant.

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
    api_instance = openapi_client.ProcessDefinitionApi(api_client)
    key = 'key_example' # str | The key of the process definition (the latest version thereof) to be activated/suspended.
tenant_id = 'tenant_id_example' # str | The id of the tenant the process definition belongs to.
process_definition_suspension_state_dto = {"suspended":true,"includeProcessInstances":true,"executionDate":"2013-11-21T10:49:45T14:42:45"} # ProcessDefinitionSuspensionStateDto | **Note**: Unallowed properties are `processDefinitionId` and `processDefinitionKey`. (optional)

    try:
        # Activate/Suspend by Id
        api_instance.update_process_definition_suspension_state_by_key_and_tenant_id(key, tenant_id, process_definition_suspension_state_dto=process_definition_suspension_state_dto)
    except ApiException as e:
        print("Exception when calling ProcessDefinitionApi->update_process_definition_suspension_state_by_key_and_tenant_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key of the process definition (the latest version thereof) to be activated/suspended. | 
 **tenant_id** | **str**| The id of the tenant the process definition belongs to. | 
 **process_definition_suspension_state_dto** | [**ProcessDefinitionSuspensionStateDto**](ProcessDefinitionSuspensionStateDto.md)| **Note**: Unallowed properties are &#x60;processDefinitionId&#x60; and &#x60;processDefinitionKey&#x60;. | [optional] 

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
**400** | Returned if some of the query parameters are invalid, for example if the provided &#x60;executionDate&#x60; parameter doesn&#39;t have the expected format or if the &#x60;processDefinitionKey&#x60; parameter is &#x60;null&#x60;. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | Process definition with given key does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

