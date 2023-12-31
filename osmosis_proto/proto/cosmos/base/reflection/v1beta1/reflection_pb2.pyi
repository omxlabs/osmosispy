"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ListAllInterfacesRequest(google.protobuf.message.Message):
    """ListAllInterfacesRequest is the request type of the ListAllInterfaces RPC."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ListAllInterfacesRequest = ListAllInterfacesRequest

class ListAllInterfacesResponse(google.protobuf.message.Message):
    """ListAllInterfacesResponse is the response type of the ListAllInterfaces RPC."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INTERFACE_NAMES_FIELD_NUMBER: builtins.int
    @property
    def interface_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """interface_names is an array of all the registered interfaces."""
    def __init__(
        self,
        *,
        interface_names: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["interface_names", b"interface_names"]) -> None: ...

global___ListAllInterfacesResponse = ListAllInterfacesResponse

class ListImplementationsRequest(google.protobuf.message.Message):
    """ListImplementationsRequest is the request type of the ListImplementations
    RPC.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INTERFACE_NAME_FIELD_NUMBER: builtins.int
    interface_name: builtins.str
    """interface_name defines the interface to query the implementations for."""
    def __init__(
        self,
        *,
        interface_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["interface_name", b"interface_name"]) -> None: ...

global___ListImplementationsRequest = ListImplementationsRequest

class ListImplementationsResponse(google.protobuf.message.Message):
    """ListImplementationsResponse is the response type of the ListImplementations
    RPC.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IMPLEMENTATION_MESSAGE_NAMES_FIELD_NUMBER: builtins.int
    @property
    def implementation_message_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        implementation_message_names: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["implementation_message_names", b"implementation_message_names"]) -> None: ...

global___ListImplementationsResponse = ListImplementationsResponse
