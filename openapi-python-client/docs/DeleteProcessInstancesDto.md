# DeleteProcessInstancesDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**process_instance_ids** | **list[str]** | A list process instance ids to delete. | [optional] 
**delete_reason** | **str** | A string with delete reason. | [optional] 
**skip_custom_listeners** | **bool** | Skip execution listener invocation for activities that are started or ended as part of this request. | [optional] 
**skip_subprocesses** | **bool** | Skip deletion of the subprocesses related to deleted processes as part of this request. | [optional] 
**process_instance_query** | [**ProcessInstanceQueryDto**](ProcessInstanceQueryDto.md) |  | [optional] 
**historic_process_instance_query** | [**HistoricProcessInstanceQueryDto**](HistoricProcessInstanceQueryDto.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


