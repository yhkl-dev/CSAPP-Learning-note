# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/simple.proto

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
  name='proto/simple.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x12proto/simple.proto\"\x14\n\x06Simple\x12\n\n\x02id\x18\x01 \x01(\rb\x06proto3')
)




_SIMPLE = _descriptor.Descriptor(
  name='Simple',
  full_name='Simple',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Simple.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=42,
)

DESCRIPTOR.message_types_by_name['Simple'] = _SIMPLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Simple = _reflection.GeneratedProtocolMessageType('Simple', (_message.Message,), dict(
  DESCRIPTOR = _SIMPLE,
  __module__ = 'proto.simple_pb2'
  # @@protoc_insertion_point(class_scope:Simple)
  ))
_sym_db.RegisterMessage(Simple)


# @@protoc_insertion_point(module_scope)
