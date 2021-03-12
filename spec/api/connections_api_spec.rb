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

# Unit tests for OpenapiClient::ConnectionsApi
# Automatically generated by openapi-generator (https://openapi-generator.tech)
# Please update as you see appropriate
describe 'ConnectionsApi' do
  before do
    # run before each test
    @api_instance = OpenapiClient::ConnectionsApi.new
  end

  after do
    # run after each test
  end

  describe 'test an instance of ConnectionsApi' do
    it 'should create an instance of ConnectionsApi' do
      expect(@api_instance).to be_instance_of(OpenapiClient::ConnectionsApi)
    end
  end

  # unit tests for create_connection_port_virtual_circuit
  # Create a new Virtual Circuit
  # Create a new Virtual Circuit on a dedicated connection using a Virtual Network record and an NNI VLAN value.
  # @param connection_id UUID of the connection
  # @param port_id UUID of the connection port
  # @param virtual_circuit Virtual Circuit details
  # @param [Hash] opts the optional parameters
  # @return [VirtualCircuitList]
  describe 'create_connection_port_virtual_circuit test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for create_organization_interconnection
  # Request a new connection for the organization
  # Creates a new connection request. A Project ID must be specified in the request body for connections on shared ports.
  # @param organization_id UUID of the organization
  # @param connection Connection details
  # @param [Hash] opts the optional parameters
  # @return [Interconnection]
  describe 'create_organization_interconnection test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for create_project_interconnection
  # Request a new connection for the project&#39;s organization
  # Creates a new connection request
  # @param project_id UUID of the project
  # @param connection Connection details
  # @param [Hash] opts the optional parameters
  # @return [Interconnection]
  describe 'create_project_interconnection test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for delete_interconnection
  # Delete connection
  # Delete a connection, its associated ports and virtual circuits.
  # @param connection_id Connection UUID
  # @param [Hash] opts the optional parameters
  # @return [Interconnection]
  describe 'delete_interconnection test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for delete_virtual_circuit
  # Delete a virtual circuit
  # Delete a virtual circuit from a dedicated port.
  # @param id Virtual Circuit UUID
  # @param [Hash] opts the optional parameters
  # @return [VirtualCircuit]
  describe 'delete_virtual_circuit test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for find_connection_events
  # Retrieve connection events
  # Returns a list of the connection events
  # @param connection_id Connection UUID
  # @param [Hash] opts the optional parameters
  # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  # @option opts [Integer] :page Page to return
  # @option opts [Integer] :per_page Items returned per page
  # @return [Event]
  describe 'find_connection_events test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for find_connection_port_events
  # Retrieve connection port events
  # Returns a list of the connection port events
  # @param connection_id Connection UUID
  # @param id Connection Port UUID
  # @param [Hash] opts the optional parameters
  # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  # @option opts [Integer] :page Page to return
  # @option opts [Integer] :per_page Items returned per page
  # @return [Event]
  describe 'find_connection_port_events test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for find_virtual_circuit_events
  # Retrieve connection events
  # Returns a list of the virtual circuit events
  # @param id Virtual Circuit UUID
  # @param [Hash] opts the optional parameters
  # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  # @option opts [Integer] :page Page to return
  # @option opts [Integer] :per_page Items returned per page
  # @return [Event]
  describe 'find_virtual_circuit_events test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for get_connection_port
  # Get a connection port
  # Get the details of an connection port.
  # @param connection_id UUID of the connection
  # @param id Port UUID
  # @param [Hash] opts the optional parameters
  # @return [InterconnectionPort]
  describe 'get_connection_port test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for get_interconnection
  # Get connection
  # Get the details of a connection
  # @param connection_id Connection UUID
  # @param [Hash] opts the optional parameters
  # @return [Interconnection]
  describe 'get_interconnection test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for get_virtual_circuit
  # Get a virtual circuit
  # Get the details of a virtual circuit
  # @param id Virtual Circuit UUID
  # @param [Hash] opts the optional parameters
  # @return [VirtualCircuit]
  describe 'get_virtual_circuit test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for list_connection_port_virtual_circuits
  # List a connection port&#39;s virtual circuits
  # List the virtual circuit record(s) associatiated with a particular connection port.
  # @param connection_id UUID of the connection
  # @param port_id UUID of the connection port
  # @param [Hash] opts the optional parameters
  # @return [VirtualCircuitList]
  describe 'list_connection_port_virtual_circuits test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for list_connection_ports
  # List a connection&#39;s ports
  # List the ports associated to an connection.
  # @param connection_id UUID of the connection
  # @param [Hash] opts the optional parameters
  # @return [InterconnectionPortList]
  describe 'list_connection_ports test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for organization_list_interconnections
  # List organization connections
  # List the connections belonging to the organization
  # @param organization_id UUID of the organization
  # @param [Hash] opts the optional parameters
  # @return [InterconnectionList]
  describe 'organization_list_interconnections test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for project_list_interconnections
  # List project connections
  # List the connections belonging to the project
  # @param project_id UUID of the project
  # @param [Hash] opts the optional parameters
  # @return [InterconnectionList]
  describe 'project_list_interconnections test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for update_interconnection
  # Update connection
  # Update the details of a connection
  # @param connection_id Connection UUID
  # @param connection Updated connection details
  # @param [Hash] opts the optional parameters
  # @return [Interconnection]
  describe 'update_interconnection test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for update_virtual_circuit
  # Update a virtual circuit
  # Update the details of a virtual circuit.
  # @param id Virtual Circuit UUID
  # @param virtual_circuit Updated Virtual Circuit details
  # @param [Hash] opts the optional parameters
  # @return [VirtualCircuit]
  describe 'update_virtual_circuit test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

end