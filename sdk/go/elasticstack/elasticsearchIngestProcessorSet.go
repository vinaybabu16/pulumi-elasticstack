// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package elasticstack

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Sets one field and associates it with the specified value. If the field already exists, its value will be replaced with the provided one.
//
// See: https://www.elastic.co/guide/en/elasticsearch/reference/current/set-processor.html
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-elasticstack/sdk/go/elasticstack"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		opt0 := "1"
// 		set, err := elasticstack.ElasticsearchIngestProcessorSet(ctx, &ElasticsearchIngestProcessorSetArgs{
// 			Field: "count",
// 			Value: &opt0,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = elasticstack.NewElasticsearchIngestPipeline(ctx, "myIngestPipeline", &elasticstack.ElasticsearchIngestPipelineArgs{
// 			Processors: pulumi.StringArray{
// 				pulumi.String(set.Json),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func ElasticsearchIngestProcessorSet(ctx *pulumi.Context, args *ElasticsearchIngestProcessorSetArgs, opts ...pulumi.InvokeOption) (*ElasticsearchIngestProcessorSetResult, error) {
	var rv ElasticsearchIngestProcessorSetResult
	err := ctx.Invoke("elasticstack:index/elasticsearchIngestProcessorSet:ElasticsearchIngestProcessorSet", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking ElasticsearchIngestProcessorSet.
type ElasticsearchIngestProcessorSetArgs struct {
	// The origin field which will be copied to `field`, cannot set `value` simultaneously.
	CopyFrom *string `pulumi:"copyFrom"`
	// Description of the processor.
	Description *string `pulumi:"description"`
	// The field to insert, upsert, or update.
	Field string `pulumi:"field"`
	// Conditionally execute the processor
	If *string `pulumi:"if"`
	// If `true` and `value` is a template snippet that evaluates to `null` or the empty string, the processor quietly exits without modifying the document
	IgnoreEmptyValue *bool `pulumi:"ignoreEmptyValue"`
	// Ignore failures for the processor.
	IgnoreFailure *bool `pulumi:"ignoreFailure"`
	// The media type for encoding value.
	MediaType *string `pulumi:"mediaType"`
	// Handle failures for the processor.
	OnFailures []string `pulumi:"onFailures"`
	// If processor will update fields with pre-existing non-null-valued field.
	Override *bool `pulumi:"override"`
	// Identifier for the processor.
	Tag *string `pulumi:"tag"`
	// The value to be set for the field. Supports template snippets. May specify only one of `value` or `copyFrom`.
	Value *string `pulumi:"value"`
}

// A collection of values returned by ElasticsearchIngestProcessorSet.
type ElasticsearchIngestProcessorSetResult struct {
	// The origin field which will be copied to `field`, cannot set `value` simultaneously.
	CopyFrom *string `pulumi:"copyFrom"`
	// Description of the processor.
	Description *string `pulumi:"description"`
	// The field to insert, upsert, or update.
	Field string `pulumi:"field"`
	// Internal identifier of the resource.
	Id string `pulumi:"id"`
	// Conditionally execute the processor
	If *string `pulumi:"if"`
	// If `true` and `value` is a template snippet that evaluates to `null` or the empty string, the processor quietly exits without modifying the document
	IgnoreEmptyValue *bool `pulumi:"ignoreEmptyValue"`
	// Ignore failures for the processor.
	IgnoreFailure *bool `pulumi:"ignoreFailure"`
	// JSON representation of this data source.
	Json string `pulumi:"json"`
	// The media type for encoding value.
	MediaType *string `pulumi:"mediaType"`
	// Handle failures for the processor.
	OnFailures []string `pulumi:"onFailures"`
	// If processor will update fields with pre-existing non-null-valued field.
	Override *bool `pulumi:"override"`
	// Identifier for the processor.
	Tag *string `pulumi:"tag"`
	// The value to be set for the field. Supports template snippets. May specify only one of `value` or `copyFrom`.
	Value *string `pulumi:"value"`
}

func ElasticsearchIngestProcessorSetOutput(ctx *pulumi.Context, args ElasticsearchIngestProcessorSetOutputArgs, opts ...pulumi.InvokeOption) ElasticsearchIngestProcessorSetResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (ElasticsearchIngestProcessorSetResult, error) {
			args := v.(ElasticsearchIngestProcessorSetArgs)
			r, err := ElasticsearchIngestProcessorSet(ctx, &args, opts...)
			return *r, err
		}).(ElasticsearchIngestProcessorSetResultOutput)
}

