# OpenapiClient::VirtualCircuit

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  | [optional] |
| **name** | **String** |  | [optional] |
| **description** | **String** |  | [optional] |
| **status** | **String** |  | [optional] |
| **vnid** | **Integer** |  | [optional] |
| **nni_vlan** | **Integer** |  | [optional] |
| **speed** | **Integer** | integer representing bps speed | [optional] |
| **tags** | **Array&lt;String&gt;** |  | [optional] |
| **project** | [**Href**](Href.md) |  | [optional] |
| **virtual_network** | [**Href**](Href.md) |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::VirtualCircuit.new(
  id: null,
  name: null,
  description: null,
  status: null,
  vnid: null,
  nni_vlan: null,
  speed: null,
  tags: null,
  project: null,
  virtual_network: null
)
```

