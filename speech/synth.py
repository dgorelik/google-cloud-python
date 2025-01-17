# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This script is used to synthesize generated parts of this library."""

import re

import synthtool as s
from synthtool import gcp

gapic = gcp.GAPICGenerator()
common = gcp.CommonTemplates()
versions = ["v1p1beta1", "v1"]


# ----------------------------------------------------------------------------
# Generate speech GAPIC layer
# ----------------------------------------------------------------------------
for version in versions:
    library = gapic.py_library("speech", version, include_protos=True)

    # Don't move over __init__.py, as we modify it to make the generated client
    # use helpers.py.
    s.move(library / f"google/cloud/speech_{version}/types.py")
    s.move(library / f"google/cloud/speech_{version}/gapic")
    s.move(library / f"google/cloud/speech_{version}/proto")
    s.move(library / f"tests/unit/gapic/{version}")
    s.move(library / f"docs/gapic/{version}")


# Use the highest version library to generate documentation import alias.
s.move(library / "google/cloud/speech.py")

# Issues exist where python files should define the source encoding
# https://github.com/googleapis/gapic-generator/issues/2097
s.replace("**/proto/*_pb2.py", r"(^.*$\n)*", r"# -*- coding: utf-8 -*-\n\g<0>")


# Fix tests to use the direct gapic client instead of the wrapped helper
# client.
s.replace(
    "tests/unit/**/test*client*.py",
    r"from google\.cloud import speech_(.+?)$",
    r"from google.cloud.speech_\1.gapic import speech_client as speech_\1",
)

# Set the maximum received message size to 256 MiB, the default of 4 MiB is
# often insufficient in practice.
s.replace(
    "google/cloud/speech_v1/gapic/transports/speech_grpc_transport.py",
    r".*scopes=cls\._OAUTH_SCOPES.*",
    """\g<0>
    options={"grpc.max_receive_message_length": 256 * 1024 * 1024}.items()
    """,
)

# ----------------------------------------------------------------------------
# Add templated files
# ----------------------------------------------------------------------------
templated_files = common.py_library(unit_cov_level=97, cov_level=100)
s.move(templated_files)

s.shell.run(["nox", "-s", "blacken"], hide_output=False)
