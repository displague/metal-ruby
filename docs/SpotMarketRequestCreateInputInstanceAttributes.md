# OpenapiClient::SpotMarketRequestCreateInputInstanceAttributes

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **plan** | **String** |  | [optional] |
| **hostname** | **String** |  | [optional] |
| **hostnames** | **Array&lt;String&gt;** |  | [optional] |
| **description** | **String** |  | [optional] |
| **billing_cycle** | **String** |  | [optional] |
| **operating_system** | **String** |  | [optional] |
| **always_pxe** | **Boolean** |  | [optional] |
| **userdata** | **String** |  | [optional] |
| **locked** | **Boolean** |  | [optional] |
| **termination_time** | **Time** |  | [optional] |
| **tags** | **Array&lt;String&gt;** |  | [optional] |
| **project_ssh_keys** | **Array&lt;String&gt;** |  | [optional] |
| **user_ssh_keys** | **Array&lt;String&gt;** | The UUIDs of users whose SSH keys should be included on the provisioned device. | [optional] |
| **features** | **Array&lt;String&gt;** |  | [optional] |
| **customdata** | **Object** |  | [optional] |
| **public_ipv4_subnet_size** | **Integer** |  | [optional] |
| **private_ipv4_subnet_size** | **Integer** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::SpotMarketRequestCreateInputInstanceAttributes.new(
  plan: null,
  hostname: null,
  hostnames: null,
  description: null,
  billing_cycle: null,
  operating_system: null,
  always_pxe: null,
  userdata: null,
  locked: null,
  termination_time: null,
  tags: null,
  project_ssh_keys: null,
  user_ssh_keys: null,
  features: null,
  customdata: null,
  public_ipv4_subnet_size: null,
  private_ipv4_subnet_size: null
)
```

