# openapi_client.EngineApi

All URIs are relative to *http://localhost:8080/engine-rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_process_engine_names**](EngineApi.md#get_process_engine_names) | **GET** /engine | 


# **get_process_engine_names**
> list[ProcessEngineDto] get_process_engine_names()



Retrieves the names of all process engines available on your platform. **Note**: You cannot prepend `/engine/{name}` to this method.

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
    api_instance = openapi_client.EngineApi(api_client)
    
    try:
        api_response = api_instance.get_process_engine_names()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EngineApi->get_process_engine_names: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ProcessEngineDto]**](ProcessEngineDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

