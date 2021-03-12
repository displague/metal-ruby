# OpenapiClient::InterconnectionUpdateInput

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** |  | [optional] |
| **redundancy** | **String** | Updating from &#39;redundant&#39; to &#39;primary&#39; will remove a secondary port, while updating from &#39;primary&#39; to &#39;redundant&#39; will add one. | [optional] |
| **description** | **String** |  | [optional] |
| **contact_email** | **String** |  | [optional] |
| **tags** | **Array&lt;String&gt;** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::InterconnectionUpdateInput.new(
  name: null,
  redundancy: null,
  description: null,
  contact_email: null,
  tags: null
)
```

