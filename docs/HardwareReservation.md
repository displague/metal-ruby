# OpenapiClient::HardwareReservation

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  | [optional] |
| **short_id** | **String** |  | [optional] |
| **facility** | [**Facility**](Facility.md) |  | [optional] |
| **plan** | [**Plan**](Plan.md) |  | [optional] |
| **href** | **String** |  | [optional] |
| **project** | [**Project**](Project.md) |  | [optional] |
| **device** | [**Device**](Device.md) |  | [optional] |
| **created_at** | **Time** |  | [optional] |
| **remove_at** | **Time** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::HardwareReservation.new(
  id: null,
  short_id: null,
  facility: null,
  plan: null,
  href: null,
  project: null,
  device: null,
  created_at: null,
  remove_at: null
)
```

