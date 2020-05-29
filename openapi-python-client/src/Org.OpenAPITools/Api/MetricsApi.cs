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
    public interface IMetricsApi : IApiAccessor
    {
        #region Synchronous Operations
        /// <summary>
        /// 
        /// </summary>
        /// <remarks>
        /// Retrieves the &#x60;sum&#x60; (count) for a given metric.
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="metricsName">The name of the metric.</param>
        /// <param name="startDate">The start date (inclusive). (optional)</param>
        /// <param name="endDate">The end date (exclusive). (optional)</param>
        /// <returns>MetricsResultDto</returns>
        MetricsResultDto GetMetrics (string metricsName, DateTime? startDate = default(DateTime?), DateTime? endDate = default(DateTime?));

        /// <summary>
        /// 
        /// </summary>
        /// <remarks>
        /// Retrieves the &#x60;sum&#x60; (count) for a given metric.
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="metricsName">The name of the metric.</param>
        /// <param name="startDate">The start date (inclusive). (optional)</param>
        /// <param name="endDate">The end date (exclusive). (optional)</param>
        /// <returns>ApiResponse of MetricsResultDto</returns>
        ApiResponse<MetricsResultDto> GetMetricsWithHttpInfo (string metricsName, DateTime? startDate = default(DateTime?), DateTime? endDate = default(DateTime?));
        /// <summary>
        /// 
        /// </summary>
        /// <remarks>
        /// Retrieves a list of metrics, aggregated for a given interval.
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="name">The name of the metric. (optional)</param>
        /// <param name="reporter">The name of the reporter (host), on which the metrics was logged. This will have value provided by the [hostname configuration property](https://docs.camunda.org/manual/7.13/reference/deployment-descriptors/tags/process-engine/#hostname). (optional)</param>
        /// <param name="startDate">The start date (inclusive). (optional)</param>
        /// <param name="endDate">The end date (exclusive). (optional)</param>
        /// <param name="firstResult">Pagination of results. Specifies the index of the first result to return. (optional)</param>
        /// <param name="maxResults">Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. (optional)</param>
        /// <param name="interval">The interval for which the metrics should be aggregated. Time unit is seconds. Default: The interval is set to 15 minutes (900 seconds). (optional, default to &quot;900&quot;)</param>
        /// <param name="aggregateByReporter">Aggregate metrics by reporter. (optional)</param>
        /// <returns>List&lt;MetricsIntervalResultDto&gt;</returns>
        List<MetricsIntervalResultDto> Interval (string name = default(string), string reporter = default(string), DateTime? startDate = default(DateTime?), DateTime? endDate = default(DateTime?), int? firstResult = default(int?), int? maxResults = default(int?), string interval = default(string), string aggregateByReporter = default(string));

        /// <summary>
        /// 
        /// </summary>
        /// <remarks>
        /// Retrieves a list of metrics, aggregated for a given interval.
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="name">The name of the metric. (optional)</param>
        /// <param name="reporter">The name of the reporter (host), on which the metrics was logged. This will have value provided by the [hostname configuration property](https://docs.camunda.org/manual/7.13/reference/deployment-descriptors/tags/process-engine/#hostname). (optional)</param>
        /// <param name="startDate">The start date (inclusive). (optional)</param>
        /// <param name="endDate">The end date (exclusive). (optional)</param>
        /// <param name="firstResult">Pagination of results. Specifies the index of the first result to return. (optional)</param>
        /// <param name="maxResults">Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. (optional)</param>
        /// <param name="interval">The interval for which the metrics should be aggregated. Time unit is seconds. Default: The interval is set to 15 minutes (900 seconds). (optional, default to &quot;900&quot;)</param>
        /// <param name="aggregateByReporter">Aggregate metrics by reporter. (optional)</param>
        /// <returns>ApiResponse of List&lt;MetricsIntervalResultDto&gt;</returns>
        ApiResponse<List<MetricsIntervalResultDto>> IntervalWithHttpInfo (string name = default(string), string reporter = default(string), DateTime? startDate = default(DateTime?), DateTime? endDate = default(DateTime?), int? firstResult = default(int?), int? maxResults = default(int?), string interval = default(string), string aggregateByReporter = default(string));
        #endregion Synchronous Operations
        #region Asynchronous Operations
        /// <summary>
        /// 
        /// </summary>
        /// <remarks>
        /// Retrieves the &#x60;sum&#x60; (count) for a given metric.
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="metricsName">The name of the metric.</param>
        /// <param name="startDate">The start date (inclusive). (optional)</param>
        /// <param name="endDate">The end date (exclusive). (optional)</param>
        /// <returns>Task of MetricsResultDto</returns>
        System.Threading.Tasks.Task<MetricsResultDto> GetMetricsAsync (string metricsName, DateTime? startDate = default(DateTime?), DateTime? endDate = default(DateTime?));

        /// <summary>
        /// 
        /// </summary>
        /// <remarks>
        /// Retrieves the &#x60;sum&#x60; (count) for a given metric.
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="metricsName">The name of the metric.</param>
        /// <param name="startDate">The start date (inclusive). (optional)</param>
        /// <param name="endDate">The end date (exclusive). (optional)</param>
        /// <returns>Task of ApiResponse (MetricsResultDto)</returns>
        System.Threading.Tasks.Task<ApiResponse<MetricsResultDto>> GetMetricsAsyncWithHttpInfo (string metricsName, DateTime? startDate = default(DateTime?), DateTime? endDate = default(DateTime?));
        /// <summary>
        /// 
        /// </summary>
        /// <remarks>
        /// Retrieves a list of metrics, aggregated for a given interval.
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="name">The name of the metric. (optional)</param>
        /// <param name="reporter">The name of the reporter (host), on which the metrics was logged. This will have value provided by the [hostname configuration property](https://docs.camunda.org/manual/7.13/reference/deployment-descriptors/tags/process-engine/#hostname). (optional)</param>
        /// <param name="startDate">The start date (inclusive). (optional)</param>
        /// <param name="endDate">The end date (exclusive). (optional)</param>
        /// <param name="firstResult">Pagination of results. Specifies the index of the first result to return. (optional)</param>
        /// <param name="maxResults">Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. (optional)</param>
        /// <param name="interval">The interval for which the metrics should be aggregated. Time unit is seconds. Default: The interval is set to 15 minutes (900 seconds). (optional, default to &quot;900&quot;)</param>
        /// <param name="aggregateByReporter">Aggregate metrics by reporter. (optional)</param>
        /// <returns>Task of List&lt;MetricsIntervalResultDto&gt;</returns>
        System.Threading.Tasks.Task<List<MetricsIntervalResultDto>> IntervalAsync (string name = default(string), string reporter = default(string), DateTime? startDate = default(DateTime?), DateTime? endDate = default(DateTime?), int? firstResult = default(int?), int? maxResults = default(int?), string interval = default(string), string aggregateByReporter = default(string));

        /// <summary>
        /// 
        /// </summary>
        /// <remarks>
        /// Retrieves a list of metrics, aggregated for a given interval.
        /// </remarks>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="name">The name of the metric. (optional)</param>
        /// <param name="reporter">The name of the reporter (host), on which the metrics was logged. This will have value provided by the [hostname configuration property](https://docs.camunda.org/manual/7.13/reference/deployment-descriptors/tags/process-engine/#hostname). (optional)</param>
        /// <param name="startDate">The start date (inclusive). (optional)</param>
        /// <param name="endDate">The end date (exclusive). (optional)</param>
        /// <param name="firstResult">Pagination of results. Specifies the index of the first result to return. (optional)</param>
        /// <param name="maxResults">Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. (optional)</param>
        /// <param name="interval">The interval for which the metrics should be aggregated. Time unit is seconds. Default: The interval is set to 15 minutes (900 seconds). (optional, default to &quot;900&quot;)</param>
        /// <param name="aggregateByReporter">Aggregate metrics by reporter. (optional)</param>
        /// <returns>Task of ApiResponse (List&lt;MetricsIntervalResultDto&gt;)</returns>
        System.Threading.Tasks.Task<ApiResponse<List<MetricsIntervalResultDto>>> IntervalAsyncWithHttpInfo (string name = default(string), string reporter = default(string), DateTime? startDate = default(DateTime?), DateTime? endDate = default(DateTime?), int? firstResult = default(int?), int? maxResults = default(int?), string interval = default(string), string aggregateByReporter = default(string));
        #endregion Asynchronous Operations
    }

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public partial class MetricsApi : IMetricsApi
    {
        private Org.OpenAPITools.Client.ExceptionFactory _exceptionFactory = (name, response) => null;

        /// <summary>
        /// Initializes a new instance of the <see cref="MetricsApi"/> class.
        /// </summary>
        /// <returns></returns>
        public MetricsApi(String basePath)
        {
            this.Configuration = new Org.OpenAPITools.Client.Configuration { BasePath = basePath };

            ExceptionFactory = Org.OpenAPITools.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="MetricsApi"/> class
        /// </summary>
        /// <returns></returns>
        public MetricsApi()
        {
            this.Configuration = Org.OpenAPITools.Client.Configuration.Default;

            ExceptionFactory = Org.OpenAPITools.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="MetricsApi"/> class
        /// using Configuration object
        /// </summary>
        /// <param name="configuration">An instance of Configuration</param>
        /// <returns></returns>
        public MetricsApi(Org.OpenAPITools.Client.Configuration configuration = null)
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
        ///  Retrieves the &#x60;sum&#x60; (count) for a given metric.
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="metricsName">The name of the metric.</param>
        /// <param name="startDate">The start date (inclusive). (optional)</param>
        /// <param name="endDate">The end date (exclusive). (optional)</param>
        /// <returns>MetricsResultDto</returns>
        public MetricsResultDto GetMetrics (string metricsName, DateTime? startDate = default(DateTime?), DateTime? endDate = default(DateTime?))
        {
             ApiResponse<MetricsResultDto> localVarResponse = GetMetricsWithHttpInfo(metricsName, startDate, endDate);
             return localVarResponse.Data;
        }

        /// <summary>
        ///  Retrieves the &#x60;sum&#x60; (count) for a given metric.
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="metricsName">The name of the metric.</param>
        /// <param name="startDate">The start date (inclusive). (optional)</param>
        /// <param name="endDate">The end date (exclusive). (optional)</param>
        /// <returns>ApiResponse of MetricsResultDto</returns>
        public ApiResponse<MetricsResultDto> GetMetricsWithHttpInfo (string metricsName, DateTime? startDate = default(DateTime?), DateTime? endDate = default(DateTime?))
        {
            // verify the required parameter 'metricsName' is set
            if (metricsName == null)
                throw new ApiException(400, "Missing required parameter 'metricsName' when calling MetricsApi->GetMetrics");

            var localVarPath = "/metrics/{metrics-name}/sum";
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

            if (metricsName != null) localVarPathParams.Add("metrics-name", this.Configuration.ApiClient.ParameterToString(metricsName)); // path parameter
            if (startDate != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "startDate", startDate)); // query parameter
            if (endDate != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "endDate", endDate)); // query parameter


            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) this.Configuration.ApiClient.CallApi(localVarPath,
                Method.GET, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("GetMetrics", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<MetricsResultDto>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (MetricsResultDto) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(MetricsResultDto)));
        }

        /// <summary>
        ///  Retrieves the &#x60;sum&#x60; (count) for a given metric.
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="metricsName">The name of the metric.</param>
        /// <param name="startDate">The start date (inclusive). (optional)</param>
        /// <param name="endDate">The end date (exclusive). (optional)</param>
        /// <returns>Task of MetricsResultDto</returns>
        public async System.Threading.Tasks.Task<MetricsResultDto> GetMetricsAsync (string metricsName, DateTime? startDate = default(DateTime?), DateTime? endDate = default(DateTime?))
        {
             ApiResponse<MetricsResultDto> localVarResponse = await GetMetricsAsyncWithHttpInfo(metricsName, startDate, endDate);
             return localVarResponse.Data;

        }

        /// <summary>
        ///  Retrieves the &#x60;sum&#x60; (count) for a given metric.
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="metricsName">The name of the metric.</param>
        /// <param name="startDate">The start date (inclusive). (optional)</param>
        /// <param name="endDate">The end date (exclusive). (optional)</param>
        /// <returns>Task of ApiResponse (MetricsResultDto)</returns>
        public async System.Threading.Tasks.Task<ApiResponse<MetricsResultDto>> GetMetricsAsyncWithHttpInfo (string metricsName, DateTime? startDate = default(DateTime?), DateTime? endDate = default(DateTime?))
        {
            // verify the required parameter 'metricsName' is set
            if (metricsName == null)
                throw new ApiException(400, "Missing required parameter 'metricsName' when calling MetricsApi->GetMetrics");

            var localVarPath = "/metrics/{metrics-name}/sum";
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

            if (metricsName != null) localVarPathParams.Add("metrics-name", this.Configuration.ApiClient.ParameterToString(metricsName)); // path parameter
            if (startDate != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "startDate", startDate)); // query parameter
            if (endDate != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "endDate", endDate)); // query parameter


            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) await this.Configuration.ApiClient.CallApiAsync(localVarPath,
                Method.GET, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("GetMetrics", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<MetricsResultDto>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (MetricsResultDto) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(MetricsResultDto)));
        }

        /// <summary>
        ///  Retrieves a list of metrics, aggregated for a given interval.
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="name">The name of the metric. (optional)</param>
        /// <param name="reporter">The name of the reporter (host), on which the metrics was logged. This will have value provided by the [hostname configuration property](https://docs.camunda.org/manual/7.13/reference/deployment-descriptors/tags/process-engine/#hostname). (optional)</param>
        /// <param name="startDate">The start date (inclusive). (optional)</param>
        /// <param name="endDate">The end date (exclusive). (optional)</param>
        /// <param name="firstResult">Pagination of results. Specifies the index of the first result to return. (optional)</param>
        /// <param name="maxResults">Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. (optional)</param>
        /// <param name="interval">The interval for which the metrics should be aggregated. Time unit is seconds. Default: The interval is set to 15 minutes (900 seconds). (optional, default to &quot;900&quot;)</param>
        /// <param name="aggregateByReporter">Aggregate metrics by reporter. (optional)</param>
        /// <returns>List&lt;MetricsIntervalResultDto&gt;</returns>
        public List<MetricsIntervalResultDto> Interval (string name = default(string), string reporter = default(string), DateTime? startDate = default(DateTime?), DateTime? endDate = default(DateTime?), int? firstResult = default(int?), int? maxResults = default(int?), string interval = default(string), string aggregateByReporter = default(string))
        {
             ApiResponse<List<MetricsIntervalResultDto>> localVarResponse = IntervalWithHttpInfo(name, reporter, startDate, endDate, firstResult, maxResults, interval, aggregateByReporter);
             return localVarResponse.Data;
        }

        /// <summary>
        ///  Retrieves a list of metrics, aggregated for a given interval.
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="name">The name of the metric. (optional)</param>
        /// <param name="reporter">The name of the reporter (host), on which the metrics was logged. This will have value provided by the [hostname configuration property](https://docs.camunda.org/manual/7.13/reference/deployment-descriptors/tags/process-engine/#hostname). (optional)</param>
        /// <param name="startDate">The start date (inclusive). (optional)</param>
        /// <param name="endDate">The end date (exclusive). (optional)</param>
        /// <param name="firstResult">Pagination of results. Specifies the index of the first result to return. (optional)</param>
        /// <param name="maxResults">Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. (optional)</param>
        /// <param name="interval">The interval for which the metrics should be aggregated. Time unit is seconds. Default: The interval is set to 15 minutes (900 seconds). (optional, default to &quot;900&quot;)</param>
        /// <param name="aggregateByReporter">Aggregate metrics by reporter. (optional)</param>
        /// <returns>ApiResponse of List&lt;MetricsIntervalResultDto&gt;</returns>
        public ApiResponse<List<MetricsIntervalResultDto>> IntervalWithHttpInfo (string name = default(string), string reporter = default(string), DateTime? startDate = default(DateTime?), DateTime? endDate = default(DateTime?), int? firstResult = default(int?), int? maxResults = default(int?), string interval = default(string), string aggregateByReporter = default(string))
        {

            var localVarPath = "/metrics";
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

            if (name != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "name", name)); // query parameter
            if (reporter != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "reporter", reporter)); // query parameter
            if (startDate != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "startDate", startDate)); // query parameter
            if (endDate != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "endDate", endDate)); // query parameter
            if (firstResult != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "firstResult", firstResult)); // query parameter
            if (maxResults != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "maxResults", maxResults)); // query parameter
            if (interval != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "interval", interval)); // query parameter
            if (aggregateByReporter != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "aggregateByReporter", aggregateByReporter)); // query parameter


            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) this.Configuration.ApiClient.CallApi(localVarPath,
                Method.GET, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("Interval", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<List<MetricsIntervalResultDto>>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (List<MetricsIntervalResultDto>) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(List<MetricsIntervalResultDto>)));
        }

        /// <summary>
        ///  Retrieves a list of metrics, aggregated for a given interval.
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="name">The name of the metric. (optional)</param>
        /// <param name="reporter">The name of the reporter (host), on which the metrics was logged. This will have value provided by the [hostname configuration property](https://docs.camunda.org/manual/7.13/reference/deployment-descriptors/tags/process-engine/#hostname). (optional)</param>
        /// <param name="startDate">The start date (inclusive). (optional)</param>
        /// <param name="endDate">The end date (exclusive). (optional)</param>
        /// <param name="firstResult">Pagination of results. Specifies the index of the first result to return. (optional)</param>
        /// <param name="maxResults">Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. (optional)</param>
        /// <param name="interval">The interval for which the metrics should be aggregated. Time unit is seconds. Default: The interval is set to 15 minutes (900 seconds). (optional, default to &quot;900&quot;)</param>
        /// <param name="aggregateByReporter">Aggregate metrics by reporter. (optional)</param>
        /// <returns>Task of List&lt;MetricsIntervalResultDto&gt;</returns>
        public async System.Threading.Tasks.Task<List<MetricsIntervalResultDto>> IntervalAsync (string name = default(string), string reporter = default(string), DateTime? startDate = default(DateTime?), DateTime? endDate = default(DateTime?), int? firstResult = default(int?), int? maxResults = default(int?), string interval = default(string), string aggregateByReporter = default(string))
        {
             ApiResponse<List<MetricsIntervalResultDto>> localVarResponse = await IntervalAsyncWithHttpInfo(name, reporter, startDate, endDate, firstResult, maxResults, interval, aggregateByReporter);
             return localVarResponse.Data;

        }

        /// <summary>
        ///  Retrieves a list of metrics, aggregated for a given interval.
        /// </summary>
        /// <exception cref="Org.OpenAPITools.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="name">The name of the metric. (optional)</param>
        /// <param name="reporter">The name of the reporter (host), on which the metrics was logged. This will have value provided by the [hostname configuration property](https://docs.camunda.org/manual/7.13/reference/deployment-descriptors/tags/process-engine/#hostname). (optional)</param>
        /// <param name="startDate">The start date (inclusive). (optional)</param>
        /// <param name="endDate">The end date (exclusive). (optional)</param>
        /// <param name="firstResult">Pagination of results. Specifies the index of the first result to return. (optional)</param>
        /// <param name="maxResults">Pagination of results. Specifies the maximum number of results to return. Will return less results if there are no more results left. (optional)</param>
        /// <param name="interval">The interval for which the metrics should be aggregated. Time unit is seconds. Default: The interval is set to 15 minutes (900 seconds). (optional, default to &quot;900&quot;)</param>
        /// <param name="aggregateByReporter">Aggregate metrics by reporter. (optional)</param>
        /// <returns>Task of ApiResponse (List&lt;MetricsIntervalResultDto&gt;)</returns>
        public async System.Threading.Tasks.Task<ApiResponse<List<MetricsIntervalResultDto>>> IntervalAsyncWithHttpInfo (string name = default(string), string reporter = default(string), DateTime? startDate = default(DateTime?), DateTime? endDate = default(DateTime?), int? firstResult = default(int?), int? maxResults = default(int?), string interval = default(string), string aggregateByReporter = default(string))
        {

            var localVarPath = "/metrics";
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

            if (name != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "name", name)); // query parameter
            if (reporter != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "reporter", reporter)); // query parameter
            if (startDate != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "startDate", startDate)); // query parameter
            if (endDate != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "endDate", endDate)); // query parameter
            if (firstResult != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "firstResult", firstResult)); // query parameter
            if (maxResults != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "maxResults", maxResults)); // query parameter
            if (interval != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "interval", interval)); // query parameter
            if (aggregateByReporter != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "aggregateByReporter", aggregateByReporter)); // query parameter


            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) await this.Configuration.ApiClient.CallApiAsync(localVarPath,
                Method.GET, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("Interval", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<List<MetricsIntervalResultDto>>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (List<MetricsIntervalResultDto>) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(List<MetricsIntervalResultDto>)));
        }

    }
}