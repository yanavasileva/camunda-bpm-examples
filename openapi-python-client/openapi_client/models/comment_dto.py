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


class CommentDto(object):
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
        'user_id': 'str',
        'task_id': 'str',
        'time': 'datetime',
        'message': 'str',
        'removal_time': 'datetime',
        'root_process_instance_id': 'str',
        'links': 'list[AtomLink]'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'userId',
        'task_id': 'taskId',
        'time': 'time',
        'message': 'message',
        'removal_time': 'removalTime',
        'root_process_instance_id': 'rootProcessInstanceId',
        'links': 'links'
    }

    def __init__(self, id=None, user_id=None, task_id=None, time=None, message=None, removal_time=None, root_process_instance_id=None, links=None, local_vars_configuration=None):  # noqa: E501
        """CommentDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._user_id = None
        self._task_id = None
        self._time = None
        self._message = None
        self._removal_time = None
        self._root_process_instance_id = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user_id is not None:
            self.user_id = user_id
        if task_id is not None:
            self.task_id = task_id
        if time is not None:
            self.time = time
        if message is not None:
            self.message = message
        self.removal_time = removal_time
        if root_process_instance_id is not None:
            self.root_process_instance_id = root_process_instance_id
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this CommentDto.  # noqa: E501

        The id of the task comment.  # noqa: E501

        :return: The id of this CommentDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CommentDto.

        The id of the task comment.  # noqa: E501

        :param id: The id of this CommentDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this CommentDto.  # noqa: E501

        The id of the user who created the comment.  # noqa: E501

        :return: The user_id of this CommentDto.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CommentDto.

        The id of the user who created the comment.  # noqa: E501

        :param user_id: The user_id of this CommentDto.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def task_id(self):
        """Gets the task_id of this CommentDto.  # noqa: E501

        The id of the task to which the comment belongs.  # noqa: E501

        :return: The task_id of this CommentDto.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this CommentDto.

        The id of the task to which the comment belongs.  # noqa: E501

        :param task_id: The task_id of this CommentDto.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def time(self):
        """Gets the time of this CommentDto.  # noqa: E501

        The time when the comment was created. [Default format]($(docsUrl)/reference/rest/overview/date-format/) `yyyy-MM-dd'T'HH:mm:ss.SSSZ`.  # noqa: E501

        :return: The time of this CommentDto.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this CommentDto.

        The time when the comment was created. [Default format]($(docsUrl)/reference/rest/overview/date-format/) `yyyy-MM-dd'T'HH:mm:ss.SSSZ`.  # noqa: E501

        :param time: The time of this CommentDto.  # noqa: E501
        :type: datetime
        """

        self._time = time

    @property
    def message(self):
        """Gets the message of this CommentDto.  # noqa: E501

        The content of the comment.  # noqa: E501

        :return: The message of this CommentDto.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CommentDto.

        The content of the comment.  # noqa: E501

        :param message: The message of this CommentDto.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def removal_time(self):
        """Gets the removal_time of this CommentDto.  # noqa: E501

        The time after which the comment should be removed by the History Cleanup job. [Default format]($(docsUrl)/reference/rest/overview/date-format/) `yyyy-MM-dd'T'HH:mm:ss.SSSZ`.  # noqa: E501

        :return: The removal_time of this CommentDto.  # noqa: E501
        :rtype: datetime
        """
        return self._removal_time

    @removal_time.setter
    def removal_time(self, removal_time):
        """Sets the removal_time of this CommentDto.

        The time after which the comment should be removed by the History Cleanup job. [Default format]($(docsUrl)/reference/rest/overview/date-format/) `yyyy-MM-dd'T'HH:mm:ss.SSSZ`.  # noqa: E501

        :param removal_time: The removal_time of this CommentDto.  # noqa: E501
        :type: datetime
        """

        self._removal_time = removal_time

    @property
    def root_process_instance_id(self):
        """Gets the root_process_instance_id of this CommentDto.  # noqa: E501

        The process instance id of the root process instance that initiated the process containing the task.  # noqa: E501

        :return: The root_process_instance_id of this CommentDto.  # noqa: E501
        :rtype: str
        """
        return self._root_process_instance_id

    @root_process_instance_id.setter
    def root_process_instance_id(self, root_process_instance_id):
        """Sets the root_process_instance_id of this CommentDto.

        The process instance id of the root process instance that initiated the process containing the task.  # noqa: E501

        :param root_process_instance_id: The root_process_instance_id of this CommentDto.  # noqa: E501
        :type: str
        """

        self._root_process_instance_id = root_process_instance_id

    @property
    def links(self):
        """Gets the links of this CommentDto.  # noqa: E501

        The links associated to this resource, with `method`, `href` and `rel`.  # noqa: E501

        :return: The links of this CommentDto.  # noqa: E501
        :rtype: list[AtomLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CommentDto.

        The links associated to this resource, with `method`, `href` and `rel`.  # noqa: E501

        :param links: The links of this CommentDto.  # noqa: E501
        :type: list[AtomLink]
        """

        self._links = links

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
        if not isinstance(other, CommentDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CommentDto):
            return True

        return self.to_dict() != other.to_dict()
