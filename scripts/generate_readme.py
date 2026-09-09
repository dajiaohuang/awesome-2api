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

CATEGORY_LABELS = {
    "网页 Chatbot": "Web Chatbot / 网页 Chatbot",
    "网页 / App Chatbot": "Web / App Chatbot / 网页 / App Chatbot",
    "嵌入式 / App 内助手": "Embedded / In-App Assistant / 嵌入式 / App 内助手",
    "嵌入式 / Web 助手": "Embedded / Web Assistant / 嵌入式 / Web 助手",
    "嵌入式 / 浏览器内助手": "Embedded / Browser Assistant / 嵌入式 / 浏览器内助手",
    "Coding / Subscription": "Coding / Subscription / 编码 / 订阅",
    "In-App / Workspace": "In-App / Workspace / 应用内 / 工作区",
}

INTERFACE_LABELS = {
    "OpenAI / Anthropic（依包装器）": "OpenAI / Anthropic (wrapper-dependent) / 依包装器",
    "OpenAI / Anthropic（依参考实现）": "OpenAI / Anthropic (reference implementation) / 依参考实现",
}

EVIDENCE_LABELS = {
    "A-直接反代": "A — Direct adapter / 直接反代",
    "B-聚合适配": "B — Aggregator adapter / 聚合适配",
    "C-包装层": "C — Wrapper layer / 包装层",
}

SHAPE_LABELS = {
    "App/小程序内置聊天助手": "In-app / mini-program chat assistant / App/小程序内置聊天助手",
    "Bot + Web 会话": "Bot + web session / Bot + Web 会话",
    "CLI 关联产品鉴权": "CLI + product authentication / CLI 关联产品鉴权",
    "CLI/产品会话": "CLI / product session / CLI/产品会话",
    "CLI/产品鉴权": "CLI / product authentication / CLI/产品鉴权",
    "Language Server / Devin HTTPS 两条路径": "Language Server / Devin HTTPS paths / Language Server / Devin HTTPS 两条路径",
    "OAuth/产品协议": "OAuth / product protocol / OAuth/产品协议",
    "Web AI 助手": "Web AI assistant / Web AI 助手",
    "Android 应用会话": "Android app session / Android 应用会话",
    "Web 会话": "Web session / Web 会话",
    "Web 会话/实时事件": "Web session / realtime events / Web 会话/实时事件",
    "Web 内置聊天助手": "Embedded web chat assistant / Web 内置聊天助手",
    "Web 聊天/Agent": "Web chat / agent / Web 聊天/Agent",
    "Web 聊天助手": "Web chat assistant / Web 聊天助手",
    "Web/App 会话": "Web/app session / Web/App 会话",
    "Zed 产品鉴权": "Zed product authentication / Zed 产品鉴权",
    "产品 OAuth": "Product OAuth / 产品 OAuth",
    "产品 Protobuf": "Product Protobuf / 产品 Protobuf",
    "产品会话": "Product session / 产品会话",
    "产品协议": "Product protocol / 产品协议",
    "产品协议/可选CLI": "Product protocol / optional CLI / 产品协议/可选CLI",
    "产品登录/会话": "Product login / session / 产品登录/会话",
    "产品鉴权": "Product authentication / 产品鉴权",
    "产品鉴权/待审计": "Product authentication / audit pending / 产品鉴权/待审计",
    "企业会话": "Enterprise session / 企业会话",
    "企业会话/WS": "Enterprise session / WebSocket / 企业会话/WS",
    "会话；HTTP/流式": "Session; HTTP/streaming / 会话；HTTP/流式",
    "会话；HTTP/流式；可选CDP": "Session; HTTP/streaming; optional CDP / 会话；HTTP/流式；可选CDP",
    "会话；Web 协议": "Session; web protocol / 会话；Web 协议",
    "免费 Web AI Chat": "Free web AI chat / 免费 Web AI Chat",
    "免费 Web 聊天": "Free web chat / 免费 Web 聊天",
    "免费网站聊天助手": "Free website chat assistant / 免费网站聊天助手",
    "匿名/免费 Web 聊天": "Anonymous / free web chat / 匿名/免费 Web 聊天",
    "外部 CLI": "External CLI / 外部 CLI",
    "外部 app-server": "External app-server / 外部 app-server",
    "多模型 Web 聊天": "Multi-model web chat / 多模型 Web 聊天",
    "工作区会话": "Workspace session / 工作区会话",
    "应用/浏览器协议": "App / browser protocol / 应用/浏览器协议",
    "应用会话": "App session / 应用会话",
    "应用鉴权": "App authentication / 应用鉴权",
    "待审计": "Audit pending / 待审计",
    "搜索产品模块": "Search product module / 搜索产品模块",
    "模块待审计": "Module audit pending / 模块待审计",
    "浏览器/WS": "Browser / WebSocket / 浏览器/WS",
    "浏览器/站点会话": "Browser / site session / 浏览器/站点会话",
    "浏览器产品协议": "Browser product protocol / 浏览器产品协议",
    "浏览器侧边栏/内置多模型助手": "Browser sidebar / embedded multi-model assistant / 浏览器侧边栏/内置多模型助手",
    "浏览器自动化（参考为 Camoufox）": "Browser automation (Camoufox reference) / 浏览器自动化（参考为 Camoufox）",
    "站点会话": "Site session / 站点会话",
    "站点登录": "Site login / 站点登录",
    "网站内嵌 AI 聊天": "Embedded website AI chat / 网站内嵌 AI 聊天",
}