// A collection of arguments for invoking ElasticsearchIngestProcessorSet.
type ElasticsearchIngestProcessorSetOutputArgs struct {
	// The origin field which will be copied to `field`, cannot set `value` simultaneously.
	CopyFrom pulumi.StringPtrInput `pulumi:"copyFrom"`
	// Description of the processor.
	Description pulumi.StringPtrInput `pulumi:"description"`
	// The field to insert, upsert, or update.
	Field pulumi.StringInput `pulumi:"field"`
	// Conditionally execute the processor
	If pulumi.StringPtrInput `pulumi:"if"`
	// If `true` and `value` is a template snippet that evaluates to `null` or the empty string, the processor quietly exits without modifying the document
	IgnoreEmptyValue pulumi.BoolPtrInput `pulumi:"ignoreEmptyValue"`
	// Ignore failures for the processor.
	IgnoreFailure pulumi.BoolPtrInput `pulumi:"ignoreFailure"`
	// The media type for encoding value.
	MediaType pulumi.StringPtrInput `pulumi:"mediaType"`
	// Handle failures for the processor.
	OnFailures pulumi.StringArrayInput `pulumi:"onFailures"`
	// If processor will update fields with pre-existing non-null-valued field.
	Override pulumi.BoolPtrInput `pulumi:"override"`
	// Identifier for the processor.
	Tag pulumi.StringPtrInput `pulumi:"tag"`
	// The value to be set for the field. Supports template snippets. May specify only one of `value` or `copyFrom`.
	Value pulumi.StringPtrInput `pulumi:"value"`
}

func (ElasticsearchIngestProcessorSetOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ElasticsearchIngestProcessorSetArgs)(nil)).Elem()
}

// A collection of values returned by ElasticsearchIngestProcessorSet.
type ElasticsearchIngestProcessorSetResultOutput struct{ *pulumi.OutputState }

func (ElasticsearchIngestProcessorSetResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ElasticsearchIngestProcessorSetResult)(nil)).Elem()
}

func (o ElasticsearchIngestProcessorSetResultOutput) ToElasticsearchIngestProcessorSetResultOutput() ElasticsearchIngestProcessorSetResultOutput {
	return o
}

func (o ElasticsearchIngestProcessorSetResultOutput) ToElasticsearchIngestProcessorSetResultOutputWithContext(ctx context.Context) ElasticsearchIngestProcessorSetResultOutput {
	return o
}

// The origin field which will be copied to `field`, cannot set `value` simultaneously.
func (o ElasticsearchIngestProcessorSetResultOutput) CopyFrom() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorSetResult) *string { return v.CopyFrom }).(pulumi.StringPtrOutput)
}

// Description of the processor.
func (o ElasticsearchIngestProcessorSetResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorSetResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// The field to insert, upsert, or update.
func (o ElasticsearchIngestProcessorSetResultOutput) Field() pulumi.StringOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorSetResult) string { return v.Field }).(pulumi.StringOutput)
}

// Internal identifier of the resource.
func (o ElasticsearchIngestProcessorSetResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorSetResult) string { return v.Id }).(pulumi.StringOutput)
}

// Conditionally execute the processor
func (o ElasticsearchIngestProcessorSetResultOutput) If() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorSetResult) *string { return v.If }).(pulumi.StringPtrOutput)
}

// If `true` and `value` is a template snippet that evaluates to `null` or the empty string, the processor quietly exits without modifying the document
func (o ElasticsearchIngestProcessorSetResultOutput) IgnoreEmptyValue() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorSetResult) *bool { return v.IgnoreEmptyValue }).(pulumi.BoolPtrOutput)
}

// Ignore failures for the processor.
func (o ElasticsearchIngestProcessorSetResultOutput) IgnoreFailure() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorSetResult) *bool { return v.IgnoreFailure }).(pulumi.BoolPtrOutput)
}

// JSON representation of this data source.
func (o ElasticsearchIngestProcessorSetResultOutput) Json() pulumi.StringOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorSetResult) string { return v.Json }).(pulumi.StringOutput)
}

// The media type for encoding value.
func (o ElasticsearchIngestProcessorSetResultOutput) MediaType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorSetResult) *string { return v.MediaType }).(pulumi.StringPtrOutput)
}

// Handle failures for the processor.
func (o ElasticsearchIngestProcessorSetResultOutput) OnFailures() pulumi.StringArrayOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorSetResult) []string { return v.OnFailures }).(pulumi.StringArrayOutput)
}

// If processor will update fields with pre-existing non-null-valued field.
func (o ElasticsearchIngestProcessorSetResultOutput) Override() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorSetResult) *bool { return v.Override }).(pulumi.BoolPtrOutput)
}

// Identifier for the processor.
func (o ElasticsearchIngestProcessorSetResultOutput) Tag() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorSetResult) *string { return v.Tag }).(pulumi.StringPtrOutput)
}

// The value to be set for the field. Supports template snippets. May specify only one of `value` or `copyFrom`.
func (o ElasticsearchIngestProcessorSetResultOutput) Value() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorSetResult) *string { return v.Value }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(ElasticsearchIngestProcessorSetResultOutput{})
}
