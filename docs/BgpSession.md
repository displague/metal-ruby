# OpenapiClient::BgpSession

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  | [optional] |
| **status** | **String** |  | [optional] |
| **learned_routes** | **Array&lt;String&gt;** |  | [optional] |
| **address_family** | **String** |  | [optional] |
| **device** | [**Href**](Href.md) |  | [optional] |
| **href** | **String** |  | [optional] |
| **default_route** | **Boolean** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::BgpSession.new(
  id: null,
  status: null,
  learned_routes: null,
  address_family: null,
  device: null,
  href: null,
  default_route: null
)
```

