# OpenapiClient::Project

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  | [optional] |
| **name** | **String** |  | [optional] |
| **created_at** | **Time** |  | [optional] |
| **updated_at** | **Time** |  | [optional] |
| **max_devices** | **Object** |  | [optional] |
| **members** | [**Array&lt;Href&gt;**](Href.md) |  | [optional] |
| **memberships** | [**Array&lt;Href&gt;**](Href.md) |  | [optional] |
| **network_status** | **Object** |  | [optional] |
| **invitations** | [**Array&lt;Href&gt;**](Href.md) |  | [optional] |
| **payment_method** | [**Href**](Href.md) |  | [optional] |
| **devices** | [**Array&lt;Href&gt;**](Href.md) |  | [optional] |
| **ssh_keys** | [**Array&lt;Href&gt;**](Href.md) |  | [optional] |
| **volumes** | [**Array&lt;Href&gt;**](Href.md) |  | [optional] |
| **bgp_config** | [**Href**](Href.md) |  | [optional] |
| **customdata** | **Object** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::Project.new(
  id: null,
  name: null,
  created_at: null,
  updated_at: null,
  max_devices: null,
  members: null,
  memberships: null,
  network_status: null,
  invitations: null,
  payment_method: null,
  devices: null,
  ssh_keys: null,
  volumes: null,
  bgp_config: null,
  customdata: null
)
```

