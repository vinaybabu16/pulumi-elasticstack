// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Elasticstack
{
    public static class ElasticsearchIngestProcessorEnrich
    {
        /// <summary>
        /// The enrich processor can enrich documents with data from another index. See enrich data section for more information about how to set this up.
        /// 
        /// See: https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest-enriching-data.html and https://www.elastic.co/guide/en/elasticsearch/reference/current/enrich-processor.html
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Elasticstack = Pulumi.Elasticstack;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var enrich = Output.Create(Elasticstack.ElasticsearchIngestProcessorEnrich.InvokeAsync(new Elasticstack.ElasticsearchIngestProcessorEnrichArgs
        ///         {
        ///             PolicyName = "users-policy",
        ///             Field = "email",
        ///             TargetField = "user",
        ///             MaxMatches = 1,
        ///         }));
        ///         var myIngestPipeline = new Elasticstack.ElasticsearchIngestPipeline("myIngestPipeline", new Elasticstack.ElasticsearchIngestPipelineArgs
        ///         {
        ///             Processors = 
        ///             {
        ///                 enrich.Apply(enrich =&gt; enrich.Json),
        ///             },
        ///         });
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<ElasticsearchIngestProcessorEnrichResult> InvokeAsync(ElasticsearchIngestProcessorEnrichArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<ElasticsearchIngestProcessorEnrichResult>("elasticstack:index/elasticsearchIngestProcessorEnrich:ElasticsearchIngestProcessorEnrich", args ?? new ElasticsearchIngestProcessorEnrichArgs(), options.WithDefaults());

        /// <summary>
        /// The enrich processor can enrich documents with data from another index. See enrich data section for more information about how to set this up.
        /// 
        /// See: https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest-enriching-data.html and https://www.elastic.co/guide/en/elasticsearch/reference/current/enrich-processor.html
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Elasticstack = Pulumi.Elasticstack;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var enrich = Output.Create(Elasticstack.ElasticsearchIngestProcessorEnrich.InvokeAsync(new Elasticstack.ElasticsearchIngestProcessorEnrichArgs
        ///         {
        ///             PolicyName = "users-policy",
        ///             Field = "email",
        ///             TargetField = "user",
        ///             MaxMatches = 1,
        ///         }));
        ///         var myIngestPipeline = new Elasticstack.ElasticsearchIngestPipeline("myIngestPipeline", new Elasticstack.ElasticsearchIngestPipelineArgs
        ///         {
        ///             Processors = 
        ///             {
        ///                 enrich.Apply(enrich =&gt; enrich.Json),
        ///             },
        ///         });
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<ElasticsearchIngestProcessorEnrichResult> Invoke(ElasticsearchIngestProcessorEnrichInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<ElasticsearchIngestProcessorEnrichResult>("elasticstack:index/elasticsearchIngestProcessorEnrich:ElasticsearchIngestProcessorEnrich", args ?? new ElasticsearchIngestProcessorEnrichInvokeArgs(), options.WithDefaults());
    }


    public sealed class ElasticsearchIngestProcessorEnrichArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Description of the processor.
        /// </summary>
        [Input("description")]
        public string? Description { get; set; }

        /// <summary>
        /// The field in the input document that matches the policies match_field used to retrieve the enrichment data.
        /// </summary>
        [Input("field", required: true)]
        public string Field { get; set; } = null!;

        /// <summary>
        /// Conditionally execute the processor
        /// </summary>
        [Input("if")]
        public string? If { get; set; }

        /// <summary>
        /// Ignore failures for the processor.
        /// </summary>
        [Input("ignoreFailure")]
        public bool? IgnoreFailure { get; set; }

        /// <summary>
        /// If `true` and `field` does not exist or is `null`, the processor quietly exits without modifying the document.
        /// </summary>
        [Input("ignoreMissing")]
        public bool? IgnoreMissing { get; set; }

        /// <summary>
        /// The maximum number of matched documents to include under the configured target field.
        /// </summary>
        [Input("maxMatches")]
        public int? MaxMatches { get; set; }

        [Input("onFailures")]
        private List<string>? _onFailures;

        /// <summary>
        /// Handle failures for the processor.
        /// </summary>
        public List<string> OnFailures
        {
            get => _onFailures ?? (_onFailures = new List<string>());
            set => _onFailures = value;
        }

        /// <summary>
        /// If processor will update fields with pre-existing non-null-valued field.
        /// </summary>
        [Input("override")]
        public bool? Override { get; set; }

        /// <summary>
        /// The name of the enrich policy to use.
        /// </summary>
        [Input("policyName", required: true)]
        public string PolicyName { get; set; } = null!;

        /// <summary>
        /// A spatial relation operator used to match the geoshape of incoming documents to documents in the enrich index.
        /// </summary>
        [Input("shapeRelation")]
        public string? ShapeRelation { get; set; }

        /// <summary>
        /// Identifier for the processor.
        /// </summary>
        [Input("tag")]
        public string? Tag { get; set; }

        /// <summary>
        /// Field added to incoming documents to contain enrich data.
        /// </summary>
        [Input("targetField", required: true)]
        public string TargetField { get; set; } = null!;

        public ElasticsearchIngestProcessorEnrichArgs()
        {
        }
    }

    public sealed class ElasticsearchIngestProcessorEnrichInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Description of the processor.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The field in the input document that matches the policies match_field used to retrieve the enrichment data.
        /// </summary>
        [Input("field", required: true)]
        public Input<string> Field { get; set; } = null!;

        /// <summary>
        /// Conditionally execute the processor
        /// </summary>
        [Input("if")]
        public Input<string>? If { get; set; }

        /// <summary>
        /// Ignore failures for the processor.
        /// </summary>
        [Input("ignoreFailure")]
        public Input<bool>? IgnoreFailure { get; set; }

        /// <summary>
        /// If `true` and `field` does not exist or is `null`, the processor quietly exits without modifying the document.
        /// </summary>
        [Input("ignoreMissing")]
        public Input<bool>? IgnoreMissing { get; set; }

        /// <summary>
        /// The maximum number of matched documents to include under the configured target field.
        /// </summary>
        [Input("maxMatches")]
        public Input<int>? MaxMatches { get; set; }

        [Input("onFailures")]
        private InputList<string>? _onFailures;

        /// <summary>
        /// Handle failures for the processor.
        /// </summary>
        public InputList<string> OnFailures
        {
            get => _onFailures ?? (_onFailures = new InputList<string>());
            set => _onFailures = value;
        }

        /// <summary>
        /// If processor will update fields with pre-existing non-null-valued field.
        /// </summary>
        [Input("override")]
        public Input<bool>? Override { get; set; }

        /// <summary>
        /// The name of the enrich policy to use.
        /// </summary>
        [Input("policyName", required: true)]
        public Input<string> PolicyName { get; set; } = null!;

        /// <summary>
        /// A spatial relation operator used to match the geoshape of incoming documents to documents in the enrich index.
        /// </summary>
        [Input("shapeRelation")]
        public Input<string>? ShapeRelation { get; set; }

        /// <summary>
        /// Identifier for the processor.
        /// </summary>
        [Input("tag")]
        public Input<string>? Tag { get; set; }

        /// <summary>
        /// Field added to incoming documents to contain enrich data.
        /// </summary>
        [Input("targetField", required: true)]
        public Input<string> TargetField { get; set; } = null!;

        public ElasticsearchIngestProcessorEnrichInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class ElasticsearchIngestProcessorEnrichResult
    {
        /// <summary>
        /// Description of the processor.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// The field in the input document that matches the policies match_field used to retrieve the enrichment data.
        /// </summary>
        public readonly string Field;
        /// <summary>
        /// Internal identifier of the resource
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Conditionally execute the processor
        /// </summary>
        public readonly string? If;
        /// <summary>
        /// Ignore failures for the processor.
        /// </summary>
        public readonly bool? IgnoreFailure;
        /// <summary>
        /// If `true` and `field` does not exist or is `null`, the processor quietly exits without modifying the document.
        /// </summary>
        public readonly bool? IgnoreMissing;
        /// <summary>
        /// JSON representation of this data source.
        /// </summary>
        public readonly string Json;
        /// <summary>
        /// The maximum number of matched documents to include under the configured target field.
        /// </summary>
        public readonly int? MaxMatches;
        /// <summary>
        /// Handle failures for the processor.
        /// </summary>
        public readonly ImmutableArray<string> OnFailures;
        /// <summary>
        /// If processor will update fields with pre-existing non-null-valued field.
        /// </summary>
        public readonly bool? Override;
        /// <summary>
        /// The name of the enrich policy to use.
        /// </summary>
        public readonly string PolicyName;
        /// <summary>
        /// A spatial relation operator used to match the geoshape of incoming documents to documents in the enrich index.
        /// </summary>
        public readonly string? ShapeRelation;
        /// <summary>
        /// Identifier for the processor.
        /// </summary>
        public readonly string? Tag;
        /// <summary>
        /// Field added to incoming documents to contain enrich data.
        /// </summary>
        public readonly string TargetField;

        [OutputConstructor]
        private ElasticsearchIngestProcessorEnrichResult(
            string? description,

            string field,

            string id,

            string? @if,

            bool? ignoreFailure,

            bool? ignoreMissing,

            string json,

            int? maxMatches,

            ImmutableArray<string> onFailures,

            bool? @override,

            string policyName,

            string? shapeRelation,

            string? tag,

            string targetField)
        {
            Description = description;
            Field = field;
            Id = id;
            If = @if;
            IgnoreFailure = ignoreFailure;
            IgnoreMissing = ignoreMissing;
            Json = json;
            MaxMatches = maxMatches;
            OnFailures = onFailures;
            Override = @override;
            PolicyName = policyName;
            ShapeRelation = shapeRelation;
            Tag = tag;
            TargetField = targetField;
        }
    }
}
