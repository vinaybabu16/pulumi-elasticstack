// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Elasticstack.Inputs
{

    public sealed class ElasticsearchIndexLifecycleElasticsearchConnectionArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Path to a custom Certificate Authority certificate
        /// </summary>
        [Input("caFile")]
        public Input<string>? CaFile { get; set; }

        [Input("endpoints")]
        private InputList<string>? _endpoints;
        public InputList<string> Endpoints
        {
            get => _endpoints ?? (_endpoints = new InputList<string>());
            set => _endpoints = value;
        }

        /// <summary>
        /// Disable TLS certificate validation
        /// </summary>
        [Input("insecure")]
        public Input<bool>? Insecure { get; set; }

        /// <summary>
        /// A password to use for API authentication to Elasticsearch.
        /// </summary>
        [Input("password")]
        public Input<string>? Password { get; set; }

        /// <summary>
        /// A username to use for API authentication to Elasticsearch.
        /// </summary>
        [Input("username")]
        public Input<string>? Username { get; set; }

        public ElasticsearchIndexLifecycleElasticsearchConnectionArgs()
        {
        }
    }
}
