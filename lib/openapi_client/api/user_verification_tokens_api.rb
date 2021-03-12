=begin
#Metal API

#This is the API for Equinix Metal Product. Interact with your devices, user account, and projects.

The version of the OpenAPI document: 1.0.0
Contact: support@equinixmetal.com
Generated by: https://openapi-generator.tech
OpenAPI Generator version: 5.1.0-SNAPSHOT

=end

require 'cgi'

module OpenapiClient
  class UserVerificationTokensApi
    attr_accessor :api_client

    def initialize(api_client = ApiClient.default)
      @api_client = api_client
    end
    # Verify a user using an email verification token
    # Consumes an email verification token and verifies the user associated with it.
    # @param token [String] User verification token
    # @param [Hash] opts the optional parameters
    # @return [nil]
    def consume_verification_request(token, opts = {})
      consume_verification_request_with_http_info(token, opts)
      nil
    end

    # Verify a user using an email verification token
    # Consumes an email verification token and verifies the user associated with it.
    # @param token [String] User verification token
    # @param [Hash] opts the optional parameters
    # @return [Array<(nil, Integer, Hash)>] nil, response status code and response headers
    def consume_verification_request_with_http_info(token, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: UserVerificationTokensApi.consume_verification_request ...'
      end
      # verify the required parameter 'token' is set
      if @api_client.config.client_side_validation && token.nil?
        fail ArgumentError, "Missing the required parameter 'token' when calling UserVerificationTokensApi.consume_verification_request"
      end
      # resource path
      local_var_path = '/verify-email'

      # query parameters
      query_params = opts[:query_params] || {}
      query_params[:'token'] = token

      # header parameters
      header_params = opts[:header_params] || {}

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:debug_body]

      # return_type
      return_type = opts[:debug_return_type]

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"UserVerificationTokensApi.consume_verification_request",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:PUT, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: UserVerificationTokensApi#consume_verification_request\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Create an email verification request
    # Creates an email verification request
    # @param login [String] Email for verification request
    # @param [Hash] opts the optional parameters
    # @return [nil]
    def create_validation_request(login, opts = {})
      create_validation_request_with_http_info(login, opts)
      nil
    end

    # Create an email verification request
    # Creates an email verification request
    # @param login [String] Email for verification request
    # @param [Hash] opts the optional parameters
    # @return [Array<(nil, Integer, Hash)>] nil, response status code and response headers
    def create_validation_request_with_http_info(login, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: UserVerificationTokensApi.create_validation_request ...'
      end
      # verify the required parameter 'login' is set
      if @api_client.config.client_side_validation && login.nil?
        fail ArgumentError, "Missing the required parameter 'login' when calling UserVerificationTokensApi.create_validation_request"
      end
      # resource path
      local_var_path = '/verify-email'

      # query parameters
      query_params = opts[:query_params] || {}
      query_params[:'login'] = login

      # header parameters
      header_params = opts[:header_params] || {}

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:debug_body]

      # return_type
      return_type = opts[:debug_return_type]

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"UserVerificationTokensApi.create_validation_request",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: UserVerificationTokensApi#create_validation_request\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
  end
end