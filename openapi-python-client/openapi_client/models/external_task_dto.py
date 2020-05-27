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


class ExternalTaskDto(object):
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
        'activity_id': 'str',
        'activity_instance_id': 'str',
        'error_message': 'str',
        'execution_id': 'str',
        'id': 'str',
        'lock_expiration_time': 'datetime',
        'process_definition_id': 'str',
        'process_definition_key': 'str',
        'process_definition_version_tag': 'str',
        'process_instance_id': 'str',
        'tenant_id': 'str',
        'retries': 'int',
        'suspended': 'bool',
        'worker_id': 'str',
        'topic_name': 'str',
        'priority': 'int',
        'business_key': 'str'
    }

    attribute_map = {
        'activity_id': 'activityId',
        'activity_instance_id': 'activityInstanceId',
        'error_message': 'errorMessage',
        'execution_id': 'executionId',
        'id': 'id',
        'lock_expiration_time': 'lockExpirationTime',
        'process_definition_id': 'processDefinitionId',
        'process_definition_key': 'processDefinitionKey',
        'process_definition_version_tag': 'processDefinitionVersionTag',
        'process_instance_id': 'processInstanceId',
        'tenant_id': 'tenantId',
        'retries': 'retries',
        'suspended': 'suspended',
        'worker_id': 'workerId',
        'topic_name': 'topicName',
        'priority': 'priority',
        'business_key': 'businessKey'
    }

    def __init__(self, activity_id=None, activity_instance_id=None, error_message=None, execution_id=None, id=None, lock_expiration_time=None, process_definition_id=None, process_definition_key=None, process_definition_version_tag=None, process_instance_id=None, tenant_id=None, retries=None, suspended=None, worker_id=None, topic_name=None, priority=None, business_key=None, local_vars_configuration=None):  # noqa: E501
        """ExternalTaskDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._activity_id = None
        self._activity_instance_id = None
        self._error_message = None
        self._execution_id = None
        self._id = None
        self._lock_expiration_time = None
        self._process_definition_id = None
        self._process_definition_key = None
        self._process_definition_version_tag = None
        self._process_instance_id = None
        self._tenant_id = None
        self._retries = None
        self._suspended = None
        self._worker_id = None
        self._topic_name = None
        self._priority = None
        self._business_key = None
        self.discriminator = None

        if activity_id is not None:
            self.activity_id = activity_id
        if activity_instance_id is not None:
            self.activity_instance_id = activity_instance_id
        if error_message is not None:
            self.error_message = error_message
        if execution_id is not None:
            self.execution_id = execution_id
        if id is not None:
            self.id = id
        self.lock_expiration_time = lock_expiration_time
        if process_definition_id is not None:
            self.process_definition_id = process_definition_id
        if process_definition_key is not None:
            self.process_definition_key = process_definition_key
        if process_definition_version_tag is not None:
            self.process_definition_version_tag = process_definition_version_tag
        if process_instance_id is not None:
            self.process_instance_id = process_instance_id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        self.retries = retries
        self.suspended = suspended
        if worker_id is not None:
            self.worker_id = worker_id
        if topic_name is not None:
            self.topic_name = topic_name
        self.priority = priority
        if business_key is not None:
            self.business_key = business_key

    @property
    def activity_id(self):
        """Gets the activity_id of this ExternalTaskDto.  # noqa: E501

        The id of the activity that this external task belongs to.  # noqa: E501

        :return: The activity_id of this ExternalTaskDto.  # noqa: E501
        :rtype: str
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """Sets the activity_id of this ExternalTaskDto.

        The id of the activity that this external task belongs to.  # noqa: E501

        :param activity_id: The activity_id of this ExternalTaskDto.  # noqa: E501
        :type: str
        """

        self._activity_id = activity_id

    @property
    def activity_instance_id(self):
        """Gets the activity_instance_id of this ExternalTaskDto.  # noqa: E501

        The id of the activity instance that the external task belongs to.  # noqa: E501

        :return: The activity_instance_id of this ExternalTaskDto.  # noqa: E501
        :rtype: str
        """
        return self._activity_instance_id

    @activity_instance_id.setter
    def activity_instance_id(self, activity_instance_id):
        """Sets the activity_instance_id of this ExternalTaskDto.

        The id of the activity instance that the external task belongs to.  # noqa: E501

        :param activity_instance_id: The activity_instance_id of this ExternalTaskDto.  # noqa: E501
        :type: str
        """

        self._activity_instance_id = activity_instance_id

    @property
    def error_message(self):
        """Gets the error_message of this ExternalTaskDto.  # noqa: E501

        The full error message submitted with the latest reported failure executing this task; `null` if no failure was reported previously or if no error message was submitted  # noqa: E501

        :return: The error_message of this ExternalTaskDto.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this ExternalTaskDto.

        The full error message submitted with the latest reported failure executing this task; `null` if no failure was reported previously or if no error message was submitted  # noqa: E501

        :param error_message: The error_message of this ExternalTaskDto.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def execution_id(self):
        """Gets the execution_id of this ExternalTaskDto.  # noqa: E501

        The id of the execution that the external task belongs to.  # noqa: E501

        :return: The execution_id of this ExternalTaskDto.  # noqa: E501
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        """Sets the execution_id of this ExternalTaskDto.

        The id of the execution that the external task belongs to.  # noqa: E501

        :param execution_id: The execution_id of this ExternalTaskDto.  # noqa: E501
        :type: str
        """

        self._execution_id = execution_id

    @property
    def id(self):
        """Gets the id of this ExternalTaskDto.  # noqa: E501

        The id of the external task.  # noqa: E501

        :return: The id of this ExternalTaskDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExternalTaskDto.

        The id of the external task.  # noqa: E501

        :param id: The id of this ExternalTaskDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def lock_expiration_time(self):
        """Gets the lock_expiration_time of this ExternalTaskDto.  # noqa: E501

        The date that the task's most recent lock expires or has expired.  # noqa: E501

        :return: The lock_expiration_time of this ExternalTaskDto.  # noqa: E501
        :rtype: datetime
        """
        return self._lock_expiration_time

    @lock_expiration_time.setter
    def lock_expiration_time(self, lock_expiration_time):
        """Sets the lock_expiration_time of this ExternalTaskDto.

        The date that the task's most recent lock expires or has expired.  # noqa: E501

        :param lock_expiration_time: The lock_expiration_time of this ExternalTaskDto.  # noqa: E501
        :type: datetime
        """

        self._lock_expiration_time = lock_expiration_time

    @property
    def process_definition_id(self):
        """Gets the process_definition_id of this ExternalTaskDto.  # noqa: E501

        The id of the process definition the external task is defined in.  # noqa: E501

        :return: The process_definition_id of this ExternalTaskDto.  # noqa: E501
        :rtype: str
        """
        return self._process_definition_id

    @process_definition_id.setter
    def process_definition_id(self, process_definition_id):
        """Sets the process_definition_id of this ExternalTaskDto.

        The id of the process definition the external task is defined in.  # noqa: E501

        :param process_definition_id: The process_definition_id of this ExternalTaskDto.  # noqa: E501
        :type: str
        """

        self._process_definition_id = process_definition_id

    @property
    def process_definition_key(self):
        """Gets the process_definition_key of this ExternalTaskDto.  # noqa: E501

        The key of the process definition the external task is defined in.  # noqa: E501

        :return: The process_definition_key of this ExternalTaskDto.  # noqa: E501
        :rtype: str
        """
        return self._process_definition_key

    @process_definition_key.setter
    def process_definition_key(self, process_definition_key):
        """Sets the process_definition_key of this ExternalTaskDto.

        The key of the process definition the external task is defined in.  # noqa: E501

        :param process_definition_key: The process_definition_key of this ExternalTaskDto.  # noqa: E501
        :type: str
        """

        self._process_definition_key = process_definition_key

    @property
    def process_definition_version_tag(self):
        """Gets the process_definition_version_tag of this ExternalTaskDto.  # noqa: E501

        The version tag of the process definition the external task is defined in.  # noqa: E501

        :return: The process_definition_version_tag of this ExternalTaskDto.  # noqa: E501
        :rtype: str
        """
        return self._process_definition_version_tag

    @process_definition_version_tag.setter
    def process_definition_version_tag(self, process_definition_version_tag):
        """Sets the process_definition_version_tag of this ExternalTaskDto.

        The version tag of the process definition the external task is defined in.  # noqa: E501

        :param process_definition_version_tag: The process_definition_version_tag of this ExternalTaskDto.  # noqa: E501
        :type: str
        """

        self._process_definition_version_tag = process_definition_version_tag

    @property
    def process_instance_id(self):
        """Gets the process_instance_id of this ExternalTaskDto.  # noqa: E501

        The id of the process instance the external task belongs to.  # noqa: E501

        :return: The process_instance_id of this ExternalTaskDto.  # noqa: E501
        :rtype: str
        """
        return self._process_instance_id

    @process_instance_id.setter
    def process_instance_id(self, process_instance_id):
        """Sets the process_instance_id of this ExternalTaskDto.

        The id of the process instance the external task belongs to.  # noqa: E501

        :param process_instance_id: The process_instance_id of this ExternalTaskDto.  # noqa: E501
        :type: str
        """

        self._process_instance_id = process_instance_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ExternalTaskDto.  # noqa: E501

        The id of the tenant the external task belongs to.  # noqa: E501

        :return: The tenant_id of this ExternalTaskDto.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ExternalTaskDto.

        The id of the tenant the external task belongs to.  # noqa: E501

        :param tenant_id: The tenant_id of this ExternalTaskDto.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def retries(self):
        """Gets the retries of this ExternalTaskDto.  # noqa: E501

        The number of retries the task currently has left.  # noqa: E501

        :return: The retries of this ExternalTaskDto.  # noqa: E501
        :rtype: int
        """
        return self._retries

    @retries.setter
    def retries(self, retries):
        """Sets the retries of this ExternalTaskDto.

        The number of retries the task currently has left.  # noqa: E501

        :param retries: The retries of this ExternalTaskDto.  # noqa: E501
        :type: int
        """

        self._retries = retries

    @property
    def suspended(self):
        """Gets the suspended of this ExternalTaskDto.  # noqa: E501

        A flag indicating whether the external task is suspended or not.  # noqa: E501

        :return: The suspended of this ExternalTaskDto.  # noqa: E501
        :rtype: bool
        """
        return self._suspended

    @suspended.setter
    def suspended(self, suspended):
        """Sets the suspended of this ExternalTaskDto.

        A flag indicating whether the external task is suspended or not.  # noqa: E501

        :param suspended: The suspended of this ExternalTaskDto.  # noqa: E501
        :type: bool
        """

        self._suspended = suspended

    @property
    def worker_id(self):
        """Gets the worker_id of this ExternalTaskDto.  # noqa: E501

        The id of the worker that posesses or posessed the most recent lock.  # noqa: E501

        :return: The worker_id of this ExternalTaskDto.  # noqa: E501
        :rtype: str
        """
        return self._worker_id

    @worker_id.setter
    def worker_id(self, worker_id):
        """Sets the worker_id of this ExternalTaskDto.

        The id of the worker that posesses or posessed the most recent lock.  # noqa: E501

        :param worker_id: The worker_id of this ExternalTaskDto.  # noqa: E501
        :type: str
        """

        self._worker_id = worker_id

    @property
    def topic_name(self):
        """Gets the topic_name of this ExternalTaskDto.  # noqa: E501

        The topic name of the external task.  # noqa: E501

        :return: The topic_name of this ExternalTaskDto.  # noqa: E501
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        """Sets the topic_name of this ExternalTaskDto.

        The topic name of the external task.  # noqa: E501

        :param topic_name: The topic_name of this ExternalTaskDto.  # noqa: E501
        :type: str
        """

        self._topic_name = topic_name

    @property
    def priority(self):
        """Gets the priority of this ExternalTaskDto.  # noqa: E501

        The priority of the external task.  # noqa: E501

        :return: The priority of this ExternalTaskDto.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this ExternalTaskDto.

        The priority of the external task.  # noqa: E501

        :param priority: The priority of this ExternalTaskDto.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def business_key(self):
        """Gets the business_key of this ExternalTaskDto.  # noqa: E501

        The business key of the process instance the external task belongs to.  # noqa: E501

        :return: The business_key of this ExternalTaskDto.  # noqa: E501
        :rtype: str
        """
        return self._business_key

    @business_key.setter
    def business_key(self, business_key):
        """Sets the business_key of this ExternalTaskDto.

        The business key of the process instance the external task belongs to.  # noqa: E501

        :param business_key: The business_key of this ExternalTaskDto.  # noqa: E501
        :type: str
        """

        self._business_key = business_key

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
        if not isinstance(other, ExternalTaskDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExternalTaskDto):
            return True

        return self.to_dict() != other.to_dict()
