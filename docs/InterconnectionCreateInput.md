# OpenapiClient::InterconnectionCreateInput

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** |  |  |
| **description** | **String** |  | [optional] |
| **facility** | **String** | A Facility ID or code. |  |
| **type** | **String** | Either &#39;shared&#39; or &#39;dedicated&#39;. |  |
| **redundancy** | **String** | Either &#39;primary&#39; or &#39;redundant&#39;. |  |
| **contact_email** | **String** |  | [optional] |
| **project** | **String** |  | [optional] |
| **speed** | **String** | A connection speed, in bps, mbps, or gbps. Ex: &#39;100000000&#39; or &#39;100 mbps&#39;. | [optional] |
| **tags** | **Array&lt;String&gt;** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::InterconnectionCreateInput.new(
  name: null,
  description: null,
  facility: null,
  type: null,
  redundancy: null,
  contact_email: null,
  project: null,
  speed: null,
  tags: null
)
```

