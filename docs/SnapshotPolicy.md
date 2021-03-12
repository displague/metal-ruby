# OpenapiClient::SnapshotPolicy

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  | [optional] |
| **snapshot_count** | **Integer** |  | [optional] |
| **snapshot_frequency** | **String** |  | [optional] |
| **created_at** | **Time** |  | [optional] |
| **updated_at** | **Time** |  | [optional] |
| **volume** | [**Href**](Href.md) |  | [optional] |
| **href** | **String** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::SnapshotPolicy.new(
  id: null,
  snapshot_count: null,
  snapshot_frequency: null,
  created_at: null,
  updated_at: null,
  volume: null,
  href: null
)
```

