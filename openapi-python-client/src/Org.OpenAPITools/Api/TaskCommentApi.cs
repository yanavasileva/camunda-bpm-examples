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
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using RestSharp;
using Org.OpenAPITools.Client;
using Org.OpenAPITools.Model;

namespace Org.OpenAPITools.Api
{
    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public interface ITaskCommentApi : IApiAccessor
    {
        #region Synchronous Operations
        /// <summary>
        /// 
        /// </summary>
        /// <remarks>
        /// Creates a comment for a task by id.
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="id">The id of the task to add the comment to.</param>
        /// <param name="commentDto">**Note:** Only the &#x60;message&#x60; property will be used. Every other property passed to this endpoint will be ignored. (optional)</param>
        /// <returns>CommentDto</returns>
        CommentDto CreateComment (string id, CommentDto commentDto = default(CommentDto));

        /// <summary>
        /// 
        /// </summary>
        /// <remarks>
        /// Creates a comment for a task by id.
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="id">The id of the task to add the comment to.</param>
        /// <param name="commentDto">**Note:** Only the &#x60;message&#x60; property will be used. Every other property passed to this endpoint will be ignored. (optional)</param>
        /// <returns>ApiResponse of CommentDto</returns>
        ApiResponse<CommentDto> CreateCommentWithHttpInfo (string id, CommentDto commentDto = default(CommentDto));
        /// <summary>
        /// 
        /// </summary>
        /// <remarks>
        /// Retrieves a task comment by task id and comment id.
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="id">The id of the task.</param>
        /// <param name="commentId">The id of the comment to be retrieved.</param>
        /// <returns>CommentDto</returns>
        CommentDto GetComment (string id, string commentId);

        /// <summary>
        /// 
        /// </summary>
        /// <remarks>
        /// Retrieves a task comment by task id and comment id.
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="id">The id of the task.</param>
        /// <param name="commentId">The id of the comment to be retrieved.</param>
        /// <returns>ApiResponse of CommentDto</returns>
        ApiResponse<CommentDto> GetCommentWithHttpInfo (string id, string commentId);
        /// <summary>
        /// 
        /// </summary>
        /// <remarks>
        /// Gets the comments for a task by id.
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="id">The id of the task to retrieve the comments for.</param>
        /// <returns>List&lt;CommentDto&gt;</returns>
        List<CommentDto> GetComments (string id);

        /// <summary>
        /// 
        /// </summary>
        /// <remarks>
        /// Gets the comments for a task by id.
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="id">The id of the task to retrieve the comments for.</param>
        /// <returns>ApiResponse of List&lt;CommentDto&gt;</returns>
        ApiResponse<List<CommentDto>> GetCommentsWithHttpInfo (string id);
        #endregion Synchronous Operations
        #region Asynchronous Operations
        /// <summary>
        /// 
        /// </summary>
        /// <remarks>
        /// Creates a comment for a task by id.
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="id">The id of the task to add the comment to.</param>
        /// <param name="commentDto">**Note:** Only the &#x60;message&#x60; property will be used. Every other property passed to this endpoint will be ignored. (optional)</param>
        /// <returns>Task of CommentDto</returns>
        System.Threading.Tasks.Task<CommentDto> CreateCommentAsync (string id, CommentDto commentDto = default(CommentDto));

        /// <summary>
        /// 
        /// </summary>
        /// <remarks>
        /// Creates a comment for a task by id.
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="id">The id of the task to add the comment to.</param>
        /// <param name="commentDto">**Note:** Only the &#x60;message&#x60; property will be used. Every other property passed to this endpoint will be ignored. (optional)</param>
        /// <returns>Task of ApiResponse (CommentDto)</returns>
        System.Threading.Tasks.Task<ApiResponse<CommentDto>> CreateCommentAsyncWithHttpInfo (string id, CommentDto commentDto = default(CommentDto));
        /// <summary>
        /// 
        /// </summary>
        /// <remarks>
        /// Retrieves a task comment by task id and comment id.
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="id">The id of the task.</param>
        /// <param name="commentId">The id of the comment to be retrieved.</param>
        /// <returns>Task of CommentDto</returns>
        System.Threading.Tasks.Task<CommentDto> GetCommentAsync (string id, string commentId);

        /// <summary>
        /// 
        /// </summary>
        /// <remarks>
        /// Retrieves a task comment by task id and comment id.
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="id">The id of the task.</param>
        /// <param name="commentId">The id of the comment to be retrieved.</param>
        /// <returns>Task of ApiResponse (CommentDto)</returns>
        System.Threading.Tasks.Task<ApiResponse<CommentDto>> GetCommentAsyncWithHttpInfo (string id, string commentId);
        /// <summary>
        /// 
        /// </summary>
        /// <remarks>
        /// Gets the comments for a task by id.
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="id">The id of the task to retrieve the comments for.</param>
        /// <returns>Task of List&lt;CommentDto&gt;</returns>
        System.Threading.Tasks.Task<List<CommentDto>> GetCommentsAsync (string id);

        /// <summary>
        /// 
        /// </summary>
        /// <remarks>
        /// Gets the comments for a task by id.
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="id">The id of the task to retrieve the comments for.</param>
        /// <returns>Task of ApiResponse (List&lt;CommentDto&gt;)</returns>
        System.Threading.Tasks.Task<ApiResponse<List<CommentDto>>> GetCommentsAsyncWithHttpInfo (string id);
        #endregion Asynchronous Operations
    }

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public partial class TaskCommentApi : ITaskCommentApi
    {
        private Org.OpenAPITools.Client.ExceptionFactory _exceptionFactory = (name, response) => null;

        /// <summary>
        /// Initializes a new instance of the <see cref="TaskCommentApi"/> class.
        /// </summary>
        /// <returns></returns>
        public TaskCommentApi(String basePath)
        {
            this.Configuration = new Org.OpenAPITools.Client.Configuration { BasePath = basePath };

            ExceptionFactory = Org.OpenAPITools.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="TaskCommentApi"/> class
        /// </summary>
        /// <returns></returns>
        public TaskCommentApi()
        {
            this.Configuration = Org.OpenAPITools.Client.Configuration.Default;

            ExceptionFactory = Org.OpenAPITools.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="TaskCommentApi"/> class
        /// using Configuration object
        /// </summary>
        /// <param name="configuration">An instance of Configuration</param>
        /// <returns></returns>
        public TaskCommentApi(Org.OpenAPITools.Client.Configuration configuration = null)
        {
            if (configuration == null) // use the default one in Configuration
                this.Configuration = Org.OpenAPITools.Client.Configuration.Default;
            else
                this.Configuration = configuration;

            ExceptionFactory = Org.OpenAPITools.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Gets the base path of the API client.
        /// </summary>
        /// <value>The base path</value>
        public String GetBasePath()
        {
            return this.Configuration.ApiClient.RestClient.BaseUrl.ToString();
        }

        /// <summary>
        /// Sets the base path of the API client.
        /// </summary>
        /// <value>The base path</value>
        [Obsolete("SetBasePath is deprecated, please do 'Configuration.ApiClient = new ApiClient(\"http://new-path\")' instead.")]
        public void SetBasePath(String basePath)
        {
            // do nothing
        }

        /// <summary>
        /// Gets or sets the configuration object
        /// </summary>
        /// <value>An instance of the Configuration</value>
        public Org.OpenAPITools.Client.Configuration Configuration {get; set;}

        /// <summary>
        /// Provides a factory method hook for the creation of exceptions.
        /// </summary>
        public Org.OpenAPITools.Client.ExceptionFactory ExceptionFactory
        {
            get
            {
                if (_exceptionFactory != null && _exceptionFactory.GetInvocationList().Length > 1)
                {
                    throw new InvalidOperationException("Multicast delegate for ExceptionFactory is unsupported.");
                }
                return _exceptionFactory;
            }
            set { _exceptionFactory = value; }
        }

        /// <summary>
        /// Gets the default header.
        /// </summary>
        /// <returns>Dictionary of HTTP header</returns>
        [Obsolete("DefaultHeader is deprecated, please use Configuration.DefaultHeader instead.")]
        public IDictionary<String, String> DefaultHeader()
        {
            return new ReadOnlyDictionary<string, string>(this.Configuration.DefaultHeader);
        }

        /// <summary>
        /// Add default header.
        /// </summary>
        /// <param name="key">Header field name.</param>
        /// <param name="value">Header field value.</param>
        /// <returns></returns>
        [Obsolete("AddDefaultHeader is deprecated, please use Configuration.AddDefaultHeader instead.")]
        public void AddDefaultHeader(string key, string value)
        {
            this.Configuration.AddDefaultHeader(key, value);
        }

        /// <summary>
        ///  Creates a comment for a task by id.
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="id">The id of the task to add the comment to.</param>
        /// <param name="commentDto">**Note:** Only the &#x60;message&#x60; property will be used. Every other property passed to this endpoint will be ignored. (optional)</param>
        /// <returns>CommentDto</returns>
        public CommentDto CreateComment (string id, CommentDto commentDto = default(CommentDto))
        {
             ApiResponse<CommentDto> localVarResponse = CreateCommentWithHttpInfo(id, commentDto);
             return localVarResponse.Data;
        }

        /// <summary>
        ///  Creates a comment for a task by id.
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="id">The id of the task to add the comment to.</param>
        /// <param name="commentDto">**Note:** Only the &#x60;message&#x60; property will be used. Every other property passed to this endpoint will be ignored. (optional)</param>
        /// <returns>ApiResponse of CommentDto</returns>
        public ApiResponse<CommentDto> CreateCommentWithHttpInfo (string id, CommentDto commentDto = default(CommentDto))
        {
            // verify the required parameter 'id' is set
            if (id == null)
                throw new ApiException(400, "Missing required parameter 'id' when calling TaskCommentApi->CreateComment");

            var localVarPath = "/task/{id}/comment/create";
            var localVarPathParams = new Dictionary<String, String>();
            var localVarQueryParams = new List<KeyValuePair<String, String>>();
            var localVarHeaderParams = new Dictionary<String, String>(this.Configuration.DefaultHeader);
            var localVarFormParams = new Dictionary<String, String>();
            var localVarFileParams = new Dictionary<String, FileParameter>();
            Object localVarPostBody = null;

            // to determine the Content-Type header
            String[] localVarHttpContentTypes = new String[] {
                "application/json"
            };
            String localVarHttpContentType = this.Configuration.ApiClient.SelectHeaderContentType(localVarHttpContentTypes);

            // to determine the Accept header
            String[] localVarHttpHeaderAccepts = new String[] {
                "application/json"
            };
            String localVarHttpHeaderAccept = this.Configuration.ApiClient.SelectHeaderAccept(localVarHttpHeaderAccepts);
            if (localVarHttpHeaderAccept != null)
                localVarHeaderParams.Add("Accept", localVarHttpHeaderAccept);

            if (id != null) localVarPathParams.Add("id", this.Configuration.ApiClient.ParameterToString(id)); // path parameter
            if (commentDto != null && commentDto.GetType() != typeof(byte[]))
            {
                localVarPostBody = this.Configuration.ApiClient.Serialize(commentDto); // http body (model) parameter
            }
            else
            {
                localVarPostBody = commentDto; // byte array
            }


            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) this.Configuration.ApiClient.CallApi(localVarPath,
                Method.POST, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("CreateComment", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<CommentDto>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (CommentDto) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(CommentDto)));
        }

        /// <summary>
        ///  Creates a comment for a task by id.
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="id">The id of the task to add the comment to.</param>
        /// <param name="commentDto">**Note:** Only the &#x60;message&#x60; property will be used. Every other property passed to this endpoint will be ignored. (optional)</param>
        /// <returns>Task of CommentDto</returns>
        public async System.Threading.Tasks.Task<CommentDto> CreateCommentAsync (string id, CommentDto commentDto = default(CommentDto))
        {
             ApiResponse<CommentDto> localVarResponse = await CreateCommentAsyncWithHttpInfo(id, commentDto);
             return localVarResponse.Data;

        }

        /// <summary>
        ///  Creates a comment for a task by id.
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="id">The id of the task to add the comment to.</param>
        /// <param name="commentDto">**Note:** Only the &#x60;message&#x60; property will be used. Every other property passed to this endpoint will be ignored. (optional)</param>
        /// <returns>Task of ApiResponse (CommentDto)</returns>
        public async System.Threading.Tasks.Task<ApiResponse<CommentDto>> CreateCommentAsyncWithHttpInfo (string id, CommentDto commentDto = default(CommentDto))
        {
            // verify the required parameter 'id' is set
            if (id == null)
                throw new ApiException(400, "Missing required parameter 'id' when calling TaskCommentApi->CreateComment");

            var localVarPath = "/task/{id}/comment/create";
            var localVarPathParams = new Dictionary<String, String>();
            var localVarQueryParams = new List<KeyValuePair<String, String>>();
            var localVarHeaderParams = new Dictionary<String, String>(this.Configuration.DefaultHeader);
            var localVarFormParams = new Dictionary<String, String>();
            var localVarFileParams = new Dictionary<String, FileParameter>();
            Object localVarPostBody = null;

            // to determine the Content-Type header
            String[] localVarHttpContentTypes = new String[] {
                "application/json"
            };
            String localVarHttpContentType = this.Configuration.ApiClient.SelectHeaderContentType(localVarHttpContentTypes);

            // to determine the Accept header
            String[] localVarHttpHeaderAccepts = new String[] {
                "application/json"
            };
            String localVarHttpHeaderAccept = this.Configuration.ApiClient.SelectHeaderAccept(localVarHttpHeaderAccepts);
            if (localVarHttpHeaderAccept != null)
                localVarHeaderParams.Add("Accept", localVarHttpHeaderAccept);

            if (id != null) localVarPathParams.Add("id", this.Configuration.ApiClient.ParameterToString(id)); // path parameter
            if (commentDto != null && commentDto.GetType() != typeof(byte[]))
            {
                localVarPostBody = this.Configuration.ApiClient.Serialize(commentDto); // http body (model) parameter
            }
            else
            {
                localVarPostBody = commentDto; // byte array
            }


            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) await this.Configuration.ApiClient.CallApiAsync(localVarPath,
                Method.POST, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("CreateComment", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<CommentDto>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (CommentDto) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(CommentDto)));
        }

        /// <summary>
        ///  Retrieves a task comment by task id and comment id.
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="id">The id of the task.</param>
        /// <param name="commentId">The id of the comment to be retrieved.</param>
        /// <returns>CommentDto</returns>
        public CommentDto GetComment (string id, string commentId)
        {
             ApiResponse<CommentDto> localVarResponse = GetCommentWithHttpInfo(id, commentId);
             return localVarResponse.Data;
        }

        /// <summary>
        ///  Retrieves a task comment by task id and comment id.
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="id">The id of the task.</param>
        /// <param name="commentId">The id of the comment to be retrieved.</param>
        /// <returns>ApiResponse of CommentDto</returns>
        public ApiResponse<CommentDto> GetCommentWithHttpInfo (string id, string commentId)
        {
            // verify the required parameter 'id' is set
            if (id == null)
                throw new ApiException(400, "Missing required parameter 'id' when calling TaskCommentApi->GetComment");
            // verify the required parameter 'commentId' is set
            if (commentId == null)
                throw new ApiException(400, "Missing required parameter 'commentId' when calling TaskCommentApi->GetComment");

            var localVarPath = "/task/{id}/comment/{commentId}";
            var localVarPathParams = new Dictionary<String, String>();
            var localVarQueryParams = new List<KeyValuePair<String, String>>();
            var localVarHeaderParams = new Dictionary<String, String>(this.Configuration.DefaultHeader);
            var localVarFormParams = new Dictionary<String, String>();
            var localVarFileParams = new Dictionary<String, FileParameter>();
            Object localVarPostBody = null;

            // to determine the Content-Type header
            String[] localVarHttpContentTypes = new String[] {
            };
            String localVarHttpContentType = this.Configuration.ApiClient.SelectHeaderContentType(localVarHttpContentTypes);

            // to determine the Accept header
            String[] localVarHttpHeaderAccepts = new String[] {
                "application/json"
            };
            String localVarHttpHeaderAccept = this.Configuration.ApiClient.SelectHeaderAccept(localVarHttpHeaderAccepts);
            if (localVarHttpHeaderAccept != null)
                localVarHeaderParams.Add("Accept", localVarHttpHeaderAccept);

            if (id != null) localVarPathParams.Add("id", this.Configuration.ApiClient.ParameterToString(id)); // path parameter
            if (commentId != null) localVarPathParams.Add("commentId", this.Configuration.ApiClient.ParameterToString(commentId)); // path parameter


            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) this.Configuration.ApiClient.CallApi(localVarPath,
                Method.GET, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("GetComment", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<CommentDto>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (CommentDto) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(CommentDto)));
        }

        /// <summary>
        ///  Retrieves a task comment by task id and comment id.
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="id">The id of the task.</param>
        /// <param name="commentId">The id of the comment to be retrieved.</param>
        /// <returns>Task of CommentDto</returns>
        public async System.Threading.Tasks.Task<CommentDto> GetCommentAsync (string id, string commentId)
        {
             ApiResponse<CommentDto> localVarResponse = await GetCommentAsyncWithHttpInfo(id, commentId);
             return localVarResponse.Data;

        }

        /// <summary>
        ///  Retrieves a task comment by task id and comment id.
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="id">The id of the task.</param>
        /// <param name="commentId">The id of the comment to be retrieved.</param>
        /// <returns>Task of ApiResponse (CommentDto)</returns>
        public async System.Threading.Tasks.Task<ApiResponse<CommentDto>> GetCommentAsyncWithHttpInfo (string id, string commentId)
        {
            // verify the required parameter 'id' is set
            if (id == null)
                throw new ApiException(400, "Missing required parameter 'id' when calling TaskCommentApi->GetComment");
            // verify the required parameter 'commentId' is set
            if (commentId == null)
                throw new ApiException(400, "Missing required parameter 'commentId' when calling TaskCommentApi->GetComment");

            var localVarPath = "/task/{id}/comment/{commentId}";
            var localVarPathParams = new Dictionary<String, String>();
            var localVarQueryParams = new List<KeyValuePair<String, String>>();
            var localVarHeaderParams = new Dictionary<String, String>(this.Configuration.DefaultHeader);
            var localVarFormParams = new Dictionary<String, String>();
            var localVarFileParams = new Dictionary<String, FileParameter>();
            Object localVarPostBody = null;

            // to determine the Content-Type header
            String[] localVarHttpContentTypes = new String[] {
            };
            String localVarHttpContentType = this.Configuration.ApiClient.SelectHeaderContentType(localVarHttpContentTypes);

            // to determine the Accept header
            String[] localVarHttpHeaderAccepts = new String[] {
                "application/json"
            };
            String localVarHttpHeaderAccept = this.Configuration.ApiClient.SelectHeaderAccept(localVarHttpHeaderAccepts);
            if (localVarHttpHeaderAccept != null)
                localVarHeaderParams.Add("Accept", localVarHttpHeaderAccept);

            if (id != null) localVarPathParams.Add("id", this.Configuration.ApiClient.ParameterToString(id)); // path parameter
            if (commentId != null) localVarPathParams.Add("commentId", this.Configuration.ApiClient.ParameterToString(commentId)); // path parameter


            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) await this.Configuration.ApiClient.CallApiAsync(localVarPath,
                Method.GET, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("GetComment", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<CommentDto>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (CommentDto) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(CommentDto)));
        }

