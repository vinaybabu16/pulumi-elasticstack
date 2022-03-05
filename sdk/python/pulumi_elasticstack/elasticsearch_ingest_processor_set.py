# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'ElasticsearchIngestProcessorSetResult',
    'AwaitableElasticsearchIngestProcessorSetResult',
    'elasticsearch_ingest_processor_set',
    'elasticsearch_ingest_processor_set_output',
]

@pulumi.output_type
class ElasticsearchIngestProcessorSetResult:
    """
    A collection of values returned by ElasticsearchIngestProcessorSet.
    """
    def __init__(__self__, copy_from=None, description=None, field=None, id=None, if_=None, ignore_empty_value=None, ignore_failure=None, json=None, media_type=None, on_failures=None, override=None, tag=None, value=None):
        if copy_from and not isinstance(copy_from, str):
            raise TypeError("Expected argument 'copy_from' to be a str")
        pulumi.set(__self__, "copy_from", copy_from)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if field and not isinstance(field, str):
            raise TypeError("Expected argument 'field' to be a str")
        pulumi.set(__self__, "field", field)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if if_ and not isinstance(if_, str):
            raise TypeError("Expected argument 'if_' to be a str")
        pulumi.set(__self__, "if_", if_)
        if ignore_empty_value and not isinstance(ignore_empty_value, bool):
            raise TypeError("Expected argument 'ignore_empty_value' to be a bool")
        pulumi.set(__self__, "ignore_empty_value", ignore_empty_value)
        if ignore_failure and not isinstance(ignore_failure, bool):
            raise TypeError("Expected argument 'ignore_failure' to be a bool")
        pulumi.set(__self__, "ignore_failure", ignore_failure)
        if json and not isinstance(json, str):
            raise TypeError("Expected argument 'json' to be a str")
        pulumi.set(__self__, "json", json)
        if media_type and not isinstance(media_type, str):
            raise TypeError("Expected argument 'media_type' to be a str")
        pulumi.set(__self__, "media_type", media_type)
        if on_failures and not isinstance(on_failures, list):
            raise TypeError("Expected argument 'on_failures' to be a list")
        pulumi.set(__self__, "on_failures", on_failures)
        if override and not isinstance(override, bool):
            raise TypeError("Expected argument 'override' to be a bool")
        pulumi.set(__self__, "override", override)
        if tag and not isinstance(tag, str):
            raise TypeError("Expected argument 'tag' to be a str")
        pulumi.set(__self__, "tag", tag)
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="copyFrom")
    def copy_from(self) -> Optional[str]:
        """
        The origin field which will be copied to `field`, cannot set `value` simultaneously.
        """
        return pulumi.get(self, "copy_from")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of the processor.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def field(self) -> str:
        """
        The field to insert, upsert, or update.
        """
        return pulumi.get(self, "field")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Internal identifier of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="if")
    def if_(self) -> Optional[str]:
        """
        Conditionally execute the processor
        """
        return pulumi.get(self, "if_")

    @property
    @pulumi.getter(name="ignoreEmptyValue")
    def ignore_empty_value(self) -> Optional[bool]:
        """
        If `true` and `value` is a template snippet that evaluates to `null` or the empty string, the processor quietly exits without modifying the document
        """
        return pulumi.get(self, "ignore_empty_value")

    @property
    @pulumi.getter(name="ignoreFailure")
    def ignore_failure(self) -> Optional[bool]:
        """
        Ignore failures for the processor.
        """
        return pulumi.get(self, "ignore_failure")

    @property
    @pulumi.getter
    def json(self) -> str:
        """
        JSON representation of this data source.
        """
        return pulumi.get(self, "json")

    @property
    @pulumi.getter(name="mediaType")
    def media_type(self) -> Optional[str]:
        """
        The media type for encoding value.
        """
        return pulumi.get(self, "media_type")

    @property
    @pulumi.getter(name="onFailures")
    def on_failures(self) -> Optional[Sequence[str]]:
        """
        Handle failures for the processor.
        """
        return pulumi.get(self, "on_failures")

    @property
    @pulumi.getter
    def override(self) -> Optional[bool]:
        """
        If processor will update fields with pre-existing non-null-valued field.
        """
        return pulumi.get(self, "override")

    @property
    @pulumi.getter
    def tag(self) -> Optional[str]:
        """
        Identifier for the processor.
        """
        return pulumi.get(self, "tag")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        The value to be set for the field. Supports template snippets. May specify only one of `value` or `copy_from`.
        """
        return pulumi.get(self, "value")


class AwaitableElasticsearchIngestProcessorSetResult(ElasticsearchIngestProcessorSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ElasticsearchIngestProcessorSetResult(
            copy_from=self.copy_from,
            description=self.description,
            field=self.field,
            id=self.id,
            if_=self.if_,
            ignore_empty_value=self.ignore_empty_value,
            ignore_failure=self.ignore_failure,
            json=self.json,
            media_type=self.media_type,
            on_failures=self.on_failures,
            override=self.override,
            tag=self.tag,
            value=self.value)


def elasticsearch_ingest_processor_set(copy_from: Optional[str] = None,
                                       description: Optional[str] = None,
                                       field: Optional[str] = None,
                                       if_: Optional[str] = None,
                                       ignore_empty_value: Optional[bool] = None,
                                       ignore_failure: Optional[bool] = None,
                                       media_type: Optional[str] = None,
                                       on_failures: Optional[Sequence[str]] = None,
                                       override: Optional[bool] = None,
                                       tag: Optional[str] = None,
                                       value: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableElasticsearchIngestProcessorSetResult:
    """
    Sets one field and associates it with the specified value. If the field already exists, its value will be replaced with the provided one.

    See: https://www.elastic.co/guide/en/elasticsearch/reference/current/set-processor.html

    ## Example Usage

    ```python
    import pulumi
    import pulumi_elasticstack as elasticstack

    set = elasticstack.elasticsearch_ingest_processor_set(field="count",
        value="1")
    my_ingest_pipeline = elasticstack.ElasticsearchIngestPipeline("myIngestPipeline", processors=[set.json])
    ```


    :param str copy_from: The origin field which will be copied to `field`, cannot set `value` simultaneously.
    :param str description: Description of the processor.
    :param str field: The field to insert, upsert, or update.
    :param str if_: Conditionally execute the processor
    :param bool ignore_empty_value: If `true` and `value` is a template snippet that evaluates to `null` or the empty string, the processor quietly exits without modifying the document
    :param bool ignore_failure: Ignore failures for the processor.
    :param str media_type: The media type for encoding value.
    :param Sequence[str] on_failures: Handle failures for the processor.
    :param bool override: If processor will update fields with pre-existing non-null-valued field.
    :param str tag: Identifier for the processor.
    :param str value: The value to be set for the field. Supports template snippets. May specify only one of `value` or `copy_from`.
    """
    __args__ = dict()
    __args__['copyFrom'] = copy_from
    __args__['description'] = description
    __args__['field'] = field
    __args__['if'] = if_
    __args__['ignoreEmptyValue'] = ignore_empty_value
    __args__['ignoreFailure'] = ignore_failure
    __args__['mediaType'] = media_type
    __args__['onFailures'] = on_failures
    __args__['override'] = override
    __args__['tag'] = tag
    __args__['value'] = value
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('elasticstack:index/elasticsearchIngestProcessorSet:ElasticsearchIngestProcessorSet', __args__, opts=opts, typ=ElasticsearchIngestProcessorSetResult).value

    return AwaitableElasticsearchIngestProcessorSetResult(
        copy_from=__ret__.copy_from,
        description=__ret__.description,
        field=__ret__.field,
        id=__ret__.id,
        if_=__ret__.if_,
        ignore_empty_value=__ret__.ignore_empty_value,
        ignore_failure=__ret__.ignore_failure,
        json=__ret__.json,
        media_type=__ret__.media_type,
        on_failures=__ret__.on_failures,
        override=__ret__.override,
        tag=__ret__.tag,
        value=__ret__.value)


@_utilities.lift_output_func(elasticsearch_ingest_processor_set)
def elasticsearch_ingest_processor_set_output(copy_from: Optional[pulumi.Input[Optional[str]]] = None,
                                              description: Optional[pulumi.Input[Optional[str]]] = None,
                                              field: Optional[pulumi.Input[str]] = None,
                                              if_: Optional[pulumi.Input[Optional[str]]] = None,
                                              ignore_empty_value: Optional[pulumi.Input[Optional[bool]]] = None,
                                              ignore_failure: Optional[pulumi.Input[Optional[bool]]] = None,
                                              media_type: Optional[pulumi.Input[Optional[str]]] = None,
                                              on_failures: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                              override: Optional[pulumi.Input[Optional[bool]]] = None,
                                              tag: Optional[pulumi.Input[Optional[str]]] = None,
                                              value: Optional[pulumi.Input[Optional[str]]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ElasticsearchIngestProcessorSetResult]:
    """
    Sets one field and associates it with the specified value. If the field already exists, its value will be replaced with the provided one.

    See: https://www.elastic.co/guide/en/elasticsearch/reference/current/set-processor.html

    ## Example Usage

    ```python
    import pulumi
    import pulumi_elasticstack as elasticstack

    set = elasticstack.elasticsearch_ingest_processor_set(field="count",
        value="1")
    my_ingest_pipeline = elasticstack.ElasticsearchIngestPipeline("myIngestPipeline", processors=[set.json])
    ```


    :param str copy_from: The origin field which will be copied to `field`, cannot set `value` simultaneously.
    :param str description: Description of the processor.
    :param str field: The field to insert, upsert, or update.
    :param str if_: Conditionally execute the processor
    :param bool ignore_empty_value: If `true` and `value` is a template snippet that evaluates to `null` or the empty string, the processor quietly exits without modifying the document
    :param bool ignore_failure: Ignore failures for the processor.
    :param str media_type: The media type for encoding value.
    :param Sequence[str] on_failures: Handle failures for the processor.
    :param bool override: If processor will update fields with pre-existing non-null-valued field.
    :param str tag: Identifier for the processor.
    :param str value: The value to be set for the field. Supports template snippets. May specify only one of `value` or `copy_from`.
    """
    ...
