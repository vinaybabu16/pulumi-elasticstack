// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package elasticstack

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Trims whitespace from field. If the field is an array of strings, all members of the array will be trimmed.
//
// **NOTE:** This only works on leading and trailing whitespace.
//
// See: https://www.elastic.co/guide/en/elasticsearch/reference/current/trim-processor.html
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
// 		trim, err := elasticstack.ElasticsearchIngestProcessorTrim(ctx, &ElasticsearchIngestProcessorTrimArgs{
// 			Field: "foo",
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = elasticstack.NewElasticsearchIngestPipeline(ctx, "myIngestPipeline", &elasticstack.ElasticsearchIngestPipelineArgs{
// 			Processors: pulumi.StringArray{
// 				pulumi.String(trim.Json),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func ElasticsearchIngestProcessorTrim(ctx *pulumi.Context, args *ElasticsearchIngestProcessorTrimArgs, opts ...pulumi.InvokeOption) (*ElasticsearchIngestProcessorTrimResult, error) {
	var rv ElasticsearchIngestProcessorTrimResult
	err := ctx.Invoke("elasticstack:index/elasticsearchIngestProcessorTrim:ElasticsearchIngestProcessorTrim", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking ElasticsearchIngestProcessorTrim.
type ElasticsearchIngestProcessorTrimArgs struct {
	// Description of the processor.
	Description *string `pulumi:"description"`
	// The string-valued field to trim whitespace from.
	Field string `pulumi:"field"`
	// Conditionally execute the processor
	If *string `pulumi:"if"`
	// Ignore failures for the processor.
	IgnoreFailure *bool `pulumi:"ignoreFailure"`
	// If `true` and `field` does not exist or is `null`, the processor quietly exits without modifying the document.
	IgnoreMissing *bool `pulumi:"ignoreMissing"`
	// Handle failures for the processor.
	OnFailures []string `pulumi:"onFailures"`
	// Identifier for the processor.
	Tag *string `pulumi:"tag"`
	// The field to assign the trimmed value to, by default `field` is updated in-place.
	TargetField *string `pulumi:"targetField"`
}

// A collection of values returned by ElasticsearchIngestProcessorTrim.
type ElasticsearchIngestProcessorTrimResult struct {
	// Description of the processor.
	Description *string `pulumi:"description"`
	// The string-valued field to trim whitespace from.
	Field string `pulumi:"field"`
	// Internal identifier of the resource.
	Id string `pulumi:"id"`
	// Conditionally execute the processor
	If *string `pulumi:"if"`
	// Ignore failures for the processor.
	IgnoreFailure *bool `pulumi:"ignoreFailure"`
	// If `true` and `field` does not exist or is `null`, the processor quietly exits without modifying the document.
	IgnoreMissing *bool `pulumi:"ignoreMissing"`
	// JSON representation of this data source.
	Json string `pulumi:"json"`
	// Handle failures for the processor.
	OnFailures []string `pulumi:"onFailures"`
	// Identifier for the processor.
	Tag *string `pulumi:"tag"`
	// The field to assign the trimmed value to, by default `field` is updated in-place.
	TargetField *string `pulumi:"targetField"`
}

func ElasticsearchIngestProcessorTrimOutput(ctx *pulumi.Context, args ElasticsearchIngestProcessorTrimOutputArgs, opts ...pulumi.InvokeOption) ElasticsearchIngestProcessorTrimResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (ElasticsearchIngestProcessorTrimResult, error) {
			args := v.(ElasticsearchIngestProcessorTrimArgs)
			r, err := ElasticsearchIngestProcessorTrim(ctx, &args, opts...)
			return *r, err
		}).(ElasticsearchIngestProcessorTrimResultOutput)
}

// A collection of arguments for invoking ElasticsearchIngestProcessorTrim.
type ElasticsearchIngestProcessorTrimOutputArgs struct {
	// Description of the processor.
	Description pulumi.StringPtrInput `pulumi:"description"`
	// The string-valued field to trim whitespace from.
	Field pulumi.StringInput `pulumi:"field"`
	// Conditionally execute the processor
	If pulumi.StringPtrInput `pulumi:"if"`
	// Ignore failures for the processor.
	IgnoreFailure pulumi.BoolPtrInput `pulumi:"ignoreFailure"`
	// If `true` and `field` does not exist or is `null`, the processor quietly exits without modifying the document.
	IgnoreMissing pulumi.BoolPtrInput `pulumi:"ignoreMissing"`
	// Handle failures for the processor.
	OnFailures pulumi.StringArrayInput `pulumi:"onFailures"`
	// Identifier for the processor.
	Tag pulumi.StringPtrInput `pulumi:"tag"`
	// The field to assign the trimmed value to, by default `field` is updated in-place.
	TargetField pulumi.StringPtrInput `pulumi:"targetField"`
}

func (ElasticsearchIngestProcessorTrimOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ElasticsearchIngestProcessorTrimArgs)(nil)).Elem()
}

