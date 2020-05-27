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
    /// VariableQueryParameterDto
    /// </summary>
    [DataContract]
    public partial class VariableQueryParameterDto :  IEquatable<VariableQueryParameterDto>, IValidatableObject
    {
        /// <summary>
        /// Comparison operator to be used
        /// </summary>
        /// <value>Comparison operator to be used</value>
        [JsonConverter(typeof(StringEnumConverter))]
        public enum OperatorEnum
        {
            /// <summary>
            /// Enum Eq for value: eq
            /// </summary>
            [EnumMember(Value = "eq")]
            Eq = 1,

            /// <summary>
            /// Enum Neq for value: neq
            /// </summary>
            [EnumMember(Value = "neq")]
            Neq = 2,

            /// <summary>
            /// Enum Gt for value: gt
            /// </summary>
            [EnumMember(Value = "gt")]
            Gt = 3,

            /// <summary>
            /// Enum Gteq for value: gteq
            /// </summary>
            [EnumMember(Value = "gteq")]
            Gteq = 4,

            /// <summary>
            /// Enum Lt for value: lt
            /// </summary>
            [EnumMember(Value = "lt")]
            Lt = 5,

            /// <summary>
            /// Enum Lteq for value: lteq
            /// </summary>
            [EnumMember(Value = "lteq")]
            Lteq = 6,

            /// <summary>
            /// Enum Like for value: like
            /// </summary>
            [EnumMember(Value = "like")]
            Like = 7

        }

        /// <summary>
        /// Comparison operator to be used
        /// </summary>
        /// <value>Comparison operator to be used</value>
        [DataMember(Name="operator", EmitDefaultValue=false)]
        public OperatorEnum? Operator { get; set; }
        /// <summary>
        /// Initializes a new instance of the <see cref="VariableQueryParameterDto" /> class.
        /// </summary>
        /// <param name="value">The variable value, could be of type boolean, string or number.</param>
        /// <param name="_operator">Comparison operator to be used.</param>
        public VariableQueryParameterDto(Object value = default(Object), OperatorEnum? _operator = default(OperatorEnum?))
        {
            this.Value = value;
            this.Operator = _operator;
        }
        
        /// <summary>
        /// The variable value, could be of type boolean, string or number
        /// </summary>
        /// <value>The variable value, could be of type boolean, string or number</value>
        [DataMember(Name="value", EmitDefaultValue=false)]
        public Object Value { get; set; }


        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class VariableQueryParameterDto {\n");
            sb.Append("  Value: ").Append(Value).Append("\n");
            sb.Append("  Operator: ").Append(Operator).Append("\n");
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
            return this.Equals(input as VariableQueryParameterDto);
        }

        /// <summary>
        /// Returns true if VariableQueryParameterDto instances are equal
        /// </summary>
        /// <param name="input">Instance of VariableQueryParameterDto to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(VariableQueryParameterDto input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Value == input.Value ||
                    (this.Value != null &&
                    this.Value.Equals(input.Value))
                ) && 
                (
                    this.Operator == input.Operator ||
                    (this.Operator != null &&
                    this.Operator.Equals(input.Operator))
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
                if (this.Value != null)
                    hashCode = hashCode * 59 + this.Value.GetHashCode();
                if (this.Operator != null)
                    hashCode = hashCode * 59 + this.Operator.GetHashCode();
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
