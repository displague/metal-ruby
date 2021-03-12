# OpenapiClient::DeviceUpdateInput

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **hostname** | **String** |  | [optional] |
| **description** | **String** |  | [optional] |
| **billing_cycle** | **String** |  | [optional] |
| **userdata** | **String** |  | [optional] |
| **locked** | **Boolean** |  | [optional] |
| **tags** | **Array&lt;String&gt;** |  | [optional] |
| **always_pxe** | **Boolean** |  | [optional] |
| **ipxe_script_url** | **String** |  | [optional] |
| **spot_instance** | **Boolean** |  | [optional] |
| **customdata** | **Object** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::DeviceUpdateInput.new(
  hostname: null,
  description: null,
  billing_cycle: null,
  userdata: null,
  locked: null,
  tags: null,
  always_pxe: null,
  ipxe_script_url: null,
  spot_instance: null,
  customdata: null
)
```

