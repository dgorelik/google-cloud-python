# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grafeas_v1/proto/common.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="grafeas_v1/proto/common.proto",
    package="grafeas.v1",
    syntax="proto3",
    serialized_options=_b(
        "\n\rio.grafeas.v1P\001Z8google.golang.org/genproto/googleapis/grafeas/v1;grafeas\242\002\003GRA"
    ),
    serialized_pb=_b(
        '\n\x1dgrafeas_v1/proto/common.proto\x12\ngrafeas.v1"(\n\nRelatedUrl\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t"5\n\tSignature\x12\x11\n\tsignature\x18\x01 \x01(\x0c\x12\x15\n\rpublic_key_id\x18\x02 \x01(\t*\x8b\x01\n\x08NoteKind\x12\x19\n\x15NOTE_KIND_UNSPECIFIED\x10\x00\x12\x11\n\rVULNERABILITY\x10\x01\x12\t\n\x05\x42UILD\x10\x02\x12\t\n\x05IMAGE\x10\x03\x12\x0b\n\x07PACKAGE\x10\x04\x12\x0e\n\nDEPLOYMENT\x10\x05\x12\r\n\tDISCOVERY\x10\x06\x12\x0f\n\x0b\x41TTESTATION\x10\x07\x42Q\n\rio.grafeas.v1P\x01Z8google.golang.org/genproto/googleapis/grafeas/v1;grafeas\xa2\x02\x03GRAb\x06proto3'
    ),
)

_NOTEKIND = _descriptor.EnumDescriptor(
    name="NoteKind",
    full_name="grafeas.v1.NoteKind",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="NOTE_KIND_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="VULNERABILITY", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="BUILD", index=2, number=2, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="IMAGE", index=3, number=3, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="PACKAGE", index=4, number=4, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="DEPLOYMENT", index=5, number=5, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="DISCOVERY", index=6, number=6, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="ATTESTATION", index=7, number=7, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=143,
    serialized_end=282,
)
_sym_db.RegisterEnumDescriptor(_NOTEKIND)

NoteKind = enum_type_wrapper.EnumTypeWrapper(_NOTEKIND)
NOTE_KIND_UNSPECIFIED = 0
VULNERABILITY = 1
BUILD = 2
IMAGE = 3
PACKAGE = 4
DEPLOYMENT = 5
DISCOVERY = 6
ATTESTATION = 7


_RELATEDURL = _descriptor.Descriptor(
    name="RelatedUrl",
    full_name="grafeas.v1.RelatedUrl",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="url",
            full_name="grafeas.v1.RelatedUrl.url",
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
        ),
        _descriptor.FieldDescriptor(
            name="label",
            full_name="grafeas.v1.RelatedUrl.label",
            index=1,
            number=2,
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
    serialized_start=45,
    serialized_end=85,
)


_SIGNATURE = _descriptor.Descriptor(
    name="Signature",
    full_name="grafeas.v1.Signature",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="signature",
            full_name="grafeas.v1.Signature.signature",
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
            name="public_key_id",
            full_name="grafeas.v1.Signature.public_key_id",
            index=1,
            number=2,
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
    serialized_start=87,
    serialized_end=140,
)

DESCRIPTOR.message_types_by_name["RelatedUrl"] = _RELATEDURL
DESCRIPTOR.message_types_by_name["Signature"] = _SIGNATURE
DESCRIPTOR.enum_types_by_name["NoteKind"] = _NOTEKIND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RelatedUrl = _reflection.GeneratedProtocolMessageType(
    "RelatedUrl",
    (_message.Message,),
    dict(
        DESCRIPTOR=_RELATEDURL,
        __module__="grafeas_v1.proto.common_pb2",
        __doc__="""Metadata for any related URL information.
  
  
  Attributes:
      url:
          Specific URL associated with the resource.
      label:
          Label to describe usage of the URL.
  """,
        # @@protoc_insertion_point(class_scope:grafeas.v1.RelatedUrl)
    ),
)
_sym_db.RegisterMessage(RelatedUrl)

Signature = _reflection.GeneratedProtocolMessageType(
    "Signature",
    (_message.Message,),
    dict(
        DESCRIPTOR=_SIGNATURE,
        __module__="grafeas_v1.proto.common_pb2",
        __doc__="""Verifiers (e.g. Kritis implementations) MUST verify signatures with
  respect to the trust anchors defined in policy (e.g. a Kritis policy).
  Typically this means that the verifier has been configured with a map
  from ``public_key_id`` to public key material (and any required
  parameters, e.g. signing algorithm).
  
  In particular, verification implementations MUST NOT treat the signature
  ``public_key_id`` as anything more than a key lookup hint. The
  ``public_key_id`` DOES NOT validate or authenticate a public key; it
  only provides a mechanism for quickly selecting a public key ALREADY
  CONFIGURED on the verifier through a trusted channel. Verification
  implementations MUST reject signatures in any of the following
  circumstances: \* The ``public_key_id`` is not recognized by the
  verifier. \* The public key that ``public_key_id`` refers to does not
  verify the signature with respect to the payload.
  
  The ``signature`` contents SHOULD NOT be "attached" (where the payload
  is included with the serialized ``signature`` bytes). Verifiers MUST
  ignore any "attached" payload and only verify signatures with respect to
  explicitly provided payload (e.g. a ``payload`` field on the proto
  message that holds this Signature, or the canonical serialization of the
  proto message that holds this signature).
  
  
  Attributes:
      signature:
          The content of the signature, an opaque bytestring. The
          payload that this signature verifies MUST be unambiguously
          provided with the Signature during verification. A wrapper
          message might provide the payload explicitly. Alternatively, a
          message might have a canonical serialization that can always
          be unambiguously computed to derive the payload.
      public_key_id:
          The identifier for the public key that verifies this
          signature. \* The ``public_key_id`` is required. \* The
          ``public_key_id`` MUST be an RFC3986 conformant URI. \* When
          possible, the ``public_key_id`` SHOULD be an immutable
          reference, such as a cryptographic digest.  Examples of valid
          ``public_key_id``\ s:  OpenPGP V4 public key fingerprint: \*
          "openpgp4fpr:74FAF3B861BDA0870C7B6DEF607E48D2A663AEEA" See
          https://www.iana.org/assignments/uri-schemes/prov/openpgp4fpr
          for more details on this scheme.  RFC6920 digest-named
          SubjectPublicKeyInfo (digest of the DER serialization): \*
          "ni:///sha-256;cD9o9Cq6LG3jD0iKXqEi\_vdjJGecm\_iXkbqVoScViaU"
          \* "nih:///sha-256;703f68f42aba2c6de30f488a5ea122fef76324679c9
          bf89791ba95a1271589a5"
  """,
        # @@protoc_insertion_point(class_scope:grafeas.v1.Signature)
    ),
)
_sym_db.RegisterMessage(Signature)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
