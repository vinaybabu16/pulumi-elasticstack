// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Elasticstack.Outputs
{

    [OutputType]
    public sealed class ElasticsearchComponentTemplateElasticsearchConnection
    {
        /// <summary>
        /// Path to a custom Certificate Authority certificate
        /// </summary>
        public readonly string? CaFile;
        public readonly ImmutableArray<string> Endpoints;
        /// <summary>
        /// Disable TLS certificate validation
        /// </summary>
        public readonly bool? Insecure;
        /// <summary>
        /// A password to use for API authentication to Elasticsearch.
        /// </summary>
        public readonly string? Password;
        /// <summary>
        /// A username to use for API authentication to Elasticsearch.
        /// </summary>
        public readonly string? Username;

        [OutputConstructor]
        private ElasticsearchComponentTemplateElasticsearchConnection(
            string? caFile,

            ImmutableArray<string> endpoints,

            bool? insecure,

            string? password,

            string? username)
        {
            CaFile = caFile;
            Endpoints = endpoints;
            Insecure = insecure;
            Password = password;
            Username = username;
        }
    }
}
