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

workspace(name = "eu_phst_emacs")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "emacs_module_header_26",
    build_file = "@//:release.BUILD",
    sha256 = "4d90e6751ad8967822c6e092db07466b9d383ef1653feb2f95c93e7de66d3485",
    strip_prefix = "emacs-26.3/src/",
    urls = ["https://ftp.gnu.org/gnu/emacs/emacs-26.3.tar.xz"],
)

http_archive(
    name = "emacs_module_header_master",
    build_file = "@//:master.BUILD",
    sha256 = "22ce644ca8c808425e43243823fb996b05fa824ff93ca82fb86611bfe9b3fe2c",
    strip_prefix = "emacs-7c5d6a2afc6c23a7fff8456f506ee2aa2d37a3b9/src/",
    urls = ["https://git.savannah.gnu.org/cgit/emacs.git/snapshot/emacs-7c5d6a2afc6c23a7fff8456f506ee2aa2d37a3b9.tar.gz"],
)
