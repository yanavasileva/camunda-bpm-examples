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
from openapi_client.models.process_definition_suspension_state_dto import ProcessDefinitionSuspensionStateDto  # noqa: E501
from openapi_client.rest import ApiException

class TestProcessDefinitionSuspensionStateDto(unittest.TestCase):
    """ProcessDefinitionSuspensionStateDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProcessDefinitionSuspensionStateDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.process_definition_suspension_state_dto.ProcessDefinitionSuspensionStateDto()  # noqa: E501
        if include_optional :
            return ProcessDefinitionSuspensionStateDto(
                suspended = True, 
                process_definition_id = '0', 
                process_definition_key = '0', 
                include_process_instances = True, 
                execution_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return ProcessDefinitionSuspensionStateDto(
        )

    def testProcessDefinitionSuspensionStateDto(self):
        """Test ProcessDefinitionSuspensionStateDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()