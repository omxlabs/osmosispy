"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Since: cosmos-sdk 0.43"""
import abc
import cosmos.feegrant.v1beta1.query_pb2
import grpc

class QueryStub:
    """Query defines the gRPC querier service."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    Allowance: grpc.UnaryUnaryMultiCallable[
        cosmos.feegrant.v1beta1.query_pb2.QueryAllowanceRequest,
        cosmos.feegrant.v1beta1.query_pb2.QueryAllowanceResponse,
    ]
    """Allowance returns fee granted to the grantee by the granter."""
    Allowances: grpc.UnaryUnaryMultiCallable[
        cosmos.feegrant.v1beta1.query_pb2.QueryAllowancesRequest,
        cosmos.feegrant.v1beta1.query_pb2.QueryAllowancesResponse,
    ]
    """Allowances returns all the grants for address."""

class QueryServicer(metaclass=abc.ABCMeta):
    """Query defines the gRPC querier service."""

    @abc.abstractmethod
    def Allowance(
        self,
        request: cosmos.feegrant.v1beta1.query_pb2.QueryAllowanceRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.feegrant.v1beta1.query_pb2.QueryAllowanceResponse:
        """Allowance returns fee granted to the grantee by the granter."""
    @abc.abstractmethod
    def Allowances(
        self,
        request: cosmos.feegrant.v1beta1.query_pb2.QueryAllowancesRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.feegrant.v1beta1.query_pb2.QueryAllowancesResponse:
        """Allowances returns all the grants for address."""

def add_QueryServicer_to_server(servicer: QueryServicer, server: grpc.Server) -> None: ...
