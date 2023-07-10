"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import cosmos.auth.v1beta1.auth_pb2
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class BaseVestingAccount(google.protobuf.message.Message):
    """BaseVestingAccount implements the VestingAccount interface. It contains all
    the necessary fields needed for any vesting account implementation.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASE_ACCOUNT_FIELD_NUMBER: builtins.int
    ORIGINAL_VESTING_FIELD_NUMBER: builtins.int
    DELEGATED_FREE_FIELD_NUMBER: builtins.int
    DELEGATED_VESTING_FIELD_NUMBER: builtins.int
    END_TIME_FIELD_NUMBER: builtins.int
    @property
    def base_account(self) -> cosmos.auth.v1beta1.auth_pb2.BaseAccount: ...
    @property
    def original_vesting(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    @property
    def delegated_free(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    @property
    def delegated_vesting(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    end_time: builtins.int
    def __init__(
        self,
        *,
        base_account: cosmos.auth.v1beta1.auth_pb2.BaseAccount | None = ...,
        original_vesting: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
        delegated_free: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
        delegated_vesting: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
        end_time: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["base_account", b"base_account"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["base_account", b"base_account", "delegated_free", b"delegated_free", "delegated_vesting", b"delegated_vesting", "end_time", b"end_time", "original_vesting", b"original_vesting"]) -> None: ...

global___BaseVestingAccount = BaseVestingAccount

class ContinuousVestingAccount(google.protobuf.message.Message):
    """ContinuousVestingAccount implements the VestingAccount interface. It
    continuously vests by unlocking coins linearly with respect to time.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASE_VESTING_ACCOUNT_FIELD_NUMBER: builtins.int
    START_TIME_FIELD_NUMBER: builtins.int
    @property
    def base_vesting_account(self) -> global___BaseVestingAccount: ...
    start_time: builtins.int
    def __init__(
        self,
        *,
        base_vesting_account: global___BaseVestingAccount | None = ...,
        start_time: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["base_vesting_account", b"base_vesting_account"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["base_vesting_account", b"base_vesting_account", "start_time", b"start_time"]) -> None: ...

global___ContinuousVestingAccount = ContinuousVestingAccount

class DelayedVestingAccount(google.protobuf.message.Message):
    """DelayedVestingAccount implements the VestingAccount interface. It vests all
    coins after a specific time, but non prior. In other words, it keeps them
    locked until a specified time.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASE_VESTING_ACCOUNT_FIELD_NUMBER: builtins.int
    @property
    def base_vesting_account(self) -> global___BaseVestingAccount: ...
    def __init__(
        self,
        *,
        base_vesting_account: global___BaseVestingAccount | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["base_vesting_account", b"base_vesting_account"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["base_vesting_account", b"base_vesting_account"]) -> None: ...

global___DelayedVestingAccount = DelayedVestingAccount

class Period(google.protobuf.message.Message):
    """Period defines a length of time and amount of coins that will vest."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LENGTH_FIELD_NUMBER: builtins.int
    AMOUNT_FIELD_NUMBER: builtins.int
    length: builtins.int
    @property
    def amount(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(
        self,
        *,
        length: builtins.int = ...,
        amount: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["amount", b"amount", "length", b"length"]) -> None: ...

global___Period = Period

class PeriodicVestingAccount(google.protobuf.message.Message):
    """PeriodicVestingAccount implements the VestingAccount interface. It
    periodically vests by unlocking coins during each specified period.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASE_VESTING_ACCOUNT_FIELD_NUMBER: builtins.int
    START_TIME_FIELD_NUMBER: builtins.int
    VESTING_PERIODS_FIELD_NUMBER: builtins.int
    @property
    def base_vesting_account(self) -> global___BaseVestingAccount: ...
    start_time: builtins.int
    @property
    def vesting_periods(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Period]: ...
    def __init__(
        self,
        *,
        base_vesting_account: global___BaseVestingAccount | None = ...,
        start_time: builtins.int = ...,
        vesting_periods: collections.abc.Iterable[global___Period] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["base_vesting_account", b"base_vesting_account"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["base_vesting_account", b"base_vesting_account", "start_time", b"start_time", "vesting_periods", b"vesting_periods"]) -> None: ...

global___PeriodicVestingAccount = PeriodicVestingAccount

class PermanentLockedAccount(google.protobuf.message.Message):
    """PermanentLockedAccount implements the VestingAccount interface. It does
    not ever release coins, locking them indefinitely. Coins in this account can
    still be used for delegating and for governance votes even while locked.

    Since: cosmos-sdk 0.43
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASE_VESTING_ACCOUNT_FIELD_NUMBER: builtins.int
    @property
    def base_vesting_account(self) -> global___BaseVestingAccount: ...
    def __init__(
        self,
        *,
        base_vesting_account: global___BaseVestingAccount | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["base_vesting_account", b"base_vesting_account"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["base_vesting_account", b"base_vesting_account"]) -> None: ...

global___PermanentLockedAccount = PermanentLockedAccount

class ClawbackVestingAccount(google.protobuf.message.Message):
    """ClawbackVestingAccount implements the VestingAccount interface. It provides
    an account that can hold contributions subject to "lockup" (like a
    PeriodicVestingAccount), or vesting which is subject to clawback
    of unvested tokens, or a combination (tokens vest, but are still locked).
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASE_VESTING_ACCOUNT_FIELD_NUMBER: builtins.int
    FUNDER_ADDRESS_FIELD_NUMBER: builtins.int
    START_TIME_FIELD_NUMBER: builtins.int
    LOCKUP_PERIODS_FIELD_NUMBER: builtins.int
    VESTING_PERIODS_FIELD_NUMBER: builtins.int
    @property
    def base_vesting_account(self) -> global___BaseVestingAccount: ...
    funder_address: builtins.str
    """funder_address specifies the account which can perform clawback."""
    start_time: builtins.int
    @property
    def lockup_periods(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Period]:
        """unlocking schedule relative to the BaseVestingAccount start_time."""
    @property
    def vesting_periods(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Period]:
        """vesting (i.e. immunity from clawback) schedule relative to the BaseVestingAccount start_time."""
    def __init__(
        self,
        *,
        base_vesting_account: global___BaseVestingAccount | None = ...,
        funder_address: builtins.str = ...,
        start_time: builtins.int = ...,
        lockup_periods: collections.abc.Iterable[global___Period] | None = ...,
        vesting_periods: collections.abc.Iterable[global___Period] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["base_vesting_account", b"base_vesting_account"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["base_vesting_account", b"base_vesting_account", "funder_address", b"funder_address", "lockup_periods", b"lockup_periods", "start_time", b"start_time", "vesting_periods", b"vesting_periods"]) -> None: ...

global___ClawbackVestingAccount = ClawbackVestingAccount
