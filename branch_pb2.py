# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: branch.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='branch.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x62ranch.proto\"@\n\nMsgRequest\x12\x11\n\tinterface\x18\x01 \x01(\t\x12\r\n\x05money\x18\x02 \x01(\x05\x12\x10\n\x08writeset\x18\x03 \x03(\x05\"A\n\x0bMsgResponse\x12\x11\n\tinterface\x18\x01 \x01(\t\x12\r\n\x05money\x18\x02 \x01(\x05\x12\x10\n\x08writeset\x18\x03 \x03(\x05\x32\x63\n\x06\x42ranch\x12*\n\x0bMsgDelivery\x12\x0b.MsgRequest\x1a\x0c.MsgResponse\"\x00\x12-\n\x0eMsgPropagation\x12\x0b.MsgRequest\x1a\x0c.MsgResponse\"\x00\x62\x06proto3'
)




_MSGREQUEST = _descriptor.Descriptor(
  name='MsgRequest',
  full_name='MsgRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='interface', full_name='MsgRequest.interface', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='money', full_name='MsgRequest.money', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='writeset', full_name='MsgRequest.writeset', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=80,
)


_MSGRESPONSE = _descriptor.Descriptor(
  name='MsgResponse',
  full_name='MsgResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='interface', full_name='MsgResponse.interface', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='money', full_name='MsgResponse.money', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='writeset', full_name='MsgResponse.writeset', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=147,
)

DESCRIPTOR.message_types_by_name['MsgRequest'] = _MSGREQUEST
DESCRIPTOR.message_types_by_name['MsgResponse'] = _MSGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgRequest = _reflection.GeneratedProtocolMessageType('MsgRequest', (_message.Message,), {
  'DESCRIPTOR' : _MSGREQUEST,
  '__module__' : 'branch_pb2'
  # @@protoc_insertion_point(class_scope:MsgRequest)
  })
_sym_db.RegisterMessage(MsgRequest)

MsgResponse = _reflection.GeneratedProtocolMessageType('MsgResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGRESPONSE,
  '__module__' : 'branch_pb2'
  # @@protoc_insertion_point(class_scope:MsgResponse)
  })
_sym_db.RegisterMessage(MsgResponse)



_BRANCH = _descriptor.ServiceDescriptor(
  name='Branch',
  full_name='Branch',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=149,
  serialized_end=248,
  methods=[
  _descriptor.MethodDescriptor(
    name='MsgDelivery',
    full_name='Branch.MsgDelivery',
    index=0,
    containing_service=None,
    input_type=_MSGREQUEST,
    output_type=_MSGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MsgPropagation',
    full_name='Branch.MsgPropagation',
    index=1,
    containing_service=None,
    input_type=_MSGREQUEST,
    output_type=_MSGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BRANCH)

DESCRIPTOR.services_by_name['Branch'] = _BRANCH

# @@protoc_insertion_point(module_scope)
