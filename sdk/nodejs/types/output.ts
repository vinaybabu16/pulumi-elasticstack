// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";

export interface ElasticsearchClusterSettingsElasticsearchConnection {
    /**
     * Path to a custom Certificate Authority certificate
     */
    caFile?: string;
    endpoints?: string[];
    /**
     * Disable TLS certificate validation
     */
    insecure?: boolean;
    /**
     * A password to use for API authentication to Elasticsearch.
     */
    password?: string;
    /**
     * A username to use for API authentication to Elasticsearch.
     */
    username?: string;
}

export interface ElasticsearchClusterSettingsPersistent {
    /**
     * Defines the setting in the cluster.
     */
    settings: outputs.ElasticsearchClusterSettingsPersistentSetting[];
}

export interface ElasticsearchClusterSettingsPersistentSetting {
    name: string;
    value?: string;
    valueLists?: string[];
}

export interface ElasticsearchClusterSettingsTransient {
    /**
     * Defines the setting in the cluster.
     */
    settings: outputs.ElasticsearchClusterSettingsTransientSetting[];
}

export interface ElasticsearchClusterSettingsTransientSetting {
    name: string;
    value?: string;
    valueLists?: string[];
}

export interface ElasticsearchComponentTemplateElasticsearchConnection {
    /**
     * Path to a custom Certificate Authority certificate
     */
    caFile?: string;
    endpoints?: string[];
    /**
     * Disable TLS certificate validation
     */
    insecure?: boolean;
    /**
     * A password to use for API authentication to Elasticsearch.
     */
    password?: string;
    /**
     * A username to use for API authentication to Elasticsearch.
     */
    username?: string;
}

export interface ElasticsearchComponentTemplateTemplate {
    /**
     * Alias to add.
     */
    aliases?: outputs.ElasticsearchComponentTemplateTemplateAlias[];
    /**
     * Mapping for fields in the index.
     */
    mappings?: string;
    /**
     * Configuration options for the index. See, https://www.elastic.co/guide/en/elasticsearch/reference/current/index-modules.html#index-modules-settings
     */
    settings?: string;
}

export interface ElasticsearchComponentTemplateTemplateAlias {
    filter?: string;
    indexRouting?: string;
    isHidden?: boolean;
    isWriteIndex?: boolean;
    /**
     * Name of the component template to create.
     */
    name: string;
    routing?: string;
    searchRouting?: string;
}

export interface ElasticsearchDataStreamElasticsearchConnection {
    /**
     * Path to a custom Certificate Authority certificate
     */
    caFile?: string;
    endpoints?: string[];
    /**
     * Disable TLS certificate validation
     */
    insecure?: boolean;
    /**
     * A password to use for API authentication to Elasticsearch.
     */
    password?: string;
    /**
     * A username to use for API authentication to Elasticsearch.
     */
    username?: string;
}

export interface ElasticsearchDataStreamIndex {
    indexName: string;
    indexUuid: string;
}

export interface ElasticsearchIndexAlias {
    /**
     * Query used to limit documents the alias can access.
     */
    filter?: string;
    /**
     * Value used to route indexing operations to a specific shard. If specified, this overwrites the `routing` value for indexing operations.
     */
    indexRouting?: string;
    /**
     * If true, the alias is hidden.
     */
    isHidden?: boolean;
    /**
     * If true, the index is the write index for the alias.
     */
    isWriteIndex?: boolean;
    /**
     * Index alias name.
     */
    name: string;
    /**
     * Value used to route indexing and search operations to a specific shard.
     */
    routing?: string;
    /**
     * Value used to route search operations to a specific shard. If specified, this overwrites the routing value for search operations.
     */
    searchRouting?: string;
}

export interface ElasticsearchIndexElasticsearchConnection {
    /**
     * Path to a custom Certificate Authority certificate
     */
    caFile?: string;
    endpoints?: string[];
    /**
     * Disable TLS certificate validation
     */
    insecure?: boolean;
    /**
     * A password to use for API authentication to Elasticsearch.
     */
    password?: string;
    /**
     * A username to use for API authentication to Elasticsearch.
     */
    username?: string;
}

