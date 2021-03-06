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
    ///  Class for testing TaskCommentApi
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by OpenAPI Generator (https://openapi-generator.tech).
    /// Please update the test case below to test the API endpoint.
    /// </remarks>
    public class TaskCommentApiTests
    {
        private TaskCommentApi instance;

        /// <summary>
        /// Setup before each unit test
        /// </summary>
        [SetUp]
        public void Init()
        {
            instance = new TaskCommentApi();
        }

        /// <summary>
        /// Clean up after each unit test
        /// </summary>
        [TearDown]
        public void Cleanup()
        {

        }

        /// <summary>
        /// Test an instance of TaskCommentApi
        /// </summary>
        [Test]
        public void InstanceTest()
        {
            // TODO uncomment below to test 'IsInstanceOf' TaskCommentApi
            //Assert.IsInstanceOf(typeof(TaskCommentApi), instance);
        }

        
        /// <summary>
        /// Test CreateComment
        /// </summary>
        [Test]
        public void CreateCommentTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string id = null;
            //CommentDto commentDto = null;
            //var response = instance.CreateComment(id, commentDto);
            //Assert.IsInstanceOf(typeof(CommentDto), response, "response is CommentDto");
        }
        
        /// <summary>
        /// Test GetComment
        /// </summary>
        [Test]
        public void GetCommentTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string id = null;
            //string commentId = null;
            //var response = instance.GetComment(id, commentId);
            //Assert.IsInstanceOf(typeof(CommentDto), response, "response is CommentDto");
        }
        
        /// <summary>
        /// Test GetComments
        /// </summary>
        [Test]
        public void GetCommentsTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string id = null;
            //var response = instance.GetComments(id);
            //Assert.IsInstanceOf(typeof(List<CommentDto>), response, "response is List<CommentDto>");
        }
        
    }

}
