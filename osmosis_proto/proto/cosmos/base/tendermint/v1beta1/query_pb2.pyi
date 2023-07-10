"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import cosmos.base.query.v1beta1.pagination_pb2
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys
import tendermint.p2p.types_pb2
import tendermint.types.block_pb2
import tendermint.types.types_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class GetValidatorSetByHeightRequest(google.protobuf.message.Message):
    """GetValidatorSetByHeightRequest is the request type for the Query/GetValidatorSetByHeight RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEIGHT_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    height: builtins.int
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest:
        """pagination defines an pagination for the request."""
    def __init__(
        self,
        *,
        height: builtins.int = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["height", b"height", "pagination", b"pagination"]) -> None: ...

global___GetValidatorSetByHeightRequest = GetValidatorSetByHeightRequest

class GetValidatorSetByHeightResponse(google.protobuf.message.Message):
    """GetValidatorSetByHeightResponse is the response type for the Query/GetValidatorSetByHeight RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BLOCK_HEIGHT_FIELD_NUMBER: builtins.int
    VALIDATORS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    block_height: builtins.int
    @property
    def validators(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Validator]: ...
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse:
        """pagination defines an pagination for the response."""
    def __init__(
        self,
        *,
        block_height: builtins.int = ...,
        validators: collections.abc.Iterable[global___Validator] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["block_height", b"block_height", "pagination", b"pagination", "validators", b"validators"]) -> None: ...

global___GetValidatorSetByHeightResponse = GetValidatorSetByHeightResponse