export interface ElasticsearchIndexLifecycleCold {
    /**
     * Updates the index settings to change which nodes are allowed to host the index shards and change the number of replicas.
     */
    allocate?: outputs.ElasticsearchIndexLifecycleColdAllocate;
    /**
     * Freeze the index to minimize its memory footprint.
     */
    freeze?: outputs.ElasticsearchIndexLifecycleColdFreeze;
    /**
     * Moves the index to the data tier that corresponds to the current phase by updating the "index.routing.allocation.include.*tier*preference" index setting.
     */
    migrate?: outputs.ElasticsearchIndexLifecycleColdMigrate;
    /**
     * ILM moves indices through the lifecycle according to their age. To control the timing of these transitions, you set a minimum age for each phase.
     */
    minAge: string;
    /**
     * Makes the index read-only.
     */
    readonly?: outputs.ElasticsearchIndexLifecycleColdReadonly;
    /**
     * Takes a snapshot of the managed index in the configured repository and mounts it as a searchable snapshot.
     */
    searchableSnapshot?: outputs.ElasticsearchIndexLifecycleColdSearchableSnapshot;
    /**
     * Sets a source index to read-only and shrinks it into a new index with fewer primary shards.
     */
    setPriority?: outputs.ElasticsearchIndexLifecycleColdSetPriority;
    /**
     * Convert a follower index to a regular index. Performed automatically before a rollover, shrink, or searchable snapshot action.
     */
    unfollow?: outputs.ElasticsearchIndexLifecycleColdUnfollow;
}

export interface ElasticsearchIndexLifecycleColdAllocate {
    exclude: string;
    include: string;
    numberOfReplicas?: number;
    require: string;
}

export interface ElasticsearchIndexLifecycleColdFreeze {
    enabled?: boolean;
}

export interface ElasticsearchIndexLifecycleColdMigrate {
    enabled?: boolean;
}

export interface ElasticsearchIndexLifecycleColdReadonly {
    enabled?: boolean;
}

export interface ElasticsearchIndexLifecycleColdSearchableSnapshot {
    forceMergeIndex?: boolean;
    snapshotRepository: string;
}

export interface ElasticsearchIndexLifecycleColdSetPriority {
    priority: number;
}

export interface ElasticsearchIndexLifecycleColdUnfollow {
    enabled?: boolean;
}

export interface ElasticsearchIndexLifecycleDelete {
    /**
     * Permanently removes the index.
     */
    delete?: outputs.ElasticsearchIndexLifecycleDeleteDelete;
    /**
     * ILM moves indices through the lifecycle according to their age. To control the timing of these transitions, you set a minimum age for each phase.
     */
    minAge: string;
    /**
     * Waits for the specified SLM policy to be executed before removing the index. This ensures that a snapshot of the deleted index is available.
     */
    waitForSnapshot?: outputs.ElasticsearchIndexLifecycleDeleteWaitForSnapshot;
}

export interface ElasticsearchIndexLifecycleDeleteDelete {
    deleteSearchableSnapshot?: boolean;
}

export interface ElasticsearchIndexLifecycleDeleteWaitForSnapshot {
    policy: string;
}

export interface ElasticsearchIndexLifecycleElasticsearchConnection {
    /**
     * Path to a custom Certificate Authority certificate
     */
    caFile?: string;
    endpoints?: string[];
    /**
     * Disable TLS certificate validation
     */
    insecure?: boolean;
    /**
     * A password to use for API authentication to Elasticsearch.
     */
    password?: string;
    /**
     * A username to use for API authentication to Elasticsearch.
     */
    username?: string;
}

export interface ElasticsearchIndexLifecycleFrozen {
    /**
     * ILM moves indices through the lifecycle according to their age. To control the timing of these transitions, you set a minimum age for each phase.
     */
    minAge: string;
    /**
     * Takes a snapshot of the managed index in the configured repository and mounts it as a searchable snapshot.
     */
    searchableSnapshot?: outputs.ElasticsearchIndexLifecycleFrozenSearchableSnapshot;
}

