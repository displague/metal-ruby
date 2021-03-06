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
  class IPAddressesApi
    attr_accessor :api_client

    def initialize(api_client = ApiClient.default)
      @api_client = api_client
    end
    # Create a ip assignment
    # Creates an ip assignment for a device.
    # @param id [String] Device UUID
    # @param ip_assignment [IPAssignmentInput] IPAssignment to create
    # @param [Hash] opts the optional parameters
    # @return [IPAssignment]
    def create_ip_assignment(id, ip_assignment, opts = {})
      data, _status_code, _headers = create_ip_assignment_with_http_info(id, ip_assignment, opts)
      data
    end

    # Create a ip assignment
    # Creates an ip assignment for a device.
    # @param id [String] Device UUID
    # @param ip_assignment [IPAssignmentInput] IPAssignment to create
    # @param [Hash] opts the optional parameters
    # @return [Array<(IPAssignment, Integer, Hash)>] IPAssignment data, response status code and response headers
    def create_ip_assignment_with_http_info(id, ip_assignment, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: IPAddressesApi.create_ip_assignment ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling IPAddressesApi.create_ip_assignment"
      end
      # verify the required parameter 'ip_assignment' is set
      if @api_client.config.client_side_validation && ip_assignment.nil?
        fail ArgumentError, "Missing the required parameter 'ip_assignment' when calling IPAddressesApi.create_ip_assignment"
      end
      # resource path
      local_var_path = '/devices/{id}/ips'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

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
      post_body = opts[:debug_body] || @api_client.object_to_http_body(ip_assignment)

      # return_type
      return_type = opts[:debug_return_type] || 'IPAssignment'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"IPAddressesApi.create_ip_assignment",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: IPAddressesApi#create_ip_assignment\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Unassign an ip address
    # Note! This call can be used to un-assign an IP assignment or delete an IP reservation. Un-assign an IP address record. Use the assignment UUID you get after attaching the IP. This will remove the relationship between an IP and the device and will make the IP address available to be assigned to another device. Delete and IP reservation. Use the reservation UUID you get after adding the IP to the project. This will permanently delete the IP block reservation from the project.
    # @param id [String] IP Address UUID
    # @param [Hash] opts the optional parameters
    # @return [nil]
    def delete_ip_address(id, opts = {})
      delete_ip_address_with_http_info(id, opts)
      nil
    end

    # Unassign an ip address
    # Note! This call can be used to un-assign an IP assignment or delete an IP reservation. Un-assign an IP address record. Use the assignment UUID you get after attaching the IP. This will remove the relationship between an IP and the device and will make the IP address available to be assigned to another device. Delete and IP reservation. Use the reservation UUID you get after adding the IP to the project. This will permanently delete the IP block reservation from the project.
    # @param id [String] IP Address UUID
    # @param [Hash] opts the optional parameters
    # @return [Array<(nil, Integer, Hash)>] nil, response status code and response headers
    def delete_ip_address_with_http_info(id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: IPAddressesApi.delete_ip_address ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling IPAddressesApi.delete_ip_address"
      end
      # resource path
      local_var_path = '/ips/{id}'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

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
        :operation => :"IPAddressesApi.delete_ip_address",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:DELETE, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: IPAddressesApi#delete_ip_address\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Retrieve an ip address
    # Returns a single ip address if the user has access.
    # @param id [String] IP Address UUID
    # @param [Hash] opts the optional parameters
    # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    # @return [IPAssignment]
    def find_ip_address_by_id(id, opts = {})
      data, _status_code, _headers = find_ip_address_by_id_with_http_info(id, opts)
      data
    end

    # Retrieve an ip address
    # Returns a single ip address if the user has access.
    # @param id [String] IP Address UUID
    # @param [Hash] opts the optional parameters
    # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    # @return [Array<(IPAssignment, Integer, Hash)>] IPAssignment data, response status code and response headers
    def find_ip_address_by_id_with_http_info(id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: IPAddressesApi.find_ip_address_by_id ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling IPAddressesApi.find_ip_address_by_id"
      end
      # resource path
      local_var_path = '/ips/{id}'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

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
      return_type = opts[:debug_return_type] || 'IPAssignment'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"IPAddressesApi.find_ip_address_by_id",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:GET, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: IPAddressesApi#find_ip_address_by_id\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Retrieve the custom metadata of an IP Reservation or IP Assignment
    # Provides the custom metadata stored for this IP Reservation or IP Assignment in json format
    # @param id [String] Ip Reservation UUID
    # @param [Hash] opts the optional parameters
    # @return [nil]
    def find_ip_address_customdata(id, opts = {})
      find_ip_address_customdata_with_http_info(id, opts)
      nil
    end

    # Retrieve the custom metadata of an IP Reservation or IP Assignment
    # Provides the custom metadata stored for this IP Reservation or IP Assignment in json format
    # @param id [String] Ip Reservation UUID
    # @param [Hash] opts the optional parameters
    # @return [Array<(nil, Integer, Hash)>] nil, response status code and response headers
    def find_ip_address_customdata_with_http_info(id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: IPAddressesApi.find_ip_address_customdata ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling IPAddressesApi.find_ip_address_customdata"
      end
      # resource path
      local_var_path = '/ips/{id}/customdata'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

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
        :operation => :"IPAddressesApi.find_ip_address_customdata",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:GET, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: IPAddressesApi#find_ip_address_customdata\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Retrieve all ip assignments
    # Returns all ip assignments for a device.
    # @param id [String] Device UUID
    # @param [Hash] opts the optional parameters
    # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    # @return [IPAssignmentList]
    def find_ip_assignments(id, opts = {})
      data, _status_code, _headers = find_ip_assignments_with_http_info(id, opts)
      data
    end

    # Retrieve all ip assignments
    # Returns all ip assignments for a device.
    # @param id [String] Device UUID
    # @param [Hash] opts the optional parameters
    # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    # @return [Array<(IPAssignmentList, Integer, Hash)>] IPAssignmentList data, response status code and response headers
    def find_ip_assignments_with_http_info(id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: IPAddressesApi.find_ip_assignments ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling IPAddressesApi.find_ip_assignments"
      end
      # resource path
      local_var_path = '/devices/{id}/ips'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

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
      return_type = opts[:debug_return_type] || 'IPAssignmentList'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"IPAddressesApi.find_ip_assignments",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:GET, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: IPAddressesApi#find_ip_assignments\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Retrieve all available subnets of a particular reservation
    # Provides a list of IP resevations for a single project.
    # @param id [String] IP Reservation UUID
    # @param cidr [String] Size of subnets in bits
    # @param [Hash] opts the optional parameters
    # @return [IPAvailabilitiesList]
    def find_ip_availabilities(id, cidr, opts = {})
      data, _status_code, _headers = find_ip_availabilities_with_http_info(id, cidr, opts)
      data
    end

    # Retrieve all available subnets of a particular reservation
    # Provides a list of IP resevations for a single project.
    # @param id [String] IP Reservation UUID
    # @param cidr [String] Size of subnets in bits
    # @param [Hash] opts the optional parameters
    # @return [Array<(IPAvailabilitiesList, Integer, Hash)>] IPAvailabilitiesList data, response status code and response headers
    def find_ip_availabilities_with_http_info(id, cidr, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: IPAddressesApi.find_ip_availabilities ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling IPAddressesApi.find_ip_availabilities"
      end
      # verify the required parameter 'cidr' is set
      if @api_client.config.client_side_validation && cidr.nil?
        fail ArgumentError, "Missing the required parameter 'cidr' when calling IPAddressesApi.find_ip_availabilities"
      end
      # verify enum value
      allowable_values = ["20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100", "101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "111", "112", "113", "114", "115", "116", "117", "118", "119", "120", "121", "122", "123", "124", "125", "126", "127", "128"]
      if @api_client.config.client_side_validation && !allowable_values.include?(cidr)
        fail ArgumentError, "invalid value for \"cidr\", must be one of #{allowable_values}"
      end
      # resource path
      local_var_path = '/ips/{id}/available'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

      # query parameters
      query_params = opts[:query_params] || {}
      query_params[:'cidr'] = cidr

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:debug_body]

      # return_type
      return_type = opts[:debug_return_type] || 'IPAvailabilitiesList'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"IPAddressesApi.find_ip_availabilities",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:GET, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: IPAddressesApi#find_ip_availabilities\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Retrieve all ip reservations
    # Provides a list of IP resevations for a single project.
    # @param id [String] Project UUID
    # @param [Hash] opts the optional parameters
    # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    # @return [IPReservationList]
    def find_ip_reservations(id, opts = {})
      data, _status_code, _headers = find_ip_reservations_with_http_info(id, opts)
      data
    end

    # Retrieve all ip reservations
    # Provides a list of IP resevations for a single project.
    # @param id [String] Project UUID
    # @param [Hash] opts the optional parameters
    # @option opts [Array<String>] :include Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    # @option opts [Array<String>] :exclude Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    # @return [Array<(IPReservationList, Integer, Hash)>] IPReservationList data, response status code and response headers
    def find_ip_reservations_with_http_info(id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: IPAddressesApi.find_ip_reservations ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling IPAddressesApi.find_ip_reservations"
      end
      # resource path
      local_var_path = '/projects/{id}/ips'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

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
      return_type = opts[:debug_return_type] || 'IPReservationList'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"IPAddressesApi.find_ip_reservations",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:GET, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: IPAddressesApi#find_ip_reservations\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Requesting IP reservations
    # Request more IP space for a project in order to have additional IP addresses to assign to devices.  If the request is within the max quota, an IP reservation will be created. If the project will exceed its IP quota, a request will be submitted for review, and will return an IP Reservation with a `state` of `pending`. You can automatically have the request fail with HTTP status 422 instead of triggering the review process by providing the `fail_on_approval_required` parameter set to `true` in the request.
    # @param id [String] Project UUID
    # @param ip_reservation_request [IPReservationRequestInput] IP Reservation Request to create
    # @param [Hash] opts the optional parameters
    # @return [IPReservation]
    def request_ip_reservation(id, ip_reservation_request, opts = {})
      data, _status_code, _headers = request_ip_reservation_with_http_info(id, ip_reservation_request, opts)
      data
    end

    # Requesting IP reservations
    # Request more IP space for a project in order to have additional IP addresses to assign to devices.  If the request is within the max quota, an IP reservation will be created. If the project will exceed its IP quota, a request will be submitted for review, and will return an IP Reservation with a &#x60;state&#x60; of &#x60;pending&#x60;. You can automatically have the request fail with HTTP status 422 instead of triggering the review process by providing the &#x60;fail_on_approval_required&#x60; parameter set to &#x60;true&#x60; in the request.
    # @param id [String] Project UUID
    # @param ip_reservation_request [IPReservationRequestInput] IP Reservation Request to create
    # @param [Hash] opts the optional parameters
    # @return [Array<(IPReservation, Integer, Hash)>] IPReservation data, response status code and response headers
    def request_ip_reservation_with_http_info(id, ip_reservation_request, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: IPAddressesApi.request_ip_reservation ...'
      end
      # verify the required parameter 'id' is set
      if @api_client.config.client_side_validation && id.nil?
        fail ArgumentError, "Missing the required parameter 'id' when calling IPAddressesApi.request_ip_reservation"
      end
      # verify the required parameter 'ip_reservation_request' is set
      if @api_client.config.client_side_validation && ip_reservation_request.nil?
        fail ArgumentError, "Missing the required parameter 'ip_reservation_request' when calling IPAddressesApi.request_ip_reservation"
      end
      # resource path
      local_var_path = '/projects/{id}/ips'.sub('{' + 'id' + '}', CGI.escape(id.to_s))

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
      post_body = opts[:debug_body] || @api_client.object_to_http_body(ip_reservation_request)

      # return_type
      return_type = opts[:debug_return_type] || 'IPReservation'

      # auth_names
      auth_names = opts[:debug_auth_names] || ['x_auth_token']

      new_options = opts.merge(
        :operation => :"IPAddressesApi.request_ip_reservation",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: IPAddressesApi#request_ip_reservation\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
  end
end
