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
  class OperatingSystemsApi
    attr_accessor :api_client

    def initialize(api_client = ApiClient.default)
      @api_client = api_client
    end
    # Retrieve all operating systems
    # Provides a listing of available operating systems to provision your new device with.
    # @param [Hash] opts the optional parameters
    # @return [Array<OperatingSystem>]
    def find_operating_systems(opts = {})
      data, _status_code, _headers = find_operating_systems_with_http_info(opts)
      data
    end

    # Retrieve all operating systems
    # Provides a listing of available operating systems to provision your new device with.
    # @param [Hash] opts the optional parameters
    # @return [Array<(Array<OperatingSystem>, Integer, Hash)>] Array<OperatingSystem> data, response status code and response headers
    def find_operating_systems_with_http_info(opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: OperatingSystemsApi.find_operating_systems ...'
      end
      # resource path
      local_var_path = '/operating-systems'

      # query parameters
      query_params = opts[:query_params] || {}

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:debug_body]

      # return_type
      return_type = opts[:debug_return_type] || 'Array<OperatingSystem>'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"OperatingSystemsApi.find_operating_systems",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:GET, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: OperatingSystemsApi#find_operating_systems\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Retrieve all operating systems visible by the organization
    # Returns a listing of available operating systems for the given organization
    # @param id [String] Organization UUID
    # @param [Hash] opts the optional parameters
    # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    # @return [Array<OperatingSystem>]
    def find_operating_systems_by_organization(id, opts = {})
      data, _status_code, _headers = find_operating_systems_by_organization_with_http_info(id, opts)
      data
    end

    # Retrieve all operating systems visible by the organization
    # Returns a listing of available operating systems for the given organization
    # @param id [String] Organization UUID
    # @param [Hash] opts the optional parameters
    # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    # @return [Array<(Array<OperatingSystem>, Integer, Hash)>] Array<OperatingSystem> data, response status code and response headers
    def find_operating_systems_by_organization_with_http_info(id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: OperatingSystemsApi.find_operating_systems_by_organization ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling OperatingSystemsApi.find_operating_systems_by_organization"
      end
      # resource path
      local_var_path = '/organizations/{id}/operating-systems'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

      # query parameters
      query_params = opts[:query_params] || {}
      query_params[:'include'] = @api_client.build_collection_param(opts[:'include'], :csv) if !opts[:'include'].nil?
      query_params[:'exclude'] = @api_client.build_collection_param(opts[:'exclude'], :csv) if !opts[:'exclude'].nil?

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:debug_body]

      # return_type
      return_type = opts[:debug_return_type] || 'Array<OperatingSystem>'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"OperatingSystemsApi.find_operating_systems_by_organization",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:GET, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: OperatingSystemsApi#find_operating_systems_by_organization\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
  end
end