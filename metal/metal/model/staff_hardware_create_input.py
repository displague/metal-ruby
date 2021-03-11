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


class StaffHardwareCreateInput(ModelNormal):
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
        return {
            'type': (str,),  # noqa: E501
            'model_number': (str,),  # noqa: E501
            'state': (str,),  # noqa: E501
            'u_spaces': (int,),  # noqa: E501
            'serial_number': (str,),  # noqa: E501
            'server_rack_id': (str,),  # noqa: E501
            'leased': (bool,),  # noqa: E501
            'lease_number': (str,),  # noqa: E501
            'lease_expires_at': (datetime,),  # noqa: E501
            'arch': (str,),  # noqa: E501
            'dhcp_group': (str,),  # noqa: E501
            'efi_boot': (bool,),  # noqa: E501
            'bios_password': (str,),  # noqa: E501
            'maintenance_state': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'static_name': (str,),  # noqa: E501
            'uefi_supports_rfc3021': (bool,),  # noqa: E501
            'link_aggregation': (str,),  # noqa: E501
            'provisioner': (str,),  # noqa: E501
            'supported_networking': ([str],),  # noqa: E501
            'services': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'management': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'data': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'role': (str,),  # noqa: E501
            'vlan_id': (int,),  # noqa: E501
            'tpm': (bool,),  # noqa: E501
            'switch_short_id': (str,),  # noqa: E501
            'is_primary': (bool,),  # noqa: E501
            'loopback_ip': (str,),  # noqa: E501
            'vrf': (str,),  # noqa: E501
            'exclude_from_narwhal': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'type': 'type',  # noqa: E501
        'model_number': 'model_number',  # noqa: E501
        'state': 'state',  # noqa: E501
        'u_spaces': 'u_spaces',  # noqa: E501
        'serial_number': 'serial_number',  # noqa: E501
        'server_rack_id': 'server_rack_id',  # noqa: E501
        'leased': 'leased',  # noqa: E501
        'lease_number': 'lease_number',  # noqa: E501
        'lease_expires_at': 'lease_expires_at',  # noqa: E501
        'arch': 'arch',  # noqa: E501
        'dhcp_group': 'dhcp_group',  # noqa: E501
        'efi_boot': 'efi_boot',  # noqa: E501
        'bios_password': 'bios_password',  # noqa: E501
        'maintenance_state': 'maintenance_state',  # noqa: E501
        'name': 'name',  # noqa: E501
        'static_name': 'static_name',  # noqa: E501
        'uefi_supports_rfc3021': 'uefi_supports_rfc3021',  # noqa: E501
        'link_aggregation': 'link_aggregation',  # noqa: E501
        'provisioner': 'provisioner',  # noqa: E501
        'supported_networking': 'supported_networking',  # noqa: E501
        'services': 'services',  # noqa: E501
        'management': 'management',  # noqa: E501
        'data': 'data',  # noqa: E501
        'role': 'role',  # noqa: E501
        'vlan_id': 'vlan_id',  # noqa: E501
        'tpm': 'tpm',  # noqa: E501
        'switch_short_id': 'switch_short_id',  # noqa: E501
        'is_primary': 'is_primary',  # noqa: E501
        'loopback_ip': 'loopback_ip',  # noqa: E501
        'vrf': 'vrf',  # noqa: E501
        'exclude_from_narwhal': 'exclude_from_narwhal',  # noqa: E501
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
    def __init__(self, type, model_number, *args, **kwargs):  # noqa: E501
        """StaffHardwareCreateInput - a model defined in OpenAPI

        Args:
            type (str):
            model_number (str):

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
            state (str): [optional]  # noqa: E501
            u_spaces (int): [optional]  # noqa: E501
            serial_number (str): [optional]  # noqa: E501
            server_rack_id (str): [optional]  # noqa: E501
            leased (bool): [optional]  # noqa: E501
            lease_number (str): [optional]  # noqa: E501
            lease_expires_at (datetime): [optional]  # noqa: E501
            arch (str): [optional]  # noqa: E501
            dhcp_group (str): [optional]  # noqa: E501
            efi_boot (bool): [optional]  # noqa: E501
            bios_password (str): [optional]  # noqa: E501
            maintenance_state (str): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            static_name (str): [optional]  # noqa: E501
            uefi_supports_rfc3021 (bool): [optional]  # noqa: E501
            link_aggregation (str): [optional]  # noqa: E501
            provisioner (str): [optional]  # noqa: E501
            supported_networking ([str]): [optional]  # noqa: E501
            services ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            management ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            data ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): Holds custom data depending on the hardware type. Any attribute set here can also be set as part of the hardware object. [optional]  # noqa: E501
            role (str): Role of the hardware. Will affect how the hardware will be named. Its required for certain hardware types.. [optional]  # noqa: E501
            vlan_id (int): On certain server nodes/sleds (t1.small.x86 and x1.small.x86), it describes the internal VLAN used to route traffic inside the BladeSwitch.. [optional]  # noqa: E501
            tpm (bool): On servers, describe if the server has a TPM card.. [optional]  # noqa: E501
            switch_short_id (str): On servers, describe the switch the server is connected too. If left empty, the value will be auto set on creation.. [optional]  # noqa: E501
            is_primary (bool): Switch attribute. On Arista switches, indicates which of the 2 Arista switches in mlag mode is the primary. Its used to properly configure the switch through Narhwal.. [optional]  # noqa: E501
            loopback_ip (str): Switch attribute. Specify the loopback_ip of the switch. Currently is not used in our automation.. [optional]  # noqa: E501
            vrf (str): Switch attribute. Specify the Virtual Routing and Forwarding tag used on the configuration.. [optional]  # noqa: E501
            exclude_from_narwhal (bool): Switch attribute. If set to true, any switch configuration task created by our automation will be skipped for this switch. [optional]  # noqa: E501
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

        self.type = type
        self.model_number = model_number
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)