class GetLatestValidatorSetRequest(google.protobuf.message.Message):
    """GetLatestValidatorSetRequest is the request type for the Query/GetValidatorSetByHeight RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PAGINATION_FIELD_NUMBER: builtins.int
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest:
        """pagination defines an pagination for the request."""
    def __init__(
        self,
        *,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> None: ...

global___GetLatestValidatorSetRequest = GetLatestValidatorSetRequest

class GetLatestValidatorSetResponse(google.protobuf.message.Message):
    """GetLatestValidatorSetResponse is the response type for the Query/GetValidatorSetByHeight RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BLOCK_HEIGHT_FIELD_NUMBER: builtins.int
    VALIDATORS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    block_height: builtins.int
    @property
    def validators(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Validator]: ...
    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse:
        """pagination defines an pagination for the response."""
    def __init__(
        self,
        *,
        block_height: builtins.int = ...,
        validators: collections.abc.Iterable[global___Validator] | None = ...,
        pagination: cosmos.base.query.v1beta1.pagination_pb2.PageResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pagination", b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["block_height", b"block_height", "pagination", b"pagination", "validators", b"validators"]) -> None: ...

global___GetLatestValidatorSetResponse = GetLatestValidatorSetResponse

class Validator(google.protobuf.message.Message):
    """Validator is the type for the validator-set."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDRESS_FIELD_NUMBER: builtins.int
    PUB_KEY_FIELD_NUMBER: builtins.int
    VOTING_POWER_FIELD_NUMBER: builtins.int
    PROPOSER_PRIORITY_FIELD_NUMBER: builtins.int
    address: builtins.str
    @property
    def pub_key(self) -> google.protobuf.any_pb2.Any: ...
    voting_power: builtins.int
    proposer_priority: builtins.int
    def __init__(
        self,
        *,
        address: builtins.str = ...,
        pub_key: google.protobuf.any_pb2.Any | None = ...,
        voting_power: builtins.int = ...,
        proposer_priority: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pub_key", b"pub_key"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["address", b"address", "proposer_priority", b"proposer_priority", "pub_key", b"pub_key", "voting_power", b"voting_power"]) -> None: ...

global___Validator = Validator

class GetBlockByHeightRequest(google.protobuf.message.Message):
    """GetBlockByHeightRequest is the request type for the Query/GetBlockByHeight RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HEIGHT_FIELD_NUMBER: builtins.int
    height: builtins.int
    def __init__(
        self,
        *,
        height: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["height", b"height"]) -> None: ...

global___GetBlockByHeightRequest = GetBlockByHeightRequest

class GetBlockByHeightResponse(google.protobuf.message.Message):
    """GetBlockByHeightResponse is the response type for the Query/GetBlockByHeight RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BLOCK_ID_FIELD_NUMBER: builtins.int
    BLOCK_FIELD_NUMBER: builtins.int
    @property
    def block_id(self) -> tendermint.types.types_pb2.BlockID: ...
    @property
    def block(self) -> tendermint.types.block_pb2.Block: ...
    def __init__(
        self,
        *,
        block_id: tendermint.types.types_pb2.BlockID | None = ...,
        block: tendermint.types.block_pb2.Block | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["block", b"block", "block_id", b"block_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["block", b"block", "block_id", b"block_id"]) -> None: ...

global___GetBlockByHeightResponse = GetBlockByHeightResponse

class GetLatestBlockRequest(google.protobuf.message.Message):
    """GetLatestBlockRequest is the request type for the Query/GetLatestBlock RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___GetLatestBlockRequest = GetLatestBlockRequest

class GetLatestBlockResponse(google.protobuf.message.Message):
    """GetLatestBlockResponse is the response type for the Query/GetLatestBlock RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BLOCK_ID_FIELD_NUMBER: builtins.int
    BLOCK_FIELD_NUMBER: builtins.int
    @property
    def block_id(self) -> tendermint.types.types_pb2.BlockID: ...
    @property
    def block(self) -> tendermint.types.block_pb2.Block: ...
    def __init__(
        self,
        *,
        block_id: tendermint.types.types_pb2.BlockID | None = ...,
        block: tendermint.types.block_pb2.Block | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["block", b"block", "block_id", b"block_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["block", b"block", "block_id", b"block_id"]) -> None: ...

global___GetLatestBlockResponse = GetLatestBlockResponse

class GetSyncingRequest(google.protobuf.message.Message):
    """GetSyncingRequest is the request type for the Query/GetSyncing RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___GetSyncingRequest = GetSyncingRequest

class GetSyncingResponse(google.protobuf.message.Message):
    """GetSyncingResponse is the response type for the Query/GetSyncing RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SYNCING_FIELD_NUMBER: builtins.int
    syncing: builtins.bool
    def __init__(
        self,
        *,
        syncing: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["syncing", b"syncing"]) -> None: ...

global___GetSyncingResponse = GetSyncingResponse

class GetNodeInfoRequest(google.protobuf.message.Message):
    """GetNodeInfoRequest is the request type for the Query/GetNodeInfo RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___GetNodeInfoRequest = GetNodeInfoRequest

class GetNodeInfoResponse(google.protobuf.message.Message):
    """GetNodeInfoResponse is the request type for the Query/GetNodeInfo RPC method."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DEFAULT_NODE_INFO_FIELD_NUMBER: builtins.int
    APPLICATION_VERSION_FIELD_NUMBER: builtins.int
    @property
    def default_node_info(self) -> tendermint.p2p.types_pb2.DefaultNodeInfo: ...
    @property
    def application_version(self) -> global___VersionInfo: ...
    def __init__(
        self,
        *,
        default_node_info: tendermint.p2p.types_pb2.DefaultNodeInfo | None = ...,
        application_version: global___VersionInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["application_version", b"application_version", "default_node_info", b"default_node_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["application_version", b"application_version", "default_node_info", b"default_node_info"]) -> None: ...

global___GetNodeInfoResponse = GetNodeInfoResponse

class VersionInfo(google.protobuf.message.Message):
    """VersionInfo is the type for the GetNodeInfoResponse message."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    APP_NAME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    GIT_COMMIT_FIELD_NUMBER: builtins.int
    BUILD_TAGS_FIELD_NUMBER: builtins.int
    GO_VERSION_FIELD_NUMBER: builtins.int
    BUILD_DEPS_FIELD_NUMBER: builtins.int
    COSMOS_SDK_VERSION_FIELD_NUMBER: builtins.int
    name: builtins.str
    app_name: builtins.str
    version: builtins.str
    git_commit: builtins.str
    build_tags: builtins.str
    go_version: builtins.str
    @property
    def build_deps(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Module]: ...
    cosmos_sdk_version: builtins.str
    """Since: cosmos-sdk 0.43"""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        app_name: builtins.str = ...,
        version: builtins.str = ...,
        git_commit: builtins.str = ...,
        build_tags: builtins.str = ...,
        go_version: builtins.str = ...,
        build_deps: collections.abc.Iterable[global___Module] | None = ...,
        cosmos_sdk_version: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["app_name", b"app_name", "build_deps", b"build_deps", "build_tags", b"build_tags", "cosmos_sdk_version", b"cosmos_sdk_version", "git_commit", b"git_commit", "go_version", b"go_version", "name", b"name", "version", b"version"]) -> None: ...

global___VersionInfo = VersionInfo

class Module(google.protobuf.message.Message):
    """Module is the type for VersionInfo"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PATH_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    SUM_FIELD_NUMBER: builtins.int
    path: builtins.str
    """module path"""
    version: builtins.str
    """module version"""
    sum: builtins.str
    """checksum"""
    def __init__(
        self,
        *,
        path: builtins.str = ...,
        version: builtins.str = ...,
        sum: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["path", b"path", "sum", b"sum", "version", b"version"]) -> None: ...

global___Module = Module