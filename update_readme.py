#!/usr/bin/python3
#
# Copyright 2020 Google LLC
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

import hashlib
import pathlib
import re
import ssl
import subprocess
import urllib.request

import certifi


def main() -> None:
    def_bzl = pathlib.Path('def.bzl').read_text('utf-8')
    release_version = re.search(r'urls = \["https://ftp.gnu.org/gnu/emacs/emacs-([.0-9]+).tar.xz"\]', def_bzl).group(1)
    master_version = re.search(r'urls = \["https://git.savannah.gnu.org/cgit/emacs.git/snapshot/emacs-([0-9A-Fa-f]+).tar.gz"\]', def_bzl).group(1)
    readme = pathlib.Path('README.md')
    text = readme.read_text('utf-8')
    commit = subprocess.run(['git', 'rev-parse', '--verify', 'HEAD'],
                            stdout=subprocess.PIPE, check=True, encoding='ascii').stdout.rstrip('\n')
    url = f'https://github.com/phst/emacs-bazel/archive/{commit}.zip'
    context = ssl.create_default_context(cafile=certifi.where())
    with urllib.request.urlopen(url, context=context) as archive:
        sha256 = hashlib.sha256(archive.read()).hexdigest()
    for pat, rep in ((r'Emacs ([.0-9]+)\.', release_version),
                     (r'commit ([0-9A-Fa-f]+)\.', master_version),
                     (r'sha256 = "(.*)"', sha256),
                     (r'urls = \["(.*)"\]', url),
                     (r'strip_prefix = "(.*)"', f'emacs-bazel-{commit}/')):
        start, end = re.search(pat, text).span(1)
        text = text[:start] + rep + text[end:]
    readme.write_text(text, 'utf-8')


if __name__ == '__main__':
    main()
