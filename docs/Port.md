# OpenapiClient::Port

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  | [optional] |
| **type** | **String** |  | [optional] |
| **name** | **String** |  | [optional] |
| **data** | **Object** |  | [optional] |
| **disbond_operation_supported** | **Boolean** | Indicates whether or not the bond can be broken on the port (when applicable). | [optional] |
| **hardware** | [**Href**](Href.md) |  | [optional] |
| **virtual_networks** | [**Array&lt;Href&gt;**](Href.md) |  | [optional] |
| **connected_port** | [**Href**](Href.md) |  | [optional] |
| **href** | **String** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::Port.new(
  id: null,
  type: null,
  name: null,
  data: null,
  disbond_operation_supported: null,
  hardware: null,
  virtual_networks: null,
  connected_port: null,
  href: null
)
```

