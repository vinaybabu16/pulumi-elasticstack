# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'ElasticsearchIngestProcessorJoinResult',
    'AwaitableElasticsearchIngestProcessorJoinResult',
    'elasticsearch_ingest_processor_join',
    'elasticsearch_ingest_processor_join_output',
]

@pulumi.output_type
class ElasticsearchIngestProcessorJoinResult:
    """
    A collection of values returned by ElasticsearchIngestProcessorJoin.
    """
    def __init__(__self__, description=None, field=None, id=None, if_=None, ignore_failure=None, json=None, on_failures=None, separator=None, tag=None, target_field=None):
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
        if ignore_failure and not isinstance(ignore_failure, bool):
            raise TypeError("Expected argument 'ignore_failure' to be a bool")
        pulumi.set(__self__, "ignore_failure", ignore_failure)
        if json and not isinstance(json, str):
            raise TypeError("Expected argument 'json' to be a str")
        pulumi.set(__self__, "json", json)
        if on_failures and not isinstance(on_failures, list):
            raise TypeError("Expected argument 'on_failures' to be a list")
        pulumi.set(__self__, "on_failures", on_failures)
        if separator and not isinstance(separator, str):
            raise TypeError("Expected argument 'separator' to be a str")
        pulumi.set(__self__, "separator", separator)
        if tag and not isinstance(tag, str):
            raise TypeError("Expected argument 'tag' to be a str")
        pulumi.set(__self__, "tag", tag)
        if target_field and not isinstance(target_field, str):
            raise TypeError("Expected argument 'target_field' to be a str")
        pulumi.set(__self__, "target_field", target_field)

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
        Field containing array values to join.
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
    @pulumi.getter(name="onFailures")
    def on_failures(self) -> Optional[Sequence[str]]:
        """
        Handle failures for the processor.
        """
        return pulumi.get(self, "on_failures")

    @property
    @pulumi.getter
    def separator(self) -> str:
        """
        The separator character.
        """
        return pulumi.get(self, "separator")

    @property
    @pulumi.getter
    def tag(self) -> Optional[str]:
        """
        Identifier for the processor.
        """
        return pulumi.get(self, "tag")

    @property
    @pulumi.getter(name="targetField")
    def target_field(self) -> Optional[str]:
        """
        The field to assign the converted value to, by default `field` is updated in-place.
        """
        return pulumi.get(self, "target_field")


class AwaitableElasticsearchIngestProcessorJoinResult(ElasticsearchIngestProcessorJoinResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ElasticsearchIngestProcessorJoinResult(
            description=self.description,
            field=self.field,
            id=self.id,
            if_=self.if_,
            ignore_failure=self.ignore_failure,
            json=self.json,
            on_failures=self.on_failures,
            separator=self.separator,
            tag=self.tag,
            target_field=self.target_field)


def elasticsearch_ingest_processor_join(description: Optional[str] = None,
                                        field: Optional[str] = None,
                                        if_: Optional[str] = None,
                                        ignore_failure: Optional[bool] = None,
                                        on_failures: Optional[Sequence[str]] = None,
                                        separator: Optional[str] = None,
                                        tag: Optional[str] = None,
                                        target_field: Optional[str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableElasticsearchIngestProcessorJoinResult:
    """
    Joins each element of an array into a single string using a separator character between each element. Throws an error when the field is not an array.

    See: https://www.elastic.co/guide/en/elasticsearch/reference/current/join-processor.html

    ## Example Usage

    ```python
    import pulumi
    import pulumi_elasticstack as elasticstack

    join = elasticstack.elasticsearch_ingest_processor_join(field="joined_array_field",
        separator="-")
    my_ingest_pipeline = elasticstack.ElasticsearchIngestPipeline("myIngestPipeline", processors=[join.json])
    ```


    :param str description: Description of the processor.
    :param str field: Field containing array values to join.
    :param str if_: Conditionally execute the processor
    :param bool ignore_failure: Ignore failures for the processor.
    :param Sequence[str] on_failures: Handle failures for the processor.
    :param str separator: The separator character.
    :param str tag: Identifier for the processor.
    :param str target_field: The field to assign the converted value to, by default `field` is updated in-place.
    """
    __args__ = dict()
    __args__['description'] = description
    __args__['field'] = field
    __args__['if'] = if_
    __args__['ignoreFailure'] = ignore_failure
    __args__['onFailures'] = on_failures
    __args__['separator'] = separator
    __args__['tag'] = tag
    __args__['targetField'] = target_field
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('elasticstack:index/elasticsearchIngestProcessorJoin:ElasticsearchIngestProcessorJoin', __args__, opts=opts, typ=ElasticsearchIngestProcessorJoinResult).value

    return AwaitableElasticsearchIngestProcessorJoinResult(
        description=__ret__.description,
        field=__ret__.field,
        id=__ret__.id,
        if_=__ret__.if_,
        ignore_failure=__ret__.ignore_failure,
        json=__ret__.json,
        on_failures=__ret__.on_failures,
        separator=__ret__.separator,
        tag=__ret__.tag,
        target_field=__ret__.target_field)


@_utilities.lift_output_func(elasticsearch_ingest_processor_join)
def elasticsearch_ingest_processor_join_output(description: Optional[pulumi.Input[Optional[str]]] = None,
                                               field: Optional[pulumi.Input[str]] = None,
                                               if_: Optional[pulumi.Input[Optional[str]]] = None,
                                               ignore_failure: Optional[pulumi.Input[Optional[bool]]] = None,
                                               on_failures: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                               separator: Optional[pulumi.Input[str]] = None,
                                               tag: Optional[pulumi.Input[Optional[str]]] = None,
                                               target_field: Optional[pulumi.Input[Optional[str]]] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ElasticsearchIngestProcessorJoinResult]:
    """
    Joins each element of an array into a single string using a separator character between each element. Throws an error when the field is not an array.

    See: https://www.elastic.co/guide/en/elasticsearch/reference/current/join-processor.html

    ## Example Usage

    ```python
    import pulumi
    import pulumi_elasticstack as elasticstack

    join = elasticstack.elasticsearch_ingest_processor_join(field="joined_array_field",
        separator="-")
    my_ingest_pipeline = elasticstack.ElasticsearchIngestPipeline("myIngestPipeline", processors=[join.json])
    ```


    :param str description: Description of the processor.
    :param str field: Field containing array values to join.
    :param str if_: Conditionally execute the processor
    :param bool ignore_failure: Ignore failures for the processor.
    :param Sequence[str] on_failures: Handle failures for the processor.
    :param str separator: The separator character.
    :param str tag: Identifier for the processor.
    :param str target_field: The field to assign the converted value to, by default `field` is updated in-place.
    """
    ...
