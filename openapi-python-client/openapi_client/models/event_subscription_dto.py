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


class EventSubscriptionDto(object):
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
        'event_type': 'str',
        'event_name': 'str',
        'execution_id': 'str',
        'process_instance_id': 'str',
        'activity_id': 'str',
        'created_date': 'datetime',
        'tenant_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'event_type': 'eventType',
        'event_name': 'eventName',
        'execution_id': 'executionId',
        'process_instance_id': 'processInstanceId',
        'activity_id': 'activityId',
        'created_date': 'createdDate',
        'tenant_id': 'tenantId'
    }

    def __init__(self, id=None, event_type=None, event_name=None, execution_id=None, process_instance_id=None, activity_id=None, created_date=None, tenant_id=None, local_vars_configuration=None):  # noqa: E501
        """EventSubscriptionDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._event_type = None
        self._event_name = None
        self._execution_id = None
        self._process_instance_id = None
        self._activity_id = None
        self._created_date = None
        self._tenant_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if event_type is not None:
            self.event_type = event_type
        if event_name is not None:
            self.event_name = event_name
        if execution_id is not None:
            self.execution_id = execution_id
        if process_instance_id is not None:
            self.process_instance_id = process_instance_id
        if activity_id is not None:
            self.activity_id = activity_id
        self.created_date = created_date
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def id(self):
        """Gets the id of this EventSubscriptionDto.  # noqa: E501

        The id of the event subscription.  # noqa: E501

        :return: The id of this EventSubscriptionDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventSubscriptionDto.

        The id of the event subscription.  # noqa: E501

        :param id: The id of this EventSubscriptionDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def event_type(self):
        """Gets the event_type of this EventSubscriptionDto.  # noqa: E501

        The type of the event subscription.  # noqa: E501

        :return: The event_type of this EventSubscriptionDto.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this EventSubscriptionDto.

        The type of the event subscription.  # noqa: E501

        :param event_type: The event_type of this EventSubscriptionDto.  # noqa: E501
        :type: str
        """

        self._event_type = event_type

    @property
    def event_name(self):
        """Gets the event_name of this EventSubscriptionDto.  # noqa: E501

        The name of the event this subscription belongs to as defined in the process model.  # noqa: E501

        :return: The event_name of this EventSubscriptionDto.  # noqa: E501
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this EventSubscriptionDto.

        The name of the event this subscription belongs to as defined in the process model.  # noqa: E501

        :param event_name: The event_name of this EventSubscriptionDto.  # noqa: E501
        :type: str
        """

        self._event_name = event_name

    @property
    def execution_id(self):
        """Gets the execution_id of this EventSubscriptionDto.  # noqa: E501

        The execution that is subscribed on the referenced event.  # noqa: E501

        :return: The execution_id of this EventSubscriptionDto.  # noqa: E501
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        """Sets the execution_id of this EventSubscriptionDto.

        The execution that is subscribed on the referenced event.  # noqa: E501

        :param execution_id: The execution_id of this EventSubscriptionDto.  # noqa: E501
        :type: str
        """

        self._execution_id = execution_id

    @property
    def process_instance_id(self):
        """Gets the process_instance_id of this EventSubscriptionDto.  # noqa: E501

        The process instance this subscription belongs to.  # noqa: E501

        :return: The process_instance_id of this EventSubscriptionDto.  # noqa: E501
        :rtype: str
        """
        return self._process_instance_id

    @process_instance_id.setter
    def process_instance_id(self, process_instance_id):
        """Sets the process_instance_id of this EventSubscriptionDto.

        The process instance this subscription belongs to.  # noqa: E501

        :param process_instance_id: The process_instance_id of this EventSubscriptionDto.  # noqa: E501
        :type: str
        """

        self._process_instance_id = process_instance_id

    @property
    def activity_id(self):
        """Gets the activity_id of this EventSubscriptionDto.  # noqa: E501

        The identifier of the activity that this event subscription belongs to. This could for example be the id of a receive task.  # noqa: E501

        :return: The activity_id of this EventSubscriptionDto.  # noqa: E501
        :rtype: str
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """Sets the activity_id of this EventSubscriptionDto.

        The identifier of the activity that this event subscription belongs to. This could for example be the id of a receive task.  # noqa: E501

        :param activity_id: The activity_id of this EventSubscriptionDto.  # noqa: E501
        :type: str
        """

        self._activity_id = activity_id

    @property
    def created_date(self):
        """Gets the created_date of this EventSubscriptionDto.  # noqa: E501

        The time this event subscription was created.  # noqa: E501

        :return: The created_date of this EventSubscriptionDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this EventSubscriptionDto.

        The time this event subscription was created.  # noqa: E501

        :param created_date: The created_date of this EventSubscriptionDto.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def tenant_id(self):
        """Gets the tenant_id of this EventSubscriptionDto.  # noqa: E501

        The id of the tenant this event subscription belongs to. Can be `null` if the subscription belongs to no single tenant.  # noqa: E501

        :return: The tenant_id of this EventSubscriptionDto.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this EventSubscriptionDto.

        The id of the tenant this event subscription belongs to. Can be `null` if the subscription belongs to no single tenant.  # noqa: E501

        :param tenant_id: The tenant_id of this EventSubscriptionDto.  # noqa: E501
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
        if not isinstance(other, EventSubscriptionDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EventSubscriptionDto):
            return True

        return self.to_dict() != other.to_dict()
