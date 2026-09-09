"""Generate the compact Awesome 2API README from sources.json."""

from __future__ import annotations

import json
from collections import Counter
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
    return f"{url.split('#', 1)[0]}#awesome-2api-entry-{number}"


def project_reference(number: int, url: str, index: int) -> str:
    return f"{url.split('#', 1)[0]}#awesome-2api-project-{number}-{index}"


def main() -> None:
    document = json.loads(DATA.read_text(encoding="utf-8"))
    entries = sorted(document["entries"], key=lambda item: int(item[F["number"]]))
    levels = Counter(str(entry[F["level"]]).split("-", 1)[0] for entry in entries)
    entry_urls: dict[int, str] = {}
    project_urls: list[tuple[str, str]] = []
    rows: list[list[str]] = []

    for entry in entries:
        number = int(entry[F["number"]])
        urls = [url.strip() for url in str(entry[F["urls"]]).splitlines() if url.strip()]
        if urls:
            entry_urls[number] = entry_reference(number, urls[0])

        projects = [project.strip() for project in str(entry[F["project"]]).split(";") if project.strip()]
        linked_projects: list[str] = []
        for index, project in enumerate(projects, start=1):
            if urls:
                label = f"p{number:03d}-{index}"
                linked_projects.append(f"[{md(project)}][{label}]")
                project_urls.append(
                    (label, project_reference(number, urls[min(index - 1, len(urls) - 1)], index))
                )
            else:
                linked_projects.append(md(project))

        rows.append(
            [
                f"[{md(entry[F['source']])}][e{number:03d}]",
                str(entry[F["category"]]),
                "; ".join(linked_projects),
                str(entry[F["interface"]]),
                str(entry[F["level"]]),
                str(entry[F["shape"]]),
                str(entry[F["status"]]),
            ]
        )

    lines = [
        "# Awesome 2API [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "",
        "> A source-backed index of web, app, desktop, browser, and coding assistants wrapped into generic chat APIs.",
        "> 将网页、App、桌面端、浏览器和编码助手反代为通用聊天接口的证据型目录。",
        "",
        f"**{len(entries)} sources** · **{levels.get('A', 0)} direct adapters** · **{levels.get('B', 0)} aggregator adapters** · **{levels.get('C', 0)} wrapper layers**",
        "",
        "Every row links to its reference project. The catalog only includes public evidence of a generic chat output such as OpenAI-compatible Chat Completions, OpenAI Responses, Anthropic Messages, or an equivalent HTTP/SSE contract.",
        "",
        "不收录官方 API-only SDK、纯媒体/业务工具、只有产品宣传的候选项，或没有公开适配器证据的逆向笔记。链接不代表当前可用性、额度、许可或服务条款允许。",
        "",
        "Machine-readable data: [sources.json](sources.json) · Run Python scripts/generate_readme.py to refresh this table.",
        "",
        "## Catalog",
        "",
    ]
    lines += table(
        ["Source", "Category", "Reference project", "Generic interface", "Evidence", "Shape", "Status"],
        rows,
    )

    # Reference definitions are invisible in the rendered README, while keeping
    # every source and project link clickable without making the table enormous.
    lines.append("")
    for number, url in sorted(entry_urls.items()):
        lines.append(f"[e{number:03d}]: {url}")
    for label, url in project_urls:
        lines.append(f"[{label}]: {url}")

    lines += [
        "",
        "## Contributing",
        "",
        "Add one row only when a public implementation or provider declaration clearly wraps a web, app, browser, desktop, or coding-assistant session into a reusable generic chat API. Keep the evidence level honest and do not submit cookies, tokens, private endpoints, personal data, or bypass instructions. See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).",
        "",
        "Related implementation: [Clash of Tokens](https://github.com/dajiaohuang/clash_of_tokens). This repository is the index and does not bundle upstream credentials.",
        "",
    ]
    README.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
