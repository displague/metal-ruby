# InstancesBatchCreateInputBatches


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 
**hostnames** | **[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**billing_cycle** | **str** |  | [optional] 
**operating_system** | **str** |  | [optional] 
**always_pxe** | **bool** |  | [optional] 
**userdata** | **str** |  | [optional] 
**locked** | **bool** |  | [optional] 
**termination_time** | **datetime** |  | [optional] 
**tags** | **[str]** |  | [optional] 
**project_ssh_keys** | **[str]** |  | [optional] 
**user_ssh_keys** | **[str]** | The UUIDs of users whose SSH keys should be included on the provisioned device. | [optional] 
**features** | **[str]** |  | [optional] 
**customdata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**ip_addresses** | [**[InstancesBatchCreateInputIpAddresses]**](InstancesBatchCreateInputIpAddresses.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


