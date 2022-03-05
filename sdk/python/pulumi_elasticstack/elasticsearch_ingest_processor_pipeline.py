# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'ElasticsearchIngestProcessorPipelineResult',
    'AwaitableElasticsearchIngestProcessorPipelineResult',
    'elasticsearch_ingest_processor_pipeline',
    'elasticsearch_ingest_processor_pipeline_output',
]

@pulumi.output_type
class ElasticsearchIngestProcessorPipelineResult:
    """
    A collection of values returned by ElasticsearchIngestProcessorPipeline.
    """
    def __init__(__self__, description=None, id=None, if_=None, ignore_failure=None, json=None, name=None, on_failures=None, tag=None):
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
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
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
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the pipeline to execute.
        """
        return pulumi.get(self, "name")

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


class AwaitableElasticsearchIngestProcessorPipelineResult(ElasticsearchIngestProcessorPipelineResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ElasticsearchIngestProcessorPipelineResult(
            description=self.description,
            id=self.id,
            if_=self.if_,
            ignore_failure=self.ignore_failure,
            json=self.json,
            name=self.name,
            on_failures=self.on_failures,
            tag=self.tag)


def elasticsearch_ingest_processor_pipeline(description: Optional[str] = None,
                                            if_: Optional[str] = None,
                                            ignore_failure: Optional[bool] = None,
                                            name: Optional[str] = None,
                                            on_failures: Optional[Sequence[str]] = None,
                                            tag: Optional[str] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableElasticsearchIngestProcessorPipelineResult:
    """
    Executes another pipeline.

    The name of the current pipeline can be accessed from the `_ingest.pipeline` ingest metadata key.

    See: https://www.elastic.co/guide/en/elasticsearch/reference/current/pipeline-processor.html

    ## Example Usage

    ```python
    import pulumi
    import pulumi_elasticstack as elasticstack

    append_tags = elasticstack.elasticsearch_ingest_processor_append(field="tags",
        values=[
            "production",
            "{{{app}}}",
            "{{{owner}}}",
        ])
    pipeline_a = elasticstack.ElasticsearchIngestPipeline("pipelineA", processors=[append_tags.json])
    fingerprint = elasticstack.elasticsearch_ingest_processor_fingerprint(fields=["owner"])
    pipeline = elasticstack.elasticsearch_ingest_processor_pipeline_output(name=pipeline_a.name)
    pipeline_b = elasticstack.ElasticsearchIngestPipeline("pipelineB", processors=[
        pipeline.json,
        fingerprint.json,
    ])
    ```


    :param str description: Description of the processor.
    :param str if_: Conditionally execute the processor
    :param bool ignore_failure: Ignore failures for the processor.
    :param str name: The name of the pipeline to execute.
    :param Sequence[str] on_failures: Handle failures for the processor.
    :param str tag: Identifier for the processor.
    """
    __args__ = dict()
    __args__['description'] = description
    __args__['if'] = if_
    __args__['ignoreFailure'] = ignore_failure
    __args__['name'] = name
    __args__['onFailures'] = on_failures
    __args__['tag'] = tag
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('elasticstack:index/elasticsearchIngestProcessorPipeline:ElasticsearchIngestProcessorPipeline', __args__, opts=opts, typ=ElasticsearchIngestProcessorPipelineResult).value

    return AwaitableElasticsearchIngestProcessorPipelineResult(
        description=__ret__.description,
        id=__ret__.id,
        if_=__ret__.if_,
        ignore_failure=__ret__.ignore_failure,
        json=__ret__.json,
        name=__ret__.name,
        on_failures=__ret__.on_failures,
        tag=__ret__.tag)


@_utilities.lift_output_func(elasticsearch_ingest_processor_pipeline)
def elasticsearch_ingest_processor_pipeline_output(description: Optional[pulumi.Input[Optional[str]]] = None,
                                                   if_: Optional[pulumi.Input[Optional[str]]] = None,
                                                   ignore_failure: Optional[pulumi.Input[Optional[bool]]] = None,
                                                   name: Optional[pulumi.Input[str]] = None,
                                                   on_failures: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                                   tag: Optional[pulumi.Input[Optional[str]]] = None,
                                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ElasticsearchIngestProcessorPipelineResult]:
    """
    Executes another pipeline.

    The name of the current pipeline can be accessed from the `_ingest.pipeline` ingest metadata key.

    See: https://www.elastic.co/guide/en/elasticsearch/reference/current/pipeline-processor.html

    ## Example Usage

    ```python
    import pulumi
    import pulumi_elasticstack as elasticstack

    append_tags = elasticstack.elasticsearch_ingest_processor_append(field="tags",
        values=[
            "production",
            "{{{app}}}",
            "{{{owner}}}",
        ])
    pipeline_a = elasticstack.ElasticsearchIngestPipeline("pipelineA", processors=[append_tags.json])
    fingerprint = elasticstack.elasticsearch_ingest_processor_fingerprint(fields=["owner"])
    pipeline = elasticstack.elasticsearch_ingest_processor_pipeline_output(name=pipeline_a.name)
    pipeline_b = elasticstack.ElasticsearchIngestPipeline("pipelineB", processors=[
        pipeline.json,
        fingerprint.json,
    ])
    ```


    :param str description: Description of the processor.
    :param str if_: Conditionally execute the processor
    :param bool ignore_failure: Ignore failures for the processor.
    :param str name: The name of the pipeline to execute.
    :param Sequence[str] on_failures: Handle failures for the processor.
    :param str tag: Identifier for the processor.
    """
    ...
