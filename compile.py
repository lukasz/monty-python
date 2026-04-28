#!/usr/bin/env python3
"""Monty Python compiler — turns .mpy files into vanilla .py files.

Walks the input directory configured in monty-config.json, tokenises each
.mpy source, rewrites NAME tokens that appear in the keyword map, and writes
the result to the output directory. Tokenising (rather than naive string
replace) means identifiers inside string literals and comments are left
alone.
"""
from __future__ import annotations

import io
import json
import sys
import tokenize
from pathlib import Path

KEYWORDS: dict[str, str] = {
    "summon": "def",
    "upper_class": "class",
    "perchance": "if",
    "or_perchance": "elif",
    "otherwise": "else",
    "merry_go_round": "for",
    "whilst": "while",
    "Indeed": "True",
    "Poppycock": "False",
    "Naught": "None",
    "announce": "print",
    "give_back": "return",
    "fetch": "import",
    "from_yonder": "from",
    "would_you_mind": "try",
    "actually_i_do_mind": "except",
    "throw_a_wobbly": "raise",
    "quickie": "lambda",
    "nevermind": "pass",
    "splendid": "break",
    "carry_on": "continue",
    "and_also": "and",
    "or_alternatively": "or",
    "not_at_all": "not",
    "amongst": "in",
    "be": "is",
    "oneself": "self",
    "summoning_ritual": "__init__",
    "nobody_expects": "assert",
}


def compile_source(src: str) -> str:
    lines = src.splitlines(keepends=True)
    edits_by_line: dict[int, list[tuple[int, int, str]]] = {}
    tokens = tokenize.tokenize(io.BytesIO(src.encode("utf-8")).readline)
    for tok in tokens:
        if tok.type == tokenize.NAME and tok.string in KEYWORDS:
            line_idx = tok.start[0] - 1
            edits_by_line.setdefault(line_idx, []).append(
                (tok.start[1], tok.end[1], KEYWORDS[tok.string])
            )
    for line_idx, edits in edits_by_line.items():
        line = lines[line_idx]
        for col_start, col_end, replacement in sorted(edits, reverse=True):
            line = line[:col_start] + replacement + line[col_end:]
        lines[line_idx] = line
    return "".join(lines)


def main() -> int:
    root = Path(__file__).resolve().parent
    config = json.loads((root / "monty-config.json").read_text())
    in_dir = (root / config["input_directory"]).resolve()
    out_dir = (root / config["output_directory"]).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    sources = sorted(in_dir.rglob("*.mpy"))
    if not sources:
        print(f"No .mpy files found in {in_dir}")
        return 1

    for src_path in sources:
        rel = src_path.relative_to(in_dir).with_suffix(".py")
        out_path = out_dir / rel
        out_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            compiled = compile_source(src_path.read_text())
        except tokenize.TokenizeError as exc:
            print(f"Tokenise error in {src_path}: {exc}", file=sys.stderr)
            return 1
        out_path.write_text(compiled)
        print(f"  {src_path.relative_to(root)} -> {out_path.relative_to(root)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
