"""Validate the machine-readable Awesome 2API catalog."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "sources.json"

REQUIRED = {
    "来源家族",
    "来源类别",
    "通用接口",
    "证据等级",
    "参考项目",
    "参考URL",
    "接入形态",
    "本轮结论",
    "状态",
    "序号",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    try:
        document = json.loads(DATA.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot read {DATA}: {exc}")

    entries = document.get("entries")
    if not isinstance(entries, list) or not entries:
        fail("entries must be a non-empty array")
    if document.get("count") != len(entries):
        fail(f"count={document.get('count')} but entries={len(entries)}")

    names: set[str] = set()
    numbers: set[int] = set()
    urls: set[str] = set()
    for index, entry in enumerate(entries, start=1):
        if not isinstance(entry, dict):
            fail(f"entry {index} is not an object")
        missing = REQUIRED - entry.keys()
        if missing:
            fail(f"entry {index} is missing: {', '.join(sorted(missing))}")
        name = entry["来源家族"]
        if name in names:
            fail(f"duplicate source family: {name}")
        names.add(name)
        number = entry["序号"]
        if not isinstance(number, int) or number in numbers:
            fail(f"invalid or duplicate 序号 at entry {index}: {number!r}")
        numbers.add(number)
        references = [part.strip() for part in entry["参考URL"].splitlines() if part.strip()]
        if not references:
            fail(f"entry {index} has no reference URL")
        for url in references:
            parsed = urlsplit(url)
            if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                fail(f"invalid reference URL in {name}: {url}")
            urls.add(url)

    if sorted(numbers) != list(range(1, len(entries) + 1)):
        fail("序号 must be a contiguous 1..count sequence")

    print(f"OK: {len(entries)} entries, {len(urls)} unique reference URLs")


if __name__ == "__main__":
    main()
