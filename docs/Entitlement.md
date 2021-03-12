# OpenapiClient::Entitlement

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  |  |
| **description** | **String** |  | [optional] |
| **slug** | **String** |  |  |
| **name** | **String** |  | [optional] |
| **weight** | **Integer** |  |  |
| **instance_quota** | **Object** |  | [optional] |
| **project_quota** | **Integer** |  | [optional] |
| **volume_quota** | **Object** |  | [optional] |
| **ip_quota** | **Object** |  | [optional] |
| **feature_access** | **Object** |  | [optional] |
| **href** | **String** |  | [optional] |
| **volume_limits** | **Object** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::Entitlement.new(
  id: null,
  description: null,
  slug: null,
  name: null,
  weight: null,
  instance_quota: null,
  project_quota: null,
  volume_quota: null,
  ip_quota: null,
  feature_access: null,
  href: null,
  volume_limits: null
)
```