export interface ElasticsearchIndexLifecycleFrozenSearchableSnapshot {
    forceMergeIndex?: boolean;
    snapshotRepository: string;
}

export interface ElasticsearchIndexLifecycleHot {
    /**
     * Force merges the index into the specified maximum number of segments. This action makes the index read-only.
     */
    forcemerge?: outputs.ElasticsearchIndexLifecycleHotForcemerge;
    /**
     * ILM moves indices through the lifecycle according to their age. To control the timing of these transitions, you set a minimum age for each phase.
     */
    minAge: string;
    /**
     * Makes the index read-only.
     */
    readonly?: outputs.ElasticsearchIndexLifecycleHotReadonly;
    /**
     * Rolls over a target to a new index when the existing index meets one or more of the rollover conditions.
     */
    rollover?: outputs.ElasticsearchIndexLifecycleHotRollover;
    /**
     * Takes a snapshot of the managed index in the configured repository and mounts it as a searchable snapshot.
     */
    searchableSnapshot?: outputs.ElasticsearchIndexLifecycleHotSearchableSnapshot;
    /**
     * Sets a source index to read-only and shrinks it into a new index with fewer primary shards.
     */
    setPriority?: outputs.ElasticsearchIndexLifecycleHotSetPriority;
    /**
     * Sets a source index to read-only and shrinks it into a new index with fewer primary shards.
     */
    shrink?: outputs.ElasticsearchIndexLifecycleHotShrink;
    /**
     * Convert a follower index to a regular index. Performed automatically before a rollover, shrink, or searchable snapshot action.
     */
    unfollow?: outputs.ElasticsearchIndexLifecycleHotUnfollow;
}

export interface ElasticsearchIndexLifecycleHotForcemerge {
    indexCodec?: string;
    maxNumSegments: number;
}

export interface ElasticsearchIndexLifecycleHotReadonly {
    enabled?: boolean;
}

export interface ElasticsearchIndexLifecycleHotRollover {
    maxAge?: string;
    maxDocs?: number;
    maxPrimaryShardSize?: string;
    maxSize?: string;
}

export interface ElasticsearchIndexLifecycleHotSearchableSnapshot {
    forceMergeIndex?: boolean;
    snapshotRepository: string;
}

export interface ElasticsearchIndexLifecycleHotSetPriority {
    priority: number;
}

export interface ElasticsearchIndexLifecycleHotShrink {
    maxPrimaryShardSize?: string;
    numberOfShards?: number;
}

export interface ElasticsearchIndexLifecycleHotUnfollow {
    enabled?: boolean;
}

export interface ElasticsearchIndexLifecycleWarm {
    /**
     * Updates the index settings to change which nodes are allowed to host the index shards and change the number of replicas.
     */
    allocate?: outputs.ElasticsearchIndexLifecycleWarmAllocate;
    /**
     * Force merges the index into the specified maximum number of segments. This action makes the index read-only.
     */
    forcemerge?: outputs.ElasticsearchIndexLifecycleWarmForcemerge;
    /**
     * Moves the index to the data tier that corresponds to the current phase by updating the "index.routing.allocation.include.*tier*preference" index setting.
     */
    migrate?: outputs.ElasticsearchIndexLifecycleWarmMigrate;
    /**
     * ILM moves indices through the lifecycle according to their age. To control the timing of these transitions, you set a minimum age for each phase.
     */
    minAge: string;
    /**
     * Makes the index read-only.
     */
    readonly?: outputs.ElasticsearchIndexLifecycleWarmReadonly;
    /**
     * Sets a source index to read-only and shrinks it into a new index with fewer primary shards.
     */
    setPriority?: outputs.ElasticsearchIndexLifecycleWarmSetPriority;
    /**
     * Sets a source index to read-only and shrinks it into a new index with fewer primary shards.
     */
    shrink?: outputs.ElasticsearchIndexLifecycleWarmShrink;
    /**
     * Convert a follower index to a regular index. Performed automatically before a rollover, shrink, or searchable snapshot action.
     */
    unfollow?: outputs.ElasticsearchIndexLifecycleWarmUnfollow;
}

