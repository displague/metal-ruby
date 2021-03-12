# OpenapiClient::SpotMarketRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  | [optional] |
| **devices_min** | **Integer** |  | [optional] |
| **devices_max** | **Integer** |  | [optional] |
| **max_bid_price** | **Float** |  | [optional] |
| **created_at** | **Time** |  | [optional] |
| **end_at** | **Time** |  | [optional] |
| **href** | **String** |  | [optional] |
| **facilities** | [**Href**](Href.md) |  | [optional] |
| **project** | [**Href**](Href.md) |  | [optional] |
| **instances** | [**Href**](Href.md) |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::SpotMarketRequest.new(
  id: null,
  devices_min: null,
  devices_max: null,
  max_bid_price: null,
  created_at: null,
  end_at: null,
  href: null,
  facilities: null,
  project: null,
  instances: null
)
```

