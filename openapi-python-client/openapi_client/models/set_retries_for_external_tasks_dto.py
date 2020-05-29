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


class SetRetriesForExternalTasksDto(object):
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
        'retries': 'int',
        'external_task_ids': 'list[str]',
        'process_instance_ids': 'list[str]',
        'external_task_query': 'ExternalTaskQueryDto',
        'process_instance_query': 'ProcessInstanceQueryDto',
        'historic_process_instance_query': 'HistoricProcessInstanceQueryDto'
    }

    attribute_map = {
        'retries': 'retries',
        'external_task_ids': 'externalTaskIds',
        'process_instance_ids': 'processInstanceIds',
        'external_task_query': 'externalTaskQuery',
        'process_instance_query': 'processInstanceQuery',
        'historic_process_instance_query': 'historicProcessInstanceQuery'
    }

    def __init__(self, retries=None, external_task_ids=None, process_instance_ids=None, external_task_query=None, process_instance_query=None, historic_process_instance_query=None, local_vars_configuration=None):  # noqa: E501
        """SetRetriesForExternalTasksDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._retries = None
        self._external_task_ids = None
        self._process_instance_ids = None
        self._external_task_query = None
        self._process_instance_query = None
        self._historic_process_instance_query = None
        self.discriminator = None

        self.retries = retries
        if external_task_ids is not None:
            self.external_task_ids = external_task_ids
        if process_instance_ids is not None:
            self.process_instance_ids = process_instance_ids
        if external_task_query is not None:
            self.external_task_query = external_task_query
        if process_instance_query is not None:
            self.process_instance_query = process_instance_query
        if historic_process_instance_query is not None:
            self.historic_process_instance_query = historic_process_instance_query

    @property
    def retries(self):
        """Gets the retries of this SetRetriesForExternalTasksDto.  # noqa: E501

        The number of retries to set for the external task.  Must be >= 0. If this is 0, an incident is created and the task cannot be fetched anymore unless the retries are increased again. Can not be null.  # noqa: E501

        :return: The retries of this SetRetriesForExternalTasksDto.  # noqa: E501
        :rtype: int
        """
        return self._retries

    @retries.setter
    def retries(self, retries):
        """Sets the retries of this SetRetriesForExternalTasksDto.

        The number of retries to set for the external task.  Must be >= 0. If this is 0, an incident is created and the task cannot be fetched anymore unless the retries are increased again. Can not be null.  # noqa: E501

        :param retries: The retries of this SetRetriesForExternalTasksDto.  # noqa: E501
        :type: int
        """

        self._retries = retries

    @property
    def external_task_ids(self):
        """Gets the external_task_ids of this SetRetriesForExternalTasksDto.  # noqa: E501

        The ids of the external tasks to set the number of retries for.  # noqa: E501

        :return: The external_task_ids of this SetRetriesForExternalTasksDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._external_task_ids

    @external_task_ids.setter
    def external_task_ids(self, external_task_ids):
        """Sets the external_task_ids of this SetRetriesForExternalTasksDto.

        The ids of the external tasks to set the number of retries for.  # noqa: E501

        :param external_task_ids: The external_task_ids of this SetRetriesForExternalTasksDto.  # noqa: E501
        :type: list[str]
        """

        self._external_task_ids = external_task_ids

    @property
    def process_instance_ids(self):
        """Gets the process_instance_ids of this SetRetriesForExternalTasksDto.  # noqa: E501

        The ids of process instances containing the tasks to set the number of retries for.  # noqa: E501

        :return: The process_instance_ids of this SetRetriesForExternalTasksDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._process_instance_ids

    @process_instance_ids.setter
    def process_instance_ids(self, process_instance_ids):
        """Sets the process_instance_ids of this SetRetriesForExternalTasksDto.

        The ids of process instances containing the tasks to set the number of retries for.  # noqa: E501

        :param process_instance_ids: The process_instance_ids of this SetRetriesForExternalTasksDto.  # noqa: E501
        :type: list[str]
        """

        self._process_instance_ids = process_instance_ids

    @property
    def external_task_query(self):
        """Gets the external_task_query of this SetRetriesForExternalTasksDto.  # noqa: E501


        :return: The external_task_query of this SetRetriesForExternalTasksDto.  # noqa: E501
        :rtype: ExternalTaskQueryDto
        """
        return self._external_task_query

    @external_task_query.setter
    def external_task_query(self, external_task_query):
        """Sets the external_task_query of this SetRetriesForExternalTasksDto.


        :param external_task_query: The external_task_query of this SetRetriesForExternalTasksDto.  # noqa: E501
        :type: ExternalTaskQueryDto
        """

        self._external_task_query = external_task_query

    @property
    def process_instance_query(self):
        """Gets the process_instance_query of this SetRetriesForExternalTasksDto.  # noqa: E501


        :return: The process_instance_query of this SetRetriesForExternalTasksDto.  # noqa: E501
        :rtype: ProcessInstanceQueryDto
        """
        return self._process_instance_query

    @process_instance_query.setter
    def process_instance_query(self, process_instance_query):
        """Sets the process_instance_query of this SetRetriesForExternalTasksDto.


        :param process_instance_query: The process_instance_query of this SetRetriesForExternalTasksDto.  # noqa: E501
        :type: ProcessInstanceQueryDto
        """

        self._process_instance_query = process_instance_query

    @property
    def historic_process_instance_query(self):
        """Gets the historic_process_instance_query of this SetRetriesForExternalTasksDto.  # noqa: E501


        :return: The historic_process_instance_query of this SetRetriesForExternalTasksDto.  # noqa: E501
        :rtype: HistoricProcessInstanceQueryDto
        """
        return self._historic_process_instance_query

    @historic_process_instance_query.setter
    def historic_process_instance_query(self, historic_process_instance_query):
        """Sets the historic_process_instance_query of this SetRetriesForExternalTasksDto.


        :param historic_process_instance_query: The historic_process_instance_query of this SetRetriesForExternalTasksDto.  # noqa: E501
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
        if not isinstance(other, SetRetriesForExternalTasksDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SetRetriesForExternalTasksDto):
            return True

        return self.to_dict() != other.to_dict()