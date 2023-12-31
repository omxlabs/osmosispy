# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from osmosis.gamm.v1beta1 import tx_pb2 as osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2


class MsgStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.JoinPool = channel.unary_unary(
                '/osmosis.gamm.v1beta1.Msg/JoinPool',
                request_serializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgJoinPool.SerializeToString,
                response_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgJoinPoolResponse.FromString,
                )
        self.ExitPool = channel.unary_unary(
                '/osmosis.gamm.v1beta1.Msg/ExitPool',
                request_serializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgExitPool.SerializeToString,
                response_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgExitPoolResponse.FromString,
                )
        self.SwapExactAmountIn = channel.unary_unary(
                '/osmosis.gamm.v1beta1.Msg/SwapExactAmountIn',
                request_serializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgSwapExactAmountIn.SerializeToString,
                response_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgSwapExactAmountInResponse.FromString,
                )
        self.SwapExactAmountOut = channel.unary_unary(
                '/osmosis.gamm.v1beta1.Msg/SwapExactAmountOut',
                request_serializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgSwapExactAmountOut.SerializeToString,
                response_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgSwapExactAmountOutResponse.FromString,
                )
        self.JoinSwapExternAmountIn = channel.unary_unary(
                '/osmosis.gamm.v1beta1.Msg/JoinSwapExternAmountIn',
                request_serializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgJoinSwapExternAmountIn.SerializeToString,
                response_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgJoinSwapExternAmountInResponse.FromString,
                )
        self.JoinSwapShareAmountOut = channel.unary_unary(
                '/osmosis.gamm.v1beta1.Msg/JoinSwapShareAmountOut',
                request_serializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgJoinSwapShareAmountOut.SerializeToString,
                response_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgJoinSwapShareAmountOutResponse.FromString,
                )
        self.ExitSwapExternAmountOut = channel.unary_unary(
                '/osmosis.gamm.v1beta1.Msg/ExitSwapExternAmountOut',
                request_serializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgExitSwapExternAmountOut.SerializeToString,
                response_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgExitSwapExternAmountOutResponse.FromString,
                )
        self.ExitSwapShareAmountIn = channel.unary_unary(
                '/osmosis.gamm.v1beta1.Msg/ExitSwapShareAmountIn',
                request_serializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgExitSwapShareAmountIn.SerializeToString,
                response_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgExitSwapShareAmountInResponse.FromString,
                )


class MsgServicer(object):
    """Missing associated documentation comment in .proto file."""

    def JoinPool(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExitPool(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SwapExactAmountIn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SwapExactAmountOut(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def JoinSwapExternAmountIn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def JoinSwapShareAmountOut(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExitSwapExternAmountOut(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExitSwapShareAmountIn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'JoinPool': grpc.unary_unary_rpc_method_handler(
                    servicer.JoinPool,
                    request_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgJoinPool.FromString,
                    response_serializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgJoinPoolResponse.SerializeToString,
            ),
            'ExitPool': grpc.unary_unary_rpc_method_handler(
                    servicer.ExitPool,
                    request_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgExitPool.FromString,
                    response_serializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgExitPoolResponse.SerializeToString,
            ),
            'SwapExactAmountIn': grpc.unary_unary_rpc_method_handler(
                    servicer.SwapExactAmountIn,
                    request_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgSwapExactAmountIn.FromString,
                    response_serializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgSwapExactAmountInResponse.SerializeToString,
            ),
            'SwapExactAmountOut': grpc.unary_unary_rpc_method_handler(
                    servicer.SwapExactAmountOut,
                    request_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgSwapExactAmountOut.FromString,
                    response_serializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgSwapExactAmountOutResponse.SerializeToString,
            ),
            'JoinSwapExternAmountIn': grpc.unary_unary_rpc_method_handler(
                    servicer.JoinSwapExternAmountIn,
                    request_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgJoinSwapExternAmountIn.FromString,
                    response_serializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgJoinSwapExternAmountInResponse.SerializeToString,
            ),
            'JoinSwapShareAmountOut': grpc.unary_unary_rpc_method_handler(
                    servicer.JoinSwapShareAmountOut,
                    request_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgJoinSwapShareAmountOut.FromString,
                    response_serializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgJoinSwapShareAmountOutResponse.SerializeToString,
            ),
            'ExitSwapExternAmountOut': grpc.unary_unary_rpc_method_handler(
                    servicer.ExitSwapExternAmountOut,
                    request_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgExitSwapExternAmountOut.FromString,
                    response_serializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgExitSwapExternAmountOutResponse.SerializeToString,
            ),
            'ExitSwapShareAmountIn': grpc.unary_unary_rpc_method_handler(
                    servicer.ExitSwapShareAmountIn,
                    request_deserializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgExitSwapShareAmountIn.FromString,
                    response_serializer=osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgExitSwapShareAmountInResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'osmosis.gamm.v1beta1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def JoinPool(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.gamm.v1beta1.Msg/JoinPool',
            osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgJoinPool.SerializeToString,
            osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgJoinPoolResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExitPool(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.gamm.v1beta1.Msg/ExitPool',
            osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgExitPool.SerializeToString,
            osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgExitPoolResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SwapExactAmountIn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.gamm.v1beta1.Msg/SwapExactAmountIn',
            osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgSwapExactAmountIn.SerializeToString,
            osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgSwapExactAmountInResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SwapExactAmountOut(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.gamm.v1beta1.Msg/SwapExactAmountOut',
            osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgSwapExactAmountOut.SerializeToString,
            osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgSwapExactAmountOutResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def JoinSwapExternAmountIn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.gamm.v1beta1.Msg/JoinSwapExternAmountIn',
            osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgJoinSwapExternAmountIn.SerializeToString,
            osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgJoinSwapExternAmountInResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def JoinSwapShareAmountOut(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.gamm.v1beta1.Msg/JoinSwapShareAmountOut',
            osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgJoinSwapShareAmountOut.SerializeToString,
            osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgJoinSwapShareAmountOutResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExitSwapExternAmountOut(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.gamm.v1beta1.Msg/ExitSwapExternAmountOut',
            osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgExitSwapExternAmountOut.SerializeToString,
            osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgExitSwapExternAmountOutResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExitSwapShareAmountIn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.gamm.v1beta1.Msg/ExitSwapShareAmountIn',
            osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgExitSwapShareAmountIn.SerializeToString,
            osmosis_dot_gamm_dot_v1beta1_dot_tx__pb2.MsgExitSwapShareAmountInResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
