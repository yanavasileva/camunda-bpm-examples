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
from openapi_client.models.process_definition_dto import ProcessDefinitionDto  # noqa: E501
from openapi_client.rest import ApiException

class TestProcessDefinitionDto(unittest.TestCase):
    """ProcessDefinitionDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProcessDefinitionDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.process_definition_dto.ProcessDefinitionDto()  # noqa: E501
        if include_optional :
            return ProcessDefinitionDto(
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
                startable_in_tasklist = True
            )
        else :
            return ProcessDefinitionDto(
        )

    def testProcessDefinitionDto(self):
        """Test ProcessDefinitionDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
