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


class ExternalTaskQueryDto(object):
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
        'external_task_id': 'str',
        'external_task_id_in': 'list[str]',
        'topic_name': 'str',
        'worker_id': 'str',
        'locked': 'bool',
        'not_locked': 'bool',
        'with_retries_left': 'bool',
        'no_retries_left': 'bool',
        'lock_expiration_after': 'datetime',
        'lock_expiration_before': 'datetime',
        'activity_id': 'str',
        'activity_id_in': 'list[str]',
        'execution_id': 'str',
        'process_instance_id': 'str',
        'process_instance_id_in': 'list[str]',
        'process_definition_id': 'str',
        'tenant_id_in': 'list[str]',
        'active': 'bool',
        'suspended': 'bool',
        'priority_higher_than_or_equals': 'int',
        'priority_lower_than_or_equals': 'int',
        'sorting': 'list[ExternalTaskQueryDtoSorting]'
    }

    attribute_map = {
        'external_task_id': 'externalTaskId',
        'external_task_id_in': 'externalTaskIdIn',
        'topic_name': 'topicName',
        'worker_id': 'workerId',
        'locked': 'locked',
        'not_locked': 'notLocked',
        'with_retries_left': 'withRetriesLeft',
        'no_retries_left': 'noRetriesLeft',
        'lock_expiration_after': 'lockExpirationAfter',
        'lock_expiration_before': 'lockExpirationBefore',
        'activity_id': 'activityId',
        'activity_id_in': 'activityIdIn',
        'execution_id': 'executionId',
        'process_instance_id': 'processInstanceId',
        'process_instance_id_in': 'processInstanceIdIn',
        'process_definition_id': 'processDefinitionId',
        'tenant_id_in': 'tenantIdIn',
        'active': 'active',
        'suspended': 'suspended',
        'priority_higher_than_or_equals': 'priorityHigherThanOrEquals',
        'priority_lower_than_or_equals': 'priorityLowerThanOrEquals',
        'sorting': 'sorting'
    }

    def __init__(self, external_task_id=None, external_task_id_in=None, topic_name=None, worker_id=None, locked=None, not_locked=None, with_retries_left=None, no_retries_left=None, lock_expiration_after=None, lock_expiration_before=None, activity_id=None, activity_id_in=None, execution_id=None, process_instance_id=None, process_instance_id_in=None, process_definition_id=None, tenant_id_in=None, active=None, suspended=None, priority_higher_than_or_equals=None, priority_lower_than_or_equals=None, sorting=None, local_vars_configuration=None):  # noqa: E501
        """ExternalTaskQueryDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._external_task_id = None
        self._external_task_id_in = None
        self._topic_name = None
        self._worker_id = None
        self._locked = None
        self._not_locked = None
        self._with_retries_left = None
        self._no_retries_left = None
        self._lock_expiration_after = None
        self._lock_expiration_before = None
        self._activity_id = None
        self._activity_id_in = None
        self._execution_id = None
        self._process_instance_id = None
        self._process_instance_id_in = None
        self._process_definition_id = None
        self._tenant_id_in = None
        self._active = None
        self._suspended = None
        self._priority_higher_than_or_equals = None
        self._priority_lower_than_or_equals = None
        self._sorting = None
        self.discriminator = None

        if external_task_id is not None:
            self.external_task_id = external_task_id
        if external_task_id_in is not None:
            self.external_task_id_in = external_task_id_in
        if topic_name is not None:
            self.topic_name = topic_name
        if worker_id is not None:
            self.worker_id = worker_id
        self.locked = locked
        self.not_locked = not_locked
        self.with_retries_left = with_retries_left
        self.no_retries_left = no_retries_left
        self.lock_expiration_after = lock_expiration_after
        self.lock_expiration_before = lock_expiration_before
        if activity_id is not None:
            self.activity_id = activity_id
        if activity_id_in is not None:
            self.activity_id_in = activity_id_in
        if execution_id is not None:
            self.execution_id = execution_id
        if process_instance_id is not None:
            self.process_instance_id = process_instance_id
        if process_instance_id_in is not None:
            self.process_instance_id_in = process_instance_id_in
        if process_definition_id is not None:
            self.process_definition_id = process_definition_id
        if tenant_id_in is not None:
            self.tenant_id_in = tenant_id_in
        self.active = active
        self.suspended = suspended
        self.priority_higher_than_or_equals = priority_higher_than_or_equals
        self.priority_lower_than_or_equals = priority_lower_than_or_equals
        if sorting is not None:
            self.sorting = sorting

    @property
    def external_task_id(self):
        """Gets the external_task_id of this ExternalTaskQueryDto.  # noqa: E501

        Filter by an external task's id.  # noqa: E501

        :return: The external_task_id of this ExternalTaskQueryDto.  # noqa: E501
        :rtype: str
        """
        return self._external_task_id

    @external_task_id.setter
    def external_task_id(self, external_task_id):
        """Sets the external_task_id of this ExternalTaskQueryDto.

        Filter by an external task's id.  # noqa: E501

        :param external_task_id: The external_task_id of this ExternalTaskQueryDto.  # noqa: E501
        :type: str
        """

        self._external_task_id = external_task_id

    @property
    def external_task_id_in(self):
        """Gets the external_task_id_in of this ExternalTaskQueryDto.  # noqa: E501

        Filter by the comma-separated list of external task ids.  # noqa: E501

        :return: The external_task_id_in of this ExternalTaskQueryDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._external_task_id_in

    @external_task_id_in.setter
    def external_task_id_in(self, external_task_id_in):
        """Sets the external_task_id_in of this ExternalTaskQueryDto.

        Filter by the comma-separated list of external task ids.  # noqa: E501

        :param external_task_id_in: The external_task_id_in of this ExternalTaskQueryDto.  # noqa: E501
        :type: list[str]
        """

        self._external_task_id_in = external_task_id_in

    @property
    def topic_name(self):
        """Gets the topic_name of this ExternalTaskQueryDto.  # noqa: E501

        Filter by an external task topic.  # noqa: E501

        :return: The topic_name of this ExternalTaskQueryDto.  # noqa: E501
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        """Sets the topic_name of this ExternalTaskQueryDto.

        Filter by an external task topic.  # noqa: E501

        :param topic_name: The topic_name of this ExternalTaskQueryDto.  # noqa: E501
        :type: str
        """

        self._topic_name = topic_name

    @property
    def worker_id(self):
        """Gets the worker_id of this ExternalTaskQueryDto.  # noqa: E501

        Filter by the id of the worker that the task was most recently locked by.  # noqa: E501

        :return: The worker_id of this ExternalTaskQueryDto.  # noqa: E501
        :rtype: str
        """
        return self._worker_id

    @worker_id.setter
    def worker_id(self, worker_id):
        """Sets the worker_id of this ExternalTaskQueryDto.

        Filter by the id of the worker that the task was most recently locked by.  # noqa: E501

        :param worker_id: The worker_id of this ExternalTaskQueryDto.  # noqa: E501
        :type: str
        """

        self._worker_id = worker_id

    @property
    def locked(self):
        """Gets the locked of this ExternalTaskQueryDto.  # noqa: E501

        Only include external tasks that are currently locked (i.e., they have a lock time and it has not expired). Value may only be `true`, as `false` matches any external task.  # noqa: E501

        :return: The locked of this ExternalTaskQueryDto.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this ExternalTaskQueryDto.

        Only include external tasks that are currently locked (i.e., they have a lock time and it has not expired). Value may only be `true`, as `false` matches any external task.  # noqa: E501

        :param locked: The locked of this ExternalTaskQueryDto.  # noqa: E501
        :type: bool
        """

        self._locked = locked

    @property
    def not_locked(self):
        """Gets the not_locked of this ExternalTaskQueryDto.  # noqa: E501

        Only include external tasks that are currently not locked (i.e., they have no lock or it has expired). Value may only be `true`, as `false` matches any external task.  # noqa: E501

        :return: The not_locked of this ExternalTaskQueryDto.  # noqa: E501
        :rtype: bool
        """
        return self._not_locked

    @not_locked.setter
    def not_locked(self, not_locked):
        """Sets the not_locked of this ExternalTaskQueryDto.

        Only include external tasks that are currently not locked (i.e., they have no lock or it has expired). Value may only be `true`, as `false` matches any external task.  # noqa: E501

        :param not_locked: The not_locked of this ExternalTaskQueryDto.  # noqa: E501
        :type: bool
        """

        self._not_locked = not_locked

    @property
    def with_retries_left(self):
        """Gets the with_retries_left of this ExternalTaskQueryDto.  # noqa: E501

        Only include external tasks that have a positive (&gt; 0) number of retries (or `null`). Value may only be `true`, as `false` matches any external task.  # noqa: E501

        :return: The with_retries_left of this ExternalTaskQueryDto.  # noqa: E501
        :rtype: bool
        """
        return self._with_retries_left

    @with_retries_left.setter
    def with_retries_left(self, with_retries_left):
        """Sets the with_retries_left of this ExternalTaskQueryDto.

        Only include external tasks that have a positive (&gt; 0) number of retries (or `null`). Value may only be `true`, as `false` matches any external task.  # noqa: E501

        :param with_retries_left: The with_retries_left of this ExternalTaskQueryDto.  # noqa: E501
        :type: bool
        """

        self._with_retries_left = with_retries_left

    @property
    def no_retries_left(self):
        """Gets the no_retries_left of this ExternalTaskQueryDto.  # noqa: E501

        Only include external tasks that have 0 retries. Value may only be `true`, as `false` matches any external task.  # noqa: E501

        :return: The no_retries_left of this ExternalTaskQueryDto.  # noqa: E501
        :rtype: bool
        """
        return self._no_retries_left

    @no_retries_left.setter
    def no_retries_left(self, no_retries_left):
        """Sets the no_retries_left of this ExternalTaskQueryDto.

        Only include external tasks that have 0 retries. Value may only be `true`, as `false` matches any external task.  # noqa: E501

        :param no_retries_left: The no_retries_left of this ExternalTaskQueryDto.  # noqa: E501
        :type: bool
        """

        self._no_retries_left = no_retries_left

    @property
    def lock_expiration_after(self):
        """Gets the lock_expiration_after of this ExternalTaskQueryDto.  # noqa: E501

        Restrict to external tasks that have a lock that expires after a given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.000+0200`.  # noqa: E501

        :return: The lock_expiration_after of this ExternalTaskQueryDto.  # noqa: E501
        :rtype: datetime
        """
        return self._lock_expiration_after

    @lock_expiration_after.setter
    def lock_expiration_after(self, lock_expiration_after):
        """Sets the lock_expiration_after of this ExternalTaskQueryDto.

        Restrict to external tasks that have a lock that expires after a given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.000+0200`.  # noqa: E501

        :param lock_expiration_after: The lock_expiration_after of this ExternalTaskQueryDto.  # noqa: E501
        :type: datetime
        """

        self._lock_expiration_after = lock_expiration_after

    @property
    def lock_expiration_before(self):
        """Gets the lock_expiration_before of this ExternalTaskQueryDto.  # noqa: E501

        Restrict to external tasks that have a lock that expires before a given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.000+0200`.  # noqa: E501

        :return: The lock_expiration_before of this ExternalTaskQueryDto.  # noqa: E501
        :rtype: datetime
        """
        return self._lock_expiration_before

    @lock_expiration_before.setter
    def lock_expiration_before(self, lock_expiration_before):
        """Sets the lock_expiration_before of this ExternalTaskQueryDto.

        Restrict to external tasks that have a lock that expires before a given date. By [default](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/), the date must have the format `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, e.g., `2013-01-23T14:42:45.000+0200`.  # noqa: E501

        :param lock_expiration_before: The lock_expiration_before of this ExternalTaskQueryDto.  # noqa: E501
        :type: datetime
        """

        self._lock_expiration_before = lock_expiration_before

    @property
    def activity_id(self):
        """Gets the activity_id of this ExternalTaskQueryDto.  # noqa: E501

        Filter by the id of the activity that an external task is created for.  # noqa: E501

        :return: The activity_id of this ExternalTaskQueryDto.  # noqa: E501
        :rtype: str
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """Sets the activity_id of this ExternalTaskQueryDto.

        Filter by the id of the activity that an external task is created for.  # noqa: E501

        :param activity_id: The activity_id of this ExternalTaskQueryDto.  # noqa: E501
        :type: str
        """

        self._activity_id = activity_id

    @property
    def activity_id_in(self):
        """Gets the activity_id_in of this ExternalTaskQueryDto.  # noqa: E501

        Filter by the comma-separated list of ids of the activities that an external task is created for.  # noqa: E501

        :return: The activity_id_in of this ExternalTaskQueryDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._activity_id_in

    @activity_id_in.setter
    def activity_id_in(self, activity_id_in):
        """Sets the activity_id_in of this ExternalTaskQueryDto.

        Filter by the comma-separated list of ids of the activities that an external task is created for.  # noqa: E501

        :param activity_id_in: The activity_id_in of this ExternalTaskQueryDto.  # noqa: E501
        :type: list[str]
        """

        self._activity_id_in = activity_id_in

    @property
    def execution_id(self):
        """Gets the execution_id of this ExternalTaskQueryDto.  # noqa: E501

        Filter by the id of the execution that an external task belongs to.  # noqa: E501

        :return: The execution_id of this ExternalTaskQueryDto.  # noqa: E501
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        """Sets the execution_id of this ExternalTaskQueryDto.

        Filter by the id of the execution that an external task belongs to.  # noqa: E501

        :param execution_id: The execution_id of this ExternalTaskQueryDto.  # noqa: E501
        :type: str
        """

        self._execution_id = execution_id

    @property
    def process_instance_id(self):
        """Gets the process_instance_id of this ExternalTaskQueryDto.  # noqa: E501

        Filter by the id of the process instance that an external task belongs to.  # noqa: E501

        :return: The process_instance_id of this ExternalTaskQueryDto.  # noqa: E501
        :rtype: str
        """
        return self._process_instance_id

    @process_instance_id.setter
    def process_instance_id(self, process_instance_id):
        """Sets the process_instance_id of this ExternalTaskQueryDto.

        Filter by the id of the process instance that an external task belongs to.  # noqa: E501

        :param process_instance_id: The process_instance_id of this ExternalTaskQueryDto.  # noqa: E501
        :type: str
        """

        self._process_instance_id = process_instance_id

    @property
    def process_instance_id_in(self):
        """Gets the process_instance_id_in of this ExternalTaskQueryDto.  # noqa: E501

        Filter by a comma-separated list of process instance ids that an external task may belong to.  # noqa: E501

        :return: The process_instance_id_in of this ExternalTaskQueryDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._process_instance_id_in

    @process_instance_id_in.setter
    def process_instance_id_in(self, process_instance_id_in):
        """Sets the process_instance_id_in of this ExternalTaskQueryDto.

        Filter by a comma-separated list of process instance ids that an external task may belong to.  # noqa: E501

        :param process_instance_id_in: The process_instance_id_in of this ExternalTaskQueryDto.  # noqa: E501
        :type: list[str]
        """

        self._process_instance_id_in = process_instance_id_in

    @property
    def process_definition_id(self):
        """Gets the process_definition_id of this ExternalTaskQueryDto.  # noqa: E501

        Filter by the id of the process definition that an external task belongs to.  # noqa: E501

        :return: The process_definition_id of this ExternalTaskQueryDto.  # noqa: E501
        :rtype: str
        """
        return self._process_definition_id

    @process_definition_id.setter
    def process_definition_id(self, process_definition_id):
        """Sets the process_definition_id of this ExternalTaskQueryDto.

        Filter by the id of the process definition that an external task belongs to.  # noqa: E501

        :param process_definition_id: The process_definition_id of this ExternalTaskQueryDto.  # noqa: E501
        :type: str
        """

        self._process_definition_id = process_definition_id

    @property
    def tenant_id_in(self):
        """Gets the tenant_id_in of this ExternalTaskQueryDto.  # noqa: E501

        Filter by a comma-separated list of tenant ids. An external task must have one of the given tenant ids.  # noqa: E501

        :return: The tenant_id_in of this ExternalTaskQueryDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._tenant_id_in

    @tenant_id_in.setter
    def tenant_id_in(self, tenant_id_in):
        """Sets the tenant_id_in of this ExternalTaskQueryDto.

        Filter by a comma-separated list of tenant ids. An external task must have one of the given tenant ids.  # noqa: E501

        :param tenant_id_in: The tenant_id_in of this ExternalTaskQueryDto.  # noqa: E501
        :type: list[str]
        """

        self._tenant_id_in = tenant_id_in

    @property
    def active(self):
        """Gets the active of this ExternalTaskQueryDto.  # noqa: E501

        Only include active tasks. Value may only be `true`, as `false` matches any external task.  # noqa: E501

        :return: The active of this ExternalTaskQueryDto.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this ExternalTaskQueryDto.

        Only include active tasks. Value may only be `true`, as `false` matches any external task.  # noqa: E501

        :param active: The active of this ExternalTaskQueryDto.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def suspended(self):
        """Gets the suspended of this ExternalTaskQueryDto.  # noqa: E501

        Only include suspended tasks. Value may only be `true`, as `false` matches any external task.  # noqa: E501

        :return: The suspended of this ExternalTaskQueryDto.  # noqa: E501
        :rtype: bool
        """
        return self._suspended

    @suspended.setter
    def suspended(self, suspended):
        """Sets the suspended of this ExternalTaskQueryDto.

        Only include suspended tasks. Value may only be `true`, as `false` matches any external task.  # noqa: E501

        :param suspended: The suspended of this ExternalTaskQueryDto.  # noqa: E501
        :type: bool
        """

        self._suspended = suspended

    @property
    def priority_higher_than_or_equals(self):
        """Gets the priority_higher_than_or_equals of this ExternalTaskQueryDto.  # noqa: E501

        Only include jobs with a priority higher than or equal to the given value. Value must be a valid `long` value.  # noqa: E501

        :return: The priority_higher_than_or_equals of this ExternalTaskQueryDto.  # noqa: E501
        :rtype: int
        """
        return self._priority_higher_than_or_equals

    @priority_higher_than_or_equals.setter
    def priority_higher_than_or_equals(self, priority_higher_than_or_equals):
        """Sets the priority_higher_than_or_equals of this ExternalTaskQueryDto.

        Only include jobs with a priority higher than or equal to the given value. Value must be a valid `long` value.  # noqa: E501

        :param priority_higher_than_or_equals: The priority_higher_than_or_equals of this ExternalTaskQueryDto.  # noqa: E501
        :type: int
        """

        self._priority_higher_than_or_equals = priority_higher_than_or_equals

    @property
    def priority_lower_than_or_equals(self):
        """Gets the priority_lower_than_or_equals of this ExternalTaskQueryDto.  # noqa: E501

        Only include jobs with a priority lower than or equal to the given value. Value must be a valid `long` value.  # noqa: E501

        :return: The priority_lower_than_or_equals of this ExternalTaskQueryDto.  # noqa: E501
        :rtype: int
        """
        return self._priority_lower_than_or_equals

    @priority_lower_than_or_equals.setter
    def priority_lower_than_or_equals(self, priority_lower_than_or_equals):
        """Sets the priority_lower_than_or_equals of this ExternalTaskQueryDto.

        Only include jobs with a priority lower than or equal to the given value. Value must be a valid `long` value.  # noqa: E501

        :param priority_lower_than_or_equals: The priority_lower_than_or_equals of this ExternalTaskQueryDto.  # noqa: E501
        :type: int
        """

        self._priority_lower_than_or_equals = priority_lower_than_or_equals

    @property
    def sorting(self):
        """Gets the sorting of this ExternalTaskQueryDto.  # noqa: E501

        A JSON array of criteria to sort the result by. Each element of the array is a JSON object that                     specifies one ordering. The position in the array identifies the rank of an ordering, i.e., whether                     it is primary, secondary, etc. The ordering objects have the following properties:                      **Note:** The `sorting` properties will not be applied to the External Task count query.  # noqa: E501

        :return: The sorting of this ExternalTaskQueryDto.  # noqa: E501
        :rtype: list[ExternalTaskQueryDtoSorting]
        """
        return self._sorting

    @sorting.setter
    def sorting(self, sorting):
        """Sets the sorting of this ExternalTaskQueryDto.

        A JSON array of criteria to sort the result by. Each element of the array is a JSON object that                     specifies one ordering. The position in the array identifies the rank of an ordering, i.e., whether                     it is primary, secondary, etc. The ordering objects have the following properties:                      **Note:** The `sorting` properties will not be applied to the External Task count query.  # noqa: E501

        :param sorting: The sorting of this ExternalTaskQueryDto.  # noqa: E501
        :type: list[ExternalTaskQueryDtoSorting]
        """

        self._sorting = sorting

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
        if not isinstance(other, ExternalTaskQueryDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExternalTaskQueryDto):
            return True

        return self.to_dict() != other.to_dict()
