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
from openapi_client.models.external_task_bpmn_error_all_of import ExternalTaskBpmnErrorAllOf  # noqa: E501
from openapi_client.rest import ApiException

class TestExternalTaskBpmnErrorAllOf(unittest.TestCase):
    """ExternalTaskBpmnErrorAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExternalTaskBpmnErrorAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.external_task_bpmn_error_all_of.ExternalTaskBpmnErrorAllOf()  # noqa: E501
        if include_optional :
            return ExternalTaskBpmnErrorAllOf(
                worker_id = '0'
            )
        else :
            return ExternalTaskBpmnErrorAllOf(
        )

    def testExternalTaskBpmnErrorAllOf(self):
        """Test ExternalTaskBpmnErrorAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
