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


class ExtendLockOnExternalTaskDto(object):
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
        'worker_id': 'str',
        'new_duration': 'int'
    }

    attribute_map = {
        'worker_id': 'workerId',
        'new_duration': 'newDuration'
    }

    def __init__(self, worker_id=None, new_duration=None, local_vars_configuration=None):  # noqa: E501
        """ExtendLockOnExternalTaskDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._worker_id = None
        self._new_duration = None
        self.discriminator = None

        if worker_id is not None:
            self.worker_id = worker_id
        if new_duration is not None:
            self.new_duration = new_duration

    @property
    def worker_id(self):
        """Gets the worker_id of this ExtendLockOnExternalTaskDto.  # noqa: E501

        The ID of a worker who is locking the external task.  # noqa: E501

        :return: The worker_id of this ExtendLockOnExternalTaskDto.  # noqa: E501
        :rtype: str
        """
        return self._worker_id

    @worker_id.setter
    def worker_id(self, worker_id):
        """Sets the worker_id of this ExtendLockOnExternalTaskDto.

        The ID of a worker who is locking the external task.  # noqa: E501

        :param worker_id: The worker_id of this ExtendLockOnExternalTaskDto.  # noqa: E501
        :type: str
        """

        self._worker_id = worker_id

    @property
    def new_duration(self):
        """Gets the new_duration of this ExtendLockOnExternalTaskDto.  # noqa: E501

        An amount of time (in milliseconds). This is the new lock duration starting from the current moment.  # noqa: E501

        :return: The new_duration of this ExtendLockOnExternalTaskDto.  # noqa: E501
        :rtype: int
        """
        return self._new_duration

    @new_duration.setter
    def new_duration(self, new_duration):
        """Sets the new_duration of this ExtendLockOnExternalTaskDto.

        An amount of time (in milliseconds). This is the new lock duration starting from the current moment.  # noqa: E501

        :param new_duration: The new_duration of this ExtendLockOnExternalTaskDto.  # noqa: E501
        :type: int
        """

        self._new_duration = new_duration

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
        if not isinstance(other, ExtendLockOnExternalTaskDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExtendLockOnExternalTaskDto):
            return True

        return self.to_dict() != other.to_dict()
