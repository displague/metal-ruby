"""
    Metal API

    This is the API for Equinix Metal Product. Interact with your devices, user account, and projects.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from metal.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from metal.model.bgp_neighbor_data_routes_in import BgpNeighborDataRoutesIn
    from metal.model.bgp_neighbor_data_routes_out import BgpNeighborDataRoutesOut
    globals()['BgpNeighborDataRoutesIn'] = BgpNeighborDataRoutesIn
    globals()['BgpNeighborDataRoutesOut'] = BgpNeighborDataRoutesOut


class BgpNeighborData(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'address_family': (float,),  # noqa: E501
            'customer_as': (float,),  # noqa: E501
            'customer_ip': (str,),  # noqa: E501
            'md5_enabled': (bool,),  # noqa: E501
            'md5_password': (str,),  # noqa: E501
            'multihop': (bool,),  # noqa: E501
            'peer_as': (float,),  # noqa: E501
            'peer_ips': ([str],),  # noqa: E501
            'routes_in': ([BgpNeighborDataRoutesIn],),  # noqa: E501
            'routes_out': ([BgpNeighborDataRoutesOut],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'address_family': 'address_family',  # noqa: E501
        'customer_as': 'customer_as',  # noqa: E501
        'customer_ip': 'customer_ip',  # noqa: E501
        'md5_enabled': 'md5_enabled',  # noqa: E501
        'md5_password': 'md5_password',  # noqa: E501
        'multihop': 'multihop',  # noqa: E501
        'peer_as': 'peer_as',  # noqa: E501
        'peer_ips': 'peer_ips',  # noqa: E501
        'routes_in': 'routes_in',  # noqa: E501
        'routes_out': 'routes_out',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """BgpNeighborData - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            address_family (float): Address Family for IP Address. [optional]  # noqa: E501
            customer_as (float): The customer's ASN. In a local BGP deployment, this will be an internal ASN used to route within the data center. For a global BGP deployment, this will be the your own ASN, configured when you set up BGP for your project.. [optional]  # noqa: E501
            customer_ip (str): The device's IP address. For an IPv4 BGP session, this is typically the private bond0 address for the device.. [optional]  # noqa: E501
            md5_enabled (bool): True if an MD5 password is configured for the project.. [optional]  # noqa: E501
            md5_password (str): The MD5 password configured for the project, if set.. [optional]  # noqa: E501
            multihop (bool): True when the BGP session should be configured as multihop.. [optional]  # noqa: E501
            peer_as (float): The Peer ASN to use when configuring BGP on your device.. [optional]  # noqa: E501
            peer_ips ([str]): A list of one or more IP addresses to use for the Peer IP section of your BGP configuration. For non-multihop sessions, this will typically be a single gateway address for the device. For multihop sessions, it will be a list of IPs.. [optional]  # noqa: E501
            routes_in ([BgpNeighborDataRoutesIn]): A list of project subnets. [optional]  # noqa: E501
            routes_out ([BgpNeighborDataRoutesOut]): A list of outgoing routes. Only populated if the BGP session has default route enabled.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
