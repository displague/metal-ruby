# OpenapiClient::Device

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  | [optional] |
| **short_id** | **String** |  | [optional] |
| **hostname** | **String** |  | [optional] |
| **description** | **String** |  | [optional] |
| **state** | **String** |  | [optional] |
| **tags** | **Array&lt;String&gt;** |  | [optional] |
| **image_url** | **String** |  | [optional] |
| **billing_cycle** | **String** |  | [optional] |
| **user** | **String** |  | [optional] |
| **iqn** | **String** |  | [optional] |
| **locked** | **Boolean** |  | [optional] |
| **bonding_mode** | **Integer** |  | [optional] |
| **created_at** | **Time** |  | [optional] |
| **updated_at** | **Time** |  | [optional] |
| **spot_instance** | **Boolean** |  | [optional] |
| **spot_price_max** | **Float** |  | [optional] |
| **termination_time** | **Time** |  | [optional] |
| **customdata** | **Object** |  | [optional] |
| **provisioning_percentage** | **Float** |  | [optional] |
| **operating_system** | [**OperatingSystem**](OperatingSystem.md) |  | [optional] |
| **always_pxe** | **Boolean** |  | [optional] |
| **ipxe_script_url** | **String** |  | [optional] |
| **location** | [**HardwareLocation**](HardwareLocation.md) |  | [optional] |
| **facility** | [**Facility**](Facility.md) |  | [optional] |
| **plan** | [**Plan**](Plan.md) |  | [optional] |
| **userdata** | **String** |  | [optional] |
| **root_password** | **String** |  | [optional] |
| **href** | **String** |  | [optional] |
| **project** | [**Href**](Href.md) |  | [optional] |
| **project_lite** | [**Href**](Href.md) |  | [optional] |
| **volumes** | [**Array&lt;Href&gt;**](Href.md) |  | [optional] |
| **hardware_reservation** | [**Href**](Href.md) |  | [optional] |
| **ssh_keys** | [**Array&lt;Href&gt;**](Href.md) |  | [optional] |
| **ip_addresses** | [**Array&lt;IPAssignment&gt;**](IPAssignment.md) |  | [optional] |
| **provisioning_events** | [**Array&lt;Event&gt;**](Event.md) |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::Device.new(
  id: null,
  short_id: null,
  hostname: null,
  description: null,
  state: null,
  tags: null,
  image_url: null,
  billing_cycle: null,
  user: null,
  iqn: null,
  locked: null,
  bonding_mode: null,
  created_at: null,
  updated_at: null,
  spot_instance: null,
  spot_price_max: null,
  termination_time: null,
  customdata: null,
  provisioning_percentage: null,
  operating_system: null,
  always_pxe: null,
  ipxe_script_url: null,
  location: null,
  facility: null,
  plan: null,
  userdata: null,
  root_password: null,
  href: null,
  project: null,
  project_lite: null,
  volumes: null,
  hardware_reservation: null,
  ssh_keys: null,
  ip_addresses: null,
  provisioning_events: null
)
```

