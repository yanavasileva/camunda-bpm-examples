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
from openapi_client.models.deployment_dto import DeploymentDto  # noqa: E501
from openapi_client.rest import ApiException

class TestDeploymentDto(unittest.TestCase):
    """DeploymentDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DeploymentDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.deployment_dto.DeploymentDto()  # noqa: E501
        if include_optional :
            return DeploymentDto(
                id = '0', 
                tenant_id = '0', 
                deployment_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                source = '0', 
                name = '0', 
                links = [
                    openapi_client.models.atom_link.AtomLink(
                        rel = '0', 
                        href = '0', 
                        method = '0', )
                    ]
            )
        else :
            return DeploymentDto(
        )

    def testDeploymentDto(self):
        """Test DeploymentDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
