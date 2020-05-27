# TaskDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The task id. | [optional] 
**name** | **str** | The task name. | [optional] 
**assignee** | **str** | The assignee&#39;s id. | [optional] 
**owner** | **str** | The owner&#39;s id. | [optional] 
**created** | **datetime** | The date the task was created on. [Default format](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/) &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;. | [optional] 
**due** | **datetime** | The task&#39;s due date. [Default format](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/) &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;. | [optional] 
**follow_up** | **datetime** | The follow-up date for the task. [Default format](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/) &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ&#x60;. | [optional] 
**delegation_state** | **str** | The task&#39;s delegation state. Possible values are &#x60;PENDING&#x60; and &#x60;RESOLVED&#x60;. | [optional] 
**description** | **str** | The task&#39;s description. | [optional] 
**execution_id** | **str** | The id of the execution the task belongs to. | [optional] 
**parent_task_id** | **str** | The id the parent task, if this task is a subtask. | [optional] 
**priority** | **int** | The task&#39;s priority. | [optional] 
**process_definition_id** | **str** | The id of the process definition the task belongs to. | [optional] 
**process_instance_id** | **str** | The id of the process instance the task belongs to. | [optional] 
**case_execution_id** | **str** | The id of the case execution the task belongs to. | [optional] 
**case_definition_id** | **str** | The id of the case definition the task belongs to. | [optional] 
**case_instance_id** | **str** | The id of the case instance the task belongs to. | [optional] 
**task_definition_key** | **str** | The task&#39;s key. | [optional] 
**suspended** | **bool** | Whether the task belongs to a process instance that is suspended. | [optional] 
**form_key** | **str** | If not &#x60;null&#x60;, the form key for the task. | [optional] 
**tenant_id** | **str** | If not &#x60;null&#x60;, the tenant id of the task. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


