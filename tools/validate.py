#!/usr/bin/env python3
"""Validate OSP profiles against the OSP JSON Schema.

Usage:
    python tools/validate.py profile.json [more.json ...]
    python tools/validate.py examples/EXAMPLES.md README.md

For .json files, the file must contain one OSP profile.
For .md files, every ```json block that looks like a profile (has "scent_id"
and "profile") is validated; other blocks (sessions, API payloads) are skipped.

Exit code: 0 when everything is valid, 1 when any profile is invalid.
Requires: pip install "jsonschema[format]"
"""

import json
import re
import sys
from pathlib import Path

from jsonschema import Draft7Validator, FormatChecker

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "schema" / "osp-profile-v1.1.json"
JSON_BLOCK = re.compile(r"```json\s*\n(.*?)```", re.DOTALL)


def load_validator():
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft7Validator.check_schema(schema)
    return Draft7Validator(schema, format_checker=FormatChecker())


def profiles_in(path):
    """Yield (label, profile) pairs found in a .json or .md file."""
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".json":
        yield str(path), json.loads(text)
        return
    for match in JSON_BLOCK.finditer(text):
        line = text.count("\n", 0, match.start()) + 1
        try:
            data = json.loads(match.group(1))
        except json.JSONDecodeError:
            continue  # illustrative snippet, not a complete document
        if isinstance(data, dict) and "scent_id" in data and "profile" in data:
            yield f"{path}:{line}", data


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    validator = load_validator()
    checked = failed = 0
    for arg in argv:
        for label, profile in profiles_in(Path(arg)):
            checked += 1
            errors = sorted(validator.iter_errors(profile), key=lambda e: list(e.path))
            if errors:
                failed += 1
                print(f"INVALID {label} ({profile.get('scent_id', '?')})")
                for error in errors:
                    where = "/".join(str(p) for p in error.path) or "(root)"
                    print(f"    {where}: {error.message}")
            else:
                print(f"ok      {label} ({profile['scent_id']})")
    print(f"\n{checked} profile(s) checked, {failed} invalid")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
