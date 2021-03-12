# OpenapiClient::VolumeCreateInput

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **description** | **String** |  | [optional] |
| **facility** | **String** | ams1, ewr1, nrt1, sjc1 |  |
| **plan** | **String** | storage_1, storage_2 |  |
| **size** | **Integer** |  |  |
| **locked** | **Boolean** |  | [optional] |
| **billing_cycle** | **String** | hourly | [optional] |
| **snapshot_policies** | [**SnapshotPolicyInput**](SnapshotPolicyInput.md) |  | [optional] |
| **customdata** | **Object** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::VolumeCreateInput.new(
  description: null,
  facility: null,
  plan: null,
  size: null,
  locked: null,
  billing_cycle: null,
  snapshot_policies: null,
  customdata: null
)
```

