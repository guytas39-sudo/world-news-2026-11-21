#!/usr/bin/env python3
"""Entrypoint for 'The World Today' — 21 November 2026.

The front page is drawn at build time by draw_image.py and stored as
entry.png next to this file. All this program does is place that image
in the output directory. It uses only the Python standard library.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(target_dir, exist_ok=True)
    dest = os.path.join(target_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    print("wrote", dest)


if __name__ == "__main__":
    main()
