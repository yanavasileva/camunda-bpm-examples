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
from openapi_client.api.event_subscription_api import EventSubscriptionApi  # noqa: E501
from openapi_client.rest import ApiException


class TestEventSubscriptionApi(unittest.TestCase):
    """EventSubscriptionApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.event_subscription_api.EventSubscriptionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_event_subscriptions(self):
        """Test case for get_event_subscriptions

        """
        pass

    def test_get_event_subscriptions_count(self):
        """Test case for get_event_subscriptions_count

        """
        pass


if __name__ == '__main__':
    unittest.main()
