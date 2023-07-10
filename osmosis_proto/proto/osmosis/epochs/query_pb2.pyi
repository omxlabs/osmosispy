"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import osmosis.epochs.genesis_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class QueryEpochsInfoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___QueryEpochsInfoRequest = QueryEpochsInfoRequest

class QueryEpochsInfoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EPOCHS_FIELD_NUMBER: builtins.int
    @property
    def epochs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.epochs.genesis_pb2.EpochInfo]: ...
    def __init__(
        self,
        *,
        epochs: collections.abc.Iterable[osmosis.epochs.genesis_pb2.EpochInfo] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["epochs", b"epochs"]) -> None: ...

global___QueryEpochsInfoResponse = QueryEpochsInfoResponse

class QueryCurrentEpochRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IDENTIFIER_FIELD_NUMBER: builtins.int
    identifier: builtins.str
    def __init__(
        self,
        *,
        identifier: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["identifier", b"identifier"]) -> None: ...

global___QueryCurrentEpochRequest = QueryCurrentEpochRequest

class QueryCurrentEpochResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CURRENT_EPOCH_FIELD_NUMBER: builtins.int
    current_epoch: builtins.int
    def __init__(
        self,
        *,
        current_epoch: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["current_epoch", b"current_epoch"]) -> None: ...

global___QueryCurrentEpochResponse = QueryCurrentEpochResponse
