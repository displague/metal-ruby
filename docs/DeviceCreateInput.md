# DeviceCreateInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility** | **str** |  | 
**plan** | **str** |  | 
**hostname** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**billing_cycle** | **str** |  | [optional] 
**operating_system** | **str** |  | 
**always_pxe** | **bool** |  | [optional] 
**ipxe_script_url** | **str** |  | [optional] 
**userdata** | **str** |  | [optional] 
**locked** | **bool** |  | [optional] 
**customdata** | **object** |  | [optional] 
**hardware_reservation_id** | **str** |  | [optional] 
**spot_instance** | **bool** |  | [optional] 
**spot_price_max** | **float** |  | [optional] 
**termination_time** | **datetime** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**project_ssh_keys** | **list[str]** |  | [optional] 
**user_ssh_keys** | **list[str]** | The UUIDs of users whose SSH keys should be included on the provisioned device. | [optional] 
**features** | **list[str]** |  | [optional] 
**public_ipv4_subnet_size** | **float** | Deprecated. Use ip_addresses. Subnet range for addresses allocated to this device. Your project must have addresses available for a non-default request. | [optional] 
**private_ipv4_subnet_size** | **float** | Deprecated. Use ip_addresses. Subnet range for addresses allocated to this device. | [optional] 
**ip_addresses** | [**list[DeviceCreateInputIpAddresses]**](DeviceCreateInputIpAddresses.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


