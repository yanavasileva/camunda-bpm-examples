# ProcessInstanceDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the process instance. | [optional] 
**definition_id** | **str** | The id of the process definition that this process instance belongs to. | [optional] 
**business_key** | **str** | The business key of the process instance. | [optional] 
**case_instance_id** | **str** | The id of the case instance associated with the process instance. | [optional] 
**ended** | **bool** | A flag indicating whether the process instance has ended or not. Deprecated: will always be false! | [optional] 
**suspended** | **bool** | A flag indicating whether the process instance is suspended or not. | [optional] 
**tenant_id** | **str** | The tenant id of the process instance. | [optional] 
**links** | [**list[AtomLink]**](AtomLink.md) | The links associated to this resource, with &#x60;method&#x60;, &#x60;href&#x60; and &#x60;rel&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


