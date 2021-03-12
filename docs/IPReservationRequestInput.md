# OpenapiClient::IPReservationRequestInput

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **type** | **String** |  |  |
| **quantity** | **Integer** |  |  |
| **comments** | **String** |  | [optional] |
| **facility** | **String** |  | [optional] |
| **customdata** | **Object** |  | [optional] |
| **tags** | **Array&lt;String&gt;** |  | [optional] |
| **details** | **String** |  | [optional] |
| **fail_on_approval_required** | **Boolean** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::IPReservationRequestInput.new(
  type: null,
  quantity: null,
  comments: null,
  facility: null,
  customdata: null,
  tags: null,
  details: null,
  fail_on_approval_required: null
)
```

