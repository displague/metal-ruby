# OpenapiClient::ProjectsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**create_device**](ProjectsApi.md#create_device) | **POST** /projects/{id}/devices | Create a device |
| [**create_license**](ProjectsApi.md#create_license) | **POST** /projects/{id}/licenses | Create a License |
| [**create_organization_project**](ProjectsApi.md#create_organization_project) | **POST** /organizations/{id}/projects | Create a project for the organization |
| [**create_project**](ProjectsApi.md#create_project) | **POST** /projects | Create a project |
| [**create_project_invitation**](ProjectsApi.md#create_project_invitation) | **POST** /projects/{project_id}/invitations | Create an invitation for a project |
| [**create_project_ssh_key**](ProjectsApi.md#create_project_ssh_key) | **POST** /projects/{id}/ssh-keys | Create a ssh key for the given project |
| [**create_spot_market_request**](ProjectsApi.md#create_spot_market_request) | **POST** /projects/{id}/spot-market-requests | Create a spot market request |
| [**create_transfer_request**](ProjectsApi.md#create_transfer_request) | **POST** /projects/{id}/transfers | Create a transfer request |
| [**create_virtual_network**](ProjectsApi.md#create_virtual_network) | **POST** /projects/{id}/virtual-networks | Create an virtual network |
| [**delete_project**](ProjectsApi.md#delete_project) | **DELETE** /projects/{id} | Delete the project |
| [**find_batches_by_project**](ProjectsApi.md#find_batches_by_project) | **GET** /projects/{id}/batches | Retrieve all batches by project |
| [**find_bgp_config_by_project**](ProjectsApi.md#find_bgp_config_by_project) | **GET** /projects/{id}/bgp-config | Retrieve a bgp config |
| [**find_device_ssh_keys**](ProjectsApi.md#find_device_ssh_keys) | **GET** /devices/{id}/ssh-keys | Retrieve a device&#39;s ssh keys |
| [**find_facilities_by_project**](ProjectsApi.md#find_facilities_by_project) | **GET** /projects/{id}/facilities | Retrieve all facilities visible by the project |
| [**find_ip_reservation_customdata**](ProjectsApi.md#find_ip_reservation_customdata) | **GET** /projects/{project_id}/ips/{id}/customdata | Retrieve the custom metadata of an IP Reservation |
| [**find_ip_reservations**](ProjectsApi.md#find_ip_reservations) | **GET** /projects/{id}/ips | Retrieve all ip reservations |
| [**find_organization_projects**](ProjectsApi.md#find_organization_projects) | **GET** /organizations/{id}/projects | Retrieve all projects of an organization |
| [**find_plans_by_project**](ProjectsApi.md#find_plans_by_project) | **GET** /projects/{id}/plans | Retrieve all plans visible by the project |
| [**find_project_bgp_sessions**](ProjectsApi.md#find_project_bgp_sessions) | **GET** /projects/{id}/bgp/sessions | Retrieve all BGP sessions for project |
| [**find_project_by_id**](ProjectsApi.md#find_project_by_id) | **GET** /projects/{id} | Retrieve a project |
| [**find_project_customdata**](ProjectsApi.md#find_project_customdata) | **GET** /projects/{id}/customdata | Retrieve the custom metadata of a project |
| [**find_project_devices**](ProjectsApi.md#find_project_devices) | **GET** /projects/{id}/devices | Retrieve all devices of a project |
| [**find_project_events**](ProjectsApi.md#find_project_events) | **GET** /projects/{id}/events | Retrieve project&#39;s events |
| [**find_project_hardware_reservations**](ProjectsApi.md#find_project_hardware_reservations) | **GET** /projects/{id}/hardware-reservations | Retrieve all hardware reservations for a given project |
| [**find_project_invitations**](ProjectsApi.md#find_project_invitations) | **GET** /projects/{project_id}/invitations | Retrieve project invitations |
| [**find_project_licenses**](ProjectsApi.md#find_project_licenses) | **GET** /projects/{id}/licenses | Retrieve all licenses |
| [**find_project_memberships**](ProjectsApi.md#find_project_memberships) | **GET** /projects/{project_id}/memberships | Retrieve project memberships |
| [**find_project_ssh_keys**](ProjectsApi.md#find_project_ssh_keys) | **GET** /projects/{id}/ssh-keys | Retrieve a project&#39;s ssh keys |
| [**find_projects**](ProjectsApi.md#find_projects) | **GET** /projects | Retrieve all projects |
| [**find_virtual_networks**](ProjectsApi.md#find_virtual_networks) | **GET** /projects/{id}/virtual-networks | Retrieve all virtual networks |
| [**list_spot_market_requests**](ProjectsApi.md#list_spot_market_requests) | **GET** /projects/{id}/spot-market-requests | List spot market requests |
| [**request_bgp_config**](ProjectsApi.md#request_bgp_config) | **POST** /projects/{id}/bgp-configs | Requesting bgp config |
| [**request_ip_reservation**](ProjectsApi.md#request_ip_reservation) | **POST** /projects/{id}/ips | Requesting IP reservations |
| [**update_project**](ProjectsApi.md#update_project) | **PUT** /projects/{id} | Update the project |


## create_device

> <Device> create_device(id, device)

Create a device

Creates a new device and provisions it in our datacenter.  Type-specific options (such as operating_system for baremetal devices) should be included in the main data structure alongside hostname and plan.  The features attribute allows you to optionally specify what features your server should have.  For example, if you require a server with a TPM chip, you may specify `{ \"features\": { \"tpm\": \"required\" } }` (or `{ \"features\": [\"tpm\"] }` in shorthand).  The request will fail if there are no available servers matching your criteria. Alternatively, if you do not require a certain feature, but would prefer to be assigned a server with that feature if there are any available, you may specify that feature with a preferred value (see the example request below).  The request will not fail if we have no servers with that feature in our inventory.  The facilities attribute specifies in what datacenter you wish to create the device.  You can either specify a single facility `{ \"facility\": \"f1\" }` , or you can instruct to create the device in the best available datacenter `{ \"facility\": \"any\" }`. Additionally it is possible to set a prioritized location selection.  For example `{ \"facility\": [\"f3\", \"f2\", \"any\"] }` will try to assign to the facility f3, if there are no available f2, and so on. If \"any\" is not specified for \"facility\", the request will fail unless it can assign in the selected locations.  The `ip_addresses attribute will allow you to specify the addresses you want created with your device.  To maintain backwards compatibility, If the attribute is not sent in the request, it will be treated as if `{ \"ip_addresses\": [{ \"address_family\": 4, \"public\": true }, { \"address_family\": 4, \"public\": false }, { \"address_family\": 6, \"public\": true }] }` was sent.  The private IPv4 address is required and always need to be sent in the array. Not all operating systems support no public IPv4 address, so in those cases you will receive an error message.  For example, to only configure your server with a private IPv4 address, you can send `{ \"ip_addresses\": [{ \"address_family\": 4, \"public\": false }] }`.  Note: when specifying a subnet size larger than a /30, you will need to supply the UUID(s) of existing ip_reservations in your project to assign IPs from.  For example, `{ \"ip_addresses\": [..., {\"address_family\": 4, \"public\": true, \"ip_reservations\": [\"uuid1\", \"uuid2\"]}] }`  To access a server without public IPs, you can use our Out-of-Band console access (SOS) or use another server with public IPs as a proxy. 

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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | Project UUID
device = OpenapiClient::DeviceCreateInput.new({facility: 'facility_example', plan: 'plan_example', operating_system: 'operating_system_example'}) # DeviceCreateInput | Device to create

begin
  # Create a device
  result = api_instance.create_device(id, device)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->create_device: #{e}"
end
```

#### Using the create_device_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Device>, Integer, Hash)> create_device_with_http_info(id, device)

```ruby
begin
  # Create a device
  data, status_code, headers = api_instance.create_device_with_http_info(id, device)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Device>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->create_device_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **device** | [**DeviceCreateInput**](DeviceCreateInput.md) | Device to create |  |

### Return type

[**Device**](Device.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | Project UUID
license = OpenapiClient::LicenseCreateInput.new # LicenseCreateInput | License to create

begin
  # Create a License
  result = api_instance.create_license(id, license)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->create_license: #{e}"
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
  puts "Error when calling ProjectsApi->create_license_with_http_info: #{e}"
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


## create_organization_project

> <Project> create_organization_project(id, project)

Create a project for the organization

Creates a new project for the organization

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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | Organization UUID
project = OpenapiClient::ProjectCreateInput.new({name: 'name_example'}) # ProjectCreateInput | Project to create

begin
  # Create a project for the organization
  result = api_instance.create_organization_project(id, project)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->create_organization_project: #{e}"
end
```

#### Using the create_organization_project_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Project>, Integer, Hash)> create_organization_project_with_http_info(id, project)

```ruby
begin
  # Create a project for the organization
  data, status_code, headers = api_instance.create_organization_project_with_http_info(id, project)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Project>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->create_organization_project_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Organization UUID |  |
| **project** | [**ProjectCreateInput**](ProjectCreateInput.md) | Project to create |  |

### Return type

[**Project**](Project.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## create_project

> <Project> create_project(project)

Create a project

Creates a new project for the user default organization. If the user don't have an organization, a new one will be created.

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

api_instance = OpenapiClient::ProjectsApi.new
project = OpenapiClient::ProjectCreateFromRootInput.new({name: 'name_example'}) # ProjectCreateFromRootInput | Project to create

begin
  # Create a project
  result = api_instance.create_project(project)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->create_project: #{e}"
end
```

#### Using the create_project_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Project>, Integer, Hash)> create_project_with_http_info(project)

```ruby
begin
  # Create a project
  data, status_code, headers = api_instance.create_project_with_http_info(project)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Project>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->create_project_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project** | [**ProjectCreateFromRootInput**](ProjectCreateFromRootInput.md) | Project to create |  |

### Return type

[**Project**](Project.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## create_project_invitation

> <Invitation> create_project_invitation(project_id, invitation)

Create an invitation for a project

In order to add a user to a project, they must first be invited.

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

api_instance = OpenapiClient::ProjectsApi.new
project_id = TODO # String | Project UUID
invitation = OpenapiClient::InvitationInput.new({invitee: 'invitee_example'}) # InvitationInput | Invitation to create

begin
  # Create an invitation for a project
  result = api_instance.create_project_invitation(project_id, invitation)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->create_project_invitation: #{e}"
end
```

#### Using the create_project_invitation_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Invitation>, Integer, Hash)> create_project_invitation_with_http_info(project_id, invitation)

```ruby
begin
  # Create an invitation for a project
  data, status_code, headers = api_instance.create_project_invitation_with_http_info(project_id, invitation)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Invitation>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->create_project_invitation_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_id** | [**String**](.md) | Project UUID |  |
| **invitation** | [**InvitationInput**](InvitationInput.md) | Invitation to create |  |

### Return type

[**Invitation**](Invitation.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## create_project_ssh_key

> <SSHKey> create_project_ssh_key(id, ssh_key)

Create a ssh key for the given project

Creates a ssh key.

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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | Project UUID
ssh_key = OpenapiClient::SSHKeyInput.new # SSHKeyInput | ssh key to create

begin
  # Create a ssh key for the given project
  result = api_instance.create_project_ssh_key(id, ssh_key)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->create_project_ssh_key: #{e}"
end
```

#### Using the create_project_ssh_key_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SSHKey>, Integer, Hash)> create_project_ssh_key_with_http_info(id, ssh_key)

```ruby
begin
  # Create a ssh key for the given project
  data, status_code, headers = api_instance.create_project_ssh_key_with_http_info(id, ssh_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SSHKey>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->create_project_ssh_key_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **ssh_key** | [**SSHKeyInput**](SSHKeyInput.md) | ssh key to create |  |

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## create_spot_market_request

> <SpotMarketRequest> create_spot_market_request(id, spot_market_request)

Create a spot market request

Creates a new spot market request.  Type-specific options (such as operating_system for baremetal devices) should be included in the main data structure alongside hostname and plan.  The features attribute allows you to optionally specify what features your server should have. For example, if you require a server with a TPM chip, you may specify `{ \"features\": { \"tpm\": \"required\" } }` (or `{ \"features\": [\"tpm\"] }` in shorthand).  The request will fail if there are no available servers matching your criteria. Alternatively, if you do not require a certain feature, but would prefer to be assigned a server with that feature if there are any available, you may specify that feature with a preferred value (see the example request below).  The request will not fail if we have no servers with that feature in our inventory.

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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | Project UUID
spot_market_request = OpenapiClient::SpotMarketRequestCreateInput.new # SpotMarketRequestCreateInput | Spot Market Request to create

begin
  # Create a spot market request
  result = api_instance.create_spot_market_request(id, spot_market_request)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->create_spot_market_request: #{e}"
end
```

#### Using the create_spot_market_request_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SpotMarketRequest>, Integer, Hash)> create_spot_market_request_with_http_info(id, spot_market_request)

```ruby
begin
  # Create a spot market request
  data, status_code, headers = api_instance.create_spot_market_request_with_http_info(id, spot_market_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SpotMarketRequest>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->create_spot_market_request_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **spot_market_request** | [**SpotMarketRequestCreateInput**](SpotMarketRequestCreateInput.md) | Spot Market Request to create |  |

### Return type

[**SpotMarketRequest**](SpotMarketRequest.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## create_transfer_request

> <TransferRequest> create_transfer_request(id, transfer_request)

Create a transfer request

Organization owners can transfer their projects to other organizations.

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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | UUID of the project to be transferred
transfer_request = OpenapiClient::TransferRequestInput.new # TransferRequestInput | Transfer Request to create

begin
  # Create a transfer request
  result = api_instance.create_transfer_request(id, transfer_request)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->create_transfer_request: #{e}"
end
```

#### Using the create_transfer_request_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TransferRequest>, Integer, Hash)> create_transfer_request_with_http_info(id, transfer_request)

```ruby
begin
  # Create a transfer request
  data, status_code, headers = api_instance.create_transfer_request_with_http_info(id, transfer_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TransferRequest>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->create_transfer_request_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | UUID of the project to be transferred |  |
| **transfer_request** | [**TransferRequestInput**](TransferRequestInput.md) | Transfer Request to create |  |

### Return type

[**TransferRequest**](TransferRequest.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## create_virtual_network

> <VirtualNetwork> create_virtual_network(id, virtual_network)

Create an virtual network

Creates an virtual network.

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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | Project UUID
virtual_network = OpenapiClient::VirtualNetworkCreateInput.new # VirtualNetworkCreateInput | Virtual Network to create

begin
  # Create an virtual network
  result = api_instance.create_virtual_network(id, virtual_network)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->create_virtual_network: #{e}"
end
```

#### Using the create_virtual_network_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<VirtualNetwork>, Integer, Hash)> create_virtual_network_with_http_info(id, virtual_network)

```ruby
begin
  # Create an virtual network
  data, status_code, headers = api_instance.create_virtual_network_with_http_info(id, virtual_network)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <VirtualNetwork>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->create_virtual_network_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **virtual_network** | [**VirtualNetworkCreateInput**](VirtualNetworkCreateInput.md) | Virtual Network to create |  |

### Return type

[**VirtualNetwork**](VirtualNetwork.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## delete_project

> delete_project(id)

Delete the project

Deletes the project.

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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | Project UUID

begin
  # Delete the project
  api_instance.delete_project(id)
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->delete_project: #{e}"
end
```

#### Using the delete_project_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> delete_project_with_http_info(id)

```ruby
begin
  # Delete the project
  data, status_code, headers = api_instance.delete_project_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->delete_project_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## find_batches_by_project

> <BatchesList> find_batches_by_project(id, opts)

Retrieve all batches by project

Returns all batches for the given project

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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | Project UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve all batches by project
  result = api_instance.find_batches_by_project(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_batches_by_project: #{e}"
end
```

#### Using the find_batches_by_project_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BatchesList>, Integer, Hash)> find_batches_by_project_with_http_info(id, opts)

```ruby
begin
  # Retrieve all batches by project
  data, status_code, headers = api_instance.find_batches_by_project_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BatchesList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_batches_by_project_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**BatchesList**](BatchesList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_bgp_config_by_project

> <BgpConfig> find_bgp_config_by_project(id, opts)

Retrieve a bgp config

Returns a bgp config

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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | Project UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve a bgp config
  result = api_instance.find_bgp_config_by_project(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_bgp_config_by_project: #{e}"
end
```

#### Using the find_bgp_config_by_project_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BgpConfig>, Integer, Hash)> find_bgp_config_by_project_with_http_info(id, opts)

```ruby
begin
  # Retrieve a bgp config
  data, status_code, headers = api_instance.find_bgp_config_by_project_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BgpConfig>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_bgp_config_by_project_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**BgpConfig**](BgpConfig.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_device_ssh_keys

> <SSHKeyList> find_device_ssh_keys(id, opts)

Retrieve a device's ssh keys

Returns a collection of the device's ssh keys.

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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | Project UUID
opts = {
  search_string: 'search_string_example', # String | Search by key, label, or fingerprint
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve a device's ssh keys
  result = api_instance.find_device_ssh_keys(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_device_ssh_keys: #{e}"
end
```

#### Using the find_device_ssh_keys_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SSHKeyList>, Integer, Hash)> find_device_ssh_keys_with_http_info(id, opts)

```ruby
begin
  # Retrieve a device's ssh keys
  data, status_code, headers = api_instance.find_device_ssh_keys_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SSHKeyList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_device_ssh_keys_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **search_string** | **String** | Search by key, label, or fingerprint | [optional] |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**SSHKeyList**](SSHKeyList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_facilities_by_project

> <FacilityList> find_facilities_by_project(id, opts)

Retrieve all facilities visible by the project

Returns a listing of available datacenters for the given project

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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | Project UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve all facilities visible by the project
  result = api_instance.find_facilities_by_project(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_facilities_by_project: #{e}"
end
```

#### Using the find_facilities_by_project_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FacilityList>, Integer, Hash)> find_facilities_by_project_with_http_info(id, opts)

```ruby
begin
  # Retrieve all facilities visible by the project
  data, status_code, headers = api_instance.find_facilities_by_project_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FacilityList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_facilities_by_project_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**FacilityList**](FacilityList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_ip_reservation_customdata

> find_ip_reservation_customdata(project_id, id)

Retrieve the custom metadata of an IP Reservation

Provides the custom metadata stored for this IP Reservation in json format

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

api_instance = OpenapiClient::ProjectsApi.new
project_id = TODO # String | Project UUID
id = TODO # String | Ip Reservation UUID

begin
  # Retrieve the custom metadata of an IP Reservation
  api_instance.find_ip_reservation_customdata(project_id, id)
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_ip_reservation_customdata: #{e}"
end
```

#### Using the find_ip_reservation_customdata_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> find_ip_reservation_customdata_with_http_info(project_id, id)

```ruby
begin
  # Retrieve the custom metadata of an IP Reservation
  data, status_code, headers = api_instance.find_ip_reservation_customdata_with_http_info(project_id, id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_ip_reservation_customdata_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_id** | [**String**](.md) | Project UUID |  |
| **id** | [**String**](.md) | Ip Reservation UUID |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## find_ip_reservations

> <IPReservationList> find_ip_reservations(id, opts)

Retrieve all ip reservations

Provides a list of IP resevations for a single project.

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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | Project UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve all ip reservations
  result = api_instance.find_ip_reservations(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_ip_reservations: #{e}"
end
```

#### Using the find_ip_reservations_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<IPReservationList>, Integer, Hash)> find_ip_reservations_with_http_info(id, opts)

```ruby
begin
  # Retrieve all ip reservations
  data, status_code, headers = api_instance.find_ip_reservations_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <IPReservationList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_ip_reservations_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**IPReservationList**](IPReservationList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_organization_projects

> <ProjectList> find_organization_projects(id, opts)

Retrieve all projects of an organization

Returns a collection of projects that belong to the organization.

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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | Organization UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve all projects of an organization
  result = api_instance.find_organization_projects(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_organization_projects: #{e}"
end
```

#### Using the find_organization_projects_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectList>, Integer, Hash)> find_organization_projects_with_http_info(id, opts)

```ruby
begin
  # Retrieve all projects of an organization
  data, status_code, headers = api_instance.find_organization_projects_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_organization_projects_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Organization UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |
| **page** | **Integer** | Page to return | [optional][default to 1] |
| **per_page** | **Integer** | Items returned per page | [optional][default to 10] |

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_plans_by_project

> <PlanList> find_plans_by_project(id, opts)

Retrieve all plans visible by the project

Returns a listing of available plans for the given project

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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | Project UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve all plans visible by the project
  result = api_instance.find_plans_by_project(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_plans_by_project: #{e}"
end
```

#### Using the find_plans_by_project_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PlanList>, Integer, Hash)> find_plans_by_project_with_http_info(id, opts)

```ruby
begin
  # Retrieve all plans visible by the project
  data, status_code, headers = api_instance.find_plans_by_project_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PlanList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_plans_by_project_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**PlanList**](PlanList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_project_bgp_sessions

> <BgpSessionList> find_project_bgp_sessions(id)

Retrieve all BGP sessions for project

Provides a listing of available BGP sessions for the project.

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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | Project UUID

begin
  # Retrieve all BGP sessions for project
  result = api_instance.find_project_bgp_sessions(id)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_project_bgp_sessions: #{e}"
end
```

#### Using the find_project_bgp_sessions_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BgpSessionList>, Integer, Hash)> find_project_bgp_sessions_with_http_info(id)

```ruby
begin
  # Retrieve all BGP sessions for project
  data, status_code, headers = api_instance.find_project_bgp_sessions_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BgpSessionList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_project_bgp_sessions_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |

### Return type

[**BgpSessionList**](BgpSessionList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_project_by_id

> <Project> find_project_by_id(id, opts)

Retrieve a project

Returns a single project if the user has access

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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | Project UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve a project
  result = api_instance.find_project_by_id(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_project_by_id: #{e}"
end
```

#### Using the find_project_by_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Project>, Integer, Hash)> find_project_by_id_with_http_info(id, opts)

```ruby
begin
  # Retrieve a project
  data, status_code, headers = api_instance.find_project_by_id_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Project>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_project_by_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**Project**](Project.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_project_customdata

> find_project_customdata(id)

Retrieve the custom metadata of a project

Provides the custom metadata stored for this project in json format

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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | Project UUID

begin
  # Retrieve the custom metadata of a project
  api_instance.find_project_customdata(id)
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_project_customdata: #{e}"
end
```

#### Using the find_project_customdata_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> find_project_customdata_with_http_info(id)

```ruby
begin
  # Retrieve the custom metadata of a project
  data, status_code, headers = api_instance.find_project_customdata_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_project_customdata_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## find_project_devices

> <DeviceList> find_project_devices(id, opts)

Retrieve all devices of a project

Provides a collection of devices for a given project.

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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | Project UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve all devices of a project
  result = api_instance.find_project_devices(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_project_devices: #{e}"
end
```

#### Using the find_project_devices_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<DeviceList>, Integer, Hash)> find_project_devices_with_http_info(id, opts)

```ruby
begin
  # Retrieve all devices of a project
  data, status_code, headers = api_instance.find_project_devices_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <DeviceList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_project_devices_with_http_info: #{e}"
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

[**DeviceList**](DeviceList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_project_events

> <EventList> find_project_events(id, opts)

Retrieve project's events

Returns a list of events for a single project

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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | Project UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve project's events
  result = api_instance.find_project_events(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_project_events: #{e}"
end
```

#### Using the find_project_events_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<EventList>, Integer, Hash)> find_project_events_with_http_info(id, opts)

```ruby
begin
  # Retrieve project's events
  data, status_code, headers = api_instance.find_project_events_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <EventList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_project_events_with_http_info: #{e}"
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

[**EventList**](EventList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_project_hardware_reservations

> <HardwareReservationList> find_project_hardware_reservations(id, opts)

Retrieve all hardware reservations for a given project

Provides a collection of hardware reservations for a given project.

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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | Project UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve all hardware reservations for a given project
  result = api_instance.find_project_hardware_reservations(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_project_hardware_reservations: #{e}"
end
```

#### Using the find_project_hardware_reservations_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<HardwareReservationList>, Integer, Hash)> find_project_hardware_reservations_with_http_info(id, opts)

```ruby
begin
  # Retrieve all hardware reservations for a given project
  data, status_code, headers = api_instance.find_project_hardware_reservations_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <HardwareReservationList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_project_hardware_reservations_with_http_info: #{e}"
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

[**HardwareReservationList**](HardwareReservationList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_project_invitations

> <InvitationList> find_project_invitations(project_id, opts)

Retrieve project invitations

Returns all invitations in a project.

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

api_instance = OpenapiClient::ProjectsApi.new
project_id = TODO # String | Project UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve project invitations
  result = api_instance.find_project_invitations(project_id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_project_invitations: #{e}"
end
```

#### Using the find_project_invitations_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<InvitationList>, Integer, Hash)> find_project_invitations_with_http_info(project_id, opts)

```ruby
begin
  # Retrieve project invitations
  data, status_code, headers = api_instance.find_project_invitations_with_http_info(project_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <InvitationList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_project_invitations_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_id** | [**String**](.md) | Project UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |
| **page** | **Integer** | Page to return | [optional][default to 1] |
| **per_page** | **Integer** | Items returned per page | [optional][default to 10] |

### Return type

[**InvitationList**](InvitationList.md)

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

api_instance = OpenapiClient::ProjectsApi.new
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
  puts "Error when calling ProjectsApi->find_project_licenses: #{e}"
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
  puts "Error when calling ProjectsApi->find_project_licenses_with_http_info: #{e}"
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


## find_project_memberships

> <MembershipList> find_project_memberships(project_id, opts)

Retrieve project memberships

Returns all memberships in a project.

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

api_instance = OpenapiClient::ProjectsApi.new
project_id = TODO # String | Project UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve project memberships
  result = api_instance.find_project_memberships(project_id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_project_memberships: #{e}"
end
```

#### Using the find_project_memberships_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<MembershipList>, Integer, Hash)> find_project_memberships_with_http_info(project_id, opts)

```ruby
begin
  # Retrieve project memberships
  data, status_code, headers = api_instance.find_project_memberships_with_http_info(project_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <MembershipList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_project_memberships_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_id** | [**String**](.md) | Project UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |
| **page** | **Integer** | Page to return | [optional][default to 1] |
| **per_page** | **Integer** | Items returned per page | [optional][default to 10] |

### Return type

[**MembershipList**](MembershipList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_project_ssh_keys

> <SSHKeyList> find_project_ssh_keys(id, opts)

Retrieve a project's ssh keys

Returns a collection of the project's ssh keys.

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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | Project UUID
opts = {
  search_string: 'search_string_example', # String | Search by key, label, or fingerprint
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve a project's ssh keys
  result = api_instance.find_project_ssh_keys(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_project_ssh_keys: #{e}"
end
```

#### Using the find_project_ssh_keys_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SSHKeyList>, Integer, Hash)> find_project_ssh_keys_with_http_info(id, opts)

```ruby
begin
  # Retrieve a project's ssh keys
  data, status_code, headers = api_instance.find_project_ssh_keys_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SSHKeyList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_project_ssh_keys_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **search_string** | **String** | Search by key, label, or fingerprint | [optional] |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**SSHKeyList**](SSHKeyList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_projects

> <ProjectList> find_projects(opts)

Retrieve all projects

Returns a collection of projects that the current user is a member of.

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

api_instance = OpenapiClient::ProjectsApi.new
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve all projects
  result = api_instance.find_projects(opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_projects: #{e}"
end
```

#### Using the find_projects_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectList>, Integer, Hash)> find_projects_with_http_info(opts)

```ruby
begin
  # Retrieve all projects
  data, status_code, headers = api_instance.find_projects_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_projects_with_http_info: #{e}"
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

[**ProjectList**](ProjectList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_virtual_networks

> <VirtualNetworkList> find_virtual_networks(id, opts)

Retrieve all virtual networks

Provides a list of virtual networks for a single project.

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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | Project UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve all virtual networks
  result = api_instance.find_virtual_networks(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_virtual_networks: #{e}"
end
```

#### Using the find_virtual_networks_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<VirtualNetworkList>, Integer, Hash)> find_virtual_networks_with_http_info(id, opts)

```ruby
begin
  # Retrieve all virtual networks
  data, status_code, headers = api_instance.find_virtual_networks_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <VirtualNetworkList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->find_virtual_networks_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**VirtualNetworkList**](VirtualNetworkList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## list_spot_market_requests

> <SpotMarketRequestList> list_spot_market_requests(id)

List spot market requests

View all spot market requests for a given project.

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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | Project UUID

begin
  # List spot market requests
  result = api_instance.list_spot_market_requests(id)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->list_spot_market_requests: #{e}"
end
```

#### Using the list_spot_market_requests_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SpotMarketRequestList>, Integer, Hash)> list_spot_market_requests_with_http_info(id)

```ruby
begin
  # List spot market requests
  data, status_code, headers = api_instance.list_spot_market_requests_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SpotMarketRequestList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->list_spot_market_requests_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |

### Return type

[**SpotMarketRequestList**](SpotMarketRequestList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## request_bgp_config

> request_bgp_config(id, bgp_config_request)

Requesting bgp config

Requests to enable bgp configuration for a project.

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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | Project UUID
bgp_config_request = OpenapiClient::BgpConfigRequestInput.new({deployment_type: 'deployment_type_example', asn: 37}) # BgpConfigRequestInput | BGP config Request to create

begin
  # Requesting bgp config
  api_instance.request_bgp_config(id, bgp_config_request)
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->request_bgp_config: #{e}"
end
```

#### Using the request_bgp_config_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> request_bgp_config_with_http_info(id, bgp_config_request)

```ruby
begin
  # Requesting bgp config
  data, status_code, headers = api_instance.request_bgp_config_with_http_info(id, bgp_config_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->request_bgp_config_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **bgp_config_request** | [**BgpConfigRequestInput**](BgpConfigRequestInput.md) | BGP config Request to create |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## request_ip_reservation

> <IPReservation> request_ip_reservation(id, ip_reservation_request)

Requesting IP reservations

Request more IP space for a project in order to have additional IP addresses to assign to devices.  If the request is within the max quota, an IP reservation will be created. If the project will exceed its IP quota, a request will be submitted for review, and will return an IP Reservation with a `state` of `pending`. You can automatically have the request fail with HTTP status 422 instead of triggering the review process by providing the `fail_on_approval_required` parameter set to `true` in the request.

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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | Project UUID
ip_reservation_request = OpenapiClient::IPReservationRequestInput.new({type: 'type_example', quantity: 37}) # IPReservationRequestInput | IP Reservation Request to create

begin
  # Requesting IP reservations
  result = api_instance.request_ip_reservation(id, ip_reservation_request)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->request_ip_reservation: #{e}"
end
```

#### Using the request_ip_reservation_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<IPReservation>, Integer, Hash)> request_ip_reservation_with_http_info(id, ip_reservation_request)

```ruby
begin
  # Requesting IP reservations
  data, status_code, headers = api_instance.request_ip_reservation_with_http_info(id, ip_reservation_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <IPReservation>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->request_ip_reservation_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **ip_reservation_request** | [**IPReservationRequestInput**](IPReservationRequestInput.md) | IP Reservation Request to create |  |

### Return type

[**IPReservation**](IPReservation.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## update_project

> <Project> update_project(id, project)

Update the project

Updates the project.

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

api_instance = OpenapiClient::ProjectsApi.new
id = TODO # String | Project UUID
project = OpenapiClient::ProjectUpdateInput.new # ProjectUpdateInput | Project to update

begin
  # Update the project
  result = api_instance.update_project(id, project)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->update_project: #{e}"
end
```

#### Using the update_project_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Project>, Integer, Hash)> update_project_with_http_info(id, project)

```ruby
begin
  # Update the project
  data, status_code, headers = api_instance.update_project_with_http_info(id, project)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Project>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ProjectsApi->update_project_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **project** | [**ProjectUpdateInput**](ProjectUpdateInput.md) | Project to update |  |

### Return type

[**Project**](Project.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

