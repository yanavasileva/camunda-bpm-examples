# coding: utf-8

"""
    Camunda BPM REST API

    OpenApi Spec for Camunda BPM REST API.  # noqa: E501

    The version of the OpenAPI document: 7.13.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.set_retries_for_external_tasks_dto import SetRetriesForExternalTasksDto  # noqa: E501
from openapi_client.rest import ApiException

class TestSetRetriesForExternalTasksDto(unittest.TestCase):
    """SetRetriesForExternalTasksDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SetRetriesForExternalTasksDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.set_retries_for_external_tasks_dto.SetRetriesForExternalTasksDto()  # noqa: E501
        if include_optional :
            return SetRetriesForExternalTasksDto(
                retries = 56, 
                external_task_ids = [
                    '0'
                    ], 
                process_instance_ids = [
                    '0'
                    ], 
                external_task_query = openapi_client.models.external_task_query_dto.ExternalTaskQueryDto(
                    external_task_id = '0', 
                    external_task_id_in = [
                        '0'
                        ], 
                    topic_name = '0', 
                    worker_id = '0', 
                    locked = True, 
                    not_locked = True, 
                    with_retries_left = True, 
                    no_retries_left = True, 
                    lock_expiration_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    lock_expiration_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    activity_id = '0', 
                    activity_id_in = [
                        '0'
                        ], 
                    execution_id = '0', 
                    process_instance_id = '0', 
                    process_instance_id_in = [
                        '0'
                        ], 
                    process_definition_id = '0', 
                    tenant_id_in = [
                        '0'
                        ], 
                    active = True, 
                    suspended = True, 
                    priority_higher_than_or_equals = 56, 
                    priority_lower_than_or_equals = 56, 
                    sorting = [
                        openapi_client.models.external_task_query_dto_sorting.ExternalTaskQueryDto_sorting(
                            sort_by = 'id', 
                            sort_order = 'asc', )
                        ], ), 
                process_instance_query = openapi_client.models.process_instance_query_dto.ProcessInstanceQueryDto(
                    deployment_id = '0', 
                    process_definition_id = '0', 
                    process_definition_key = '0', 
                    process_definition_key_in = [
                        '0'
                        ], 
                    process_definition_key_not_in = [
                        '0'
                        ], 
                    business_key = '0', 
                    business_key_like = '0', 
                    case_instance_id = '0', 
                    super_process_instance = '0', 
                    sub_process_instance = '0', 
                    super_case_instance = '0', 
                    sub_case_instance = '0', 
                    active = True, 
                    suspended = True, 
                    process_instance_ids = [
                        '0'
                        ], 
                    with_incident = True, 
                    incident_id = '0', 
                    incident_type = '0', 
                    incident_message = '0', 
                    incident_message_like = '0', 
                    tenant_id_in = [
                        '0'
                        ], 
                    without_tenant_id = True, 
                    process_definition_without_tenant_id = True, 
                    activity_id_in = [
                        '0'
                        ], 
                    root_process_instances = True, 
                    leaf_process_instances = True, 
                    variables = [
                        openapi_client.models.variable_query_parameter_dto.VariableQueryParameterDto(
                            value = openapi_client.models.value.value(), 
                            operator = 'eq', )
                        ], 
                    variable_names_ignore_case = True, 
                    variable_values_ignore_case = True, 
                    or_queries = [
                        openapi_client.models.process_instance_query_dto.ProcessInstanceQueryDto(
                            deployment_id = '0', 
                            process_definition_id = '0', 
                            process_definition_key = '0', 
                            business_key = '0', 
                            business_key_like = '0', 
                            case_instance_id = '0', 
                            super_process_instance = '0', 
                            sub_process_instance = '0', 
                            super_case_instance = '0', 
                            sub_case_instance = '0', 
                            active = True, 
                            suspended = True, 
                            with_incident = True, 
                            incident_id = '0', 
                            incident_type = '0', 
                            incident_message = '0', 
                            incident_message_like = '0', 
                            without_tenant_id = True, 
                            process_definition_without_tenant_id = True, 
                            root_process_instances = True, 
                            leaf_process_instances = True, 
                            variable_names_ignore_case = True, 
                            variable_values_ignore_case = True, 
                            sorting = [
                                openapi_client.models.process_instance_query_dto_sorting.ProcessInstanceQueryDto_sorting(
                                    sort_by = 'instanceId', 
                                    sort_order = 'asc', )
                                ], )
                        ], 
                    sorting = [
                        openapi_client.models.process_instance_query_dto_sorting.ProcessInstanceQueryDto_sorting(
                            sort_by = 'instanceId', 
                            sort_order = 'asc', )
                        ], ), 
                historic_process_instance_query = openapi_client.models.historic_process_instance_query_dto.HistoricProcessInstanceQueryDto(
                    process_instance_id = '0', 
                    process_instance_ids = [
                        '0'
                        ], 
                    process_definition_id = '0', 
                    process_definition_key = '0', 
                    process_definition_key_in = [
                        '0'
                        ], 
                    process_definition_name = '0', 
                    process_definition_name_like = '0', 
                    process_definition_key_not_in = [
                        '0'
                        ], 
                    process_instance_business_key = '0', 
                    process_instance_business_key_like = '0', 
                    root_process_instances = True, 
                    finished = True, 
                    unfinished = True, 
                    with_incidents = True, 
                    with_root_incidents = True, 
                    incident_type = '0', 
                    incident_status = 'open', 
                    incident_message = '0', 
                    incident_message_like = '0', 
                    started_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    started_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    finished_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    finished_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    executed_activity_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    executed_activity_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    executed_job_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    executed_job_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    started_by = '0', 
                    super_process_instance_id = '0', 
                    sub_process_instance_id = '0', 
                    super_case_instance_id = '0', 
                    sub_case_instance_id = '0', 
                    case_instance_id = '0', 
                    tenant_id_in = [
                        '0'
                        ], 
                    without_tenant_id = True, 
                    executed_activity_id_in = [
                        '0'
                        ], 
                    active_activity_id_in = [
                        '0'
                        ], 
                    active = True, 
                    suspended = True, 
                    completed = True, 
                    externally_terminated = True, 
                    internally_terminated = True, 
                    variables = [
                        openapi_client.models.variable_query_parameter_dto.VariableQueryParameterDto(
                            value = openapi_client.models.value.value(), 
                            operator = 'eq', )
                        ], 
                    variable_names_ignore_case = True, 
                    variable_values_ignore_case = True, 
                    or_queries = [
                        openapi_client.models.historic_process_instance_query_dto.HistoricProcessInstanceQueryDto(
                            process_instance_id = '0', 
                            process_definition_id = '0', 
                            process_definition_key = '0', 
                            process_definition_name = '0', 
                            process_definition_name_like = '0', 
                            process_instance_business_key = '0', 
                            process_instance_business_key_like = '0', 
                            root_process_instances = True, 
                            finished = True, 
                            unfinished = True, 
                            with_incidents = True, 
                            with_root_incidents = True, 
                            incident_type = '0', 
                            incident_status = 'open', 
                            incident_message = '0', 
                            incident_message_like = '0', 
                            started_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            started_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            finished_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            finished_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            executed_activity_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            executed_activity_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            executed_job_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            executed_job_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            started_by = '0', 
                            super_process_instance_id = '0', 
                            sub_process_instance_id = '0', 
                            super_case_instance_id = '0', 
                            sub_case_instance_id = '0', 
                            case_instance_id = '0', 
                            without_tenant_id = True, 
                            active = True, 
                            suspended = True, 
                            completed = True, 
                            externally_terminated = True, 
                            internally_terminated = True, 
                            variable_names_ignore_case = True, 
                            variable_values_ignore_case = True, 
                            sorting = [
                                openapi_client.models.historic_process_instance_query_dto_sorting.HistoricProcessInstanceQueryDto_sorting(
                                    sort_by = 'instanceId', 
                                    sort_order = 'asc', )
                                ], )
                        ], 
                    sorting = [
                        openapi_client.models.historic_process_instance_query_dto_sorting.HistoricProcessInstanceQueryDto_sorting(
                            sort_by = 'instanceId', 
                            sort_order = 'asc', )
                        ], )
            )
        else :
            return SetRetriesForExternalTasksDto(
        )

    def testSetRetriesForExternalTasksDto(self):
        """Test SetRetriesForExternalTasksDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
