# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ElasticsearchIndexLifecycleArgs', 'ElasticsearchIndexLifecycle']

@pulumi.input_type
class ElasticsearchIndexLifecycleArgs:
    def __init__(__self__, *,
                 cold: Optional[pulumi.Input['ElasticsearchIndexLifecycleColdArgs']] = None,
                 delete: Optional[pulumi.Input['ElasticsearchIndexLifecycleDeleteArgs']] = None,
                 elasticsearch_connection: Optional[pulumi.Input['ElasticsearchIndexLifecycleElasticsearchConnectionArgs']] = None,
                 frozen: Optional[pulumi.Input['ElasticsearchIndexLifecycleFrozenArgs']] = None,
                 hot: Optional[pulumi.Input['ElasticsearchIndexLifecycleHotArgs']] = None,
                 metadata: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 warm: Optional[pulumi.Input['ElasticsearchIndexLifecycleWarmArgs']] = None):
        """
        The set of arguments for constructing a ElasticsearchIndexLifecycle resource.
        :param pulumi.Input['ElasticsearchIndexLifecycleColdArgs'] cold: The index is no longer being updated and is queried infrequently. The information still needs to be searchable, but it’s okay if those queries are slower.
        :param pulumi.Input['ElasticsearchIndexLifecycleDeleteArgs'] delete: The index is no longer needed and can safely be removed.
        :param pulumi.Input['ElasticsearchIndexLifecycleElasticsearchConnectionArgs'] elasticsearch_connection: Used to establish connection to Elasticsearch server. Overrides environment variables if present.
        :param pulumi.Input['ElasticsearchIndexLifecycleFrozenArgs'] frozen: The index is no longer being updated and is queried rarely. The information still needs to be searchable, but it’s okay if those queries are extremely slow.
        :param pulumi.Input['ElasticsearchIndexLifecycleHotArgs'] hot: The index is actively being updated and queried.
        :param pulumi.Input[str] metadata: Optional user metadata about the ilm policy. Must be valid JSON document.
        :param pulumi.Input[str] name: Identifier for the policy.
        :param pulumi.Input['ElasticsearchIndexLifecycleWarmArgs'] warm: The index is no longer being updated but is still being queried.
        """
        if cold is not None:
            pulumi.set(__self__, "cold", cold)
        if delete is not None:
            pulumi.set(__self__, "delete", delete)
        if elasticsearch_connection is not None:
            pulumi.set(__self__, "elasticsearch_connection", elasticsearch_connection)
        if frozen is not None:
            pulumi.set(__self__, "frozen", frozen)
        if hot is not None:
            pulumi.set(__self__, "hot", hot)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if warm is not None:
            pulumi.set(__self__, "warm", warm)

    @property
    @pulumi.getter
    def cold(self) -> Optional[pulumi.Input['ElasticsearchIndexLifecycleColdArgs']]:
        """
        The index is no longer being updated and is queried infrequently. The information still needs to be searchable, but it’s okay if those queries are slower.
        """
        return pulumi.get(self, "cold")

    @cold.setter
    def cold(self, value: Optional[pulumi.Input['ElasticsearchIndexLifecycleColdArgs']]):
        pulumi.set(self, "cold", value)

    @property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input['ElasticsearchIndexLifecycleDeleteArgs']]:
        """
        The index is no longer needed and can safely be removed.
        """
        return pulumi.get(self, "delete")

    @delete.setter
    def delete(self, value: Optional[pulumi.Input['ElasticsearchIndexLifecycleDeleteArgs']]):
        pulumi.set(self, "delete", value)

    @property
    @pulumi.getter(name="elasticsearchConnection")
    def elasticsearch_connection(self) -> Optional[pulumi.Input['ElasticsearchIndexLifecycleElasticsearchConnectionArgs']]:
        """
        Used to establish connection to Elasticsearch server. Overrides environment variables if present.
        """
        return pulumi.get(self, "elasticsearch_connection")

    @elasticsearch_connection.setter
    def elasticsearch_connection(self, value: Optional[pulumi.Input['ElasticsearchIndexLifecycleElasticsearchConnectionArgs']]):
        pulumi.set(self, "elasticsearch_connection", value)

    @property
    @pulumi.getter
    def frozen(self) -> Optional[pulumi.Input['ElasticsearchIndexLifecycleFrozenArgs']]:
        """
        The index is no longer being updated and is queried rarely. The information still needs to be searchable, but it’s okay if those queries are extremely slow.
        """
        return pulumi.get(self, "frozen")

    @frozen.setter
    def frozen(self, value: Optional[pulumi.Input['ElasticsearchIndexLifecycleFrozenArgs']]):
        pulumi.set(self, "frozen", value)

    @property
    @pulumi.getter
    def hot(self) -> Optional[pulumi.Input['ElasticsearchIndexLifecycleHotArgs']]:
        """
        The index is actively being updated and queried.
        """
        return pulumi.get(self, "hot")

    @hot.setter
    def hot(self, value: Optional[pulumi.Input['ElasticsearchIndexLifecycleHotArgs']]):
        pulumi.set(self, "hot", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[str]]:
        """
        Optional user metadata about the ilm policy. Must be valid JSON document.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier for the policy.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def warm(self) -> Optional[pulumi.Input['ElasticsearchIndexLifecycleWarmArgs']]:
        """
        The index is no longer being updated but is still being queried.
        """
        return pulumi.get(self, "warm")

    @warm.setter
    def warm(self, value: Optional[pulumi.Input['ElasticsearchIndexLifecycleWarmArgs']]):
        pulumi.set(self, "warm", value)


@pulumi.input_type
class _ElasticsearchIndexLifecycleState:
    def __init__(__self__, *,
                 cold: Optional[pulumi.Input['ElasticsearchIndexLifecycleColdArgs']] = None,
                 delete: Optional[pulumi.Input['ElasticsearchIndexLifecycleDeleteArgs']] = None,
                 elasticsearch_connection: Optional[pulumi.Input['ElasticsearchIndexLifecycleElasticsearchConnectionArgs']] = None,
                 frozen: Optional[pulumi.Input['ElasticsearchIndexLifecycleFrozenArgs']] = None,
                 hot: Optional[pulumi.Input['ElasticsearchIndexLifecycleHotArgs']] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[str]] = None,
                 modified_date: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 warm: Optional[pulumi.Input['ElasticsearchIndexLifecycleWarmArgs']] = None):
        """
        Input properties used for looking up and filtering ElasticsearchIndexLifecycle resources.
        :param pulumi.Input['ElasticsearchIndexLifecycleColdArgs'] cold: The index is no longer being updated and is queried infrequently. The information still needs to be searchable, but it’s okay if those queries are slower.
        :param pulumi.Input['ElasticsearchIndexLifecycleDeleteArgs'] delete: The index is no longer needed and can safely be removed.
        :param pulumi.Input['ElasticsearchIndexLifecycleElasticsearchConnectionArgs'] elasticsearch_connection: Used to establish connection to Elasticsearch server. Overrides environment variables if present.
        :param pulumi.Input['ElasticsearchIndexLifecycleFrozenArgs'] frozen: The index is no longer being updated and is queried rarely. The information still needs to be searchable, but it’s okay if those queries are extremely slow.
        :param pulumi.Input['ElasticsearchIndexLifecycleHotArgs'] hot: The index is actively being updated and queried.
        :param pulumi.Input[str] id: Internal identifier of the resource
        :param pulumi.Input[str] metadata: Optional user metadata about the ilm policy. Must be valid JSON document.
        :param pulumi.Input[str] modified_date: The DateTime of the last modification.
        :param pulumi.Input[str] name: Identifier for the policy.
        :param pulumi.Input['ElasticsearchIndexLifecycleWarmArgs'] warm: The index is no longer being updated but is still being queried.
        """
        if cold is not None:
            pulumi.set(__self__, "cold", cold)
        if delete is not None:
            pulumi.set(__self__, "delete", delete)
        if elasticsearch_connection is not None:
            pulumi.set(__self__, "elasticsearch_connection", elasticsearch_connection)
        if frozen is not None:
            pulumi.set(__self__, "frozen", frozen)
        if hot is not None:
            pulumi.set(__self__, "hot", hot)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if modified_date is not None:
            pulumi.set(__self__, "modified_date", modified_date)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if warm is not None:
            pulumi.set(__self__, "warm", warm)

    @property
    @pulumi.getter
    def cold(self) -> Optional[pulumi.Input['ElasticsearchIndexLifecycleColdArgs']]:
        """
        The index is no longer being updated and is queried infrequently. The information still needs to be searchable, but it’s okay if those queries are slower.
        """
        return pulumi.get(self, "cold")

    @cold.setter
    def cold(self, value: Optional[pulumi.Input['ElasticsearchIndexLifecycleColdArgs']]):
        pulumi.set(self, "cold", value)

    @property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input['ElasticsearchIndexLifecycleDeleteArgs']]:
        """
        The index is no longer needed and can safely be removed.
        """
        return pulumi.get(self, "delete")

    @delete.setter
    def delete(self, value: Optional[pulumi.Input['ElasticsearchIndexLifecycleDeleteArgs']]):
        pulumi.set(self, "delete", value)

    @property
    @pulumi.getter(name="elasticsearchConnection")
    def elasticsearch_connection(self) -> Optional[pulumi.Input['ElasticsearchIndexLifecycleElasticsearchConnectionArgs']]:
        """
        Used to establish connection to Elasticsearch server. Overrides environment variables if present.
        """
        return pulumi.get(self, "elasticsearch_connection")

    @elasticsearch_connection.setter
    def elasticsearch_connection(self, value: Optional[pulumi.Input['ElasticsearchIndexLifecycleElasticsearchConnectionArgs']]):
        pulumi.set(self, "elasticsearch_connection", value)

    @property
    @pulumi.getter
    def frozen(self) -> Optional[pulumi.Input['ElasticsearchIndexLifecycleFrozenArgs']]:
        """
        The index is no longer being updated and is queried rarely. The information still needs to be searchable, but it’s okay if those queries are extremely slow.
        """
        return pulumi.get(self, "frozen")

    @frozen.setter
    def frozen(self, value: Optional[pulumi.Input['ElasticsearchIndexLifecycleFrozenArgs']]):
        pulumi.set(self, "frozen", value)

    @property
    @pulumi.getter
    def hot(self) -> Optional[pulumi.Input['ElasticsearchIndexLifecycleHotArgs']]:
        """
        The index is actively being updated and queried.
        """
        return pulumi.get(self, "hot")

    @hot.setter
    def hot(self, value: Optional[pulumi.Input['ElasticsearchIndexLifecycleHotArgs']]):
        pulumi.set(self, "hot", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Internal identifier of the resource
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[str]]:
        """
        Optional user metadata about the ilm policy. Must be valid JSON document.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter(name="modifiedDate")
    def modified_date(self) -> Optional[pulumi.Input[str]]:
        """
        The DateTime of the last modification.
        """
        return pulumi.get(self, "modified_date")

    @modified_date.setter
    def modified_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "modified_date", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier for the policy.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def warm(self) -> Optional[pulumi.Input['ElasticsearchIndexLifecycleWarmArgs']]:
        """
        The index is no longer being updated but is still being queried.
        """
        return pulumi.get(self, "warm")

    @warm.setter
    def warm(self, value: Optional[pulumi.Input['ElasticsearchIndexLifecycleWarmArgs']]):
        pulumi.set(self, "warm", value)


