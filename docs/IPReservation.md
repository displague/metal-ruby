# OpenapiClient::IPReservation

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
| **addon** | **Boolean** |  | [optional] |
| **bill** | **Boolean** |  | [optional] |
| **assignments** | [**Array&lt;IPAssignment&gt;**](IPAssignment.md) |  | [optional] |
| **network** | **String** |  | [optional] |
| **created_at** | **Time** |  | [optional] |
| **facility** | [**Facility**](Facility.md) |  | [optional] |
| **href** | **String** |  | [optional] |
| **tags** | **Array&lt;String&gt;** |  | [optional] |
| **state** | **String** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::IPReservation.new(
  id: null,
  address_family: null,
  netmask: null,
  public: null,
  enabled: null,
  cidr: null,
  management: null,
  manageable: null,
  addon: null,
  bill: null,
  assignments: null,
  network: null,
  created_at: null,
  facility: null,
  href: null,
  tags: null,
  state: null
)
```

