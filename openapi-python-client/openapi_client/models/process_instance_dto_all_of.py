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


class ProcessInstanceDtoAllOf(object):
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
        'id': 'str',
        'definition_id': 'str',
        'business_key': 'str',
        'case_instance_id': 'str',
        'ended': 'bool',
        'suspended': 'bool',
        'tenant_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'definition_id': 'definitionId',
        'business_key': 'businessKey',
        'case_instance_id': 'caseInstanceId',
        'ended': 'ended',
        'suspended': 'suspended',
        'tenant_id': 'tenantId'
    }

    def __init__(self, id=None, definition_id=None, business_key=None, case_instance_id=None, ended=None, suspended=None, tenant_id=None, local_vars_configuration=None):  # noqa: E501
        """ProcessInstanceDtoAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._definition_id = None
        self._business_key = None
        self._case_instance_id = None
        self._ended = None
        self._suspended = None
        self._tenant_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if definition_id is not None:
            self.definition_id = definition_id
        if business_key is not None:
            self.business_key = business_key
        if case_instance_id is not None:
            self.case_instance_id = case_instance_id
        if ended is not None:
            self.ended = ended
        if suspended is not None:
            self.suspended = suspended
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def id(self):
        """Gets the id of this ProcessInstanceDtoAllOf.  # noqa: E501

        The id of the process instance.  # noqa: E501

        :return: The id of this ProcessInstanceDtoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProcessInstanceDtoAllOf.

        The id of the process instance.  # noqa: E501

        :param id: The id of this ProcessInstanceDtoAllOf.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def definition_id(self):
        """Gets the definition_id of this ProcessInstanceDtoAllOf.  # noqa: E501

        The id of the process definition that this process instance belongs to.  # noqa: E501

        :return: The definition_id of this ProcessInstanceDtoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._definition_id

    @definition_id.setter
    def definition_id(self, definition_id):
        """Sets the definition_id of this ProcessInstanceDtoAllOf.

        The id of the process definition that this process instance belongs to.  # noqa: E501

        :param definition_id: The definition_id of this ProcessInstanceDtoAllOf.  # noqa: E501
        :type: str
        """

        self._definition_id = definition_id

    @property
    def business_key(self):
        """Gets the business_key of this ProcessInstanceDtoAllOf.  # noqa: E501

        The business key of the process instance.  # noqa: E501

        :return: The business_key of this ProcessInstanceDtoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._business_key

    @business_key.setter
    def business_key(self, business_key):
        """Sets the business_key of this ProcessInstanceDtoAllOf.

        The business key of the process instance.  # noqa: E501

        :param business_key: The business_key of this ProcessInstanceDtoAllOf.  # noqa: E501
        :type: str
        """

        self._business_key = business_key

    @property
    def case_instance_id(self):
        """Gets the case_instance_id of this ProcessInstanceDtoAllOf.  # noqa: E501

        The id of the case instance associated with the process instance.  # noqa: E501

        :return: The case_instance_id of this ProcessInstanceDtoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._case_instance_id

    @case_instance_id.setter
    def case_instance_id(self, case_instance_id):
        """Sets the case_instance_id of this ProcessInstanceDtoAllOf.

        The id of the case instance associated with the process instance.  # noqa: E501

        :param case_instance_id: The case_instance_id of this ProcessInstanceDtoAllOf.  # noqa: E501
        :type: str
        """

        self._case_instance_id = case_instance_id

    @property
    def ended(self):
        """Gets the ended of this ProcessInstanceDtoAllOf.  # noqa: E501

        A flag indicating whether the process instance has ended or not. Deprecated: will always be false!  # noqa: E501

        :return: The ended of this ProcessInstanceDtoAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._ended

    @ended.setter
    def ended(self, ended):
        """Sets the ended of this ProcessInstanceDtoAllOf.

        A flag indicating whether the process instance has ended or not. Deprecated: will always be false!  # noqa: E501

        :param ended: The ended of this ProcessInstanceDtoAllOf.  # noqa: E501
        :type: bool
        """

        self._ended = ended

    @property
    def suspended(self):
        """Gets the suspended of this ProcessInstanceDtoAllOf.  # noqa: E501

        A flag indicating whether the process instance is suspended or not.  # noqa: E501

        :return: The suspended of this ProcessInstanceDtoAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._suspended

    @suspended.setter
    def suspended(self, suspended):
        """Sets the suspended of this ProcessInstanceDtoAllOf.

        A flag indicating whether the process instance is suspended or not.  # noqa: E501

        :param suspended: The suspended of this ProcessInstanceDtoAllOf.  # noqa: E501
        :type: bool
        """

        self._suspended = suspended

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ProcessInstanceDtoAllOf.  # noqa: E501

        The tenant id of the process instance.  # noqa: E501

        :return: The tenant_id of this ProcessInstanceDtoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ProcessInstanceDtoAllOf.

        The tenant id of the process instance.  # noqa: E501

        :param tenant_id: The tenant_id of this ProcessInstanceDtoAllOf.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

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
        if not isinstance(other, ProcessInstanceDtoAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProcessInstanceDtoAllOf):
            return True

        return self.to_dict() != other.to_dict()
