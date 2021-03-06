# coding: utf-8

"""
    Camunda BPM REST API

    OpenApi Spec for Camunda BPM REST API.  # noqa: E501

    The version of the OpenAPI document: 7.13.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class MultiFormVariableBinaryDto(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'data': 'file',
        'value_type': 'str'
    }

    attribute_map = {
        'data': 'data',
        'value_type': 'valueType'
    }

    def __init__(self, data=None, value_type=None, local_vars_configuration=None):  # noqa: E501
        """MultiFormVariableBinaryDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._data = None
        self._value_type = None
        self.discriminator = None

        self.data = data
        if value_type is not None:
            self.value_type = value_type

    @property
    def data(self):
        """Gets the data of this MultiFormVariableBinaryDto.  # noqa: E501

        The binary data to be set. For File variables, this multipart can contain the filename, binary value and MIME type of the file variable to be set Only the filename is mandatory.  # noqa: E501

        :return: The data of this MultiFormVariableBinaryDto.  # noqa: E501
        :rtype: file
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this MultiFormVariableBinaryDto.

        The binary data to be set. For File variables, this multipart can contain the filename, binary value and MIME type of the file variable to be set Only the filename is mandatory.  # noqa: E501

        :param data: The data of this MultiFormVariableBinaryDto.  # noqa: E501
        :type: file
        """

        self._data = data

    @property
    def value_type(self):
        """Gets the value_type of this MultiFormVariableBinaryDto.  # noqa: E501

        The name of the variable type. Either Bytes for a byte array variable or File for a file variable.  # noqa: E501

        :return: The value_type of this MultiFormVariableBinaryDto.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this MultiFormVariableBinaryDto.

        The name of the variable type. Either Bytes for a byte array variable or File for a file variable.  # noqa: E501

        :param value_type: The value_type of this MultiFormVariableBinaryDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Bytes", "File"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and value_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `value_type` ({0}), must be one of {1}"  # noqa: E501
                .format(value_type, allowed_values)
            )

        self._value_type = value_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MultiFormVariableBinaryDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MultiFormVariableBinaryDto):
            return True

        return self.to_dict() != other.to_dict()
