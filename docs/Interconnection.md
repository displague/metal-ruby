# OpenapiClient::Interconnection

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  | [optional] |
| **name** | **String** |  | [optional] |
| **description** | **String** |  | [optional] |
| **contact_email** | **String** |  | [optional] |
| **status** | **String** |  | [optional] |
| **type** | **String** |  | [optional] |
| **redundancy** | **String** |  | [optional] |
| **speed** | **Integer** | The connection&#39;s speed in bps. | [optional] |
| **tags** | **Array&lt;String&gt;** |  | [optional] |
| **ports** | [**Array&lt;InterconnectionPort&gt;**](InterconnectionPort.md) |  | [optional] |
| **facility** | [**Href**](Href.md) |  | [optional] |
| **organization** | [**Href**](Href.md) |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::Interconnection.new(
  id: null,
  name: null,
  description: null,
  contact_email: null,
  status: null,
  type: null,
  redundancy: null,
  speed: null,
  tags: null,
  ports: null,
  facility: null,
  organization: null
)
```

