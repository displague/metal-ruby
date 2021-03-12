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
  class CapacityReport
    attr_accessor :ams1

    attr_accessor :atl1

    attr_accessor :dfw1

    attr_accessor :ewr1

    attr_accessor :fra1

    attr_accessor :iad1

    attr_accessor :lax1

    attr_accessor :nrt1

    attr_accessor :ord1

    attr_accessor :sea1

    attr_accessor :sin1

    attr_accessor :sjc1

    attr_accessor :syd1

    attr_accessor :yyz1

    # Attribute mapping from ruby-style variable name to JSON key.
    def self.attribute_map
      {
        :'ams1' => :'ams1',
        :'atl1' => :'atl1',
        :'dfw1' => :'dfw1',
        :'ewr1' => :'ewr1',
        :'fra1' => :'fra1',
        :'iad1' => :'iad1',
        :'lax1' => :'lax1',
        :'nrt1' => :'nrt1',
        :'ord1' => :'ord1',
        :'sea1' => :'sea1',
        :'sin1' => :'sin1',
        :'sjc1' => :'sjc1',
        :'syd1' => :'syd1',
        :'yyz1' => :'yyz1'
      }
    end

    # Returns all the JSON keys this model knows about
    def self.acceptable_attributes
      attribute_map.values
    end

    # Attribute type mapping.
    def self.openapi_types
      {
        :'ams1' => :'CapacityPerFacility',
        :'atl1' => :'CapacityPerNewFacility',
        :'dfw1' => :'CapacityPerNewFacility',
        :'ewr1' => :'CapacityPerFacility',
        :'fra1' => :'CapacityPerNewFacility',
        :'iad1' => :'CapacityPerNewFacility',
        :'lax1' => :'CapacityPerNewFacility',
        :'nrt1' => :'CapacityPerFacility',
        :'ord1' => :'CapacityPerNewFacility',
        :'sea1' => :'CapacityPerNewFacility',
        :'sin1' => :'CapacityPerNewFacility',
        :'sjc1' => :'CapacityPerFacility',
        :'syd1' => :'CapacityPerNewFacility',
        :'yyz1' => :'CapacityPerNewFacility'
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
        fail ArgumentError, "The input argument (attributes) must be a hash in `OpenapiClient::CapacityReport` initialize method"
      end

      # check to see if the attribute exists and convert string to symbol for hash key
      attributes = attributes.each_with_object({}) { |(k, v), h|
        if (!self.class.attribute_map.key?(k.to_sym))
          fail ArgumentError, "`#{k}` is not a valid attribute in `OpenapiClient::CapacityReport`. Please check the name to make sure it's valid. List of attributes: " + self.class.attribute_map.keys.inspect
        end
        h[k.to_sym] = v
      }

      if attributes.key?(:'ams1')
        self.ams1 = attributes[:'ams1']
      end

      if attributes.key?(:'atl1')
        self.atl1 = attributes[:'atl1']
      end

      if attributes.key?(:'dfw1')
        self.dfw1 = attributes[:'dfw1']
      end

      if attributes.key?(:'ewr1')
        self.ewr1 = attributes[:'ewr1']
      end

      if attributes.key?(:'fra1')
        self.fra1 = attributes[:'fra1']
      end

      if attributes.key?(:'iad1')
        self.iad1 = attributes[:'iad1']
      end

      if attributes.key?(:'lax1')
        self.lax1 = attributes[:'lax1']
      end

      if attributes.key?(:'nrt1')
        self.nrt1 = attributes[:'nrt1']
      end

      if attributes.key?(:'ord1')
        self.ord1 = attributes[:'ord1']
      end

      if attributes.key?(:'sea1')
        self.sea1 = attributes[:'sea1']
      end

      if attributes.key?(:'sin1')
        self.sin1 = attributes[:'sin1']
      end

      if attributes.key?(:'sjc1')
        self.sjc1 = attributes[:'sjc1']
      end

      if attributes.key?(:'syd1')
        self.syd1 = attributes[:'syd1']
      end

      if attributes.key?(:'yyz1')
        self.yyz1 = attributes[:'yyz1']
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
          ams1 == o.ams1 &&
          atl1 == o.atl1 &&
          dfw1 == o.dfw1 &&
          ewr1 == o.ewr1 &&
          fra1 == o.fra1 &&
          iad1 == o.iad1 &&
          lax1 == o.lax1 &&
          nrt1 == o.nrt1 &&
          ord1 == o.ord1 &&
          sea1 == o.sea1 &&
          sin1 == o.sin1 &&
          sjc1 == o.sjc1 &&
          syd1 == o.syd1 &&
          yyz1 == o.yyz1
    end

    # @see the `==` method
    # @param [Object] Object to be compared
    def eql?(o)
      self == o
    end

    # Calculates hash code according to all attributes.
    # @return [Integer] Hash code
    def hash
      [ams1, atl1, dfw1, ewr1, fra1, iad1, lax1, nrt1, ord1, sea1, sin1, sjc1, syd1, yyz1].hash
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
