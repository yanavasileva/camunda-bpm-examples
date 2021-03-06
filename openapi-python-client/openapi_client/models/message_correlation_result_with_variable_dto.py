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


class MessageCorrelationResultWithVariableDto(object):
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
        'result_type': 'str',
        'process_instance': 'ProcessInstanceDto',
        'execution': 'ExecutionDto',
        'variables': 'dict(str, VariableValueDto)'
    }

    attribute_map = {
        'result_type': 'resultType',
        'process_instance': 'processInstance',
        'execution': 'execution',
        'variables': 'variables'
    }

    def __init__(self, result_type=None, process_instance=None, execution=None, variables=None, local_vars_configuration=None):  # noqa: E501
        """MessageCorrelationResultWithVariableDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._result_type = None
        self._process_instance = None
        self._execution = None
        self._variables = None
        self.discriminator = None

        if result_type is not None:
            self.result_type = result_type
        if process_instance is not None:
            self.process_instance = process_instance
        if execution is not None:
            self.execution = execution
        if variables is not None:
            self.variables = variables

    @property
    def result_type(self):
        """Gets the result_type of this MessageCorrelationResultWithVariableDto.  # noqa: E501

        Indicates if the message was correlated to a message start event or an  intermediate message catching event. In the first case, the resultType is  `ProcessDefinition` and otherwise `Execution`.  # noqa: E501

        :return: The result_type of this MessageCorrelationResultWithVariableDto.  # noqa: E501
        :rtype: str
        """
        return self._result_type

    @result_type.setter
    def result_type(self, result_type):
        """Sets the result_type of this MessageCorrelationResultWithVariableDto.

        Indicates if the message was correlated to a message start event or an  intermediate message catching event. In the first case, the resultType is  `ProcessDefinition` and otherwise `Execution`.  # noqa: E501

        :param result_type: The result_type of this MessageCorrelationResultWithVariableDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["Execution", "ProcessDefinition"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and result_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `result_type` ({0}), must be one of {1}"  # noqa: E501
                .format(result_type, allowed_values)
            )

        self._result_type = result_type

    @property
    def process_instance(self):
        """Gets the process_instance of this MessageCorrelationResultWithVariableDto.  # noqa: E501


        :return: The process_instance of this MessageCorrelationResultWithVariableDto.  # noqa: E501
        :rtype: ProcessInstanceDto
        """
        return self._process_instance

    @process_instance.setter
    def process_instance(self, process_instance):
        """Sets the process_instance of this MessageCorrelationResultWithVariableDto.


        :param process_instance: The process_instance of this MessageCorrelationResultWithVariableDto.  # noqa: E501
        :type: ProcessInstanceDto
        """

        self._process_instance = process_instance

    @property
    def execution(self):
        """Gets the execution of this MessageCorrelationResultWithVariableDto.  # noqa: E501


        :return: The execution of this MessageCorrelationResultWithVariableDto.  # noqa: E501
        :rtype: ExecutionDto
        """
        return self._execution

    @execution.setter
    def execution(self, execution):
        """Sets the execution of this MessageCorrelationResultWithVariableDto.


        :param execution: The execution of this MessageCorrelationResultWithVariableDto.  # noqa: E501
        :type: ExecutionDto
        """

        self._execution = execution

    @property
    def variables(self):
        """Gets the variables of this MessageCorrelationResultWithVariableDto.  # noqa: E501

        This property is returned if the `variablesInResultEnabled` is set to `true`. Contains a list of the process variables.   # noqa: E501

        :return: The variables of this MessageCorrelationResultWithVariableDto.  # noqa: E501
        :rtype: dict(str, VariableValueDto)
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this MessageCorrelationResultWithVariableDto.

        This property is returned if the `variablesInResultEnabled` is set to `true`. Contains a list of the process variables.   # noqa: E501

        :param variables: The variables of this MessageCorrelationResultWithVariableDto.  # noqa: E501
        :type: dict(str, VariableValueDto)
        """

        self._variables = variables

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
        if not isinstance(other, MessageCorrelationResultWithVariableDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MessageCorrelationResultWithVariableDto):
            return True

        return self.to_dict() != other.to_dict()
