# OpenapiClient::SpotMarketRequestCreateInput

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **instance_attributes** | [**SpotMarketRequestCreateInputInstanceAttributes**](SpotMarketRequestCreateInputInstanceAttributes.md) |  | [optional] |
| **devices_min** | **Integer** |  | [optional] |
| **devices_max** | **Integer** |  | [optional] |
| **max_bid_price** | **Float** |  | [optional] |
| **end_at** | **Time** |  | [optional] |
| **facilities** | **Array&lt;String&gt;** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::SpotMarketRequestCreateInput.new(
  instance_attributes: null,
  devices_min: null,
  devices_max: null,
  max_bid_price: null,
  end_at: null,
  facilities: null
)
```

