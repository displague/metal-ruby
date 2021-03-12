# OpenapiClient::BgpConfig

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  | [optional] |
| **status** | **String** | status requested is valid only for global deployment | [optional] |
| **deployment_type** | **String** | In a Local BGP deployment, a customer uses an internal ASN to control routes within a single Equinix Metal datacenter. This means that the routes are never advertised to the global Internet. Global BGP, on the other hand, requires a customer to have a registered ASN and IP space.  | [optional] |
| **asn** | **Integer** | Autonomous System Number | [optional] |
| **route_object** | **String** | Specifies AS-MACRO (aka AS-SET) to use when building client route filters | [optional] |
| **md5** | **String** | (Optional) Password for BGP session in plaintext (not a checksum) | [optional] |
| **max_prefix** | **Integer** | The maximum number of route filters allowed per server | [optional] |
| **project** | [**Href**](Href.md) |  | [optional] |
| **created_at** | **Time** |  | [optional] |
| **requested_at** | **Time** |  | [optional] |
| **sessions** | [**Array&lt;BgpSession&gt;**](BgpSession.md) | The direct connections between neighboring routers that want to exchange routing information. | [optional] |
| **ranges** | [**Array&lt;GlobalBgpRange&gt;**](GlobalBgpRange.md) | The IP block ranges associated to the ASN (Populated in Global BGP only) | [optional] |
| **href** | **String** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::BgpConfig.new(
  id: null,
  status: null,
  deployment_type: null,
  asn: null,
  route_object: null,
  md5: null,
  max_prefix: null,
  project: null,
  created_at: null,
  requested_at: null,
  sessions: null,
  ranges: null,
  href: null
)
```

