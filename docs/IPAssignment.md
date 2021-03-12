# OpenapiClient::IPAssignment

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  | [optional] |
| **address_family** | **Integer** |  | [optional] |
| **netmask** | **String** |  | [optional] |
| **public** | **Boolean** |  | [optional] |
| **enabled** | **Boolean** |  | [optional] |
| **cidr** | **Integer** |  | [optional] |
| **management** | **Boolean** |  | [optional] |
| **manageable** | **Boolean** |  | [optional] |
| **assigned_to** | [**Href**](Href.md) |  | [optional] |
| **network** | **String** |  | [optional] |
| **address** | **String** |  | [optional] |
| **gateway** | **String** |  | [optional] |
| **href** | **String** |  | [optional] |
| **created_at** | **Time** |  | [optional] |
| **parent_block** | [**ParentBlock**](ParentBlock.md) |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::IPAssignment.new(
  id: null,
  address_family: null,
  netmask: null,
  public: null,
  enabled: null,
  cidr: null,
  management: null,
  manageable: null,
  assigned_to: null,
  network: null,
  address: null,
  gateway: null,
  href: null,
  created_at: null,
  parent_block: null
)
```