// A collection of values returned by ElasticsearchIngestProcessorTrim.
type ElasticsearchIngestProcessorTrimResultOutput struct{ *pulumi.OutputState }

func (ElasticsearchIngestProcessorTrimResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ElasticsearchIngestProcessorTrimResult)(nil)).Elem()
}

func (o ElasticsearchIngestProcessorTrimResultOutput) ToElasticsearchIngestProcessorTrimResultOutput() ElasticsearchIngestProcessorTrimResultOutput {
	return o
}

func (o ElasticsearchIngestProcessorTrimResultOutput) ToElasticsearchIngestProcessorTrimResultOutputWithContext(ctx context.Context) ElasticsearchIngestProcessorTrimResultOutput {
	return o
}

// Description of the processor.
func (o ElasticsearchIngestProcessorTrimResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorTrimResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// The string-valued field to trim whitespace from.
func (o ElasticsearchIngestProcessorTrimResultOutput) Field() pulumi.StringOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorTrimResult) string { return v.Field }).(pulumi.StringOutput)
}

// Internal identifier of the resource.
func (o ElasticsearchIngestProcessorTrimResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorTrimResult) string { return v.Id }).(pulumi.StringOutput)
}

// Conditionally execute the processor
func (o ElasticsearchIngestProcessorTrimResultOutput) If() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorTrimResult) *string { return v.If }).(pulumi.StringPtrOutput)
}

// Ignore failures for the processor.
func (o ElasticsearchIngestProcessorTrimResultOutput) IgnoreFailure() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorTrimResult) *bool { return v.IgnoreFailure }).(pulumi.BoolPtrOutput)
}

// If `true` and `field` does not exist or is `null`, the processor quietly exits without modifying the document.
func (o ElasticsearchIngestProcessorTrimResultOutput) IgnoreMissing() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorTrimResult) *bool { return v.IgnoreMissing }).(pulumi.BoolPtrOutput)
}

// JSON representation of this data source.
func (o ElasticsearchIngestProcessorTrimResultOutput) Json() pulumi.StringOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorTrimResult) string { return v.Json }).(pulumi.StringOutput)
}

// Handle failures for the processor.
func (o ElasticsearchIngestProcessorTrimResultOutput) OnFailures() pulumi.StringArrayOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorTrimResult) []string { return v.OnFailures }).(pulumi.StringArrayOutput)
}

// Identifier for the processor.
func (o ElasticsearchIngestProcessorTrimResultOutput) Tag() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorTrimResult) *string { return v.Tag }).(pulumi.StringPtrOutput)
}

// The field to assign the trimmed value to, by default `field` is updated in-place.
func (o ElasticsearchIngestProcessorTrimResultOutput) TargetField() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorTrimResult) *string { return v.TargetField }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(ElasticsearchIngestProcessorTrimResultOutput{})
}
