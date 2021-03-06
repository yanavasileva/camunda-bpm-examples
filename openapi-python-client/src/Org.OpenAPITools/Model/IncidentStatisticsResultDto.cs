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
    /// IncidentStatisticsResultDto
    /// </summary>
    [DataContract]
    public partial class IncidentStatisticsResultDto :  IEquatable<IncidentStatisticsResultDto>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="IncidentStatisticsResultDto" /> class.
        /// </summary>
        /// <param name="incidentType">The type of the incident the number of incidents is aggregated for. See the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/incidents/#incident-types) for a list of incident types..</param>
        /// <param name="incidentCount">The total number of incidents for the corresponding incident type..</param>
        public IncidentStatisticsResultDto(string incidentType = default(string), int incidentCount = default(int))
        {
            this.IncidentType = incidentType;
            this.IncidentCount = incidentCount;
        }
        
        /// <summary>
        /// The type of the incident the number of incidents is aggregated for. See the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/incidents/#incident-types) for a list of incident types.
        /// </summary>
        /// <value>The type of the incident the number of incidents is aggregated for. See the [User Guide](https://docs.camunda.org/manual/7.13/user-guide/process-engine/incidents/#incident-types) for a list of incident types.</value>
        [DataMember(Name="incidentType", EmitDefaultValue=false)]
        public string IncidentType { get; set; }

        /// <summary>
        /// The total number of incidents for the corresponding incident type.
        /// </summary>
        /// <value>The total number of incidents for the corresponding incident type.</value>
        [DataMember(Name="incidentCount", EmitDefaultValue=false)]
        public int IncidentCount { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class IncidentStatisticsResultDto {\n");
            sb.Append("  IncidentType: ").Append(IncidentType).Append("\n");
            sb.Append("  IncidentCount: ").Append(IncidentCount).Append("\n");
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
            return this.Equals(input as IncidentStatisticsResultDto);
        }

        /// <summary>
        /// Returns true if IncidentStatisticsResultDto instances are equal
        /// </summary>
        /// <param name="input">Instance of IncidentStatisticsResultDto to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(IncidentStatisticsResultDto input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.IncidentType == input.IncidentType ||
                    (this.IncidentType != null &&
                    this.IncidentType.Equals(input.IncidentType))
                ) && 
                (
                    this.IncidentCount == input.IncidentCount ||
                    (this.IncidentCount != null &&
                    this.IncidentCount.Equals(input.IncidentCount))
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
                if (this.IncidentType != null)
                    hashCode = hashCode * 59 + this.IncidentType.GetHashCode();
                if (this.IncidentCount != null)
                    hashCode = hashCode * 59 + this.IncidentCount.GetHashCode();
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
