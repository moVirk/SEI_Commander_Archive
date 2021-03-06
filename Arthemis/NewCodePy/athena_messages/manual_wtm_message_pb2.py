# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: manual_wtm_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='manual_wtm_message.proto',
  package='WeaponTargetMatchMessage',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18manual_wtm_message.proto\x12\x18WeaponTargetMatchMessage\"n\n\x1bWeapon_Target_Match_Message\x12\x11\n\tsource_id\x18\x01 \x01(\t\x12\x16\n\x0e\x64\x65stination_id\x18\x02 \x03(\t\x12\x11\n\tweapon_id\x18\x03 \x01(\t\x12\x11\n\ttarget_id\x18\x04 \x01(\tb\x06proto3')
)




_WEAPON_TARGET_MATCH_MESSAGE = _descriptor.Descriptor(
  name='Weapon_Target_Match_Message',
  full_name='WeaponTargetMatchMessage.Weapon_Target_Match_Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_id', full_name='WeaponTargetMatchMessage.Weapon_Target_Match_Message.source_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destination_id', full_name='WeaponTargetMatchMessage.Weapon_Target_Match_Message.destination_id', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weapon_id', full_name='WeaponTargetMatchMessage.Weapon_Target_Match_Message.weapon_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_id', full_name='WeaponTargetMatchMessage.Weapon_Target_Match_Message.target_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=54,
  serialized_end=164,
)

DESCRIPTOR.message_types_by_name['Weapon_Target_Match_Message'] = _WEAPON_TARGET_MATCH_MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Weapon_Target_Match_Message = _reflection.GeneratedProtocolMessageType('Weapon_Target_Match_Message', (_message.Message,), dict(
  DESCRIPTOR = _WEAPON_TARGET_MATCH_MESSAGE,
  __module__ = 'manual_wtm_message_pb2'
  # @@protoc_insertion_point(class_scope:WeaponTargetMatchMessage.Weapon_Target_Match_Message)
  ))
_sym_db.RegisterMessage(Weapon_Target_Match_Message)


# @@protoc_insertion_point(module_scope)
