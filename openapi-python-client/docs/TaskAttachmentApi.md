# openapi_client.TaskAttachmentApi

All URIs are relative to *http://localhost:8080/engine-rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_attachment**](TaskAttachmentApi.md#add_attachment) | **POST** /task/{id}/attachment/create | 
[**delete_attachment**](TaskAttachmentApi.md#delete_attachment) | **DELETE** /task/{id}/attachment/{attachmentId} | 
[**get_attachment**](TaskAttachmentApi.md#get_attachment) | **GET** /task/{id}/attachment/{attachmentId} | 
[**get_attachment_data**](TaskAttachmentApi.md#get_attachment_data) | **GET** /task/{id}/attachment/{attachmentId}/data | 
[**get_attachments**](TaskAttachmentApi.md#get_attachments) | **GET** /task/{id}/attachment | 


# **add_attachment**
> AttachmentDto add_attachment(id, attachment_name=attachment_name, attachment_description=attachment_description, attachment_type=attachment_type, url=url, content=content)



Creates an attachment for a task.

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
    api_instance = openapi_client.TaskAttachmentApi(api_client)
    id = 'id_example' # str | The id of the task to add the attachment to.
attachment_name = 'attachment_name_example' # str | The name of the attachment. (optional)
attachment_description = 'attachment_description_example' # str | The description of the attachment. (optional)
attachment_type = 'attachment_type_example' # str | The type of the attachment. (optional)
url = 'url_example' # str | The url to the remote content of the attachment. (optional)
content = '/path/to/file' # file | The content of the attachment. (optional)

    try:
        api_response = api_instance.add_attachment(id, attachment_name=attachment_name, attachment_description=attachment_description, attachment_type=attachment_type, url=url, content=content)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskAttachmentApi->add_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to add the attachment to. | 
 **attachment_name** | **str**| The name of the attachment. | [optional] 
 **attachment_description** | **str**| The description of the attachment. | [optional] 
 **attachment_type** | **str**| The type of the attachment. | [optional] 
 **url** | **str**| The url to the remote content of the attachment. | [optional] 
 **content** | **file**| The content of the attachment. | [optional] 

### Return type

[**AttachmentDto**](AttachmentDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | The task does not exists or task id is null. No content or url to remote content exists. See the [Introduction](/reference/rest/overview/#error-handling) for the error response format. |  -  |
**403** | The history of the engine is disabled. See the [Introduction](/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_attachment**
> delete_attachment(id, attachment_id)



Removes an attachment from a task by id.

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
    api_instance = openapi_client.TaskAttachmentApi(api_client)
    id = 'id_example' # str | The id of the task.
attachment_id = 'attachment_id_example' # str | The id of the attachment to be removed.

    try:
        api_instance.delete_attachment(id, attachment_id)
    except ApiException as e:
        print("Exception when calling TaskAttachmentApi->delete_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task. | 
 **attachment_id** | **str**| The id of the attachment to be removed. | 

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
**403** | The history of the engine is disabled. See the [Introduction](/reference/rest/overview/#error-handling) for the error response format. |  -  |
**404** | A Task Attachment for the given task id and attachment id does not exist. See the [Introduction](/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment**
> AttachmentDto get_attachment(id, attachment_id)



Retrieves a task attachment by task id and attachment id.

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
    api_instance = openapi_client.TaskAttachmentApi(api_client)
    id = 'id_example' # str | The id of the task.
attachment_id = 'attachment_id_example' # str | The id of the attachment to be retrieved.

    try:
        api_response = api_instance.get_attachment(id, attachment_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskAttachmentApi->get_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task. | 
 **attachment_id** | **str**| The id of the attachment to be retrieved. | 

### Return type

[**AttachmentDto**](AttachmentDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**404** | The attachment for the given task and attachment id does not exist or the history of the engine is disabled.  See the [Introduction](/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment_data**
> file get_attachment_data(id, attachment_id)



Retrieves the binary content of a task attachment by task id and attachment id.

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
    api_instance = openapi_client.TaskAttachmentApi(api_client)
    id = 'id_example' # str | The id of the task.
attachment_id = 'attachment_id_example' # str | The id of the attachment to be retrieved.

    try:
        api_response = api_instance.get_attachment_data(id, attachment_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskAttachmentApi->get_attachment_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task. | 
 **attachment_id** | **str**| The id of the attachment to be retrieved. | 

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
**200** | Request successful. |  -  |
**404** | The attachment content for the given task id and attachment id does not exist, or the history of the engine is disabled.  See the [Introduction](/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachments**
> list[AttachmentDto] get_attachments(id)



Gets the attachments for a task.

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
    api_instance = openapi_client.TaskAttachmentApi(api_client)
    id = 'id_example' # str | The id of the task to retrieve the attachments for.

    try:
        api_response = api_instance.get_attachments(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskAttachmentApi->get_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to retrieve the attachments for. | 

### Return type

[**list[AttachmentDto]**](AttachmentDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**404** | No task exists for the given task id. See the [Introduction](/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

