# Device


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**short_id** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**tags** | **[str]** |  | [optional] 
**image_url** | **str** |  | [optional] 
**billing_cycle** | **str** |  | [optional] 
**user** | **str** |  | [optional] 
**iqn** | **str** |  | [optional] 
**locked** | **bool** |  | [optional] 
**bonding_mode** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**spot_instance** | **bool** |  | [optional] 
**spot_price_max** | **float** |  | [optional] 
**termination_time** | **datetime** |  | [optional] 
**customdata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**provisioning_percentage** | **float** |  | [optional] 
**operating_system** | [**OperatingSystem**](OperatingSystem.md) |  | [optional] 
**always_pxe** | **bool** |  | [optional] 
**ipxe_script_url** | **str** |  | [optional] 
**location** | [**HardwareLocation**](HardwareLocation.md) |  | [optional] 
**facility** | [**Facility**](Facility.md) |  | [optional] 
**plan** | [**Plan**](Plan.md) |  | [optional] 
**userdata** | **str** |  | [optional] 
**root_password** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**project** | [**Href**](Href.md) |  | [optional] 
**project_lite** | [**Href**](Href.md) |  | [optional] 
**volumes** | [**[Href]**](Href.md) |  | [optional] 
**hardware_reservation** | [**Href**](Href.md) |  | [optional] 
**ssh_keys** | [**[Href]**](Href.md) |  | [optional] 
**ip_addresses** | [**[IPAssignment]**](IPAssignment.md) |  | [optional] 
**provisioning_events** | [**[Event]**](Event.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


