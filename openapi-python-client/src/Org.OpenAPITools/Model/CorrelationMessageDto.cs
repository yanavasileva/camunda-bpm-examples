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
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using OpenAPIDateConverter = Org.OpenAPITools.Client.OpenAPIDateConverter;

namespace Org.OpenAPITools.Model
{
    /// <summary>
    /// CorrelationMessageDto
    /// </summary>
    [DataContract]
    public partial class CorrelationMessageDto :  IEquatable<CorrelationMessageDto>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="CorrelationMessageDto" /> class.
        /// </summary>
        /// <param name="messageName">The name of the message to deliver..</param>
        /// <param name="businessKey">Used for correlation of process instances that wait for incoming messages. Will only correlate to executions that belong to a process instance with the provided business key..</param>
        /// <param name="tenantId">Used to correlate the message for a tenant with the given id. Will only correlate to executions and process definitions which belong to the tenant. Must not be supplied in conjunction with a &#x60;withoutTenantId&#x60;..</param>
        /// <param name="withoutTenantId">A Boolean value that indicates whether the message should only be correlated to executions and process definitions which belong to no tenant or not. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. Must not be supplied in conjunction with a &#x60;tenantId&#x60;. (default to false).</param>
        /// <param name="processInstanceId">Used to correlate the message to the process instance with the given id..</param>
        /// <param name="correlationKeys">Used for correlation of process instances that wait for incoming messages. Has to be a JSON object containing key-value pairs that are matched against process instance variables during correlation. Each key is a variable name and each value a JSON variable value object with the following properties..</param>
        /// <param name="localCorrelationKeys">Local variables used for correlation of executions (process instances) that wait for incoming messages. Has to be a JSON object containing key-value pairs that are matched against local variables during correlation. Each key is a variable name and each value a JSON variable value object with the following properties..</param>
        /// <param name="processVariables">A map of variables that is injected into the triggered execution or process instance after the message has been delivered. Each key is a variable name and each value a JSON variable value object with the following properties..</param>
        /// <param name="processVariablesLocal">A map of local variables that is injected into the triggered execution or process instance after the message has been delivered. Each key is a variable name and each value a JSON variable value object with the following properties..</param>
        /// <param name="all">A Boolean value that indicates whether the message should be correlated to exactly one entity or multiple entities. If the value is set to &#x60;false&#x60;, the message will be correlated to exactly one entity (execution or process definition). If the value is set to &#x60;true&#x60;, the message will be correlated to multiple executions and a process definition that can be instantiated by this message in one go. (default to false).</param>
        /// <param name="resultEnabled">A Boolean value that indicates whether the result of the correlation should be returned or not. If this property is set to &#x60;true&#x60;, there will be returned a list of message correlation result objects. Depending on the all property, there will be either one ore more returned results in the list.  The default value is &#x60;false&#x60;, which means no result will be returned. (default to false).</param>
        /// <param name="variablesInResultEnabled">A Boolean value that indicates whether the result of the correlation should contain process variables or not. The parameter resultEnabled should be set to &#x60;true&#x60; in order to use this it.  The default value is &#x60;false&#x60;, which means the variables will not be returned. (default to false).</param>
        public CorrelationMessageDto(string messageName = default(string), string businessKey = default(string), string tenantId = default(string), bool? withoutTenantId = false, string processInstanceId = default(string), Dictionary<string, VariableValueDto> correlationKeys = default(Dictionary<string, VariableValueDto>), Dictionary<string, VariableValueDto> localCorrelationKeys = default(Dictionary<string, VariableValueDto>), Dictionary<string, VariableValueDto> processVariables = default(Dictionary<string, VariableValueDto>), Dictionary<string, VariableValueDto> processVariablesLocal = default(Dictionary<string, VariableValueDto>), bool? all = false, bool? resultEnabled = false, bool? variablesInResultEnabled = false)
        {
            this.WithoutTenantId = withoutTenantId;
            this.All = all;
            this.ResultEnabled = resultEnabled;
            this.VariablesInResultEnabled = variablesInResultEnabled;
            this.MessageName = messageName;
            this.BusinessKey = businessKey;
            this.TenantId = tenantId;
            // use default value if no "withoutTenantId" provided
            if (withoutTenantId == null)
            {
                this.WithoutTenantId = false;
            }
            else
            {
                this.WithoutTenantId = withoutTenantId;
            }
            this.ProcessInstanceId = processInstanceId;
            this.CorrelationKeys = correlationKeys;
            this.LocalCorrelationKeys = localCorrelationKeys;
            this.ProcessVariables = processVariables;
            this.ProcessVariablesLocal = processVariablesLocal;
            // use default value if no "all" provided
            if (all == null)
            {
                this.All = false;
            }
            else
            {
                this.All = all;
            }
            // use default value if no "resultEnabled" provided
            if (resultEnabled == null)
            {
                this.ResultEnabled = false;
            }
            else
            {
                this.ResultEnabled = resultEnabled;
            }
            // use default value if no "variablesInResultEnabled" provided
            if (variablesInResultEnabled == null)
            {
                this.VariablesInResultEnabled = false;
            }
            else
            {
                this.VariablesInResultEnabled = variablesInResultEnabled;
            }
        }
        
