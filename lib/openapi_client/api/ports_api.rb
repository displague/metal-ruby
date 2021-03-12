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
  class PortsApi
    attr_accessor :api_client

    def initialize(api_client = ApiClient.default)
      @api_client = api_client
    end
    # Assign a native VLAN
    # Assigns a virtual network to this port as a \"native VLAN\"
    # @param id [String] Port UUID
    # @param vnid [String] UUID or VNID of the virtual network to assign
    # @param [Hash] opts the optional parameters
    # @return [Port]
    def assign_native_vlan(id, vnid, opts = {})
      data, _status_code, _headers = assign_native_vlan_with_http_info(id, vnid, opts)
      data
    end

    # Assign a native VLAN
    # Assigns a virtual network to this port as a \&quot;native VLAN\&quot;
    # @param id [String] Port UUID
    # @param vnid [String] UUID or VNID of the virtual network to assign
    # @param [Hash] opts the optional parameters
    # @return [Array<(Port, Integer, Hash)>] Port data, response status code and response headers
    def assign_native_vlan_with_http_info(id, vnid, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: PortsApi.assign_native_vlan ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling PortsApi.assign_native_vlan"
      end
      # verify the required parameter 'vnid' is set
      if @api_client.config.client_side_validation && vnid.nil?
        fail ArgumentError, "Missing the required parameter 'vnid' when calling PortsApi.assign_native_vlan"
      end
      # resource path
      local_var_path = '/ports/{id}/native-vlan'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

      # query parameters
      query_params = opts[:query_params] || {}
      query_params[:'vnid'] = vnid

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:debug_body]

      # return_type
      return_type = opts[:debug_return_type] || 'Port'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"PortsApi.assign_native_vlan",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: PortsApi#assign_native_vlan\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Assign a port to virtual network
    # Assign a port for a hardware to virtual network.
    # @param id [String] Port UUID
    # @param vnid [PortAssignInput] Virtual Network ID
    # @param [Hash] opts the optional parameters
    # @return [Port]
    def assign_port(id, vnid, opts = {})
      data, _status_code, _headers = assign_port_with_http_info(id, vnid, opts)
      data
    end

    # Assign a port to virtual network
    # Assign a port for a hardware to virtual network.
    # @param id [String] Port UUID
    # @param vnid [PortAssignInput] Virtual Network ID
    # @param [Hash] opts the optional parameters
    # @return [Array<(Port, Integer, Hash)>] Port data, response status code and response headers
    def assign_port_with_http_info(id, vnid, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: PortsApi.assign_port ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling PortsApi.assign_port"
      end
      # verify the required parameter 'vnid' is set
      if @api_client.config.client_side_validation && vnid.nil?
        fail ArgumentError, "Missing the required parameter 'vnid' when calling PortsApi.assign_port"
      end
      # resource path
      local_var_path = '/ports/{id}/assign'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

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
      post_body = opts[:debug_body] || @api_client.object_to_http_body(vnid)

      # return_type
      return_type = opts[:debug_return_type] || 'Port'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"PortsApi.assign_port",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: PortsApi#assign_port\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Enabling bonding
    # Enabling bonding for one or all ports
    # @param id [String] Port UUID
    # @param [Hash] opts the optional parameters
    # @option opts [Boolean] :bulk_enable enable both ports
    # @return [Port]
    def bond_port(id, opts = {})
      data, _status_code, _headers = bond_port_with_http_info(id, opts)
      data
    end

    # Enabling bonding
    # Enabling bonding for one or all ports
    # @param id [String] Port UUID
    # @param [Hash] opts the optional parameters
    # @option opts [Boolean] :bulk_enable enable both ports
    # @return [Array<(Port, Integer, Hash)>] Port data, response status code and response headers
    def bond_port_with_http_info(id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: PortsApi.bond_port ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling PortsApi.bond_port"
      end
      # resource path
      local_var_path = '/ports/{id}/bond'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

      # query parameters
      query_params = opts[:query_params] || {}
      query_params[:'bulk_enable'] = opts[:'bulk_enable'] if !opts[:'bulk_enable'].nil?

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:debug_body]

      # return_type
      return_type = opts[:debug_return_type] || 'Port'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"PortsApi.bond_port",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: PortsApi#bond_port\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Convert to Layer 2
    # Converts a bond port to Layer 2. IP assignments of the port will be removed.
    # @param id [String] Port UUID
    # @param [Hash] opts the optional parameters
    # @option opts [PortAssignInput] :vnid Virtual Network ID
    # @return [Port]
    def convert_layer2(id, opts = {})
      data, _status_code, _headers = convert_layer2_with_http_info(id, opts)
      data
    end

    # Convert to Layer 2
    # Converts a bond port to Layer 2. IP assignments of the port will be removed.
    # @param id [String] Port UUID
    # @param [Hash] opts the optional parameters
    # @option opts [PortAssignInput] :vnid Virtual Network ID
    # @return [Array<(Port, Integer, Hash)>] Port data, response status code and response headers
    def convert_layer2_with_http_info(id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: PortsApi.convert_layer2 ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling PortsApi.convert_layer2"
      end
      # resource path
      local_var_path = '/ports/{id}/convert/layer-2'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

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
      post_body = opts[:debug_body] || @api_client.object_to_http_body(opts[:'vnid'])

      # return_type
      return_type = opts[:debug_return_type] || 'Port'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"PortsApi.convert_layer2",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: PortsApi#convert_layer2\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Convert to Layer 3
    # Converts a bond port to Layer 3. VLANs must first be unassigned.
    # @param id [String] Port UUID
    # @param [Hash] opts the optional parameters
    # @option opts [PortConvertLayer3Input] :request_ips IPs to request
    # @return [Port]
    def convert_layer3(id, opts = {})
      data, _status_code, _headers = convert_layer3_with_http_info(id, opts)
      data
    end

    # Convert to Layer 3
    # Converts a bond port to Layer 3. VLANs must first be unassigned.
    # @param id [String] Port UUID
    # @param [Hash] opts the optional parameters
    # @option opts [PortConvertLayer3Input] :request_ips IPs to request
    # @return [Array<(Port, Integer, Hash)>] Port data, response status code and response headers
    def convert_layer3_with_http_info(id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: PortsApi.convert_layer3 ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling PortsApi.convert_layer3"
      end
      # resource path
      local_var_path = '/ports/{id}/convert/layer-3'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

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
      post_body = opts[:debug_body] || @api_client.object_to_http_body(opts[:'request_ips'])

      # return_type
      return_type = opts[:debug_return_type] || 'Port'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"PortsApi.convert_layer3",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: PortsApi#convert_layer3\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Remove native VLAN
    # Removes the native VLAN from this port
    # @param id [String] Port UUID
    # @param [Hash] opts the optional parameters
    # @return [Port]
    def delete_native_vlan(id, opts = {})
      data, _status_code, _headers = delete_native_vlan_with_http_info(id, opts)
      data
    end

    # Remove native VLAN
    # Removes the native VLAN from this port
    # @param id [String] Port UUID
    # @param [Hash] opts the optional parameters
    # @return [Array<(Port, Integer, Hash)>] Port data, response status code and response headers
    def delete_native_vlan_with_http_info(id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: PortsApi.delete_native_vlan ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling PortsApi.delete_native_vlan"
      end
      # resource path
      local_var_path = '/ports/{id}/native-vlan'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

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
      return_type = opts[:debug_return_type] || 'Port'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"PortsApi.delete_native_vlan",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:DELETE, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: PortsApi#delete_native_vlan\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Disabling bonding
    # Disabling bonding for one or all ports
    # @param id [String] Port UUID
    # @param [Hash] opts the optional parameters
    # @option opts [Boolean] :bulk_disable disable both ports
    # @return [Port]
    def disbond_port(id, opts = {})
      data, _status_code, _headers = disbond_port_with_http_info(id, opts)
      data
    end

    # Disabling bonding
    # Disabling bonding for one or all ports
    # @param id [String] Port UUID
    # @param [Hash] opts the optional parameters
    # @option opts [Boolean] :bulk_disable disable both ports
    # @return [Array<(Port, Integer, Hash)>] Port data, response status code and response headers
    def disbond_port_with_http_info(id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: PortsApi.disbond_port ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling PortsApi.disbond_port"
      end
      # resource path
      local_var_path = '/ports/{id}/disbond'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

      # query parameters
      query_params = opts[:query_params] || {}
      query_params[:'bulk_disable'] = opts[:'bulk_disable'] if !opts[:'bulk_disable'].nil?

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:debug_body]

      # return_type
      return_type = opts[:debug_return_type] || 'Port'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"PortsApi.disbond_port",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: PortsApi#disbond_port\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Retrieve a port
    # Returns a port
    # @param id [String] Port UUID
    # @param [Hash] opts the optional parameters
    # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    # @return [Port]
    def find_port_by_id(id, opts = {})
      data, _status_code, _headers = find_port_by_id_with_http_info(id, opts)
      data
    end

    # Retrieve a port
    # Returns a port
    # @param id [String] Port UUID
    # @param [Hash] opts the optional parameters
    # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    # @return [Array<(Port, Integer, Hash)>] Port data, response status code and response headers
    def find_port_by_id_with_http_info(id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: PortsApi.find_port_by_id ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling PortsApi.find_port_by_id"
      end
      # resource path
      local_var_path = '/ports/{id}'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

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
      return_type = opts[:debug_return_type] || 'Port'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"PortsApi.find_port_by_id",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:GET, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: PortsApi#find_port_by_id\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Unassign a port
    # Unassign a port for a hardware.
    # @param id [String] Port UUID
    # @param vnid [PortAssignInput] Virtual Network ID
    # @param [Hash] opts the optional parameters
    # @return [Port]
    def unassign_port(id, vnid, opts = {})
      data, _status_code, _headers = unassign_port_with_http_info(id, vnid, opts)
      data
    end

    # Unassign a port
    # Unassign a port for a hardware.
    # @param id [String] Port UUID
    # @param vnid [PortAssignInput] Virtual Network ID
    # @param [Hash] opts the optional parameters
    # @return [Array<(Port, Integer, Hash)>] Port data, response status code and response headers
    def unassign_port_with_http_info(id, vnid, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: PortsApi.unassign_port ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling PortsApi.unassign_port"
      end
      # verify the required parameter 'vnid' is set
      if @api_client.config.client_side_validation && vnid.nil?
        fail ArgumentError, "Missing the required parameter 'vnid' when calling PortsApi.unassign_port"
      end
      # resource path
      local_var_path = '/ports/{id}/unassign'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

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
      post_body = opts[:debug_body] || @api_client.object_to_http_body(vnid)

      # return_type
      return_type = opts[:debug_return_type] || 'Port'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"PortsApi.unassign_port",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: PortsApi#unassign_port\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
  end
end
