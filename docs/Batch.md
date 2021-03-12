# OpenapiClient::Batch

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  | [optional] |
| **error_messages** | **Array&lt;String&gt;** |  | [optional] |
| **quantity** | **Integer** |  | [optional] |
| **state** | **String** |  | [optional] |
| **created_at** | **Time** |  | [optional] |
| **updated_at** | **Time** |  | [optional] |
| **devices** | [**Array&lt;Href&gt;**](Href.md) |  | [optional] |
| **project** | [**Href**](Href.md) |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::Batch.new(
  id: null,
  error_messages: null,
  quantity: null,
  state: null,
  created_at: null,
  updated_at: null,
  devices: null,
  project: null
)
```

