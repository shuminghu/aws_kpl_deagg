# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kpl.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='kpl.proto',
  package='',
  serialized_pb=_b('\n\tkpl.proto\"j\n\x10\x41ggregatedRecord\x12\x1b\n\x13partition_key_table\x18\x01 \x03(\t\x12\x1f\n\x17\x65xplicit_hash_key_table\x18\x02 \x03(\t\x12\x18\n\x07records\x18\x03 \x03(\x0b\x32\x07.Record\"!\n\x03Tag\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x01(\t\"h\n\x06Record\x12\x1b\n\x13partition_key_index\x18\x01 \x02(\x04\x12\x1f\n\x17\x65xplicit_hash_key_index\x18\x02 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x03 \x02(\x0c\x12\x12\n\x04tags\x18\x04 \x03(\x0b\x32\x04.Tag')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_AGGREGATEDRECORD = _descriptor.Descriptor(
  name='AggregatedRecord',
  full_name='AggregatedRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partition_key_table', full_name='AggregatedRecord.partition_key_table', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='explicit_hash_key_table', full_name='AggregatedRecord.explicit_hash_key_table', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='records', full_name='AggregatedRecord.records', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13,
  serialized_end=119,
)


_TAG = _descriptor.Descriptor(
  name='Tag',
  full_name='Tag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Tag.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='Tag.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=154,
)


_RECORD = _descriptor.Descriptor(
  name='Record',
  full_name='Record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partition_key_index', full_name='Record.partition_key_index', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='explicit_hash_key_index', full_name='Record.explicit_hash_key_index', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='Record.data', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tags', full_name='Record.tags', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=156,
  serialized_end=260,
)

_AGGREGATEDRECORD.fields_by_name['records'].message_type = _RECORD
_RECORD.fields_by_name['tags'].message_type = _TAG
DESCRIPTOR.message_types_by_name['AggregatedRecord'] = _AGGREGATEDRECORD
DESCRIPTOR.message_types_by_name['Tag'] = _TAG
DESCRIPTOR.message_types_by_name['Record'] = _RECORD

AggregatedRecord = _reflection.GeneratedProtocolMessageType('AggregatedRecord', (_message.Message,), dict(
  DESCRIPTOR = _AGGREGATEDRECORD,
  __module__ = 'kpl_pb2'
  # @@protoc_insertion_point(class_scope:AggregatedRecord)
  ))
_sym_db.RegisterMessage(AggregatedRecord)

Tag = _reflection.GeneratedProtocolMessageType('Tag', (_message.Message,), dict(
  DESCRIPTOR = _TAG,
  __module__ = 'kpl_pb2'
  # @@protoc_insertion_point(class_scope:Tag)
  ))
_sym_db.RegisterMessage(Tag)

Record = _reflection.GeneratedProtocolMessageType('Record', (_message.Message,), dict(
  DESCRIPTOR = _RECORD,
  __module__ = 'kpl_pb2'
  # @@protoc_insertion_point(class_scope:Record)
  ))
_sym_db.RegisterMessage(Record)


# @@protoc_insertion_point(module_scope)
