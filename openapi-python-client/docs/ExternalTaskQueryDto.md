# ExternalTaskQueryDto

A JSON object with the following properties:
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_task_id** | **str** | Filter by an external task&#39;s id. | [optional] 
**external_task_id_in** | **list[str]** | Filter by the comma-separated list of external task ids. | [optional] 
**topic_name** | **str** | Filter by an external task topic. | [optional] 
**worker_id** | **str** | Filter by the id of the worker that the task was most recently locked by. | [optional] 
**locked** | **bool** | Only include external tasks that are currently locked (i.e., they have a lock time and it has not expired). Value may only be &#x60;true&#x60;, as &#x60;false&#x60; matches any external task. | [optional] 
**not_locked** | **bool** | Only include external tasks that are currently not locked (i.e., they have no lock or it has expired). Value may only be &#x60;true&#x60;, as &#x60;false&#x60; matches any external task. | [optional] 
**with_retries_left** | **bool** | Only include external tasks that have a positive (&amp;gt; 0) number of retries (or &#x60;null&#x60;). Value may only be &#x60;true&#x60;, as &#x60;false&#x60; matches any external task. | [optional] 
**no_retries_left** | **bool** | Only include external tasks that have 0 retries. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; matches any external task. | [optional] 
**lock_expiration_after** | **datetime** | Restrict to external tasks that have a lock that expires after a given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.000+0200&#x60;. | [optional] 
**lock_expiration_before** | **datetime** | Restrict to external tasks that have a lock that expires before a given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;, e.g., &#x60;2013-01-23T14:42:45.000+0200&#x60;. | [optional] 
**activity_id** | **str** | Filter by the id of the activity that an external task is created for. | [optional] 
**activity_id_in** | **list[str]** | Filter by the comma-separated list of ids of the activities that an external task is created for. | [optional] 
**execution_id** | **str** | Filter by the id of the execution that an external task belongs to. | [optional] 
**process_instance_id** | **str** | Filter by the id of the process instance that an external task belongs to. | [optional] 
**process_instance_id_in** | **list[str]** | Filter by a comma-separated list of process instance ids that an external task may belong to. | [optional] 
**process_definition_id** | **str** | Filter by the id of the process definition that an external task belongs to. | [optional] 
**tenant_id_in** | **list[str]** | Filter by a comma-separated list of tenant ids. An external task must have one of the given tenant ids. | [optional] 
**active** | **bool** | Only include active tasks. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; matches any external task. | [optional] 
**suspended** | **bool** | Only include suspended tasks. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; matches any external task. | [optional] 
**priority_higher_than_or_equals** | **int** | Only include jobs with a priority higher than or equal to the given value. Value must be a valid &#x60;long&#x60; value. | [optional] 
**priority_lower_than_or_equals** | **int** | Only include jobs with a priority lower than or equal to the given value. Value must be a valid &#x60;long&#x60; value. | [optional] 
**sorting** | [**list[ExternalTaskQueryDtoSorting]**](ExternalTaskQueryDtoSorting.md) | A JSON array of criteria to sort the result by. Each element of the array is a JSON object that                     specifies one ordering. The position in the array identifies the rank of an ordering, i.e., whether                     it is primary, secondary, etc. The ordering objects have the following properties:                      **Note:** The &#x60;sorting&#x60; properties will not be applied to the External Task count query. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


