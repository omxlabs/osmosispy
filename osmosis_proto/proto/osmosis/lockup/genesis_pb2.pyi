"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import osmosis.lockup.lock_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GenesisState(google.protobuf.message.Message):
    """GenesisState defines the lockup module's genesis state."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LAST_LOCK_ID_FIELD_NUMBER: builtins.int
    LOCKS_FIELD_NUMBER: builtins.int
    SYNTHETIC_LOCKS_FIELD_NUMBER: builtins.int
    last_lock_id: builtins.int
    @property
    def locks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.lockup.lock_pb2.PeriodLock]: ...
    @property
    def synthetic_locks(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.lockup.lock_pb2.SyntheticLock]: ...
    def __init__(
        self,
        *,
        last_lock_id: builtins.int = ...,
        locks: collections.abc.Iterable[osmosis.lockup.lock_pb2.PeriodLock] | None = ...,
        synthetic_locks: collections.abc.Iterable[osmosis.lockup.lock_pb2.SyntheticLock] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["last_lock_id", b"last_lock_id", "locks", b"locks", "synthetic_locks", b"synthetic_locks"]) -> None: ...

global___GenesisState = GenesisState
