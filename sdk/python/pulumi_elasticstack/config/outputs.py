# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'Elasticsearch',
]

@pulumi.output_type
class Elasticsearch(dict):
    def __init__(__self__, *,
                 ca_file: Optional[str] = None,
                 endpoints: Optional[Sequence[str]] = None,
                 insecure: Optional[bool] = None,
                 password: Optional[str] = None,
                 username: Optional[str] = None):
        if ca_file is not None:
            pulumi.set(__self__, "ca_file", ca_file)
        if endpoints is not None:
            pulumi.set(__self__, "endpoints", endpoints)
        if insecure is not None:
            pulumi.set(__self__, "insecure", insecure)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="caFile")
    def ca_file(self) -> Optional[str]:
        return pulumi.get(self, "ca_file")

    @property
    @pulumi.getter
    def endpoints(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter
    def insecure(self) -> Optional[bool]:
        return pulumi.get(self, "insecure")

    @property
    @pulumi.getter
    def password(self) -> Optional[str]:
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def username(self) -> Optional[str]:
        return pulumi.get(self, "username")


