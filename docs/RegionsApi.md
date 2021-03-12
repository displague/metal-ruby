# OpenapiClient::RegionsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**find_regions**](RegionsApi.md#find_regions) | **GET** /regions | Retrieve all regions |


## find_regions

> <RegionsList> find_regions(opts)

Retrieve all regions

Returns all regions.

### Examples

```ruby
require 'time'
require 'openapi_client'
# setup authorization
OpenapiClient.configure do |config|
  # Configure API key authorization: x_auth_token
  config.api_key['x_auth_token'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x_auth_token'] = 'Bearer'
end

api_instance = OpenapiClient::RegionsApi.new
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve all regions
  result = api_instance.find_regions(opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling RegionsApi->find_regions: #{e}"
end
```

#### Using the find_regions_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<RegionsList>, Integer, Hash)> find_regions_with_http_info(opts)

```ruby
begin
  # Retrieve all regions
  data, status_code, headers = api_instance.find_regions_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <RegionsList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling RegionsApi->find_regions_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |
| **page** | **Integer** | Page to return | [optional][default to 1] |
| **per_page** | **Integer** | Items returned per page | [optional][default to 10] |

### Return type

[**RegionsList**](RegionsList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

