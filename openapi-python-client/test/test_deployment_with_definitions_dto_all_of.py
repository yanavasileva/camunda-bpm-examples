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
from openapi_client.models.deployment_with_definitions_dto_all_of import DeploymentWithDefinitionsDtoAllOf  # noqa: E501
from openapi_client.rest import ApiException

class TestDeploymentWithDefinitionsDtoAllOf(unittest.TestCase):
    """DeploymentWithDefinitionsDtoAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DeploymentWithDefinitionsDtoAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.deployment_with_definitions_dto_all_of.DeploymentWithDefinitionsDtoAllOf()  # noqa: E501
        if include_optional :
            return DeploymentWithDefinitionsDtoAllOf(
                deployed_process_definitions = {
                    'key' : openapi_client.models.process_definition_dto.ProcessDefinitionDto(
                        id = '0', 
                        key = '0', 
                        category = '0', 
                        description = '0', 
                        name = '0', 
                        version = 56, 
                        resource = '0', 
                        deployment_id = '0', 
                        diagram = '0', 
                        suspended = True, 
                        tenant_id = '0', 
                        version_tag = '0', 
                        history_time_to_live = 0, 
                        startable_in_tasklist = True, )
                    }, 
                deployed_decision_definitions = {
                    'key' : openapi_client.models.decision_definition_dto.DecisionDefinitionDto(
                        id = '0', 
                        key = '0', 
                        category = '0', 
                        name = '0', 
                        version = 56, 
                        resource = '0', 
                        deployment_id = '0', 
                        tenant_id = '0', 
                        decision_requirements_definition_id = '0', 
                        decision_requirements_definition_key = '0', 
                        history_time_to_live = 0, 
                        version_tag = '0', )
                    }, 
                deployed_decision_requirements_definitions = {
                    'key' : openapi_client.models.decision_requirements_definition_dto.DecisionRequirementsDefinitionDto(
                        id = '0', 
                        key = '0', 
                        name = '0', 
                        category = '0', 
                        version = 56, 
                        resource = '0', 
                        deployment_id = '0', 
                        tenant_id = '0', )
                    }, 
                deployed_case_definitions = {
                    'key' : openapi_client.models.case_definition_dto.CaseDefinitionDto(
                        id = '0', 
                        key = '0', 
                        category = '0', 
                        name = '0', 
                        version = 56, 
                        resource = '0', 
                        deployment_id = '0', 
                        tenant_id = '0', 
                        history_time_to_live = 0, )
                    }
            )
        else :
            return DeploymentWithDefinitionsDtoAllOf(
        )

    def testDeploymentWithDefinitionsDtoAllOf(self):
        """Test DeploymentWithDefinitionsDtoAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
