# HardwareUpdateInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | [optional] 
**u_spaces** | **int** |  | [optional] 
**model_number** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**server_rack_id** | **str** |  | [optional] 
**leased** | **bool** |  | [optional] 
**lease_number** | **str** |  | [optional] 
**lease_expires_at** | **datetime** |  | [optional] 
**arch** | **str** |  | [optional] 
**dhcp_group** | **str** |  | [optional] 
**efi_boot** | **bool** |  | [optional] 
**bios_password** | **str** |  | [optional] 
**maintenance_state** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**static_name** | **str** |  | [optional] 
**uefi_supports_rfc3021** | **bool** |  | [optional] 
**preinstalled_operating_system_version_id** | **str** |  | [optional] 
**link_aggregation** | **str** |  | [optional] 
**provisioner** | **str** |  | [optional] 
**supported_networking** | **[str]** |  | [optional] 
**services** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**management** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**data** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Holds custom data depending on the hardware type. Any attribute set here can also be set as part of the hardware object | [optional] 
**role** | **str** | Role of the hardware. Will affect how the hardware will be named. Its required for certain hardware types. | [optional] 
**vlan_id** | **int** | On certain server nodes/sleds (t1.small.x86 and x1.small.x86), it describes the internal VLAN used to route traffic inside the BladeSwitch. | [optional] 
**tpm** | **bool** | On servers, describe if the server has a TPM card. | [optional] 
**switch_short_id** | **str** | On servers, describe the switch the server is connected too. If left empty, the value will be auto set on creation. | [optional] 
**is_primary** | **bool** | Switch attribute. On Arista switches, indicates which of the 2 Arista switches in mlag mode is the primary. Its used to properly configure the switch through Narhwal. | [optional] 
**loopback_ip** | **str** | Switch attribute. Specify the loopback_ip of the switch. Currently is not used in our automation. | [optional] 
**vrf** | **str** | Switch attribute. Specify the Virtual Routing and Forwarding tag used on the configuration. | [optional] 
**exclude_from_narwhal** | **bool** | Switch attribute. If set to true, any switch configuration task created by our automation will be skipped for this switch | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


