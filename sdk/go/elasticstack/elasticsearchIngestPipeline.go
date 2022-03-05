// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package elasticstack

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// ## Import
//
// ```sh
//  $ pulumi import elasticstack:index/elasticsearchIngestPipeline:ElasticsearchIngestPipeline my_ingest_pipeline <cluster_uuid>/<ingest pipeline name>
// ```
type ElasticsearchIngestPipeline struct {
	pulumi.CustomResourceState

	// Description of the ingest pipeline.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Used to establish connection to Elasticsearch server. Overrides environment variables if present.
	ElasticsearchConnection ElasticsearchIngestPipelineElasticsearchConnectionPtrOutput `pulumi:"elasticsearchConnection"`
	// Internal identifier of the resource
	Id pulumi.StringOutput `pulumi:"id"`
	// Optional user metadata about the index template.
	Metadata pulumi.StringPtrOutput `pulumi:"metadata"`
	// The name of the ingest pipeline.
	Name pulumi.StringOutput `pulumi:"name"`
	// Processors to run immediately after a processor failure. Each processor supports a processor-level `onFailure` value. If a processor without an `onFailure` value fails, Elasticsearch uses this pipeline-level parameter as a fallback. The processors in this parameter run sequentially in the order specified. Elasticsearch will not attempt to run the pipeline’s remaining processors. See: https://www.elastic.co/guide/en/elasticsearch/reference/current/processors.html. Each record must be a valid JSON document
	OnFailures pulumi.StringArrayOutput `pulumi:"onFailures"`
	// Processors used to perform transformations on documents before indexing. Processors run sequentially in the order specified. See: https://www.elastic.co/guide/en/elasticsearch/reference/current/processors.html. Each record must be a valid JSON document.
	Processors pulumi.StringArrayOutput `pulumi:"processors"`
}

