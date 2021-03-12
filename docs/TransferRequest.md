# OpenapiClient::TransferRequest

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  | [optional] |
| **created_at** | **Time** |  | [optional] |
| **updated_at** | **Time** |  | [optional] |
| **target_organization** | [**Href**](Href.md) |  | [optional] |
| **project** | [**Href**](Href.md) |  | [optional] |
| **href** | **String** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::TransferRequest.new(
  id: null,
  created_at: null,
  updated_at: null,
  target_organization: null,
  project: null,
  href: null
)
```

