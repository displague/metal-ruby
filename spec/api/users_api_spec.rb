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

# Unit tests for OpenapiClient::UsersApi
# Automatically generated by openapi-generator (https://openapi-generator.tech)
# Please update as you see appropriate
describe 'UsersApi' do
  before do
    # run before each test
    @api_instance = OpenapiClient::UsersApi.new
  end

  after do
    # run after each test
  end

  describe 'test an instance of UsersApi' do
    it 'should create an instance of UsersApi' do
      expect(@api_instance).to be_instance_of(OpenapiClient::UsersApi)
    end
  end

  # unit tests for find_current_user
  # Retrieve the current user
  # Returns the user object for the currently logged-in user.
  # @param [Hash] opts the optional parameters
  # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  # @return [User]
  describe 'find_current_user test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for find_invitations
  # Retrieve current user invitations
  # Returns all invitations in current user.
  # @param [Hash] opts the optional parameters
  # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  # @option opts [Integer] :page Page to return
  # @option opts [Integer] :per_page Items returned per page
  # @return [InvitationList]
  describe 'find_invitations test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for find_user_by_id
  # Retrieve a user
  # Returns a single user if the user has access
  # @param id User UUID
  # @param [Hash] opts the optional parameters
  # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  # @return [User]
  describe 'find_user_by_id test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for find_user_customdata
  # Retrieve the custom metadata of a user
  # Provides the custom metadata stored for this user in json format
  # @param id User UUID
  # @param [Hash] opts the optional parameters
  # @return [nil]
  describe 'find_user_customdata test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for find_users
  # Retrieve all users
  # Returns a list of users that the are accessible to the current user (all users in the current user???s projects, essentially).
  # @param [Hash] opts the optional parameters
  # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  # @option opts [Integer] :page Page to return
  # @option opts [Integer] :per_page Items returned per page
  # @return [UserList]
  describe 'find_users test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for update_current_user
  # Update the current user
  # Updates the currently logged-in user.
  # @param user User to update
  # @param [Hash] opts the optional parameters
  # @return [User]
  describe 'update_current_user test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

end