// NewElasticsearchIngestPipeline registers a new resource with the given unique name, arguments, and options.
func NewElasticsearchIngestPipeline(ctx *pulumi.Context,
	name string, args *ElasticsearchIngestPipelineArgs, opts ...pulumi.ResourceOption) (*ElasticsearchIngestPipeline, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Processors == nil {
		return nil, errors.New("invalid value for required argument 'Processors'")
	}
	var resource ElasticsearchIngestPipeline
	err := ctx.RegisterResource("elasticstack:index/elasticsearchIngestPipeline:ElasticsearchIngestPipeline", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetElasticsearchIngestPipeline gets an existing ElasticsearchIngestPipeline resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetElasticsearchIngestPipeline(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ElasticsearchIngestPipelineState, opts ...pulumi.ResourceOption) (*ElasticsearchIngestPipeline, error) {
	var resource ElasticsearchIngestPipeline
	err := ctx.ReadResource("elasticstack:index/elasticsearchIngestPipeline:ElasticsearchIngestPipeline", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ElasticsearchIngestPipeline resources.
type elasticsearchIngestPipelineState struct {
	// Description of the ingest pipeline.
	Description *string `pulumi:"description"`
	// Used to establish connection to Elasticsearch server. Overrides environment variables if present.
	ElasticsearchConnection *ElasticsearchIngestPipelineElasticsearchConnection `pulumi:"elasticsearchConnection"`
	// Internal identifier of the resource
	Id *string `pulumi:"id"`
	// Optional user metadata about the index template.
	Metadata *string `pulumi:"metadata"`
	// The name of the ingest pipeline.
	Name *string `pulumi:"name"`
	// Processors to run immediately after a processor failure. Each processor supports a processor-level `onFailure` value. If a processor without an `onFailure` value fails, Elasticsearch uses this pipeline-level parameter as a fallback. The processors in this parameter run sequentially in the order specified. Elasticsearch will not attempt to run the pipeline’s remaining processors. See: https://www.elastic.co/guide/en/elasticsearch/reference/current/processors.html. Each record must be a valid JSON document
	OnFailures []string `pulumi:"onFailures"`
	// Processors used to perform transformations on documents before indexing. Processors run sequentially in the order specified. See: https://www.elastic.co/guide/en/elasticsearch/reference/current/processors.html. Each record must be a valid JSON document.
	Processors []string `pulumi:"processors"`
}

type ElasticsearchIngestPipelineState struct {
	// Description of the ingest pipeline.
	Description pulumi.StringPtrInput
	// Used to establish connection to Elasticsearch server. Overrides environment variables if present.
	ElasticsearchConnection ElasticsearchIngestPipelineElasticsearchConnectionPtrInput
	// Internal identifier of the resource
	Id pulumi.StringPtrInput
	// Optional user metadata about the index template.
	Metadata pulumi.StringPtrInput
	// The name of the ingest pipeline.
	Name pulumi.StringPtrInput
	// Processors to run immediately after a processor failure. Each processor supports a processor-level `onFailure` value. If a processor without an `onFailure` value fails, Elasticsearch uses this pipeline-level parameter as a fallback. The processors in this parameter run sequentially in the order specified. Elasticsearch will not attempt to run the pipeline’s remaining processors. See: https://www.elastic.co/guide/en/elasticsearch/reference/current/processors.html. Each record must be a valid JSON document
	OnFailures pulumi.StringArrayInput
	// Processors used to perform transformations on documents before indexing. Processors run sequentially in the order specified. See: https://www.elastic.co/guide/en/elasticsearch/reference/current/processors.html. Each record must be a valid JSON document.
	Processors pulumi.StringArrayInput
}

func (ElasticsearchIngestPipelineState) ElementType() reflect.Type {
	return reflect.TypeOf((*elasticsearchIngestPipelineState)(nil)).Elem()
}

type elasticsearchIngestPipelineArgs struct {
	// Description of the ingest pipeline.
	Description *string `pulumi:"description"`
	// Used to establish connection to Elasticsearch server. Overrides environment variables if present.
	ElasticsearchConnection *ElasticsearchIngestPipelineElasticsearchConnection `pulumi:"elasticsearchConnection"`
	// Optional user metadata about the index template.
	Metadata *string `pulumi:"metadata"`
	// The name of the ingest pipeline.
	Name *string `pulumi:"name"`
	// Processors to run immediately after a processor failure. Each processor supports a processor-level `onFailure` value. If a processor without an `onFailure` value fails, Elasticsearch uses this pipeline-level parameter as a fallback. The processors in this parameter run sequentially in the order specified. Elasticsearch will not attempt to run the pipeline’s remaining processors. See: https://www.elastic.co/guide/en/elasticsearch/reference/current/processors.html. Each record must be a valid JSON document
	OnFailures []string `pulumi:"onFailures"`
	// Processors used to perform transformations on documents before indexing. Processors run sequentially in the order specified. See: https://www.elastic.co/guide/en/elasticsearch/reference/current/processors.html. Each record must be a valid JSON document.
	Processors []string `pulumi:"processors"`
}

// The set of arguments for constructing a ElasticsearchIngestPipeline resource.
type ElasticsearchIngestPipelineArgs struct {
	// Description of the ingest pipeline.
	Description pulumi.StringPtrInput
	// Used to establish connection to Elasticsearch server. Overrides environment variables if present.
	ElasticsearchConnection ElasticsearchIngestPipelineElasticsearchConnectionPtrInput
	// Optional user metadata about the index template.
	Metadata pulumi.StringPtrInput
	// The name of the ingest pipeline.
	Name pulumi.StringPtrInput
	// Processors to run immediately after a processor failure. Each processor supports a processor-level `onFailure` value. If a processor without an `onFailure` value fails, Elasticsearch uses this pipeline-level parameter as a fallback. The processors in this parameter run sequentially in the order specified. Elasticsearch will not attempt to run the pipeline’s remaining processors. See: https://www.elastic.co/guide/en/elasticsearch/reference/current/processors.html. Each record must be a valid JSON document
	OnFailures pulumi.StringArrayInput
	// Processors used to perform transformations on documents before indexing. Processors run sequentially in the order specified. See: https://www.elastic.co/guide/en/elasticsearch/reference/current/processors.html. Each record must be a valid JSON document.
	Processors pulumi.StringArrayInput
}

func (ElasticsearchIngestPipelineArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*elasticsearchIngestPipelineArgs)(nil)).Elem()
}

type ElasticsearchIngestPipelineInput interface {
	pulumi.Input

	ToElasticsearchIngestPipelineOutput() ElasticsearchIngestPipelineOutput
	ToElasticsearchIngestPipelineOutputWithContext(ctx context.Context) ElasticsearchIngestPipelineOutput
}

func (*ElasticsearchIngestPipeline) ElementType() reflect.Type {
	return reflect.TypeOf((**ElasticsearchIngestPipeline)(nil)).Elem()
}

func (i *ElasticsearchIngestPipeline) ToElasticsearchIngestPipelineOutput() ElasticsearchIngestPipelineOutput {
	return i.ToElasticsearchIngestPipelineOutputWithContext(context.Background())
}

func (i *ElasticsearchIngestPipeline) ToElasticsearchIngestPipelineOutputWithContext(ctx context.Context) ElasticsearchIngestPipelineOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ElasticsearchIngestPipelineOutput)
}

// ElasticsearchIngestPipelineArrayInput is an input type that accepts ElasticsearchIngestPipelineArray and ElasticsearchIngestPipelineArrayOutput values.
// You can construct a concrete instance of `ElasticsearchIngestPipelineArrayInput` via:
//
//          ElasticsearchIngestPipelineArray{ ElasticsearchIngestPipelineArgs{...} }
type ElasticsearchIngestPipelineArrayInput interface {
	pulumi.Input

	ToElasticsearchIngestPipelineArrayOutput() ElasticsearchIngestPipelineArrayOutput
	ToElasticsearchIngestPipelineArrayOutputWithContext(context.Context) ElasticsearchIngestPipelineArrayOutput
}

type ElasticsearchIngestPipelineArray []ElasticsearchIngestPipelineInput

func (ElasticsearchIngestPipelineArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ElasticsearchIngestPipeline)(nil)).Elem()
}

