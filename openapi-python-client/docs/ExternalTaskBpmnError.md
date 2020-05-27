# ExternalTaskBpmnError

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**worker_id** | **str** | The id of the worker that reports the failure. Must match the id of the worker who has most recently locked the task. | [optional] 
**error_code** | **str** | An error code that indicates the predefined error. It is used to identify the BPMN error handler. | [optional] 
**error_message** | **str** | An error message that describes the error. | [optional] 
**variables** | [**dict(str, VariableValueDto)**](VariableValueDto.md) | A JSON object containing variable key-value pairs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


