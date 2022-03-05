// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The enrich processor can enrich documents with data from another index. See enrich data section for more information about how to set this up.
 *
 * See: https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest-enriching-data.html and https://www.elastic.co/guide/en/elasticsearch/reference/current/enrich-processor.html
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as elasticstack from "@pulumi/elasticstack";
 *
 * const enrich = elasticstack.ElasticsearchIngestProcessorEnrich({
 *     policyName: "users-policy",
 *     field: "email",
 *     targetField: "user",
 *     maxMatches: 1,
 * });
 * const myIngestPipeline = new elasticstack.ElasticsearchIngestPipeline("myIngestPipeline", {processors: [enrich.then(enrich => enrich.json)]});
 * ```
 */
export function elasticsearchIngestProcessorEnrich(args: ElasticsearchIngestProcessorEnrichArgs, opts?: pulumi.InvokeOptions): Promise<ElasticsearchIngestProcessorEnrichResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("elasticstack:index/elasticsearchIngestProcessorEnrich:ElasticsearchIngestProcessorEnrich", {
        "description": args.description,
        "field": args.field,
        "if": args.if,
        "ignoreFailure": args.ignoreFailure,
        "ignoreMissing": args.ignoreMissing,
        "maxMatches": args.maxMatches,
        "onFailures": args.onFailures,
        "override": args.override,
        "policyName": args.policyName,
        "shapeRelation": args.shapeRelation,
        "tag": args.tag,
        "targetField": args.targetField,
    }, opts);
}

/**
 * A collection of arguments for invoking ElasticsearchIngestProcessorEnrich.
 */
export interface ElasticsearchIngestProcessorEnrichArgs {
    /**
     * Description of the processor.
     */
    description?: string;
    /**
     * The field in the input document that matches the policies matchField used to retrieve the enrichment data.
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
     * The maximum number of matched documents to include under the configured target field.
     */
    maxMatches?: number;
    /**
     * Handle failures for the processor.
     */
    onFailures?: string[];
    /**
     * If processor will update fields with pre-existing non-null-valued field.
     */
    override?: boolean;
    /**
     * The name of the enrich policy to use.
     */
    policyName: string;
    /**
     * A spatial relation operator used to match the geoshape of incoming documents to documents in the enrich index.
     */
    shapeRelation?: string;
    /**
     * Identifier for the processor.
     */
    tag?: string;
    /**
     * Field added to incoming documents to contain enrich data.
     */
    targetField: string;
}

/**
 * A collection of values returned by ElasticsearchIngestProcessorEnrich.
 */
export interface ElasticsearchIngestProcessorEnrichResult {
    /**
     * Description of the processor.
     */
    readonly description?: string;
    /**
     * The field in the input document that matches the policies matchField used to retrieve the enrichment data.
     */
    readonly field: string;
    /**
     * Internal identifier of the resource
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
     * The maximum number of matched documents to include under the configured target field.
     */
    readonly maxMatches?: number;
    /**
     * Handle failures for the processor.
     */
    readonly onFailures?: string[];
    /**
     * If processor will update fields with pre-existing non-null-valued field.
     */
    readonly override?: boolean;
    /**
     * The name of the enrich policy to use.
     */
    readonly policyName: string;
    /**
     * A spatial relation operator used to match the geoshape of incoming documents to documents in the enrich index.
     */
    readonly shapeRelation?: string;
    /**
     * Identifier for the processor.
     */
    readonly tag?: string;
    /**
     * Field added to incoming documents to contain enrich data.
     */
    readonly targetField: string;
}

export function elasticsearchIngestProcessorEnrichOutput(args: ElasticsearchIngestProcessorEnrichOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<ElasticsearchIngestProcessorEnrichResult> {
    return pulumi.output(args).apply(a => elasticsearchIngestProcessorEnrich(a, opts))
}

/**
 * A collection of arguments for invoking ElasticsearchIngestProcessorEnrich.
 */
export interface ElasticsearchIngestProcessorEnrichOutputArgs {
    /**
     * Description of the processor.
     */
    description?: pulumi.Input<string>;
    /**
     * The field in the input document that matches the policies matchField used to retrieve the enrichment data.
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
     * The maximum number of matched documents to include under the configured target field.
     */
    maxMatches?: pulumi.Input<number>;
    /**
     * Handle failures for the processor.
     */
    onFailures?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * If processor will update fields with pre-existing non-null-valued field.
     */
    override?: pulumi.Input<boolean>;
    /**
     * The name of the enrich policy to use.
     */
    policyName: pulumi.Input<string>;
    /**
     * A spatial relation operator used to match the geoshape of incoming documents to documents in the enrich index.
     */
    shapeRelation?: pulumi.Input<string>;
    /**
     * Identifier for the processor.
     */
    tag?: pulumi.Input<string>;
    /**
     * Field added to incoming documents to contain enrich data.
     */
    targetField: pulumi.Input<string>;
}
