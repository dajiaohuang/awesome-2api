"""Check the catalog's public reference URLs without downloading response bodies."""

from __future__ import annotations

import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]


def check(url: str) -> tuple[str, str]:
    request = Request(url, method="HEAD", headers={"User-Agent": "awesome-2api-link-check/1.0"})
    try:
        with urlopen(request, timeout=20) as response:
            return url, str(response.status)
    except HTTPError as error:
        return url, f"HTTP {error.code}"
    except URLError as error:
        return url, f"URL error: {error.reason}"
    except Exception as error:  # pragma: no cover - network-specific fallback
        return url, f"error: {error}"


def main() -> None:
    document = json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))
    urls = sorted(
        {
            url.strip()
            for entry in document["entries"]
            for url in entry["参考URL"].splitlines()
            if url.strip()
        }
    )
    results: list[tuple[str, str]] = []
    with ThreadPoolExecutor(max_workers=12) as executor:
        futures = [executor.submit(check, url) for url in urls]
        for future in as_completed(futures):
            results.append(future.result())
    results.sort()
    failures = [(url, status) for url, status in results if not status.isdigit() or not status.startswith("2")]
    for url, status in failures:
        print(f"{status}\t{url}")
    print(f"Checked {len(results)} URLs; {len(failures)} non-2xx or unavailable")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
