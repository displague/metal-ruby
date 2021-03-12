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

# Unit tests for OpenapiClient::OperatingSystemsApi
# Automatically generated by openapi-generator (https://openapi-generator.tech)
# Please update as you see appropriate
describe 'OperatingSystemsApi' do
  before do
    # run before each test
    @api_instance = OpenapiClient::OperatingSystemsApi.new
  end

  after do
    # run after each test
  end

  describe 'test an instance of OperatingSystemsApi' do
    it 'should create an instance of OperatingSystemsApi' do
      expect(@api_instance).to be_instance_of(OpenapiClient::OperatingSystemsApi)
    end
  end

  # unit tests for find_operating_systems
  # Retrieve all operating systems
  # Provides a listing of available operating systems to provision your new device with.
  # @param [Hash] opts the optional parameters
  # @return [Array<OperatingSystem>]
  describe 'find_operating_systems test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for find_operating_systems_by_organization
  # Retrieve all operating systems visible by the organization
  # Returns a listing of available operating systems for the given organization
  # @param id Organization UUID
  # @param [Hash] opts the optional parameters
  # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  # @return [Array<OperatingSystem>]
  describe 'find_operating_systems_by_organization test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

end
