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


class ProcessInstanceSuspensionStateDto(object):
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
        'suspended': 'bool',
        'process_definition_id': 'str',
        'process_definition_key': 'str',
        'process_definition_tenant_id': 'str',
        'process_definition_without_tenant_id': 'bool',
        'process_instance_ids': 'list[str]',
        'process_instance_query': 'ProcessInstanceQueryDto',
        'historic_process_instance_query': 'HistoricProcessInstanceQueryDto'
    }

    attribute_map = {
        'suspended': 'suspended',
        'process_definition_id': 'processDefinitionId',
        'process_definition_key': 'processDefinitionKey',
        'process_definition_tenant_id': 'processDefinitionTenantId',
        'process_definition_without_tenant_id': 'processDefinitionWithoutTenantId',
        'process_instance_ids': 'processInstanceIds',
        'process_instance_query': 'processInstanceQuery',
        'historic_process_instance_query': 'historicProcessInstanceQuery'
    }

    def __init__(self, suspended=None, process_definition_id=None, process_definition_key=None, process_definition_tenant_id=None, process_definition_without_tenant_id=None, process_instance_ids=None, process_instance_query=None, historic_process_instance_query=None, local_vars_configuration=None):  # noqa: E501
        """ProcessInstanceSuspensionStateDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._suspended = None
        self._process_definition_id = None
        self._process_definition_key = None
        self._process_definition_tenant_id = None
        self._process_definition_without_tenant_id = None
        self._process_instance_ids = None
        self._process_instance_query = None
        self._historic_process_instance_query = None
        self.discriminator = None

        self.suspended = suspended
        if process_definition_id is not None:
            self.process_definition_id = process_definition_id
        if process_definition_key is not None:
            self.process_definition_key = process_definition_key
        if process_definition_tenant_id is not None:
            self.process_definition_tenant_id = process_definition_tenant_id
        self.process_definition_without_tenant_id = process_definition_without_tenant_id
        if process_instance_ids is not None:
            self.process_instance_ids = process_instance_ids
        if process_instance_query is not None:
            self.process_instance_query = process_instance_query
        if historic_process_instance_query is not None:
            self.historic_process_instance_query = historic_process_instance_query

    @property
    def suspended(self):
        """Gets the suspended of this ProcessInstanceSuspensionStateDto.  # noqa: E501

        A `Boolean` value which indicates whether to activate or suspend a given process instance. When the value is set to `true`, the given process instance will be suspended and when the value is set to `false`, the given process instance will be activated.  # noqa: E501

        :return: The suspended of this ProcessInstanceSuspensionStateDto.  # noqa: E501
        :rtype: bool
        """
        return self._suspended

    @suspended.setter
    def suspended(self, suspended):
        """Sets the suspended of this ProcessInstanceSuspensionStateDto.

        A `Boolean` value which indicates whether to activate or suspend a given process instance. When the value is set to `true`, the given process instance will be suspended and when the value is set to `false`, the given process instance will be activated.  # noqa: E501

        :param suspended: The suspended of this ProcessInstanceSuspensionStateDto.  # noqa: E501
        :type: bool
        """

        self._suspended = suspended

    @property
    def process_definition_id(self):
        """Gets the process_definition_id of this ProcessInstanceSuspensionStateDto.  # noqa: E501

        The process definition id of the process instances to activate or suspend.  **Note**: This parameter can be used only with combination of `suspended`.  # noqa: E501

        :return: The process_definition_id of this ProcessInstanceSuspensionStateDto.  # noqa: E501
        :rtype: str
        """
        return self._process_definition_id

    @process_definition_id.setter
    def process_definition_id(self, process_definition_id):
        """Sets the process_definition_id of this ProcessInstanceSuspensionStateDto.

        The process definition id of the process instances to activate or suspend.  **Note**: This parameter can be used only with combination of `suspended`.  # noqa: E501

        :param process_definition_id: The process_definition_id of this ProcessInstanceSuspensionStateDto.  # noqa: E501
        :type: str
        """

        self._process_definition_id = process_definition_id

    @property
    def process_definition_key(self):
        """Gets the process_definition_key of this ProcessInstanceSuspensionStateDto.  # noqa: E501

        The process definition key of the process instances to activate or suspend.  **Note**: This parameter can be used only with combination of `suspended`, `processDefinitionTenantId`, and `processDefinitionWithoutTenantId`.  # noqa: E501

        :return: The process_definition_key of this ProcessInstanceSuspensionStateDto.  # noqa: E501
        :rtype: str
        """
        return self._process_definition_key

    @process_definition_key.setter
    def process_definition_key(self, process_definition_key):
        """Sets the process_definition_key of this ProcessInstanceSuspensionStateDto.

        The process definition key of the process instances to activate or suspend.  **Note**: This parameter can be used only with combination of `suspended`, `processDefinitionTenantId`, and `processDefinitionWithoutTenantId`.  # noqa: E501

        :param process_definition_key: The process_definition_key of this ProcessInstanceSuspensionStateDto.  # noqa: E501
        :type: str
        """

        self._process_definition_key = process_definition_key

    @property
    def process_definition_tenant_id(self):
        """Gets the process_definition_tenant_id of this ProcessInstanceSuspensionStateDto.  # noqa: E501

        Only activate or suspend process instances of a process definition which belongs to a tenant with the given id.  **Note**: This parameter can be used only with combination of `suspended`, `processDefinitionKey`, and `processDefinitionWithoutTenantId`.  # noqa: E501

        :return: The process_definition_tenant_id of this ProcessInstanceSuspensionStateDto.  # noqa: E501
        :rtype: str
        """
        return self._process_definition_tenant_id

    @process_definition_tenant_id.setter
    def process_definition_tenant_id(self, process_definition_tenant_id):
        """Sets the process_definition_tenant_id of this ProcessInstanceSuspensionStateDto.

        Only activate or suspend process instances of a process definition which belongs to a tenant with the given id.  **Note**: This parameter can be used only with combination of `suspended`, `processDefinitionKey`, and `processDefinitionWithoutTenantId`.  # noqa: E501

        :param process_definition_tenant_id: The process_definition_tenant_id of this ProcessInstanceSuspensionStateDto.  # noqa: E501
        :type: str
        """

        self._process_definition_tenant_id = process_definition_tenant_id

    @property
    def process_definition_without_tenant_id(self):
        """Gets the process_definition_without_tenant_id of this ProcessInstanceSuspensionStateDto.  # noqa: E501

        Only activate or suspend process instances of a process definition which belongs to no tenant. Value may only be true, as false is the default behavior.  **Note**: This parameter can be used only with combination of `suspended`, `processDefinitionKey`, and `processDefinitionTenantId`.  # noqa: E501

        :return: The process_definition_without_tenant_id of this ProcessInstanceSuspensionStateDto.  # noqa: E501
        :rtype: bool
        """
        return self._process_definition_without_tenant_id

    @process_definition_without_tenant_id.setter
    def process_definition_without_tenant_id(self, process_definition_without_tenant_id):
        """Sets the process_definition_without_tenant_id of this ProcessInstanceSuspensionStateDto.

        Only activate or suspend process instances of a process definition which belongs to no tenant. Value may only be true, as false is the default behavior.  **Note**: This parameter can be used only with combination of `suspended`, `processDefinitionKey`, and `processDefinitionTenantId`.  # noqa: E501

        :param process_definition_without_tenant_id: The process_definition_without_tenant_id of this ProcessInstanceSuspensionStateDto.  # noqa: E501
        :type: bool
        """

        self._process_definition_without_tenant_id = process_definition_without_tenant_id

    @property
    def process_instance_ids(self):
        """Gets the process_instance_ids of this ProcessInstanceSuspensionStateDto.  # noqa: E501

        A list of process instance ids which defines a group of process instances which will be activated or suspended by the operation.  **Note**: This parameter can be used only with combination of `suspended`, `processInstanceQuery`, and `historicProcessInstanceQuery`.  # noqa: E501

        :return: The process_instance_ids of this ProcessInstanceSuspensionStateDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._process_instance_ids

    @process_instance_ids.setter
    def process_instance_ids(self, process_instance_ids):
        """Sets the process_instance_ids of this ProcessInstanceSuspensionStateDto.

        A list of process instance ids which defines a group of process instances which will be activated or suspended by the operation.  **Note**: This parameter can be used only with combination of `suspended`, `processInstanceQuery`, and `historicProcessInstanceQuery`.  # noqa: E501

        :param process_instance_ids: The process_instance_ids of this ProcessInstanceSuspensionStateDto.  # noqa: E501
        :type: list[str]
        """

        self._process_instance_ids = process_instance_ids

    @property
    def process_instance_query(self):
        """Gets the process_instance_query of this ProcessInstanceSuspensionStateDto.  # noqa: E501


        :return: The process_instance_query of this ProcessInstanceSuspensionStateDto.  # noqa: E501
        :rtype: ProcessInstanceQueryDto
        """
        return self._process_instance_query

    @process_instance_query.setter
    def process_instance_query(self, process_instance_query):
        """Sets the process_instance_query of this ProcessInstanceSuspensionStateDto.


        :param process_instance_query: The process_instance_query of this ProcessInstanceSuspensionStateDto.  # noqa: E501
        :type: ProcessInstanceQueryDto
        """

        self._process_instance_query = process_instance_query

    @property
    def historic_process_instance_query(self):
        """Gets the historic_process_instance_query of this ProcessInstanceSuspensionStateDto.  # noqa: E501


        :return: The historic_process_instance_query of this ProcessInstanceSuspensionStateDto.  # noqa: E501
        :rtype: HistoricProcessInstanceQueryDto
        """
        return self._historic_process_instance_query

    @historic_process_instance_query.setter
    def historic_process_instance_query(self, historic_process_instance_query):
        """Sets the historic_process_instance_query of this ProcessInstanceSuspensionStateDto.


        :param historic_process_instance_query: The historic_process_instance_query of this ProcessInstanceSuspensionStateDto.  # noqa: E501
        :type: HistoricProcessInstanceQueryDto
        """

        self._historic_process_instance_query = historic_process_instance_query

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
        if not isinstance(other, ProcessInstanceSuspensionStateDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProcessInstanceSuspensionStateDto):
            return True

        return self.to_dict() != other.to_dict()
