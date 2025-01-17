# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grafeas_v1/proto/image.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="grafeas_v1/proto/image.proto",
    package="grafeas.v1",
    syntax="proto3",
    serialized_options=_b(
        "\n\rio.grafeas.v1P\001Z8google.golang.org/genproto/googleapis/grafeas/v1;grafeas\242\002\003GRA"
    ),
    serialized_pb=_b(
        '\n\x1cgrafeas_v1/proto/image.proto\x12\ngrafeas.v1"-\n\x05Layer\x12\x11\n\tdirective\x18\x01 \x01(\t\x12\x11\n\targuments\x18\x02 \x01(\t"@\n\x0b\x46ingerprint\x12\x0f\n\x07v1_name\x18\x01 \x01(\t\x12\x0f\n\x07v2_blob\x18\x02 \x03(\t\x12\x0f\n\x07v2_name\x18\x03 \x01(\t"O\n\tImageNote\x12\x14\n\x0cresource_url\x18\x01 \x01(\t\x12,\n\x0b\x66ingerprint\x18\x02 \x01(\x0b\x32\x17.grafeas.v1.Fingerprint"\x93\x01\n\x0fImageOccurrence\x12,\n\x0b\x66ingerprint\x18\x01 \x01(\x0b\x32\x17.grafeas.v1.Fingerprint\x12\x10\n\x08\x64istance\x18\x02 \x01(\x05\x12%\n\nlayer_info\x18\x03 \x03(\x0b\x32\x11.grafeas.v1.Layer\x12\x19\n\x11\x62\x61se_resource_url\x18\x04 \x01(\tBQ\n\rio.grafeas.v1P\x01Z8google.golang.org/genproto/googleapis/grafeas/v1;grafeas\xa2\x02\x03GRAb\x06proto3'
    ),
)


_LAYER = _descriptor.Descriptor(
    name="Layer",
    full_name="grafeas.v1.Layer",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="directive",
            full_name="grafeas.v1.Layer.directive",
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
            name="arguments",
            full_name="grafeas.v1.Layer.arguments",
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
    serialized_start=44,
    serialized_end=89,
)


