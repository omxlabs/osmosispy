"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class MsgSubmitEvidence(google.protobuf.message.Message):
    """MsgSubmitEvidence represents a message that supports submitting arbitrary
    Evidence of misbehavior such as equivocation or counterfactual signing.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBMITTER_FIELD_NUMBER: builtins.int
    EVIDENCE_FIELD_NUMBER: builtins.int
    submitter: builtins.str
    @property
    def evidence(self) -> google.protobuf.any_pb2.Any: ...
    def __init__(
        self,
        *,
        submitter: builtins.str = ...,
        evidence: google.protobuf.any_pb2.Any | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["evidence", b"evidence"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["evidence", b"evidence", "submitter", b"submitter"]) -> None: ...

global___MsgSubmitEvidence = MsgSubmitEvidence

class MsgSubmitEvidenceResponse(google.protobuf.message.Message):
    """MsgSubmitEvidenceResponse defines the Msg/SubmitEvidence response type."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HASH_FIELD_NUMBER: builtins.int
    hash: builtins.bytes
    """hash defines the hash of the evidence."""
    def __init__(
        self,
        *,
        hash: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["hash", b"hash"]) -> None: ...

global___MsgSubmitEvidenceResponse = MsgSubmitEvidenceResponse
