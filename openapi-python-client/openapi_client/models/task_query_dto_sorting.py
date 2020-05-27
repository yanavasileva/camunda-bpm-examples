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


class TaskQueryDtoSorting(object):
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
        'sort_by': 'str',
        'sort_order': 'str',
        'parameters': 'SortTaskQueryParametersDto'
    }

    attribute_map = {
        'sort_by': 'sortBy',
        'sort_order': 'sortOrder',
        'parameters': 'parameters'
    }

    def __init__(self, sort_by=None, sort_order=None, parameters=None, local_vars_configuration=None):  # noqa: E501
        """TaskQueryDtoSorting - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sort_by = None
        self._sort_order = None
        self._parameters = None
        self.discriminator = None

        if sort_by is not None:
            self.sort_by = sort_by
        if sort_order is not None:
            self.sort_order = sort_order
        if parameters is not None:
            self.parameters = parameters

    @property
    def sort_by(self):
        """Gets the sort_by of this TaskQueryDtoSorting.  # noqa: E501

        Sort the results lexicographically by a given criterion. Must be used in conjunction with the sortOrder parameter.  # noqa: E501

        :return: The sort_by of this TaskQueryDtoSorting.  # noqa: E501
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this TaskQueryDtoSorting.

        Sort the results lexicographically by a given criterion. Must be used in conjunction with the sortOrder parameter.  # noqa: E501

        :param sort_by: The sort_by of this TaskQueryDtoSorting.  # noqa: E501
        :type: str
        """
        allowed_values = ["instanceId", "caseInstanceId", "dueDate", "executionId", "caseExecutionId", "assignee", "created", "description", "id", "name", "nameCaseInsensitive", "priority", "processVariable", "executionVariable", "taskVariable", "caseExecutionVariable", "caseInstanceVariable"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and sort_by not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `sort_by` ({0}), must be one of {1}"  # noqa: E501
                .format(sort_by, allowed_values)
            )

        self._sort_by = sort_by

    @property
    def sort_order(self):
        """Gets the sort_order of this TaskQueryDtoSorting.  # noqa: E501

        Sort the results in a given order. Values may be `asc` for ascending order or `desc` for descending order. Must be used in conjunction with the sortBy parameter.  # noqa: E501

        :return: The sort_order of this TaskQueryDtoSorting.  # noqa: E501
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this TaskQueryDtoSorting.

        Sort the results in a given order. Values may be `asc` for ascending order or `desc` for descending order. Must be used in conjunction with the sortBy parameter.  # noqa: E501

        :param sort_order: The sort_order of this TaskQueryDtoSorting.  # noqa: E501
        :type: str
        """
        allowed_values = ["asc", "desc"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and sort_order not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `sort_order` ({0}), must be one of {1}"  # noqa: E501
                .format(sort_order, allowed_values)
            )

        self._sort_order = sort_order

    @property
    def parameters(self):
        """Gets the parameters of this TaskQueryDtoSorting.  # noqa: E501


        :return: The parameters of this TaskQueryDtoSorting.  # noqa: E501
        :rtype: SortTaskQueryParametersDto
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this TaskQueryDtoSorting.


        :param parameters: The parameters of this TaskQueryDtoSorting.  # noqa: E501
        :type: SortTaskQueryParametersDto
        """

        self._parameters = parameters

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
        if not isinstance(other, TaskQueryDtoSorting):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskQueryDtoSorting):
            return True

        return self.to_dict() != other.to_dict()
