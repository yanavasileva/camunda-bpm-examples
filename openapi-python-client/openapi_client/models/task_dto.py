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


class TaskDto(object):
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
        'name': 'str',
        'assignee': 'str',
        'owner': 'str',
        'created': 'datetime',
        'due': 'datetime',
        'follow_up': 'datetime',
        'delegation_state': 'str',
        'description': 'str',
        'execution_id': 'str',
        'parent_task_id': 'str',
        'priority': 'int',
        'process_definition_id': 'str',
        'process_instance_id': 'str',
        'case_execution_id': 'str',
        'case_definition_id': 'str',
        'case_instance_id': 'str',
        'task_definition_key': 'str',
        'suspended': 'bool',
        'form_key': 'str',
        'tenant_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'assignee': 'assignee',
        'owner': 'owner',
        'created': 'created',
        'due': 'due',
        'follow_up': 'followUp',
        'delegation_state': 'delegationState',
        'description': 'description',
        'execution_id': 'executionId',
        'parent_task_id': 'parentTaskId',
        'priority': 'priority',
        'process_definition_id': 'processDefinitionId',
        'process_instance_id': 'processInstanceId',
        'case_execution_id': 'caseExecutionId',
        'case_definition_id': 'caseDefinitionId',
        'case_instance_id': 'caseInstanceId',
        'task_definition_key': 'taskDefinitionKey',
        'suspended': 'suspended',
        'form_key': 'formKey',
        'tenant_id': 'tenantId'
    }

    def __init__(self, id=None, name=None, assignee=None, owner=None, created=None, due=None, follow_up=None, delegation_state=None, description=None, execution_id=None, parent_task_id=None, priority=None, process_definition_id=None, process_instance_id=None, case_execution_id=None, case_definition_id=None, case_instance_id=None, task_definition_key=None, suspended=None, form_key=None, tenant_id=None, local_vars_configuration=None):  # noqa: E501
        """TaskDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._assignee = None
        self._owner = None
        self._created = None
        self._due = None
        self._follow_up = None
        self._delegation_state = None
        self._description = None
        self._execution_id = None
        self._parent_task_id = None
        self._priority = None
        self._process_definition_id = None
        self._process_instance_id = None
        self._case_execution_id = None
        self._case_definition_id = None
        self._case_instance_id = None
        self._task_definition_key = None
        self._suspended = None
        self._form_key = None
        self._tenant_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if assignee is not None:
            self.assignee = assignee
        if owner is not None:
            self.owner = owner
        if created is not None:
            self.created = created
        self.due = due
        self.follow_up = follow_up
        if delegation_state is not None:
            self.delegation_state = delegation_state
        if description is not None:
            self.description = description
        if execution_id is not None:
            self.execution_id = execution_id
        if parent_task_id is not None:
            self.parent_task_id = parent_task_id
        self.priority = priority
        if process_definition_id is not None:
            self.process_definition_id = process_definition_id
        if process_instance_id is not None:
            self.process_instance_id = process_instance_id
        if case_execution_id is not None:
            self.case_execution_id = case_execution_id
        if case_definition_id is not None:
            self.case_definition_id = case_definition_id
        if case_instance_id is not None:
            self.case_instance_id = case_instance_id
        if task_definition_key is not None:
            self.task_definition_key = task_definition_key
        self.suspended = suspended
        if form_key is not None:
            self.form_key = form_key
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def id(self):
        """Gets the id of this TaskDto.  # noqa: E501

        The task id.  # noqa: E501

        :return: The id of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskDto.

        The task id.  # noqa: E501

        :param id: The id of this TaskDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this TaskDto.  # noqa: E501

        The task name.  # noqa: E501

        :return: The name of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskDto.

        The task name.  # noqa: E501

        :param name: The name of this TaskDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def assignee(self):
        """Gets the assignee of this TaskDto.  # noqa: E501

        The assignee's id.  # noqa: E501

        :return: The assignee of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        """Sets the assignee of this TaskDto.

        The assignee's id.  # noqa: E501

        :param assignee: The assignee of this TaskDto.  # noqa: E501
        :type: str
        """

        self._assignee = assignee

    @property
    def owner(self):
        """Gets the owner of this TaskDto.  # noqa: E501

        The owner's id.  # noqa: E501

        :return: The owner of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this TaskDto.

        The owner's id.  # noqa: E501

        :param owner: The owner of this TaskDto.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def created(self):
        """Gets the created of this TaskDto.  # noqa: E501

        The date the task was created on. [Default format](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/) `yyyy-MM-dd'T'HH:mm:ss.SSSZ`.  # noqa: E501

        :return: The created of this TaskDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this TaskDto.

        The date the task was created on. [Default format](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/) `yyyy-MM-dd'T'HH:mm:ss.SSSZ`.  # noqa: E501

        :param created: The created of this TaskDto.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def due(self):
        """Gets the due of this TaskDto.  # noqa: E501

        The task's due date. [Default format](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/) `yyyy-MM-dd'T'HH:mm:ss.SSSZ`.  # noqa: E501

        :return: The due of this TaskDto.  # noqa: E501
        :rtype: datetime
        """
        return self._due

    @due.setter
    def due(self, due):
        """Sets the due of this TaskDto.

        The task's due date. [Default format](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/) `yyyy-MM-dd'T'HH:mm:ss.SSSZ`.  # noqa: E501

        :param due: The due of this TaskDto.  # noqa: E501
        :type: datetime
        """

        self._due = due

    @property
    def follow_up(self):
        """Gets the follow_up of this TaskDto.  # noqa: E501

        The follow-up date for the task. [Default format](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/) `yyyy-MM-dd'T'HH:mm:ss.SSSZ`.  # noqa: E501

        :return: The follow_up of this TaskDto.  # noqa: E501
        :rtype: datetime
        """
        return self._follow_up

    @follow_up.setter
    def follow_up(self, follow_up):
        """Sets the follow_up of this TaskDto.

        The follow-up date for the task. [Default format](https://docs.camunda.org/manual/7.13/reference/rest/overview/date-format/) `yyyy-MM-dd'T'HH:mm:ss.SSSZ`.  # noqa: E501

        :param follow_up: The follow_up of this TaskDto.  # noqa: E501
        :type: datetime
        """

        self._follow_up = follow_up

    @property
    def delegation_state(self):
        """Gets the delegation_state of this TaskDto.  # noqa: E501

        The task's delegation state. Possible values are `PENDING` and `RESOLVED`.  # noqa: E501

        :return: The delegation_state of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._delegation_state

    @delegation_state.setter
    def delegation_state(self, delegation_state):
        """Sets the delegation_state of this TaskDto.

        The task's delegation state. Possible values are `PENDING` and `RESOLVED`.  # noqa: E501

        :param delegation_state: The delegation_state of this TaskDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["PENDING", "RESOLVED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and delegation_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `delegation_state` ({0}), must be one of {1}"  # noqa: E501
                .format(delegation_state, allowed_values)
            )

        self._delegation_state = delegation_state

    @property
    def description(self):
        """Gets the description of this TaskDto.  # noqa: E501

        The task's description.  # noqa: E501

        :return: The description of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskDto.

        The task's description.  # noqa: E501

        :param description: The description of this TaskDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def execution_id(self):
        """Gets the execution_id of this TaskDto.  # noqa: E501

        The id of the execution the task belongs to.  # noqa: E501

        :return: The execution_id of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        """Sets the execution_id of this TaskDto.

        The id of the execution the task belongs to.  # noqa: E501

        :param execution_id: The execution_id of this TaskDto.  # noqa: E501
        :type: str
        """

        self._execution_id = execution_id

    @property
    def parent_task_id(self):
        """Gets the parent_task_id of this TaskDto.  # noqa: E501

        The id the parent task, if this task is a subtask.  # noqa: E501

        :return: The parent_task_id of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._parent_task_id

    @parent_task_id.setter
    def parent_task_id(self, parent_task_id):
        """Sets the parent_task_id of this TaskDto.

        The id the parent task, if this task is a subtask.  # noqa: E501

        :param parent_task_id: The parent_task_id of this TaskDto.  # noqa: E501
        :type: str
        """

        self._parent_task_id = parent_task_id

    @property
    def priority(self):
        """Gets the priority of this TaskDto.  # noqa: E501

        The task's priority.  # noqa: E501

        :return: The priority of this TaskDto.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this TaskDto.

        The task's priority.  # noqa: E501

        :param priority: The priority of this TaskDto.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def process_definition_id(self):
        """Gets the process_definition_id of this TaskDto.  # noqa: E501

        The id of the process definition the task belongs to.  # noqa: E501

        :return: The process_definition_id of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._process_definition_id

    @process_definition_id.setter
    def process_definition_id(self, process_definition_id):
        """Sets the process_definition_id of this TaskDto.

        The id of the process definition the task belongs to.  # noqa: E501

        :param process_definition_id: The process_definition_id of this TaskDto.  # noqa: E501
        :type: str
        """

        self._process_definition_id = process_definition_id

    @property
    def process_instance_id(self):
        """Gets the process_instance_id of this TaskDto.  # noqa: E501

        The id of the process instance the task belongs to.  # noqa: E501

        :return: The process_instance_id of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._process_instance_id

    @process_instance_id.setter
    def process_instance_id(self, process_instance_id):
        """Sets the process_instance_id of this TaskDto.

        The id of the process instance the task belongs to.  # noqa: E501

        :param process_instance_id: The process_instance_id of this TaskDto.  # noqa: E501
        :type: str
        """

        self._process_instance_id = process_instance_id

    @property
    def case_execution_id(self):
        """Gets the case_execution_id of this TaskDto.  # noqa: E501

        The id of the case execution the task belongs to.  # noqa: E501

        :return: The case_execution_id of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._case_execution_id

    @case_execution_id.setter
    def case_execution_id(self, case_execution_id):
        """Sets the case_execution_id of this TaskDto.

        The id of the case execution the task belongs to.  # noqa: E501

        :param case_execution_id: The case_execution_id of this TaskDto.  # noqa: E501
        :type: str
        """

        self._case_execution_id = case_execution_id

    @property
    def case_definition_id(self):
        """Gets the case_definition_id of this TaskDto.  # noqa: E501

        The id of the case definition the task belongs to.  # noqa: E501

        :return: The case_definition_id of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._case_definition_id

    @case_definition_id.setter
    def case_definition_id(self, case_definition_id):
        """Sets the case_definition_id of this TaskDto.

        The id of the case definition the task belongs to.  # noqa: E501

        :param case_definition_id: The case_definition_id of this TaskDto.  # noqa: E501
        :type: str
        """

        self._case_definition_id = case_definition_id

    @property
    def case_instance_id(self):
        """Gets the case_instance_id of this TaskDto.  # noqa: E501

        The id of the case instance the task belongs to.  # noqa: E501

        :return: The case_instance_id of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._case_instance_id

    @case_instance_id.setter
    def case_instance_id(self, case_instance_id):
        """Sets the case_instance_id of this TaskDto.

        The id of the case instance the task belongs to.  # noqa: E501

        :param case_instance_id: The case_instance_id of this TaskDto.  # noqa: E501
        :type: str
        """

        self._case_instance_id = case_instance_id

    @property
    def task_definition_key(self):
        """Gets the task_definition_key of this TaskDto.  # noqa: E501

        The task's key.  # noqa: E501

        :return: The task_definition_key of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._task_definition_key

    @task_definition_key.setter
    def task_definition_key(self, task_definition_key):
        """Sets the task_definition_key of this TaskDto.

        The task's key.  # noqa: E501

        :param task_definition_key: The task_definition_key of this TaskDto.  # noqa: E501
        :type: str
        """

        self._task_definition_key = task_definition_key

    @property
    def suspended(self):
        """Gets the suspended of this TaskDto.  # noqa: E501

        Whether the task belongs to a process instance that is suspended.  # noqa: E501

        :return: The suspended of this TaskDto.  # noqa: E501
        :rtype: bool
        """
        return self._suspended

    @suspended.setter
    def suspended(self, suspended):
        """Sets the suspended of this TaskDto.

        Whether the task belongs to a process instance that is suspended.  # noqa: E501

        :param suspended: The suspended of this TaskDto.  # noqa: E501
        :type: bool
        """

        self._suspended = suspended

    @property
    def form_key(self):
        """Gets the form_key of this TaskDto.  # noqa: E501

        If not `null`, the form key for the task.  # noqa: E501

        :return: The form_key of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._form_key

    @form_key.setter
    def form_key(self, form_key):
        """Sets the form_key of this TaskDto.

        If not `null`, the form key for the task.  # noqa: E501

        :param form_key: The form_key of this TaskDto.  # noqa: E501
        :type: str
        """

        self._form_key = form_key

    @property
    def tenant_id(self):
        """Gets the tenant_id of this TaskDto.  # noqa: E501

        If not `null`, the tenant id of the task.  # noqa: E501

        :return: The tenant_id of this TaskDto.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this TaskDto.

        If not `null`, the tenant id of the task.  # noqa: E501

        :param tenant_id: The tenant_id of this TaskDto.  # noqa: E501
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
        if not isinstance(other, TaskDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskDto):
            return True

        return self.to_dict() != other.to_dict()
