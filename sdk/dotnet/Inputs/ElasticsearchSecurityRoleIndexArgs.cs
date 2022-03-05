// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Elasticstack.Inputs
{

    public sealed class ElasticsearchSecurityRoleIndexArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The document fields that the owners of the role have read access to.
        /// </summary>
        [Input("fieldSecurity")]
        public Input<Inputs.ElasticsearchSecurityRoleIndexFieldSecurityArgs>? FieldSecurity { get; set; }

        [Input("names", required: true)]
        private InputList<string>? _names;

        /// <summary>
        /// A list of indices (or index name patterns) to which the permissions in this entry apply.
        /// </summary>
        public InputList<string> Names
        {
            get => _names ?? (_names = new InputList<string>());
            set => _names = value;
        }

        [Input("privileges", required: true)]
        private InputList<string>? _privileges;

        /// <summary>
        /// The index level privileges that the owners of the role have on the specified indices.
        /// </summary>
        public InputList<string> Privileges
        {
            get => _privileges ?? (_privileges = new InputList<string>());
            set => _privileges = value;
        }

        /// <summary>
        /// A search query that defines the documents the owners of the role have read access to.
        /// </summary>
        [Input("query")]
        public Input<string>? Query { get; set; }

        public ElasticsearchSecurityRoleIndexArgs()
        {
        }
    }
}
