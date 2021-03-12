# OpenapiClient::BgpNeighborData

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **address_family** | **Float** | Address Family for IP Address | [optional] |
| **customer_as** | **Float** | The customer&#39;s ASN. In a local BGP deployment, this will be an internal ASN used to route within the data center. For a global BGP deployment, this will be the your own ASN, configured when you set up BGP for your project. | [optional] |
| **customer_ip** | **String** | The device&#39;s IP address. For an IPv4 BGP session, this is typically the private bond0 address for the device. | [optional] |
| **md5_enabled** | **Boolean** | True if an MD5 password is configured for the project. | [optional] |
| **md5_password** | **String** | The MD5 password configured for the project, if set. | [optional] |
| **multihop** | **Boolean** | True when the BGP session should be configured as multihop. | [optional] |
| **peer_as** | **Float** | The Peer ASN to use when configuring BGP on your device. | [optional] |
| **peer_ips** | **Array&lt;String&gt;** | A list of one or more IP addresses to use for the Peer IP section of your BGP configuration. For non-multihop sessions, this will typically be a single gateway address for the device. For multihop sessions, it will be a list of IPs. | [optional] |
| **routes_in** | [**Array&lt;BgpNeighborDataRoutesIn&gt;**](BgpNeighborDataRoutesIn.md) | A list of project subnets | [optional] |
| **routes_out** | [**Array&lt;BgpNeighborDataRoutesOut&gt;**](BgpNeighborDataRoutesOut.md) | A list of outgoing routes. Only populated if the BGP session has default route enabled. | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::BgpNeighborData.new(
  address_family: null,
  customer_as: 65000.0,
  customer_ip: 10.32.16.1 (IPv4) or 2604:1380:4111:2700::1 (IPv6),
  md5_enabled: null,
  md5_password: null,
  multihop: null,
  peer_as: 65530.0,
  peer_ips: [&quot;10.32.16.0&quot;] or [&quot;169.254.255.1&quot;, &quot;169.254.255.2&quot;],
  routes_in: null,
  routes_out: null
)
```

