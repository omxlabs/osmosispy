"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _SuperfluidAssetType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _SuperfluidAssetTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_SuperfluidAssetType.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    SuperfluidAssetTypeNative: _SuperfluidAssetType.ValueType  # 0
    SuperfluidAssetTypeLPShare: _SuperfluidAssetType.ValueType  # 1
    """SuperfluidAssetTypeLendingShare = 2; // for now not exist"""

class SuperfluidAssetType(_SuperfluidAssetType, metaclass=_SuperfluidAssetTypeEnumTypeWrapper):
    """SuperfluidAssetType indicates whether the superfluid asset is
    a native token itself or the lp share of a pool.
    """

SuperfluidAssetTypeNative: SuperfluidAssetType.ValueType  # 0
SuperfluidAssetTypeLPShare: SuperfluidAssetType.ValueType  # 1
"""SuperfluidAssetTypeLendingShare = 2; // for now not exist"""
global___SuperfluidAssetType = SuperfluidAssetType

class SuperfluidAsset(google.protobuf.message.Message):
    """SuperfluidAsset stores the pair of superfluid asset type and denom pair"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DENOM_FIELD_NUMBER: builtins.int
    ASSET_TYPE_FIELD_NUMBER: builtins.int
    denom: builtins.str
    asset_type: global___SuperfluidAssetType.ValueType
    """AssetType indicates whether the superfluid asset is a native token or an lp
    share
    """
    def __init__(
        self,
        *,
        denom: builtins.str = ...,
        asset_type: global___SuperfluidAssetType.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["asset_type", b"asset_type", "denom", b"denom"]) -> None: ...

global___SuperfluidAsset = SuperfluidAsset

class SuperfluidIntermediaryAccount(google.protobuf.message.Message):
    """SuperfluidIntermediaryAccount takes the role of intermediary between LP token
    and OSMO tokens for superfluid staking. The intermediary account is the
    actual account responsible for delegation, not the validator account itself.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DENOM_FIELD_NUMBER: builtins.int
    VAL_ADDR_FIELD_NUMBER: builtins.int
    GAUGE_ID_FIELD_NUMBER: builtins.int
    denom: builtins.str
    """Denom indicates the denom of the superfluid asset."""
    val_addr: builtins.str
    gauge_id: builtins.int
    """perpetual gauge for rewards distribution"""
    def __init__(
        self,
        *,
        denom: builtins.str = ...,
        val_addr: builtins.str = ...,
        gauge_id: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["denom", b"denom", "gauge_id", b"gauge_id", "val_addr", b"val_addr"]) -> None: ...

global___SuperfluidIntermediaryAccount = SuperfluidIntermediaryAccount

class OsmoEquivalentMultiplierRecord(google.protobuf.message.Message):
    """The Osmo-Equivalent-Multiplier Record for epoch N refers to the osmo worth we
    treat an LP share as having, for all of epoch N. Eventually this is intended
    to be set as the Time-weighted-average-osmo-backing for the entire duration
    of epoch N-1. (Thereby locking whats in use for epoch N as based on the prior
    epochs rewards) However for now, this is not the TWAP but instead the spot
    price at the boundary. For different types of assets in the future, it could
    change.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EPOCH_NUMBER_FIELD_NUMBER: builtins.int
    DENOM_FIELD_NUMBER: builtins.int
    MULTIPLIER_FIELD_NUMBER: builtins.int
    epoch_number: builtins.int
    denom: builtins.str
    """superfluid asset denom, can be LP token or native token"""
    multiplier: builtins.str
    def __init__(
        self,
        *,
        epoch_number: builtins.int = ...,
        denom: builtins.str = ...,
        multiplier: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["denom", b"denom", "epoch_number", b"epoch_number", "multiplier", b"multiplier"]) -> None: ...

global___OsmoEquivalentMultiplierRecord = OsmoEquivalentMultiplierRecord

class SuperfluidDelegationRecord(google.protobuf.message.Message):
    """SuperfluidDelegationRecord is a struct used to indicate superfluid
    delegations of an account in the state machine in a user friendly form.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DELEGATOR_ADDRESS_FIELD_NUMBER: builtins.int
    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    DELEGATION_AMOUNT_FIELD_NUMBER: builtins.int
    EQUIVALENT_STAKED_AMOUNT_FIELD_NUMBER: builtins.int
    delegator_address: builtins.str
    validator_address: builtins.str
    @property
    def delegation_amount(self) -> cosmos.base.v1beta1.coin_pb2.Coin: ...
    @property
    def equivalent_staked_amount(self) -> cosmos.base.v1beta1.coin_pb2.Coin: ...
    def __init__(
        self,
        *,
        delegator_address: builtins.str = ...,
        validator_address: builtins.str = ...,
        delegation_amount: cosmos.base.v1beta1.coin_pb2.Coin | None = ...,
        equivalent_staked_amount: cosmos.base.v1beta1.coin_pb2.Coin | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["delegation_amount", b"delegation_amount", "equivalent_staked_amount", b"equivalent_staked_amount"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["delegation_amount", b"delegation_amount", "delegator_address", b"delegator_address", "equivalent_staked_amount", b"equivalent_staked_amount", "validator_address", b"validator_address"]) -> None: ...

global___SuperfluidDelegationRecord = SuperfluidDelegationRecord

class LockIdIntermediaryAccountConnection(google.protobuf.message.Message):
    """LockIdIntermediaryAccountConnection is a struct used to indicate the
    relationship between the underlying lock id and superfluid delegation done
    via lp shares.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOCK_ID_FIELD_NUMBER: builtins.int
    INTERMEDIARY_ACCOUNT_FIELD_NUMBER: builtins.int
    lock_id: builtins.int
    intermediary_account: builtins.str
    def __init__(
        self,
        *,
        lock_id: builtins.int = ...,
        intermediary_account: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["intermediary_account", b"intermediary_account", "lock_id", b"lock_id"]) -> None: ...

global___LockIdIntermediaryAccountConnection = LockIdIntermediaryAccountConnection

class UnpoolWhitelistedPools(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IDS_FIELD_NUMBER: builtins.int
    @property
    def ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        ids: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ids", b"ids"]) -> None: ...

global___UnpoolWhitelistedPools = UnpoolWhitelistedPools
