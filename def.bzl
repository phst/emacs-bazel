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

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

def eu_phst_emacs_repos():
    """Adds repositories needed for the eu_phst_emacs workspace."""
    http_archive(
        name = "emacs_module_header_release",
        build_file = "@eu_phst_emacs//:release.BUILD",
        sha256 = "4d90e6751ad8967822c6e092db07466b9d383ef1653feb2f95c93e7de66d3485",
        strip_prefix = "emacs-26.3/src/",
        urls = ["https://ftp.gnu.org/gnu/emacs/emacs-26.3.tar.xz"],
    )
    http_archive(
        name = "emacs_module_header_master",
        build_file = "@eu_phst_emacs//:master.BUILD",
        sha256 = "e80ff4fae6350e295732b40ad74820f1c6ed404547abc7fe57ff7349ecc6d297",
        strip_prefix = "emacs-52db14b0dc5a93d7a7219917b8f603b14f94f24f/src/",
        urls = ["https://git.savannah.gnu.org/cgit/emacs.git/snapshot/emacs-52db14b0dc5a93d7a7219917b8f603b14f94f24f.tar.gz"],
    )
