=begin
#Metal API

#This is the API for Equinix Metal Product. Interact with your devices, user account, and projects.

The version of the OpenAPI document: 1.0.0
Contact: support@equinixmetal.com
Generated by: https://openapi-generator.tech
OpenAPI Generator version: 5.1.0-SNAPSHOT

=end

require 'spec_helper'
require 'json'

# Unit tests for OpenapiClient::DevicesApi
# Automatically generated by openapi-generator (https://openapi-generator.tech)
# Please update as you see appropriate
describe 'DevicesApi' do
  before do
    # run before each test
    @api_instance = OpenapiClient::DevicesApi.new
  end

  after do
    # run after each test
  end

  describe 'test an instance of DevicesApi' do
    it 'should create an instance of DevicesApi' do
      expect(@api_instance).to be_instance_of(OpenapiClient::DevicesApi)
    end
  end

  # unit tests for create_bgp_session
  # Create a BGP session
  # Creates a BGP session.
  # @param id Device UUID
  # @param bgp_session BGP session to create
  # @param [Hash] opts the optional parameters
  # @return [BgpSession]
  describe 'create_bgp_session test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for create_device
  # Create a device
  # Creates a new device and provisions it in our datacenter.  Type-specific options (such as operating_system for baremetal devices) should be included in the main data structure alongside hostname and plan.  The features attribute allows you to optionally specify what features your server should have.  For example, if you require a server with a TPM chip, you may specify &#x60;{ \&quot;features\&quot;: { \&quot;tpm\&quot;: \&quot;required\&quot; } }&#x60; (or &#x60;{ \&quot;features\&quot;: [\&quot;tpm\&quot;] }&#x60; in shorthand).  The request will fail if there are no available servers matching your criteria. Alternatively, if you do not require a certain feature, but would prefer to be assigned a server with that feature if there are any available, you may specify that feature with a preferred value (see the example request below).  The request will not fail if we have no servers with that feature in our inventory.  The facilities attribute specifies in what datacenter you wish to create the device.  You can either specify a single facility &#x60;{ \&quot;facility\&quot;: \&quot;f1\&quot; }&#x60; , or you can instruct to create the device in the best available datacenter &#x60;{ \&quot;facility\&quot;: \&quot;any\&quot; }&#x60;. Additionally it is possible to set a prioritized location selection.  For example &#x60;{ \&quot;facility\&quot;: [\&quot;f3\&quot;, \&quot;f2\&quot;, \&quot;any\&quot;] }&#x60; will try to assign to the facility f3, if there are no available f2, and so on. If \&quot;any\&quot; is not specified for \&quot;facility\&quot;, the request will fail unless it can assign in the selected locations.  The &#x60;ip_addresses attribute will allow you to specify the addresses you want created with your device.  To maintain backwards compatibility, If the attribute is not sent in the request, it will be treated as if &#x60;{ \&quot;ip_addresses\&quot;: [{ \&quot;address_family\&quot;: 4, \&quot;public\&quot;: true }, { \&quot;address_family\&quot;: 4, \&quot;public\&quot;: false }, { \&quot;address_family\&quot;: 6, \&quot;public\&quot;: true }] }&#x60; was sent.  The private IPv4 address is required and always need to be sent in the array. Not all operating systems support no public IPv4 address, so in those cases you will receive an error message.  For example, to only configure your server with a private IPv4 address, you can send &#x60;{ \&quot;ip_addresses\&quot;: [{ \&quot;address_family\&quot;: 4, \&quot;public\&quot;: false }] }&#x60;.  Note: when specifying a subnet size larger than a /30, you will need to supply the UUID(s) of existing ip_reservations in your project to assign IPs from.  For example, &#x60;{ \&quot;ip_addresses\&quot;: [..., {\&quot;address_family\&quot;: 4, \&quot;public\&quot;: true, \&quot;ip_reservations\&quot;: [\&quot;uuid1\&quot;, \&quot;uuid2\&quot;]}] }&#x60;  To access a server without public IPs, you can use our Out-of-Band console access (SOS) or use another server with public IPs as a proxy. 
  # @param id Project UUID
  # @param device Device to create
  # @param [Hash] opts the optional parameters
  # @return [Device]
  describe 'create_device test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for create_device_batch
  # Create a devices batch
  # Creates new devices in batch and provisions them in our datacenter.  Type-specific options (such as operating_system for baremetal devices) should be included in the main data structure alongside hostname and plan.  The features attribute allows you to optionally specify what features your server should have.  For example, if you require a server with a TPM chip, you may specify &#x60;{ \&quot;features\&quot;: { \&quot;tpm\&quot;: \&quot;required\&quot; } }&#x60; (or &#x60;{ \&quot;features\&quot;: [\&quot;tpm\&quot;] }&#x60; in shorthand).  The request will fail if there are no available servers matching your criteria. Alternatively, if you do not require a certain feature, but would prefer to be assigned a server with that feature if there are any available, you may specify that feature with a preferred value (see the example request below).  The request will not fail if we have no servers with that feature in our inventory.  The facilities attribute specifies in what datacenter you wish to create the device.  You can either specify a single facility &#x60;{ \&quot;facility\&quot;: \&quot;f1\&quot; }&#x60; , or you can instruct to create the device in the best available datacenter &#x60;{ \&quot;facility\&quot;: \&quot;any\&quot; }&#x60;. Additionally it is possible to set a prioritized location selection.  For example &#x60;{ \&quot;facility\&quot;: [\&quot;f3\&quot;, \&quot;f2\&quot;, \&quot;any\&quot;] }&#x60; will try to assign to the facility f3, if there are no available f2, and so on. If \&quot;any\&quot; is not specified for \&quot;facility\&quot;, the request will fail unless it can assign in the selected locations.  With &#x60;{ \&quot;facility\&quot;: \&quot;any\&quot; }&#x60; you have the option to diversify to indicate how many facilities you are willing to be spread across. For this purpose use parameter: &#x60;facility_diversity_level &#x3D; N&#x60;.  For example:  &#x60;{ \&quot;facilities\&quot;: [\&quot;sjc1\&quot;, \&quot;ewr1\&quot;, \&quot;any\&quot;] ,  \&quot;facility_diversity_level\&quot; &#x3D; 1, \&quot;quantity\&quot; &#x3D; 10 }&#x60; will assign 10 devices into the same facility, trying first in \&quot;sjc1\&quot;, and if there aren’t available, it will try in  \&quot;ewr1\&quot;, otherwise any other.  The &#x60;ip_addresses&#x60; attribute will allow you to specify the addresses you want created with your device.  To maintain backwards compatibility, If the attribute is not sent in the request, it will be treated as if &#x60;{ \&quot;ip_addresses\&quot;: [{ \&quot;address_family\&quot;: 4, \&quot;public\&quot;: true }, { \&quot;address_family\&quot;: 4, \&quot;public\&quot;: false }, { \&quot;address_family\&quot;: 6, \&quot;public\&quot;: true }] }&#x60; was sent.  The private IPv4 address is required and always need to be sent in the array. Not all operating systems support no public IPv4 address, so in those cases you will receive an error message.  For example, to only configure your server with a private IPv4 address, you can send &#x60;{ \&quot;ip_addresses\&quot;: [{ \&quot;address_family\&quot;: 4, \&quot;public\&quot;: false }] }&#x60;.  Note: when specifying a subnet size larger than a /30, you will need to supply the UUID(s) of existing ip_reservations in your project to assign IPs from.  For example, &#x60;{ \&quot;ip_addresses\&quot;: [..., {\&quot;address_family\&quot;: 4, \&quot;public\&quot;: true, \&quot;ip_reservations\&quot;: [\&quot;uuid1\&quot;, \&quot;uuid2\&quot;]}] }&#x60;  To access a server without public IPs, you can use our Out-of-Band console access (SOS) or use another server with public IPs as a proxy.
  # @param id Project UUID
  # @param batch Batches to create
  # @param [Hash] opts the optional parameters
  # @return [BatchesList]
  describe 'create_device_batch test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for create_ip_assignment
  # Create a ip assignment
  # Creates an ip assignment for a device.
  # @param id Device UUID
  # @param ip_assignment IPAssignment to create
  # @param [Hash] opts the optional parameters
  # @return [IPAssignment]
  describe 'create_ip_assignment test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for delete_device
  # Delete the device
  # Deletes a device and deprovisions it in our datacenter.
  # @param id Device UUID
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :force_delete Force the deletion of the device, by detaching any storage volume still active.
  # @return [nil]
  describe 'delete_device test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for find_bgp_sessions
  # Retrieve all BGP sessions
  # Provides a listing of available BGP sessions for the device.
  # @param id Device UUID
  # @param [Hash] opts the optional parameters
  # @return [BgpSessionList]
  describe 'find_bgp_sessions test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for find_device_by_id
  # Retrieve a device
  # Type-specific options (such as facility for baremetal devices) will be included as part of the main data structure.                          State value can be one of: active inactive queued or provisioning
  # @param id Device UUID
  # @param [Hash] opts the optional parameters
  # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  # @return [Device]
  describe 'find_device_by_id test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for find_device_customdata
  # Retrieve the custom metadata of an instance
  # Provides the custom metadata stored for this instance in json format
  # @param id Instance UUID
  # @param [Hash] opts the optional parameters
  # @return [nil]
  describe 'find_device_customdata test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for find_device_events
  # Retrieve device&#39;s events
  # Returns a list of events pertaining to a specific device
  # @param id Device UUID
  # @param [Hash] opts the optional parameters
  # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  # @option opts [Integer] :page Page to return
  # @option opts [Integer] :per_page Items returned per page
  # @return [EventList]
  describe 'find_device_events test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for find_device_usages
  # Retrieve all usages for device
  # Returns all usages for a device.
  # @param id Device UUID
  # @param [Hash] opts the optional parameters
  # @option opts [String] :created_after Filter usages created after this date
  # @option opts [String] :created_before Filter usages created before this date
  # @return [DeviceUsageList]
  describe 'find_device_usages test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for find_instance_bandwidth
  # Retrieve an instance bandwidth
  # Retrieve an instance bandwidth for a given period of time.
  # @param id Device UUID
  # @param from Timestamp from range
  # @param _until Timestamp to range
  # @param [Hash] opts the optional parameters
  # @return [nil]
  describe 'find_instance_bandwidth test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for find_ip_assignment_customdata
  # Retrieve the custom metadata of an IP Assignment
  # Provides the custom metadata stored for this IP Assignment in json format
  # @param instance_id Instance UUID
  # @param id Ip Assignment UUID
  # @param [Hash] opts the optional parameters
  # @return [nil]
  describe 'find_ip_assignment_customdata test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for find_ip_assignments
  # Retrieve all ip assignments
  # Returns all ip assignments for a device.
  # @param id Device UUID
  # @param [Hash] opts the optional parameters
  # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  # @return [IPAssignmentList]
  describe 'find_ip_assignments test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for find_organization_devices
  # Retrieve all devices of an organization
  # Provides a collection of devices for a given organization.
  # @param id Organization UUID
  # @param [Hash] opts the optional parameters
  # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  # @option opts [Integer] :page Page to return
  # @option opts [Integer] :per_page Items returned per page
  # @return [DeviceList]
  describe 'find_organization_devices test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for find_project_devices
  # Retrieve all devices of a project
  # Provides a collection of devices for a given project.
  # @param id Project UUID
  # @param [Hash] opts the optional parameters
  # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  # @option opts [Integer] :page Page to return
  # @option opts [Integer] :per_page Items returned per page
  # @return [DeviceList]
  describe 'find_project_devices test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for find_project_usage
  # Retrieve all usages for project
  # Returns all usages for a project.
  # @param id Project UUID
  # @param [Hash] opts the optional parameters
  # @option opts [String] :created_after Filter usages created after this date
  # @option opts [String] :created_before Filter usages created before this date
  # @return [ProjectUsageList]
  describe 'find_project_usage test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for find_traffic
  # Retrieve device traffic
  # Returns traffic for a specific device.
  # @param id Device UUID
  # @param direction Traffic direction
  # @param timeframe Traffic timeframe
  # @param [Hash] opts the optional parameters
  # @option opts [String] :interval Traffic interval
  # @option opts [String] :bucket Traffic bucket
  # @return [nil]
  describe 'find_traffic test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for get_bgp_neighbor_data
  # Retrieve BGP neighbor data for this device
  # Provides a summary of the BGP neighbor data associated to the BGP sessions for this device.
  # @param id Device UUID
  # @param [Hash] opts the optional parameters
  # @return [BgpSessionNeighbors]
  describe 'get_bgp_neighbor_data test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for perform_action
  # Perform an action
  # Performs an action for the given device.  Possible actions include: power_on, power_off, reboot, reinstall, and rescue (reboot the device into rescue OS.)
  # @param id Device UUID
  # @param type Action to perform
  # @param [Hash] opts the optional parameters
  # @return [nil]
  describe 'perform_action test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for update_device
  # Update the device
  # Updates the device.
  # @param id Device UUID
  # @param device Facility to update
  # @param [Hash] opts the optional parameters
  # @return [Device]
  describe 'update_device test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

end