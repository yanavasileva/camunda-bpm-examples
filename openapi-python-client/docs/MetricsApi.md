# openapi_client.MetricsApi

All URIs are relative to *http://localhost:8080/engine-rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metrics**](MetricsApi.md#get_metrics) | **GET** /metrics/{metrics-name}/sum | 
[**interval**](MetricsApi.md#interval) | **GET** /metrics | 


# **get_metrics**
> MetricsResultDto get_metrics(metrics_name, start_date=start_date, end_date=end_date)



Retrieves the `sum` (count) for a given metric.

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
    api_instance = openapi_client.MetricsApi(api_client)
    metrics_name = 'metrics_name_example' # str | The name of the metric.
start_date = '2013-10-20T19:20:30+01:00' # datetime | The start date (inclusive). (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | The end date (exclusive). (optional)

    try:
        api_response = api_instance.get_metrics(metrics_name, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->get_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metrics_name** | **str**| The name of the metric. | 
 **start_date** | **datetime**| The start date (inclusive). | [optional] 
 **end_date** | **datetime**| The end date (exclusive). | [optional] 

### Return type

[**MetricsResultDto**](MetricsResultDto.md)

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

# **interval**
> list[MetricsIntervalResultDto] interval(name=name, reporter=reporter, start_date=start_date, end_date=end_date, first_result=first_result, max_results=max_results, interval=interval, aggregate_by_reporter=aggregate_by_reporter)



Retrieves a list of metrics, aggregated for a given interval.

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
    api_instance = openapi_client.MetricsApi(api_client)
    name = 'name_example' # str | The name of the metric. (optional)
reporter = 'reporter_example' # str | The name of the reporter (host), on which the metrics was logged. This will have value provided by the [hostname configuration property](https://docs.camunda.org/manual/7.13/reference/deployment-descriptors/tags/process-engine/#hostname). (optional)
start_date = '2013-10-20T19:20:30+01:00' # datetime | The start date (inclusive). (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | The end date (exclusive). (optional)
first_result = 56 # int | Pagination of results. Specifies the index of the first result to return. (optional)
max_results = 56 # int | Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. (optional)
interval = '900' # str | The interval for which the metrics should be aggregated. Time unit is seconds. Default: The interval is set to 15 minutes (900 seconds). (optional) (default to '900')
aggregate_by_reporter = 'aggregate_by_reporter_example' # str | Aggregate metrics by reporter. (optional)

    try:
        api_response = api_instance.interval(name=name, reporter=reporter, start_date=start_date, end_date=end_date, first_result=first_result, max_results=max_results, interval=interval, aggregate_by_reporter=aggregate_by_reporter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->interval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the metric. | [optional] 
 **reporter** | **str**| The name of the reporter (host), on which the metrics was logged. This will have value provided by the [hostname configuration property](https://docs.camunda.org/manual/7.13/reference/deployment-descriptors/tags/process-engine/#hostname). | [optional] 
 **start_date** | **datetime**| The start date (inclusive). | [optional] 
 **end_date** | **datetime**| The end date (exclusive). | [optional] 
 **first_result** | **int**| Pagination of results. Specifies the index of the first result to return. | [optional] 
 **max_results** | **int**| Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. | [optional] 
 **interval** | **str**| The interval for which the metrics should be aggregated. Time unit is seconds. Default: The interval is set to 15 minutes (900 seconds). | [optional] [default to &#39;900&#39;]
 **aggregate_by_reporter** | **str**| Aggregate metrics by reporter. | [optional] 

### Return type

[**list[MetricsIntervalResultDto]**](MetricsIntervalResultDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | Returned if some of the query parameters are invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

