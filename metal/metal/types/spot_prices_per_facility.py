# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal.types.spot_prices_per_baremetal import SpotPricesPerBaremetal
from metal import util

from metal.types.spot_prices_per_baremetal import SpotPricesPerBaremetal  # noqa: E501

class SpotPricesPerFacility(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, baremetal_2a=None, baremetal_2a2=None, baremetal_1=None, baremetal_3=None, c2_medium_x86=None, baremetal_2=None, m2_xlarge_x86=None, baremetal_s=None, baremetal_0=None):  # noqa: E501
        """SpotPricesPerFacility - a model defined in OpenAPI

        :param baremetal_2a: The baremetal_2a of this SpotPricesPerFacility.  # noqa: E501
        :type baremetal_2a: SpotPricesPerBaremetal
        :param baremetal_2a2: The baremetal_2a2 of this SpotPricesPerFacility.  # noqa: E501
        :type baremetal_2a2: SpotPricesPerBaremetal
        :param baremetal_1: The baremetal_1 of this SpotPricesPerFacility.  # noqa: E501
        :type baremetal_1: SpotPricesPerBaremetal
        :param baremetal_3: The baremetal_3 of this SpotPricesPerFacility.  # noqa: E501
        :type baremetal_3: SpotPricesPerBaremetal
        :param c2_medium_x86: The c2_medium_x86 of this SpotPricesPerFacility.  # noqa: E501
        :type c2_medium_x86: SpotPricesPerBaremetal
        :param baremetal_2: The baremetal_2 of this SpotPricesPerFacility.  # noqa: E501
        :type baremetal_2: SpotPricesPerBaremetal
        :param m2_xlarge_x86: The m2_xlarge_x86 of this SpotPricesPerFacility.  # noqa: E501
        :type m2_xlarge_x86: SpotPricesPerBaremetal
        :param baremetal_s: The baremetal_s of this SpotPricesPerFacility.  # noqa: E501
        :type baremetal_s: SpotPricesPerBaremetal
        :param baremetal_0: The baremetal_0 of this SpotPricesPerFacility.  # noqa: E501
        :type baremetal_0: SpotPricesPerBaremetal
        """
        self.openapi_types = {
            'baremetal_2a': SpotPricesPerBaremetal,
            'baremetal_2a2': SpotPricesPerBaremetal,
            'baremetal_1': SpotPricesPerBaremetal,
            'baremetal_3': SpotPricesPerBaremetal,
            'c2_medium_x86': SpotPricesPerBaremetal,
            'baremetal_2': SpotPricesPerBaremetal,
            'm2_xlarge_x86': SpotPricesPerBaremetal,
            'baremetal_s': SpotPricesPerBaremetal,
            'baremetal_0': SpotPricesPerBaremetal
        }

        self.attribute_map = {
            'baremetal_2a': 'baremetal_2a',
            'baremetal_2a2': 'baremetal_2a2',
            'baremetal_1': 'baremetal_1',
            'baremetal_3': 'baremetal_3',
            'c2_medium_x86': 'c2.medium.x86',
            'baremetal_2': 'baremetal_2',
            'm2_xlarge_x86': 'm2.xlarge.x86',
            'baremetal_s': 'baremetal_s',
            'baremetal_0': 'baremetal_0'
        }

        self._baremetal_2a = baremetal_2a
        self._baremetal_2a2 = baremetal_2a2
        self._baremetal_1 = baremetal_1
        self._baremetal_3 = baremetal_3
        self._c2_medium_x86 = c2_medium_x86
        self._baremetal_2 = baremetal_2
        self._m2_xlarge_x86 = m2_xlarge_x86
        self._baremetal_s = baremetal_s
        self._baremetal_0 = baremetal_0

    @classmethod
    def from_dict(cls, dikt) -> 'SpotPricesPerFacility':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SpotPricesPerFacility of this SpotPricesPerFacility.  # noqa: E501
        :rtype: SpotPricesPerFacility
        """
        return util.deserialize_model(dikt, cls)

    @property
    def baremetal_2a(self):
        """Gets the baremetal_2a of this SpotPricesPerFacility.


        :return: The baremetal_2a of this SpotPricesPerFacility.
        :rtype: SpotPricesPerBaremetal
        """
        return self._baremetal_2a

    @baremetal_2a.setter
    def baremetal_2a(self, baremetal_2a):
        """Sets the baremetal_2a of this SpotPricesPerFacility.


        :param baremetal_2a: The baremetal_2a of this SpotPricesPerFacility.
        :type baremetal_2a: SpotPricesPerBaremetal
        """

        self._baremetal_2a = baremetal_2a

    @property
    def baremetal_2a2(self):
        """Gets the baremetal_2a2 of this SpotPricesPerFacility.


        :return: The baremetal_2a2 of this SpotPricesPerFacility.
        :rtype: SpotPricesPerBaremetal
        """
        return self._baremetal_2a2

    @baremetal_2a2.setter
    def baremetal_2a2(self, baremetal_2a2):
        """Sets the baremetal_2a2 of this SpotPricesPerFacility.


        :param baremetal_2a2: The baremetal_2a2 of this SpotPricesPerFacility.
        :type baremetal_2a2: SpotPricesPerBaremetal
        """

        self._baremetal_2a2 = baremetal_2a2

    @property
    def baremetal_1(self):
        """Gets the baremetal_1 of this SpotPricesPerFacility.


        :return: The baremetal_1 of this SpotPricesPerFacility.
        :rtype: SpotPricesPerBaremetal
        """
        return self._baremetal_1

    @baremetal_1.setter
    def baremetal_1(self, baremetal_1):
        """Sets the baremetal_1 of this SpotPricesPerFacility.


        :param baremetal_1: The baremetal_1 of this SpotPricesPerFacility.
        :type baremetal_1: SpotPricesPerBaremetal
        """

        self._baremetal_1 = baremetal_1

    @property
    def baremetal_3(self):
        """Gets the baremetal_3 of this SpotPricesPerFacility.


        :return: The baremetal_3 of this SpotPricesPerFacility.
        :rtype: SpotPricesPerBaremetal
        """
        return self._baremetal_3

    @baremetal_3.setter
    def baremetal_3(self, baremetal_3):
        """Sets the baremetal_3 of this SpotPricesPerFacility.


        :param baremetal_3: The baremetal_3 of this SpotPricesPerFacility.
        :type baremetal_3: SpotPricesPerBaremetal
        """

        self._baremetal_3 = baremetal_3

    @property
    def c2_medium_x86(self):
        """Gets the c2_medium_x86 of this SpotPricesPerFacility.


        :return: The c2_medium_x86 of this SpotPricesPerFacility.
        :rtype: SpotPricesPerBaremetal
        """
        return self._c2_medium_x86

    @c2_medium_x86.setter
    def c2_medium_x86(self, c2_medium_x86):
        """Sets the c2_medium_x86 of this SpotPricesPerFacility.


        :param c2_medium_x86: The c2_medium_x86 of this SpotPricesPerFacility.
        :type c2_medium_x86: SpotPricesPerBaremetal
        """

        self._c2_medium_x86 = c2_medium_x86

    @property
    def baremetal_2(self):
        """Gets the baremetal_2 of this SpotPricesPerFacility.


        :return: The baremetal_2 of this SpotPricesPerFacility.
        :rtype: SpotPricesPerBaremetal
        """
        return self._baremetal_2

    @baremetal_2.setter
    def baremetal_2(self, baremetal_2):
        """Sets the baremetal_2 of this SpotPricesPerFacility.


        :param baremetal_2: The baremetal_2 of this SpotPricesPerFacility.
        :type baremetal_2: SpotPricesPerBaremetal
        """

        self._baremetal_2 = baremetal_2

    @property
    def m2_xlarge_x86(self):
        """Gets the m2_xlarge_x86 of this SpotPricesPerFacility.


        :return: The m2_xlarge_x86 of this SpotPricesPerFacility.
        :rtype: SpotPricesPerBaremetal
        """
        return self._m2_xlarge_x86

    @m2_xlarge_x86.setter
    def m2_xlarge_x86(self, m2_xlarge_x86):
        """Sets the m2_xlarge_x86 of this SpotPricesPerFacility.


        :param m2_xlarge_x86: The m2_xlarge_x86 of this SpotPricesPerFacility.
        :type m2_xlarge_x86: SpotPricesPerBaremetal
        """

        self._m2_xlarge_x86 = m2_xlarge_x86

    @property
    def baremetal_s(self):
        """Gets the baremetal_s of this SpotPricesPerFacility.


        :return: The baremetal_s of this SpotPricesPerFacility.
        :rtype: SpotPricesPerBaremetal
        """
        return self._baremetal_s

    @baremetal_s.setter
    def baremetal_s(self, baremetal_s):
        """Sets the baremetal_s of this SpotPricesPerFacility.


        :param baremetal_s: The baremetal_s of this SpotPricesPerFacility.
        :type baremetal_s: SpotPricesPerBaremetal
        """

        self._baremetal_s = baremetal_s

    @property
    def baremetal_0(self):
        """Gets the baremetal_0 of this SpotPricesPerFacility.


        :return: The baremetal_0 of this SpotPricesPerFacility.
        :rtype: SpotPricesPerBaremetal
        """
        return self._baremetal_0

    @baremetal_0.setter
    def baremetal_0(self, baremetal_0):
        """Sets the baremetal_0 of this SpotPricesPerFacility.


        :param baremetal_0: The baremetal_0 of this SpotPricesPerFacility.
        :type baremetal_0: SpotPricesPerBaremetal
        """

        self._baremetal_0 = baremetal_0