func (i ElasticsearchIngestPipelineArray) ToElasticsearchIngestPipelineArrayOutput() ElasticsearchIngestPipelineArrayOutput {
	return i.ToElasticsearchIngestPipelineArrayOutputWithContext(context.Background())
}

func (i ElasticsearchIngestPipelineArray) ToElasticsearchIngestPipelineArrayOutputWithContext(ctx context.Context) ElasticsearchIngestPipelineArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ElasticsearchIngestPipelineArrayOutput)
}

// ElasticsearchIngestPipelineMapInput is an input type that accepts ElasticsearchIngestPipelineMap and ElasticsearchIngestPipelineMapOutput values.
// You can construct a concrete instance of `ElasticsearchIngestPipelineMapInput` via:
//
//          ElasticsearchIngestPipelineMap{ "key": ElasticsearchIngestPipelineArgs{...} }
type ElasticsearchIngestPipelineMapInput interface {
	pulumi.Input

	ToElasticsearchIngestPipelineMapOutput() ElasticsearchIngestPipelineMapOutput
	ToElasticsearchIngestPipelineMapOutputWithContext(context.Context) ElasticsearchIngestPipelineMapOutput
}

type ElasticsearchIngestPipelineMap map[string]ElasticsearchIngestPipelineInput

func (ElasticsearchIngestPipelineMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ElasticsearchIngestPipeline)(nil)).Elem()
}

func (i ElasticsearchIngestPipelineMap) ToElasticsearchIngestPipelineMapOutput() ElasticsearchIngestPipelineMapOutput {
	return i.ToElasticsearchIngestPipelineMapOutputWithContext(context.Background())
}

func (i ElasticsearchIngestPipelineMap) ToElasticsearchIngestPipelineMapOutputWithContext(ctx context.Context) ElasticsearchIngestPipelineMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ElasticsearchIngestPipelineMapOutput)
}

type ElasticsearchIngestPipelineOutput struct{ *pulumi.OutputState }

func (ElasticsearchIngestPipelineOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ElasticsearchIngestPipeline)(nil)).Elem()
}

func (o ElasticsearchIngestPipelineOutput) ToElasticsearchIngestPipelineOutput() ElasticsearchIngestPipelineOutput {
	return o
}

func (o ElasticsearchIngestPipelineOutput) ToElasticsearchIngestPipelineOutputWithContext(ctx context.Context) ElasticsearchIngestPipelineOutput {
	return o
}

type ElasticsearchIngestPipelineArrayOutput struct{ *pulumi.OutputState }

func (ElasticsearchIngestPipelineArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ElasticsearchIngestPipeline)(nil)).Elem()
}

func (o ElasticsearchIngestPipelineArrayOutput) ToElasticsearchIngestPipelineArrayOutput() ElasticsearchIngestPipelineArrayOutput {
	return o
}

func (o ElasticsearchIngestPipelineArrayOutput) ToElasticsearchIngestPipelineArrayOutputWithContext(ctx context.Context) ElasticsearchIngestPipelineArrayOutput {
	return o
}

func (o ElasticsearchIngestPipelineArrayOutput) Index(i pulumi.IntInput) ElasticsearchIngestPipelineOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *ElasticsearchIngestPipeline {
		return vs[0].([]*ElasticsearchIngestPipeline)[vs[1].(int)]
	}).(ElasticsearchIngestPipelineOutput)
}

type ElasticsearchIngestPipelineMapOutput struct{ *pulumi.OutputState }

func (ElasticsearchIngestPipelineMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ElasticsearchIngestPipeline)(nil)).Elem()
}

func (o ElasticsearchIngestPipelineMapOutput) ToElasticsearchIngestPipelineMapOutput() ElasticsearchIngestPipelineMapOutput {
	return o
}

func (o ElasticsearchIngestPipelineMapOutput) ToElasticsearchIngestPipelineMapOutputWithContext(ctx context.Context) ElasticsearchIngestPipelineMapOutput {
	return o
}

func (o ElasticsearchIngestPipelineMapOutput) MapIndex(k pulumi.StringInput) ElasticsearchIngestPipelineOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *ElasticsearchIngestPipeline {
		return vs[0].(map[string]*ElasticsearchIngestPipeline)[vs[1].(string)]
	}).(ElasticsearchIngestPipelineOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ElasticsearchIngestPipelineInput)(nil)).Elem(), &ElasticsearchIngestPipeline{})
	pulumi.RegisterInputType(reflect.TypeOf((*ElasticsearchIngestPipelineArrayInput)(nil)).Elem(), ElasticsearchIngestPipelineArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ElasticsearchIngestPipelineMapInput)(nil)).Elem(), ElasticsearchIngestPipelineMap{})
	pulumi.RegisterOutputType(ElasticsearchIngestPipelineOutput{})
	pulumi.RegisterOutputType(ElasticsearchIngestPipelineArrayOutput{})
	pulumi.RegisterOutputType(ElasticsearchIngestPipelineMapOutput{})
}