export interface ElasticsearchIndexLifecycleWarmAllocate {
    exclude: string;
    include: string;
    numberOfReplicas?: number;
    require: string;
}

export interface ElasticsearchIndexLifecycleWarmForcemerge {
    indexCodec?: string;
    maxNumSegments: number;
}

export interface ElasticsearchIndexLifecycleWarmMigrate {
    enabled?: boolean;
}

export interface ElasticsearchIndexLifecycleWarmReadonly {
    enabled?: boolean;
}

export interface ElasticsearchIndexLifecycleWarmSetPriority {
    priority: number;
}

export interface ElasticsearchIndexLifecycleWarmShrink {
    maxPrimaryShardSize?: string;
    numberOfShards?: number;
}

export interface ElasticsearchIndexLifecycleWarmUnfollow {
    enabled?: boolean;
}

export interface ElasticsearchIndexSettings {
    /**
     * Defines the setting for the index.
     */
    settings: outputs.ElasticsearchIndexSettingsSetting[];
}

export interface ElasticsearchIndexSettingsSetting {
    /**
     * Name of the index you wish to create.
     */
    name: string;
    value: string;
}

export interface ElasticsearchIndexTemplateDataStream {
    /**
     * If true, the data stream is hidden.
     */
    hidden?: boolean;
}

export interface ElasticsearchIndexTemplateElasticsearchConnection {
    /**
     * Path to a custom Certificate Authority certificate
     */
    caFile?: string;
    endpoints?: string[];
    /**
     * Disable TLS certificate validation
     */
    insecure?: boolean;
    /**
     * A password to use for API authentication to Elasticsearch.
     */
    password?: string;
    /**
     * A username to use for API authentication to Elasticsearch.
     */
    username?: string;
}

export interface ElasticsearchIndexTemplateTemplate {
    /**
     * Alias to add.
     */
    aliases?: outputs.ElasticsearchIndexTemplateTemplateAlias[];
    /**
     * Mapping for fields in the index.
     */
    mappings?: string;
    /**
     * Configuration options for the index. See, https://www.elastic.co/guide/en/elasticsearch/reference/current/index-modules.html#index-modules-settings
     */
    settings?: string;
}

export interface ElasticsearchIndexTemplateTemplateAlias {
    filter?: string;
    indexRouting?: string;
    isHidden?: boolean;
    isWriteIndex?: boolean;
    /**
     * Name of the index template to create.
     */
    name: string;
    routing?: string;
    searchRouting?: string;
}

export interface ElasticsearchIngestPipelineElasticsearchConnection {
    /**
     * Path to a custom Certificate Authority certificate
     */
    caFile?: string;
    endpoints?: string[];
    /**
     * Disable TLS certificate validation
     */
    insecure?: boolean;
    /**
     * A password to use for API authentication to Elasticsearch.
     */
    password?: string;
    /**
     * A username to use for API authentication to Elasticsearch.
     */
    username?: string;
}

export interface ElasticsearchSecurityRoleApplication {
    /**
     * The name of the application to which this entry applies.
     */
    application: string;
    /**
     * A list of strings, where each element is the name of an application privilege or action.
     */
    privileges: string[];
    /**
     * A list resources to which the privileges are applied.
     */
    resources: string[];
}

export interface ElasticsearchSecurityRoleElasticsearchConnection {
    /**
     * Path to a custom Certificate Authority certificate
     */
    caFile?: string;
    endpoints?: string[];
    /**
     * Disable TLS certificate validation
     */
    insecure?: boolean;
    /**
     * A password to use for API authentication to Elasticsearch.
     */
    password?: string;
    /**
     * A username to use for API authentication to Elasticsearch.
     */
    username?: string;
}

