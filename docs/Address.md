# OpenapiClient::Address

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **address** | **String** |  |  |
| **address2** | **String** |  | [optional] |
| **city** | **String** |  | [optional] |
| **state** | **String** |  | [optional] |
| **zip_code** | **String** |  |  |
| **country** | **String** |  |  |
| **coordinates** | [**Coordinates**](Coordinates.md) |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::Address.new(
  address: null,
  address2: null,
  city: null,
  state: null,
  zip_code: null,
  country: null,
  coordinates: null
)
```

