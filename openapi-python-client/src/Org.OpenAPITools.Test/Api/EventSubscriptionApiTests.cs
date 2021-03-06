/* 
 * Camunda BPM REST API
 *
 * OpenApi Spec for Camunda BPM REST API.
 *
 * The version of the OpenAPI document: 7.13.0
 * 
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.IO;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Reflection;
using RestSharp;
using NUnit.Framework;

using Org.OpenAPITools.Client;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Model;

namespace Org.OpenAPITools.Test
{
    /// <summary>
    ///  Class for testing EventSubscriptionApi
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by OpenAPI Generator (https://openapi-generator.tech).
    /// Please update the test case below to test the API endpoint.
    /// </remarks>
    public class EventSubscriptionApiTests
    {
        private EventSubscriptionApi instance;

        /// <summary>
        /// Setup before each unit test
        /// </summary>
        [SetUp]
        public void Init()
        {
            instance = new EventSubscriptionApi();
        }

        /// <summary>
        /// Clean up after each unit test
        /// </summary>
        [TearDown]
        public void Cleanup()
        {

        }

        /// <summary>
        /// Test an instance of EventSubscriptionApi
        /// </summary>
        [Test]
        public void InstanceTest()
        {
            // TODO uncomment below to test 'IsInstanceOf' EventSubscriptionApi
            //Assert.IsInstanceOf(typeof(EventSubscriptionApi), instance);
        }

        
        /// <summary>
        /// Test GetEventSubscriptions
        /// </summary>
        [Test]
        public void GetEventSubscriptionsTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string eventSubscriptionId = null;
            //string eventName = null;
            //string eventType = null;
            //string executionId = null;
            //string processInstanceId = null;
            //string activityId = null;
            //string tenantIdIn = null;
            //bool? withoutTenantId = null;
            //bool? includeEventSubscriptionsWithoutTenantId = null;
            //string sortBy = null;
            //string sortOrder = null;
            //int? firstResult = null;
            //int? maxResults = null;
            //var response = instance.GetEventSubscriptions(eventSubscriptionId, eventName, eventType, executionId, processInstanceId, activityId, tenantIdIn, withoutTenantId, includeEventSubscriptionsWithoutTenantId, sortBy, sortOrder, firstResult, maxResults);
            //Assert.IsInstanceOf(typeof(List<EventSubscriptionDto>), response, "response is List<EventSubscriptionDto>");
        }
        
        /// <summary>
        /// Test GetEventSubscriptionsCount
        /// </summary>
        [Test]
        public void GetEventSubscriptionsCountTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string eventSubscriptionId = null;
            //string eventName = null;
            //string eventType = null;
            //string executionId = null;
            //string processInstanceId = null;
            //string activityId = null;
            //string tenantIdIn = null;
            //bool? withoutTenantId = null;
            //bool? includeEventSubscriptionsWithoutTenantId = null;
            //var response = instance.GetEventSubscriptionsCount(eventSubscriptionId, eventName, eventType, executionId, processInstanceId, activityId, tenantIdIn, withoutTenantId, includeEventSubscriptionsWithoutTenantId);
            //Assert.IsInstanceOf(typeof(CountResultDto), response, "response is CountResultDto");
        }
        
    }

}
