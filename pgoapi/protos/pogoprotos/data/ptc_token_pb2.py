# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/ptc_token.proto

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
  name='pogoprotos/data/ptc_token.proto',
  package='pogoprotos.data',
  syntax='proto3',
  serialized_pb=_b('\n\x1fpogoprotos/data/ptc_token.proto\x12\x0fpogoprotos.data\"-\n\x08PtcToken\x12\r\n\x05token\x18\x01 \x01(\t\x12\x12\n\nexpiration\x18\x02 \x01(\x05\x62\x06proto3')
)




_PTCTOKEN = _descriptor.Descriptor(
  name='PtcToken',
  full_name='pogoprotos.data.PtcToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='pogoprotos.data.PtcToken.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expiration', full_name='pogoprotos.data.PtcToken.expiration', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=97,
)

DESCRIPTOR.message_types_by_name['PtcToken'] = _PTCTOKEN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PtcToken = _reflection.GeneratedProtocolMessageType('PtcToken', (_message.Message,), dict(
  DESCRIPTOR = _PTCTOKEN,
  __module__ = 'pogoprotos.data.ptc_token_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.PtcToken)
  ))
_sym_db.RegisterMessage(PtcToken)


# @@protoc_insertion_point(module_scope)
