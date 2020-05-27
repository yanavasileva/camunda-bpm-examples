# openapi_client.MessageApi

All URIs are relative to *http://localhost:8080/engine-rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deliver_message**](MessageApi.md#deliver_message) | **POST** /message | 


# **deliver_message**
> list[MessageCorrelationResultWithVariableDto] deliver_message(correlation_message_dto=correlation_message_dto)



Correlates a message to the process engine to either trigger a message start event or an intermediate message  catching event. Internally this maps to the engine's message correlation builder methods `MessageCorrelationBuilder#correlateWithResult()` and `MessageCorrelationBuilder#correlateAllWithResult()`. For more information about the correlation behavior, see the [Message Events](https://docs.camunda.org/manual/7.13/bpmn20/events/message-events/) section of the [BPMN 2.0 Implementation Reference](https://docs.camunda.org/manual/7.13/reference/bpmn20/).

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
    api_instance = openapi_client.MessageApi(api_client)
    correlation_message_dto = {"messageName":"aMessage","businessKey":"aBusinessKey","correlationKeys":{"aVariable":{"value":"aValue","type":"String"}},"processVariables":{"aVariable":{"value":"aNewValue","type":"String","valueInfo":{"transient":true}},"anotherVariable":{"value":true,"type":"Boolean"}}} # CorrelationMessageDto |  (optional)

    try:
        api_response = api_instance.deliver_message(correlation_message_dto=correlation_message_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessageApi->deliver_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **correlation_message_dto** | [**CorrelationMessageDto**](CorrelationMessageDto.md)|  | [optional] 

### Return type

[**list[MessageCorrelationResultWithVariableDto]**](MessageCorrelationResultWithVariableDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. The property &#x60;resultEnabled&#x60; in the request body was &#x60;true&#x60;. The &#x60;variables&#x60; property is only returned, if the property variablesInResultEnable&#x60; was set to &#x60;true&#x60; in the request. |  -  |
**204** | Request successful. The property &#x60;resultEnabled&#x60; in the request body was &#x60;false&#x60; (Default). |  -  |
**400** | Returned if: * no &#x60;messageName&#x60; was supplied * both &#x60;tenantId&#x60; and &#x60;withoutTenantId&#x60; are supplied * the message has not been correlated to exactly one entity (execution or process definition) * the variable value or type is invalid, for example if the value could not be parsed to an Integer value or the passed variable type is not supported.  See the [Introduction](https://docs.camunda.org/manual/7.13/reference/rest/overview/#error-handling) for the error response format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

