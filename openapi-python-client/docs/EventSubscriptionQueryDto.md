# EventSubscriptionQueryDto

A event subscription query which retrieves a list of event subscriptions
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_subscription_id** | **str** | The id of the event subscription. | [optional] 
**event_name** | **str** | The name of the event this subscription belongs to as defined in the process model. | [optional] 
**event_type** | **str** | The type of the event subscription. | [optional] 
**execution_id** | **str** | The execution that is subscribed on the referenced event. | [optional] 
**process_instance_id** | **str** | The process instance this subscription belongs to. | [optional] 
**activity_id** | **str** | The identifier of the activity that this event subscription belongs to. This could for example be the id of a receive task. | [optional] 
**tenant_id_in** | **list[str]** | Filter by a comma-separated list of tenant ids. Only select subscriptions that belong to one of the given tenant ids. | [optional] 
**without_tenant_id** | **bool** | Only select subscriptions which have no tenant id. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] 
**include_event_subscriptions_without_tenant_id** | **bool** | Select event subscriptions which have no tenant id. Can be used in combination with tenantIdIn parameter. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. | [optional] 
**sorting** | [**list[EventSubscriptionQueryDtoSorting]**](EventSubscriptionQueryDtoSorting.md) | Apply sorting of the result | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


