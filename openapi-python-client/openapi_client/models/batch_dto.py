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


class BatchDto(object):
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
        'type': 'str',
        'total_jobs': 'int',
        'jobs_created': 'int',
        'batch_jobs_per_seed': 'int',
        'invocations_per_batch_job': 'int',
        'seed_job_definition_id': 'str',
        'monitor_job_definition_id': 'str',
        'batch_job_definition_id': 'str',
        'suspended': 'bool',
        'tenant_id': 'str',
        'create_user_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'total_jobs': 'totalJobs',
        'jobs_created': 'jobsCreated',
        'batch_jobs_per_seed': 'batchJobsPerSeed',
        'invocations_per_batch_job': 'invocationsPerBatchJob',
        'seed_job_definition_id': 'seedJobDefinitionId',
        'monitor_job_definition_id': 'monitorJobDefinitionId',
        'batch_job_definition_id': 'batchJobDefinitionId',
        'suspended': 'suspended',
        'tenant_id': 'tenantId',
        'create_user_id': 'createUserId'
    }

    def __init__(self, id=None, type=None, total_jobs=None, jobs_created=None, batch_jobs_per_seed=None, invocations_per_batch_job=None, seed_job_definition_id=None, monitor_job_definition_id=None, batch_job_definition_id=None, suspended=None, tenant_id=None, create_user_id=None, local_vars_configuration=None):  # noqa: E501
        """BatchDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._total_jobs = None
        self._jobs_created = None
        self._batch_jobs_per_seed = None
        self._invocations_per_batch_job = None
        self._seed_job_definition_id = None
        self._monitor_job_definition_id = None
        self._batch_job_definition_id = None
        self._suspended = None
        self._tenant_id = None
        self._create_user_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if total_jobs is not None:
            self.total_jobs = total_jobs
        if jobs_created is not None:
            self.jobs_created = jobs_created
        if batch_jobs_per_seed is not None:
            self.batch_jobs_per_seed = batch_jobs_per_seed
        if invocations_per_batch_job is not None:
            self.invocations_per_batch_job = invocations_per_batch_job
        if seed_job_definition_id is not None:
            self.seed_job_definition_id = seed_job_definition_id
        if monitor_job_definition_id is not None:
            self.monitor_job_definition_id = monitor_job_definition_id
        if batch_job_definition_id is not None:
            self.batch_job_definition_id = batch_job_definition_id
        if suspended is not None:
            self.suspended = suspended
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if create_user_id is not None:
            self.create_user_id = create_user_id

    @property
    def id(self):
        """Gets the id of this BatchDto.  # noqa: E501

        The id of the batch.  # noqa: E501

        :return: The id of this BatchDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BatchDto.

        The id of the batch.  # noqa: E501

        :param id: The id of this BatchDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this BatchDto.  # noqa: E501

        The type of the batch.  # noqa: E501

        :return: The type of this BatchDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BatchDto.

        The type of the batch.  # noqa: E501

        :param type: The type of this BatchDto.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def total_jobs(self):
        """Gets the total_jobs of this BatchDto.  # noqa: E501

        The total jobs of a batch is the number of batch execution jobs required to complete the batch.  # noqa: E501

        :return: The total_jobs of this BatchDto.  # noqa: E501
        :rtype: int
        """
        return self._total_jobs

    @total_jobs.setter
    def total_jobs(self, total_jobs):
        """Sets the total_jobs of this BatchDto.

        The total jobs of a batch is the number of batch execution jobs required to complete the batch.  # noqa: E501

        :param total_jobs: The total_jobs of this BatchDto.  # noqa: E501
        :type: int
        """

        self._total_jobs = total_jobs

    @property
    def jobs_created(self):
        """Gets the jobs_created of this BatchDto.  # noqa: E501

        The number of batch execution jobs already created by the seed job.  # noqa: E501

        :return: The jobs_created of this BatchDto.  # noqa: E501
        :rtype: int
        """
        return self._jobs_created

    @jobs_created.setter
    def jobs_created(self, jobs_created):
        """Sets the jobs_created of this BatchDto.

        The number of batch execution jobs already created by the seed job.  # noqa: E501

        :param jobs_created: The jobs_created of this BatchDto.  # noqa: E501
        :type: int
        """

        self._jobs_created = jobs_created

    @property
    def batch_jobs_per_seed(self):
        """Gets the batch_jobs_per_seed of this BatchDto.  # noqa: E501

        The number of batch execution jobs created per seed job invocation. The batch seed job is invoked until it has created all batch execution jobs required by the batch (see totalJobs property).  # noqa: E501

        :return: The batch_jobs_per_seed of this BatchDto.  # noqa: E501
        :rtype: int
        """
        return self._batch_jobs_per_seed

    @batch_jobs_per_seed.setter
    def batch_jobs_per_seed(self, batch_jobs_per_seed):
        """Sets the batch_jobs_per_seed of this BatchDto.

        The number of batch execution jobs created per seed job invocation. The batch seed job is invoked until it has created all batch execution jobs required by the batch (see totalJobs property).  # noqa: E501

        :param batch_jobs_per_seed: The batch_jobs_per_seed of this BatchDto.  # noqa: E501
        :type: int
        """

        self._batch_jobs_per_seed = batch_jobs_per_seed

    @property
    def invocations_per_batch_job(self):
        """Gets the invocations_per_batch_job of this BatchDto.  # noqa: E501

        Every batch execution job invokes the command executed by the batch invocationsPerBatchJob times. E.g., for a process instance migration batch this specifies the number of process instances which are migrated per batch execution job.  # noqa: E501

        :return: The invocations_per_batch_job of this BatchDto.  # noqa: E501
        :rtype: int
        """
        return self._invocations_per_batch_job

    @invocations_per_batch_job.setter
    def invocations_per_batch_job(self, invocations_per_batch_job):
        """Sets the invocations_per_batch_job of this BatchDto.

        Every batch execution job invokes the command executed by the batch invocationsPerBatchJob times. E.g., for a process instance migration batch this specifies the number of process instances which are migrated per batch execution job.  # noqa: E501

        :param invocations_per_batch_job: The invocations_per_batch_job of this BatchDto.  # noqa: E501
        :type: int
        """

        self._invocations_per_batch_job = invocations_per_batch_job

    @property
    def seed_job_definition_id(self):
        """Gets the seed_job_definition_id of this BatchDto.  # noqa: E501

        The job definition id for the seed jobs of this batch.  # noqa: E501

        :return: The seed_job_definition_id of this BatchDto.  # noqa: E501
        :rtype: str
        """
        return self._seed_job_definition_id

    @seed_job_definition_id.setter
    def seed_job_definition_id(self, seed_job_definition_id):
        """Sets the seed_job_definition_id of this BatchDto.

        The job definition id for the seed jobs of this batch.  # noqa: E501

        :param seed_job_definition_id: The seed_job_definition_id of this BatchDto.  # noqa: E501
        :type: str
        """

        self._seed_job_definition_id = seed_job_definition_id

    @property
    def monitor_job_definition_id(self):
        """Gets the monitor_job_definition_id of this BatchDto.  # noqa: E501

        The job definition id for the monitor jobs of this batch.  # noqa: E501

        :return: The monitor_job_definition_id of this BatchDto.  # noqa: E501
        :rtype: str
        """
        return self._monitor_job_definition_id

    @monitor_job_definition_id.setter
    def monitor_job_definition_id(self, monitor_job_definition_id):
        """Sets the monitor_job_definition_id of this BatchDto.

        The job definition id for the monitor jobs of this batch.  # noqa: E501

        :param monitor_job_definition_id: The monitor_job_definition_id of this BatchDto.  # noqa: E501
        :type: str
        """

        self._monitor_job_definition_id = monitor_job_definition_id

    @property
    def batch_job_definition_id(self):
        """Gets the batch_job_definition_id of this BatchDto.  # noqa: E501

        The job definition id for the batch execution jobs of this batch.  # noqa: E501

        :return: The batch_job_definition_id of this BatchDto.  # noqa: E501
        :rtype: str
        """
        return self._batch_job_definition_id

    @batch_job_definition_id.setter
    def batch_job_definition_id(self, batch_job_definition_id):
        """Sets the batch_job_definition_id of this BatchDto.

        The job definition id for the batch execution jobs of this batch.  # noqa: E501

        :param batch_job_definition_id: The batch_job_definition_id of this BatchDto.  # noqa: E501
        :type: str
        """

        self._batch_job_definition_id = batch_job_definition_id

    @property
    def suspended(self):
        """Gets the suspended of this BatchDto.  # noqa: E501

        Indicates whether this batch is suspended or not.  # noqa: E501

        :return: The suspended of this BatchDto.  # noqa: E501
        :rtype: bool
        """
        return self._suspended

    @suspended.setter
    def suspended(self, suspended):
        """Sets the suspended of this BatchDto.

        Indicates whether this batch is suspended or not.  # noqa: E501

        :param suspended: The suspended of this BatchDto.  # noqa: E501
        :type: bool
        """

        self._suspended = suspended

    @property
    def tenant_id(self):
        """Gets the tenant_id of this BatchDto.  # noqa: E501

        The tenant id of the batch.  # noqa: E501

        :return: The tenant_id of this BatchDto.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this BatchDto.

        The tenant id of the batch.  # noqa: E501

        :param tenant_id: The tenant_id of this BatchDto.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def create_user_id(self):
        """Gets the create_user_id of this BatchDto.  # noqa: E501

        The id of the user that created the batch.  # noqa: E501

        :return: The create_user_id of this BatchDto.  # noqa: E501
        :rtype: str
        """
        return self._create_user_id

    @create_user_id.setter
    def create_user_id(self, create_user_id):
        """Sets the create_user_id of this BatchDto.

        The id of the user that created the batch.  # noqa: E501

        :param create_user_id: The create_user_id of this BatchDto.  # noqa: E501
        :type: str
        """

        self._create_user_id = create_user_id

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
        if not isinstance(other, BatchDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BatchDto):
            return True

        return self.to_dict() != other.to_dict()
