# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: osmosis/txfees/v1beta1/gov.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from osmosis.txfees.v1beta1 import feetoken_pb2 as osmosis_dot_txfees_dot_v1beta1_dot_feetoken__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n osmosis/txfees/v1beta1/gov.proto\x12\x16osmosis.txfees.v1beta1\x1a\x14gogoproto/gogo.proto\x1a%osmosis/txfees/v1beta1/feetoken.proto\"\xc2\x01\n\x16UpdateFeeTokenProposal\x12\x1f\n\x05title\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:\"title\"\x12+\n\x0b\x64\x65scription\x18\x02 \x01(\tB\x16\xf2\xde\x1f\x12yaml:\"description\"\x12L\n\x08\x66\x65\x65token\x18\x03 \x01(\x0b\x32 .osmosis.txfees.v1beta1.FeeTokenB\x18\xf2\xde\x1f\x10yaml:\"fee_token\"\xc8\xde\x1f\x00:\x0c\xe8\xa0\x1f\x01\x88\xa0\x1f\x00\x98\xa0\x1f\x00\x42\x34Z2github.com/osmosis-labs/osmosis/v14/x/txfees/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.txfees.v1beta1.gov_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2github.com/osmosis-labs/osmosis/v14/x/txfees/types'
  _UPDATEFEETOKENPROPOSAL.fields_by_name['title']._options = None
  _UPDATEFEETOKENPROPOSAL.fields_by_name['title']._serialized_options = b'\362\336\037\014yaml:\"title\"'
  _UPDATEFEETOKENPROPOSAL.fields_by_name['description']._options = None
  _UPDATEFEETOKENPROPOSAL.fields_by_name['description']._serialized_options = b'\362\336\037\022yaml:\"description\"'
  _UPDATEFEETOKENPROPOSAL.fields_by_name['feetoken']._options = None
  _UPDATEFEETOKENPROPOSAL.fields_by_name['feetoken']._serialized_options = b'\362\336\037\020yaml:\"fee_token\"\310\336\037\000'
  _UPDATEFEETOKENPROPOSAL._options = None
  _UPDATEFEETOKENPROPOSAL._serialized_options = b'\350\240\037\001\210\240\037\000\230\240\037\000'
  _UPDATEFEETOKENPROPOSAL._serialized_start=122
  _UPDATEFEETOKENPROPOSAL._serialized_end=316
# @@protoc_insertion_point(module_scope)
