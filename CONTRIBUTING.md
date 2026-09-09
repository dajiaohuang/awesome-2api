# Contributing

Thanks for helping keep this list useful and evidence-backed.

## What belongs here

Submit a row only when a public implementation, adapter, or provider clearly
turns a web, app, desktop, browser, or coding-assistant session into a generic
chat API. The reference must expose or document a reusable interface such as
OpenAI Chat Completions, OpenAI Responses, Anthropic Messages, or an equivalent
generic HTTP/SSE contract.

The list does not include official API-only SDKs, product-only announcements,
media-only tools, business-only App APIs, private code, or candidates without
an implementation reference.

## Required evidence

Each entry needs:

1. A stable public URL to the implementation or provider declaration.
2. The source product or embedded assistant being wrapped.
3. The output protocol and transport (HTTP, SSE, browser session, CLI, and so on).
4. An honest evidence level. A direct adapter is different from a provider
   appearing only in an aggregator catalog.
5. The date the entry was last checked.

Do not include cookies, access tokens, private endpoints, or instructions for
bypassing authentication, quotas, paywalls, or access controls.

## Updating the list

Edit `sources.json`, then run:

```text
python scripts/validate.py
python scripts/generate_readme.py
```

Keep one row per source family. If a project supports several models or has
forks, link the canonical implementation and explain the distinction in the
notes instead of multiplying rows.
