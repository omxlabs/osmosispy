"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Since: cosmos-sdk 0.43"""
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

class MsgGrantAllowance(google.protobuf.message.Message):
    """MsgGrantAllowance adds permission for Grantee to spend up to Allowance
    of fees from the account of Granter.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GRANTER_FIELD_NUMBER: builtins.int
    GRANTEE_FIELD_NUMBER: builtins.int
    ALLOWANCE_FIELD_NUMBER: builtins.int
    granter: builtins.str
    """granter is the address of the user granting an allowance of their funds."""
    grantee: builtins.str
    """grantee is the address of the user being granted an allowance of another user's funds."""
    @property
    def allowance(self) -> google.protobuf.any_pb2.Any:
        """allowance can be any of basic and filtered fee allowance."""
    def __init__(
        self,
        *,
        granter: builtins.str = ...,
        grantee: builtins.str = ...,
        allowance: google.protobuf.any_pb2.Any | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["allowance", b"allowance"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["allowance", b"allowance", "grantee", b"grantee", "granter", b"granter"]) -> None: ...

global___MsgGrantAllowance = MsgGrantAllowance

class MsgGrantAllowanceResponse(google.protobuf.message.Message):
    """MsgGrantAllowanceResponse defines the Msg/GrantAllowanceResponse response type."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___MsgGrantAllowanceResponse = MsgGrantAllowanceResponse

class MsgRevokeAllowance(google.protobuf.message.Message):
    """MsgRevokeAllowance removes any existing Allowance from Granter to Grantee."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GRANTER_FIELD_NUMBER: builtins.int
    GRANTEE_FIELD_NUMBER: builtins.int
    granter: builtins.str
    """granter is the address of the user granting an allowance of their funds."""
    grantee: builtins.str
    """grantee is the address of the user being granted an allowance of another user's funds."""
    def __init__(
        self,
        *,
        granter: builtins.str = ...,
        grantee: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["grantee", b"grantee", "granter", b"granter"]) -> None: ...

global___MsgRevokeAllowance = MsgRevokeAllowance

class MsgRevokeAllowanceResponse(google.protobuf.message.Message):
    """MsgRevokeAllowanceResponse defines the Msg/RevokeAllowanceResponse response type."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___MsgRevokeAllowanceResponse = MsgRevokeAllowanceResponse
