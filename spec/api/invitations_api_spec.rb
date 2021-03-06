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

# Unit tests for OpenapiClient::InvitationsApi
# Automatically generated by openapi-generator (https://openapi-generator.tech)
# Please update as you see appropriate
describe 'InvitationsApi' do
  before do
    # run before each test
    @api_instance = OpenapiClient::InvitationsApi.new
  end

  after do
    # run after each test
  end

  describe 'test an instance of InvitationsApi' do
    it 'should create an instance of InvitationsApi' do
      expect(@api_instance).to be_instance_of(OpenapiClient::InvitationsApi)
    end
  end

  # unit tests for accept_invitation
  # Accept an invitation
  # Accept an invitation.
  # @param id Invitation UUID
  # @param [Hash] opts the optional parameters
  # @return [Membership]
  describe 'accept_invitation test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for create_organization_invitation
  # Create an invitation for an organization
  # In order to add a user to an organization, they must first be invited. To invite to several projects the parameter &#x60;projects_ids:[a,b,c]&#x60; can be used
  # @param id Organization UUID
  # @param invitation Invitation to create
  # @param [Hash] opts the optional parameters
  # @return [Invitation]
  describe 'create_organization_invitation test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for create_project_invitation
  # Create an invitation for a project
  # In order to add a user to a project, they must first be invited.
  # @param project_id Project UUID
  # @param invitation Invitation to create
  # @param [Hash] opts the optional parameters
  # @return [Invitation]
  describe 'create_project_invitation test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for decline_invitation
  # Decline an invitation
  # Decline an invitation.
  # @param id Invitation UUID
  # @param [Hash] opts the optional parameters
  # @return [nil]
  describe 'decline_invitation test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for find_invitation_by_id
  # View an invitation
  # Returns a single invitation. (It include the &#x60;invitable&#x60; to maintain backward compatibility but will be removed soon)
  # @param id Invitation UUID
  # @param [Hash] opts the optional parameters
  # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  # @return [Invitation]
  describe 'find_invitation_by_id test' do
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

  # unit tests for find_organization_invitations
  # Retrieve organization invitations
  # Returns all invitations in an organization.
  # @param id Organization UUID
  # @param [Hash] opts the optional parameters
  # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  # @option opts [Integer] :page Page to return
  # @option opts [Integer] :per_page Items returned per page
  # @return [InvitationList]
  describe 'find_organization_invitations test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for find_project_invitations
  # Retrieve project invitations
  # Returns all invitations in a project.
  # @param project_id Project UUID
  # @param [Hash] opts the optional parameters
  # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  # @option opts [Integer] :page Page to return
  # @option opts [Integer] :per_page Items returned per page
  # @return [InvitationList]
  describe 'find_project_invitations test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

end
