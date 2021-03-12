# OpenapiClient::VirtualCircuitUpdateInput

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **description** | **String** |  | [optional] |
| **name** | **String** |  | [optional] |
| **speed** | **String** |  | [optional] |
| **tags** | **Array&lt;String&gt;** |  | [optional] |
| **vnid** | **String** | A Virtual Network record UUID or the VNID of a Virtual Network in your project. | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::VirtualCircuitUpdateInput.new(
  description: null,
  name: null,
  speed: null,
  tags: null,
  vnid: null
)
```

