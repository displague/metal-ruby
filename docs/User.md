# OpenapiClient::User

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  | [optional] |
| **short_id** | **String** |  | [optional] |
| **first_name** | **String** |  | [optional] |
| **last_name** | **String** |  | [optional] |
| **full_name** | **String** |  | [optional] |
| **email** | **String** |  | [optional] |
| **avatar_url** | **String** |  | [optional] |
| **avatar_thumb_url** | **String** |  | [optional] |
| **two_factor_auth** | **String** |  | [optional] |
| **max_projects** | **Integer** |  | [optional] |
| **max_organizations** | **Integer** |  | [optional] |
| **created_at** | **Time** |  | [optional] |
| **updated_at** | **Time** |  | [optional] |
| **timezone** | **String** |  | [optional] |
| **fraud_score** | **String** |  | [optional] |
| **last_login_at** | **Time** |  | [optional] |
| **emails** | [**Array&lt;Href&gt;**](Href.md) |  | [optional] |
| **href** | **String** |  | [optional] |
| **phone_number** | **String** |  | [optional] |
| **customdata** | **Object** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::User.new(
  id: null,
  short_id: null,
  first_name: null,
  last_name: null,
  full_name: null,
  email: null,
  avatar_url: null,
  avatar_thumb_url: null,
  two_factor_auth: null,
  max_projects: null,
  max_organizations: null,
  created_at: null,
  updated_at: null,
  timezone: null,
  fraud_score: null,
  last_login_at: null,
  emails: null,
  href: null,
  phone_number: null,
  customdata: null
)
```

