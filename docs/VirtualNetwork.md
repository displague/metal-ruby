# OpenapiClient::VirtualNetwork

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  | [optional] |
| **description** | **String** |  | [optional] |
| **vxlan** | **Integer** |  | [optional] |
| **facility** | [**Href**](Href.md) |  | [optional] |
| **instances** | [**Array&lt;Href&gt;**](Href.md) |  | [optional] |
| **assigned_to** | [**Href**](Href.md) |  | [optional] |
| **href** | **String** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::VirtualNetwork.new(
  id: null,
  description: null,
  vxlan: null,
  facility: null,
  instances: null,
  assigned_to: null,
  href: null
)
```

