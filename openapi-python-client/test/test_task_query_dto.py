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
from openapi_client.models.task_query_dto import TaskQueryDto  # noqa: E501
from openapi_client.rest import ApiException

class TestTaskQueryDto(unittest.TestCase):
    """TaskQueryDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TaskQueryDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.task_query_dto.TaskQueryDto()  # noqa: E501
        if include_optional :
            return TaskQueryDto(
                process_instance_id = '0', 
                process_instance_id_in = [
                    '0'
                    ], 
                process_instance_business_key = '0', 
                process_instance_business_key_expression = '0', 
                process_instance_business_key_in = [
                    '0'
                    ], 
                process_instance_business_key_like = '0', 
                process_instance_business_key_like_expression = '0', 
                process_definition_id = '0', 
                process_definition_key = '0', 
                process_definition_key_in = [
                    '0'
                    ], 
                process_definition_name = '0', 
                process_definition_name_like = '0', 
                execution_id = '0', 
                case_instance_id = '0', 
                case_instance_business_key = '0', 
                case_instance_business_key_like = '0', 
                case_definition_id = '0', 
                case_definition_key = '0', 
                case_definition_name = '0', 
                case_definition_name_like = '0', 
                case_execution_id = '0', 
                activity_instance_id_in = [
                    '0'
                    ], 
                tenant_id_in = [
                    '0'
                    ], 
                without_tenant_id = True, 
                assignee = '0', 
                assignee_expression = '0', 
                assignee_like = '0', 
                assignee_like_expression = '0', 
                assignee_in = [
                    '0'
                    ], 
                owner = '0', 
                owner_expression = '0', 
                candidate_group = '0', 
                candidate_group_expression = '0', 
                candidate_user = '0', 
                candidate_user_expression = '0', 
                include_assigned_tasks = True, 
                involved_user = '0', 
                involved_user_expression = '0', 
                assigned = True, 
                unassigned = True, 
                task_definition_key = '0', 
                task_definition_key_in = [
                    '0'
                    ], 
                task_definition_key_like = '0', 
                name = '0', 
                name_not_equal = '0', 
                name_like = '0', 
                name_not_like = '0', 
                description = '0', 
                description_like = '0', 
                priority = 56, 
                max_priority = 56, 
                min_priority = 56, 
                due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                due_date_expression = '0', 
                due_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                due_after_expression = '0', 
                due_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                due_before_expression = '0', 
                follow_up_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                follow_up_date_expression = '0', 
                follow_up_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                follow_up_after_expression = '0', 
                follow_up_before = '0', 
                follow_up_before_expression = '0', 
                follow_up_before_or_not_existent = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                follow_up_before_or_not_existent_expression = '0', 
                created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                created_on_expression = '0', 
                created_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                created_after_expression = '0', 
                created_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                created_before_expression = '0', 
                delegation_state = 'PENDING', 
                candidate_groups = [
                    '0'
                    ], 
                candidate_groups_expression = '0', 
                with_candidate_groups = True, 
                without_candidate_groups = True, 
                with_candidate_users = True, 
                without_candidate_users = True, 
                active = True, 
                suspended = True, 
                task_variables = [
                    openapi_client.models.variable_query_parameter_dto.VariableQueryParameterDto(
                        value = openapi_client.models.value.value(), 
                        operator = 'eq', )
                    ], 
                process_variables = [
                    openapi_client.models.variable_query_parameter_dto.VariableQueryParameterDto(
                        value = openapi_client.models.value.value(), 
                        operator = 'eq', )
                    ], 
                case_instance_variables = [
                    openapi_client.models.variable_query_parameter_dto.VariableQueryParameterDto(
                        value = openapi_client.models.value.value(), 
                        operator = 'eq', )
                    ], 
                variable_names_ignore_case = True, 
                variable_values_ignore_case = True, 
                parent_task_id = '0', 
                or_queries = [
                    openapi_client.models.task_query_dto.TaskQueryDto(
                        process_instance_id = '0', 
                        process_instance_id_in = [
                            '0'
                            ], 
                        process_instance_business_key = '0', 
                        process_instance_business_key_expression = '0', 
                        process_instance_business_key_in = [
                            '0'
                            ], 
                        process_instance_business_key_like = '0', 
                        process_instance_business_key_like_expression = '0', 
                        process_definition_id = '0', 
                        process_definition_key = '0', 
                        process_definition_key_in = [
                            '0'
                            ], 
                        process_definition_name = '0', 
                        process_definition_name_like = '0', 
                        execution_id = '0', 
                        case_instance_id = '0', 
                        case_instance_business_key = '0', 
                        case_instance_business_key_like = '0', 
                        case_definition_id = '0', 
                        case_definition_key = '0', 
                        case_definition_name = '0', 
                        case_definition_name_like = '0', 
                        case_execution_id = '0', 
                        activity_instance_id_in = [
                            '0'
                            ], 
                        tenant_id_in = [
                            '0'
                            ], 
                        without_tenant_id = True, 
                        assignee = '0', 
                        assignee_expression = '0', 
                        assignee_like = '0', 
                        assignee_like_expression = '0', 
                        assignee_in = [
                            '0'
                            ], 
                        owner = '0', 
                        owner_expression = '0', 
                        candidate_group = '0', 
                        candidate_group_expression = '0', 
                        candidate_user = '0', 
                        candidate_user_expression = '0', 
                        include_assigned_tasks = True, 
                        involved_user = '0', 
                        involved_user_expression = '0', 
                        assigned = True, 
                        unassigned = True, 
                        task_definition_key = '0', 
                        task_definition_key_in = [
                            '0'
                            ], 
                        task_definition_key_like = '0', 
                        name = '0', 
                        name_not_equal = '0', 
                        name_like = '0', 
                        name_not_like = '0', 
                        description = '0', 
                        description_like = '0', 
                        priority = 56, 
                        max_priority = 56, 
                        min_priority = 56, 
                        due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        due_date_expression = '0', 
                        due_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        due_after_expression = '0', 
                        due_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        due_before_expression = '0', 
                        follow_up_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        follow_up_date_expression = '0', 
                        follow_up_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        follow_up_after_expression = '0', 
                        follow_up_before = '0', 
                        follow_up_before_expression = '0', 
                        follow_up_before_or_not_existent = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        follow_up_before_or_not_existent_expression = '0', 
                        created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_on_expression = '0', 
                        created_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_after_expression = '0', 
                        created_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_before_expression = '0', 
                        delegation_state = 'PENDING', 
                        candidate_groups = [
                            '0'
                            ], 
                        candidate_groups_expression = '0', 
                        with_candidate_groups = True, 
                        without_candidate_groups = True, 
                        with_candidate_users = True, 
                        without_candidate_users = True, 
                        active = True, 
                        suspended = True, 
                        task_variables = [
                            openapi_client.models.variable_query_parameter_dto.VariableQueryParameterDto(
                                value = openapi_client.models.value.value(), 
                                operator = 'eq', )
                            ], 
                        process_variables = [
                            openapi_client.models.variable_query_parameter_dto.VariableQueryParameterDto(
                                value = openapi_client.models.value.value(), 
                                operator = 'eq', )
                            ], 
                        case_instance_variables = [
                            openapi_client.models.variable_query_parameter_dto.VariableQueryParameterDto(
                                value = openapi_client.models.value.value(), 
                                operator = 'eq', )
                            ], 
                        variable_names_ignore_case = True, 
                        variable_values_ignore_case = True, 
                        parent_task_id = '0', 
                        or_queries = [
                            openapi_client.models.task_query_dto.TaskQueryDto(
                                process_instance_id = '0', 
                                process_instance_business_key = '0', 
                                process_instance_business_key_expression = '0', 
                                process_instance_business_key_like = '0', 
                                process_instance_business_key_like_expression = '0', 
                                process_definition_id = '0', 
                                process_definition_key = '0', 
                                process_definition_name = '0', 
                                process_definition_name_like = '0', 
                                execution_id = '0', 
                                case_instance_id = '0', 
                                case_instance_business_key = '0', 
                                case_instance_business_key_like = '0', 
                                case_definition_id = '0', 
                                case_definition_key = '0', 
                                case_definition_name = '0', 
                                case_definition_name_like = '0', 
                                case_execution_id = '0', 
                                without_tenant_id = True, 
                                assignee = '0', 
                                assignee_expression = '0', 
                                assignee_like = '0', 
                                assignee_like_expression = '0', 
                                owner = '0', 
                                owner_expression = '0', 
                                candidate_group = '0', 
                                candidate_group_expression = '0', 
                                candidate_user = '0', 
                                candidate_user_expression = '0', 
                                include_assigned_tasks = True, 
                                involved_user = '0', 
                                involved_user_expression = '0', 
                                assigned = True, 
                                unassigned = True, 
                                task_definition_key = '0', 
                                task_definition_key_like = '0', 
                                name = '0', 
                                name_not_equal = '0', 
                                name_like = '0', 
                                name_not_like = '0', 
                                description = '0', 
                                description_like = '0', 
                                priority = 56, 
                                max_priority = 56, 
                                min_priority = 56, 
                                due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                due_date_expression = '0', 
                                due_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                due_after_expression = '0', 
                                due_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                due_before_expression = '0', 
                                follow_up_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                follow_up_date_expression = '0', 
                                follow_up_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                follow_up_after_expression = '0', 
                                follow_up_before = '0', 
                                follow_up_before_expression = '0', 
                                follow_up_before_or_not_existent = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                follow_up_before_or_not_existent_expression = '0', 
                                created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                created_on_expression = '0', 
                                created_after = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                created_after_expression = '0', 
                                created_before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                created_before_expression = '0', 
                                delegation_state = 'PENDING', 
                                candidate_groups_expression = '0', 
                                with_candidate_groups = True, 
                                without_candidate_groups = True, 
                                with_candidate_users = True, 
                                without_candidate_users = True, 
                                active = True, 
                                suspended = True, 
                                variable_names_ignore_case = True, 
                                variable_values_ignore_case = True, 
                                parent_task_id = '0', 
                                sorting = [
                                    openapi_client.models.task_query_dto_sorting.TaskQueryDto_sorting(
                                        sort_by = 'instanceId', 
                                        sort_order = 'asc', 
                                        parameters = openapi_client.models.sort_task_query_parameters_dto.SortTaskQueryParametersDto(
                                            variable = '0', 
                                            type = '0', ), )
                                    ], )
                            ], 
                        sorting = [
                            openapi_client.models.task_query_dto_sorting.TaskQueryDto_sorting(
                                sort_by = 'instanceId', 
                                sort_order = 'asc', )
                            ], )
                    ], 
                sorting = [
                    openapi_client.models.task_query_dto_sorting.TaskQueryDto_sorting(
                        sort_by = 'instanceId', 
                        sort_order = 'asc', 
                        parameters = openapi_client.models.sort_task_query_parameters_dto.SortTaskQueryParametersDto(
                            variable = '0', 
                            type = '0', ), )
                    ]
            )
        else :
            return TaskQueryDto(
        )

    def testTaskQueryDto(self):
        """Test TaskQueryDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()