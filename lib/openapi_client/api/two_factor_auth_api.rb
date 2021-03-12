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
  class TwoFactorAuthApi
    attr_accessor :api_client

    def initialize(api_client = ApiClient.default)
      @api_client = api_client
    end
    # Disable two factor authentication
    # Disables two factor authentication.
    # @param [Hash] opts the optional parameters
    # @return [nil]
    def disable_tfa_app(opts = {})
      disable_tfa_app_with_http_info(opts)
      nil
    end

    # Disable two factor authentication
    # Disables two factor authentication.
    # @param [Hash] opts the optional parameters
    # @return [Array<(nil, Integer, Hash)>] nil, response status code and response headers
    def disable_tfa_app_with_http_info(opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: TwoFactorAuthApi.disable_tfa_app ...'
      end
      # resource path
      local_var_path = '/user/otp/app'

      # query parameters
      query_params = opts[:query_params] || {}

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
        :operation => :"TwoFactorAuthApi.disable_tfa_app",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:DELETE, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: TwoFactorAuthApi#disable_tfa_app\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Disable two factor authentication
    # Disables two factor authentication.
    # @param [Hash] opts the optional parameters
    # @return [nil]
    def disable_tfa_sms(opts = {})
      disable_tfa_sms_with_http_info(opts)
      nil
    end

    # Disable two factor authentication
    # Disables two factor authentication.
    # @param [Hash] opts the optional parameters
    # @return [Array<(nil, Integer, Hash)>] nil, response status code and response headers
    def disable_tfa_sms_with_http_info(opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: TwoFactorAuthApi.disable_tfa_sms ...'
      end
      # resource path
      local_var_path = '/user/otp/sms'

      # query parameters
      query_params = opts[:query_params] || {}

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
        :operation => :"TwoFactorAuthApi.disable_tfa_sms",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:DELETE, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: TwoFactorAuthApi#disable_tfa_sms\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Enable two factor auth using app
    # Enables two factor authentication using authenticator app.
    # @param [Hash] opts the optional parameters
    # @return [nil]
    def enable_tfa_app(opts = {})
      enable_tfa_app_with_http_info(opts)
      nil
    end

    # Enable two factor auth using app
    # Enables two factor authentication using authenticator app.
    # @param [Hash] opts the optional parameters
    # @return [Array<(nil, Integer, Hash)>] nil, response status code and response headers
    def enable_tfa_app_with_http_info(opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: TwoFactorAuthApi.enable_tfa_app ...'
      end
      # resource path
      local_var_path = '/user/otp/app'

      # query parameters
      query_params = opts[:query_params] || {}

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
        :operation => :"TwoFactorAuthApi.enable_tfa_app",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: TwoFactorAuthApi#enable_tfa_app\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Enable two factor auth using sms
    # Enables two factor authentication with sms.
    # @param [Hash] opts the optional parameters
    # @return [nil]
    def enable_tfa_sms(opts = {})
      enable_tfa_sms_with_http_info(opts)
      nil
    end

    # Enable two factor auth using sms
    # Enables two factor authentication with sms.
    # @param [Hash] opts the optional parameters
    # @return [Array<(nil, Integer, Hash)>] nil, response status code and response headers
    def enable_tfa_sms_with_http_info(opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: TwoFactorAuthApi.enable_tfa_sms ...'
      end
      # resource path
      local_var_path = '/user/otp/sms'

      # query parameters
      query_params = opts[:query_params] || {}

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
        :operation => :"TwoFactorAuthApi.enable_tfa_sms",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: TwoFactorAuthApi#enable_tfa_sms\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
  end
end