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

# Unit tests for OpenapiClient::InternetGatewaysApi
# Automatically generated by openapi-generator (https://openapi-generator.tech)
# Please update as you see appropriate
describe 'InternetGatewaysApi' do
  before do
    # run before each test
    @api_instance = OpenapiClient::InternetGatewaysApi.new
  end

  after do
    # run after each test
  end

  describe 'test an instance of InternetGatewaysApi' do
    it 'should create an instance of InternetGatewaysApi' do
      expect(@api_instance).to be_instance_of(OpenapiClient::InternetGatewaysApi)
    end
  end

  # unit tests for create_internet_gateway
  # Create an internet gateway
  # Creates an internet gateway.
  # @param id Virtual Network UUID
  # @param length IP Reservation length
  # @param [Hash] opts the optional parameters
  # @return [InternetGateway]
  describe 'create_internet_gateway test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

end