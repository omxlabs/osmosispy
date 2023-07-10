"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.mint.v1beta1.mint_pb2
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class QueryParamsRequest(google.protobuf.message.Message):
    """QueryParamsRequest is the request type for the Query/Params RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QueryParamsRequest = QueryParamsRequest

class QueryParamsResponse(google.protobuf.message.Message):
    """QueryParamsResponse is the response type for the Query/Params RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMS_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> cosmos.mint.v1beta1.mint_pb2.Params:
        """params defines the parameters of the module."""
    def __init__(
        self,
        *,
        params: cosmos.mint.v1beta1.mint_pb2.Params | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["params", b"params"]) -> None: ...

global___QueryParamsResponse = QueryParamsResponse

class QueryInflationRequest(google.protobuf.message.Message):
    """QueryInflationRequest is the request type for the Query/Inflation RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QueryInflationRequest = QueryInflationRequest

class QueryInflationResponse(google.protobuf.message.Message):
    """QueryInflationResponse is the response type for the Query/Inflation RPC
    method.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INFLATION_FIELD_NUMBER: builtins.int
    inflation: builtins.bytes
    """inflation is the current minting inflation value."""
    def __init__(
        self,
        *,
        inflation: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["inflation", b"inflation"]) -> None: ...

global___QueryInflationResponse = QueryInflationResponse

class QueryAnnualProvisionsRequest(google.protobuf.message.Message):
    """QueryAnnualProvisionsRequest is the request type for the
    Query/AnnualProvisions RPC method.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QueryAnnualProvisionsRequest = QueryAnnualProvisionsRequest

class QueryAnnualProvisionsResponse(google.protobuf.message.Message):
    """QueryAnnualProvisionsResponse is the response type for the
    Query/AnnualProvisions RPC method.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ANNUAL_PROVISIONS_FIELD_NUMBER: builtins.int
    annual_provisions: builtins.bytes
    """annual_provisions is the current minting annual provisions value."""
    def __init__(
        self,
        *,
        annual_provisions: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["annual_provisions", b"annual_provisions"]) -> None: ...

global___QueryAnnualProvisionsResponse = QueryAnnualProvisionsResponse
