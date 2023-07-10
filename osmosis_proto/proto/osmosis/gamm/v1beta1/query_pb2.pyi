"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import cosmos.base.query.v1beta1.pagination_pb2
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import osmosis.gamm.v1beta1.tx_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class QueryPoolRequest(google.protobuf.message.Message):
    """=============================== Pool"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOL_ID_FIELD_NUMBER: builtins.int
    pool_id: builtins.int
    def __init__(
        self,
        *,
        pool_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pool_id", b"pool_id"]) -> None: ...

global___QueryPoolRequest = QueryPoolRequest

class QueryPoolResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOL_FIELD_NUMBER: builtins.int
    @property
    def pool(self) -> google.protobuf.any_pb2.Any: ...
    def __init__(
        self,
        *,
        pool: google.protobuf.any_pb2.Any | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pool", b"pool"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["pool", b"pool"]) -> None: ...

global___QueryPoolResponse = QueryPoolResponse

class QueryPoolsRequest(google.protobuf.message.Message):
    """=============================== Pools"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest:
        """pagination defines an optional pagination for the request."""
    def __init__(
        self,
        *,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> None: ...

global___QueryPoolsRequest = QueryPoolsRequest

class QueryPoolsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOLS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def pools(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.any_pb2.Any]: ...
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse:
        """pagination defines the pagination in the response."""
    def __init__(
        self,
        *,
        pools: collections.abc.Iterable[google.protobuf.any_pb2.Any] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["pagination", b"pagination", "pools", b"pools"]) -> None: ...

global___QueryPoolsResponse = QueryPoolsResponse

class QueryNumPoolsRequest(google.protobuf.message.Message):
    """=============================== NumPools"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QueryNumPoolsRequest = QueryNumPoolsRequest

class QueryNumPoolsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NUM_POOLS_FIELD_NUMBER: builtins.int
    num_pools: builtins.int
    def __init__(
        self,
        *,
        num_pools: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["num_pools", b"num_pools"]) -> None: ...

global___QueryNumPoolsResponse = QueryNumPoolsResponse

class QueryPoolTypeRequest(google.protobuf.message.Message):
    """=============================== PoolType"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOL_ID_FIELD_NUMBER: builtins.int
    pool_id: builtins.int
    def __init__(
        self,
        *,
        pool_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pool_id", b"pool_id"]) -> None: ...

global___QueryPoolTypeRequest = QueryPoolTypeRequest

class QueryPoolTypeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOL_TYPE_FIELD_NUMBER: builtins.int
    pool_type: builtins.str
    def __init__(
        self,
        *,
        pool_type: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pool_type", b"pool_type"]) -> None: ...

global___QueryPoolTypeResponse = QueryPoolTypeResponse

class QueryCalcJoinPoolSharesRequest(google.protobuf.message.Message):
    """=============================== CalcJoinPoolShares"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOL_ID_FIELD_NUMBER: builtins.int
    TOKENS_IN_FIELD_NUMBER: builtins.int
    pool_id: builtins.int
    @property
    def tokens_in(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(
        self,
        *,
        pool_id: builtins.int = ...,
        tokens_in: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pool_id", b"pool_id", "tokens_in", b"tokens_in"]) -> None: ...

global___QueryCalcJoinPoolSharesRequest = QueryCalcJoinPoolSharesRequest

class QueryCalcJoinPoolSharesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SHARE_OUT_AMOUNT_FIELD_NUMBER: builtins.int
    TOKENS_OUT_FIELD_NUMBER: builtins.int
    share_out_amount: builtins.str
    @property
    def tokens_out(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(
        self,
        *,
        share_out_amount: builtins.str = ...,
        tokens_out: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["share_out_amount", b"share_out_amount", "tokens_out", b"tokens_out"]) -> None: ...

global___QueryCalcJoinPoolSharesResponse = QueryCalcJoinPoolSharesResponse

class QueryCalcExitPoolCoinsFromSharesRequest(google.protobuf.message.Message):
    """=============================== CalcExitPoolCoinsFromShares"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOL_ID_FIELD_NUMBER: builtins.int
    SHARE_IN_AMOUNT_FIELD_NUMBER: builtins.int
    pool_id: builtins.int
    share_in_amount: builtins.str
    def __init__(
        self,
        *,
        pool_id: builtins.int = ...,
        share_in_amount: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pool_id", b"pool_id", "share_in_amount", b"share_in_amount"]) -> None: ...

global___QueryCalcExitPoolCoinsFromSharesRequest = QueryCalcExitPoolCoinsFromSharesRequest

class QueryCalcExitPoolCoinsFromSharesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOKENS_OUT_FIELD_NUMBER: builtins.int
    @property
    def tokens_out(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(
        self,
        *,
        tokens_out: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["tokens_out", b"tokens_out"]) -> None: ...

global___QueryCalcExitPoolCoinsFromSharesResponse = QueryCalcExitPoolCoinsFromSharesResponse

class QueryPoolParamsRequest(google.protobuf.message.Message):
    """=============================== PoolParams"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOL_ID_FIELD_NUMBER: builtins.int
    pool_id: builtins.int
    def __init__(
        self,
        *,
        pool_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pool_id", b"pool_id"]) -> None: ...

global___QueryPoolParamsRequest = QueryPoolParamsRequest

class QueryPoolParamsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMS_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> google.protobuf.any_pb2.Any: ...
    def __init__(
        self,
        *,
        params: google.protobuf.any_pb2.Any | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["params", b"params"]) -> None: ...

global___QueryPoolParamsResponse = QueryPoolParamsResponse

class QueryTotalPoolLiquidityRequest(google.protobuf.message.Message):
    """=============================== PoolLiquidity"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOL_ID_FIELD_NUMBER: builtins.int
    pool_id: builtins.int
    def __init__(
        self,
        *,
        pool_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pool_id", b"pool_id"]) -> None: ...

global___QueryTotalPoolLiquidityRequest = QueryTotalPoolLiquidityRequest

class QueryTotalPoolLiquidityResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIQUIDITY_FIELD_NUMBER: builtins.int
    @property
    def liquidity(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(
        self,
        *,
        liquidity: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["liquidity", b"liquidity"]) -> None: ...

global___QueryTotalPoolLiquidityResponse = QueryTotalPoolLiquidityResponse

class QueryTotalSharesRequest(google.protobuf.message.Message):
    """=============================== TotalShares"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOL_ID_FIELD_NUMBER: builtins.int
    pool_id: builtins.int
    def __init__(
        self,
        *,
        pool_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pool_id", b"pool_id"]) -> None: ...

global___QueryTotalSharesRequest = QueryTotalSharesRequest

class QueryTotalSharesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOTAL_SHARES_FIELD_NUMBER: builtins.int
    @property
    def total_shares(self) -> cosmos.base.v1beta1.coin_pb2.Coin: ...
    def __init__(
        self,
        *,
        total_shares: cosmos.base.v1beta1.coin_pb2.Coin | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["total_shares", b"total_shares"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["total_shares", b"total_shares"]) -> None: ...

global___QueryTotalSharesResponse = QueryTotalSharesResponse

class QueryCalcJoinPoolNoSwapSharesRequest(google.protobuf.message.Message):
    """=============================== CalcJoinPoolNoSwapShares"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOL_ID_FIELD_NUMBER: builtins.int
    TOKENS_IN_FIELD_NUMBER: builtins.int
    pool_id: builtins.int
    @property
    def tokens_in(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(
        self,
        *,
        pool_id: builtins.int = ...,
        tokens_in: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pool_id", b"pool_id", "tokens_in", b"tokens_in"]) -> None: ...

global___QueryCalcJoinPoolNoSwapSharesRequest = QueryCalcJoinPoolNoSwapSharesRequest

class QueryCalcJoinPoolNoSwapSharesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOKENS_OUT_FIELD_NUMBER: builtins.int
    SHARES_OUT_FIELD_NUMBER: builtins.int
    @property
    def tokens_out(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    shares_out: builtins.str
    def __init__(
        self,
        *,
        tokens_out: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
        shares_out: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["shares_out", b"shares_out", "tokens_out", b"tokens_out"]) -> None: ...

global___QueryCalcJoinPoolNoSwapSharesResponse = QueryCalcJoinPoolNoSwapSharesResponse

class QuerySpotPriceRequest(google.protobuf.message.Message):
    """QuerySpotPriceRequest defines the gRPC request structure for a SpotPrice
    query.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOL_ID_FIELD_NUMBER: builtins.int
    BASE_ASSET_DENOM_FIELD_NUMBER: builtins.int
    QUOTE_ASSET_DENOM_FIELD_NUMBER: builtins.int
    pool_id: builtins.int
    base_asset_denom: builtins.str
    quote_asset_denom: builtins.str
    def __init__(
        self,
        *,
        pool_id: builtins.int = ...,
        base_asset_denom: builtins.str = ...,
        quote_asset_denom: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["base_asset_denom", b"base_asset_denom", "pool_id", b"pool_id", "quote_asset_denom", b"quote_asset_denom"]) -> None: ...

global___QuerySpotPriceRequest = QuerySpotPriceRequest

class QueryPoolsWithFilterRequest(google.protobuf.message.Message):
    """=============================== PoolsWithFilter"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MIN_LIQUIDITY_FIELD_NUMBER: builtins.int
    POOL_TYPE_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    min_liquidity: builtins.str
    """String of the coins in single string seperated by comma. Ex)
    10uatom,100uosmo
    """
    pool_type: builtins.str
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...
    def __init__(
        self,
        *,
        min_liquidity: builtins.str = ...,
        pool_type: builtins.str = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["min_liquidity", b"min_liquidity", "pagination", b"pagination", "pool_type", b"pool_type"]) -> None: ...

global___QueryPoolsWithFilterRequest = QueryPoolsWithFilterRequest

class QueryPoolsWithFilterResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOLS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def pools(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.any_pb2.Any]: ...
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse:
        """pagination defines the pagination in the response."""
    def __init__(
        self,
        *,
        pools: collections.abc.Iterable[google.protobuf.any_pb2.Any] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["pagination", b"pagination", "pools", b"pools"]) -> None: ...

global___QueryPoolsWithFilterResponse = QueryPoolsWithFilterResponse

class QuerySpotPriceResponse(google.protobuf.message.Message):
    """QuerySpotPriceResponse defines the gRPC response structure for a SpotPrice
    query.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SPOT_PRICE_FIELD_NUMBER: builtins.int
    spot_price: builtins.str
    """String of the Dec. Ex) 10.203uatom"""
    def __init__(
        self,
        *,
        spot_price: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["spot_price", b"spot_price"]) -> None: ...

global___QuerySpotPriceResponse = QuerySpotPriceResponse

class QuerySwapExactAmountInRequest(google.protobuf.message.Message):
    """=============================== EstimateSwapExactAmountIn"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SENDER_FIELD_NUMBER: builtins.int
    POOL_ID_FIELD_NUMBER: builtins.int
    TOKEN_IN_FIELD_NUMBER: builtins.int
    ROUTES_FIELD_NUMBER: builtins.int
    sender: builtins.str
    """TODO: CHANGE THIS TO RESERVED IN A PATCH RELEASE"""
    pool_id: builtins.int
    token_in: builtins.str
    @property
    def routes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.gamm.v1beta1.tx_pb2.SwapAmountInRoute]: ...
    def __init__(
        self,
        *,
        sender: builtins.str = ...,
        pool_id: builtins.int = ...,
        token_in: builtins.str = ...,
        routes: collections.abc.Iterable[osmosis.gamm.v1beta1.tx_pb2.SwapAmountInRoute] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pool_id", b"pool_id", "routes", b"routes", "sender", b"sender", "token_in", b"token_in"]) -> None: ...

global___QuerySwapExactAmountInRequest = QuerySwapExactAmountInRequest

class QuerySwapExactAmountInResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOKEN_OUT_AMOUNT_FIELD_NUMBER: builtins.int
    token_out_amount: builtins.str
    def __init__(
        self,
        *,
        token_out_amount: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["token_out_amount", b"token_out_amount"]) -> None: ...

global___QuerySwapExactAmountInResponse = QuerySwapExactAmountInResponse

class QuerySwapExactAmountOutRequest(google.protobuf.message.Message):
    """=============================== EstimateSwapExactAmountOut"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SENDER_FIELD_NUMBER: builtins.int
    POOL_ID_FIELD_NUMBER: builtins.int
    ROUTES_FIELD_NUMBER: builtins.int
    TOKEN_OUT_FIELD_NUMBER: builtins.int
    sender: builtins.str
    """TODO: CHANGE THIS TO RESERVED IN A PATCH RELEASE"""
    pool_id: builtins.int
    @property
    def routes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.gamm.v1beta1.tx_pb2.SwapAmountOutRoute]: ...
    token_out: builtins.str
    def __init__(
        self,
        *,
        sender: builtins.str = ...,
        pool_id: builtins.int = ...,
        routes: collections.abc.Iterable[osmosis.gamm.v1beta1.tx_pb2.SwapAmountOutRoute] | None = ...,
        token_out: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pool_id", b"pool_id", "routes", b"routes", "sender", b"sender", "token_out", b"token_out"]) -> None: ...

global___QuerySwapExactAmountOutRequest = QuerySwapExactAmountOutRequest

class QuerySwapExactAmountOutResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOKEN_IN_AMOUNT_FIELD_NUMBER: builtins.int
    token_in_amount: builtins.str
    def __init__(
        self,
        *,
        token_in_amount: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["token_in_amount", b"token_in_amount"]) -> None: ...

global___QuerySwapExactAmountOutResponse = QuerySwapExactAmountOutResponse

class QueryTotalLiquidityRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QueryTotalLiquidityRequest = QueryTotalLiquidityRequest

class QueryTotalLiquidityResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIQUIDITY_FIELD_NUMBER: builtins.int
    @property
    def liquidity(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(
        self,
        *,
        liquidity: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["liquidity", b"liquidity"]) -> None: ...

global___QueryTotalLiquidityResponse = QueryTotalLiquidityResponse
