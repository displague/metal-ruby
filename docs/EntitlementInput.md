# OpenapiClient::EntitlementInput

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **description** | **String** |  | [optional] |
| **slug** | **String** |  | [optional] |
| **weight** | **Integer** |  | [optional] |
| **instance_quota** | **Object** |  | [optional] |
| **project_quota** | **Integer** |  | [optional] |
| **volume_quota** | **Object** |  | [optional] |
| **feature_access** | **Object** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::EntitlementInput.new(
  description: null,
  slug: null,
  weight: null,
  instance_quota: null,
  project_quota: null,
  volume_quota: null,
  feature_access: null
)
```

