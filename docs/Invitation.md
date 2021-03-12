# OpenapiClient::Invitation

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** |  | [optional] |
| **roles** | **Array&lt;String&gt;** |  | [optional] |
| **invitee** | **String** |  | [optional] |
| **created_at** | **Time** |  | [optional] |
| **updated_at** | **Time** |  | [optional] |
| **invited_by** | [**Href**](Href.md) |  | [optional] |
| **organization** | [**Href**](Href.md) |  | [optional] |
| **projects_ids** | **Array&lt;String&gt;** |  | [optional] |
| **invitation** | [**Href**](Href.md) |  | [optional] |
| **href** | **String** |  | [optional] |

## Example

```ruby
require 'openapi_client'

instance = OpenapiClient::Invitation.new(
  id: null,
  roles: null,
  invitee: null,
  created_at: null,
  updated_at: null,
  invited_by: null,
  organization: null,
  projects_ids: null,
  invitation: null,
  href: null
)
```

