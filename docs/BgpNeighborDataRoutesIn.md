# OpenapiClient::BgpNeighborDataRoutesIn

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **route** | **String** | A project network | [optional] |
| **exact** | **Boolean** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::BgpNeighborDataRoutesIn.new(
  route: 10.32.16.0/31,
  exact: null
)
```

