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

# Unit tests for OpenapiClient::SpotMarketRequestApi
# Automatically generated by openapi-generator (https://openapi-generator.tech)
# Please update as you see appropriate
describe 'SpotMarketRequestApi' do
  before do
    # run before each test
    @api_instance = OpenapiClient::SpotMarketRequestApi.new
  end

  after do
    # run after each test
  end

  describe 'test an instance of SpotMarketRequestApi' do
    it 'should create an instance of SpotMarketRequestApi' do
      expect(@api_instance).to be_instance_of(OpenapiClient::SpotMarketRequestApi)
    end
  end

  # unit tests for create_spot_market_request
  # Create a spot market request
  # Creates a new spot market request.  Type-specific options (such as operating_system for baremetal devices) should be included in the main data structure alongside hostname and plan.  The features attribute allows you to optionally specify what features your server should have. For example, if you require a server with a TPM chip, you may specify &#x60;{ \&quot;features\&quot;: { \&quot;tpm\&quot;: \&quot;required\&quot; } }&#x60; (or &#x60;{ \&quot;features\&quot;: [\&quot;tpm\&quot;] }&#x60; in shorthand).  The request will fail if there are no available servers matching your criteria. Alternatively, if you do not require a certain feature, but would prefer to be assigned a server with that feature if there are any available, you may specify that feature with a preferred value (see the example request below).  The request will not fail if we have no servers with that feature in our inventory.
  # @param id Project UUID
  # @param spot_market_request Spot Market Request to create
  # @param [Hash] opts the optional parameters
  # @return [SpotMarketRequest]
  describe 'create_spot_market_request test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for delete_spot_market_request
  # Delete the spot market request
  # Deletes the spot market request.
  # @param id SpotMarketRequest UUID
  # @param [Hash] opts the optional parameters
  # @option opts [Boolean] :force_termination Terminate associated spot instances
  # @return [nil]
  describe 'delete_spot_market_request test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for find_spot_market_request_by_id
  # Retrieve a spot market request
  # Returns a single spot market request
  # @param id SpotMarketRequest UUID
  # @param [Hash] opts the optional parameters
  # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  # @return [SpotMarketRequest]
  describe 'find_spot_market_request_by_id test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for list_spot_market_requests
  # List spot market requests
  # View all spot market requests for a given project.
  # @param id Project UUID
  # @param [Hash] opts the optional parameters
  # @return [SpotMarketRequestList]
  describe 'list_spot_market_requests test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

end