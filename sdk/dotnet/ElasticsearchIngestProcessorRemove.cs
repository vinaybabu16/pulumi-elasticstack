// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Elasticstack
{
    public static class ElasticsearchIngestProcessorRemove
    {
        /// <summary>
        /// Removes existing fields. If one field doesn’t exist, an exception will be thrown.
        /// 
        /// See: https://www.elastic.co/guide/en/elasticsearch/reference/current/remove-processor.html
        /// 
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
        ///         var @remove = Output.Create(Elasticstack.ElasticsearchIngestProcessorRemove.InvokeAsync(new Elasticstack.ElasticsearchIngestProcessorRemoveArgs
        ///         {
        ///             Fields = 
        ///             {
        ///                 "user_agent",
        ///                 "url",
        ///             },
        ///         }));
        ///         var myIngestPipeline = new Elasticstack.ElasticsearchIngestPipeline("myIngestPipeline", new Elasticstack.ElasticsearchIngestPipelineArgs
        ///         {
        ///             Processors = 
        ///             {
        ///                 @remove.Apply(@remove =&gt; @remove.Json),
        ///             },
        ///         });
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<ElasticsearchIngestProcessorRemoveResult> InvokeAsync(ElasticsearchIngestProcessorRemoveArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<ElasticsearchIngestProcessorRemoveResult>("elasticstack:index/elasticsearchIngestProcessorRemove:ElasticsearchIngestProcessorRemove", args ?? new ElasticsearchIngestProcessorRemoveArgs(), options.WithDefaults());

        /// <summary>
        /// Removes existing fields. If one field doesn’t exist, an exception will be thrown.
        /// 
        /// See: https://www.elastic.co/guide/en/elasticsearch/reference/current/remove-processor.html
        /// 
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
        ///         var @remove = Output.Create(Elasticstack.ElasticsearchIngestProcessorRemove.InvokeAsync(new Elasticstack.ElasticsearchIngestProcessorRemoveArgs
        ///         {
        ///             Fields = 
        ///             {
        ///                 "user_agent",
        ///                 "url",
        ///             },
        ///         }));
        ///         var myIngestPipeline = new Elasticstack.ElasticsearchIngestPipeline("myIngestPipeline", new Elasticstack.ElasticsearchIngestPipelineArgs
        ///         {
        ///             Processors = 
        ///             {
        ///                 @remove.Apply(@remove =&gt; @remove.Json),
        ///             },
        ///         });
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<ElasticsearchIngestProcessorRemoveResult> Invoke(ElasticsearchIngestProcessorRemoveInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<ElasticsearchIngestProcessorRemoveResult>("elasticstack:index/elasticsearchIngestProcessorRemove:ElasticsearchIngestProcessorRemove", args ?? new ElasticsearchIngestProcessorRemoveInvokeArgs(), options.WithDefaults());
    }


    public sealed class ElasticsearchIngestProcessorRemoveArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Description of the processor.
        /// </summary>
        [Input("description")]
        public string? Description { get; set; }

        [Input("fields", required: true)]
        private List<string>? _fields;

        /// <summary>
        /// Fields to be removed.
        /// </summary>
        public List<string> Fields
        {
            get => _fields ?? (_fields = new List<string>());
            set => _fields = value;
        }

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
        /// Identifier for the processor.
        /// </summary>
        [Input("tag")]
        public string? Tag { get; set; }

        public ElasticsearchIngestProcessorRemoveArgs()
        {
        }
    }

    public sealed class ElasticsearchIngestProcessorRemoveInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Description of the processor.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("fields", required: true)]
        private InputList<string>? _fields;

        /// <summary>
        /// Fields to be removed.
        /// </summary>
        public InputList<string> Fields
        {
            get => _fields ?? (_fields = new InputList<string>());
            set => _fields = value;
        }

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
        /// Identifier for the processor.
        /// </summary>
        [Input("tag")]
        public Input<string>? Tag { get; set; }

        public ElasticsearchIngestProcessorRemoveInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class ElasticsearchIngestProcessorRemoveResult
    {
        /// <summary>
        /// Description of the processor.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// Fields to be removed.
        /// </summary>
        public readonly ImmutableArray<string> Fields;
        /// <summary>
        /// Internal identifier of the resource.
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
        /// Handle failures for the processor.
        /// </summary>
        public readonly ImmutableArray<string> OnFailures;
        /// <summary>
        /// Identifier for the processor.
        /// </summary>
        public readonly string? Tag;

        [OutputConstructor]
        private ElasticsearchIngestProcessorRemoveResult(
            string? description,

            ImmutableArray<string> fields,

            string id,

            string? @if,

            bool? ignoreFailure,

            bool? ignoreMissing,

            string json,

            ImmutableArray<string> onFailures,

            string? tag)
        {
            Description = description;
            Fields = fields;
            Id = id;
            If = @if;
            IgnoreFailure = ignoreFailure;
            IgnoreMissing = ignoreMissing;
            Json = json;
            OnFailures = onFailures;
            Tag = tag;
        }
    }
}
