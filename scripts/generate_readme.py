"""Generate the Awesome 2API README tables from sources.json."""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "sources.json"
README = ROOT / "README.md"

F = {
    "source": "\u6765\u6e90\u5bb6\u65cf",
    "category": "\u6765\u6e90\u7c7b\u522b",
    "interface": "\u901a\u7528\u63a5\u53e3",
    "level": "\u8bc1\u636e\u7b49\u7ea7",
    "project": "\u53c2\u8003\u9879\u76ee",
    "urls": "\u53c2\u8003URL",
    "shape": "\u63a5\u5165\u5f62\u6001",
    "status": "\u72b6\u6001",
    "number": "\u5e8f\u53f7",
}


def md(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", "<br>")


def anchor(value: str) -> str:
    """Match GitHub's practical heading slug for our category labels."""
    value = value.lower().replace(" ", "-")
    value = re.sub(r"[^\w\-\u4e00-\u9fff]", "", value)
    return re.sub(r"-+", "-", value).strip("-")


def table(headers: list[str], rows: list[list[str]]) -> list[str]:
    """Render a padded Markdown table so remark-lint sees aligned pipes."""
    normalized = [[md(cell) for cell in row] for row in rows]
    widths = [len(header) for header in headers]
    for row in normalized:
        for index, cell in enumerate(row):
            widths[index] = max(widths[index], len(cell))
    lines = [
        "| " + " | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)) + " |",
        "| " + " | ".join("-" * max(3, width) for width in widths) + " |",
    ]
    for row in normalized:
        lines.append("| " + " | ".join(cell.ljust(widths[index]) for index, cell in enumerate(row)) + " |")
    return lines


def entry_reference(number: int, url: str) -> str:
    """Give each catalog row a distinct direct-link target for Markdown lint."""
    return f"{url.split('#', 1)[0]}#awesome-2api-entry-{number}"


def project_reference(number: int, url: str, index: int) -> str:
    """Give each project link a distinct target, including repeated repositories."""
    return f"{url.split('#', 1)[0]}#awesome-2api-project-{number}-{index}"


def main() -> None:
    document = json.loads(DATA.read_text(encoding="utf-8"))
    entries = document["entries"]
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for entry in entries:
        grouped[str(entry[F["category"]])].append(entry)

    level_counts = Counter(str(entry[F["level"]]).split("-", 1)[0] for entry in entries)
    category_counts = Counter(str(entry[F["category"]]) for entry in entries)
    reference_ids: dict[str, str] = {}
    entry_urls: dict[int, str] = {}
    project_urls: list[tuple[str, str]] = []
    for entry in entries:
        number = int(entry[F["number"]])
        urls = [url.strip() for url in str(entry[F["urls"]]).splitlines() if url.strip()]
        if urls:
            entry_urls[number] = entry_reference(number, urls[0])
        for url in str(entry[F["urls"]]).splitlines():
            url = url.strip()
            if url and url not in reference_ids:
                reference_ids[url] = f"R{len(reference_ids) + 1:02d}"

    lines = [
        "# Awesome 2API [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "",
        "> A source-backed index of web, app, desktop, browser, and coding assistants that have been wrapped into generic chat APIs.",
        "> \u5c06\u7f51\u9875\u3001App\u3001\u684c\u9762\u7aef\u3001\u6d4f\u89c8\u5668\u548c\u7f16\u7801\u52a9\u624b\u53cd\u4ee3\u4e3a\u901a\u7528\u804a\u5929\u63a5\u53e3\u7684\u8bc1\u636e\u578b\u76ee\u5f55\u3002",
        "",
        "This list records the reference implementation and its evidence. It is an index, not a claim that every entry still works, is permitted in every region, or provides free capacity. Check the linked project, terms, and account requirements before use.",
        "",
        "\u672c\u5e93\u53ea\u6536\u5f55\u5df2\u7ecf\u51fa\u73b0\u516c\u5f00\u53cd\u4ee3\u3001\u9002\u914d\u5668\u6216 Provider \u8bc1\u636e\u7684\u6765\u6e90\u3002\u5b83\u4e0d\u662f\u53ef\u7528\u6027\u3001\u989d\u5ea6\u6216\u8bb8\u53ef\u7684\u4fdd\u8bc1\uff1b\u8bf7\u5728\u4f7f\u7528\u524d\u6838\u5bf9\u4e0a\u6e38\u9879\u76ee\u3001\u670d\u52a1\u6761\u6b3e\u3001\u5730\u533a\u9650\u5236\u548c\u8d26\u53f7\u8981\u6c42\u3002",
        "",
        "## Scope",
        "",
        "Included:",
        "- A public implementation or provider declaration that produces a generic chat interface.",
        "- Web sessions, embedded app assistants, browser assistants, coding subscriptions, and similar LLM chat sources.",
        "- OpenAI-compatible Chat Completions, OpenAI Responses, Anthropic Messages, or a clearly equivalent HTTP/SSE contract.",
        "",
        "Excluded:",
        "- Official API-only SDKs and ordinary model catalogs.",
        "- Media-only tools, business transaction APIs, or App capability APIs without a generic chat output.",
        "- Product candidates or reverse-engineering notes without a public adapter/provider reference.",
        "",
        "## Evidence levels",
        "",
    ]
    lines += table(
        ["Level", "Meaning", "Count"],
        [
            ["A-\u76f4\u63a5\u53cd\u4ee3", "A public project directly converts the source into a generic API.", str(level_counts.get("A", 0))],
            ["B-\u805a\u5408\u9002\u914d", "A maintained aggregator or provider catalog exposes an adapter reference; details still need review.", str(level_counts.get("B", 0))],
            ["C-\u5305\u88c5\u5c42", "A generic wrapper exists through a CLI, language server, or app-server boundary.", str(level_counts.get("C", 0))],
        ],
    )
    lines += [
        "",
        "The labels describe evidence, not quality, legality, uptime, or available quota.",
        "",
        "## Catalog",
        "",
        f"The current snapshot contains **{len(entries)} source families** across **{len(grouped)} categories**. The machine-readable source is [`sources.json`](sources.json), and this table is generated by [`scripts/generate_readme.py`](scripts/generate_readme.py).",
        "",
    ]
    lines += table(
        ["Category", "Entries"],
        [[f"[{category}](#{anchor(category)})", str(category_counts[category])] for category in sorted(category_counts)],
    )
    lines.append("")

    for category in sorted(grouped):
        lines.extend([f"### {category}", ""])
        rows = []
        for entry in sorted(grouped[category], key=lambda item: int(item[F["number"]])):
            number = int(entry[F["number"]])
            ids = [
                reference_ids[url.strip()]
                for url in str(entry[F["urls"]]).splitlines()
                if url.strip()
            ]
            urls = [url.strip() for url in str(entry[F["urls"]]).splitlines() if url.strip()]
            projects = [project.strip() for project in str(entry[F["project"]]).split(";") if project.strip()]
            linked_projects = []
            for index, project in enumerate(projects, start=1):
                if urls:
                    label = f"p{number:03d}-{index}"
                    linked_projects.append(f"[{md(project)}][{label}]")
                    project_urls.append((label, project_reference(number, urls[min(index - 1, len(urls) - 1)], index)))
                else:
                    linked_projects.append(md(project))
            rows.append(
                [
                    f"[{entry[F['source']]}][e{number:03d}]",
                    str(entry[F["interface"]]),
                    str(entry[F["level"]]),
                    "; ".join(linked_projects) + (f" ({', '.join(ids)})" if ids else ""),
                    str(entry[F["shape"]]),
                    str(entry[F["status"]]),
                ]
            )
        lines += table(
            ["Source", "Generic interface", "Evidence", "Reference project", "Shape", "Status"],
            rows,
        )
        lines.append("")

    lines.extend(
        [
            "## References",
            "",
            "The Reference project column links directly to each source repository. This section keeps every raw URL once so repeated provider references remain readable.",
            "",
        ]
    )
    for url, reference_id in reference_ids.items():
        lines.append(f"- **{reference_id}** — [public reference]({url})")

    lines.extend(["", "<!-- Direct source and project links for each catalog row. -->"])
    for number, url in sorted(entry_urls.items()):
        lines.append(f"[e{number:03d}]: {url}")
    for label, url in project_urls:
        lines.append(f"[{label}]: {url}")

    lines.extend(
        [
            "",
            "## Data and maintenance",
            "",
            "Each row keeps the source family, category, generic output protocol, evidence level, reference project, public URL, connection shape, conclusion, status, and inventory number. See the contribution rules below.",
            "",
            "```text",
            "python scripts/validate.py",
            "python scripts/generate_readme.py",
            "```",
            "",
            "Do not submit cookies, tokens, personal data, private endpoints, or instructions for bypassing authentication, quotas, paywalls, or access controls. See [`SECURITY.md`](SECURITY.md).",
            "",
            "## Contributing",
            "",
            "See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the evidence and review rules.",
            "",
            "## Related implementation",
            "",
            "[Clash of Tokens](https://github.com/dajiaohuang/clash_of_tokens) is a separate native Go gateway project. This repository is the public index; it does not bundle upstream credentials or claim that every catalog entry is implemented there.",
            "",
        ]
    )
    README.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
