# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'ElasticsearchIngestProcessorFailResult',
    'AwaitableElasticsearchIngestProcessorFailResult',
    'elasticsearch_ingest_processor_fail',
    'elasticsearch_ingest_processor_fail_output',
]

@pulumi.output_type
class ElasticsearchIngestProcessorFailResult:
    """
    A collection of values returned by ElasticsearchIngestProcessorFail.
    """
    def __init__(__self__, description=None, id=None, if_=None, ignore_failure=None, json=None, message=None, on_failures=None, tag=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
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
        if message and not isinstance(message, str):
            raise TypeError("Expected argument 'message' to be a str")
        pulumi.set(__self__, "message", message)
        if on_failures and not isinstance(on_failures, list):
            raise TypeError("Expected argument 'on_failures' to be a list")
        pulumi.set(__self__, "on_failures", on_failures)
        if tag and not isinstance(tag, str):
            raise TypeError("Expected argument 'tag' to be a str")
        pulumi.set(__self__, "tag", tag)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of the processor.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Internal identifier of the resource
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
    @pulumi.getter
    def message(self) -> str:
        """
        The error message thrown by the processor.
        """
        return pulumi.get(self, "message")

    @property
    @pulumi.getter(name="onFailures")
    def on_failures(self) -> Optional[Sequence[str]]:
        """
        Handle failures for the processor.
        """
        return pulumi.get(self, "on_failures")

    @property
    @pulumi.getter
    def tag(self) -> Optional[str]:
        """
        Identifier for the processor.
        """
        return pulumi.get(self, "tag")


class AwaitableElasticsearchIngestProcessorFailResult(ElasticsearchIngestProcessorFailResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ElasticsearchIngestProcessorFailResult(
            description=self.description,
            id=self.id,
            if_=self.if_,
            ignore_failure=self.ignore_failure,
            json=self.json,
            message=self.message,
            on_failures=self.on_failures,
            tag=self.tag)


def elasticsearch_ingest_processor_fail(description: Optional[str] = None,
                                        if_: Optional[str] = None,
                                        ignore_failure: Optional[bool] = None,
                                        message: Optional[str] = None,
                                        on_failures: Optional[Sequence[str]] = None,
                                        tag: Optional[str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableElasticsearchIngestProcessorFailResult:
    """
    Raises an exception. This is useful for when you expect a pipeline to fail and want to relay a specific message to the requester.

    See: https://www.elastic.co/guide/en/elasticsearch/reference/current/fail-processor.html

    ## Example Usage

    ```python
    import pulumi
    import pulumi_elasticstack as elasticstack

    fail = elasticstack.elasticsearch_ingest_processor_fail(if_="ctx.tags.contains('production') != true",
        message="The production tag is not present, found tags: {{{tags}}}")
    my_ingest_pipeline = elasticstack.ElasticsearchIngestPipeline("myIngestPipeline", processors=[fail.json])
    ```


    :param str description: Description of the processor.
    :param str if_: Conditionally execute the processor
    :param bool ignore_failure: Ignore failures for the processor.
    :param str message: The error message thrown by the processor.
    :param Sequence[str] on_failures: Handle failures for the processor.
    :param str tag: Identifier for the processor.
    """
    __args__ = dict()
    __args__['description'] = description
    __args__['if'] = if_
    __args__['ignoreFailure'] = ignore_failure
    __args__['message'] = message
    __args__['onFailures'] = on_failures
    __args__['tag'] = tag
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('elasticstack:index/elasticsearchIngestProcessorFail:ElasticsearchIngestProcessorFail', __args__, opts=opts, typ=ElasticsearchIngestProcessorFailResult).value

    return AwaitableElasticsearchIngestProcessorFailResult(
        description=__ret__.description,
        id=__ret__.id,
        if_=__ret__.if_,
        ignore_failure=__ret__.ignore_failure,
        json=__ret__.json,
        message=__ret__.message,
        on_failures=__ret__.on_failures,
        tag=__ret__.tag)


@_utilities.lift_output_func(elasticsearch_ingest_processor_fail)
def elasticsearch_ingest_processor_fail_output(description: Optional[pulumi.Input[Optional[str]]] = None,
                                               if_: Optional[pulumi.Input[Optional[str]]] = None,
                                               ignore_failure: Optional[pulumi.Input[Optional[bool]]] = None,
                                               message: Optional[pulumi.Input[str]] = None,
                                               on_failures: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                               tag: Optional[pulumi.Input[Optional[str]]] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ElasticsearchIngestProcessorFailResult]:
    """
    Raises an exception. This is useful for when you expect a pipeline to fail and want to relay a specific message to the requester.

    See: https://www.elastic.co/guide/en/elasticsearch/reference/current/fail-processor.html

    ## Example Usage

    ```python
    import pulumi
    import pulumi_elasticstack as elasticstack

    fail = elasticstack.elasticsearch_ingest_processor_fail(if_="ctx.tags.contains('production') != true",
        message="The production tag is not present, found tags: {{{tags}}}")
    my_ingest_pipeline = elasticstack.ElasticsearchIngestPipeline("myIngestPipeline", processors=[fail.json])
    ```


    :param str description: Description of the processor.
    :param str if_: Conditionally execute the processor
    :param bool ignore_failure: Ignore failures for the processor.
    :param str message: The error message thrown by the processor.
    :param Sequence[str] on_failures: Handle failures for the processor.
    :param str tag: Identifier for the processor.
    """
    ...
