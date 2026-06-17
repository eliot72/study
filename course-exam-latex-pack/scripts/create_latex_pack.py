#!/usr/bin/env python3
"""Create a three-PDF LaTeX exam-prep pack from the bundled template."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def copy_template(output: Path, force: bool) -> None:
    skill_dir = Path(__file__).resolve().parents[1]
    template = skill_dir / "assets" / "latex-pack-template"
    if not template.exists():
        raise SystemExit(f"Template not found: {template}")

    if output.exists():
        if not force:
            raise SystemExit(f"Output already exists: {output}. Pass --force to overwrite.")
        shutil.rmtree(output)

    shutil.copytree(template, output)


def replace_metadata(output: Path, course: str, author: str) -> None:
    metadata = output / "content" / "metadata.tex"
    text = metadata.read_text(encoding="utf-8")
    text = text.replace("__COURSE_TITLE__", course)
    text = text.replace("__AUTHOR_MARK__", author)
    metadata.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, help="Directory to create.")
    parser.add_argument("--course", required=True, help="Course title used in headers and titles.")
    parser.add_argument("--author", default="Codex", help="Short mark used in page headers.")
    parser.add_argument("--force", action="store_true", help="Overwrite the output directory.")
    args = parser.parse_args()

    output = Path(args.output).expanduser().resolve()
    copy_template(output, args.force)
    replace_metadata(output, args.course, args.author)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
