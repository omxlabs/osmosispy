"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import osmosis.txfees.v1beta1.feetoken_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class QueryFeeTokensRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QueryFeeTokensRequest = QueryFeeTokensRequest

class QueryFeeTokensResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEE_TOKENS_FIELD_NUMBER: builtins.int
    @property
    def fee_tokens(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.txfees.v1beta1.feetoken_pb2.FeeToken]: ...
    def __init__(
        self,
        *,
        fee_tokens: collections.abc.Iterable[osmosis.txfees.v1beta1.feetoken_pb2.FeeToken] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["fee_tokens", b"fee_tokens"]) -> None: ...

global___QueryFeeTokensResponse = QueryFeeTokensResponse

class QueryDenomSpotPriceRequest(google.protobuf.message.Message):
    """QueryDenomSpotPriceRequest defines grpc request structure for querying spot
    price for the specified tx fee denom
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DENOM_FIELD_NUMBER: builtins.int
    denom: builtins.str
    def __init__(
        self,
        *,
        denom: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["denom", b"denom"]) -> None: ...

global___QueryDenomSpotPriceRequest = QueryDenomSpotPriceRequest

class QueryDenomSpotPriceResponse(google.protobuf.message.Message):
    """QueryDenomSpotPriceRequest defines grpc response structure for querying spot
    price for the specified tx fee denom
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOLID_FIELD_NUMBER: builtins.int
    SPOT_PRICE_FIELD_NUMBER: builtins.int
    poolID: builtins.int
    spot_price: builtins.str
    def __init__(
        self,
        *,
        poolID: builtins.int = ...,
        spot_price: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["poolID", b"poolID", "spot_price", b"spot_price"]) -> None: ...

global___QueryDenomSpotPriceResponse = QueryDenomSpotPriceResponse

class QueryDenomPoolIdRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DENOM_FIELD_NUMBER: builtins.int
    denom: builtins.str
    def __init__(
        self,
        *,
        denom: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["denom", b"denom"]) -> None: ...

global___QueryDenomPoolIdRequest = QueryDenomPoolIdRequest

class QueryDenomPoolIdResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOLID_FIELD_NUMBER: builtins.int
    poolID: builtins.int
    def __init__(
        self,
        *,
        poolID: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["poolID", b"poolID"]) -> None: ...

global___QueryDenomPoolIdResponse = QueryDenomPoolIdResponse

class QueryBaseDenomRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QueryBaseDenomRequest = QueryBaseDenomRequest

class QueryBaseDenomResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASE_DENOM_FIELD_NUMBER: builtins.int
    base_denom: builtins.str
    def __init__(
        self,
        *,
        base_denom: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["base_denom", b"base_denom"]) -> None: ...

global___QueryBaseDenomResponse = QueryBaseDenomResponse
