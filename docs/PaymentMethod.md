# OpenapiClient::PaymentMethod

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  | [optional] |
| **name** | **String** |  | [optional] |
| **type** | **String** |  | [optional] |
| **default** | **Boolean** |  | [optional] |
| **created_at** | **Time** |  | [optional] |
| **updated_at** | **Time** |  | [optional] |
| **card_type** | **String** |  | [optional] |
| **expiration_month** | **String** |  | [optional] |
| **expiration_year** | **String** |  | [optional] |
| **cardholder_name** | **String** |  | [optional] |
| **billing_address** | [**PaymentMethodBillingAddress**](PaymentMethodBillingAddress.md) |  | [optional] |
| **email** | **String** |  | [optional] |
| **created_by_user** | [**Href**](Href.md) |  | [optional] |
| **organization** | [**Href**](Href.md) |  | [optional] |
| **projects** | [**Array&lt;Href&gt;**](Href.md) |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::PaymentMethod.new(
  id: null,
  name: null,
  type: null,
  default: null,
  created_at: null,
  updated_at: null,
  card_type: null,
  expiration_month: null,
  expiration_year: null,
  cardholder_name: null,
  billing_address: null,
  email: null,
  created_by_user: null,
  organization: null,
  projects: null
)
```

