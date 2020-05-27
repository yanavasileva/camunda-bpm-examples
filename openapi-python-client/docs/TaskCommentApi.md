# openapi_client.TaskCommentApi

All URIs are relative to *http://localhost:8080/engine-rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_comment**](TaskCommentApi.md#create_comment) | **POST** /task/{id}/comment/create | 
[**get_comment**](TaskCommentApi.md#get_comment) | **GET** /task/{id}/comment/{commentId} | 
[**get_comments**](TaskCommentApi.md#get_comments) | **GET** /task/{id}/comment | 


# **create_comment**
> CommentDto create_comment(id, comment_dto=comment_dto)



Creates a comment for a task by id.

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
    api_instance = openapi_client.TaskCommentApi(api_client)
    id = 'id_example' # str | The id of the task to add the comment to.
comment_dto = {"message":"a task comment"} # CommentDto | **Note:** Only the `message` property will be used. Every other property passed to this endpoint will be ignored. (optional)

    try:
        api_response = api_instance.create_comment(id, comment_dto=comment_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskCommentApi->create_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to add the comment to. | 
 **comment_dto** | [**CommentDto**](CommentDto.md)| **Note:** Only the &#x60;message&#x60; property will be used. Every other property passed to this endpoint will be ignored. | [optional] 

### Return type

[**CommentDto**](CommentDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | The task does not exist or no comment message was submitted. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**403** | The history of the engine is disabled. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment**
> CommentDto get_comment(id, comment_id)



Retrieves a task comment by task id and comment id.

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
    api_instance = openapi_client.TaskCommentApi(api_client)
    id = 'id_example' # str | The id of the task.
comment_id = 'comment_id_example' # str | The id of the comment to be retrieved.

    try:
        api_response = api_instance.get_comment(id, comment_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskCommentApi->get_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task. | 
 **comment_id** | **str**| The id of the comment to be retrieved. | 

### Return type

[**CommentDto**](CommentDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**404** | The task or comment with given task and comment id does not exist, or the history of the engine is disabled. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comments**
> list[CommentDto] get_comments(id)



Gets the comments for a task by id.

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
    api_instance = openapi_client.TaskCommentApi(api_client)
    id = 'id_example' # str | The id of the task to retrieve the comments for.

    try:
        api_response = api_instance.get_comments(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskCommentApi->get_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the task to retrieve the comments for. | 

### Return type

[**list[CommentDto]**](CommentDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**404** | No task exists for the given task id. See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

