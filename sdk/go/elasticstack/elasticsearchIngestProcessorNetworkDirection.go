// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package elasticstack

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Calculates the network direction given a source IP address, destination IP address, and a list of internal networks.
//
// The network direction processor reads IP addresses from Elastic Common Schema (ECS) fields by default. If you use the ECS, only the `internalNetworks` option must be specified.
//
// One of either `internalNetworks` or `internalNetworksField` must be specified. If `internalNetworksField` is specified, it follows the behavior specified by `ignoreMissing`.
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
// 		networkDirection, err := elasticstack.ElasticsearchIngestProcessorNetworkDirection(ctx, &ElasticsearchIngestProcessorNetworkDirectionArgs{
// 			InternalNetworks: []string{
// 				"private",
// 			},
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = elasticstack.NewElasticsearchIngestPipeline(ctx, "myIngestPipeline", &elasticstack.ElasticsearchIngestPipelineArgs{
// 			Processors: pulumi.StringArray{
// 				pulumi.String(networkDirection.Json),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func ElasticsearchIngestProcessorNetworkDirection(ctx *pulumi.Context, args *ElasticsearchIngestProcessorNetworkDirectionArgs, opts ...pulumi.InvokeOption) (*ElasticsearchIngestProcessorNetworkDirectionResult, error) {
	var rv ElasticsearchIngestProcessorNetworkDirectionResult
	err := ctx.Invoke("elasticstack:index/elasticsearchIngestProcessorNetworkDirection:ElasticsearchIngestProcessorNetworkDirection", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking ElasticsearchIngestProcessorNetworkDirection.
type ElasticsearchIngestProcessorNetworkDirectionArgs struct {
	// Description of the processor.
	Description *string `pulumi:"description"`
	// Field containing the destination IP address.
	DestinationIp *string `pulumi:"destinationIp"`
	// Conditionally execute the processor
	If *string `pulumi:"if"`
	// Ignore failures for the processor.
	IgnoreFailure *bool `pulumi:"ignoreFailure"`
	// If `true` and `field` does not exist or is `null`, the processor quietly exits without modifying the document.
	IgnoreMissing *bool `pulumi:"ignoreMissing"`
	// List of internal networks.
	InternalNetworks []string `pulumi:"internalNetworks"`
	// A field on the given document to read the internalNetworks configuration from.
	InternalNetworksField *string `pulumi:"internalNetworksField"`
	// Handle failures for the processor.
	OnFailures []string `pulumi:"onFailures"`
	// Field containing the source IP address.
	SourceIp *string `pulumi:"sourceIp"`
	// Identifier for the processor.
	Tag *string `pulumi:"tag"`
	// Output field for the network direction.
	TargetField *string `pulumi:"targetField"`
}

// A collection of values returned by ElasticsearchIngestProcessorNetworkDirection.
type ElasticsearchIngestProcessorNetworkDirectionResult struct {
	// Description of the processor.
	Description *string `pulumi:"description"`
	// Field containing the destination IP address.
	DestinationIp *string `pulumi:"destinationIp"`
	// Internal identifier of the resource.
	Id string `pulumi:"id"`
	// Conditionally execute the processor
	If *string `pulumi:"if"`
	// Ignore failures for the processor.
	IgnoreFailure *bool `pulumi:"ignoreFailure"`
	// If `true` and `field` does not exist or is `null`, the processor quietly exits without modifying the document.
	IgnoreMissing *bool `pulumi:"ignoreMissing"`
	// List of internal networks.
	InternalNetworks []string `pulumi:"internalNetworks"`
	// A field on the given document to read the internalNetworks configuration from.
	InternalNetworksField *string `pulumi:"internalNetworksField"`
	// JSON representation of this data source.
	Json string `pulumi:"json"`
	// Handle failures for the processor.
	OnFailures []string `pulumi:"onFailures"`
	// Field containing the source IP address.
	SourceIp *string `pulumi:"sourceIp"`
	// Identifier for the processor.
	Tag *string `pulumi:"tag"`
	// Output field for the network direction.
	TargetField *string `pulumi:"targetField"`
}

func ElasticsearchIngestProcessorNetworkDirectionOutput(ctx *pulumi.Context, args ElasticsearchIngestProcessorNetworkDirectionOutputArgs, opts ...pulumi.InvokeOption) ElasticsearchIngestProcessorNetworkDirectionResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (ElasticsearchIngestProcessorNetworkDirectionResult, error) {
			args := v.(ElasticsearchIngestProcessorNetworkDirectionArgs)
			r, err := ElasticsearchIngestProcessorNetworkDirection(ctx, &args, opts...)
			return *r, err
		}).(ElasticsearchIngestProcessorNetworkDirectionResultOutput)
}

// A collection of arguments for invoking ElasticsearchIngestProcessorNetworkDirection.
type ElasticsearchIngestProcessorNetworkDirectionOutputArgs struct {
	// Description of the processor.
	Description pulumi.StringPtrInput `pulumi:"description"`
	// Field containing the destination IP address.
	DestinationIp pulumi.StringPtrInput `pulumi:"destinationIp"`
	// Conditionally execute the processor
	If pulumi.StringPtrInput `pulumi:"if"`
	// Ignore failures for the processor.
	IgnoreFailure pulumi.BoolPtrInput `pulumi:"ignoreFailure"`
	// If `true` and `field` does not exist or is `null`, the processor quietly exits without modifying the document.
	IgnoreMissing pulumi.BoolPtrInput `pulumi:"ignoreMissing"`
	// List of internal networks.
	InternalNetworks pulumi.StringArrayInput `pulumi:"internalNetworks"`
	// A field on the given document to read the internalNetworks configuration from.
	InternalNetworksField pulumi.StringPtrInput `pulumi:"internalNetworksField"`
	// Handle failures for the processor.
	OnFailures pulumi.StringArrayInput `pulumi:"onFailures"`
	// Field containing the source IP address.
	SourceIp pulumi.StringPtrInput `pulumi:"sourceIp"`
	// Identifier for the processor.
	Tag pulumi.StringPtrInput `pulumi:"tag"`
	// Output field for the network direction.
	TargetField pulumi.StringPtrInput `pulumi:"targetField"`
}

func (ElasticsearchIngestProcessorNetworkDirectionOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ElasticsearchIngestProcessorNetworkDirectionArgs)(nil)).Elem()
}

