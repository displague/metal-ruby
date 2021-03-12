=begin
#Metal API

#This is the API for Equinix Metal Product. Interact with your devices, user account, and projects.

The version of the OpenAPI document: 1.0.0
Contact: support@equinixmetal.com
Generated by: https://openapi-generator.tech
OpenAPI Generator version: 5.1.0-SNAPSHOT

=end

require 'date'
require 'time'

module OpenapiClient
  class InstancesBatchCreateInputBatches
    attr_accessor :plan

    attr_accessor :hostname

    attr_accessor :hostnames

    attr_accessor :description

    attr_accessor :billing_cycle

    attr_accessor :operating_system

    attr_accessor :always_pxe

    attr_accessor :userdata

    attr_accessor :locked

    attr_accessor :termination_time

    attr_accessor :tags

    attr_accessor :project_ssh_keys

    # The UUIDs of users whose SSH keys should be included on the provisioned device.
    attr_accessor :user_ssh_keys

    attr_accessor :features

    attr_accessor :customdata

    attr_accessor :ip_addresses

    # Attribute mapping from ruby-style variable name to JSON key.
    def self.attribute_map
      {
        :'plan' => :'plan',
        :'hostname' => :'hostname',
        :'hostnames' => :'hostnames',
        :'description' => :'description',
        :'billing_cycle' => :'billing_cycle',
        :'operating_system' => :'operating_system',
        :'always_pxe' => :'always_pxe',
        :'userdata' => :'userdata',
        :'locked' => :'locked',
        :'termination_time' => :'termination_time',
        :'tags' => :'tags',
        :'project_ssh_keys' => :'project_ssh_keys',
        :'user_ssh_keys' => :'user_ssh_keys',
        :'features' => :'features',
        :'customdata' => :'customdata',
        :'ip_addresses' => :'ip_addresses'
      }
    end

    # Returns all the JSON keys this model knows about
    def self.acceptable_attributes
      attribute_map.values
    end

    # Attribute type mapping.
    def self.openapi_types
      {
        :'plan' => :'String',
        :'hostname' => :'String',
        :'hostnames' => :'Array<String>',
        :'description' => :'String',
        :'billing_cycle' => :'String',
        :'operating_system' => :'String',
        :'always_pxe' => :'Boolean',
        :'userdata' => :'String',
        :'locked' => :'Boolean',
        :'termination_time' => :'Time',
        :'tags' => :'Array<String>',
        :'project_ssh_keys' => :'Array<String>',
        :'user_ssh_keys' => :'Array<String>',
        :'features' => :'Array<String>',
        :'customdata' => :'Object',
        :'ip_addresses' => :'Array<InstancesBatchCreateInputIpAddresses>'
      }
    end

    # List of attributes with nullable: true
    def self.openapi_nullable
      Set.new([
      ])
    end

    # Initializes the object
    # @param [Hash] attributes Model attributes in the form of hash
    def initialize(attributes = {})
      if (!attributes.is_a?(Hash))
        fail ArgumentError, "The input argument (attributes) must be a hash in `OpenapiClient::InstancesBatchCreateInputBatches` initialize method"
      end

      # check to see if the attribute exists and convert string to symbol for hash key
      attributes = attributes.each_with_object({}) { |(k, v), h|
        if (!self.class.attribute_map.key?(k.to_sym))
          fail ArgumentError, "`#{k}` is not a valid attribute in `OpenapiClient::InstancesBatchCreateInputBatches`. Please check the name to make sure it's valid. List of attributes: " + self.class.attribute_map.keys.inspect
        end
        h[k.to_sym] = v
      }

      if attributes.key?(:'plan')
        self.plan = attributes[:'plan']
      end

      if attributes.key?(:'hostname')
        self.hostname = attributes[:'hostname']
      end

      if attributes.key?(:'hostnames')
        if (value = attributes[:'hostnames']).is_a?(Array)
          self.hostnames = value
        end
      end

      if attributes.key?(:'description')
        self.description = attributes[:'description']
      end

      if attributes.key?(:'billing_cycle')
        self.billing_cycle = attributes[:'billing_cycle']
      end

      if attributes.key?(:'operating_system')
        self.operating_system = attributes[:'operating_system']
      end

      if attributes.key?(:'always_pxe')
        self.always_pxe = attributes[:'always_pxe']
      end

      if attributes.key?(:'userdata')
        self.userdata = attributes[:'userdata']
      end

      if attributes.key?(:'locked')
        self.locked = attributes[:'locked']
      end

      if attributes.key?(:'termination_time')
        self.termination_time = attributes[:'termination_time']
      end

      if attributes.key?(:'tags')
        if (value = attributes[:'tags']).is_a?(Array)
          self.tags = value
        end
      end

      if attributes.key?(:'project_ssh_keys')
        if (value = attributes[:'project_ssh_keys']).is_a?(Array)
          self.project_ssh_keys = value
        end
      end

      if attributes.key?(:'user_ssh_keys')
        if (value = attributes[:'user_ssh_keys']).is_a?(Array)
          self.user_ssh_keys = value
        end
      end

      if attributes.key?(:'features')
        if (value = attributes[:'features']).is_a?(Array)
          self.features = value
        end
      end

      if attributes.key?(:'customdata')
        self.customdata = attributes[:'customdata']
      end

      if attributes.key?(:'ip_addresses')
        if (value = attributes[:'ip_addresses']).is_a?(Array)
          self.ip_addresses = value
        end
      end
    end

    # Show invalid properties with the reasons. Usually used together with valid?
    # @return Array for valid properties with the reasons
    def list_invalid_properties
      invalid_properties = Array.new
      invalid_properties
    end

    # Check to see if the all the properties in the model are valid
    # @return true if the model is valid
    def valid?
      true
    end

    # Checks equality by comparing each attribute.
    # @param [Object] Object to be compared
    def ==(o)
      return true if self.equal?(o)
      self.class == o.class &&
          plan == o.plan &&
          hostname == o.hostname &&
          hostnames == o.hostnames &&
          description == o.description &&
          billing_cycle == o.billing_cycle &&
          operating_system == o.operating_system &&
          always_pxe == o.always_pxe &&
          userdata == o.userdata &&
          locked == o.locked &&
          termination_time == o.termination_time &&
          tags == o.tags &&
          project_ssh_keys == o.project_ssh_keys &&
          user_ssh_keys == o.user_ssh_keys &&
          features == o.features &&
          customdata == o.customdata &&
          ip_addresses == o.ip_addresses
    end

    # @see the `==` method
    # @param [Object] Object to be compared
    def eql?(o)
      self == o
    end

    # Calculates hash code according to all attributes.
    # @return [Integer] Hash code
    def hash
      [plan, hostname, hostnames, description, billing_cycle, operating_system, always_pxe, userdata, locked, termination_time, tags, project_ssh_keys, user_ssh_keys, features, customdata, ip_addresses].hash
    end

    # Builds the object from hash
    # @param [Hash] attributes Model attributes in the form of hash
    # @return [Object] Returns the model itself
    def self.build_from_hash(attributes)
      new.build_from_hash(attributes)
    end

    # Builds the object from hash
    # @param [Hash] attributes Model attributes in the form of hash
    # @return [Object] Returns the model itself
    def build_from_hash(attributes)
      return nil unless attributes.is_a?(Hash)
      self.class.openapi_types.each_pair do |key, type|
        if attributes[self.class.attribute_map[key]].nil? && self.class.openapi_nullable.include?(key)
          self.send("#{key}=", nil)
        elsif type =~ /\AArray<(.*)>/i
          # check to ensure the input is an array given that the attribute
          # is documented as an array but the input is not
          if attributes[self.class.attribute_map[key]].is_a?(Array)
            self.send("#{key}=", attributes[self.class.attribute_map[key]].map { |v| _deserialize($1, v) })
          end
        elsif !attributes[self.class.attribute_map[key]].nil?
          self.send("#{key}=", _deserialize(type, attributes[self.class.attribute_map[key]]))
        end
      end

      self
    end

    # Deserializes the data based on type
    # @param string type Data type
    # @param string value Value to be deserialized
    # @return [Object] Deserialized data
    def _deserialize(type, value)
      case type.to_sym
      when :Time
        Time.parse(value)
      when :Date
        Date.parse(value)
      when :String
        value.to_s
      when :Integer
        value.to_i
      when :Float
        value.to_f
      when :Boolean
        if value.to_s =~ /\A(true|t|yes|y|1)\z/i
          true
        else
          false
        end
      when :Object
        # generic object (usually a Hash), return directly
        value
      when /\AArray<(?<inner_type>.+)>\z/
        inner_type = Regexp.last_match[:inner_type]
        value.map { |v| _deserialize(inner_type, v) }
      when /\AHash<(?<k_type>.+?), (?<v_type>.+)>\z/
        k_type = Regexp.last_match[:k_type]
        v_type = Regexp.last_match[:v_type]
        {}.tap do |hash|
          value.each do |k, v|
            hash[_deserialize(k_type, k)] = _deserialize(v_type, v)
          end
        end
      else # model
        # models (e.g. Pet) or oneOf
        klass = OpenapiClient.const_get(type)
        klass.respond_to?(:openapi_one_of) ? klass.build(value) : klass.build_from_hash(value)
      end
    end

    # Returns the string representation of the object
    # @return [String] String presentation of the object
    def to_s
      to_hash.to_s
    end

    # to_body is an alias to to_hash (backward compatibility)
    # @return [Hash] Returns the object in the form of hash
    def to_body
      to_hash
    end

    # Returns the object in the form of hash
    # @return [Hash] Returns the object in the form of hash
    def to_hash
      hash = {}
      self.class.attribute_map.each_pair do |attr, param|
        value = self.send(attr)
        if value.nil?
          is_nullable = self.class.openapi_nullable.include?(attr)
          next if !is_nullable || (is_nullable && !instance_variable_defined?(:"@#{attr}"))
        end

        hash[param] = _to_hash(value)
      end
      hash
    end

    # Outputs non-array value in the form of hash
    # For object, use to_hash. Otherwise, just return the value
    # @param [Object] value Any valid value
    # @return [Hash] Returns the value in the form of hash
    def _to_hash(value)
      if value.is_a?(Array)
        value.compact.map { |v| _to_hash(v) }
      elsif value.is_a?(Hash)
        {}.tap do |hash|
          value.each { |k, v| hash[k] = _to_hash(v) }
        end
      elsif value.respond_to? :to_hash
        value.to_hash
      else
        value
      end
    end

  end

end