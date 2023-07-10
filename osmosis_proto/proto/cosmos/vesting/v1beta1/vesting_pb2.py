# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/vesting/v1beta1/vesting.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.auth.v1beta1 import auth_pb2 as cosmos_dot_auth_dot_v1beta1_dot_auth__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/vesting/v1beta1/vesting.proto\x12\x16\x63osmos.vesting.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1e\x63osmos/auth/v1beta1/auth.proto\"\x89\x04\n\x12\x42\x61seVestingAccount\x12<\n\x0c\x62\x61se_account\x18\x01 \x01(\x0b\x32 .cosmos.auth.v1beta1.BaseAccountB\x04\xd0\xde\x1f\x01\x12\x80\x01\n\x10original_vesting\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBK\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xf2\xde\x1f\x17yaml:\"original_vesting\"\x12|\n\x0e\x64\x65legated_free\x18\x03 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBI\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xf2\xde\x1f\x15yaml:\"delegated_free\"\x12\x82\x01\n\x11\x64\x65legated_vesting\x18\x04 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinBL\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\xf2\xde\x1f\x18yaml:\"delegated_vesting\"\x12%\n\x08\x65nd_time\x18\x05 \x01(\x03\x42\x13\xf2\xde\x1f\x0fyaml:\"end_time\":\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00\"\x9f\x01\n\x18\x43ontinuousVestingAccount\x12N\n\x14\x62\x61se_vesting_account\x18\x01 \x01(\x0b\x32*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01\x12)\n\nstart_time\x18\x02 \x01(\x03\x42\x15\xf2\xde\x1f\x11yaml:\"start_time\":\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00\"q\n\x15\x44\x65layedVestingAccount\x12N\n\x14\x62\x61se_vesting_account\x18\x01 \x01(\x0b\x32*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00\"{\n\x06Period\x12\x0e\n\x06length\x18\x01 \x01(\x03\x12[\n\x06\x61mount\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins:\x04\x98\xa0\x1f\x00\"\xf6\x01\n\x16PeriodicVestingAccount\x12N\n\x14\x62\x61se_vesting_account\x18\x01 \x01(\x0b\x32*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01\x12)\n\nstart_time\x18\x02 \x01(\x03\x42\x15\xf2\xde\x1f\x11yaml:\"start_time\"\x12W\n\x0fvesting_periods\x18\x03 \x03(\x0b\x32\x1e.cosmos.vesting.v1beta1.PeriodB\x1e\xf2\xde\x1f\x16yaml:\"vesting_periods\"\xc8\xde\x1f\x00:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00\"r\n\x16PermanentLockedAccount\x12N\n\x14\x62\x61se_vesting_account\x18\x01 \x01(\x0b\x32*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00\"\x80\x03\n\x16\x43lawbackVestingAccount\x12N\n\x14\x62\x61se_vesting_account\x18\x01 \x01(\x0b\x32*.cosmos.vesting.v1beta1.BaseVestingAccountB\x04\xd0\xde\x1f\x01\x12\x31\n\x0e\x66under_address\x18\x02 \x01(\tB\x19\xf2\xde\x1f\x15yaml:\"funder_address\"\x12)\n\nstart_time\x18\x03 \x01(\x03\x42\x15\xf2\xde\x1f\x11yaml:\"start_time\"\x12U\n\x0elockup_periods\x18\x04 \x03(\x0b\x32\x1e.cosmos.vesting.v1beta1.PeriodB\x1d\xf2\xde\x1f\x15yaml:\"lockup_periods\"\xc8\xde\x1f\x00\x12W\n\x0fvesting_periods\x18\x05 \x03(\x0b\x32\x1e.cosmos.vesting.v1beta1.PeriodB\x1e\xf2\xde\x1f\x16yaml:\"vesting_periods\"\xc8\xde\x1f\x00:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00\x42\x33Z1github.com/cosmos/cosmos-sdk/x/auth/vesting/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.vesting.v1beta1.vesting_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1github.com/cosmos/cosmos-sdk/x/auth/vesting/types'
  _BASEVESTINGACCOUNT.fields_by_name['base_account']._options = None
  _BASEVESTINGACCOUNT.fields_by_name['base_account']._serialized_options = b'\320\336\037\001'
  _BASEVESTINGACCOUNT.fields_by_name['original_vesting']._options = None
  _BASEVESTINGACCOUNT.fields_by_name['original_vesting']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\362\336\037\027yaml:\"original_vesting\"'
  _BASEVESTINGACCOUNT.fields_by_name['delegated_free']._options = None
  _BASEVESTINGACCOUNT.fields_by_name['delegated_free']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\362\336\037\025yaml:\"delegated_free\"'
  _BASEVESTINGACCOUNT.fields_by_name['delegated_vesting']._options = None
  _BASEVESTINGACCOUNT.fields_by_name['delegated_vesting']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins\362\336\037\030yaml:\"delegated_vesting\"'
  _BASEVESTINGACCOUNT.fields_by_name['end_time']._options = None
  _BASEVESTINGACCOUNT.fields_by_name['end_time']._serialized_options = b'\362\336\037\017yaml:\"end_time\"'
  _BASEVESTINGACCOUNT._options = None
  _BASEVESTINGACCOUNT._serialized_options = b'\210\240\037\000\230\240\037\000'
  _CONTINUOUSVESTINGACCOUNT.fields_by_name['base_vesting_account']._options = None
  _CONTINUOUSVESTINGACCOUNT.fields_by_name['base_vesting_account']._serialized_options = b'\320\336\037\001'
  _CONTINUOUSVESTINGACCOUNT.fields_by_name['start_time']._options = None
  _CONTINUOUSVESTINGACCOUNT.fields_by_name['start_time']._serialized_options = b'\362\336\037\021yaml:\"start_time\"'
  _CONTINUOUSVESTINGACCOUNT._options = None
  _CONTINUOUSVESTINGACCOUNT._serialized_options = b'\210\240\037\000\230\240\037\000'
  _DELAYEDVESTINGACCOUNT.fields_by_name['base_vesting_account']._options = None
  _DELAYEDVESTINGACCOUNT.fields_by_name['base_vesting_account']._serialized_options = b'\320\336\037\001'
  _DELAYEDVESTINGACCOUNT._options = None
  _DELAYEDVESTINGACCOUNT._serialized_options = b'\210\240\037\000\230\240\037\000'
  _PERIOD.fields_by_name['amount']._options = None
  _PERIOD.fields_by_name['amount']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _PERIOD._options = None
  _PERIOD._serialized_options = b'\230\240\037\000'
  _PERIODICVESTINGACCOUNT.fields_by_name['base_vesting_account']._options = None
  _PERIODICVESTINGACCOUNT.fields_by_name['base_vesting_account']._serialized_options = b'\320\336\037\001'
  _PERIODICVESTINGACCOUNT.fields_by_name['start_time']._options = None
  _PERIODICVESTINGACCOUNT.fields_by_name['start_time']._serialized_options = b'\362\336\037\021yaml:\"start_time\"'
  _PERIODICVESTINGACCOUNT.fields_by_name['vesting_periods']._options = None
  _PERIODICVESTINGACCOUNT.fields_by_name['vesting_periods']._serialized_options = b'\362\336\037\026yaml:\"vesting_periods\"\310\336\037\000'
  _PERIODICVESTINGACCOUNT._options = None
  _PERIODICVESTINGACCOUNT._serialized_options = b'\210\240\037\000\230\240\037\000'
  _PERMANENTLOCKEDACCOUNT.fields_by_name['base_vesting_account']._options = None
  _PERMANENTLOCKEDACCOUNT.fields_by_name['base_vesting_account']._serialized_options = b'\320\336\037\001'
  _PERMANENTLOCKEDACCOUNT._options = None
  _PERMANENTLOCKEDACCOUNT._serialized_options = b'\210\240\037\000\230\240\037\000'
  _CLAWBACKVESTINGACCOUNT.fields_by_name['base_vesting_account']._options = None
  _CLAWBACKVESTINGACCOUNT.fields_by_name['base_vesting_account']._serialized_options = b'\320\336\037\001'
  _CLAWBACKVESTINGACCOUNT.fields_by_name['funder_address']._options = None
  _CLAWBACKVESTINGACCOUNT.fields_by_name['funder_address']._serialized_options = b'\362\336\037\025yaml:\"funder_address\"'
  _CLAWBACKVESTINGACCOUNT.fields_by_name['start_time']._options = None
  _CLAWBACKVESTINGACCOUNT.fields_by_name['start_time']._serialized_options = b'\362\336\037\021yaml:\"start_time\"'
  _CLAWBACKVESTINGACCOUNT.fields_by_name['lockup_periods']._options = None
  _CLAWBACKVESTINGACCOUNT.fields_by_name['lockup_periods']._serialized_options = b'\362\336\037\025yaml:\"lockup_periods\"\310\336\037\000'
  _CLAWBACKVESTINGACCOUNT.fields_by_name['vesting_periods']._options = None
  _CLAWBACKVESTINGACCOUNT.fields_by_name['vesting_periods']._serialized_options = b'\362\336\037\026yaml:\"vesting_periods\"\310\336\037\000'
  _CLAWBACKVESTINGACCOUNT._options = None
  _CLAWBACKVESTINGACCOUNT._serialized_options = b'\210\240\037\000\230\240\037\000'
  _BASEVESTINGACCOUNT._serialized_start=184
  _BASEVESTINGACCOUNT._serialized_end=705
  _CONTINUOUSVESTINGACCOUNT._serialized_start=708
  _CONTINUOUSVESTINGACCOUNT._serialized_end=867
  _DELAYEDVESTINGACCOUNT._serialized_start=869
  _DELAYEDVESTINGACCOUNT._serialized_end=982
  _PERIOD._serialized_start=984
  _PERIOD._serialized_end=1107
  _PERIODICVESTINGACCOUNT._serialized_start=1110
  _PERIODICVESTINGACCOUNT._serialized_end=1356
  _PERMANENTLOCKEDACCOUNT._serialized_start=1358
  _PERMANENTLOCKEDACCOUNT._serialized_end=1472
  _CLAWBACKVESTINGACCOUNT._serialized_start=1475
  _CLAWBACKVESTINGACCOUNT._serialized_end=1859
# @@protoc_insertion_point(module_scope)
