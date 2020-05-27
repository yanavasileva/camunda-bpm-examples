# coding: utf-8

"""
    Camunda BPM REST API

    OpenApi Spec for Camunda BPM REST API.  # noqa: E501

    The version of the OpenAPI document: 7.13.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.task_local_variable_api import TaskLocalVariableApi  # noqa: E501
from openapi_client.rest import ApiException


class TestTaskLocalVariableApi(unittest.TestCase):
    """TaskLocalVariableApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.task_local_variable_api.TaskLocalVariableApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_task_local_variable(self):
        """Test case for delete_task_local_variable

        """
        pass

    def test_get_task_local_variable(self):
        """Test case for get_task_local_variable

        """
        pass

    def test_get_task_local_variable_binary(self):
        """Test case for get_task_local_variable_binary

        """
        pass

    def test_get_task_local_variables(self):
        """Test case for get_task_local_variables

        """
        pass

    def test_modify_task_local_variables(self):
        """Test case for modify_task_local_variables

        """
        pass

    def test_put_task_local_variable(self):
        """Test case for put_task_local_variable

        """
        pass

    def test_set_binary_task_local_variable(self):
        """Test case for set_binary_task_local_variable

        """
        pass


if __name__ == '__main__':
    unittest.main()
