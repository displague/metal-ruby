# OpenapiClient::Volume

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  | [optional] |
| **name** | **String** |  | [optional] |
| **description** | **String** |  | [optional] |
| **size** | **Integer** |  | [optional] |
| **locked** | **Boolean** |  | [optional] |
| **billing_cycle** | **String** |  | [optional] |
| **state** | **String** |  | [optional] |
| **created_at** | **Time** |  | [optional] |
| **updated_at** | **Time** |  | [optional] |
| **project** | [**Href**](Href.md) |  | [optional] |
| **facility** | [**Href**](Href.md) |  | [optional] |
| **snapshot_policies** | [**Array&lt;Href&gt;**](Href.md) |  | [optional] |
| **attachments** | [**Array&lt;Href&gt;**](Href.md) |  | [optional] |
| **plan** | [**Plan**](Plan.md) |  | [optional] |
| **href** | **String** |  | [optional] |
| **customdata** | **Object** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::Volume.new(
  id: null,
  name: null,
  description: null,
  size: null,
  locked: null,
  billing_cycle: null,
  state: null,
  created_at: null,
  updated_at: null,
  project: null,
  facility: null,
  snapshot_policies: null,
  attachments: null,
  plan: null,
  href: null,
  customdata: null
)
```

