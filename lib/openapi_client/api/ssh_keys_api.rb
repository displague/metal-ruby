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
  class SSHKeysApi
    attr_accessor :api_client

    def initialize(api_client = ApiClient.default)
      @api_client = api_client
    end
    # Create a ssh key for the given project
    # Creates a ssh key.
    # @param id [String] Project UUID
    # @param ssh_key [SSHKeyInput] ssh key to create
    # @param [Hash] opts the optional parameters
    # @return [SSHKey]
    def create_project_ssh_key(id, ssh_key, opts = {})
      data, _status_code, _headers = create_project_ssh_key_with_http_info(id, ssh_key, opts)
      data
    end

    # Create a ssh key for the given project
    # Creates a ssh key.
    # @param id [String] Project UUID
    # @param ssh_key [SSHKeyInput] ssh key to create
    # @param [Hash] opts the optional parameters
    # @return [Array<(SSHKey, Integer, Hash)>] SSHKey data, response status code and response headers
    def create_project_ssh_key_with_http_info(id, ssh_key, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: SSHKeysApi.create_project_ssh_key ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling SSHKeysApi.create_project_ssh_key"
      end
      # verify the required parameter 'ssh_key' is set
      if @api_client.config.client_side_validation && ssh_key.nil?
        fail ArgumentError, "Missing the required parameter 'ssh_key' when calling SSHKeysApi.create_project_ssh_key"
      end
      # resource path
      local_var_path = '/projects/{id}/ssh-keys'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

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
      post_body = opts[:debug_body] || @api_client.object_to_http_body(ssh_key)

      # return_type
      return_type = opts[:debug_return_type] || 'SSHKey'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"SSHKeysApi.create_project_ssh_key",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: SSHKeysApi#create_project_ssh_key\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Create a ssh key for the current user
    # Creates a ssh key.
    # @param ssh_key [SSHKeyInput] ssh key to create
    # @param [Hash] opts the optional parameters
    # @return [SSHKey]
    def create_ssh_key(ssh_key, opts = {})
      data, _status_code, _headers = create_ssh_key_with_http_info(ssh_key, opts)
      data
    end

    # Create a ssh key for the current user
    # Creates a ssh key.
    # @param ssh_key [SSHKeyInput] ssh key to create
    # @param [Hash] opts the optional parameters
    # @return [Array<(SSHKey, Integer, Hash)>] SSHKey data, response status code and response headers
    def create_ssh_key_with_http_info(ssh_key, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: SSHKeysApi.create_ssh_key ...'
      end
      # verify the required parameter 'ssh_key' is set
      if @api_client.config.client_side_validation && ssh_key.nil?
        fail ArgumentError, "Missing the required parameter 'ssh_key' when calling SSHKeysApi.create_ssh_key"
      end
      # resource path
      local_var_path = '/ssh-keys'

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
      post_body = opts[:debug_body] || @api_client.object_to_http_body(ssh_key)

      # return_type
      return_type = opts[:debug_return_type] || 'SSHKey'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"SSHKeysApi.create_ssh_key",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: SSHKeysApi#create_ssh_key\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Delete the ssh key
    # Deletes the ssh key.
    # @param id [String] ssh key UUID
    # @param [Hash] opts the optional parameters
    # @return [nil]
    def delete_ssh_key(id, opts = {})
      delete_ssh_key_with_http_info(id, opts)
      nil
    end

    # Delete the ssh key
    # Deletes the ssh key.
    # @param id [String] ssh key UUID
    # @param [Hash] opts the optional parameters
    # @return [Array<(nil, Integer, Hash)>] nil, response status code and response headers
    def delete_ssh_key_with_http_info(id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: SSHKeysApi.delete_ssh_key ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling SSHKeysApi.delete_ssh_key"
      end
      # resource path
      local_var_path = '/ssh-keys/{id}'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

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
        :operation => :"SSHKeysApi.delete_ssh_key",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:DELETE, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: SSHKeysApi#delete_ssh_key\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Retrieve a device's ssh keys
    # Returns a collection of the device's ssh keys.
    # @param id [String] Project UUID
    # @param [Hash] opts the optional parameters
    # @option opts [String] :search_string Search by key, label, or fingerprint
    # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    # @return [SSHKeyList]
    def find_device_ssh_keys(id, opts = {})
      data, _status_code, _headers = find_device_ssh_keys_with_http_info(id, opts)
      data
    end

    # Retrieve a device&#39;s ssh keys
    # Returns a collection of the device&#39;s ssh keys.
    # @param id [String] Project UUID
    # @param [Hash] opts the optional parameters
    # @option opts [String] :search_string Search by key, label, or fingerprint
    # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    # @return [Array<(SSHKeyList, Integer, Hash)>] SSHKeyList data, response status code and response headers
    def find_device_ssh_keys_with_http_info(id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: SSHKeysApi.find_device_ssh_keys ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling SSHKeysApi.find_device_ssh_keys"
      end
      # resource path
      local_var_path = '/devices/{id}/ssh-keys'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

      # query parameters
      query_params = opts[:query_params] || {}
      query_params[:'Search string'] = opts[:'search_string'] if !opts[:'search_string'].nil?
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
      return_type = opts[:debug_return_type] || 'SSHKeyList'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"SSHKeysApi.find_device_ssh_keys",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:GET, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: SSHKeysApi#find_device_ssh_keys\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Retrieve a project's ssh keys
    # Returns a collection of the project's ssh keys.
    # @param id [String] Project UUID
    # @param [Hash] opts the optional parameters
    # @option opts [String] :search_string Search by key, label, or fingerprint
    # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    # @return [SSHKeyList]
    def find_project_ssh_keys(id, opts = {})
      data, _status_code, _headers = find_project_ssh_keys_with_http_info(id, opts)
      data
    end

    # Retrieve a project&#39;s ssh keys
    # Returns a collection of the project&#39;s ssh keys.
    # @param id [String] Project UUID
    # @param [Hash] opts the optional parameters
    # @option opts [String] :search_string Search by key, label, or fingerprint
    # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    # @return [Array<(SSHKeyList, Integer, Hash)>] SSHKeyList data, response status code and response headers
    def find_project_ssh_keys_with_http_info(id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: SSHKeysApi.find_project_ssh_keys ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling SSHKeysApi.find_project_ssh_keys"
      end
      # resource path
      local_var_path = '/projects/{id}/ssh-keys'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

      # query parameters
      query_params = opts[:query_params] || {}
      query_params[:'Search string'] = opts[:'search_string'] if !opts[:'search_string'].nil?
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
      return_type = opts[:debug_return_type] || 'SSHKeyList'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"SSHKeysApi.find_project_ssh_keys",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:GET, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: SSHKeysApi#find_project_ssh_keys\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Retrieve a ssh key
    # Returns a single ssh key if the user has access
    # @param id [String] SSH Key UUID
    # @param [Hash] opts the optional parameters
    # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    # @return [SSHKey]
    def find_ssh_key_by_id(id, opts = {})
      data, _status_code, _headers = find_ssh_key_by_id_with_http_info(id, opts)
      data
    end

    # Retrieve a ssh key
    # Returns a single ssh key if the user has access
    # @param id [String] SSH Key UUID
    # @param [Hash] opts the optional parameters
    # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    # @return [Array<(SSHKey, Integer, Hash)>] SSHKey data, response status code and response headers
    def find_ssh_key_by_id_with_http_info(id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: SSHKeysApi.find_ssh_key_by_id ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling SSHKeysApi.find_ssh_key_by_id"
      end
      # resource path
      local_var_path = '/ssh-keys/{id}'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

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
      return_type = opts[:debug_return_type] || 'SSHKey'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"SSHKeysApi.find_ssh_key_by_id",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:GET, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: SSHKeysApi#find_ssh_key_by_id\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Retrieve all ssh keys
    # Returns a collection of the user’s ssh keys.
    # @param [Hash] opts the optional parameters
    # @option opts [String] :search_string Search by key, label, or fingerprint
    # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    # @return [SSHKeyList]
    def find_ssh_keys(opts = {})
      data, _status_code, _headers = find_ssh_keys_with_http_info(opts)
      data
    end

    # Retrieve all ssh keys
    # Returns a collection of the user’s ssh keys.
    # @param [Hash] opts the optional parameters
    # @option opts [String] :search_string Search by key, label, or fingerprint
    # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    # @return [Array<(SSHKeyList, Integer, Hash)>] SSHKeyList data, response status code and response headers
    def find_ssh_keys_with_http_info(opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: SSHKeysApi.find_ssh_keys ...'
      end
      # resource path
      local_var_path = '/ssh-keys'

      # query parameters
      query_params = opts[:query_params] || {}
      query_params[:'Search string'] = opts[:'search_string'] if !opts[:'search_string'].nil?
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
      return_type = opts[:debug_return_type] || 'SSHKeyList'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"SSHKeysApi.find_ssh_keys",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:GET, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: SSHKeysApi#find_ssh_keys\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Update the ssh key
    # Updates the ssh key.
    # @param id [String] SSH Key UUID
    # @param ssh_key [SSHKeyInput] ssh key to update
    # @param [Hash] opts the optional parameters
    # @return [SSHKey]
    def update_ssh_key(id, ssh_key, opts = {})
      data, _status_code, _headers = update_ssh_key_with_http_info(id, ssh_key, opts)
      data
    end

    # Update the ssh key
    # Updates the ssh key.
    # @param id [String] SSH Key UUID
    # @param ssh_key [SSHKeyInput] ssh key to update
    # @param [Hash] opts the optional parameters
    # @return [Array<(SSHKey, Integer, Hash)>] SSHKey data, response status code and response headers
    def update_ssh_key_with_http_info(id, ssh_key, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: SSHKeysApi.update_ssh_key ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling SSHKeysApi.update_ssh_key"
      end
      # verify the required parameter 'ssh_key' is set
      if @api_client.config.client_side_validation && ssh_key.nil?
        fail ArgumentError, "Missing the required parameter 'ssh_key' when calling SSHKeysApi.update_ssh_key"
      end
      # resource path
      local_var_path = '/ssh-keys/{id}'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

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
      post_body = opts[:debug_body] || @api_client.object_to_http_body(ssh_key)

      # return_type
      return_type = opts[:debug_return_type] || 'SSHKey'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"SSHKeysApi.update_ssh_key",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:PUT, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: SSHKeysApi#update_ssh_key\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
  end
end