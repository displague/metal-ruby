# OpenapiClient::UserCreateInput

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **first_name** | **String** |  |  |
| **last_name** | **String** |  |  |
| **phone_number** | **String** |  | [optional] |
| **timezone** | **String** |  | [optional] |
| **password** | **String** |  | [optional] |
| **level** | **String** |  | [optional] |
| **title** | **String** |  | [optional] |
| **company_name** | **String** |  | [optional] |
| **company_url** | **String** |  | [optional] |
| **verified_at** | **Time** |  | [optional] |
| **social_accounts** | **Object** |  | [optional] |
| **two_factor_auth** | **String** |  | [optional] |
| **avatar** | **File** |  | [optional] |
| **emails** | [**Array&lt;EmailInput&gt;**](EmailInput.md) |  |  |
| **locked** | **Boolean** |  | [optional] |
| **customdata** | **Object** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::UserCreateInput.new(
  first_name: null,
  last_name: null,
  phone_number: null,
  timezone: null,
  password: null,
  level: null,
  title: null,
  company_name: null,
  company_url: null,
  verified_at: null,
  social_accounts: null,
  two_factor_auth: null,
  avatar: null,
  emails: null,
  locked: null,
  customdata: null
)
```

