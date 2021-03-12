# OpenapiClient::PaymentMethodUpdateInput

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** |  | [optional] |
| **default** | **Boolean** |  | [optional] |
| **cardholder_name** | **String** |  | [optional] |
| **expiration_month** | **String** |  | [optional] |
| **expiration_year** | **Integer** |  | [optional] |
| **billing_address** | **Object** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::PaymentMethodUpdateInput.new(
  name: null,
  default: null,
  cardholder_name: null,
  expiration_month: null,
  expiration_year: null,
  billing_address: null
)
```

