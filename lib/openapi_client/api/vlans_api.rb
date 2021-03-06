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
  class VLANsApi
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
        @api_client.config.logger.debug 'Calling API: VLANsApi.assign_native_vlan ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling VLANsApi.assign_native_vlan"
      end
      # verify the required parameter 'vnid' is set
      if @api_client.config.client_side_validation && vnid.nil?
        fail ArgumentError, "Missing the required parameter 'vnid' when calling VLANsApi.assign_native_vlan"
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
        :operation => :"VLANsApi.assign_native_vlan",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: VLANsApi#assign_native_vlan\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Create an internet gateway
    # Creates an internet gateway.
    # @param id [String] Virtual Network UUID
    # @param length [String] IP Reservation length
    # @param [Hash] opts the optional parameters
    # @return [InternetGateway]
    def create_internet_gateway(id, length, opts = {})
      data, _status_code, _headers = create_internet_gateway_with_http_info(id, length, opts)
      data
    end

    # Create an internet gateway
    # Creates an internet gateway.
    # @param id [String] Virtual Network UUID
    # @param length [String] IP Reservation length
    # @param [Hash] opts the optional parameters
    # @return [Array<(InternetGateway, Integer, Hash)>] InternetGateway data, response status code and response headers
    def create_internet_gateway_with_http_info(id, length, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: VLANsApi.create_internet_gateway ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling VLANsApi.create_internet_gateway"
      end
      # verify the required parameter 'length' is set
      if @api_client.config.client_side_validation && length.nil?
        fail ArgumentError, "Missing the required parameter 'length' when calling VLANsApi.create_internet_gateway"
      end
      # resource path
      local_var_path = '/virtual-networks/{id}/internet-gateways'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

      # query parameters
      query_params = opts[:query_params] || {}
      query_params[:'length'] = length

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:debug_body]

      # return_type
      return_type = opts[:debug_return_type] || 'InternetGateway'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"VLANsApi.create_internet_gateway",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: VLANsApi#create_internet_gateway\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Create an virtual network
    # Creates an virtual network.
    # @param id [String] Project UUID
    # @param virtual_network [VirtualNetworkCreateInput] Virtual Network to create
    # @param [Hash] opts the optional parameters
    # @return [VirtualNetwork]
    def create_virtual_network(id, virtual_network, opts = {})
      data, _status_code, _headers = create_virtual_network_with_http_info(id, virtual_network, opts)
      data
    end

    # Create an virtual network
    # Creates an virtual network.
    # @param id [String] Project UUID
    # @param virtual_network [VirtualNetworkCreateInput] Virtual Network to create
    # @param [Hash] opts the optional parameters
    # @return [Array<(VirtualNetwork, Integer, Hash)>] VirtualNetwork data, response status code and response headers
    def create_virtual_network_with_http_info(id, virtual_network, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: VLANsApi.create_virtual_network ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling VLANsApi.create_virtual_network"
      end
      # verify the required parameter 'virtual_network' is set
      if @api_client.config.client_side_validation && virtual_network.nil?
        fail ArgumentError, "Missing the required parameter 'virtual_network' when calling VLANsApi.create_virtual_network"
      end
      # resource path
      local_var_path = '/projects/{id}/virtual-networks'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

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
      post_body = opts[:debug_body] || @api_client.object_to_http_body(virtual_network)

      # return_type
      return_type = opts[:debug_return_type] || 'VirtualNetwork'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"VLANsApi.create_virtual_network",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: VLANsApi#create_virtual_network\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
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
        @api_client.config.logger.debug 'Calling API: VLANsApi.delete_native_vlan ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling VLANsApi.delete_native_vlan"
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
        :operation => :"VLANsApi.delete_native_vlan",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:DELETE, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: VLANsApi#delete_native_vlan\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Delete a virtual network
    # Deletes a virtual network.
    # @param id [String] Virtual Network UUID
    # @param [Hash] opts the optional parameters
    # @return [VirtualNetwork]
    def delete_virtual_network(id, opts = {})
      data, _status_code, _headers = delete_virtual_network_with_http_info(id, opts)
      data
    end

    # Delete a virtual network
    # Deletes a virtual network.
    # @param id [String] Virtual Network UUID
    # @param [Hash] opts the optional parameters
    # @return [Array<(VirtualNetwork, Integer, Hash)>] VirtualNetwork data, response status code and response headers
    def delete_virtual_network_with_http_info(id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: VLANsApi.delete_virtual_network ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling VLANsApi.delete_virtual_network"
      end
      # resource path
      local_var_path = '/virtual-networks/{id}'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

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
      return_type = opts[:debug_return_type] || 'VirtualNetwork'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"VLANsApi.delete_virtual_network",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:DELETE, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: VLANsApi#delete_virtual_network\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Retrieve all virtual networks
    # Provides a list of virtual networks for a single project.
    # @param id [String] Project UUID
    # @param [Hash] opts the optional parameters
    # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    # @return [VirtualNetworkList]
    def find_virtual_networks(id, opts = {})
      data, _status_code, _headers = find_virtual_networks_with_http_info(id, opts)
      data
    end

    # Retrieve all virtual networks
    # Provides a list of virtual networks for a single project.
    # @param id [String] Project UUID
    # @param [Hash] opts the optional parameters
    # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    # @return [Array<(VirtualNetworkList, Integer, Hash)>] VirtualNetworkList data, response status code and response headers
    def find_virtual_networks_with_http_info(id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: VLANsApi.find_virtual_networks ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling VLANsApi.find_virtual_networks"
      end
      # resource path
      local_var_path = '/projects/{id}/virtual-networks'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

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
      return_type = opts[:debug_return_type] || 'VirtualNetworkList'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"VLANsApi.find_virtual_networks",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:GET, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: VLANsApi#find_virtual_networks\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Get a virtual network
    # Get a virtual network.
    # @param id [String] Virtual Network UUID
    # @param [Hash] opts the optional parameters
    # @return [VirtualNetwork]
    def get_virtual_network(id, opts = {})
      data, _status_code, _headers = get_virtual_network_with_http_info(id, opts)
      data
    end

    # Get a virtual network
    # Get a virtual network.
    # @param id [String] Virtual Network UUID
    # @param [Hash] opts the optional parameters
    # @return [Array<(VirtualNetwork, Integer, Hash)>] VirtualNetwork data, response status code and response headers
    def get_virtual_network_with_http_info(id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: VLANsApi.get_virtual_network ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling VLANsApi.get_virtual_network"
      end
      # resource path
      local_var_path = '/virtual-networks/{id}'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

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
      return_type = opts[:debug_return_type] || 'VirtualNetwork'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"VLANsApi.get_virtual_network",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:GET, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: VLANsApi#get_virtual_network\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
  end
end
