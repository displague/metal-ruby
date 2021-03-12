# OpenapiClient::InterconnectionPort

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  | [optional] |
| **role** | **String** | Either &#39;primary&#39; or &#39;secondary&#39;. | [optional] |
| **status** | **String** |  | [optional] |
| **switch_id** | **String** | A switch &#39;short ID&#39; | [optional] |
| **virtual_circuits** | [**VirtualCircuitList**](VirtualCircuitList.md) |  | [optional] |
| **organization** | [**Href**](Href.md) |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::InterconnectionPort.new(
  id: null,
  role: null,
  status: null,
  switch_id: null,
  virtual_circuits: null,
  organization: null
)
```

