# OpenapiClient::VirtualCircuitCreateInput

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **description** | **String** |  | [optional] |
| **name** | **String** |  | [optional] |
| **speed** | **Integer** | speed can be passed as integer number representing bps speed or string (e.g. &#39;52m&#39; or &#39;100g&#39; or &#39;4 gbps&#39;) | [optional] |
| **tags** | **Array&lt;String&gt;** |  | [optional] |
| **vnid** | **String** | A Virtual Network record UUID or the VNID of a Virtual Network in your project (sent as integer). | [optional] |
| **nni_vlan** | **Integer** |  | [optional] |
| **project** | **String** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::VirtualCircuitCreateInput.new(
  description: null,
  name: null,
  speed: null,
  tags: null,
  vnid: null,
  nni_vlan: null,
  project: null
)
```

