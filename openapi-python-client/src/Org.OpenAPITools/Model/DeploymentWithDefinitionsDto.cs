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
    /// DeploymentWithDefinitionsDto
    /// </summary>
    [DataContract]
    public partial class DeploymentWithDefinitionsDto :  IEquatable<DeploymentWithDefinitionsDto>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DeploymentWithDefinitionsDto" /> class.
        /// </summary>
        /// <param name="deployedProcessDefinitions">A JSON Object containing a property for each of the process definitions, which are successfully deployed with that deployment. The key is the process definition id, the value is a JSON Object corresponding to the process definition..</param>
        /// <param name="deployedDecisionDefinitions">A JSON Object containing a property for each of the decision definitions, which are successfully deployed with that deployment. The key is the decision definition id, the value is a JSON Object corresponding to the decision definition..</param>
        /// <param name="deployedDecisionRequirementsDefinitions">A JSON Object containing a property for each of the decision requirements definitions, which are successfully deployed with that deployment. The key is the decision requirements definition id, the value is a JSON Object corresponding to the decision requirements definition..</param>
        /// <param name="deployedCaseDefinitions">A JSON Object containing a property for each of the case definitions, which are successfully deployed with that deployment. The key is the case definition id, the value is a JSON Object corresponding to the case definition..</param>
        /// <param name="id">The id of the deployment..</param>
        /// <param name="tenantId">The tenant id of the deployment..</param>
        /// <param name="deploymentTime">The time when the deployment was created..</param>
        /// <param name="source">The source of the deployment..</param>
        /// <param name="name">The name of the deployment..</param>
        /// <param name="links">The links associated to this resource, with &#x60;method&#x60;, &#x60;href&#x60; and &#x60;rel&#x60;..</param>
        public DeploymentWithDefinitionsDto(Dictionary<string, ProcessDefinitionDto> deployedProcessDefinitions = default(Dictionary<string, ProcessDefinitionDto>), Dictionary<string, DecisionDefinitionDto> deployedDecisionDefinitions = default(Dictionary<string, DecisionDefinitionDto>), Dictionary<string, DecisionRequirementsDefinitionDto> deployedDecisionRequirementsDefinitions = default(Dictionary<string, DecisionRequirementsDefinitionDto>), Dictionary<string, CaseDefinitionDto> deployedCaseDefinitions = default(Dictionary<string, CaseDefinitionDto>), string id = default(string), string tenantId = default(string), DateTime deploymentTime = default(DateTime), string source = default(string), string name = default(string), List<AtomLink> links = default(List<AtomLink>))
        {
            this.DeployedProcessDefinitions = deployedProcessDefinitions;
            this.DeployedDecisionDefinitions = deployedDecisionDefinitions;
            this.DeployedDecisionRequirementsDefinitions = deployedDecisionRequirementsDefinitions;
            this.DeployedCaseDefinitions = deployedCaseDefinitions;
            this.Id = id;
            this.TenantId = tenantId;
            this.DeploymentTime = deploymentTime;
            this.Source = source;
            this.Name = name;
            this.Links = links;
        }
        
        /// <summary>
        /// A JSON Object containing a property for each of the process definitions, which are successfully deployed with that deployment. The key is the process definition id, the value is a JSON Object corresponding to the process definition.
        /// </summary>
        /// <value>A JSON Object containing a property for each of the process definitions, which are successfully deployed with that deployment. The key is the process definition id, the value is a JSON Object corresponding to the process definition.</value>
        [DataMember(Name="deployedProcessDefinitions", EmitDefaultValue=false)]
        public Dictionary<string, ProcessDefinitionDto> DeployedProcessDefinitions { get; set; }

        /// <summary>
        /// A JSON Object containing a property for each of the decision definitions, which are successfully deployed with that deployment. The key is the decision definition id, the value is a JSON Object corresponding to the decision definition.
        /// </summary>
        /// <value>A JSON Object containing a property for each of the decision definitions, which are successfully deployed with that deployment. The key is the decision definition id, the value is a JSON Object corresponding to the decision definition.</value>
        [DataMember(Name="deployedDecisionDefinitions", EmitDefaultValue=false)]
        public Dictionary<string, DecisionDefinitionDto> DeployedDecisionDefinitions { get; set; }

        /// <summary>
        /// A JSON Object containing a property for each of the decision requirements definitions, which are successfully deployed with that deployment. The key is the decision requirements definition id, the value is a JSON Object corresponding to the decision requirements definition.
        /// </summary>
        /// <value>A JSON Object containing a property for each of the decision requirements definitions, which are successfully deployed with that deployment. The key is the decision requirements definition id, the value is a JSON Object corresponding to the decision requirements definition.</value>
        [DataMember(Name="deployedDecisionRequirementsDefinitions", EmitDefaultValue=false)]
        public Dictionary<string, DecisionRequirementsDefinitionDto> DeployedDecisionRequirementsDefinitions { get; set; }

        /// <summary>
        /// A JSON Object containing a property for each of the case definitions, which are successfully deployed with that deployment. The key is the case definition id, the value is a JSON Object corresponding to the case definition.
        /// </summary>
        /// <value>A JSON Object containing a property for each of the case definitions, which are successfully deployed with that deployment. The key is the case definition id, the value is a JSON Object corresponding to the case definition.</value>
        [DataMember(Name="deployedCaseDefinitions", EmitDefaultValue=false)]
        public Dictionary<string, CaseDefinitionDto> DeployedCaseDefinitions { get; set; }

        /// <summary>
        /// The id of the deployment.
        /// </summary>
        /// <value>The id of the deployment.</value>
        [DataMember(Name="id", EmitDefaultValue=false)]
        public string Id { get; set; }

        /// <summary>
        /// The tenant id of the deployment.
        /// </summary>
        /// <value>The tenant id of the deployment.</value>
        [DataMember(Name="tenantId", EmitDefaultValue=false)]
        public string TenantId { get; set; }

        /// <summary>
        /// The time when the deployment was created.
        /// </summary>
        /// <value>The time when the deployment was created.</value>
        [DataMember(Name="deploymentTime", EmitDefaultValue=false)]
        public DateTime DeploymentTime { get; set; }

        /// <summary>
        /// The source of the deployment.
        /// </summary>
        /// <value>The source of the deployment.</value>
        [DataMember(Name="source", EmitDefaultValue=false)]
        public string Source { get; set; }

        /// <summary>
        /// The name of the deployment.
        /// </summary>
        /// <value>The name of the deployment.</value>
        [DataMember(Name="name", EmitDefaultValue=false)]
        public string Name { get; set; }

        /// <summary>
        /// The links associated to this resource, with &#x60;method&#x60;, &#x60;href&#x60; and &#x60;rel&#x60;.
        /// </summary>
        /// <value>The links associated to this resource, with &#x60;method&#x60;, &#x60;href&#x60; and &#x60;rel&#x60;.</value>
        [DataMember(Name="links", EmitDefaultValue=false)]
        public List<AtomLink> Links { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class DeploymentWithDefinitionsDto {\n");
            sb.Append("  DeployedProcessDefinitions: ").Append(DeployedProcessDefinitions).Append("\n");
            sb.Append("  DeployedDecisionDefinitions: ").Append(DeployedDecisionDefinitions).Append("\n");
            sb.Append("  DeployedDecisionRequirementsDefinitions: ").Append(DeployedDecisionRequirementsDefinitions).Append("\n");
            sb.Append("  DeployedCaseDefinitions: ").Append(DeployedCaseDefinitions).Append("\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  TenantId: ").Append(TenantId).Append("\n");
            sb.Append("  DeploymentTime: ").Append(DeploymentTime).Append("\n");
            sb.Append("  Source: ").Append(Source).Append("\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  Links: ").Append(Links).Append("\n");
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
            return this.Equals(input as DeploymentWithDefinitionsDto);
        }

        /// <summary>
        /// Returns true if DeploymentWithDefinitionsDto instances are equal
        /// </summary>
        /// <param name="input">Instance of DeploymentWithDefinitionsDto to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(DeploymentWithDefinitionsDto input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.DeployedProcessDefinitions == input.DeployedProcessDefinitions ||
                    this.DeployedProcessDefinitions != null &&
                    input.DeployedProcessDefinitions != null &&
                    this.DeployedProcessDefinitions.SequenceEqual(input.DeployedProcessDefinitions)
                ) && 
                (
                    this.DeployedDecisionDefinitions == input.DeployedDecisionDefinitions ||
                    this.DeployedDecisionDefinitions != null &&
                    input.DeployedDecisionDefinitions != null &&
                    this.DeployedDecisionDefinitions.SequenceEqual(input.DeployedDecisionDefinitions)
                ) && 
                (
                    this.DeployedDecisionRequirementsDefinitions == input.DeployedDecisionRequirementsDefinitions ||
                    this.DeployedDecisionRequirementsDefinitions != null &&
                    input.DeployedDecisionRequirementsDefinitions != null &&
                    this.DeployedDecisionRequirementsDefinitions.SequenceEqual(input.DeployedDecisionRequirementsDefinitions)
                ) && 
                (
                    this.DeployedCaseDefinitions == input.DeployedCaseDefinitions ||
                    this.DeployedCaseDefinitions != null &&
                    input.DeployedCaseDefinitions != null &&
                    this.DeployedCaseDefinitions.SequenceEqual(input.DeployedCaseDefinitions)
                ) && 
                (
                    this.Id == input.Id ||
                    (this.Id != null &&
                    this.Id.Equals(input.Id))
                ) && 
                (
                    this.TenantId == input.TenantId ||
                    (this.TenantId != null &&
                    this.TenantId.Equals(input.TenantId))
                ) && 
                (
                    this.DeploymentTime == input.DeploymentTime ||
                    (this.DeploymentTime != null &&
                    this.DeploymentTime.Equals(input.DeploymentTime))
                ) && 
                (
                    this.Source == input.Source ||
                    (this.Source != null &&
                    this.Source.Equals(input.Source))
                ) && 
                (
                    this.Name == input.Name ||
                    (this.Name != null &&
                    this.Name.Equals(input.Name))
                ) && 
                (
                    this.Links == input.Links ||
                    this.Links != null &&
                    input.Links != null &&
                    this.Links.SequenceEqual(input.Links)
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
                if (this.DeployedProcessDefinitions != null)
                    hashCode = hashCode * 59 + this.DeployedProcessDefinitions.GetHashCode();
                if (this.DeployedDecisionDefinitions != null)
                    hashCode = hashCode * 59 + this.DeployedDecisionDefinitions.GetHashCode();
                if (this.DeployedDecisionRequirementsDefinitions != null)
                    hashCode = hashCode * 59 + this.DeployedDecisionRequirementsDefinitions.GetHashCode();
                if (this.DeployedCaseDefinitions != null)
                    hashCode = hashCode * 59 + this.DeployedCaseDefinitions.GetHashCode();
                if (this.Id != null)
                    hashCode = hashCode * 59 + this.Id.GetHashCode();
                if (this.TenantId != null)
                    hashCode = hashCode * 59 + this.TenantId.GetHashCode();
                if (this.DeploymentTime != null)
                    hashCode = hashCode * 59 + this.DeploymentTime.GetHashCode();
                if (this.Source != null)
                    hashCode = hashCode * 59 + this.Source.GetHashCode();
                if (this.Name != null)
                    hashCode = hashCode * 59 + this.Name.GetHashCode();
                if (this.Links != null)
                    hashCode = hashCode * 59 + this.Links.GetHashCode();
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
