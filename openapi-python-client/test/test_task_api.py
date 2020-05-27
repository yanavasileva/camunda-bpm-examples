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
from openapi_client.api.task_api import TaskApi  # noqa: E501
from openapi_client.rest import ApiException


class TestTaskApi(unittest.TestCase):
    """TaskApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.task_api.TaskApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_claim(self):
        """Test case for claim

        """
        pass

    def test_complete(self):
        """Test case for complete

        """
        pass

    def test_create_task(self):
        """Test case for create_task

        """
        pass

    def test_delegate_task(self):
        """Test case for delegate_task

        """
        pass

    def test_delete_task(self):
        """Test case for delete_task

        """
        pass

    def test_get_deployed_form(self):
        """Test case for get_deployed_form

        """
        pass

    def test_get_form(self):
        """Test case for get_form

        """
        pass

    def test_get_form_variables(self):
        """Test case for get_form_variables

        """
        pass

    def test_get_rendered_form(self):
        """Test case for get_rendered_form

        """
        pass

    def test_get_task(self):
        """Test case for get_task

        """
        pass

    def test_get_tasks(self):
        """Test case for get_tasks

        """
        pass

    def test_get_tasks_count(self):
        """Test case for get_tasks_count

        """
        pass

    def test_handle_bpmn_error(self):
        """Test case for handle_bpmn_error

        """
        pass

    def test_handle_escalation(self):
        """Test case for handle_escalation

        """
        pass

    def test_query_tasks(self):
        """Test case for query_tasks

        """
        pass

    def test_query_tasks_count(self):
        """Test case for query_tasks_count

        """
        pass

    def test_resolve(self):
        """Test case for resolve

        """
        pass

    def test_set_assignee(self):
        """Test case for set_assignee

        """
        pass

    def test_submit(self):
        """Test case for submit

        """
        pass

    def test_unclaim(self):
        """Test case for unclaim

        """
        pass

    def test_update_task(self):
        """Test case for update_task

        """
        pass


if __name__ == '__main__':
    unittest.main()