        /// <summary>
        /// The name of the message to deliver.
        /// </summary>
        /// <value>The name of the message to deliver.</value>
        [DataMember(Name="messageName", EmitDefaultValue=false)]
        public string MessageName { get; set; }

        /// <summary>
        /// Used for correlation of process instances that wait for incoming messages. Will only correlate to executions that belong to a process instance with the provided business key.
        /// </summary>
        /// <value>Used for correlation of process instances that wait for incoming messages. Will only correlate to executions that belong to a process instance with the provided business key.</value>
        [DataMember(Name="businessKey", EmitDefaultValue=false)]
        public string BusinessKey { get; set; }

        /// <summary>
        /// Used to correlate the message for a tenant with the given id. Will only correlate to executions and process definitions which belong to the tenant. Must not be supplied in conjunction with a &#x60;withoutTenantId&#x60;.
        /// </summary>
        /// <value>Used to correlate the message for a tenant with the given id. Will only correlate to executions and process definitions which belong to the tenant. Must not be supplied in conjunction with a &#x60;withoutTenantId&#x60;.</value>
        [DataMember(Name="tenantId", EmitDefaultValue=false)]
        public string TenantId { get; set; }

        /// <summary>
        /// A Boolean value that indicates whether the message should only be correlated to executions and process definitions which belong to no tenant or not. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. Must not be supplied in conjunction with a &#x60;tenantId&#x60;.
        /// </summary>
        /// <value>A Boolean value that indicates whether the message should only be correlated to executions and process definitions which belong to no tenant or not. Value may only be &#x60;true&#x60;, as &#x60;false&#x60; is the default behavior. Must not be supplied in conjunction with a &#x60;tenantId&#x60;.</value>
        [DataMember(Name="withoutTenantId", EmitDefaultValue=true)]
        public bool? WithoutTenantId { get; set; }

        /// <summary>
        /// Used to correlate the message to the process instance with the given id.
        /// </summary>
        /// <value>Used to correlate the message to the process instance with the given id.</value>
        [DataMember(Name="processInstanceId", EmitDefaultValue=false)]
        public string ProcessInstanceId { get; set; }

        /// <summary>
        /// Used for correlation of process instances that wait for incoming messages. Has to be a JSON object containing key-value pairs that are matched against process instance variables during correlation. Each key is a variable name and each value a JSON variable value object with the following properties.
        /// </summary>
        /// <value>Used for correlation of process instances that wait for incoming messages. Has to be a JSON object containing key-value pairs that are matched against process instance variables during correlation. Each key is a variable name and each value a JSON variable value object with the following properties.</value>
        [DataMember(Name="correlationKeys", EmitDefaultValue=false)]
        public Dictionary<string, VariableValueDto> CorrelationKeys { get; set; }

        /// <summary>
        /// Local variables used for correlation of executions (process instances) that wait for incoming messages. Has to be a JSON object containing key-value pairs that are matched against local variables during correlation. Each key is a variable name and each value a JSON variable value object with the following properties.
        /// </summary>
        /// <value>Local variables used for correlation of executions (process instances) that wait for incoming messages. Has to be a JSON object containing key-value pairs that are matched against local variables during correlation. Each key is a variable name and each value a JSON variable value object with the following properties.</value>
        [DataMember(Name="localCorrelationKeys", EmitDefaultValue=false)]
        public Dictionary<string, VariableValueDto> LocalCorrelationKeys { get; set; }