export interface ElasticsearchSecurityRoleIndex {
    /**
     * The document fields that the owners of the role have read access to.
     */
    fieldSecurity?: outputs.ElasticsearchSecurityRoleIndexFieldSecurity;
    /**
     * A list of indices (or index name patterns) to which the permissions in this entry apply.
     */
    names: string[];
    /**
     * The index level privileges that the owners of the role have on the specified indices.
     */
    privileges: string[];
    /**
     * A search query that defines the documents the owners of the role have read access to.
     */
    query?: string;
}

export interface ElasticsearchSecurityRoleIndexFieldSecurity {
    excepts?: string[];
    grants?: string[];
}

export interface ElasticsearchSecurityUserElasticsearchConnection {
    /**
     * Path to a custom Certificate Authority certificate
     */
    caFile?: string;
    endpoints?: string[];
    /**
     * Disable TLS certificate validation
     */
    insecure?: boolean;
    /**
     * A password to use for API authentication to Elasticsearch.
     */
    password?: string;
    /**
     * A username to use for API authentication to Elasticsearch.
     */
    username?: string;
}

export interface ElasticsearchSnapshotLifecycleElasticsearchConnection {
    /**
     * Path to a custom Certificate Authority certificate
     */
    caFile?: string;
    endpoints?: string[];
    /**
     * Disable TLS certificate validation
     */
    insecure?: boolean;
    /**
     * A password to use for API authentication to Elasticsearch.
     */
    password?: string;
    /**
     * A username to use for API authentication to Elasticsearch.
     */
    username?: string;
}

export interface ElasticsearchSnapshotRepositoryAzure {
    /**
     * Specifies the path within the container to the repository data.
     */
    basePath: string;
    /**
     * Maximum size of files in snapshots.
     */
    chunkSize?: string;
    /**
     * Azure named client to use.
     */
    client?: string;
    /**
     * If true, metadata files, such as index mappings and settings, are compressed in snapshots.
     */
    compress?: boolean;
    /**
     * Container name. You must create the Azure container before creating the repository.
     */
    container: string;
    /**
     * Location mode. `primaryOnly` or `secondaryOnly`. See: https://docs.microsoft.com/en-us/azure/storage/common/storage-redundancy
     */
    locationMode?: string;
    /**
     * Maximum snapshot restore rate per node.
     */
    maxRestoreBytesPerSec?: string;
    /**
     * Maximum snapshot creation rate per node.
     */
    maxSnapshotBytesPerSec?: string;
    /**
     * If true, the repository is read-only.
     */
    readonly?: boolean;
}

export interface ElasticsearchSnapshotRepositoryElasticsearchConnection {
    /**
     * Path to a custom Certificate Authority certificate
     */
    caFile?: string;
    endpoints?: string[];
    /**
     * Disable TLS certificate validation
     */
    insecure?: boolean;
    /**
     * A password to use for API authentication to Elasticsearch.
     */
    password?: string;
    /**
     * A username to use for API authentication to Elasticsearch.
     */
    username?: string;
}

export interface ElasticsearchSnapshotRepositoryFs {
    /**
     * Maximum size of files in snapshots.
     */
    chunkSize?: string;
    /**
     * If true, metadata files, such as index mappings and settings, are compressed in snapshots.
     */
    compress?: boolean;
    /**
     * Location of the shared filesystem used to store and retrieve snapshots.
     */
    location: string;
    /**
     * Maximum number of snapshots the repository can contain.
     */
    maxNumberOfSnapshots?: number;
    /**
     * Maximum snapshot restore rate per node.
     */
    maxRestoreBytesPerSec?: string;
    /**
     * Maximum snapshot creation rate per node.
     */
    maxSnapshotBytesPerSec?: string;
    /**
     * If true, the repository is read-only.
     */
    readonly?: boolean;
}

