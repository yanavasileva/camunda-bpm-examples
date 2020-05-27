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
from openapi_client.models.authorization_exception_dto import AuthorizationExceptionDto  # noqa: E501
from openapi_client.rest import ApiException

class TestAuthorizationExceptionDto(unittest.TestCase):
    """AuthorizationExceptionDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AuthorizationExceptionDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.authorization_exception_dto.AuthorizationExceptionDto()  # noqa: E501
        if include_optional :
            return AuthorizationExceptionDto(
                user_id = '0', 
                missing_authorizations = [
                    openapi_client.models.missing_authorization_dto.MissingAuthorizationDto(
                        permission_name = '0', 
                        resource_name = '0', 
                        resource_id = '0', )
                    ], 
                type = '0', 
                message = '0'
            )
        else :
            return AuthorizationExceptionDto(
        )

    def testAuthorizationExceptionDto(self):
        """Test AuthorizationExceptionDto"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
