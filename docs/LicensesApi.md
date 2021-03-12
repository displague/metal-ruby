# OpenapiClient::LicensesApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**create_license**](LicensesApi.md#create_license) | **POST** /projects/{id}/licenses | Create a License |
| [**delete_license**](LicensesApi.md#delete_license) | **DELETE** /licenses/{id} | Delete the license |
| [**find_license_by_id**](LicensesApi.md#find_license_by_id) | **GET** /licenses/{id} | Retrieve a license |
| [**find_project_licenses**](LicensesApi.md#find_project_licenses) | **GET** /projects/{id}/licenses | Retrieve all licenses |
| [**update_license**](LicensesApi.md#update_license) | **PUT** /licenses/{id} | Update the license |


## create_license

> <License> create_license(id, license)

Create a License

Creates a new license for the given project

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

api_instance = OpenapiClient::LicensesApi.new
id = TODO # String | Project UUID
license = OpenapiClient::LicenseCreateInput.new # LicenseCreateInput | License to create

begin
  # Create a License
  result = api_instance.create_license(id, license)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling LicensesApi->create_license: #{e}"
end
```

#### Using the create_license_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<License>, Integer, Hash)> create_license_with_http_info(id, license)

```ruby
begin
  # Create a License
  data, status_code, headers = api_instance.create_license_with_http_info(id, license)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <License>
rescue OpenapiClient::ApiError => e
  puts "Error when calling LicensesApi->create_license_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **license** | [**LicenseCreateInput**](LicenseCreateInput.md) | License to create |  |

### Return type

[**License**](License.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## delete_license

> delete_license(id)

Delete the license

Deletes a license.

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

api_instance = OpenapiClient::LicensesApi.new
id = TODO # String | License UUID

begin
  # Delete the license
  api_instance.delete_license(id)
rescue OpenapiClient::ApiError => e
  puts "Error when calling LicensesApi->delete_license: #{e}"
end
```

#### Using the delete_license_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> delete_license_with_http_info(id)

```ruby
begin
  # Delete the license
  data, status_code, headers = api_instance.delete_license_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling LicensesApi->delete_license_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | License UUID |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## find_license_by_id

> <License> find_license_by_id(id, opts)

Retrieve a license

Returns a license

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

api_instance = OpenapiClient::LicensesApi.new
id = TODO # String | License UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve a license
  result = api_instance.find_license_by_id(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling LicensesApi->find_license_by_id: #{e}"
end
```

#### Using the find_license_by_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<License>, Integer, Hash)> find_license_by_id_with_http_info(id, opts)

```ruby
begin
  # Retrieve a license
  data, status_code, headers = api_instance.find_license_by_id_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <License>
rescue OpenapiClient::ApiError => e
  puts "Error when calling LicensesApi->find_license_by_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | License UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**License**](License.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_project_licenses

> <LicenseList> find_project_licenses(id, opts)

Retrieve all licenses

Provides a collection of licenses for a given project.

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

api_instance = OpenapiClient::LicensesApi.new
id = TODO # String | Project UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve all licenses
  result = api_instance.find_project_licenses(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling LicensesApi->find_project_licenses: #{e}"
end
```

#### Using the find_project_licenses_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<LicenseList>, Integer, Hash)> find_project_licenses_with_http_info(id, opts)

```ruby
begin
  # Retrieve all licenses
  data, status_code, headers = api_instance.find_project_licenses_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <LicenseList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling LicensesApi->find_project_licenses_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |
| **page** | **Integer** | Page to return | [optional][default to 1] |
| **per_page** | **Integer** | Items returned per page | [optional][default to 10] |

### Return type

[**LicenseList**](LicenseList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## update_license

> <License> update_license(id, license)

Update the license

Updates the license.

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

api_instance = OpenapiClient::LicensesApi.new
id = TODO # String | License UUID
license = OpenapiClient::LicenseUpdateInput.new # LicenseUpdateInput | License to update

begin
  # Update the license
  result = api_instance.update_license(id, license)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling LicensesApi->update_license: #{e}"
end
```

#### Using the update_license_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<License>, Integer, Hash)> update_license_with_http_info(id, license)

```ruby
begin
  # Update the license
  data, status_code, headers = api_instance.update_license_with_http_info(id, license)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <License>
rescue OpenapiClient::ApiError => e
  puts "Error when calling LicensesApi->update_license_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | License UUID |  |
| **license** | [**LicenseUpdateInput**](LicenseUpdateInput.md) | License to update |  |

### Return type

[**License**](License.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

