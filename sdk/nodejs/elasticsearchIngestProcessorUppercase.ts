// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Converts a string to its uppercase equivalent. If the field is an array of strings, all members of the array will be converted.
 *
 * See: https://www.elastic.co/guide/en/elasticsearch/reference/current/uppercase-processor.html
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as elasticstack from "@pulumi/elasticstack";
 *
 * const uppercase = elasticstack.ElasticsearchIngestProcessorUppercase({
 *     field: "foo",
 * });
 * const myIngestPipeline = new elasticstack.ElasticsearchIngestPipeline("myIngestPipeline", {processors: [uppercase.then(uppercase => uppercase.json)]});
 * ```
 */
export function elasticsearchIngestProcessorUppercase(args: ElasticsearchIngestProcessorUppercaseArgs, opts?: pulumi.InvokeOptions): Promise<ElasticsearchIngestProcessorUppercaseResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("elasticstack:index/elasticsearchIngestProcessorUppercase:ElasticsearchIngestProcessorUppercase", {
        "description": args.description,
        "field": args.field,
        "if": args.if,
        "ignoreFailure": args.ignoreFailure,
        "ignoreMissing": args.ignoreMissing,
        "onFailures": args.onFailures,
        "tag": args.tag,
        "targetField": args.targetField,
    }, opts);
}

/**
 * A collection of arguments for invoking ElasticsearchIngestProcessorUppercase.
 */
export interface ElasticsearchIngestProcessorUppercaseArgs {
    /**
     * Description of the processor.
     */
    description?: string;
    /**
     * The field to make uppercase.
     */
    field: string;
    /**
     * Conditionally execute the processor
     */
    if?: string;
    /**
     * Ignore failures for the processor.
     */
    ignoreFailure?: boolean;
    /**
     * If `true` and `field` does not exist or is `null`, the processor quietly exits without modifying the document.
     */
    ignoreMissing?: boolean;
    /**
     * Handle failures for the processor.
     */
    onFailures?: string[];
    /**
     * Identifier for the processor.
     */
    tag?: string;
    /**
     * The field to assign the converted value to, by default `field` is updated in-place.
     */
    targetField?: string;
}

/**
 * A collection of values returned by ElasticsearchIngestProcessorUppercase.
 */
export interface ElasticsearchIngestProcessorUppercaseResult {
    /**
     * Description of the processor.
     */
    readonly description?: string;
    /**
     * The field to make uppercase.
     */
    readonly field: string;
    /**
     * Internal identifier of the resource.
     */
    readonly id: string;
    /**
     * Conditionally execute the processor
     */
    readonly if?: string;
    /**
     * Ignore failures for the processor.
     */
    readonly ignoreFailure?: boolean;
    /**
     * If `true` and `field` does not exist or is `null`, the processor quietly exits without modifying the document.
     */
    readonly ignoreMissing?: boolean;
    /**
     * JSON representation of this data source.
     */
    readonly json: string;
    /**
     * Handle failures for the processor.
     */
    readonly onFailures?: string[];
    /**
     * Identifier for the processor.
     */
    readonly tag?: string;
    /**
     * The field to assign the converted value to, by default `field` is updated in-place.
     */
    readonly targetField?: string;
}

export function elasticsearchIngestProcessorUppercaseOutput(args: ElasticsearchIngestProcessorUppercaseOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<ElasticsearchIngestProcessorUppercaseResult> {
    return pulumi.output(args).apply(a => elasticsearchIngestProcessorUppercase(a, opts))
}

/**
 * A collection of arguments for invoking ElasticsearchIngestProcessorUppercase.
 */
export interface ElasticsearchIngestProcessorUppercaseOutputArgs {
    /**
     * Description of the processor.
     */
    description?: pulumi.Input<string>;
    /**
     * The field to make uppercase.
     */
    field: pulumi.Input<string>;
    /**
     * Conditionally execute the processor
     */
    if?: pulumi.Input<string>;
    /**
     * Ignore failures for the processor.
     */
    ignoreFailure?: pulumi.Input<boolean>;
    /**
     * If `true` and `field` does not exist or is `null`, the processor quietly exits without modifying the document.
     */
    ignoreMissing?: pulumi.Input<boolean>;
    /**
     * Handle failures for the processor.
     */
    onFailures?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Identifier for the processor.
     */
    tag?: pulumi.Input<string>;
    /**
     * The field to assign the converted value to, by default `field` is updated in-place.
     */
    targetField?: pulumi.Input<string>;
}
