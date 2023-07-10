"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import osmosis.twap.v1beta1.twap_record_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Params(google.protobuf.message.Message):
    """Params holds parameters for the twap module"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PRUNE_EPOCH_IDENTIFIER_FIELD_NUMBER: builtins.int
    RECORD_HISTORY_KEEP_PERIOD_FIELD_NUMBER: builtins.int
    prune_epoch_identifier: builtins.str
    @property
    def record_history_keep_period(self) -> google.protobuf.duration_pb2.Duration: ...
    def __init__(
        self,
        *,
        prune_epoch_identifier: builtins.str = ...,
        record_history_keep_period: google.protobuf.duration_pb2.Duration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["record_history_keep_period", b"record_history_keep_period"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["prune_epoch_identifier", b"prune_epoch_identifier", "record_history_keep_period", b"record_history_keep_period"]) -> None: ...

global___Params = Params

class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the twap module's genesis state."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TWAPS_FIELD_NUMBER: builtins.int
    PARAMS_FIELD_NUMBER: builtins.int
    @property
    def twaps(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.twap.v1beta1.twap_record_pb2.TwapRecord]:
        """twaps is the collection of all twap records."""
    @property
    def params(self) -> global___Params:
        """params is the container of twap parameters."""
    def __init__(
        self,
        *,
        twaps: collections.abc.Iterable[osmosis.twap.v1beta1.twap_record_pb2.TwapRecord] | None = ...,
        params: global___Params | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["params", b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["params", b"params", "twaps", b"twaps"]) -> None: ...

global___GenesisState = GenesisState
