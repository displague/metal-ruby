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
    from metal.model.device_create_input_ip_addresses import DeviceCreateInputIpAddresses
    globals()['DeviceCreateInputIpAddresses'] = DeviceCreateInputIpAddresses


class DeviceCreateInput(ModelNormal):
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
            'facility': (str,),  # noqa: E501
            'plan': (str,),  # noqa: E501
            'operating_system': (str,),  # noqa: E501
            'hostname': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'billing_cycle': (str,),  # noqa: E501
            'always_pxe': (bool,),  # noqa: E501
            'ipxe_script_url': (str,),  # noqa: E501
            'userdata': (str,),  # noqa: E501
            'locked': (bool,),  # noqa: E501
            'customdata': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'hardware_reservation_id': (str,),  # noqa: E501
            'spot_instance': (bool,),  # noqa: E501
            'spot_price_max': (float,),  # noqa: E501
            'termination_time': (datetime,),  # noqa: E501
            'tags': ([str],),  # noqa: E501
            'project_ssh_keys': ([str],),  # noqa: E501
            'user_ssh_keys': ([str],),  # noqa: E501
            'features': ([str],),  # noqa: E501
            'public_ipv4_subnet_size': (float,),  # noqa: E501
            'private_ipv4_subnet_size': (float,),  # noqa: E501
            'ip_addresses': ([DeviceCreateInputIpAddresses],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'facility': 'facility',  # noqa: E501
        'plan': 'plan',  # noqa: E501
        'operating_system': 'operating_system',  # noqa: E501
        'hostname': 'hostname',  # noqa: E501
        'description': 'description',  # noqa: E501
        'billing_cycle': 'billing_cycle',  # noqa: E501
        'always_pxe': 'always_pxe',  # noqa: E501
        'ipxe_script_url': 'ipxe_script_url',  # noqa: E501
        'userdata': 'userdata',  # noqa: E501
        'locked': 'locked',  # noqa: E501
        'customdata': 'customdata',  # noqa: E501
        'hardware_reservation_id': 'hardware_reservation_id',  # noqa: E501
        'spot_instance': 'spot_instance',  # noqa: E501
        'spot_price_max': 'spot_price_max',  # noqa: E501
        'termination_time': 'termination_time',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'project_ssh_keys': 'project_ssh_keys',  # noqa: E501
        'user_ssh_keys': 'user_ssh_keys',  # noqa: E501
        'features': 'features',  # noqa: E501
        'public_ipv4_subnet_size': 'public_ipv4_subnet_size',  # noqa: E501
        'private_ipv4_subnet_size': 'private_ipv4_subnet_size',  # noqa: E501
        'ip_addresses': 'ip_addresses',  # noqa: E501
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
    def __init__(self, facility, plan, operating_system, *args, **kwargs):  # noqa: E501
        """DeviceCreateInput - a model defined in OpenAPI

        Args:
            facility (str):
            plan (str):
            operating_system (str):

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
            hostname (str): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
            billing_cycle (str): [optional]  # noqa: E501
            always_pxe (bool): [optional]  # noqa: E501
            ipxe_script_url (str): [optional]  # noqa: E501
            userdata (str): [optional]  # noqa: E501
            locked (bool): [optional]  # noqa: E501
            customdata ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            hardware_reservation_id (str): [optional]  # noqa: E501
            spot_instance (bool): [optional]  # noqa: E501
            spot_price_max (float): [optional]  # noqa: E501
            termination_time (datetime): [optional]  # noqa: E501
            tags ([str]): [optional]  # noqa: E501
            project_ssh_keys ([str]): [optional]  # noqa: E501
            user_ssh_keys ([str]): The UUIDs of users whose SSH keys should be included on the provisioned device.. [optional]  # noqa: E501
            features ([str]): [optional]  # noqa: E501
            public_ipv4_subnet_size (float): Deprecated. Use ip_addresses. Subnet range for addresses allocated to this device. Your project must have addresses available for a non-default request.. [optional]  # noqa: E501
            private_ipv4_subnet_size (float): Deprecated. Use ip_addresses. Subnet range for addresses allocated to this device.. [optional]  # noqa: E501
            ip_addresses ([DeviceCreateInputIpAddresses]): [optional]  # noqa: E501
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

        self.facility = facility
        self.plan = plan
        self.operating_system = operating_system
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)