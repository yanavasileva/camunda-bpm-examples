# openapi_client.DeploymentApi

All URIs are relative to *http://localhost:8080/engine-rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_deployment**](DeploymentApi.md#create_deployment) | **POST** /deployment/create | 
[**delete_deployment**](DeploymentApi.md#delete_deployment) | **DELETE** /deployment/{id} | 
[**get_deployment**](DeploymentApi.md#get_deployment) | **GET** /deployment/{id} | 
[**get_deployment_resource**](DeploymentApi.md#get_deployment_resource) | **GET** /deployment/{id}/resources/{resourceId} | 
[**get_deployment_resource_data**](DeploymentApi.md#get_deployment_resource_data) | **GET** /deployment/{id}/resources/{resourceId}/data | 
[**get_deployment_resources**](DeploymentApi.md#get_deployment_resources) | **GET** /deployment/{id}/resources | 
[**get_deployments**](DeploymentApi.md#get_deployments) | **GET** /deployment | 
[**get_deployments_count**](DeploymentApi.md#get_deployments_count) | **GET** /deployment/count | 
[**redeploy**](DeploymentApi.md#redeploy) | **POST** /deployment/{id}/redeploy | 


# **create_deployment**
> DeploymentWithDefinitionsDto create_deployment(tenant_id=tenant_id, deployment_source=deployment_source, deploy_changed_only=deploy_changed_only, enable_duplicate_filtering=enable_duplicate_filtering, deployment_name=deployment_name, data=data)



Creates a deployment.  **Security Consideration**  Deployments can contain custom code in form of scripts or EL expressions to customize process behavior. This may be abused for remote execution of arbitrary code.

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
    api_instance = openapi_client.DeploymentApi(api_client)
    tenant_id = 'tenant_id_example' # str | The tenant id for the deployment to be created. (optional)
deployment_source = 'deployment_source_example' # str | The source for the deployment to be created. (optional)
deploy_changed_only = False # bool | A flag indicating whether the process engine should perform duplicate checking on a per-resource basis. If set to true, only those resources that have actually changed are deployed. Checks are made against resources included previous deployments of the same name and only against the latest versions of those resources. If set to true, the option enable-duplicate-filtering is overridden and set to true. (optional) (default to False)
enable_duplicate_filtering = False # bool | A flag indicating whether the process engine should perform duplicate checking for the deployment or not. This allows you to check if a deployment with the same name and the same resouces already exists and if true, not create a new deployment but instead return the existing deployment. The default value is false. (optional) (default to False)
deployment_name = 'deployment_name_example' # str | The name for the deployment to be created. (optional)
data = '/path/to/file' # file | The binary data to create the deployment resource. It is possible to have more than one form part with different form part names for the binary data to create a deployment. (optional)

    try:
        api_response = api_instance.create_deployment(tenant_id=tenant_id, deployment_source=deployment_source, deploy_changed_only=deploy_changed_only, enable_duplicate_filtering=enable_duplicate_filtering, deployment_name=deployment_name, data=data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentApi->create_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenant id for the deployment to be created. | [optional] 
 **deployment_source** | **str**| The source for the deployment to be created. | [optional] 
 **deploy_changed_only** | **bool**| A flag indicating whether the process engine should perform duplicate checking on a per-resource basis. If set to true, only those resources that have actually changed are deployed. Checks are made against resources included previous deployments of the same name and only against the latest versions of those resources. If set to true, the option enable-duplicate-filtering is overridden and set to true. | [optional] [default to False]
 **enable_duplicate_filtering** | **bool**| A flag indicating whether the process engine should perform duplicate checking for the deployment or not. This allows you to check if a deployment with the same name and the same resouces already exists and if true, not create a new deployment but instead return the existing deployment. The default value is false. | [optional] [default to False]
 **deployment_name** | **str**| The name for the deployment to be created. | [optional] 
 **data** | **file**| The binary data to create the deployment resource. It is possible to have more than one form part with different form part names for the binary data to create a deployment. | [optional] 

### Return type

[**DeploymentWithDefinitionsDto**](DeploymentWithDefinitionsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | Bad Request. In case one of the bpmn resources cannot be parsed.  See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#parse-exceptions) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_deployment**
> delete_deployment(id, cascade=cascade, skip_custom_listeners=skip_custom_listeners, skip_io_mappings=skip_io_mappings)



Deletes a deployment by id.

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
    api_instance = openapi_client.DeploymentApi(api_client)
    id = 'id_example' # str | The id of the deployment to be deleted.
cascade = False # bool | `true`, if all process instances, historic process instances and jobs for this deployment should be deleted. (optional) (default to False)
skip_custom_listeners = False # bool | `true`, if only the built-in ExecutionListeners should be notified with the end event. (optional) (default to False)
skip_io_mappings = False # bool | `true`, if all input/output mappings should not be invoked. (optional) (default to False)

    try:
        api_instance.delete_deployment(id, cascade=cascade, skip_custom_listeners=skip_custom_listeners, skip_io_mappings=skip_io_mappings)
    except ApiException as e:
        print("Exception when calling DeploymentApi->delete_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the deployment to be deleted. | 
 **cascade** | **bool**| &#x60;true&#x60;, if all process instances, historic process instances and jobs for this deployment should be deleted. | [optional] [default to False]
 **skip_custom_listeners** | **bool**| &#x60;true&#x60;, if only the built-in ExecutionListeners should be notified with the end event. | [optional] [default to False]
 **skip_io_mappings** | **bool**| &#x60;true&#x60;, if all input/output mappings should not be invoked. | [optional] [default to False]

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
**404** | A Deployment with the provided id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment**
> list[DeploymentDto] get_deployment(id)



Retrieves a deployment by id, according to the `Deployment` interface of the engine.

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
    api_instance = openapi_client.DeploymentApi(api_client)
    id = 'id_example' # str | The id of the deployment.

    try:
        api_response = api_instance.get_deployment(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentApi->get_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the deployment. | 

### Return type

[**list[DeploymentDto]**](DeploymentDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**404** | Deployment with given id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_resource**
> DeploymentResourceDto get_deployment_resource(id, resource_id)



Retrieves a deployment resource by resource id for the given deployment.

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
    api_instance = openapi_client.DeploymentApi(api_client)
    id = 'id_example' # str | The id of the deployment
resource_id = 'resource_id_example' # str | The id of the deployment resource

    try:
        api_response = api_instance.get_deployment_resource(id, resource_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentApi->get_deployment_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the deployment | 
 **resource_id** | **str**| The id of the deployment resource | 

### Return type

[**DeploymentResourceDto**](DeploymentResourceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**404** | Deployment Resource with given resource id or deployment id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_resource_data**
> file get_deployment_resource_data(id, resource_id)



Retrieves the binary content of a deployment resource for the given deployment by id.

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
    api_instance = openapi_client.DeploymentApi(api_client)
    id = 'id_example' # str | The id of the deployment.
resource_id = 'resource_id_example' # str | The id of the deployment resource.

    try:
        api_response = api_instance.get_deployment_resource_data(id, resource_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentApi->get_deployment_resource_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the deployment. | 
 **resource_id** | **str**| The id of the deployment resource. | 

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
**200** | Request successful. The media type of the response depends on the filename. |  -  |
**400** | Deployment Resource with given resource id or deployment id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_resources**
> list[DeploymentResourceDto] get_deployment_resources(id)



Retrieves all deployment resources of a given deployment.

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
    api_instance = openapi_client.DeploymentApi(api_client)
    id = 'id_example' # str | The id of the deployment to retrieve the deployment resources for.

    try:
        api_response = api_instance.get_deployment_resources(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentApi->get_deployment_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the deployment to retrieve the deployment resources for. | 

### Return type

[**list[DeploymentResourceDto]**](DeploymentResourceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**404** | Deployment resources for the given deployment do not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployments**
> list[DeploymentDto] get_deployments(id=id, name=name, name_like=name_like, source=source, without_source=without_source, tenant_id_in=tenant_id_in, without_tenant_id=without_tenant_id, include_deployments_without_tenant_id=include_deployments_without_tenant_id, after=after, before=before, sort_by=sort_by, sort_order=sort_order, first_result=first_result, max_results=max_results)



Queries for deployments that fulfill given parameters. Parameters may be the properties of deployments, such as the id or name or a range of the deployment time. The size of the result set can be retrieved by using the [Get Deployment count](https://docs.camunda.org/manual/7.13/reference/rest/deployment/get-query-count/) method.

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
    api_instance = openapi_client.DeploymentApi(api_client)
    id = 'id_example' # str | Filter by deployment id (optional)
name = 'name_example' # str | Filter by the deployment name. Exact match. (optional)
name_like = 'name_like_example' # str | Filter by the deployment name that the parameter is a substring of. The parameter can include the wildcard `%` to express like-strategy such as: starts with (`%`name), ends with (name`%`) or contains (`%`name`%`). (optional)
source = 'source_example' # str | Filter by the deployment source. (optional)
without_source = False # bool | Filter by the deployment source whereby source is equal to `null`. (optional) (default to False)
tenant_id_in = 'tenant_id_in_example' # str | Filter by a comma-separated list of tenant ids. A deployment must have one of the given tenant ids. (optional)
without_tenant_id = False # bool | Only include deployments which belong to no tenant. Value may only be `true`, as `false` is the default behavior. (optional) (default to False)
include_deployments_without_tenant_id = False # bool | Include deployments which belong to no tenant. Can be used in combination with `tenantIdIn`. Value may only be `true`, as `false` is the default behavior. (optional) (default to False)
after = '2013-10-20T19:20:30+01:00' # datetime | Restricts to all deployments after the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.000+0200`. (optional)
before = '2013-10-20T19:20:30+01:00' # datetime | Restricts to all deployments before the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.000+0200`. (optional)
sort_by = 'sort_by_example' # str | Sort the results lexicographically by a given criterion. Must be used in conjunction with the sortOrder parameter. (optional)
sort_order = 'sort_order_example' # str | Sort the results in a given order. Values may be asc for ascending order or desc for descending order. Must be used in conjunction with the sortBy parameter. (optional)
first_result = 56 # int | Pagination of results. Specifies the index of the first result to return. (optional)
max_results = 56 # int | Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. (optional)

    try:
        api_response = api_instance.get_deployments(id=id, name=name, name_like=name_like, source=source, without_source=without_source, tenant_id_in=tenant_id_in, without_tenant_id=without_tenant_id, include_deployments_without_tenant_id=include_deployments_without_tenant_id, after=after, before=before, sort_by=sort_by, sort_order=sort_order, first_result=first_result, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentApi->get_deployments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Filter by deployment id | [optional] 
 **name** | **str**| Filter by the deployment name. Exact match. | [optional] 
 **name_like** | **str**| Filter by the deployment name that the parameter is a substring of. The parameter can include the wildcard &#x60;%&#x60; to express like-strategy such as: starts with (&#x60;%&#x60;name), ends with (name&#x60;%&#x60;) or contains (&#x60;%&#x60;name&#x60;%&#x60;). | [optional] 
 **source** | **str**| Filter by the deployment source. | [optional] 
 **without_source** | **bool**| Filter by the deployment source whereby source is equal to &#x60;null&#x60;. | [optional] [default to False]
 **tenant_id_in** | **str**| Filter by a comma-separated list of tenant ids. A deployment must have one of the given tenant ids. | [optional] 
 **without_tenant_id** | **bool**| Only include deployments which belong to no tenant. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] [default to False]
 **include_deployments_without_tenant_id** | **bool**| Include deployments which belong to no tenant. Can be used in combination with &#x60;tenantIdIn&#x60;. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] [default to False]
 **after** | **datetime**| Restricts to all deployments after the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.000+0200&#x60;. | [optional] 
 **before** | **datetime**| Restricts to all deployments before the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.000+0200&#x60;. | [optional] 
 **sort_by** | **str**| Sort the results lexicographically by a given criterion. Must be used in conjunction with the sortOrder parameter. | [optional] 
 **sort_order** | **str**| Sort the results in a given order. Values may be asc for ascending order or desc for descending order. Must be used in conjunction with the sortBy parameter. | [optional] 
 **first_result** | **int**| Pagination of results. Specifies the index of the first result to return. | [optional] 
 **max_results** | **int**| Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. | [optional] 

### Return type

[**list[DeploymentDto]**](DeploymentDto.md)

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

# **get_deployments_count**
> CountResultDto get_deployments_count(id=id, name=name, name_like=name_like, source=source, without_source=without_source, tenant_id_in=tenant_id_in, without_tenant_id=without_tenant_id, include_deployments_without_tenant_id=include_deployments_without_tenant_id, after=after, before=before)



Queries for the number of deployments that fulfill given parameters. Takes the same parameters as the [Get Deployments](https://docs.camunda.org/manual/7.13/reference/rest/deployment/get-query/) method.

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
    api_instance = openapi_client.DeploymentApi(api_client)
    id = 'id_example' # str | Filter by deployment id (optional)
name = 'name_example' # str | Filter by the deployment name. Exact match. (optional)
name_like = 'name_like_example' # str | Filter by the deployment name that the parameter is a substring of. The parameter can include the wildcard `%` to express like-strategy such as: starts with (`%`name), ends with (name`%`) or contains (`%`name`%`). (optional)
source = 'source_example' # str | Filter by the deployment source. (optional)
without_source = False # bool | Filter by the deployment source whereby source is equal to `null`. (optional) (default to False)
tenant_id_in = 'tenant_id_in_example' # str | Filter by a comma-separated list of tenant ids. A deployment must have one of the given tenant ids. (optional)
without_tenant_id = False # bool | Only include deployments which belong to no tenant. Value may only be `true`, as `false` is the default behavior. (optional) (default to False)
include_deployments_without_tenant_id = False # bool | Include deployments which belong to no tenant. Can be used in combination with `tenantIdIn`. Value may only be `true`, as `false` is the default behavior. (optional) (default to False)
after = '2013-10-20T19:20:30+01:00' # datetime | Restricts to all deployments after the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.000+0200`. (optional)
before = '2013-10-20T19:20:30+01:00' # datetime | Restricts to all deployments before the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.000+0200`. (optional)

    try:
        api_response = api_instance.get_deployments_count(id=id, name=name, name_like=name_like, source=source, without_source=without_source, tenant_id_in=tenant_id_in, without_tenant_id=without_tenant_id, include_deployments_without_tenant_id=include_deployments_without_tenant_id, after=after, before=before)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentApi->get_deployments_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Filter by deployment id | [optional] 
 **name** | **str**| Filter by the deployment name. Exact match. | [optional] 
 **name_like** | **str**| Filter by the deployment name that the parameter is a substring of. The parameter can include the wildcard &#x60;%&#x60; to express like-strategy such as: starts with (&#x60;%&#x60;name), ends with (name&#x60;%&#x60;) or contains (&#x60;%&#x60;name&#x60;%&#x60;). | [optional] 
 **source** | **str**| Filter by the deployment source. | [optional] 
 **without_source** | **bool**| Filter by the deployment source whereby source is equal to &#x60;null&#x60;. | [optional] [default to False]
 **tenant_id_in** | **str**| Filter by a comma-separated list of tenant ids. A deployment must have one of the given tenant ids. | [optional] 
 **without_tenant_id** | **bool**| Only include deployments which belong to no tenant. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] [default to False]
 **include_deployments_without_tenant_id** | **bool**| Include deployments which belong to no tenant. Can be used in combination with &#x60;tenantIdIn&#x60;. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] [default to False]
 **after** | **datetime**| Restricts to all deployments after the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.000+0200&#x60;. | [optional] 
 **before** | **datetime**| Restricts to all deployments before the given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.000+0200&#x60;. | [optional] 

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
**400** | Returned if some of the query parameters are invalid, for example, if an invalid operator for variable comparison is used. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeploy**
> DeploymentWithDefinitionsDto redeploy(id, redeployment_dto=redeployment_dto)



Re-deploys an existing deployment.  The deployment resources to re-deploy can be restricted by using the properties `resourceIds` or `resourceNames`. If no deployment resources to re-deploy are passed then all existing resources of the given deployment are re-deployed.  **Warning**: Deployments can contain custom code in form of scripts or EL expressions to customize process behavior. This may be abused for remote execution of arbitrary code. See the section on [security considerations for custom code](https://docs.camunda.org/manual/7.13/user-guide/process-engine/securing-custom-code/) in the user guide for details.

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
    api_instance = openapi_client.DeploymentApi(api_client)
    id = 'id_example' # str | The id of the deployment to re-deploy.
redeployment_dto = {"resourceIds":["aResourceId"],"resourceNames":["aResourceName"],"source":"cockpit"} # RedeploymentDto |  (optional)

    try:
        api_response = api_instance.redeploy(id, redeployment_dto=redeployment_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeploymentApi->redeploy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the deployment to re-deploy. | 
 **redeployment_dto** | [**RedeploymentDto**](RedeploymentDto.md)|  | [optional] 

### Return type

[**DeploymentWithDefinitionsDto**](DeploymentWithDefinitionsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**404** | Deployment or a deployment resource for the given deployment does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

