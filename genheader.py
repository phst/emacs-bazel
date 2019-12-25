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

import argparse
import pathlib
import re
from typing import Tuple

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--template', type=pathlib.Path)
    parser.add_argument('--output', type=pathlib.Path)
    parser.add_argument('snippets', type=_snippet, nargs='+')
    args = parser.parse_args()
    snippets = dict(args.snippets)
    newest_version = max(snippets.keys())
    output = args.template.read_text('utf-8').replace(
        '@emacs_major_version@', str(newest_version))
    for version, snippet in snippets.items():
        output = output.replace(f'@module_env_snippet_{version}@', snippet)
    args.output.write_text(output, 'utf-8')

def _snippet(arg: str) -> Tuple[int, str]:
    path = pathlib.Path(arg)
    match = re.match(r'^module-env-(\d+)\.h$', path.name)
    if not match:
        raise ValueError(f'unexpected argument {arg}')
    version = int(match.group(1))
    if version <= 0:
        raise ValueError(f'unexpected argument {arg}')
    return version, path.read_text('utf-8')

if __name__ == '__main__':
    main()
