# openapi_client.TaskIdentityLinkApi

All URIs are relative to *http://localhost:8080/engine-rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_identity_link**](TaskIdentityLinkApi.md#add_identity_link) | **POST** /task/{id}/identity-links | 
[**delete_identity_link**](TaskIdentityLinkApi.md#delete_identity_link) | **POST** /task/{id}/identity-links/delete | 
[**get_identity_links**](TaskIdentityLinkApi.md#get_identity_links) | **GET** /task/{id}/identity-links | 


# **add_identity_link**
> add_identity_link(id, identity_link_dto=identity_link_dto)



Adds an identity link to a task by id. Can be used to link any user or group to a task and specify a relation.

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
    api_instance = openapi_client.TaskIdentityLinkApi(api_client)
    id = 'id_example' # str | The id of the task to add a link to.
identity_link_dto = {"groupId":"aNewGroupId","type":"candidate"} # IdentityLinkDto |  (optional)

    try:
        api_instance.add_identity_link(id, identity_link_dto=identity_link_dto)
    except ApiException as e:
        print("Exception when calling TaskIdentityLinkApi->add_identity_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to add a link to. | 
 **identity_link_dto** | [**IdentityLinkDto**](IdentityLinkDto.md)|  | [optional] 

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
**400** | Task with given id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identity_link**
> delete_identity_link(id, identity_link_dto=identity_link_dto)



Removes an identity link from a task by id

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
    api_instance = openapi_client.TaskIdentityLinkApi(api_client)
    id = 'id_example' # str | The id of the task to remove a link from.
identity_link_dto = {"groupId":"theOldGroupId","type":"candidate"} # IdentityLinkDto |  (optional)

    try:
        api_instance.delete_identity_link(id, identity_link_dto=identity_link_dto)
    except ApiException as e:
        print("Exception when calling TaskIdentityLinkApi->delete_identity_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to remove a link from. | 
 **identity_link_dto** | [**IdentityLinkDto**](IdentityLinkDto.md)|  | [optional] 

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
**400** | Task with given id does not exist. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_links**
> list[IdentityLinkDto] get_identity_links(id, type=type)



Gets the identity links for a task by id, which are the users and groups that are in *some* relation to it (including assignee and owner).

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
    api_instance = openapi_client.TaskIdentityLinkApi(api_client)
    id = 'id_example' # str | The id of the task to retrieve the identity links for.
type = 'type_example' # str | Filter by the type of links to include. (optional)

    try:
        api_response = api_instance.get_identity_links(id, type=type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskIdentityLinkApi->get_identity_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to retrieve the identity links for. | 
 **type** | **str**| Filter by the type of links to include. | [optional] 

### Return type

[**list[IdentityLinkDto]**](IdentityLinkDto.md)

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

