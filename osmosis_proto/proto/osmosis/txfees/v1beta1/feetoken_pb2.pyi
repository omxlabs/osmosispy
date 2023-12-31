"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class FeeToken(google.protobuf.message.Message):
    """FeeToken is a struct that specifies a coin denom, and pool ID pair.
    This marks the token as eligible for use as a tx fee asset in Osmosis.
    Its price in osmo is derived through looking at the provided pool ID.
    The pool ID must have osmo as one of its assets.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DENOM_FIELD_NUMBER: builtins.int
    POOLID_FIELD_NUMBER: builtins.int
    denom: builtins.str
    poolID: builtins.int
    def __init__(
        self,
        *,
        denom: builtins.str = ...,
        poolID: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["denom", b"denom", "poolID", b"poolID"]) -> None: ...

global___FeeToken = FeeToken
