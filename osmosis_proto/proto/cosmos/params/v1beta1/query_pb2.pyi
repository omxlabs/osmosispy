"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.params.v1beta1.params_pb2
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class QueryParamsRequest(google.protobuf.message.Message):
    """QueryParamsRequest is request type for the Query/Params RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBSPACE_FIELD_NUMBER: builtins.int
    KEY_FIELD_NUMBER: builtins.int
    subspace: builtins.str
    """subspace defines the module to query the parameter for."""
    key: builtins.str
    """key defines the key of the parameter in the subspace."""
    def __init__(
        self,
        *,
        subspace: builtins.str = ...,
        key: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "subspace", b"subspace"]) -> None: ...

global___QueryParamsRequest = QueryParamsRequest

class QueryParamsResponse(google.protobuf.message.Message):
    """QueryParamsResponse is response type for the Query/Params RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAM_FIELD_NUMBER: builtins.int
    @property
    def param(self) -> cosmos.params.v1beta1.params_pb2.ParamChange:
        """param defines the queried parameter."""
    def __init__(
        self,
        *,
        param: cosmos.params.v1beta1.params_pb2.ParamChange | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["param", b"param"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["param", b"param"]) -> None: ...

global___QueryParamsResponse = QueryParamsResponse
