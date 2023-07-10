# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: osmosis/lockup/lock.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19osmosis/lockup/lock.proto\x12\x0eosmosis.lockup\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\"\xc0\x02\n\nPeriodLock\x12\n\n\x02ID\x18\x01 \x01(\x04\x12\x1f\n\x05owner\x18\x02 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:\"owner\"\x12^\n\x08\x64uration\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationB1\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xea\xde\x1f\x12\x64uration,omitempty\xf2\xde\x1f\x0fyaml:\"duration\"\x12I\n\x08\x65nd_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x1b\x90\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:\"end_time\"\x12Z\n\x05\x63oins\x18\x05 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\"\xee\x01\n\x0eQueryCondition\x12\x36\n\x0flock_query_type\x18\x01 \x01(\x0e\x32\x1d.osmosis.lockup.LockQueryType\x12\r\n\x05\x64\x65nom\x18\x02 \x01(\t\x12H\n\x08\x64uration\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationB\x1b\x98\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:\"duration\"\x12K\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x1c\x90\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:\"timestamp\"\"\xeb\x01\n\rSyntheticLock\x12\x1a\n\x12underlying_lock_id\x18\x01 \x01(\x04\x12\x13\n\x0bsynth_denom\x18\x02 \x01(\t\x12I\n\x08\x65nd_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x1b\x90\xdf\x1f\x01\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:\"end_time\"\x12^\n\x08\x64uration\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationB1\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xea\xde\x1f\x12\x64uration,omitempty\xf2\xde\x1f\x0fyaml:\"duration\"*1\n\rLockQueryType\x12\x0e\n\nByDuration\x10\x00\x12\n\n\x06\x42yTime\x10\x01\x1a\x04\x88\xa3\x1e\x00\x42\x34Z2github.com/osmosis-labs/osmosis/v14/x/lockup/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.lockup.lock_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2github.com/osmosis-labs/osmosis/v14/x/lockup/types'
  _LOCKQUERYTYPE._options = None
  _LOCKQUERYTYPE._serialized_options = b'\210\243\036\000'
  _PERIODLOCK.fields_by_name['owner']._options = None
  _PERIODLOCK.fields_by_name['owner']._serialized_options = b'\362\336\037\014yaml:\"owner\"'
  _PERIODLOCK.fields_by_name['duration']._options = None
  _PERIODLOCK.fields_by_name['duration']._serialized_options = b'\310\336\037\000\230\337\037\001\352\336\037\022duration,omitempty\362\336\037\017yaml:\"duration\"'
  _PERIODLOCK.fields_by_name['end_time']._options = None
  _PERIODLOCK.fields_by_name['end_time']._serialized_options = b'\220\337\037\001\310\336\037\000\362\336\037\017yaml:\"end_time\"'
  _PERIODLOCK.fields_by_name['coins']._options = None
  _PERIODLOCK.fields_by_name['coins']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _QUERYCONDITION.fields_by_name['duration']._options = None
  _QUERYCONDITION.fields_by_name['duration']._serialized_options = b'\230\337\037\001\310\336\037\000\362\336\037\017yaml:\"duration\"'
  _QUERYCONDITION.fields_by_name['timestamp']._options = None
  _QUERYCONDITION.fields_by_name['timestamp']._serialized_options = b'\220\337\037\001\310\336\037\000\362\336\037\020yaml:\"timestamp\"'
  _SYNTHETICLOCK.fields_by_name['end_time']._options = None
  _SYNTHETICLOCK.fields_by_name['end_time']._serialized_options = b'\220\337\037\001\310\336\037\000\362\336\037\017yaml:\"end_time\"'
  _SYNTHETICLOCK.fields_by_name['duration']._options = None
  _SYNTHETICLOCK.fields_by_name['duration']._serialized_options = b'\310\336\037\000\230\337\037\001\352\336\037\022duration,omitempty\362\336\037\017yaml:\"duration\"'
  _LOCKQUERYTYPE._serialized_start=966
  _LOCKQUERYTYPE._serialized_end=1015
  _PERIODLOCK._serialized_start=165
  _PERIODLOCK._serialized_end=485
  _QUERYCONDITION._serialized_start=488
  _QUERYCONDITION._serialized_end=726
  _SYNTHETICLOCK._serialized_start=729
  _SYNTHETICLOCK._serialized_end=964
# @@protoc_insertion_point(module_scope)
