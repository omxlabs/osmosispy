"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import cosmos.base.reflection.v1beta1.reflection_pb2
import grpc

class ReflectionServiceStub:
    """ReflectionService defines a service for interface reflection."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    ListAllInterfaces: grpc.UnaryUnaryMultiCallable[
        cosmos.base.reflection.v1beta1.reflection_pb2.ListAllInterfacesRequest,
        cosmos.base.reflection.v1beta1.reflection_pb2.ListAllInterfacesResponse,
    ]
    """ListAllInterfaces lists all the interfaces registered in the interface
    registry.
    """
    ListImplementations: grpc.UnaryUnaryMultiCallable[
        cosmos.base.reflection.v1beta1.reflection_pb2.ListImplementationsRequest,
        cosmos.base.reflection.v1beta1.reflection_pb2.ListImplementationsResponse,
    ]
    """ListImplementations list all the concrete types that implement a given
    interface.
    """

class ReflectionServiceServicer(metaclass=abc.ABCMeta):
    """ReflectionService defines a service for interface reflection."""

    @abc.abstractmethod
    def ListAllInterfaces(
        self,
        request: cosmos.base.reflection.v1beta1.reflection_pb2.ListAllInterfacesRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.base.reflection.v1beta1.reflection_pb2.ListAllInterfacesResponse:
        """ListAllInterfaces lists all the interfaces registered in the interface
        registry.
        """
    @abc.abstractmethod
    def ListImplementations(
        self,
        request: cosmos.base.reflection.v1beta1.reflection_pb2.ListImplementationsRequest,
        context: grpc.ServicerContext,
    ) -> cosmos.base.reflection.v1beta1.reflection_pb2.ListImplementationsResponse:
        """ListImplementations list all the concrete types that implement a given
        interface.
        """

def add_ReflectionServiceServicer_to_server(servicer: ReflectionServiceServicer, server: grpc.Server) -> None: ...
