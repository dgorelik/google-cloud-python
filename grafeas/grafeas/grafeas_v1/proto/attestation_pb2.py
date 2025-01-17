# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grafeas_v1/proto/attestation.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from grafeas.grafeas_v1.proto import common_pb2 as grafeas__v1_dot_proto_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="grafeas_v1/proto/attestation.proto",
    package="grafeas.v1",
    syntax="proto3",
    serialized_options=_b(
        "\n\rio.grafeas.v1P\001Z8google.golang.org/genproto/googleapis/grafeas/v1;grafeas\242\002\003GRA"
    ),
    serialized_pb=_b(
        '\n"grafeas_v1/proto/attestation.proto\x12\ngrafeas.v1\x1a\x1dgrafeas_v1/proto/common.proto"f\n\x0f\x41ttestationNote\x12.\n\x04hint\x18\x01 \x01(\x0b\x32 .grafeas.v1.AttestationNote.Hint\x1a#\n\x04Hint\x12\x1b\n\x13human_readable_name\x18\x01 \x01(\t"^\n\x15\x41ttestationOccurrence\x12\x1a\n\x12serialized_payload\x18\x01 \x01(\x0c\x12)\n\nsignatures\x18\x02 \x03(\x0b\x32\x15.grafeas.v1.SignatureBQ\n\rio.grafeas.v1P\x01Z8google.golang.org/genproto/googleapis/grafeas/v1;grafeas\xa2\x02\x03GRAb\x06proto3'
    ),
    dependencies=[grafeas__v1_dot_proto_dot_common__pb2.DESCRIPTOR],
)


_ATTESTATIONNOTE_HINT = _descriptor.Descriptor(
    name="Hint",
    full_name="grafeas.v1.AttestationNote.Hint",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="human_readable_name",
            full_name="grafeas.v1.AttestationNote.Hint.human_readable_name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=148,
    serialized_end=183,
)

_ATTESTATIONNOTE = _descriptor.Descriptor(
    name="AttestationNote",
    full_name="grafeas.v1.AttestationNote",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="hint",
            full_name="grafeas.v1.AttestationNote.hint",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[_ATTESTATIONNOTE_HINT],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=81,
    serialized_end=183,
)


_ATTESTATIONOCCURRENCE = _descriptor.Descriptor(
    name="AttestationOccurrence",
    full_name="grafeas.v1.AttestationOccurrence",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="serialized_payload",
            full_name="grafeas.v1.AttestationOccurrence.serialized_payload",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="signatures",
            full_name="grafeas.v1.AttestationOccurrence.signatures",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=185,
    serialized_end=279,
)

_ATTESTATIONNOTE_HINT.containing_type = _ATTESTATIONNOTE
_ATTESTATIONNOTE.fields_by_name["hint"].message_type = _ATTESTATIONNOTE_HINT
_ATTESTATIONOCCURRENCE.fields_by_name[
    "signatures"
].message_type = grafeas__v1_dot_proto_dot_common__pb2._SIGNATURE
DESCRIPTOR.message_types_by_name["AttestationNote"] = _ATTESTATIONNOTE
DESCRIPTOR.message_types_by_name["AttestationOccurrence"] = _ATTESTATIONOCCURRENCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AttestationNote = _reflection.GeneratedProtocolMessageType(
    "AttestationNote",
    (_message.Message,),
    dict(
        Hint=_reflection.GeneratedProtocolMessageType(
            "Hint",
            (_message.Message,),
            dict(
                DESCRIPTOR=_ATTESTATIONNOTE_HINT,
                __module__="grafeas_v1.proto.attestation_pb2",
                __doc__="""This submessage provides human-readable hints about the purpose of the
    authority. Because the name of a note acts as its resource reference, it
    is important to disambiguate the canonical name of the Note (which might
    be a UUID for security purposes) from "readable" names more suitable for
    debug output. Note that these hints should not be used to look up
    authorities in security sensitive contexts, such as when looking up
    attestations to verify.
    
    
    Attributes:
        human_readable_name:
            Required. The human readable name of this attestation
            authority, for example "qa".
    """,
                # @@protoc_insertion_point(class_scope:grafeas.v1.AttestationNote.Hint)
            ),
        ),
        DESCRIPTOR=_ATTESTATIONNOTE,
        __module__="grafeas_v1.proto.attestation_pb2",
        __doc__="""Note kind that represents a logical attestation "role" or "authority".
  For example, an organization might have one ``Authority`` for "QA" and
  one for "build". This note is intended to act strictly as a grouping
  mechanism for the attached occurrences (Attestations). This grouping
  mechanism also provides a security boundary, since IAM ACLs gate the
  ability for a principle to attach an occurrence to a given note. It also
  provides a single point of lookup to find all attached attestation
  occurrences, even if they don't all live in the same project.
  
  
  Attributes:
      hint:
          Hint hints at the purpose of the attestation authority.
  """,
        # @@protoc_insertion_point(class_scope:grafeas.v1.AttestationNote)
    ),
)
_sym_db.RegisterMessage(AttestationNote)
_sym_db.RegisterMessage(AttestationNote.Hint)

AttestationOccurrence = _reflection.GeneratedProtocolMessageType(
    "AttestationOccurrence",
    (_message.Message,),
    dict(
        DESCRIPTOR=_ATTESTATIONOCCURRENCE,
        __module__="grafeas_v1.proto.attestation_pb2",
        __doc__="""Occurrence that represents a single "attestation". The authenticity of
  an attestation can be verified using the attached signature. If the
  verifier trusts the public key of the signer, then verifying the
  signature is sufficient to establish trust. In this circumstance, the
  authority to which this attestation is attached is primarily useful for
  lookup (how to find this attestation if you already know the authority
  and artifact to be verified) and intent (for which authority this
  attestation was intended to sign.
  
  
  Attributes:
      serialized_payload:
          Required. The serialized payload that is verified by one or
          more ``signatures``.
      signatures:
          One or more signatures over ``serialized_payload``. Verifier
          implementations should consider this attestation message
          verified if at least one ``signature`` verifies
          ``serialized_payload``. See ``Signature`` in common.proto for
          more details on signature structure and verification.
  """,
        # @@protoc_insertion_point(class_scope:grafeas.v1.AttestationOccurrence)
    ),
)
_sym_db.RegisterMessage(AttestationOccurrence)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
