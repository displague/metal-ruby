# OpenapiClient::OrganizationInput

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **name** | **String** |  | [optional] |
| **description** | **String** |  | [optional] |
| **website** | **String** |  | [optional] |
| **twitter** | **String** |  | [optional] |
| **logo** | **File** |  | [optional] |
| **address** | [**Address**](Address.md) |  | [optional] |
| **billing_address** | [**Address**](Address.md) |  | [optional] |
| **customdata** | **Object** |  | [optional] |
| **enforce_2fa_at** | **Time** | Force to all members to have enabled the two factor authentication after that date, unless the value is null | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::OrganizationInput.new(
  name: null,
  description: null,
  website: null,
  twitter: null,
  logo: null,
  address: null,
  billing_address: null,
  customdata: null,
  enforce_2fa_at: null
)
```