_FINGERPRINT = _descriptor.Descriptor(
    name="Fingerprint",
    full_name="grafeas.v1.Fingerprint",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="v1_name",
            full_name="grafeas.v1.Fingerprint.v1_name",
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
            name="v2_blob",
            full_name="grafeas.v1.Fingerprint.v2_blob",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
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
        _descriptor.FieldDescriptor(
            name="v2_name",
            full_name="grafeas.v1.Fingerprint.v2_name",
            index=2,
            number=3,
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
    serialized_start=91,
    serialized_end=155,
)


_IMAGENOTE = _descriptor.Descriptor(
    name="ImageNote",
    full_name="grafeas.v1.ImageNote",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="resource_url",
            full_name="grafeas.v1.ImageNote.resource_url",
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
            name="fingerprint",
            full_name="grafeas.v1.ImageNote.fingerprint",
            index=1,
            number=2,
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
    serialized_start=157,
    serialized_end=236,
)


_IMAGEOCCURRENCE = _descriptor.Descriptor(
    name="ImageOccurrence",
    full_name="grafeas.v1.ImageOccurrence",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="fingerprint",
            full_name="grafeas.v1.ImageOccurrence.fingerprint",
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
        ),
        _descriptor.FieldDescriptor(
            name="distance",
            full_name="grafeas.v1.ImageOccurrence.distance",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="layer_info",
            full_name="grafeas.v1.ImageOccurrence.layer_info",
            index=2,
            number=3,
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
        _descriptor.FieldDescriptor(
            name="base_resource_url",
            full_name="grafeas.v1.ImageOccurrence.base_resource_url",
            index=3,
            number=4,
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
    serialized_start=239,
    serialized_end=386,
)

_IMAGENOTE.fields_by_name["fingerprint"].message_type = _FINGERPRINT
_IMAGEOCCURRENCE.fields_by_name["fingerprint"].message_type = _FINGERPRINT
_IMAGEOCCURRENCE.fields_by_name["layer_info"].message_type = _LAYER
DESCRIPTOR.message_types_by_name["Layer"] = _LAYER
DESCRIPTOR.message_types_by_name["Fingerprint"] = _FINGERPRINT
DESCRIPTOR.message_types_by_name["ImageNote"] = _IMAGENOTE
DESCRIPTOR.message_types_by_name["ImageOccurrence"] = _IMAGEOCCURRENCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Layer = _reflection.GeneratedProtocolMessageType(
    "Layer",
    (_message.Message,),
    dict(
        DESCRIPTOR=_LAYER,
        __module__="grafeas_v1.proto.image_pb2",
        __doc__="""Layer holds metadata specific to a layer of a Docker image.
  
  
  Attributes:
      directive:
          Required. The recovered Dockerfile directive used to construct
          this layer. See
          https://docs.docker.com/engine/reference/builder/ for more
          information.
      arguments:
          The recovered arguments to the Dockerfile directive.
  """,
        # @@protoc_insertion_point(class_scope:grafeas.v1.Layer)
    ),
)
_sym_db.RegisterMessage(Layer)

Fingerprint = _reflection.GeneratedProtocolMessageType(
    "Fingerprint",
    (_message.Message,),
    dict(
        DESCRIPTOR=_FINGERPRINT,
        __module__="grafeas_v1.proto.image_pb2",
        __doc__="""A set of properties that uniquely identify a given Docker image.
  
  
  Attributes:
      v1_name:
          Required. The layer ID of the final layer in the Docker
          image's v1 representation.
      v2_blob:
          Required. The ordered list of v2 blobs that represent a given
          image.
      v2_name:
          Output only. The name of the image's v2 blobs computed via:
          [bottom] := v2\_blob[bottom][N] := sha256(v2\_blob[N] + " " +
          v2\_name[N+1]) Only the name of the final blob is kept.
  """,
        # @@protoc_insertion_point(class_scope:grafeas.v1.Fingerprint)
    ),
)
_sym_db.RegisterMessage(Fingerprint)

ImageNote = _reflection.GeneratedProtocolMessageType(
    "ImageNote",
    (_message.Message,),
    dict(
        DESCRIPTOR=_IMAGENOTE,
        __module__="grafeas_v1.proto.image_pb2",
        __doc__="""Basis describes the base image portion (Note) of the DockerImage
  relationship. Linked occurrences are derived from this or an equivalent
  image via: FROM Or an equivalent reference, e.g., a tag of the
  resource\_url.
  
  
  Attributes:
      resource_url:
          Required. Immutable. The resource\_url for the resource
          representing the basis of associated occurrence images.
      fingerprint:
          Required. Immutable. The fingerprint of the base image.
  """,
        # @@protoc_insertion_point(class_scope:grafeas.v1.ImageNote)
    ),
)
_sym_db.RegisterMessage(ImageNote)

ImageOccurrence = _reflection.GeneratedProtocolMessageType(
    "ImageOccurrence",
    (_message.Message,),
    dict(
        DESCRIPTOR=_IMAGEOCCURRENCE,
        __module__="grafeas_v1.proto.image_pb2",
        __doc__="""Details of the derived image portion of the DockerImage relationship.
  This image would be produced from a Dockerfile with FROM .
  
  
  Attributes:
      fingerprint:
          Required. The fingerprint of the derived image.
      distance:
          Output only. The number of layers by which this image differs
          from the associated image basis.
      layer_info:
          This contains layer-specific metadata, if populated it has
          length "distance" and is ordered with [distance] being the
          layer immediately following the base image and [1] being the
          final layer.
      base_resource_url:
          Output only. This contains the base image URL for the derived
          image occurrence.
  """,
        # @@protoc_insertion_point(class_scope:grafeas.v1.ImageOccurrence)
    ),
)
_sym_db.RegisterMessage(ImageOccurrence)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
