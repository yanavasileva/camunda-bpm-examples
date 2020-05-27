# TransitionInstanceDto

A JSON object corresponding to the Activity Instance tree of the given process instance.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the transition instance. | [optional] 
**parent_activity_instance_id** | **str** | The id of the parent activity instance, for example a sub process instance. | [optional] 
**activity_id** | **str** | The id of the activity that this instance enters (asyncBefore job) or leaves (asyncAfter job) | [optional] 
**activity_name** | **str** | The name of the activity that this instance enters (asyncBefore job) or leaves (asyncAfter job) | [optional] 
**activity_type** | **str** | The type of the activity that this instance enters (asyncBefore job) or leaves (asyncAfter job) | [optional] 
**process_instance_id** | **str** | The id of the process instance this instance is part of. | [optional] 
**process_definition_id** | **str** | The id of the process definition. | [optional] 
**execution_id** | **str** | The execution id. | [optional] 
**incident_ids** | **list[str]** | A list of incident ids. | [optional] 
**incidents** | [**list[ActivityInstanceIncidentDto]**](ActivityInstanceIncidentDto.md) | A list of JSON objects containing incident specific properties: * &#x60;id&#x60;: the id of the incident * &#x60;activityId&#x60;: the activity id in which the incident occurred | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


