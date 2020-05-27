# openapi_client.ConditionApi

All URIs are relative to *http://localhost:8080/engine-rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**evaluate_condition**](ConditionApi.md#evaluate_condition) | **POST** /condition | 


# **evaluate_condition**
> list[ProcessInstanceDto] evaluate_condition(evaluation_condition_dto=evaluation_condition_dto)



Triggers evaluation of conditions for conditional start event(s).  Internally this maps to the engines condition evaluation builder method ConditionEvaluationBuilder#evaluateStartConditions().  For more information see the [Conditional Start Events](https://docs.camunda.org/manual/7.13/reference/bpmn20/events/conditional-events/#conditional-start-event) section of the [BPMN 2.0 Implementation Reference](https://docs.camunda.org/manual/7.13/reference/bpmn20/).

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
    api_instance = openapi_client.ConditionApi(api_client)
    evaluation_condition_dto = {"variables":{"temperature":{"value":24,"type":"Integer","valueInfo":{"transient":true}},"city":{"value":"Parma","type":"String"}},"businessKey":"aBusinessKey","tenantId":"aTenantId"} # EvaluationConditionDto |  (optional)

    try:
        api_response = api_instance.evaluate_condition(evaluation_condition_dto=evaluation_condition_dto)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConditionApi->evaluate_condition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evaluation_condition_dto** | [**EvaluationConditionDto**](EvaluationConditionDto.md)|  | [optional] 

### Return type

[**list[ProcessInstanceDto]**](ProcessInstanceDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful. |  -  |
**400** | If both tenantId and withoutTenantId are supplied. |  -  |
**403** | If the user is not allowed to start the process instance of the process definition, which start condition was evaluated to &#x60;true&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