        /// <summary>
        /// A map of variables that is injected into the triggered execution or process instance after the message has been delivered. Each key is a variable name and each value a JSON variable value object with the following properties.
        /// </summary>
        /// <value>A map of variables that is injected into the triggered execution or process instance after the message has been delivered. Each key is a variable name and each value a JSON variable value object with the following properties.</value>
        [DataMember(Name="processVariables", EmitDefaultValue=false)]
        public Dictionary<string, VariableValueDto> ProcessVariables { get; set; }

        /// <summary>
        /// A map of local variables that is injected into the triggered execution or process instance after the message has been delivered. Each key is a variable name and each value a JSON variable value object with the following properties.
        /// </summary>
        /// <value>A map of local variables that is injected into the triggered execution or process instance after the message has been delivered. Each key is a variable name and each value a JSON variable value object with the following properties.</value>
        [DataMember(Name="processVariablesLocal", EmitDefaultValue=false)]
        public Dictionary<string, VariableValueDto> ProcessVariablesLocal { get; set; }

        /// <summary>
        /// A Boolean value that indicates whether the message should be correlated to exactly one entity or multiple entities. If the value is set to &#x60;false&#x60;, the message will be correlated to exactly one entity (execution or process definition). If the value is set to &#x60;true&#x60;, the message will be correlated to multiple executions and a process definition that can be instantiated by this message in one go.
        /// </summary>
        /// <value>A Boolean value that indicates whether the message should be correlated to exactly one entity or multiple entities. If the value is set to &#x60;false&#x60;, the message will be correlated to exactly one entity (execution or process definition). If the value is set to &#x60;true&#x60;, the message will be correlated to multiple executions and a process definition that can be instantiated by this message in one go.</value>
        [DataMember(Name="all", EmitDefaultValue=true)]
        public bool? All { get; set; }

        /// <summary>
        /// A Boolean value that indicates whether the result of the correlation should be returned or not. If this property is set to &#x60;true&#x60;, there will be returned a list of message correlation result objects. Depending on the all property, there will be either one ore more returned results in the list.  The default value is &#x60;false&#x60;, which means no result will be returned.
        /// </summary>
        /// <value>A Boolean value that indicates whether the result of the correlation should be returned or not. If this property is set to &#x60;true&#x60;, there will be returned a list of message correlation result objects. Depending on the all property, there will be either one ore more returned results in the list.  The default value is &#x60;false&#x60;, which means no result will be returned.</value>
        [DataMember(Name="resultEnabled", EmitDefaultValue=true)]
        public bool? ResultEnabled { get; set; }

        /// <summary>
        /// A Boolean value that indicates whether the result of the correlation should contain process variables or not. The parameter resultEnabled should be set to &#x60;true&#x60; in order to use this it.  The default value is &#x60;false&#x60;, which means the variables will not be returned.
        /// </summary>
        /// <value>A Boolean value that indicates whether the result of the correlation should contain process variables or not. The parameter resultEnabled should be set to &#x60;true&#x60; in order to use this it.  The default value is &#x60;false&#x60;, which means the variables will not be returned.</value>
        [DataMember(Name="variablesInResultEnabled", EmitDefaultValue=true)]
        public bool? VariablesInResultEnabled { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class CorrelationMessageDto {\n");
            sb.Append("  MessageName: ").Append(MessageName).Append("\n");
            sb.Append("  BusinessKey: ").Append(BusinessKey).Append("\n");
            sb.Append("  TenantId: ").Append(TenantId).Append("\n");
            sb.Append("  WithoutTenantId: ").Append(WithoutTenantId).Append("\n");
            sb.Append("  ProcessInstanceId: ").Append(ProcessInstanceId).Append("\n");
            sb.Append("  CorrelationKeys: ").Append(CorrelationKeys).Append("\n");
            sb.Append("  LocalCorrelationKeys: ").Append(LocalCorrelationKeys).Append("\n");
            sb.Append("  ProcessVariables: ").Append(ProcessVariables).Append("\n");
            sb.Append("  ProcessVariablesLocal: ").Append(ProcessVariablesLocal).Append("\n");
            sb.Append("  All: ").Append(All).Append("\n");
            sb.Append("  ResultEnabled: ").Append(ResultEnabled).Append("\n");
            sb.Append("  VariablesInResultEnabled: ").Append(VariablesInResultEnabled).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as CorrelationMessageDto);
        }

