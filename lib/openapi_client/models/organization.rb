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
  class Organization
    attr_accessor :id

    attr_accessor :name

    attr_accessor :description

    attr_accessor :website

    attr_accessor :twitter

    attr_accessor :logo

    attr_accessor :created_at

    attr_accessor :updated_at

    attr_accessor :projects

    attr_accessor :members

    attr_accessor :memberships

    attr_accessor :address

    attr_accessor :billing_address

    attr_accessor :entitlement

    attr_accessor :terms

    attr_accessor :credit_amount

    attr_accessor :customdata

    # Force to all members to have enabled the two factor authentication after that date, unless the value is null
    attr_accessor :enforce_2fa_at

    # Attribute mapping from ruby-style variable name to JSON key.
    def self.attribute_map
      {
        :'id' => :'id',
        :'name' => :'name',
        :'description' => :'description',
        :'website' => :'website',
        :'twitter' => :'twitter',
        :'logo' => :'logo',
        :'created_at' => :'created_at',
        :'updated_at' => :'updated_at',
        :'projects' => :'projects',
        :'members' => :'members',
        :'memberships' => :'memberships',
        :'address' => :'address',
        :'billing_address' => :'billing_address',
        :'entitlement' => :'entitlement',
        :'terms' => :'terms',
        :'credit_amount' => :'credit_amount',
        :'customdata' => :'customdata',
        :'enforce_2fa_at' => :'enforce_2fa_at'
      }
    end

    # Returns all the JSON keys this model knows about
    def self.acceptable_attributes
      attribute_map.values
    end

    # Attribute type mapping.
    def self.openapi_types
      {
        :'id' => :'String',
        :'name' => :'String',
        :'description' => :'String',
        :'website' => :'String',
        :'twitter' => :'String',
        :'logo' => :'File',
        :'created_at' => :'Time',
        :'updated_at' => :'Time',
        :'projects' => :'Array<Href>',
        :'members' => :'Array<Href>',
        :'memberships' => :'Array<Href>',
        :'address' => :'Address',
        :'billing_address' => :'Address',
        :'entitlement' => :'Entitlement',
        :'terms' => :'Integer',
        :'credit_amount' => :'Float',
        :'customdata' => :'Object',
        :'enforce_2fa_at' => :'Time'
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
        fail ArgumentError, "The input argument (attributes) must be a hash in `OpenapiClient::Organization` initialize method"
      end

      # check to see if the attribute exists and convert string to symbol for hash key
      attributes = attributes.each_with_object({}) { |(k, v), h|
        if (!self.class.attribute_map.key?(k.to_sym))
          fail ArgumentError, "`#{k}` is not a valid attribute in `OpenapiClient::Organization`. Please check the name to make sure it's valid. List of attributes: " + self.class.attribute_map.keys.inspect
        end
        h[k.to_sym] = v
      }

      if attributes.key?(:'id')
        self.id = attributes[:'id']
      end

      if attributes.key?(:'name')
        self.name = attributes[:'name']
      end

      if attributes.key?(:'description')
        self.description = attributes[:'description']
      end

      if attributes.key?(:'website')
        self.website = attributes[:'website']
      end

      if attributes.key?(:'twitter')
        self.twitter = attributes[:'twitter']
      end

      if attributes.key?(:'logo')
        self.logo = attributes[:'logo']
      end

      if attributes.key?(:'created_at')
        self.created_at = attributes[:'created_at']
      end

      if attributes.key?(:'updated_at')
        self.updated_at = attributes[:'updated_at']
      end

      if attributes.key?(:'projects')
        if (value = attributes[:'projects']).is_a?(Array)
          self.projects = value
        end
      end

      if attributes.key?(:'members')
        if (value = attributes[:'members']).is_a?(Array)
          self.members = value
        end
      end

      if attributes.key?(:'memberships')
        if (value = attributes[:'memberships']).is_a?(Array)
          self.memberships = value
        end
      end

      if attributes.key?(:'address')
        self.address = attributes[:'address']
      end

      if attributes.key?(:'billing_address')
        self.billing_address = attributes[:'billing_address']
      end

      if attributes.key?(:'entitlement')
        self.entitlement = attributes[:'entitlement']
      end

      if attributes.key?(:'terms')
        self.terms = attributes[:'terms']
      end

      if attributes.key?(:'credit_amount')
        self.credit_amount = attributes[:'credit_amount']
      end

      if attributes.key?(:'customdata')
        self.customdata = attributes[:'customdata']
      end

      if attributes.key?(:'enforce_2fa_at')
        self.enforce_2fa_at = attributes[:'enforce_2fa_at']
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
          id == o.id &&
          name == o.name &&
          description == o.description &&
          website == o.website &&
          twitter == o.twitter &&
          logo == o.logo &&
          created_at == o.created_at &&
          updated_at == o.updated_at &&
          projects == o.projects &&
          members == o.members &&
          memberships == o.memberships &&
          address == o.address &&
          billing_address == o.billing_address &&
          entitlement == o.entitlement &&
          terms == o.terms &&
          credit_amount == o.credit_amount &&
          customdata == o.customdata &&
          enforce_2fa_at == o.enforce_2fa_at
    end

    # @see the `==` method
    # @param [Object] Object to be compared
    def eql?(o)
      self == o
    end

    # Calculates hash code according to all attributes.
    # @return [Integer] Hash code
    def hash
      [id, name, description, website, twitter, logo, created_at, updated_at, projects, members, memberships, address, billing_address, entitlement, terms, credit_amount, customdata, enforce_2fa_at].hash
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