class ElasticsearchIndexLifecycle(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cold: Optional[pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleColdArgs']]] = None,
                 delete: Optional[pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleDeleteArgs']]] = None,
                 elasticsearch_connection: Optional[pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleElasticsearchConnectionArgs']]] = None,
                 frozen: Optional[pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleFrozenArgs']]] = None,
                 hot: Optional[pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleHotArgs']]] = None,
                 metadata: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 warm: Optional[pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleWarmArgs']]] = None,
                 __props__=None):
        """
        Creates or updates lifecycle policy. See: https://www.elastic.co/guide/en/elasticsearch/reference/current/ilm-put-lifecycle.html and https://www.elastic.co/guide/en/elasticsearch/reference/current/ilm-index-lifecycle.html

        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumi_elasticstack as elasticstack

        my_ilm = elasticstack.ElasticsearchIndexLifecycle("myIlm",
            hot=elasticstack.ElasticsearchIndexLifecycleHotArgs(
                min_age="1h",
                set_priority=elasticstack.ElasticsearchIndexLifecycleHotSetPriorityArgs(
                    priority=10,
                ),
                rollover=elasticstack.ElasticsearchIndexLifecycleHotRolloverArgs(
                    max_age="1d",
                ),
                readonly=elasticstack.ElasticsearchIndexLifecycleHotReadonlyArgs(),
            ),
            warm=elasticstack.ElasticsearchIndexLifecycleWarmArgs(
                min_age="0ms",
                set_priority=elasticstack.ElasticsearchIndexLifecycleWarmSetPriorityArgs(
                    priority=60,
                ),
                readonly=elasticstack.ElasticsearchIndexLifecycleWarmReadonlyArgs(),
                allocate=elasticstack.ElasticsearchIndexLifecycleWarmAllocateArgs(
                    exclude=json.dumps({
                        "box_type": "hot",
                    }),
                    number_of_replicas=0,
                ),
            ),
            delete=elasticstack.ElasticsearchIndexLifecycleDeleteArgs(
                min_age="2d",
                delete=elasticstack.ElasticsearchIndexLifecycleDeleteDeleteArgs(),
            ))
        ```

        ## Import

        ```sh
         $ pulumi import elasticstack:index/elasticsearchIndexLifecycle:ElasticsearchIndexLifecycle my_ilm <cluster_uuid>/<ilm_name>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleColdArgs']] cold: The index is no longer being updated and is queried infrequently. The information still needs to be searchable, but it’s okay if those queries are slower.
        :param pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleDeleteArgs']] delete: The index is no longer needed and can safely be removed.
        :param pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleElasticsearchConnectionArgs']] elasticsearch_connection: Used to establish connection to Elasticsearch server. Overrides environment variables if present.
        :param pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleFrozenArgs']] frozen: The index is no longer being updated and is queried rarely. The information still needs to be searchable, but it’s okay if those queries are extremely slow.
        :param pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleHotArgs']] hot: The index is actively being updated and queried.
        :param pulumi.Input[str] metadata: Optional user metadata about the ilm policy. Must be valid JSON document.
        :param pulumi.Input[str] name: Identifier for the policy.
        :param pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleWarmArgs']] warm: The index is no longer being updated but is still being queried.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ElasticsearchIndexLifecycleArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates or updates lifecycle policy. See: https://www.elastic.co/guide/en/elasticsearch/reference/current/ilm-put-lifecycle.html and https://www.elastic.co/guide/en/elasticsearch/reference/current/ilm-index-lifecycle.html

        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumi_elasticstack as elasticstack

        my_ilm = elasticstack.ElasticsearchIndexLifecycle("myIlm",
            hot=elasticstack.ElasticsearchIndexLifecycleHotArgs(
                min_age="1h",
                set_priority=elasticstack.ElasticsearchIndexLifecycleHotSetPriorityArgs(
                    priority=10,
                ),
                rollover=elasticstack.ElasticsearchIndexLifecycleHotRolloverArgs(
                    max_age="1d",
                ),
                readonly=elasticstack.ElasticsearchIndexLifecycleHotReadonlyArgs(),
            ),
            warm=elasticstack.ElasticsearchIndexLifecycleWarmArgs(
                min_age="0ms",
                set_priority=elasticstack.ElasticsearchIndexLifecycleWarmSetPriorityArgs(
                    priority=60,
                ),
                readonly=elasticstack.ElasticsearchIndexLifecycleWarmReadonlyArgs(),
                allocate=elasticstack.ElasticsearchIndexLifecycleWarmAllocateArgs(
                    exclude=json.dumps({
                        "box_type": "hot",
                    }),
                    number_of_replicas=0,
                ),
            ),
            delete=elasticstack.ElasticsearchIndexLifecycleDeleteArgs(
                min_age="2d",
                delete=elasticstack.ElasticsearchIndexLifecycleDeleteDeleteArgs(),
            ))
        ```

        ## Import

        ```sh
         $ pulumi import elasticstack:index/elasticsearchIndexLifecycle:ElasticsearchIndexLifecycle my_ilm <cluster_uuid>/<ilm_name>
        ```

        :param str resource_name: The name of the resource.
        :param ElasticsearchIndexLifecycleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ElasticsearchIndexLifecycleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cold: Optional[pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleColdArgs']]] = None,
                 delete: Optional[pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleDeleteArgs']]] = None,
                 elasticsearch_connection: Optional[pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleElasticsearchConnectionArgs']]] = None,
                 frozen: Optional[pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleFrozenArgs']]] = None,
                 hot: Optional[pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleHotArgs']]] = None,
                 metadata: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 warm: Optional[pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleWarmArgs']]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ElasticsearchIndexLifecycleArgs.__new__(ElasticsearchIndexLifecycleArgs)

            __props__.__dict__["cold"] = cold
            __props__.__dict__["delete"] = delete
            __props__.__dict__["elasticsearch_connection"] = elasticsearch_connection
            __props__.__dict__["frozen"] = frozen
            __props__.__dict__["hot"] = hot
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["name"] = name
            __props__.__dict__["warm"] = warm
            __props__.__dict__["id"] = None
            __props__.__dict__["modified_date"] = None
        super(ElasticsearchIndexLifecycle, __self__).__init__(
            'elasticstack:index/elasticsearchIndexLifecycle:ElasticsearchIndexLifecycle',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cold: Optional[pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleColdArgs']]] = None,
            delete: Optional[pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleDeleteArgs']]] = None,
            elasticsearch_connection: Optional[pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleElasticsearchConnectionArgs']]] = None,
            frozen: Optional[pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleFrozenArgs']]] = None,
            hot: Optional[pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleHotArgs']]] = None,
            id: Optional[pulumi.Input[str]] = None,
            metadata: Optional[pulumi.Input[str]] = None,
            modified_date: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            warm: Optional[pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleWarmArgs']]] = None) -> 'ElasticsearchIndexLifecycle':
        """
        Get an existing ElasticsearchIndexLifecycle resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleColdArgs']] cold: The index is no longer being updated and is queried infrequently. The information still needs to be searchable, but it’s okay if those queries are slower.
        :param pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleDeleteArgs']] delete: The index is no longer needed and can safely be removed.
        :param pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleElasticsearchConnectionArgs']] elasticsearch_connection: Used to establish connection to Elasticsearch server. Overrides environment variables if present.
        :param pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleFrozenArgs']] frozen: The index is no longer being updated and is queried rarely. The information still needs to be searchable, but it’s okay if those queries are extremely slow.
        :param pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleHotArgs']] hot: The index is actively being updated and queried.
        :param pulumi.Input[str] id: Internal identifier of the resource
        :param pulumi.Input[str] metadata: Optional user metadata about the ilm policy. Must be valid JSON document.
        :param pulumi.Input[str] modified_date: The DateTime of the last modification.
        :param pulumi.Input[str] name: Identifier for the policy.
        :param pulumi.Input[pulumi.InputType['ElasticsearchIndexLifecycleWarmArgs']] warm: The index is no longer being updated but is still being queried.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ElasticsearchIndexLifecycleState.__new__(_ElasticsearchIndexLifecycleState)

        __props__.__dict__["cold"] = cold
        __props__.__dict__["delete"] = delete
        __props__.__dict__["elasticsearch_connection"] = elasticsearch_connection
        __props__.__dict__["frozen"] = frozen
        __props__.__dict__["hot"] = hot
        __props__.__dict__["id"] = id
        __props__.__dict__["metadata"] = metadata
        __props__.__dict__["modified_date"] = modified_date
        __props__.__dict__["name"] = name
        __props__.__dict__["warm"] = warm
        return ElasticsearchIndexLifecycle(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def cold(self) -> pulumi.Output[Optional['outputs.ElasticsearchIndexLifecycleCold']]:
        """
        The index is no longer being updated and is queried infrequently. The information still needs to be searchable, but it’s okay if those queries are slower.
        """
        return pulumi.get(self, "cold")

    @property
    @pulumi.getter
    def delete(self) -> pulumi.Output[Optional['outputs.ElasticsearchIndexLifecycleDelete']]:
        """
        The index is no longer needed and can safely be removed.
        """
        return pulumi.get(self, "delete")

    @property
    @pulumi.getter(name="elasticsearchConnection")
    def elasticsearch_connection(self) -> pulumi.Output[Optional['outputs.ElasticsearchIndexLifecycleElasticsearchConnection']]:
        """
        Used to establish connection to Elasticsearch server. Overrides environment variables if present.
        """
        return pulumi.get(self, "elasticsearch_connection")

    @property
    @pulumi.getter
    def frozen(self) -> pulumi.Output[Optional['outputs.ElasticsearchIndexLifecycleFrozen']]:
        """
        The index is no longer being updated and is queried rarely. The information still needs to be searchable, but it’s okay if those queries are extremely slow.
        """
        return pulumi.get(self, "frozen")

    @property
    @pulumi.getter
    def hot(self) -> pulumi.Output[Optional['outputs.ElasticsearchIndexLifecycleHot']]:
        """
        The index is actively being updated and queried.
        """
        return pulumi.get(self, "hot")

    @property
    @pulumi.getter
    def id(self) -> pulumi.Output[str]:
        """
        Internal identifier of the resource
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[str]]:
        """
        Optional user metadata about the ilm policy. Must be valid JSON document.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter(name="modifiedDate")
    def modified_date(self) -> pulumi.Output[str]:
        """
        The DateTime of the last modification.
        """
        return pulumi.get(self, "modified_date")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Identifier for the policy.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def warm(self) -> pulumi.Output[Optional['outputs.ElasticsearchIndexLifecycleWarm']]:
        """
        The index is no longer being updated but is still being queried.
        """
        return pulumi.get(self, "warm")

