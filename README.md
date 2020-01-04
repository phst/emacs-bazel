This repository contains [Bazel](https://bazel.build/) targets for the
[GNU Emacs](https://www.gnu.org/software/emacs/) `emacs-module.h` header file.
Using these targets you can compile dynamic modules for Emacs using Bazel.  To
use, add the following to your [WORKSPACE
file](https://docs.bazel.build/versions/master/external.html):

```python
http_archive(
    name = "phst_emacs",
    sha256 = "8efac2440a8e98a08b9e79a378ad33b7475a8e1dfcda909b45e4fc715cb0cc78",
    strip_prefix = "emacs-bazel-9e7722694cf5239ab53dc12b70ed795f08c03f8d/",
    urls = ["https://github.com/phst/emacs-bazel/archive/9e7722694cf5239ab53dc12b70ed795f08c03f8d.zip"],
)

load("@phst_emacs//:def.bzl", "phst_emacs_repos")

phst_emacs_repos()
```

Then you can use the following
[`cc_library`](https://docs.bazel.build/versions/master/be/c-cpp.html#cc_library)
targets:

-   `@phst_emacs//:module_header_release` exports `emacs-module.h` for the
    latest stable Emacs release.  Currently, this is Emacs 26.3.

-   `@phst_emacs//:module_header_master` exports `emacs-module.h` for a recent
    version of the upstream master branch.  Currently, this uses
    commit 52db14b0dc5a93d7a7219917b8f603b14f94f24f.

That way you can test your module with both the release and the upstream
version of Emacs independently.

This is not an officially supported Google product.

