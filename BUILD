# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

cc_library(
    name = "module_header_release",
    visibility = ["//visibility:public"],
    deps = ["@emacs_module_header_release//:header"],
)

cc_library(
    name = "module_header_master",
    visibility = ["//visibility:public"],
    deps = ["@emacs_module_header_master//:header"],
)

py_binary(
    name = "genheader",
    srcs = ["genheader.py"],
    python_version = "PY3",
    srcs_version = "PY3",
    visibility = ["@emacs_module_header_master//:__pkg__"],
)

# Smoke tests to check whether the header can be included.
cc_test(
    name = "release_test",
    srcs = ["test.c"],
    deps = [":module_header_release"],
)

cc_test(
    name = "master_test",
    srcs = ["test.c"],
    deps = [":module_header_master"],
)
