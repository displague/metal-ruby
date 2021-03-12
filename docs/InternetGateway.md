# OpenapiClient::InternetGateway

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  | [optional] |
| **created_at** | **Time** |  | [optional] |
| **virtual_network** | [**Href**](Href.md) |  | [optional] |
| **created_by** | **String** |  | [optional] |
| **ip_reservations** | [**Array&lt;Href&gt;**](Href.md) |  | [optional] |
| **href** | **String** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::InternetGateway.new(
  id: null,
  created_at: null,
  virtual_network: null,
  created_by: null,
  ip_reservations: null,
  href: null
)
```

