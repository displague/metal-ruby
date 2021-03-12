# OpenapiClient::InstancesBatchCreateInputIpAddresses

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **address_family** | **Float** | Address Family for IP Address | [optional] |
| **public** | **Boolean** | Address Type for IP Address | [optional][default to true] |
| **cidr** | **Float** | Cidr Size for the IP Block created. Valid values depends on the operating system been provisioned (28..32 for IPv4 addresses, 124..127 for IPv6 addresses). | [optional] |
| **ip_reservations** | **Array&lt;String&gt;** | UUIDs of any IP reservations to use when assigning IPs | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::InstancesBatchCreateInputIpAddresses.new(
  address_family: 4.0,
  public: false,
  cidr: 28.0,
  ip_reservations: null
)
```

