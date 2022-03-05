// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Elasticstack.Inputs
{

    public sealed class ElasticsearchIndexLifecycleWarmGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Updates the index settings to change which nodes are allowed to host the index shards and change the number of replicas.
        /// </summary>
        [Input("allocate")]
        public Input<Inputs.ElasticsearchIndexLifecycleWarmAllocateGetArgs>? Allocate { get; set; }

        /// <summary>
        /// Force merges the index into the specified maximum number of segments. This action makes the index read-only.
        /// </summary>
        [Input("forcemerge")]
        public Input<Inputs.ElasticsearchIndexLifecycleWarmForcemergeGetArgs>? Forcemerge { get; set; }

        /// <summary>
        /// Moves the index to the data tier that corresponds to the current phase by updating the "index.routing.allocation.include.*tier*preference" index setting.
        /// </summary>
        [Input("migrate")]
        public Input<Inputs.ElasticsearchIndexLifecycleWarmMigrateGetArgs>? Migrate { get; set; }

        /// <summary>
        /// ILM moves indices through the lifecycle according to their age. To control the timing of these transitions, you set a minimum age for each phase.
        /// </summary>
        [Input("minAge")]
        public Input<string>? MinAge { get; set; }

        /// <summary>
        /// Makes the index read-only.
        /// </summary>
        [Input("readonly")]
        public Input<Inputs.ElasticsearchIndexLifecycleWarmReadonlyGetArgs>? Readonly { get; set; }

        /// <summary>
        /// Sets a source index to read-only and shrinks it into a new index with fewer primary shards.
        /// </summary>
        [Input("setPriority")]
        public Input<Inputs.ElasticsearchIndexLifecycleWarmSetPriorityGetArgs>? SetPriority { get; set; }

        /// <summary>
        /// Sets a source index to read-only and shrinks it into a new index with fewer primary shards.
        /// </summary>
        [Input("shrink")]
        public Input<Inputs.ElasticsearchIndexLifecycleWarmShrinkGetArgs>? Shrink { get; set; }

        /// <summary>
        /// Convert a follower index to a regular index. Performed automatically before a rollover, shrink, or searchable snapshot action.
        /// </summary>
        [Input("unfollow")]
        public Input<Inputs.ElasticsearchIndexLifecycleWarmUnfollowGetArgs>? Unfollow { get; set; }

        public ElasticsearchIndexLifecycleWarmGetArgs()
        {
        }
    }
}
