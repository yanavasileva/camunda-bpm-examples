# openapi_client.SchemaLogApi

All URIs are relative to *http://localhost:8080/engine-rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_schema_log**](SchemaLogApi.md#get_schema_log) | **GET** /schema/log | 
[**query_schema_log**](SchemaLogApi.md#query_schema_log) | **POST** /schema/log | 


# **get_schema_log**
> list[SchemaLogEntryDto] get_schema_log(version=version, first_result=first_result, max_results=max_results)



Queries for schema log entries that fulfill given parameters.

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
    api_instance = openapi_client.SchemaLogApi(api_client)
    version = 'version_example' # str | Only return schema log entries with a specific version. (optional)
first_result = 56 # int | Pagination of results. Specifies the index of the first result to return. (optional)
max_results = 56 # int | Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. (optional)

    try:
        api_response = api_instance.get_schema_log(version=version, first_result=first_result, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SchemaLogApi->get_schema_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Only return schema log entries with a specific version. | [optional] 
 **first_result** | **int**| Pagination of results. Specifies the index of the first result to return. | [optional] 
 **max_results** | **int**| Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. | [optional] 

### Return type

[**list[SchemaLogEntryDto]**](SchemaLogEntryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. **Note**: In order to get any results a user of group &#x60;camunda-admin&#x60; must be authenticated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_schema_log**
> list[SchemaLogEntryDto] query_schema_log(first_result=first_result, max_results=max_results, schema_log_query_dto=schema_log_query_dto)



Queries for schema log entries that fulfill given parameters.

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
    api_instance = openapi_client.SchemaLogApi(api_client)
    first_result = 56 # int | Pagination of results. Specifies the index of the first result to return. (optional)
max_results = 56 # int | Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. (optional)
schema_log_query_dto = {"version":"7.11.0","sortBy":"timestamp","sortOrder":"asc"} # SchemaLogQueryDto |  (optional)

    try:
        api_response = api_instance.query_schema_log(first_result=first_result, max_results=max_results, schema_log_query_dto=schema_log_query_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SchemaLogApi->query_schema_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_result** | **int**| Pagination of results. Specifies the index of the first result to return. | [optional] 
 **max_results** | **int**| Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. | [optional] 
 **schema_log_query_dto** | [**SchemaLogQueryDto**](SchemaLogQueryDto.md)|  | [optional] 

### Return type

[**list[SchemaLogEntryDto]**](SchemaLogEntryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. **Note**: In order to get any results a user of group camunda-admin must be authenticated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