STATUS_LABELS = {"纳入": "Included / 纳入"}


def bilingual(value: object, labels: dict[str, str]) -> str:
    text = str(value)
    return labels.get(text, text)


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
                bilingual(entry[F["category"]], CATEGORY_LABELS),
                "; ".join(linked_projects),
                bilingual(entry[F["interface"]], INTERFACE_LABELS),
                bilingual(entry[F["level"]], EVIDENCE_LABELS),
                bilingual(entry[F["shape"]], SHAPE_LABELS),
                bilingual(entry[F["status"]], STATUS_LABELS),
            ]
        )

    lines = [
        "# Awesome 2API [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "",
        "> A source-backed index of web, app, desktop, browser, and coding assistants wrapped into generic chat APIs.",
        "> 基于公开来源，整理将网页、App、桌面端、浏览器和编码助手接入通用聊天 API 的项目。",
        "",
        "> Companion implementation: [Clash of Tokens](https://github.com/dajiaohuang/clash_of_tokens).",
        "> 配套实现见上方的 Clash of Tokens 项目。",
        "",
        f"**{len(entries)} sources / 来源** · **{levels.get('A', 0)} direct adapters / 直接反代** · **{levels.get('B', 0)} aggregator adapters / 聚合适配** · **{levels.get('C', 0)} wrapper layers / 包装层**",
        "",
        "Every row links to its reference project. The catalog only includes public evidence of a generic chat output such as OpenAI-compatible Chat Completions, OpenAI Responses, Anthropic Messages, or an equivalent HTTP/SSE contract.",
        "",
        "每行都链接到参考项目。仅收录公开证据表明其能输出通用聊天接口（如 OpenAI 兼容 Chat Completions、OpenAI Responses、Anthropic Messages 或等价 HTTP/SSE 契约）的来源。",
        "",
        "Official API-only SDKs, media/business tools, product-only claims, and reverse-engineering notes without public adapter evidence are excluded. Links do not guarantee current availability, quota, licensing, or permitted use. / 不收录官方 API-only SDK、纯媒体或业务工具、只有产品宣传的候选项，或没有公开适配器证据的逆向笔记；链接不代表当前可用性、额度、许可或服务条款允许。",
        "",
        "Machine-readable data / 机器可读数据: [sources.json](sources.json) · Run `python scripts/generate_readme.py` to refresh this table. / 运行该命令可刷新表格。",
        "",
        "## Catalog",
        "",
    ]
    lines += table(
        [
            "Source / 来源",
            "Category / 类别",
            "Reference project / 参考项目",
            "Generic interface / 通用接口",
            "Evidence / 证据",
            "Shape / 形态",
            "Status / 状态",
        ],
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
        "Add one row only when a public implementation or provider declaration clearly wraps a web, app, browser, desktop, or coding-assistant session into a reusable generic chat API. Keep the evidence level honest and do not submit cookies, tokens, private endpoints, personal data, or bypass instructions. See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md). / 仅在公开实现或 Provider 声明确实将网页、App、浏览器、桌面端或编码助手会话包装为可复用通用聊天 API 时新增条目；如实填写证据等级，不要提交 Cookie、Token、私有端点、个人数据或绕过说明。详见上述文档。",
        "",
        "",
    ]
    README.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
