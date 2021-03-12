# OpenapiClient::DeviceCreateInput

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **facility** | **String** |  |  |
| **plan** | **String** |  |  |
| **hostname** | **String** |  | [optional] |
| **description** | **String** |  | [optional] |
| **billing_cycle** | **String** |  | [optional] |
| **operating_system** | **String** |  |  |
| **always_pxe** | **Boolean** |  | [optional] |
| **ipxe_script_url** | **String** |  | [optional] |
| **userdata** | **String** |  | [optional] |
| **locked** | **Boolean** |  | [optional] |
| **customdata** | **Object** |  | [optional] |
| **hardware_reservation_id** | **String** |  | [optional] |
| **spot_instance** | **Boolean** |  | [optional] |
| **spot_price_max** | **Float** |  | [optional] |
| **termination_time** | **Time** |  | [optional] |
| **tags** | **Array&lt;String&gt;** |  | [optional] |
| **project_ssh_keys** | **Array&lt;String&gt;** |  | [optional] |
| **user_ssh_keys** | **Array&lt;String&gt;** | The UUIDs of users whose SSH keys should be included on the provisioned device. | [optional] |
| **features** | **Array&lt;String&gt;** |  | [optional] |
| **public_ipv4_subnet_size** | **Float** | Deprecated. Use ip_addresses. Subnet range for addresses allocated to this device. Your project must have addresses available for a non-default request. | [optional] |
| **private_ipv4_subnet_size** | **Float** | Deprecated. Use ip_addresses. Subnet range for addresses allocated to this device. | [optional] |
| **ip_addresses** | [**Array&lt;DeviceCreateInputIpAddresses&gt;**](DeviceCreateInputIpAddresses.md) |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::DeviceCreateInput.new(
  facility: null,
  plan: null,
  hostname: null,
  description: null,
  billing_cycle: null,
  operating_system: null,
  always_pxe: null,
  ipxe_script_url: null,
  userdata: null,
  locked: null,
  customdata: null,
  hardware_reservation_id: null,
  spot_instance: null,
  spot_price_max: null,
  termination_time: null,
  tags: null,
  project_ssh_keys: null,
  user_ssh_keys: null,
  features: null,
  public_ipv4_subnet_size: null,
  private_ipv4_subnet_size: null,
  ip_addresses: null
)
```

