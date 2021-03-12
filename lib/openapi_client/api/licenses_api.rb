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
  class LicensesApi
    attr_accessor :api_client

    def initialize(api_client = ApiClient.default)
      @api_client = api_client
    end
    # Create a License
    # Creates a new license for the given project
    # @param id [String] Project UUID
    # @param license [LicenseCreateInput] License to create
    # @param [Hash] opts the optional parameters
    # @return [License]
    def create_license(id, license, opts = {})
      data, _status_code, _headers = create_license_with_http_info(id, license, opts)
      data
    end

    # Create a License
    # Creates a new license for the given project
    # @param id [String] Project UUID
    # @param license [LicenseCreateInput] License to create
    # @param [Hash] opts the optional parameters
    # @return [Array<(License, Integer, Hash)>] License data, response status code and response headers
    def create_license_with_http_info(id, license, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: LicensesApi.create_license ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling LicensesApi.create_license"
      end
      # verify the required parameter 'license' is set
      if @api_client.config.client_side_validation && license.nil?
        fail ArgumentError, "Missing the required parameter 'license' when calling LicensesApi.create_license"
      end
      # resource path
      local_var_path = '/projects/{id}/licenses'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

      # query parameters
      query_params = opts[:query_params] || {}

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])
      # HTTP header 'Content-Type'
      header_params['Content-Type'] = @api_client.select_header_content_type(['application/json'])

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:debug_body] || @api_client.object_to_http_body(license)

      # return_type
      return_type = opts[:debug_return_type] || 'License'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"LicensesApi.create_license",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: LicensesApi#create_license\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Delete the license
    # Deletes a license.
    # @param id [String] License UUID
    # @param [Hash] opts the optional parameters
    # @return [nil]
    def delete_license(id, opts = {})
      delete_license_with_http_info(id, opts)
      nil
    end

    # Delete the license
    # Deletes a license.
    # @param id [String] License UUID
    # @param [Hash] opts the optional parameters
    # @return [Array<(nil, Integer, Hash)>] nil, response status code and response headers
    def delete_license_with_http_info(id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: LicensesApi.delete_license ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling LicensesApi.delete_license"
      end
      # resource path
      local_var_path = '/licenses/{id}'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

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
        :operation => :"LicensesApi.delete_license",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:DELETE, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: LicensesApi#delete_license\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Retrieve a license
    # Returns a license
    # @param id [String] License UUID
    # @param [Hash] opts the optional parameters
    # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    # @return [License]
    def find_license_by_id(id, opts = {})
      data, _status_code, _headers = find_license_by_id_with_http_info(id, opts)
      data
    end

    # Retrieve a license
    # Returns a license
    # @param id [String] License UUID
    # @param [Hash] opts the optional parameters
    # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    # @return [Array<(License, Integer, Hash)>] License data, response status code and response headers
    def find_license_by_id_with_http_info(id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: LicensesApi.find_license_by_id ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling LicensesApi.find_license_by_id"
      end
      # resource path
      local_var_path = '/licenses/{id}'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

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
      return_type = opts[:debug_return_type] || 'License'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"LicensesApi.find_license_by_id",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:GET, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: LicensesApi#find_license_by_id\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Retrieve all licenses
    # Provides a collection of licenses for a given project.
    # @param id [String] Project UUID
    # @param [Hash] opts the optional parameters
    # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    # @option opts [Integer] :page Page to return (default to 1)
    # @option opts [Integer] :per_page Items returned per page (default to 10)
    # @return [LicenseList]
    def find_project_licenses(id, opts = {})
      data, _status_code, _headers = find_project_licenses_with_http_info(id, opts)
      data
    end

    # Retrieve all licenses
    # Provides a collection of licenses for a given project.
    # @param id [String] Project UUID
    # @param [Hash] opts the optional parameters
    # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    # @option opts [Integer] :page Page to return
    # @option opts [Integer] :per_page Items returned per page
    # @return [Array<(LicenseList, Integer, Hash)>] LicenseList data, response status code and response headers
    def find_project_licenses_with_http_info(id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: LicensesApi.find_project_licenses ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling LicensesApi.find_project_licenses"
      end
      if @api_client.config.client_side_validation && !opts[:'page'].nil? && opts[:'page'] > 100000
        fail ArgumentError, 'invalid value for "opts[:"page"]" when calling LicensesApi.find_project_licenses, must be smaller than or equal to 100000.'
      end

      if @api_client.config.client_side_validation && !opts[:'page'].nil? && opts[:'page'] < 1
        fail ArgumentError, 'invalid value for "opts[:"page"]" when calling LicensesApi.find_project_licenses, must be greater than or equal to 1.'
      end

      if @api_client.config.client_side_validation && !opts[:'per_page'].nil? && opts[:'per_page'] > 1000
        fail ArgumentError, 'invalid value for "opts[:"per_page"]" when calling LicensesApi.find_project_licenses, must be smaller than or equal to 1000.'
      end

      if @api_client.config.client_side_validation && !opts[:'per_page'].nil? && opts[:'per_page'] < 1
        fail ArgumentError, 'invalid value for "opts[:"per_page"]" when calling LicensesApi.find_project_licenses, must be greater than or equal to 1.'
      end

      # resource path
      local_var_path = '/projects/{id}/licenses'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

      # query parameters
      query_params = opts[:query_params] || {}
      query_params[:'include'] = @api_client.build_collection_param(opts[:'include'], :csv) if !opts[:'include'].nil?
      query_params[:'exclude'] = @api_client.build_collection_param(opts[:'exclude'], :csv) if !opts[:'exclude'].nil?
      query_params[:'page'] = opts[:'page'] if !opts[:'page'].nil?
      query_params[:'per_page'] = opts[:'per_page'] if !opts[:'per_page'].nil?

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:debug_body]

      # return_type
      return_type = opts[:debug_return_type] || 'LicenseList'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"LicensesApi.find_project_licenses",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:GET, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: LicensesApi#find_project_licenses\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Update the license
    # Updates the license.
    # @param id [String] License UUID
    # @param license [LicenseUpdateInput] License to update
    # @param [Hash] opts the optional parameters
    # @return [License]
    def update_license(id, license, opts = {})
      data, _status_code, _headers = update_license_with_http_info(id, license, opts)
      data
    end

    # Update the license
    # Updates the license.
    # @param id [String] License UUID
    # @param license [LicenseUpdateInput] License to update
    # @param [Hash] opts the optional parameters
    # @return [Array<(License, Integer, Hash)>] License data, response status code and response headers
    def update_license_with_http_info(id, license, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: LicensesApi.update_license ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling LicensesApi.update_license"
      end
      # verify the required parameter 'license' is set
      if @api_client.config.client_side_validation && license.nil?
        fail ArgumentError, "Missing the required parameter 'license' when calling LicensesApi.update_license"
      end
      # resource path
      local_var_path = '/licenses/{id}'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

      # query parameters
      query_params = opts[:query_params] || {}

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])
      # HTTP header 'Content-Type'
      header_params['Content-Type'] = @api_client.select_header_content_type(['application/json'])

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:debug_body] || @api_client.object_to_http_body(license)

      # return_type
      return_type = opts[:debug_return_type] || 'License'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"LicensesApi.update_license",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:PUT, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: LicensesApi#update_license\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
  end
end
