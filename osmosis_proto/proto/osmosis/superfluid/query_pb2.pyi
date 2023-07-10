"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import cosmos.base.query.v1beta1.pagination_pb2
import cosmos.base.v1beta1.coin_pb2
import cosmos.staking.v1beta1.staking_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import osmosis.lockup.lock_pb2
import osmosis.superfluid.params_pb2
import osmosis.superfluid.superfluid_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class QueryParamsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QueryParamsRequest = QueryParamsRequest

class QueryParamsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMS_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> osmosis.superfluid.params_pb2.Params:
        """params defines the parameters of the module."""
    def __init__(
        self,
        *,
        params: osmosis.superfluid.params_pb2.Params | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["params", b"params"]) -> None: ...

global___QueryParamsResponse = QueryParamsResponse

class AssetTypeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DENOM_FIELD_NUMBER: builtins.int
    denom: builtins.str
    def __init__(
        self,
        *,
        denom: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["denom", b"denom"]) -> None: ...

global___AssetTypeRequest = AssetTypeRequest

class AssetTypeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ASSET_TYPE_FIELD_NUMBER: builtins.int
    asset_type: osmosis.superfluid.superfluid_pb2.SuperfluidAssetType.ValueType
    def __init__(
        self,
        *,
        asset_type: osmosis.superfluid.superfluid_pb2.SuperfluidAssetType.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["asset_type", b"asset_type"]) -> None: ...

global___AssetTypeResponse = AssetTypeResponse

class AllAssetsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___AllAssetsRequest = AllAssetsRequest

class AllAssetsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ASSETS_FIELD_NUMBER: builtins.int
    @property
    def assets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.superfluid.superfluid_pb2.SuperfluidAsset]: ...
    def __init__(
        self,
        *,
        assets: collections.abc.Iterable[osmosis.superfluid.superfluid_pb2.SuperfluidAsset] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["assets", b"assets"]) -> None: ...

global___AllAssetsResponse = AllAssetsResponse

class AssetMultiplierRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DENOM_FIELD_NUMBER: builtins.int
    denom: builtins.str
    def __init__(
        self,
        *,
        denom: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["denom", b"denom"]) -> None: ...

global___AssetMultiplierRequest = AssetMultiplierRequest

class AssetMultiplierResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OSMO_EQUIVALENT_MULTIPLIER_FIELD_NUMBER: builtins.int
    @property
    def osmo_equivalent_multiplier(self) -> osmosis.superfluid.superfluid_pb2.OsmoEquivalentMultiplierRecord: ...
    def __init__(
        self,
        *,
        osmo_equivalent_multiplier: osmosis.superfluid.superfluid_pb2.OsmoEquivalentMultiplierRecord | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["osmo_equivalent_multiplier", b"osmo_equivalent_multiplier"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["osmo_equivalent_multiplier", b"osmo_equivalent_multiplier"]) -> None: ...

global___AssetMultiplierResponse = AssetMultiplierResponse

class SuperfluidIntermediaryAccountInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DENOM_FIELD_NUMBER: builtins.int
    VAL_ADDR_FIELD_NUMBER: builtins.int
    GAUGE_ID_FIELD_NUMBER: builtins.int
    ADDRESS_FIELD_NUMBER: builtins.int
    denom: builtins.str
    val_addr: builtins.str
    gauge_id: builtins.int
    address: builtins.str
    def __init__(
        self,
        *,
        denom: builtins.str = ...,
        val_addr: builtins.str = ...,
        gauge_id: builtins.int = ...,
        address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address", b"address", "denom", b"denom", "gauge_id", b"gauge_id", "val_addr", b"val_addr"]) -> None: ...

global___SuperfluidIntermediaryAccountInfo = SuperfluidIntermediaryAccountInfo

class AllIntermediaryAccountsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...
    def __init__(
        self,
        *,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> None: ...

global___AllIntermediaryAccountsRequest = AllIntermediaryAccountsRequest

class AllIntermediaryAccountsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNTS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def accounts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SuperfluidIntermediaryAccountInfo]: ...
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...
    def __init__(
        self,
        *,
        accounts: collections.abc.Iterable[global___SuperfluidIntermediaryAccountInfo] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["accounts", b"accounts", "pagination", b"pagination"]) -> None: ...

global___AllIntermediaryAccountsResponse = AllIntermediaryAccountsResponse

class ConnectedIntermediaryAccountRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOCK_ID_FIELD_NUMBER: builtins.int
    lock_id: builtins.int
    def __init__(
        self,
        *,
        lock_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["lock_id", b"lock_id"]) -> None: ...

global___ConnectedIntermediaryAccountRequest = ConnectedIntermediaryAccountRequest

class ConnectedIntermediaryAccountResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ACCOUNT_FIELD_NUMBER: builtins.int
    @property
    def account(self) -> global___SuperfluidIntermediaryAccountInfo: ...
    def __init__(
        self,
        *,
        account: global___SuperfluidIntermediaryAccountInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["account", b"account"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["account", b"account"]) -> None: ...

global___ConnectedIntermediaryAccountResponse = ConnectedIntermediaryAccountResponse

class QueryTotalDelegationByValidatorForDenomRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DENOM_FIELD_NUMBER: builtins.int
    denom: builtins.str
    def __init__(
        self,
        *,
        denom: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["denom", b"denom"]) -> None: ...

global___QueryTotalDelegationByValidatorForDenomRequest = QueryTotalDelegationByValidatorForDenomRequest

class QueryTotalDelegationByValidatorForDenomResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ASSETS_FIELD_NUMBER: builtins.int
    @property
    def assets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Delegations]: ...
    def __init__(
        self,
        *,
        assets: collections.abc.Iterable[global___Delegations] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["assets", b"assets"]) -> None: ...

global___QueryTotalDelegationByValidatorForDenomResponse = QueryTotalDelegationByValidatorForDenomResponse

class Delegations(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VAL_ADDR_FIELD_NUMBER: builtins.int
    AMOUNT_SFSD_FIELD_NUMBER: builtins.int
    OSMO_EQUIVALENT_FIELD_NUMBER: builtins.int
    val_addr: builtins.str
    amount_sfsd: builtins.str
    osmo_equivalent: builtins.str
    def __init__(
        self,
        *,
        val_addr: builtins.str = ...,
        amount_sfsd: builtins.str = ...,
        osmo_equivalent: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["amount_sfsd", b"amount_sfsd", "osmo_equivalent", b"osmo_equivalent", "val_addr", b"val_addr"]) -> None: ...

global___Delegations = Delegations

class TotalSuperfluidDelegationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___TotalSuperfluidDelegationsRequest = TotalSuperfluidDelegationsRequest

class TotalSuperfluidDelegationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOTAL_DELEGATIONS_FIELD_NUMBER: builtins.int
    total_delegations: builtins.str
    def __init__(
        self,
        *,
        total_delegations: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["total_delegations", b"total_delegations"]) -> None: ...

global___TotalSuperfluidDelegationsResponse = TotalSuperfluidDelegationsResponse

class SuperfluidDelegationAmountRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DELEGATOR_ADDRESS_FIELD_NUMBER: builtins.int
    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    DENOM_FIELD_NUMBER: builtins.int
    delegator_address: builtins.str
    validator_address: builtins.str
    denom: builtins.str
    def __init__(
        self,
        *,
        delegator_address: builtins.str = ...,
        validator_address: builtins.str = ...,
        denom: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["delegator_address", b"delegator_address", "denom", b"denom", "validator_address", b"validator_address"]) -> None: ...

global___SuperfluidDelegationAmountRequest = SuperfluidDelegationAmountRequest

class SuperfluidDelegationAmountResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AMOUNT_FIELD_NUMBER: builtins.int
    @property
    def amount(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(
        self,
        *,
        amount: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["amount", b"amount"]) -> None: ...

global___SuperfluidDelegationAmountResponse = SuperfluidDelegationAmountResponse

class SuperfluidDelegationsByDelegatorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DELEGATOR_ADDRESS_FIELD_NUMBER: builtins.int
    delegator_address: builtins.str
    def __init__(
        self,
        *,
        delegator_address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["delegator_address", b"delegator_address"]) -> None: ...

global___SuperfluidDelegationsByDelegatorRequest = SuperfluidDelegationsByDelegatorRequest

class SuperfluidDelegationsByDelegatorResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUPERFLUID_DELEGATION_RECORDS_FIELD_NUMBER: builtins.int
    TOTAL_DELEGATED_COINS_FIELD_NUMBER: builtins.int
    TOTAL_EQUIVALENT_STAKED_AMOUNT_FIELD_NUMBER: builtins.int
    @property
    def superfluid_delegation_records(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.superfluid.superfluid_pb2.SuperfluidDelegationRecord]: ...
    @property
    def total_delegated_coins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    @property
    def total_equivalent_staked_amount(self) -> cosmos.base.v1beta1.coin_pb2.Coin: ...
    def __init__(
        self,
        *,
        superfluid_delegation_records: collections.abc.Iterable[osmosis.superfluid.superfluid_pb2.SuperfluidDelegationRecord] | None = ...,
        total_delegated_coins: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
        total_equivalent_staked_amount: cosmos.base.v1beta1.coin_pb2.Coin | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["total_equivalent_staked_amount", b"total_equivalent_staked_amount"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["superfluid_delegation_records", b"superfluid_delegation_records", "total_delegated_coins", b"total_delegated_coins", "total_equivalent_staked_amount", b"total_equivalent_staked_amount"]) -> None: ...

global___SuperfluidDelegationsByDelegatorResponse = SuperfluidDelegationsByDelegatorResponse

class SuperfluidUndelegationsByDelegatorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DELEGATOR_ADDRESS_FIELD_NUMBER: builtins.int
    DENOM_FIELD_NUMBER: builtins.int
    delegator_address: builtins.str
    denom: builtins.str
    def __init__(
        self,
        *,
        delegator_address: builtins.str = ...,
        denom: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["delegator_address", b"delegator_address", "denom", b"denom"]) -> None: ...

global___SuperfluidUndelegationsByDelegatorRequest = SuperfluidUndelegationsByDelegatorRequest

class SuperfluidUndelegationsByDelegatorResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUPERFLUID_DELEGATION_RECORDS_FIELD_NUMBER: builtins.int
    TOTAL_UNDELEGATED_COINS_FIELD_NUMBER: builtins.int
    SYNTHETIC_LOCKS_FIELD_NUMBER: builtins.int
    @property
    def superfluid_delegation_records(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.superfluid.superfluid_pb2.SuperfluidDelegationRecord]: ...
    @property
    def total_undelegated_coins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    @property
    def synthetic_locks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.lockup.lock_pb2.SyntheticLock]: ...
    def __init__(
        self,
        *,
        superfluid_delegation_records: collections.abc.Iterable[osmosis.superfluid.superfluid_pb2.SuperfluidDelegationRecord] | None = ...,
        total_undelegated_coins: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
        synthetic_locks: collections.abc.Iterable[osmosis.lockup.lock_pb2.SyntheticLock] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["superfluid_delegation_records", b"superfluid_delegation_records", "synthetic_locks", b"synthetic_locks", "total_undelegated_coins", b"total_undelegated_coins"]) -> None: ...

global___SuperfluidUndelegationsByDelegatorResponse = SuperfluidUndelegationsByDelegatorResponse

class SuperfluidDelegationsByValidatorDenomRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    DENOM_FIELD_NUMBER: builtins.int
    validator_address: builtins.str
    denom: builtins.str
    def __init__(
        self,
        *,
        validator_address: builtins.str = ...,
        denom: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["denom", b"denom", "validator_address", b"validator_address"]) -> None: ...

global___SuperfluidDelegationsByValidatorDenomRequest = SuperfluidDelegationsByValidatorDenomRequest

class SuperfluidDelegationsByValidatorDenomResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUPERFLUID_DELEGATION_RECORDS_FIELD_NUMBER: builtins.int
    @property
    def superfluid_delegation_records(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.superfluid.superfluid_pb2.SuperfluidDelegationRecord]: ...
    def __init__(
        self,
        *,
        superfluid_delegation_records: collections.abc.Iterable[osmosis.superfluid.superfluid_pb2.SuperfluidDelegationRecord] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["superfluid_delegation_records", b"superfluid_delegation_records"]) -> None: ...

global___SuperfluidDelegationsByValidatorDenomResponse = SuperfluidDelegationsByValidatorDenomResponse

class EstimateSuperfluidDelegatedAmountByValidatorDenomRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    DENOM_FIELD_NUMBER: builtins.int
    validator_address: builtins.str
    denom: builtins.str
    def __init__(
        self,
        *,
        validator_address: builtins.str = ...,
        denom: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["denom", b"denom", "validator_address", b"validator_address"]) -> None: ...

global___EstimateSuperfluidDelegatedAmountByValidatorDenomRequest = EstimateSuperfluidDelegatedAmountByValidatorDenomRequest

class EstimateSuperfluidDelegatedAmountByValidatorDenomResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOTAL_DELEGATED_COINS_FIELD_NUMBER: builtins.int
    @property
    def total_delegated_coins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(
        self,
        *,
        total_delegated_coins: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["total_delegated_coins", b"total_delegated_coins"]) -> None: ...

global___EstimateSuperfluidDelegatedAmountByValidatorDenomResponse = EstimateSuperfluidDelegatedAmountByValidatorDenomResponse

class QueryTotalDelegationByDelegatorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DELEGATOR_ADDRESS_FIELD_NUMBER: builtins.int
    delegator_address: builtins.str
    def __init__(
        self,
        *,
        delegator_address: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["delegator_address", b"delegator_address"]) -> None: ...

global___QueryTotalDelegationByDelegatorRequest = QueryTotalDelegationByDelegatorRequest

class QueryTotalDelegationByDelegatorResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUPERFLUID_DELEGATION_RECORDS_FIELD_NUMBER: builtins.int
    DELEGATION_RESPONSE_FIELD_NUMBER: builtins.int
    TOTAL_DELEGATED_COINS_FIELD_NUMBER: builtins.int
    TOTAL_EQUIVALENT_STAKED_AMOUNT_FIELD_NUMBER: builtins.int
    @property
    def superfluid_delegation_records(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.superfluid.superfluid_pb2.SuperfluidDelegationRecord]: ...
    @property
    def delegation_response(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.staking.v1beta1.staking_pb2.DelegationResponse]: ...
    @property
    def total_delegated_coins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    @property
    def total_equivalent_staked_amount(self) -> cosmos.base.v1beta1.coin_pb2.Coin: ...
    def __init__(
        self,
        *,
        superfluid_delegation_records: collections.abc.Iterable[osmosis.superfluid.superfluid_pb2.SuperfluidDelegationRecord] | None = ...,
        delegation_response: collections.abc.Iterable[cosmos.staking.v1beta1.staking_pb2.DelegationResponse] | None = ...,
        total_delegated_coins: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
        total_equivalent_staked_amount: cosmos.base.v1beta1.coin_pb2.Coin | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["total_equivalent_staked_amount", b"total_equivalent_staked_amount"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["delegation_response", b"delegation_response", "superfluid_delegation_records", b"superfluid_delegation_records", "total_delegated_coins", b"total_delegated_coins", "total_equivalent_staked_amount", b"total_equivalent_staked_amount"]) -> None: ...

global___QueryTotalDelegationByDelegatorResponse = QueryTotalDelegationByDelegatorResponse

class QueryUnpoolWhitelistRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QueryUnpoolWhitelistRequest = QueryUnpoolWhitelistRequest

class QueryUnpoolWhitelistResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOL_IDS_FIELD_NUMBER: builtins.int
    @property
    def pool_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        pool_ids: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["pool_ids", b"pool_ids"]) -> None: ...

global___QueryUnpoolWhitelistResponse = QueryUnpoolWhitelistResponse
