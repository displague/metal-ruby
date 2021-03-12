# OpenapiClient::VolumeUpdateInput

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **description** | **String** |  | [optional] |
| **size** | **Integer** |  | [optional] |
| **locked** | **Boolean** |  | [optional] |
| **billing_cycle** | **String** | hourly | [optional] |
| **customdata** | **Object** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::VolumeUpdateInput.new(
  description: null,
  size: null,
  locked: null,
  billing_cycle: null,
  customdata: null
)
```

