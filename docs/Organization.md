# OpenapiClient::Organization

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  | [optional] |
| **name** | **String** |  | [optional] |
| **description** | **String** |  | [optional] |
| **website** | **String** |  | [optional] |
| **twitter** | **String** |  | [optional] |
| **logo** | **File** |  | [optional] |
| **created_at** | **Time** |  | [optional] |
| **updated_at** | **Time** |  | [optional] |
| **projects** | [**Array&lt;Href&gt;**](Href.md) |  | [optional] |
| **members** | [**Array&lt;Href&gt;**](Href.md) |  | [optional] |
| **memberships** | [**Array&lt;Href&gt;**](Href.md) |  | [optional] |
| **address** | [**Address**](Address.md) |  | [optional] |
| **billing_address** | [**Address**](Address.md) |  | [optional] |
| **entitlement** | [**Entitlement**](Entitlement.md) |  | [optional] |
| **terms** | **Integer** |  | [optional] |
| **credit_amount** | **Float** |  | [optional] |
| **customdata** | **Object** |  | [optional] |
| **enforce_2fa_at** | **Time** | Force to all members to have enabled the two factor authentication after that date, unless the value is null | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::Organization.new(
  id: null,
  name: null,
  description: null,
  website: null,
  twitter: null,
  logo: null,
  created_at: null,
  updated_at: null,
  projects: null,
  members: null,
  memberships: null,
  address: null,
  billing_address: null,
  entitlement: null,
  terms: null,
  credit_amount: null,
  customdata: null,
  enforce_2fa_at: null
)
```

