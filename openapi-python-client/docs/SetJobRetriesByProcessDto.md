# SetJobRetriesByProcessDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**process_instances** | **list[str]** | A list of process instance ids to fetch jobs, for which retries will be set. | [optional] 
**retries** | **int** | An integer representing the number of retries. Please note that the value cannot be negative or null. | [optional] 
**process_instance_query** | [**ProcessInstanceQueryDto**](ProcessInstanceQueryDto.md) |  | [optional] 
**historic_process_instance_query** | [**HistoricProcessInstanceQueryDto**](HistoricProcessInstanceQueryDto.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