        /// <summary>
        ///  Gets the comments for a task by id.
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="id">The id of the task to retrieve the comments for.</param>
        /// <returns>List&lt;CommentDto&gt;</returns>
        public List<CommentDto> GetComments (string id)
        {
             ApiResponse<List<CommentDto>> localVarResponse = GetCommentsWithHttpInfo(id);
             return localVarResponse.Data;
        }

        /// <summary>
        ///  Gets the comments for a task by id.
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="id">The id of the task to retrieve the comments for.</param>
        /// <returns>ApiResponse of List&lt;CommentDto&gt;</returns>
        public ApiResponse<List<CommentDto>> GetCommentsWithHttpInfo (string id)
        {
            // verify the required parameter 'id' is set
            if (id == null)
                throw new ApiException(400, "Missing required parameter 'id' when calling TaskCommentApi->GetComments");

            var localVarPath = "/task/{id}/comment";
            var localVarPathParams = new Dictionary<String, String>();
            var localVarQueryParams = new List<KeyValuePair<String, String>>();
            var localVarHeaderParams = new Dictionary<String, String>(this.Configuration.DefaultHeader);
            var localVarFormParams = new Dictionary<String, String>();
            var localVarFileParams = new Dictionary<String, FileParameter>();
            Object localVarPostBody = null;

            // to determine the Content-Type header
            String[] localVarHttpContentTypes = new String[] {
            };
            String localVarHttpContentType = this.Configuration.ApiClient.SelectHeaderContentType(localVarHttpContentTypes);

            // to determine the Accept header
            String[] localVarHttpHeaderAccepts = new String[] {
                "application/json"
            };
            String localVarHttpHeaderAccept = this.Configuration.ApiClient.SelectHeaderAccept(localVarHttpHeaderAccepts);
            if (localVarHttpHeaderAccept != null)
                localVarHeaderParams.Add("Accept", localVarHttpHeaderAccept);

            if (id != null) localVarPathParams.Add("id", this.Configuration.ApiClient.ParameterToString(id)); // path parameter


            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) this.Configuration.ApiClient.CallApi(localVarPath,
                Method.GET, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("GetComments", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<List<CommentDto>>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (List<CommentDto>) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(List<CommentDto>)));
        }

        /// <summary>
        ///  Gets the comments for a task by id.
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="id">The id of the task to retrieve the comments for.</param>
        /// <returns>Task of List&lt;CommentDto&gt;</returns>
        public async System.Threading.Tasks.Task<List<CommentDto>> GetCommentsAsync (string id)
        {
             ApiResponse<List<CommentDto>> localVarResponse = await GetCommentsAsyncWithHttpInfo(id);
             return localVarResponse.Data;

        }

        /// <summary>
        ///  Gets the comments for a task by id.
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="id">The id of the task to retrieve the comments for.</param>
        /// <returns>Task of ApiResponse (List&lt;CommentDto&gt;)</returns>
        public async System.Threading.Tasks.Task<ApiResponse<List<CommentDto>>> GetCommentsAsyncWithHttpInfo (string id)
        {
            // verify the required parameter 'id' is set
            if (id == null)
                throw new ApiException(400, "Missing required parameter 'id' when calling TaskCommentApi->GetComments");

            var localVarPath = "/task/{id}/comment";
            var localVarPathParams = new Dictionary<String, String>();
            var localVarQueryParams = new List<KeyValuePair<String, String>>();
            var localVarHeaderParams = new Dictionary<String, String>(this.Configuration.DefaultHeader);
            var localVarFormParams = new Dictionary<String, String>();
            var localVarFileParams = new Dictionary<String, FileParameter>();
            Object localVarPostBody = null;

            // to determine the Content-Type header
            String[] localVarHttpContentTypes = new String[] {
            };
            String localVarHttpContentType = this.Configuration.ApiClient.SelectHeaderContentType(localVarHttpContentTypes);

            // to determine the Accept header
            String[] localVarHttpHeaderAccepts = new String[] {
                "application/json"
            };
            String localVarHttpHeaderAccept = this.Configuration.ApiClient.SelectHeaderAccept(localVarHttpHeaderAccepts);
            if (localVarHttpHeaderAccept != null)
                localVarHeaderParams.Add("Accept", localVarHttpHeaderAccept);

            if (id != null) localVarPathParams.Add("id", this.Configuration.ApiClient.ParameterToString(id)); // path parameter


            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) await this.Configuration.ApiClient.CallApiAsync(localVarPath,
                Method.GET, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("GetComments", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<List<CommentDto>>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (List<CommentDto>) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(List<CommentDto>)));
        }

    }
}