// A collection of values returned by ElasticsearchIngestProcessorNetworkDirection.
type ElasticsearchIngestProcessorNetworkDirectionResultOutput struct{ *pulumi.OutputState }

func (ElasticsearchIngestProcessorNetworkDirectionResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ElasticsearchIngestProcessorNetworkDirectionResult)(nil)).Elem()
}

func (o ElasticsearchIngestProcessorNetworkDirectionResultOutput) ToElasticsearchIngestProcessorNetworkDirectionResultOutput() ElasticsearchIngestProcessorNetworkDirectionResultOutput {
	return o
}

func (o ElasticsearchIngestProcessorNetworkDirectionResultOutput) ToElasticsearchIngestProcessorNetworkDirectionResultOutputWithContext(ctx context.Context) ElasticsearchIngestProcessorNetworkDirectionResultOutput {
	return o
}

// Description of the processor.
func (o ElasticsearchIngestProcessorNetworkDirectionResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorNetworkDirectionResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// Field containing the destination IP address.
func (o ElasticsearchIngestProcessorNetworkDirectionResultOutput) DestinationIp() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorNetworkDirectionResult) *string { return v.DestinationIp }).(pulumi.StringPtrOutput)
}

// Internal identifier of the resource.
func (o ElasticsearchIngestProcessorNetworkDirectionResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorNetworkDirectionResult) string { return v.Id }).(pulumi.StringOutput)
}

// Conditionally execute the processor
func (o ElasticsearchIngestProcessorNetworkDirectionResultOutput) If() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorNetworkDirectionResult) *string { return v.If }).(pulumi.StringPtrOutput)
}

// Ignore failures for the processor.
func (o ElasticsearchIngestProcessorNetworkDirectionResultOutput) IgnoreFailure() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorNetworkDirectionResult) *bool { return v.IgnoreFailure }).(pulumi.BoolPtrOutput)
}

// If `true` and `field` does not exist or is `null`, the processor quietly exits without modifying the document.
func (o ElasticsearchIngestProcessorNetworkDirectionResultOutput) IgnoreMissing() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorNetworkDirectionResult) *bool { return v.IgnoreMissing }).(pulumi.BoolPtrOutput)
}

// List of internal networks.
func (o ElasticsearchIngestProcessorNetworkDirectionResultOutput) InternalNetworks() pulumi.StringArrayOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorNetworkDirectionResult) []string { return v.InternalNetworks }).(pulumi.StringArrayOutput)
}

// A field on the given document to read the internalNetworks configuration from.
func (o ElasticsearchIngestProcessorNetworkDirectionResultOutput) InternalNetworksField() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorNetworkDirectionResult) *string { return v.InternalNetworksField }).(pulumi.StringPtrOutput)
}

// JSON representation of this data source.
func (o ElasticsearchIngestProcessorNetworkDirectionResultOutput) Json() pulumi.StringOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorNetworkDirectionResult) string { return v.Json }).(pulumi.StringOutput)
}

// Handle failures for the processor.
func (o ElasticsearchIngestProcessorNetworkDirectionResultOutput) OnFailures() pulumi.StringArrayOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorNetworkDirectionResult) []string { return v.OnFailures }).(pulumi.StringArrayOutput)
}

// Field containing the source IP address.
func (o ElasticsearchIngestProcessorNetworkDirectionResultOutput) SourceIp() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorNetworkDirectionResult) *string { return v.SourceIp }).(pulumi.StringPtrOutput)
}

// Identifier for the processor.
func (o ElasticsearchIngestProcessorNetworkDirectionResultOutput) Tag() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorNetworkDirectionResult) *string { return v.Tag }).(pulumi.StringPtrOutput)
}

// Output field for the network direction.
func (o ElasticsearchIngestProcessorNetworkDirectionResultOutput) TargetField() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ElasticsearchIngestProcessorNetworkDirectionResult) *string { return v.TargetField }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(ElasticsearchIngestProcessorNetworkDirectionResultOutput{})
}
