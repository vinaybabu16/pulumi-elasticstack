# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'ElasticsearchIngestProcessorForeachResult',
    'AwaitableElasticsearchIngestProcessorForeachResult',
    'elasticsearch_ingest_processor_foreach',
    'elasticsearch_ingest_processor_foreach_output',
]

@pulumi.output_type
class ElasticsearchIngestProcessorForeachResult:
    """
    A collection of values returned by ElasticsearchIngestProcessorForeach.
    """
    def __init__(__self__, description=None, field=None, id=None, if_=None, ignore_failure=None, ignore_missing=None, json=None, on_failures=None, processor=None, tag=None):
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
        if ignore_missing and not isinstance(ignore_missing, bool):
            raise TypeError("Expected argument 'ignore_missing' to be a bool")
        pulumi.set(__self__, "ignore_missing", ignore_missing)
        if json and not isinstance(json, str):
            raise TypeError("Expected argument 'json' to be a str")
        pulumi.set(__self__, "json", json)
        if on_failures and not isinstance(on_failures, list):
            raise TypeError("Expected argument 'on_failures' to be a list")
        pulumi.set(__self__, "on_failures", on_failures)
        if processor and not isinstance(processor, str):
            raise TypeError("Expected argument 'processor' to be a str")
        pulumi.set(__self__, "processor", processor)
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
    def field(self) -> str:
        """
        Field containing array or object values.
        """
        return pulumi.get(self, "field")

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
    @pulumi.getter(name="ignoreMissing")
    def ignore_missing(self) -> Optional[bool]:
        """
        If `true`, the processor silently exits without changing the document if the `field` is `null` or missing.
        """
        return pulumi.get(self, "ignore_missing")

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
    def processor(self) -> str:
        """
        Ingest processor to run on each element.
        """
        return pulumi.get(self, "processor")

    @property
    @pulumi.getter
    def tag(self) -> Optional[str]:
        """
        Identifier for the processor.
        """
        return pulumi.get(self, "tag")


class AwaitableElasticsearchIngestProcessorForeachResult(ElasticsearchIngestProcessorForeachResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ElasticsearchIngestProcessorForeachResult(
            description=self.description,
            field=self.field,
            id=self.id,
            if_=self.if_,
            ignore_failure=self.ignore_failure,
            ignore_missing=self.ignore_missing,
            json=self.json,
            on_failures=self.on_failures,
            processor=self.processor,
            tag=self.tag)


def elasticsearch_ingest_processor_foreach(description: Optional[str] = None,
                                           field: Optional[str] = None,
                                           if_: Optional[str] = None,
                                           ignore_failure: Optional[bool] = None,
                                           ignore_missing: Optional[bool] = None,
                                           on_failures: Optional[Sequence[str]] = None,
                                           processor: Optional[str] = None,
                                           tag: Optional[str] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableElasticsearchIngestProcessorForeachResult:
    """
    Runs an ingest processor on each element of an array or object.

    All ingest processors can run on array or object elements. However, if the number of elements is unknown, it can be cumbersome to process each one in the same way.

    The `foreach` processor lets you specify a `field` containing array or object values and a `processor` to run on each element in the field.

    See: https://www.elastic.co/guide/en/elasticsearch/reference/current/foreach-processor.html

    ## Example Usage

    ```python
    import pulumi
    import pulumi_elasticstack as elasticstack

    convert = elasticstack.elasticsearch_ingest_processor_convert(field="_ingest._value",
        type="integer")
    foreach = elasticstack.elasticsearch_ingest_processor_foreach(field="values",
        processor=convert.json)
    my_ingest_pipeline = elasticstack.ElasticsearchIngestPipeline("myIngestPipeline", processors=[foreach.json])
    ```


    :param str description: Description of the processor.
    :param str field: Field containing array or object values.
    :param str if_: Conditionally execute the processor
    :param bool ignore_failure: Ignore failures for the processor.
    :param bool ignore_missing: If `true`, the processor silently exits without changing the document if the `field` is `null` or missing.
    :param Sequence[str] on_failures: Handle failures for the processor.
    :param str processor: Ingest processor to run on each element.
    :param str tag: Identifier for the processor.
    """
    __args__ = dict()
    __args__['description'] = description
    __args__['field'] = field
    __args__['if'] = if_
    __args__['ignoreFailure'] = ignore_failure
    __args__['ignoreMissing'] = ignore_missing
    __args__['onFailures'] = on_failures
    __args__['processor'] = processor
    __args__['tag'] = tag
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('elasticstack:index/elasticsearchIngestProcessorForeach:ElasticsearchIngestProcessorForeach', __args__, opts=opts, typ=ElasticsearchIngestProcessorForeachResult).value

    return AwaitableElasticsearchIngestProcessorForeachResult(
        description=__ret__.description,
        field=__ret__.field,
        id=__ret__.id,
        if_=__ret__.if_,
        ignore_failure=__ret__.ignore_failure,
        ignore_missing=__ret__.ignore_missing,
        json=__ret__.json,
        on_failures=__ret__.on_failures,
        processor=__ret__.processor,
        tag=__ret__.tag)


@_utilities.lift_output_func(elasticsearch_ingest_processor_foreach)
def elasticsearch_ingest_processor_foreach_output(description: Optional[pulumi.Input[Optional[str]]] = None,
                                                  field: Optional[pulumi.Input[str]] = None,
                                                  if_: Optional[pulumi.Input[Optional[str]]] = None,
                                                  ignore_failure: Optional[pulumi.Input[Optional[bool]]] = None,
                                                  ignore_missing: Optional[pulumi.Input[Optional[bool]]] = None,
                                                  on_failures: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                                  processor: Optional[pulumi.Input[str]] = None,
                                                  tag: Optional[pulumi.Input[Optional[str]]] = None,
                                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ElasticsearchIngestProcessorForeachResult]:
    """
    Runs an ingest processor on each element of an array or object.

    All ingest processors can run on array or object elements. However, if the number of elements is unknown, it can be cumbersome to process each one in the same way.

    The `foreach` processor lets you specify a `field` containing array or object values and a `processor` to run on each element in the field.

    See: https://www.elastic.co/guide/en/elasticsearch/reference/current/foreach-processor.html

    ## Example Usage

    ```python
    import pulumi
    import pulumi_elasticstack as elasticstack

    convert = elasticstack.elasticsearch_ingest_processor_convert(field="_ingest._value",
        type="integer")
    foreach = elasticstack.elasticsearch_ingest_processor_foreach(field="values",
        processor=convert.json)
    my_ingest_pipeline = elasticstack.ElasticsearchIngestPipeline("myIngestPipeline", processors=[foreach.json])
    ```


    :param str description: Description of the processor.
    :param str field: Field containing array or object values.
    :param str if_: Conditionally execute the processor
    :param bool ignore_failure: Ignore failures for the processor.
    :param bool ignore_missing: If `true`, the processor silently exits without changing the document if the `field` is `null` or missing.
    :param Sequence[str] on_failures: Handle failures for the processor.
    :param str processor: Ingest processor to run on each element.
    :param str tag: Identifier for the processor.
    """
    ...
