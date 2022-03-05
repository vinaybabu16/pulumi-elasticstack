// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * Manages data streams. This resource can create, delete and show the information about the created data stream. See: https://www.elastic.co/guide/en/elasticsearch/reference/current/data-stream-apis.html
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as elasticstack from "@pulumi/elasticstack";
 *
 * // Create an ILM policy for our data stream
 * const myIlm = new elasticstack.ElasticsearchIndexLifecycle("myIlm", {
 *     hot: {
 *         minAge: "1h",
 *         setPriority: {
 *             priority: 10,
 *         },
 *         rollover: {
 *             maxAge: "1d",
 *         },
 *         readonly: {},
 *     },
 *     "delete": {
 *         minAge: "2d",
 *         "delete": {},
 *     },
 * });
 * // First we must have a index template created
 * const myDataStreamTemplate = new elasticstack.ElasticsearchIndexTemplate("myDataStreamTemplate", {
 *     indexPatterns: ["my-stream*"],
 *     template: {
 *         settings: myIlm.name.apply(name => JSON.stringify({
 *             "lifecycle.name": name,
 *         })),
 *     },
 *     dataStream: {},
 * });
 * // and now we can create data stream based on the index template
 * const myDataStream = new elasticstack.ElasticsearchDataStream("myDataStream", {}, {
 *     dependsOn: [myDataStreamTemplate],
 * });
 * ```
 *
 * ## Import
 *
 * ```sh
 *  $ pulumi import elasticstack:index/elasticsearchDataStream:ElasticsearchDataStream my_data_stream <cluster_uuid>/<data_stream_name>
 * ```
 */
export class ElasticsearchDataStream extends pulumi.CustomResource {
    /**
     * Get an existing ElasticsearchDataStream resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ElasticsearchDataStreamState, opts?: pulumi.CustomResourceOptions): ElasticsearchDataStream {
        return new ElasticsearchDataStream(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'elasticstack:index/elasticsearchDataStream:ElasticsearchDataStream';

    /**
     * Returns true if the given object is an instance of ElasticsearchDataStream.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ElasticsearchDataStream {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ElasticsearchDataStream.__pulumiType;
    }

    /**
     * Used to establish connection to Elasticsearch server. Overrides environment variables if present.
     */
    public readonly elasticsearchConnection!: pulumi.Output<outputs.ElasticsearchDataStreamElasticsearchConnection | undefined>;
    /**
     * Current generation for the data stream.
     */
    public /*out*/ readonly generation!: pulumi.Output<number>;
    /**
     * If `true`, the data stream is hidden.
     */
    public /*out*/ readonly hidden!: pulumi.Output<boolean>;
    /**
     * Internal identifier of the resource
     */
    public /*out*/ readonly id!: pulumi.Output<string>;
    /**
     * Name of the current ILM lifecycle policy in the stream’s matching index template.
     */
    public /*out*/ readonly ilmPolicy!: pulumi.Output<string>;
    /**
     * Array of objects containing information about the data stream’s backing indices. The last item in this array contains information about the stream’s current write index.
     */
    public /*out*/ readonly indices!: pulumi.Output<outputs.ElasticsearchDataStreamIndex[]>;
    /**
     * Custom metadata for the stream, copied from the _meta object of the stream’s matching index template.
     */
    public /*out*/ readonly metadata!: pulumi.Output<string>;
    /**
     * Name of the data stream to create.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * If `true`, the data stream is created and managed by cross-cluster replication and the local cluster can not write into this data stream or change its mappings.
     */
    public /*out*/ readonly replicated!: pulumi.Output<boolean>;
    /**
     * Health status of the data stream.
     */
    public /*out*/ readonly status!: pulumi.Output<string>;
    /**
     * If `true`, the data stream is created and managed by an Elastic stack component and cannot be modified through normal user interaction.
     */
    public /*out*/ readonly system!: pulumi.Output<boolean>;
    /**
     * Name of the index template used to create the data stream’s backing indices.
     */
    public /*out*/ readonly template!: pulumi.Output<string>;
    /**
     * Contains information about the data stream’s @timestamp field.
     */
    public /*out*/ readonly timestampField!: pulumi.Output<string>;

    /**
     * Create a ElasticsearchDataStream resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ElasticsearchDataStreamArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ElasticsearchDataStreamArgs | ElasticsearchDataStreamState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ElasticsearchDataStreamState | undefined;
            resourceInputs["elasticsearchConnection"] = state ? state.elasticsearchConnection : undefined;
            resourceInputs["generation"] = state ? state.generation : undefined;
            resourceInputs["hidden"] = state ? state.hidden : undefined;
            resourceInputs["id"] = state ? state.id : undefined;
            resourceInputs["ilmPolicy"] = state ? state.ilmPolicy : undefined;
            resourceInputs["indices"] = state ? state.indices : undefined;
            resourceInputs["metadata"] = state ? state.metadata : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["replicated"] = state ? state.replicated : undefined;
            resourceInputs["status"] = state ? state.status : undefined;
            resourceInputs["system"] = state ? state.system : undefined;
            resourceInputs["template"] = state ? state.template : undefined;
            resourceInputs["timestampField"] = state ? state.timestampField : undefined;
        } else {
            const args = argsOrState as ElasticsearchDataStreamArgs | undefined;
            resourceInputs["elasticsearchConnection"] = args ? args.elasticsearchConnection : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["generation"] = undefined /*out*/;
            resourceInputs["hidden"] = undefined /*out*/;
            resourceInputs["id"] = undefined /*out*/;
            resourceInputs["ilmPolicy"] = undefined /*out*/;
            resourceInputs["indices"] = undefined /*out*/;
            resourceInputs["metadata"] = undefined /*out*/;
            resourceInputs["replicated"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["system"] = undefined /*out*/;
            resourceInputs["template"] = undefined /*out*/;
            resourceInputs["timestampField"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ElasticsearchDataStream.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ElasticsearchDataStream resources.
 */
export interface ElasticsearchDataStreamState {
    /**
     * Used to establish connection to Elasticsearch server. Overrides environment variables if present.
     */
    elasticsearchConnection?: pulumi.Input<inputs.ElasticsearchDataStreamElasticsearchConnection>;
    /**
     * Current generation for the data stream.
     */
    generation?: pulumi.Input<number>;
    /**
     * If `true`, the data stream is hidden.
     */
    hidden?: pulumi.Input<boolean>;
    /**
     * Internal identifier of the resource
     */
    id?: pulumi.Input<string>;
    /**
     * Name of the current ILM lifecycle policy in the stream’s matching index template.
     */
    ilmPolicy?: pulumi.Input<string>;
    /**
     * Array of objects containing information about the data stream’s backing indices. The last item in this array contains information about the stream’s current write index.
     */
    indices?: pulumi.Input<pulumi.Input<inputs.ElasticsearchDataStreamIndex>[]>;
    /**
     * Custom metadata for the stream, copied from the _meta object of the stream’s matching index template.
     */
    metadata?: pulumi.Input<string>;
    /**
     * Name of the data stream to create.
     */
    name?: pulumi.Input<string>;
    /**
     * If `true`, the data stream is created and managed by cross-cluster replication and the local cluster can not write into this data stream or change its mappings.
     */
    replicated?: pulumi.Input<boolean>;
    /**
     * Health status of the data stream.
     */
    status?: pulumi.Input<string>;
    /**
     * If `true`, the data stream is created and managed by an Elastic stack component and cannot be modified through normal user interaction.
     */
    system?: pulumi.Input<boolean>;
    /**
     * Name of the index template used to create the data stream’s backing indices.
     */
    template?: pulumi.Input<string>;
    /**
     * Contains information about the data stream’s @timestamp field.
     */
    timestampField?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ElasticsearchDataStream resource.
 */
export interface ElasticsearchDataStreamArgs {
    /**
     * Used to establish connection to Elasticsearch server. Overrides environment variables if present.
     */
    elasticsearchConnection?: pulumi.Input<inputs.ElasticsearchDataStreamElasticsearchConnection>;
    /**
     * Name of the data stream to create.
     */
    name?: pulumi.Input<string>;
}
