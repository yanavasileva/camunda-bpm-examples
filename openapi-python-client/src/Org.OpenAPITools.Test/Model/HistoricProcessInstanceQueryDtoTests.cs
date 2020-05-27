/* 
 * Camunda BPM REST API
 *
 * OpenApi Spec for Camunda BPM REST API.
 *
 * The version of the OpenAPI document: 7.13.0
 * 
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */


using NUnit.Framework;

using System;
using System.Linq;
using System.IO;
using System.Collections.Generic;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Model;
using Org.OpenAPITools.Client;
using System.Reflection;
using Newtonsoft.Json;

namespace Org.OpenAPITools.Test
{
    /// <summary>
    ///  Class for testing HistoricProcessInstanceQueryDto
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by OpenAPI Generator (https://openapi-generator.tech).
    /// Please update the test case below to test the model.
    /// </remarks>
    public class HistoricProcessInstanceQueryDtoTests
    {
        // TODO uncomment below to declare an instance variable for HistoricProcessInstanceQueryDto
        //private HistoricProcessInstanceQueryDto instance;

        /// <summary>
        /// Setup before each test
        /// </summary>
        [SetUp]
        public void Init()
        {
            // TODO uncomment below to create an instance of HistoricProcessInstanceQueryDto
            //instance = new HistoricProcessInstanceQueryDto();
        }

        /// <summary>
        /// Clean up after each test
        /// </summary>
        [TearDown]
        public void Cleanup()
        {

        }

        /// <summary>
        /// Test an instance of HistoricProcessInstanceQueryDto
        /// </summary>
        [Test]
        public void HistoricProcessInstanceQueryDtoInstanceTest()
        {
            // TODO uncomment below to test "IsInstanceOf" HistoricProcessInstanceQueryDto
            //Assert.IsInstanceOf(typeof(HistoricProcessInstanceQueryDto), instance);
        }


        /// <summary>
        /// Test the property 'ProcessInstanceId'
        /// </summary>
        [Test]
        public void ProcessInstanceIdTest()
        {
            // TODO unit test for the property 'ProcessInstanceId'
        }
        /// <summary>
        /// Test the property 'ProcessInstanceIds'
        /// </summary>
        [Test]
        public void ProcessInstanceIdsTest()
        {
            // TODO unit test for the property 'ProcessInstanceIds'
        }
        /// <summary>
        /// Test the property 'ProcessDefinitionId'
        /// </summary>
        [Test]
        public void ProcessDefinitionIdTest()
        {
            // TODO unit test for the property 'ProcessDefinitionId'
        }
        /// <summary>
        /// Test the property 'ProcessDefinitionKey'
        /// </summary>
        [Test]
        public void ProcessDefinitionKeyTest()
        {
            // TODO unit test for the property 'ProcessDefinitionKey'
        }
        /// <summary>
        /// Test the property 'ProcessDefinitionKeyIn'
        /// </summary>
        [Test]
        public void ProcessDefinitionKeyInTest()
        {
            // TODO unit test for the property 'ProcessDefinitionKeyIn'
        }
        /// <summary>
        /// Test the property 'ProcessDefinitionName'
        /// </summary>
        [Test]
        public void ProcessDefinitionNameTest()
        {
            // TODO unit test for the property 'ProcessDefinitionName'
        }
        /// <summary>
        /// Test the property 'ProcessDefinitionNameLike'
        /// </summary>
        [Test]
        public void ProcessDefinitionNameLikeTest()
        {
            // TODO unit test for the property 'ProcessDefinitionNameLike'
        }
        /// <summary>
        /// Test the property 'ProcessDefinitionKeyNotIn'
        /// </summary>
        [Test]
        public void ProcessDefinitionKeyNotInTest()
        {
            // TODO unit test for the property 'ProcessDefinitionKeyNotIn'
        }
        /// <summary>
        /// Test the property 'ProcessInstanceBusinessKey'
        /// </summary>
        [Test]
        public void ProcessInstanceBusinessKeyTest()
        {
            // TODO unit test for the property 'ProcessInstanceBusinessKey'
        }
        /// <summary>
        /// Test the property 'ProcessInstanceBusinessKeyLike'
        /// </summary>
        [Test]
        public void ProcessInstanceBusinessKeyLikeTest()
        {
            // TODO unit test for the property 'ProcessInstanceBusinessKeyLike'
        }
        /// <summary>
        /// Test the property 'RootProcessInstances'
        /// </summary>
        [Test]
        public void RootProcessInstancesTest()
        {
            // TODO unit test for the property 'RootProcessInstances'
        }
        /// <summary>
        /// Test the property 'Finished'
        /// </summary>
        [Test]
        public void FinishedTest()
        {
            // TODO unit test for the property 'Finished'
        }
        /// <summary>
        /// Test the property 'Unfinished'
        /// </summary>
        [Test]
        public void UnfinishedTest()
        {
            // TODO unit test for the property 'Unfinished'
        }
        /// <summary>
        /// Test the property 'WithIncidents'
        /// </summary>
        [Test]
        public void WithIncidentsTest()
        {
            // TODO unit test for the property 'WithIncidents'
        }
        /// <summary>
        /// Test the property 'WithRootIncidents'
        /// </summary>
        [Test]
        public void WithRootIncidentsTest()
        {
            // TODO unit test for the property 'WithRootIncidents'
        }
        /// <summary>
        /// Test the property 'IncidentType'
        /// </summary>
        [Test]
        public void IncidentTypeTest()
        {
            // TODO unit test for the property 'IncidentType'
        }
        /// <summary>
        /// Test the property 'IncidentStatus'
        /// </summary>
        [Test]
        public void IncidentStatusTest()
        {
            // TODO unit test for the property 'IncidentStatus'
        }
        /// <summary>
        /// Test the property 'IncidentMessage'
        /// </summary>
        [Test]
        public void IncidentMessageTest()
        {
            // TODO unit test for the property 'IncidentMessage'
        }
        /// <summary>
        /// Test the property 'IncidentMessageLike'
        /// </summary>
        [Test]
        public void IncidentMessageLikeTest()
        {
            // TODO unit test for the property 'IncidentMessageLike'
        }
        /// <summary>
        /// Test the property 'StartedBefore'
        /// </summary>
        [Test]
        public void StartedBeforeTest()
        {
            // TODO unit test for the property 'StartedBefore'
        }
        /// <summary>
        /// Test the property 'StartedAfter'
        /// </summary>
        [Test]
        public void StartedAfterTest()
        {
            // TODO unit test for the property 'StartedAfter'
        }
        /// <summary>
        /// Test the property 'FinishedBefore'
        /// </summary>
        [Test]
        public void FinishedBeforeTest()
        {
            // TODO unit test for the property 'FinishedBefore'
        }
        /// <summary>
        /// Test the property 'FinishedAfter'
        /// </summary>
        [Test]
        public void FinishedAfterTest()
        {
            // TODO unit test for the property 'FinishedAfter'
        }
        /// <summary>
        /// Test the property 'ExecutedActivityAfter'
        /// </summary>
        [Test]
        public void ExecutedActivityAfterTest()
        {
            // TODO unit test for the property 'ExecutedActivityAfter'
        }
        /// <summary>
        /// Test the property 'ExecutedActivityBefore'
        /// </summary>
        [Test]
        public void ExecutedActivityBeforeTest()
        {
            // TODO unit test for the property 'ExecutedActivityBefore'
        }
        /// <summary>
        /// Test the property 'ExecutedJobAfter'
        /// </summary>
        [Test]
        public void ExecutedJobAfterTest()
        {
            // TODO unit test for the property 'ExecutedJobAfter'
        }
        /// <summary>
        /// Test the property 'ExecutedJobBefore'
        /// </summary>
        [Test]
        public void ExecutedJobBeforeTest()
        {
            // TODO unit test for the property 'ExecutedJobBefore'
        }
        /// <summary>
        /// Test the property 'StartedBy'
        /// </summary>
        [Test]
        public void StartedByTest()
        {
            // TODO unit test for the property 'StartedBy'
        }
        /// <summary>
        /// Test the property 'SuperProcessInstanceId'
        /// </summary>
        [Test]
        public void SuperProcessInstanceIdTest()
        {
            // TODO unit test for the property 'SuperProcessInstanceId'
        }
        /// <summary>
        /// Test the property 'SubProcessInstanceId'
        /// </summary>
        [Test]
        public void SubProcessInstanceIdTest()
        {
            // TODO unit test for the property 'SubProcessInstanceId'
        }
        /// <summary>
        /// Test the property 'SuperCaseInstanceId'
        /// </summary>
        [Test]
        public void SuperCaseInstanceIdTest()
        {
            // TODO unit test for the property 'SuperCaseInstanceId'
        }
        /// <summary>
        /// Test the property 'SubCaseInstanceId'
        /// </summary>
        [Test]
        public void SubCaseInstanceIdTest()
        {
            // TODO unit test for the property 'SubCaseInstanceId'
        }
        /// <summary>
        /// Test the property 'CaseInstanceId'
        /// </summary>
        [Test]
        public void CaseInstanceIdTest()
        {
            // TODO unit test for the property 'CaseInstanceId'
        }
        /// <summary>
        /// Test the property 'TenantIdIn'
        /// </summary>
        [Test]
        public void TenantIdInTest()
        {
            // TODO unit test for the property 'TenantIdIn'
        }
        /// <summary>
        /// Test the property 'WithoutTenantId'
        /// </summary>
        [Test]
        public void WithoutTenantIdTest()
        {
            // TODO unit test for the property 'WithoutTenantId'
        }
        /// <summary>
        /// Test the property 'ExecutedActivityIdIn'
        /// </summary>
        [Test]
        public void ExecutedActivityIdInTest()
        {
            // TODO unit test for the property 'ExecutedActivityIdIn'
        }
        /// <summary>
        /// Test the property 'ActiveActivityIdIn'
        /// </summary>
        [Test]
        public void ActiveActivityIdInTest()
        {
            // TODO unit test for the property 'ActiveActivityIdIn'
        }
        /// <summary>
        /// Test the property 'Active'
        /// </summary>
        [Test]
        public void ActiveTest()
        {
            // TODO unit test for the property 'Active'
        }
        /// <summary>
        /// Test the property 'Suspended'
        /// </summary>
        [Test]
        public void SuspendedTest()
        {
            // TODO unit test for the property 'Suspended'
        }
        /// <summary>
        /// Test the property 'Completed'
        /// </summary>
        [Test]
        public void CompletedTest()
        {
            // TODO unit test for the property 'Completed'
        }
        /// <summary>
        /// Test the property 'ExternallyTerminated'
        /// </summary>
        [Test]
        public void ExternallyTerminatedTest()
        {
            // TODO unit test for the property 'ExternallyTerminated'
        }
        /// <summary>
        /// Test the property 'InternallyTerminated'
        /// </summary>
        [Test]
        public void InternallyTerminatedTest()
        {
            // TODO unit test for the property 'InternallyTerminated'
        }
        /// <summary>
        /// Test the property 'Variables'
        /// </summary>
        [Test]
        public void VariablesTest()
        {
            // TODO unit test for the property 'Variables'
        }
        /// <summary>
        /// Test the property 'VariableNamesIgnoreCase'
        /// </summary>
        [Test]
        public void VariableNamesIgnoreCaseTest()
        {
            // TODO unit test for the property 'VariableNamesIgnoreCase'
        }
        /// <summary>
        /// Test the property 'VariableValuesIgnoreCase'
        /// </summary>
        [Test]
        public void VariableValuesIgnoreCaseTest()
        {
            // TODO unit test for the property 'VariableValuesIgnoreCase'
        }
        /// <summary>
        /// Test the property 'OrQueries'
        /// </summary>
        [Test]
        public void OrQueriesTest()
        {
            // TODO unit test for the property 'OrQueries'
        }
        /// <summary>
        /// Test the property 'Sorting'
        /// </summary>
        [Test]
        public void SortingTest()
        {
            // TODO unit test for the property 'Sorting'
        }

    }

}
