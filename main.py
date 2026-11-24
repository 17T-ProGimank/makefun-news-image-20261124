"""news-image-20261124 entrypoint.

Copies the pre-rendered poster (entry.png, 1024x1024, drawn offline) to
$MAKEFUN_OUTPUT_DIR/entry.png. Standard library only: the grader's Python
image ships no Pillow and no system fonts, so the poster is rendered
locally beforehand and committed at the repository root.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # sanity guard: the gate refuses anything over 1 MiB or 1024x1024
    if os.path.getsize(dst) > 1048576:
        print("entry.png exceeds 1 MiB", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes)" % (dst, os.path.getsize(dst)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
