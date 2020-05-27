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
    /// IdentityLinkDto
    /// </summary>
    [DataContract]
    public partial class IdentityLinkDto :  IEquatable<IdentityLinkDto>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="IdentityLinkDto" /> class.
        /// </summary>
        [JsonConstructorAttribute]
        protected IdentityLinkDto() { }
        /// <summary>
        /// Initializes a new instance of the <see cref="IdentityLinkDto" /> class.
        /// </summary>
        /// <param name="userId">The id of the user participating in this link. Either &#x60;userId&#x60; or &#x60;groupId&#x60; is set..</param>
        /// <param name="groupId">The id of the group participating in this link. Either &#x60;groupId&#x60; or &#x60;userId&#x60; is set..</param>
        /// <param name="type">The type of the identity link. The value of the this property can be user-defined. The Process Engine provides three pre-defined Identity Link &#x60;type&#x60;s:  * &#x60;candidate&#x60; * &#x60;assignee&#x60; - reserved for the task assignee * &#x60;owner&#x60; - reserved for the task owner  **Note**: When adding or removing an Identity Link, the &#x60;type&#x60; property must be defined. (required).</param>
        public IdentityLinkDto(string userId = default(string), string groupId = default(string), string type = default(string))
        {
            // to ensure "type" is required (not null)
            if (type == null)
            {
                throw new InvalidDataException("type is a required property for IdentityLinkDto and cannot be null");
            }
            else
            {
                this.Type = type;
            }
            
            this.UserId = userId;
            this.GroupId = groupId;
        }
        
        /// <summary>
        /// The id of the user participating in this link. Either &#x60;userId&#x60; or &#x60;groupId&#x60; is set.
        /// </summary>
        /// <value>The id of the user participating in this link. Either &#x60;userId&#x60; or &#x60;groupId&#x60; is set.</value>
        [DataMember(Name="userId", EmitDefaultValue=false)]
        public string UserId { get; set; }

        /// <summary>
        /// The id of the group participating in this link. Either &#x60;groupId&#x60; or &#x60;userId&#x60; is set.
        /// </summary>
        /// <value>The id of the group participating in this link. Either &#x60;groupId&#x60; or &#x60;userId&#x60; is set.</value>
        [DataMember(Name="groupId", EmitDefaultValue=false)]
        public string GroupId { get; set; }

        /// <summary>
        /// The type of the identity link. The value of the this property can be user-defined. The Process Engine provides three pre-defined Identity Link &#x60;type&#x60;s:  * &#x60;candidate&#x60; * &#x60;assignee&#x60; - reserved for the task assignee * &#x60;owner&#x60; - reserved for the task owner  **Note**: When adding or removing an Identity Link, the &#x60;type&#x60; property must be defined.
        /// </summary>
        /// <value>The type of the identity link. The value of the this property can be user-defined. The Process Engine provides three pre-defined Identity Link &#x60;type&#x60;s:  * &#x60;candidate&#x60; * &#x60;assignee&#x60; - reserved for the task assignee * &#x60;owner&#x60; - reserved for the task owner  **Note**: When adding or removing an Identity Link, the &#x60;type&#x60; property must be defined.</value>
        [DataMember(Name="type", EmitDefaultValue=true)]
        public string Type { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class IdentityLinkDto {\n");
            sb.Append("  UserId: ").Append(UserId).Append("\n");
            sb.Append("  GroupId: ").Append(GroupId).Append("\n");
            sb.Append("  Type: ").Append(Type).Append("\n");
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
            return this.Equals(input as IdentityLinkDto);
        }

        /// <summary>
        /// Returns true if IdentityLinkDto instances are equal
        /// </summary>
        /// <param name="input">Instance of IdentityLinkDto to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(IdentityLinkDto input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.UserId == input.UserId ||
                    (this.UserId != null &&
                    this.UserId.Equals(input.UserId))
                ) && 
                (
                    this.GroupId == input.GroupId ||
                    (this.GroupId != null &&
                    this.GroupId.Equals(input.GroupId))
                ) && 
                (
                    this.Type == input.Type ||
                    (this.Type != null &&
                    this.Type.Equals(input.Type))
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
                if (this.UserId != null)
                    hashCode = hashCode * 59 + this.UserId.GetHashCode();
                if (this.GroupId != null)
                    hashCode = hashCode * 59 + this.GroupId.GetHashCode();
                if (this.Type != null)
                    hashCode = hashCode * 59 + this.Type.GetHashCode();
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
