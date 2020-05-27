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
    /// AuthorizationExceptionDtoAllOf
    /// </summary>
    [DataContract]
    public partial class AuthorizationExceptionDtoAllOf :  IEquatable<AuthorizationExceptionDtoAllOf>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="AuthorizationExceptionDtoAllOf" /> class.
        /// </summary>
        /// <param name="userId">The id of the user that does not have expected permissions.</param>
        /// <param name="missingAuthorizations">missingAuthorizations.</param>
        public AuthorizationExceptionDtoAllOf(string userId = default(string), List<MissingAuthorizationDto> missingAuthorizations = default(List<MissingAuthorizationDto>))
        {
            this.UserId = userId;
            this.MissingAuthorizations = missingAuthorizations;
        }
        
        /// <summary>
        /// The id of the user that does not have expected permissions
        /// </summary>
        /// <value>The id of the user that does not have expected permissions</value>
        [DataMember(Name="userId", EmitDefaultValue=false)]
        public string UserId { get; set; }

        /// <summary>
        /// Gets or Sets MissingAuthorizations
        /// </summary>
        [DataMember(Name="missingAuthorizations", EmitDefaultValue=false)]
        public List<MissingAuthorizationDto> MissingAuthorizations { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class AuthorizationExceptionDtoAllOf {\n");
            sb.Append("  UserId: ").Append(UserId).Append("\n");
            sb.Append("  MissingAuthorizations: ").Append(MissingAuthorizations).Append("\n");
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
            return this.Equals(input as AuthorizationExceptionDtoAllOf);
        }

        /// <summary>
        /// Returns true if AuthorizationExceptionDtoAllOf instances are equal
        /// </summary>
        /// <param name="input">Instance of AuthorizationExceptionDtoAllOf to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(AuthorizationExceptionDtoAllOf input)
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
                    this.MissingAuthorizations == input.MissingAuthorizations ||
                    this.MissingAuthorizations != null &&
                    input.MissingAuthorizations != null &&
                    this.MissingAuthorizations.SequenceEqual(input.MissingAuthorizations)
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
                if (this.MissingAuthorizations != null)
                    hashCode = hashCode * 59 + this.MissingAuthorizations.GetHashCode();
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
