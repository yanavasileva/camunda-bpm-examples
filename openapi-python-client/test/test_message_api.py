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
from openapi_client.api.message_api import MessageApi  # noqa: E501
from openapi_client.rest import ApiException


class TestMessageApi(unittest.TestCase):
    """MessageApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.message_api.MessageApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_deliver_message(self):
        """Test case for deliver_message

        """
        pass


if __name__ == '__main__':
    unittest.main()
