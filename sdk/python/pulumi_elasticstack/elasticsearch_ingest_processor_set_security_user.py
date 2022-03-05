# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'ElasticsearchIngestProcessorSetSecurityUserResult',
    'AwaitableElasticsearchIngestProcessorSetSecurityUserResult',
    'elasticsearch_ingest_processor_set_security_user',
    'elasticsearch_ingest_processor_set_security_user_output',
]

@pulumi.output_type
class ElasticsearchIngestProcessorSetSecurityUserResult:
    """
    A collection of values returned by ElasticsearchIngestProcessorSetSecurityUser.
    """
    def __init__(__self__, description=None, field=None, id=None, if_=None, ignore_failure=None, json=None, on_failures=None, properties=None, tag=None):
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
        if properties and not isinstance(properties, list):
            raise TypeError("Expected argument 'properties' to be a list")
        pulumi.set(__self__, "properties", properties)
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
        The field to store the user information into.
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
    def properties(self) -> Optional[Sequence[str]]:
        """
        Controls what user related properties are added to the `field`.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def tag(self) -> Optional[str]:
        """
        Identifier for the processor.
        """
        return pulumi.get(self, "tag")


class AwaitableElasticsearchIngestProcessorSetSecurityUserResult(ElasticsearchIngestProcessorSetSecurityUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ElasticsearchIngestProcessorSetSecurityUserResult(
            description=self.description,
            field=self.field,
            id=self.id,
            if_=self.if_,
            ignore_failure=self.ignore_failure,
            json=self.json,
            on_failures=self.on_failures,
            properties=self.properties,
            tag=self.tag)


def elasticsearch_ingest_processor_set_security_user(description: Optional[str] = None,
                                                     field: Optional[str] = None,
                                                     if_: Optional[str] = None,
                                                     ignore_failure: Optional[bool] = None,
                                                     on_failures: Optional[Sequence[str]] = None,
                                                     properties: Optional[Sequence[str]] = None,
                                                     tag: Optional[str] = None,
                                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableElasticsearchIngestProcessorSetSecurityUserResult:
    """
    Sets user-related details (such as `username`, `roles`, `email`, `full_name`, `metadata`, `api_key`, `realm` and `authentication_typ`e) from the current authenticated user to the current document by pre-processing the ingest. The `api_key` property exists only if the user authenticates with an API key. It is an object containing the id, name and metadata (if it exists and is non-empty) fields of the API key. The realm property is also an object with two fields, name and type. When using API key authentication, the realm property refers to the realm from which the API key is created. The `authentication_type property` is a string that can take value from `REALM`, `API_KEY`, `TOKEN` and `ANONYMOUS`.

    See: https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest-node-set-security-user-processor.html

    ## Example Usage

    ```python
    import pulumi
    import pulumi_elasticstack as elasticstack

    user = elasticstack.elasticsearch_ingest_processor_set_security_user(field="user",
        properties=[
            "username",
            "realm",
        ])
    my_ingest_pipeline = elasticstack.ElasticsearchIngestPipeline("myIngestPipeline", processors=[user.json])
    ```


    :param str description: Description of the processor.
    :param str field: The field to store the user information into.
    :param str if_: Conditionally execute the processor
    :param bool ignore_failure: Ignore failures for the processor.
    :param Sequence[str] on_failures: Handle failures for the processor.
    :param Sequence[str] properties: Controls what user related properties are added to the `field`.
    :param str tag: Identifier for the processor.
    """
    __args__ = dict()
    __args__['description'] = description
    __args__['field'] = field
    __args__['if'] = if_
    __args__['ignoreFailure'] = ignore_failure
    __args__['onFailures'] = on_failures
    __args__['properties'] = properties
    __args__['tag'] = tag
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('elasticstack:index/elasticsearchIngestProcessorSetSecurityUser:ElasticsearchIngestProcessorSetSecurityUser', __args__, opts=opts, typ=ElasticsearchIngestProcessorSetSecurityUserResult).value

    return AwaitableElasticsearchIngestProcessorSetSecurityUserResult(
        description=__ret__.description,
        field=__ret__.field,
        id=__ret__.id,
        if_=__ret__.if_,
        ignore_failure=__ret__.ignore_failure,
        json=__ret__.json,
        on_failures=__ret__.on_failures,
        properties=__ret__.properties,
        tag=__ret__.tag)


@_utilities.lift_output_func(elasticsearch_ingest_processor_set_security_user)
def elasticsearch_ingest_processor_set_security_user_output(description: Optional[pulumi.Input[Optional[str]]] = None,
                                                            field: Optional[pulumi.Input[str]] = None,
                                                            if_: Optional[pulumi.Input[Optional[str]]] = None,
                                                            ignore_failure: Optional[pulumi.Input[Optional[bool]]] = None,
                                                            on_failures: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                                            properties: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                                            tag: Optional[pulumi.Input[Optional[str]]] = None,
                                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ElasticsearchIngestProcessorSetSecurityUserResult]:
    """
    Sets user-related details (such as `username`, `roles`, `email`, `full_name`, `metadata`, `api_key`, `realm` and `authentication_typ`e) from the current authenticated user to the current document by pre-processing the ingest. The `api_key` property exists only if the user authenticates with an API key. It is an object containing the id, name and metadata (if it exists and is non-empty) fields of the API key. The realm property is also an object with two fields, name and type. When using API key authentication, the realm property refers to the realm from which the API key is created. The `authentication_type property` is a string that can take value from `REALM`, `API_KEY`, `TOKEN` and `ANONYMOUS`.

    See: https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest-node-set-security-user-processor.html

    ## Example Usage

    ```python
    import pulumi
    import pulumi_elasticstack as elasticstack

    user = elasticstack.elasticsearch_ingest_processor_set_security_user(field="user",
        properties=[
            "username",
            "realm",
        ])
    my_ingest_pipeline = elasticstack.ElasticsearchIngestPipeline("myIngestPipeline", processors=[user.json])
    ```


    :param str description: Description of the processor.
    :param str field: The field to store the user information into.
    :param str if_: Conditionally execute the processor
    :param bool ignore_failure: Ignore failures for the processor.
    :param Sequence[str] on_failures: Handle failures for the processor.
    :param Sequence[str] properties: Controls what user related properties are added to the `field`.
    :param str tag: Identifier for the processor.
    """
    ...