        /// <summary>
        /// Returns true if CorrelationMessageDto instances are equal
        /// </summary>
        /// <param name="input">Instance of CorrelationMessageDto to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(CorrelationMessageDto input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.MessageName == input.MessageName ||
                    (this.MessageName != null &&
                    this.MessageName.Equals(input.MessageName))
                ) && 
                (
                    this.BusinessKey == input.BusinessKey ||
                    (this.BusinessKey != null &&
                    this.BusinessKey.Equals(input.BusinessKey))
                ) && 
                (
                    this.TenantId == input.TenantId ||
                    (this.TenantId != null &&
                    this.TenantId.Equals(input.TenantId))
                ) && 
                (
                    this.WithoutTenantId == input.WithoutTenantId ||
                    (this.WithoutTenantId != null &&
                    this.WithoutTenantId.Equals(input.WithoutTenantId))
                ) && 
                (
                    this.ProcessInstanceId == input.ProcessInstanceId ||
                    (this.ProcessInstanceId != null &&
                    this.ProcessInstanceId.Equals(input.ProcessInstanceId))
                ) && 
                (
                    this.CorrelationKeys == input.CorrelationKeys ||
                    this.CorrelationKeys != null &&
                    input.CorrelationKeys != null &&
                    this.CorrelationKeys.SequenceEqual(input.CorrelationKeys)
                ) && 
                (
                    this.LocalCorrelationKeys == input.LocalCorrelationKeys ||
                    this.LocalCorrelationKeys != null &&
                    input.LocalCorrelationKeys != null &&
                    this.LocalCorrelationKeys.SequenceEqual(input.LocalCorrelationKeys)
                ) && 
                (
                    this.ProcessVariables == input.ProcessVariables ||
                    this.ProcessVariables != null &&
                    input.ProcessVariables != null &&
                    this.ProcessVariables.SequenceEqual(input.ProcessVariables)
                ) && 
                (
                    this.ProcessVariablesLocal == input.ProcessVariablesLocal ||
                    this.ProcessVariablesLocal != null &&
                    input.ProcessVariablesLocal != null &&
                    this.ProcessVariablesLocal.SequenceEqual(input.ProcessVariablesLocal)
                ) && 
                (
                    this.All == input.All ||
                    (this.All != null &&
                    this.All.Equals(input.All))
                ) && 
                (
                    this.ResultEnabled == input.ResultEnabled ||
                    (this.ResultEnabled != null &&
                    this.ResultEnabled.Equals(input.ResultEnabled))
                ) && 
                (
                    this.VariablesInResultEnabled == input.VariablesInResultEnabled ||
                    (this.VariablesInResultEnabled != null &&
                    this.VariablesInResultEnabled.Equals(input.VariablesInResultEnabled))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.MessageName != null)
                    hashCode = hashCode * 59 + this.MessageName.GetHashCode();
                if (this.BusinessKey != null)
                    hashCode = hashCode * 59 + this.BusinessKey.GetHashCode();
                if (this.TenantId != null)
                    hashCode = hashCode * 59 + this.TenantId.GetHashCode();
                if (this.WithoutTenantId != null)
                    hashCode = hashCode * 59 + this.WithoutTenantId.GetHashCode();
                if (this.ProcessInstanceId != null)
                    hashCode = hashCode * 59 + this.ProcessInstanceId.GetHashCode();
                if (this.CorrelationKeys != null)
                    hashCode = hashCode * 59 + this.CorrelationKeys.GetHashCode();
                if (this.LocalCorrelationKeys != null)
                    hashCode = hashCode * 59 + this.LocalCorrelationKeys.GetHashCode();
                if (this.ProcessVariables != null)
                    hashCode = hashCode * 59 + this.ProcessVariables.GetHashCode();
                if (this.ProcessVariablesLocal != null)
                    hashCode = hashCode * 59 + this.ProcessVariablesLocal.GetHashCode();
                if (this.All != null)
                    hashCode = hashCode * 59 + this.All.GetHashCode();
                if (this.ResultEnabled != null)
                    hashCode = hashCode * 59 + this.ResultEnabled.GetHashCode();
                if (this.VariablesInResultEnabled != null)
                    hashCode = hashCode * 59 + this.VariablesInResultEnabled.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}