export interface ElasticsearchSnapshotRepositoryGcs {
    /**
     * Specifies the path within the bucket to the repository data. Defaults to the root of the bucket.
     */
    basePath: string;
    /**
     * The name of the bucket to be used for snapshots.
     */
    bucket: string;
    /**
     * Maximum size of files in snapshots.
     */
    chunkSize?: string;
    /**
     * The name of the client to use to connect to Google Cloud Storage.
     */
    client?: string;
    /**
     * If true, metadata files, such as index mappings and settings, are compressed in snapshots.
     */
    compress?: boolean;
    /**
     * Maximum snapshot restore rate per node.
     */
    maxRestoreBytesPerSec?: string;
    /**
     * Maximum snapshot creation rate per node.
     */
    maxSnapshotBytesPerSec?: string;
    /**
     * If true, the repository is read-only.
     */
    readonly?: boolean;
}

export interface ElasticsearchSnapshotRepositoryHdfs {
    /**
     * Maximum size of files in snapshots.
     */
    chunkSize?: string;
    /**
     * If true, metadata files, such as index mappings and settings, are compressed in snapshots.
     */
    compress?: boolean;
    /**
     * Whether to load the default Hadoop configuration or not.
     */
    loadDefaults?: boolean;
    /**
     * Maximum snapshot restore rate per node.
     */
    maxRestoreBytesPerSec?: string;
    /**
     * Maximum snapshot creation rate per node.
     */
    maxSnapshotBytesPerSec?: string;
    /**
     * The file path within the filesystem where data is stored/loaded.
     */
    path: string;
    /**
     * If true, the repository is read-only.
     */
    readonly?: boolean;
    /**
     * The uri address for hdfs. ex: "hdfs://\n\n:\n\n/".
     */
    uri: string;
}

export interface ElasticsearchSnapshotRepositoryS3 {
    /**
     * Specifies the path to the repository data within its bucket.
     */
    basePath: string;
    /**
     * Name of the S3 bucket to use for snapshots.
     */
    bucket: string;
    /**
     * Minimum threshold below which the chunk is uploaded using a single request.
     */
    bufferSize: string;
    /**
     * The S3 repository supports all S3 canned ACLs.
     */
    cannedAcl?: string;
    /**
     * Maximum size of files in snapshots.
     */
    chunkSize?: string;
    /**
     * The name of the S3 client to use to connect to S3.
     */
    client?: string;
    /**
     * If true, metadata files, such as index mappings and settings, are compressed in snapshots.
     */
    compress?: boolean;
    /**
     * Maximum snapshot restore rate per node.
     */
    maxRestoreBytesPerSec?: string;
    /**
     * Maximum snapshot creation rate per node.
     */
    maxSnapshotBytesPerSec?: string;
    /**
     * If true, the repository is read-only.
     */
    readonly?: boolean;
    /**
     * When true, files are encrypted server-side using AES-256 algorithm.
     */
    serverSideEncryption?: boolean;
    /**
     * Sets the S3 storage class for objects stored in the snapshot repository.
     */
    storageClass?: string;
}

export interface ElasticsearchSnapshotRepositoryUrl {
    /**
     * Maximum size of files in snapshots.
     */
    chunkSize?: string;
    /**
     * If true, metadata files, such as index mappings and settings, are compressed in snapshots.
     */
    compress?: boolean;
    /**
     * Maximum number of retries for http and https URLs.
     */
    httpMaxRetries?: number;
    /**
     * Maximum wait time for data transfers over a connection.
     */
    httpSocketTimeout?: string;
    /**
     * Maximum number of snapshots the repository can contain.
     */
    maxNumberOfSnapshots?: number;
    /**
     * Maximum snapshot restore rate per node.
     */
    maxRestoreBytesPerSec?: string;
    /**
     * Maximum snapshot creation rate per node.
     */
    maxSnapshotBytesPerSec?: string;
    /**
     * If true, the repository is read-only.
     */
    readonly?: boolean;
    /**
     * URL location of the root of the shared filesystem repository.
     */
    url: string;
}

export namespace config {
    export interface Elasticsearch {
        caFile?: string;
        endpoints?: string[];
        insecure?: boolean;
        password?: string;
        username?: string;
    }

}
