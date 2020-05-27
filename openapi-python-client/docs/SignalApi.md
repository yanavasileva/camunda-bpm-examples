# openapi_client.SignalApi

All URIs are relative to *http://localhost:8080/engine-rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**throw_signal**](SignalApi.md#throw_signal) | **POST** /signal | 


# **throw_signal**
> throw_signal(signal_dto=signal_dto)



A signal is an event of global scope (broadcast semantics) and is delivered to all active handlers. Internally this maps to the engine's signal event received builder method `RuntimeService#createSignalEvent()`. For more information about the signal behavior, see the [Signal Events](https://docs.camunda.org/manual/7.13/reference/bpmn20/events/signal-events/) section of the [BPMN 2.0 Implementation Reference](https://docs.camunda.org/manual/7.13/reference/bpmn20/).

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
    api_instance = openapi_client.SignalApi(api_client)
    signal_dto = {"name":"policy_conditions_changed","variables":{"newTimePeriodInMonth":{"value":24}}} # SignalDto |  (optional)

    try:
        api_instance.throw_signal(signal_dto=signal_dto)
    except ApiException as e:
        print("Exception when calling SignalApi->throw_signal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signal_dto** | [**SignalDto**](SignalDto.md)|  | [optional] 

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
**400** | Returned if:  * no name was given * the variable value or type is invalid, for example if the value could not be parsed to an integer value or the passed variable type is not supported * a tenant id and an execution id is specified.  See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**403** | Returned if the user is not allowed to throw a signal event.  See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |
**500** | Returned if a single execution is specified and no such execution exists or has not subscribed to the signal.  See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

