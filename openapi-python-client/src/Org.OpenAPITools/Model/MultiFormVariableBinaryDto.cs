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
    /// MultiFormVariableBinaryDto
    /// </summary>
    [DataContract]
    public partial class MultiFormVariableBinaryDto :  IEquatable<MultiFormVariableBinaryDto>, IValidatableObject
    {
        /// <summary>
        /// The name of the variable type. Either Bytes for a byte array variable or File for a file variable.
        /// </summary>
        /// <value>The name of the variable type. Either Bytes for a byte array variable or File for a file variable.</value>
        [JsonConverter(typeof(StringEnumConverter))]
        public enum ValueTypeEnum
        {
            /// <summary>
            /// Enum Bytes for value: Bytes
            /// </summary>
            [EnumMember(Value = "Bytes")]
            Bytes = 1,

            /// <summary>
            /// Enum File for value: File
            /// </summary>
            [EnumMember(Value = "File")]
            File = 2

        }

        /// <summary>
        /// The name of the variable type. Either Bytes for a byte array variable or File for a file variable.
        /// </summary>
        /// <value>The name of the variable type. Either Bytes for a byte array variable or File for a file variable.</value>
        [DataMember(Name="valueType", EmitDefaultValue=false)]
        public ValueTypeEnum? ValueType { get; set; }
        /// <summary>
        /// Initializes a new instance of the <see cref="MultiFormVariableBinaryDto" /> class.
        /// </summary>
        /// <param name="data">The binary data to be set. For File variables, this multipart can contain the filename, binary value and MIME type of the file variable to be set Only the filename is mandatory..</param>
        /// <param name="valueType">The name of the variable type. Either Bytes for a byte array variable or File for a file variable..</param>
        public MultiFormVariableBinaryDto(System.IO.Stream data = default(System.IO.Stream), ValueTypeEnum? valueType = default(ValueTypeEnum?))
        {
            this.Data = data;
            this.Data = data;
            this.ValueType = valueType;
        }
        
        /// <summary>
        /// The binary data to be set. For File variables, this multipart can contain the filename, binary value and MIME type of the file variable to be set Only the filename is mandatory.
        /// </summary>
        /// <value>The binary data to be set. For File variables, this multipart can contain the filename, binary value and MIME type of the file variable to be set Only the filename is mandatory.</value>
        [DataMember(Name="data", EmitDefaultValue=true)]
        public System.IO.Stream Data { get; set; }


        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class MultiFormVariableBinaryDto {\n");
            sb.Append("  Data: ").Append(Data).Append("\n");
            sb.Append("  ValueType: ").Append(ValueType).Append("\n");
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
            return this.Equals(input as MultiFormVariableBinaryDto);
        }

        /// <summary>
        /// Returns true if MultiFormVariableBinaryDto instances are equal
        /// </summary>
        /// <param name="input">Instance of MultiFormVariableBinaryDto to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(MultiFormVariableBinaryDto input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Data == input.Data ||
                    (this.Data != null &&
                    this.Data.Equals(input.Data))
                ) && 
                (
                    this.ValueType == input.ValueType ||
                    (this.ValueType != null &&
                    this.ValueType.Equals(input.ValueType))
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
                if (this.Data != null)
                    hashCode = hashCode * 59 + this.Data.GetHashCode();
                if (this.ValueType != null)
                    hashCode = hashCode * 59 + this.ValueType.GetHashCode();
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
