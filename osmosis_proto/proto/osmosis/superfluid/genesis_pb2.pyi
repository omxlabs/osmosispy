"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import osmosis.superfluid.params_pb2
import osmosis.superfluid.superfluid_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the module's genesis state."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAMS_FIELD_NUMBER: builtins.int
    SUPERFLUID_ASSETS_FIELD_NUMBER: builtins.int
    OSMO_EQUIVALENT_MULTIPLIERS_FIELD_NUMBER: builtins.int
    INTERMEDIARY_ACCOUNTS_FIELD_NUMBER: builtins.int
    INTEMEDIARY_ACCOUNT_CONNECTIONS_FIELD_NUMBER: builtins.int
    @property
    def params(self) -> osmosis.superfluid.params_pb2.Params: ...
    @property
    def superfluid_assets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.superfluid.superfluid_pb2.SuperfluidAsset]:
        """superfluid_assets defines the registered superfluid assets that have been
        registered via governance.
        """
    @property
    def osmo_equivalent_multipliers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.superfluid.superfluid_pb2.OsmoEquivalentMultiplierRecord]:
        """osmo_equivalent_multipliers is the records of osmo equivalent amount of
        each superfluid registered pool, updated every epoch.
        """
    @property
    def intermediary_accounts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.superfluid.superfluid_pb2.SuperfluidIntermediaryAccount]:
        """intermediary_accounts is a secondary account for superfluid staking that
        plays an intermediary role between validators and the delegators.
        """
    @property
    def intemediary_account_connections(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.superfluid.superfluid_pb2.LockIdIntermediaryAccountConnection]: ...
    def __init__(
        self,
        *,
        params: osmosis.superfluid.params_pb2.Params | None = ...,
        superfluid_assets: collections.abc.Iterable[osmosis.superfluid.superfluid_pb2.SuperfluidAsset] | None = ...,
        osmo_equivalent_multipliers: collections.abc.Iterable[osmosis.superfluid.superfluid_pb2.OsmoEquivalentMultiplierRecord] | None = ...,
        intermediary_accounts: collections.abc.Iterable[osmosis.superfluid.superfluid_pb2.SuperfluidIntermediaryAccount] | None = ...,
        intemediary_account_connections: collections.abc.Iterable[osmosis.superfluid.superfluid_pb2.LockIdIntermediaryAccountConnection] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["intemediary_account_connections", b"intemediary_account_connections", "intermediary_accounts", b"intermediary_accounts", "osmo_equivalent_multipliers", b"osmo_equivalent_multipliers", "params", b"params", "superfluid_assets", b"superfluid_assets"]) -> None: ...

global___GenesisState = GenesisState
