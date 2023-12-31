"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import osmosis.pool_incentives.v1beta1.incentives_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ReplacePoolIncentivesProposal(google.protobuf.message.Message):
    """ReplacePoolIncentivesProposal is a gov Content type for updating the pool
    incentives. If a ReplacePoolIncentivesProposal passes, the proposal’s records
    override the existing DistrRecords set in the module. Each record has a
    specified gauge id and weight, and the incentives are distributed to each
    gauge according to weight/total_weight. The incentives are put in the fee
    pool and it is allocated to gauges and community pool by the DistrRecords
    configuration. Note that gaugeId=0 represents the community pool.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TITLE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    RECORDS_FIELD_NUMBER: builtins.int
    title: builtins.str
    description: builtins.str
    @property
    def records(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.pool_incentives.v1beta1.incentives_pb2.DistrRecord]: ...
    def __init__(
        self,
        *,
        title: builtins.str = ...,
        description: builtins.str = ...,
        records: collections.abc.Iterable[osmosis.pool_incentives.v1beta1.incentives_pb2.DistrRecord] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "records", b"records", "title", b"title"]) -> None: ...

global___ReplacePoolIncentivesProposal = ReplacePoolIncentivesProposal

class UpdatePoolIncentivesProposal(google.protobuf.message.Message):
    """UpdatePoolIncentivesProposal is a gov Content type for updating the pool
    incentives. If a UpdatePoolIncentivesProposal passes, all the DistrRecords
    in the proposals are edited. An existing DistrRecord is not overriden unless
    explicitly included in the proposal.
    This differs from an ReplacePoolIncentivesProposal because it only does an
    in place update of the DistrRecords for gauges explicitly mentioned in the
    proposal.

    For example: if the existing DistrRecords were:
    [(Gauge 0, 5), (Gauge 1, 6), (Gauge 2, 6)]
    An UpdatePoolIncentivesProposal includes
    [(Gauge 1, 0), (Gauge 2, 4), (Gauge 3, 10)]
    This would delete Gauge 1, Edit Gauge 2, and Add Gauge 3
    The result DistrRecords in state would be:
    [(Gauge 0, 5), (Gauge 2, 4), (Gauge 3, 10)]
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TITLE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    RECORDS_FIELD_NUMBER: builtins.int
    title: builtins.str
    description: builtins.str
    @property
    def records(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[osmosis.pool_incentives.v1beta1.incentives_pb2.DistrRecord]: ...
    def __init__(
        self,
        *,
        title: builtins.str = ...,
        description: builtins.str = ...,
        records: collections.abc.Iterable[osmosis.pool_incentives.v1beta1.incentives_pb2.DistrRecord] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "records", b"records", "title", b"title"]) -> None: ...

global___UpdatePoolIncentivesProposal = UpdatePoolIncentivesProposal
