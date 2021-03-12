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

# Unit tests for OpenapiClient::PasswordResetTokensApi
# Automatically generated by openapi-generator (https://openapi-generator.tech)
# Please update as you see appropriate
describe 'PasswordResetTokensApi' do
  before do
    # run before each test
    @api_instance = OpenapiClient::PasswordResetTokensApi.new
  end

  after do
    # run after each test
  end

  describe 'test an instance of PasswordResetTokensApi' do
    it 'should create an instance of PasswordResetTokensApi' do
      expect(@api_instance).to be_instance_of(OpenapiClient::PasswordResetTokensApi)
    end
  end

  # unit tests for create_password_reset_token
  # Create a password reset token
  # Creates a password reset token
  # @param email Email of user to create password reset token
  # @param [Hash] opts the optional parameters
  # @return [nil]
  describe 'create_password_reset_token test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for reset_password
  # Reset current user password
  # Resets current user password.
  # @param [Hash] opts the optional parameters
  # @return [NewPassword]
  describe 'reset_password test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

end