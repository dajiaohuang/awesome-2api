# Awesome 2API [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A source-backed index of web, app, desktop, browser, and coding assistants wrapped into generic chat APIs.
> 将网页、App、桌面端、浏览器和编码助手反代为通用聊天接口的证据型目录。

**93 sources** · **48 direct adapters** · **41 aggregator adapters** · **4 wrapper layers**

Every row links to its reference project. The catalog only includes public evidence of a generic chat output such as OpenAI-compatible Chat Completions, OpenAI Responses, Anthropic Messages, or an equivalent HTTP/SSE contract.

不收录官方 API-only SDK、纯媒体/业务工具、只有产品宣传的候选项，或没有公开适配器证据的逆向笔记。链接不代表当前可用性、额度、许可或服务条款允许。

Machine-readable data: [sources.json](sources.json) · Run python scripts/generate_readme.py to refresh this table.

## Catalog

| Source                                   | Category              | Reference project                                                                         | Generic interface                          | Evidence | Shape                              | Status |
| ---------------------------------------- | --------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------ | -------- | ---------------------------------- | ------ |
| [Adapta One][e001]                       | 网页 Chatbot            | [OmniRoute adapta-web][p001-1]                                                            | OpenAI-compatible                          | B-聚合适配   | Web 会话                             | 纳入     |
| [Arena / LMArena][e002]                  | 网页 Chatbot            | [g4f: LMArena][p002-1]; [OmniRoute lmarena][p002-2]                                       | OpenAI-compatible                          | B-聚合适配   | Web 会话                             | 纳入     |
| [BLACKBOX AI Web][e003]                  | 网页 Chatbot            | [g4f: BlackboxPro][p003-1]; [OmniRoute blackbox-web][p003-2]                              | OpenAI-compatible                          | B-聚合适配   | Web 会话                             | 纳入     |
| [ChatGPT Web][e004]                      | 网页 Chatbot            | [aurorax-neo/chat2api][p004-1]; [Octo-Lex/ChatGPT-Web2API][p004-2]                        | OpenAI-compatible                          | A-直接反代   | 会话；HTTP/流式；可选CDP                   | 纳入     |
| [Claude Web][e005]                       | 网页 Chatbot            | [yushangxiao/claude2api][p005-1]                                                          | OpenAI / Anthropic（依参考实现）                  | A-直接反代   | 会话；HTTP/流式                         | 纳入     |
| [Conol][e006]                            | 网页 Chatbot            | [OmniRoute conol-web][p006-1]                                                             | OpenAI-compatible                          | B-聚合适配   | Web 会话                             | 纳入     |
| [Duck.ai][e007]                          | 网页 Chatbot            | [g4f][p007-1]; [OmniRoute duckduckgo-web][p007-2]                                         | OpenAI-compatible                          | B-聚合适配   | 站点会话                               | 纳入     |
| [Gemini Web][e008]                       | 网页 Chatbot            | [ntthanh2603/gemini-web-to-api][p008-1]                                                   | OpenAI-compatible                          | A-直接反代   | 会话；Web 协议                          | 纳入     |
| [Genspark][e009]                         | 网页 Chatbot            | [deanxv/genspark2api][p009-1]                                                             | OpenAI-compatible                          | A-直接反代   | Web/App 会话                         | 纳入     |
| [GigaChat][e010]                         | 网页 Chatbot            | [g4f: GigaChat][p010-1]                                                                   | OpenAI-compatible                          | B-聚合适配   | 模块待审计                              | 纳入     |
| [Grok Console 产品入口][e011]                | 网页 Chatbot            | [chenyme/grok2api][p011-1]                                                                | OpenAI-compatible                          | A-直接反代   | 产品鉴权                               | 纳入     |
| [Grok Web][e012]                         | 网页 Chatbot            | [chenyme/grok2api][p012-1]                                                                | OpenAI-compatible                          | A-直接反代   | Web 会话                             | 纳入     |
| [HuggingChat][e013]                      | 网页 Chatbot            | [g4f: HuggingChat][p013-1]; [OmniRoute][p013-2]                                           | OpenAI-compatible                          | B-聚合适配   | Web 会话                             | 纳入     |
| [HyperAgent][e014]                       | 网页 Chatbot            | [OmniRoute hyperagent][p014-1]                                                            | OpenAI-compatible                          | B-聚合适配   | Web 会话                             | 纳入     |
| [Inner AI][e015]                         | 网页 Chatbot            | [OmniRoute inner-ai][p015-1]                                                              | OpenAI-compatible                          | B-聚合适配   | Web 会话                             | 纳入     |
| [Meta AI Web][e016]                      | 网页 Chatbot            | [g4f: MetaAI/MetaAIAccount][p016-1]; [OmniRoute muse-spark-web][p016-2]                   | OpenAI-compatible                          | B-聚合适配   | Web 会话/实时事件                        | 纳入     |
| [Microsoft Copilot Web / App][e017]      | 网页 Chatbot            | [g4f: Copilot/CopilotApp][p017-1]; [OmniRoute][p017-2]                                    | OpenAI-compatible                          | B-聚合适配   | Web/App 会话                         | 纳入     |
| [Perplexity Web][e018]                   | 网页 Chatbot            | [jamie950315/pplx-proxy][p018-1]                                                          | OpenAI-compatible                          | A-直接反代   | Web 会话                             | 纳入     |
| [Phind][e019]                            | 网页 Chatbot            | [g4f: PhindAi][p019-1]                                                                    | OpenAI-compatible                          | B-聚合适配   | 模块待审计                              | 纳入     |
| [Pi][e020]                               | 网页 Chatbot            | [g4f: Pi][p020-1]                                                                         | OpenAI-compatible                          | B-聚合适配   | 模块待审计                              | 纳入     |
| [Poe Web / Bot marketplace][e021]        | 网页 Chatbot            | [OmniRoute poe-web][p021-1]; [snowby666/poe-api-wrapper][p021-2]                          | OpenAI-compatible                          | B-聚合适配   | Bot + Web 会话                       | 纳入     |
| [Reka Chat][e022]                        | 网页 Chatbot            | [g4f: Reka][p022-1]                                                                       | OpenAI-compatible                          | B-聚合适配   | 模块待审计                              | 纳入     |
| [T3 Chat][e023]                          | 网页 Chatbot            | [OmniRoute t3-web][p023-1]                                                                | OpenAI-compatible                          | B-聚合适配   | Web 会话                             | 纳入     |
| [TinyCMS AI][e024]                       | 网页 Chatbot            | [OmniRoute tinycms-web][p024-1]                                                           | OpenAI-compatible                          | B-聚合适配   | Web/App 会话                         | 纳入     |
| [UC / uncensored.com][e025]              | 网页 Chatbot            | [OmniRoute uc][p025-1]                                                                    | OpenAI-compatible                          | B-聚合适配   | Web 会话                             | 纳入     |
| [Venice Web][e026]                       | 网页 Chatbot            | [OmniRoute venice-web][p026-1]                                                            | OpenAI-compatible                          | B-聚合适配   | Web 会话                             | 纳入     |
| [WhiteRabbitNeo][e027]                   | 网页 Chatbot            | [g4f: WhiteRabbitNeo][p027-1]                                                             | OpenAI-compatible                          | B-聚合适配   | 模块待审计                              | 纳入     |
| [You.com][e028]                          | 网页 Chatbot            | [g4f: You][p028-1]                                                                        | OpenAI-compatible                          | B-聚合适配   | 模块待审计                              | 纳入     |
| [ZenMux Web][e029]                       | 网页 Chatbot            | [OmniRoute zenmux-free][p029-1]                                                           | OpenAI-compatible                          | B-聚合适配   | Web 会话                             | 纳入     |
| [DeepSeek Web][e030]                     | 网页 / App Chatbot      | [xiaoY233/Chat2API][p030-1]; [lza6/Deepseek-2api][p030-2]                                 | OpenAI-compatible                          | A-直接反代   | Web 会话                             | 纳入     |
| [Dola 国际站][e031]                         | 网页 / App Chatbot      | [OmniRoute doubao-web][p031-1]                                                            | OpenAI-compatible                          | B-聚合适配   | Web 会话                             | 纳入     |
| [Kimi Web][e032]                         | 网页 / App Chatbot      | [xiaoY233/Chat2API][p032-1]; [lza6/kimi-ai-2api][p032-2]                                  | OpenAI-compatible                          | A-直接反代   | Web 会话                             | 纳入     |
| [MiniMax Web / Agent][e033]              | 网页 / App Chatbot      | [xiaoY233/Chat2API][p033-1]                                                               | OpenAI-compatible                          | A-直接反代   | Web/App 会话                         | 纳入     |
| [Qwen Chat 国际站][e034]                    | 网页 / App Chatbot      | [xiaoY233/Chat2API][p034-1]; [lza6/Qwen-2api][p034-2]                                     | OpenAI-compatible                          | A-直接反代   | Web 会话                             | 纳入     |
| [Z.ai Web][e035]                         | 网页 / App Chatbot      | [Chat2API][p035-1]; [OmniRoute][p035-2]; [lza6/zai.is-2api-python][p035-3]                | OpenAI-compatible                          | B-聚合适配   | Web 会话                             | 纳入     |
| [小米 MiMo Web][e036]                      | 网页 / App Chatbot      | [xiaoY233/Chat2API][p036-1]                                                               | OpenAI-compatible                          | A-直接反代   | Web 会话                             | 纳入     |
| [智谱清言 / GLM Web][e037]                   | 网页 / App Chatbot      | [xiaoY233/Chat2API][p037-1]                                                               | OpenAI-compatible                          | A-直接反代   | Web 会话                             | 纳入     |
| [秘塔 AI 搜索][e038]                         | 网页 / App Chatbot      | [step-free-api README: metaso-free-api][p038-1]                                           | OpenAI-compatible                          | B-聚合适配   | 待审计                                | 纳入     |
| [聆心智能 / Emohaa][e039]                    | 网页 / App Chatbot      | [step-free-api README: emohaa-free-api][p039-1]                                           | OpenAI-compatible                          | B-聚合适配   | 待审计                                | 纳入     |
| [腾讯 AI Studio][e040]                     | 网页 / App Chatbot      | [OmniRoute tencent-aistudio-web][p040-1]                                                  | OpenAI-compatible                          | B-聚合适配   | Web 会话                             | 纳入     |
| [腾讯元宝][e041]                             | 网页 / App Chatbot      | [chenwr727/yuanbao-free-api][p041-1]                                                      | OpenAI-compatible                          | A-直接反代   | Web/App 会话                         | 纳入     |
| [讯飞星火][e042]                             | 网页 / App Chatbot      | [step-free-api README 索引][p042-1]; [SelfExistFiles/spark-free-api][p042-2]                | OpenAI-compatible                          | B-聚合适配   | 待审计                                | 纳入     |
| [豆包中国站][e043]                            | 网页 / App Chatbot      | [lza6/doubao-2api][p043-1]                                                                | OpenAI-compatible                          | A-直接反代   | 浏览器/站点会话                           | 纳入     |
| [跃问 / StepChat][e044]                    | 网页 / App Chatbot      | [jonnyquan/step-free-api][p044-1]                                                         | OpenAI-compatible                          | A-直接反代   | Web 会话                             | 纳入     |
| [通义 / Qwen 中国站][e045]                    | 网页 / App Chatbot      | [xiaoY233/Chat2API][p045-1]; [lza6/Qwen-2api][p045-2]                                     | OpenAI-compatible                          | A-直接反代   | 站点登录                               | 纳入     |
| [国家反诈AI][e046]                           | 嵌入式 / App 内助手         | [lfzk550/fanzha-ai-proxy][p046-1]                                                         | OpenAI /v1/chat/completions                | A-直接反代   | App/小程序内置聊天助手                      | 纳入     |
| [Tabbit 内置 AI][e047]                     | 嵌入式 / 浏览器内助手          | [hoinata/tabbit2api][p047-1]; [hwttop5/tabbit2api][p047-2]                                | OpenAI Chat/Responses + Anthropic Messages | A-直接反代   | 浏览器侧边栏/内置多模型助手                     | 纳入     |
| [AI Free Forever][e048]                  | 嵌入式 / Web 助手          | [lza6/Aifreeforever-2api][p048-1]                                                         | OpenAI-style chat/completions              | A-直接反代   | 免费 Web 聊天                          | 纳入     |
| [ChatAI GPT][e049]                       | 嵌入式 / Web 助手          | [lza6/Chataigpt-2api][p049-1]                                                             | OpenAI /v1/chat/completions                | A-直接反代   | 多模型 Web 聊天                         | 纳入     |
| [chatgptfree.ai][e050]                   | 嵌入式 / Web 助手          | [lza6/FreeAIchat-2api][p050-1]                                                            | OpenAI /v1/chat/completions                | A-直接反代   | 免费网站聊天助手                           | 纳入     |
| [EaseMate AI][e051]                      | 嵌入式 / Web 助手          | [lza6/easemate-2api][p051-1]                                                              | OpenAI /v1/chat/completions                | A-直接反代   | Web 聊天助手                           | 纳入     |
| [Flowith][e052]                          | 嵌入式 / Web 助手          | [lza6/flowith-2api][p052-1]                                                               | OpenAI /v1/chat/completions                | A-直接反代   | Web 聊天/Agent                       | 纳入     |
| [GPTAnon][e053]                          | 嵌入式 / Web 助手          | [lza6/gptanon-2api-cfwork][p053-1]                                                        | OpenAI /v1/chat/completions                | A-直接反代   | 匿名/免费 Web 聊天                       | 纳入     |
| [Inkeep][e054]                           | 嵌入式 / Web 助手          | [lza6/inkeep-2api][p054-1]                                                                | OpenAI /v1/chat/completions                | A-直接反代   | 网站内嵌 AI 聊天                         | 纳入     |
| [LangFast][e055]                         | 嵌入式 / Web 助手          | [lza6/langfast-2api][p055-1]                                                              | OpenAI /v1/chat/completions                | A-直接反代   | Web AI 助手                          | 纳入     |
| [LiaoBots][e056]                         | 嵌入式 / Web 助手          | [lza6/liaobots-2api-cfwork][p056-1]                                                       | OpenAI /v1/chat/completions                | A-直接反代   | 多模型 Web 聊天                         | 纳入     |
| [Perfect Assistant][e057]                | 嵌入式 / Web 助手          | [lza6/perfectassistant-2api-cfwork][p057-1]                                               | OpenAI /v1/chat/completions                | A-直接反代   | Web 内置聊天助手                         | 纳入     |
| [ToolBaz Chat][e058]                     | 嵌入式 / Web 助手          | [lza6/toolbaz-2api-docker][p058-1]                                                        | OpenAI /v1/chat/completions                | A-直接反代   | 免费 Web AI Chat                     | 纳入     |
| [Amazon Q Developer][e059]               | Coding / Subscription | [OmniRoute amazon-q][p059-1]                                                              | OpenAI-compatible                          | B-聚合适配   | 产品鉴权                               | 纳入     |
| [Antigravity][e060]                      | Coding / Subscription | [router-for-me/CLIProxyAPI][p060-1]                                                       | OpenAI / Anthropic（依包装器）                   | A-直接反代   | 产品 OAuth                           | 纳入     |
| [Augment Code / Auggie][e061]            | Coding / Subscription | [linqiu919/augment2api][p061-1]; [OmniRoute auggie][p061-2]                               | OpenAI-compatible                          | A-直接反代   | 产品协议/可选CLI                         | 纳入     |
| [Claude Code 订阅入口][e062]                 | Coding / Subscription | [router-for-me/CLIProxyAPI][p062-1]                                                       | OpenAI / Anthropic（依包装器）                   | A-直接反代   | 产品 OAuth                           | 纳入     |
| [CodeBuddy（中国/国际配置）][e063]               | Coding / Subscription | [xueyue33/codebuddy2api][p063-1]                                                          | OpenAI-compatible                          | A-直接反代   | 产品登录/会话                            | 纳入     |
| [Codex 订阅入口][e064]                       | Coding / Subscription | [router-for-me/CLIProxyAPI][p064-1]                                                       | OpenAI-compatible                          | A-直接反代   | 产品 OAuth                           | 纳入     |
| [Cursor][e065]                           | Coding / Subscription | [tageecc/cursor-agent-api-proxy][p065-1]; [OmniRoute][p065-2]; [lza6/cursor-2api][p065-3] | OpenAI-compatible                          | C-包装层    | CLI/产品会话                           | 纳入     |
| [Devin CLI 产品入口][e066]                   | Coding / Subscription | [OmniRoute devin-cli / devin-cli-agentic][p066-1]                                         | OpenAI-compatible                          | C-包装层    | 外部 CLI                             | 纳入     |
| [Freebuff / Codebuff 入口][e067]           | Coding / Subscription | [lza6/Freebuff-2API][p067-1]                                                              | OpenAI-compatible                          | A-直接反代   | 产品协议                               | 纳入     |
| [Gemini CLI / Code Assist 路径][e068]      | Coding / Subscription | [g4f: GeminiCLI][p068-1]; [CLIProxyAPI][p068-2]                                           | OpenAI-compatible                          | B-聚合适配   | CLI 关联产品鉴权                         | 纳入     |
| [GitHub Copilot（含 Enterprise 配置）][e069]  | Coding / Subscription | [messense/copilot-api-proxy][p069-1]                                                      | OpenAI-compatible                          | A-直接反代   | 产品鉴权                               | 纳入     |
| [Grok Build / CLI][e070]                 | Coding / Subscription | [CLIProxyAPI][p070-1]; [chenyme/grok2api][p070-2]                                         | OpenAI-compatible                          | A-直接反代   | 产品 OAuth                           | 纳入     |
| [Kiro][e071]                             | Coding / Subscription | [caidaoli/kiro2api][p071-1]                                                               | OpenAI-compatible                          | A-直接反代   | OAuth/产品协议                         | 纳入     |
| [Qoder][e072]                            | Coding / Subscription | [onehub-work/qoder-cli-api][p072-1]; [OmniRoute][p072-2]; [cubk1/qoder2api][p072-3]       | OpenAI-compatible                          | C-包装层    | CLI/产品鉴权                           | 纳入     |
| [Qwen Code][e073]                        | Coding / Subscription | [g4f: QwenCode][p073-1]                                                                   | OpenAI-compatible                          | B-聚合适配   | 产品鉴权/待审计                           | 纳入     |
| [Trae / SOLO][e074]                      | Coding / Subscription | [OmniRoute trae][p074-1]                                                                  | OpenAI-compatible                          | B-聚合适配   | 产品会话                               | 纳入     |
| [v0 Web][e075]                           | Coding / Subscription | [OmniRoute v0-vercel-web][p075-1]                                                         | OpenAI-compatible                          | B-聚合适配   | Web 会话                             | 纳入     |
| [Warp AI][e076]                          | Coding / Subscription | [Xchat1/Warp2Api][p076-1]                                                                 | OpenAI-compatible                          | A-直接反代   | 产品 Protobuf                        | 纳入     |
| [Windsurf / Codeium][e077]               | Coding / Subscription | [dwgx/WindsurfAPI][p077-1]                                                                | OpenAI-compatible                          | A-直接反代   | Language Server / Devin HTTPS 两条路径 | 纳入     |
| [ZCode 应用入口][e078]                       | Coding / Subscription | [OmniRoute zcode][p078-1]                                                                 | OpenAI-compatible                          | C-包装层    | 外部 app-server                      | 纳入     |
| [Zed 托管模型][e079]                         | Coding / Subscription | [OmniRoute zed-hosted][p079-1]                                                            | OpenAI-compatible                          | B-聚合适配   | Zed 产品鉴权                           | 纳入     |
| [Cloudflare AI Playground][e080]         | In-App / Workspace    | [OmniRoute cloudflare-playground][p080-1]                                                 | OpenAI-compatible                          | B-聚合适配   | 浏览器/WS                             | 纳入     |
| [Gemini Business / Enterprise Web][e081] | In-App / Workspace    | [OmniRoute gemini-business][p081-1]; [lulistart/business-gemini-2api][p081-2]             | OpenAI-compatible                          | B-聚合适配   | 企业会话                               | 纳入     |
| [Google AI Studio Build][e082]           | In-App / Workspace    | [iBUHub/AIStudioToAPI][p082-1]                                                            | OpenAI-compatible                          | A-直接反代   | 应用/浏览器协议                           | 纳入     |
| [Google AI Studio Playground][e083]      | In-App / Workspace    | [Mag1cFall/AIStudio2API][p083-1]                                                          | OpenAI-compatible                          | A-直接反代   | 浏览器自动化（参考为 Camoufox）               | 纳入     |
| [Google 搜索 AI Mode][e084]                | In-App / Workspace    | [g4f: GoogleAiMode][p084-1]                                                               | OpenAI-compatible                          | B-聚合适配   | 搜索产品模块                             | 纳入     |
| [MaxAI][e085]                            | In-App / Workspace    | [OmniRoute maxai][p085-1]                                                                 | OpenAI-compatible                          | B-聚合适配   | 应用会话                               | 纳入     |
| [Merlin][e086]                           | In-App / Workspace    | [cchking/merlin2api][p086-1]                                                              | OpenAI-compatible                          | A-直接反代   | 应用会话                               | 纳入     |
| [Microsoft 365 Copilot / BizChat][e087]  | In-App / Workspace    | [OmniRoute copilot-m365-web][p087-1]                                                      | OpenAI-compatible                          | B-聚合适配   | 企业会话/WS                            | 纳入     |
| [Monica][e088]                           | In-App / Workspace    | [SimonUTD/monica2api][p088-1]                                                             | OpenAI-compatible                          | A-直接反代   | 应用会话                               | 纳入     |
| [Notion AI][e089]                        | In-App / Workspace    | [lza6/notion-2api][p089-1]                                                                | OpenAI-compatible                          | A-直接反代   | 工作区会话                              | 纳入     |
| [Opera Aria][e090]                       | In-App / Workspace    | [g4f: OperaAria][p090-1]                                                                  | OpenAI-compatible                          | B-聚合适配   | 浏览器产品协议                            | 纳入     |
| [PromptQL 应用聊天][e091]                    | In-App / Workspace    | [OmniRoute promptql][p091-1]                                                              | OpenAI-compatible                          | B-聚合适配   | 应用会话                               | 纳入     |
| [Raycast AI][e092]                       | In-App / Workspace    | [xxxbrian/raycast2api][p092-1]                                                            | OpenAI-compatible                          | A-直接反代   | 应用鉴权                               | 纳入     |
| [Sider][e093]                            | In-App / Workspace    | [yeuxuan/sider2api][p093-1]                                                               | OpenAI-compatible                          | A-直接反代   | 应用会话                               | 纳入     |

[e001]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-entry-1
[e002]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-entry-2
[e003]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-entry-3
[e004]: https://github.com/aurorax-neo/chat2api#awesome-2api-entry-4
[e005]: https://github.com/yushangxiao/claude2api#awesome-2api-entry-5
[e006]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-entry-6
[e007]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-entry-7
[e008]: https://github.com/ntthanh2603/gemini-web-to-api#awesome-2api-entry-8
[e009]: https://github.com/deanxv/genspark2api#awesome-2api-entry-9
[e010]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-entry-10
[e011]: https://github.com/chenyme/grok2api#awesome-2api-entry-11
[e012]: https://github.com/chenyme/grok2api#awesome-2api-entry-12
[e013]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-entry-13
[e014]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-entry-14
[e015]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-entry-15
[e016]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-entry-16
[e017]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-entry-17
[e018]: https://github.com/jamie950315/pplx-proxy#awesome-2api-entry-18
[e019]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-entry-19
[e020]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-entry-20
[e021]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-entry-21
[e022]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-entry-22
[e023]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-entry-23
[e024]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-entry-24
[e025]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-entry-25
[e026]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-entry-26
[e027]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-entry-27
[e028]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-entry-28
[e029]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-entry-29
[e030]: https://github.com/xiaoY233/Chat2API#awesome-2api-entry-30
[e031]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-entry-31
[e032]: https://github.com/xiaoY233/Chat2API#awesome-2api-entry-32
[e033]: https://github.com/xiaoY233/Chat2API#awesome-2api-entry-33
[e034]: https://github.com/xiaoY233/Chat2API#awesome-2api-entry-34
[e035]: https://github.com/xiaoY233/Chat2API#awesome-2api-entry-35
[e036]: https://github.com/xiaoY233/Chat2API#awesome-2api-entry-36
[e037]: https://github.com/xiaoY233/Chat2API#awesome-2api-entry-37
[e038]: https://github.com/jonnyquan/step-free-api#awesome-2api-entry-38
[e039]: https://github.com/jonnyquan/step-free-api#awesome-2api-entry-39
[e040]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-entry-40
[e041]: https://github.com/chenwr727/yuanbao-free-api#awesome-2api-entry-41
[e042]: https://github.com/jonnyquan/step-free-api#awesome-2api-entry-42
[e043]: https://github.com/lza6/doubao-2api#awesome-2api-entry-43
[e044]: https://github.com/jonnyquan/step-free-api#awesome-2api-entry-44
[e045]: https://github.com/xiaoY233/Chat2API#awesome-2api-entry-45
[e046]: https://github.com/lfzk550/fanzha-ai-proxy#awesome-2api-entry-46
[e047]: https://github.com/hoinata/tabbit2api#awesome-2api-entry-47
[e048]: https://github.com/lza6/Aifreeforever-2api#awesome-2api-entry-48
[e049]: https://github.com/lza6/Chataigpt-2api#awesome-2api-entry-49
[e050]: https://github.com/lza6/FreeAIchat-2api#awesome-2api-entry-50
[e051]: https://github.com/lza6/easemate-2api#awesome-2api-entry-51
[e052]: https://github.com/lza6/flowith-2api#awesome-2api-entry-52
[e053]: https://github.com/lza6/gptanon-2api-cfwork#awesome-2api-entry-53
[e054]: https://github.com/lza6/inkeep-2api#awesome-2api-entry-54
[e055]: https://github.com/lza6/langfast-2api#awesome-2api-entry-55
[e056]: https://github.com/lza6/liaobots-2api-cfwork#awesome-2api-entry-56
[e057]: https://github.com/lza6/perfectassistant-2api-cfwork#awesome-2api-entry-57
[e058]: https://github.com/lza6/toolbaz-2api-docker#awesome-2api-entry-58
[e059]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-entry-59
[e060]: https://github.com/router-for-me/CLIProxyAPI#awesome-2api-entry-60
[e061]: https://github.com/linqiu919/augment2api#awesome-2api-entry-61
[e062]: https://github.com/router-for-me/CLIProxyAPI#awesome-2api-entry-62
[e063]: https://github.com/xueyue33/codebuddy2api#awesome-2api-entry-63
[e064]: https://github.com/router-for-me/CLIProxyAPI#awesome-2api-entry-64
[e065]: https://github.com/tageecc/cursor-agent-api-proxy#awesome-2api-entry-65
[e066]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-entry-66
[e067]: https://github.com/lza6/Freebuff-2API#awesome-2api-entry-67
[e068]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-entry-68
[e069]: https://github.com/messense/copilot-api-proxy#awesome-2api-entry-69
[e070]: https://github.com/router-for-me/CLIProxyAPI#awesome-2api-entry-70
[e071]: https://github.com/caidaoli/kiro2api#awesome-2api-entry-71
[e072]: https://github.com/onehub-work/qoder-cli-api#awesome-2api-entry-72
[e073]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-entry-73
[e074]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-entry-74
[e075]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-entry-75
[e076]: https://github.com/Xchat1/Warp2Api#awesome-2api-entry-76
[e077]: https://github.com/dwgx/WindsurfAPI#awesome-2api-entry-77
[e078]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-entry-78
[e079]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-entry-79
[e080]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-entry-80
[e081]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-entry-81
[e082]: https://github.com/iBUHub/AIStudioToAPI#awesome-2api-entry-82
[e083]: https://github.com/Mag1cFall/AIStudio2API#awesome-2api-entry-83
[e084]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-entry-84
[e085]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-entry-85
[e086]: https://github.com/cchking/merlin2api#awesome-2api-entry-86
[e087]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-entry-87
[e088]: https://github.com/SimonUTD/monica2api#awesome-2api-entry-88
[e089]: https://github.com/lza6/notion-2api#awesome-2api-entry-89
[e090]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-entry-90
[e091]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-entry-91
[e092]: https://github.com/xxxbrian/raycast2api#awesome-2api-entry-92
[e093]: https://github.com/yeuxuan/sider2api#awesome-2api-entry-93
[p001-1]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-1-1
[p002-1]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-project-2-1
[p002-2]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-2-2
[p003-1]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-project-3-1
[p003-2]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-3-2
[p004-1]: https://github.com/aurorax-neo/chat2api#awesome-2api-project-4-1
[p004-2]: https://github.com/Octo-Lex/ChatGPT-Web2API#awesome-2api-project-4-2
[p005-1]: https://github.com/yushangxiao/claude2api#awesome-2api-project-5-1
[p006-1]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-6-1
[p007-1]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-project-7-1
[p007-2]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-7-2
[p008-1]: https://github.com/ntthanh2603/gemini-web-to-api#awesome-2api-project-8-1
[p009-1]: https://github.com/deanxv/genspark2api#awesome-2api-project-9-1
[p010-1]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-project-10-1
[p011-1]: https://github.com/chenyme/grok2api#awesome-2api-project-11-1
[p012-1]: https://github.com/chenyme/grok2api#awesome-2api-project-12-1
[p013-1]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-project-13-1
[p013-2]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-13-2
[p014-1]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-14-1
[p015-1]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-15-1
[p016-1]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-project-16-1
[p016-2]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-16-2
[p017-1]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-project-17-1
[p017-2]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-17-2
[p018-1]: https://github.com/jamie950315/pplx-proxy#awesome-2api-project-18-1
[p019-1]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-project-19-1
[p020-1]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-project-20-1
[p021-1]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-21-1
[p021-2]: https://github.com/snowby666/poe-api-wrapper#awesome-2api-project-21-2
[p022-1]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-project-22-1
[p023-1]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-23-1
[p024-1]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-24-1
[p025-1]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-25-1
[p026-1]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-26-1
[p027-1]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-project-27-1
[p028-1]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-project-28-1
[p029-1]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-29-1
[p030-1]: https://github.com/xiaoY233/Chat2API#awesome-2api-project-30-1
[p030-2]: https://github.com/lza6/Deepseek-2api#awesome-2api-project-30-2
[p031-1]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-31-1
[p032-1]: https://github.com/xiaoY233/Chat2API#awesome-2api-project-32-1
[p032-2]: https://github.com/lza6/kimi-ai-2api#awesome-2api-project-32-2
[p033-1]: https://github.com/xiaoY233/Chat2API#awesome-2api-project-33-1
[p034-1]: https://github.com/xiaoY233/Chat2API#awesome-2api-project-34-1
[p034-2]: https://github.com/lza6/Qwen-2api#awesome-2api-project-34-2
[p035-1]: https://github.com/xiaoY233/Chat2API#awesome-2api-project-35-1
[p035-2]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-35-2
[p035-3]: https://github.com/lza6/zai.is-2api-python#awesome-2api-project-35-3
[p036-1]: https://github.com/xiaoY233/Chat2API#awesome-2api-project-36-1
[p037-1]: https://github.com/xiaoY233/Chat2API#awesome-2api-project-37-1
[p038-1]: https://github.com/jonnyquan/step-free-api#awesome-2api-project-38-1
[p039-1]: https://github.com/jonnyquan/step-free-api#awesome-2api-project-39-1
[p040-1]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-40-1
[p041-1]: https://github.com/chenwr727/yuanbao-free-api#awesome-2api-project-41-1
[p042-1]: https://github.com/jonnyquan/step-free-api#awesome-2api-project-42-1
[p042-2]: https://github.com/SelfExistFiles/spark-free-api#awesome-2api-project-42-2
[p043-1]: https://github.com/lza6/doubao-2api#awesome-2api-project-43-1
[p044-1]: https://github.com/jonnyquan/step-free-api#awesome-2api-project-44-1
[p045-1]: https://github.com/xiaoY233/Chat2API#awesome-2api-project-45-1
[p045-2]: https://github.com/lza6/Qwen-2api#awesome-2api-project-45-2
[p046-1]: https://github.com/lfzk550/fanzha-ai-proxy#awesome-2api-project-46-1
[p047-1]: https://github.com/hoinata/tabbit2api#awesome-2api-project-47-1
[p047-2]: https://github.com/hwttop5/tabbit2api#awesome-2api-project-47-2
[p048-1]: https://github.com/lza6/Aifreeforever-2api#awesome-2api-project-48-1
[p049-1]: https://github.com/lza6/Chataigpt-2api#awesome-2api-project-49-1
[p050-1]: https://github.com/lza6/FreeAIchat-2api#awesome-2api-project-50-1
[p051-1]: https://github.com/lza6/easemate-2api#awesome-2api-project-51-1
[p052-1]: https://github.com/lza6/flowith-2api#awesome-2api-project-52-1
[p053-1]: https://github.com/lza6/gptanon-2api-cfwork#awesome-2api-project-53-1
[p054-1]: https://github.com/lza6/inkeep-2api#awesome-2api-project-54-1
[p055-1]: https://github.com/lza6/langfast-2api#awesome-2api-project-55-1
[p056-1]: https://github.com/lza6/liaobots-2api-cfwork#awesome-2api-project-56-1
[p057-1]: https://github.com/lza6/perfectassistant-2api-cfwork#awesome-2api-project-57-1
[p058-1]: https://github.com/lza6/toolbaz-2api-docker#awesome-2api-project-58-1
[p059-1]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-59-1
[p060-1]: https://github.com/router-for-me/CLIProxyAPI#awesome-2api-project-60-1
[p061-1]: https://github.com/linqiu919/augment2api#awesome-2api-project-61-1
[p061-2]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-61-2
[p062-1]: https://github.com/router-for-me/CLIProxyAPI#awesome-2api-project-62-1
[p063-1]: https://github.com/xueyue33/codebuddy2api#awesome-2api-project-63-1
[p064-1]: https://github.com/router-for-me/CLIProxyAPI#awesome-2api-project-64-1
[p065-1]: https://github.com/tageecc/cursor-agent-api-proxy#awesome-2api-project-65-1
[p065-2]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-65-2
[p065-3]: https://github.com/lza6/cursor-2api#awesome-2api-project-65-3
[p066-1]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-66-1
[p067-1]: https://github.com/lza6/Freebuff-2API#awesome-2api-project-67-1
[p068-1]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-project-68-1
[p068-2]: https://github.com/router-for-me/CLIProxyAPI#awesome-2api-project-68-2
[p069-1]: https://github.com/messense/copilot-api-proxy#awesome-2api-project-69-1
[p070-1]: https://github.com/router-for-me/CLIProxyAPI#awesome-2api-project-70-1
[p070-2]: https://github.com/chenyme/grok2api#awesome-2api-project-70-2
[p071-1]: https://github.com/caidaoli/kiro2api#awesome-2api-project-71-1
[p072-1]: https://github.com/onehub-work/qoder-cli-api#awesome-2api-project-72-1
[p072-2]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-72-2
[p072-3]: https://github.com/cubk1/qoder2api#awesome-2api-project-72-3
[p073-1]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-project-73-1
[p074-1]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-74-1
[p075-1]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-75-1
[p076-1]: https://github.com/Xchat1/Warp2Api#awesome-2api-project-76-1
[p077-1]: https://github.com/dwgx/WindsurfAPI#awesome-2api-project-77-1
[p078-1]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-78-1
[p079-1]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-79-1
[p080-1]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-80-1
[p081-1]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-81-1
[p081-2]: https://github.com/lulistart/business-gemini-2api#awesome-2api-project-81-2
[p082-1]: https://github.com/iBUHub/AIStudioToAPI#awesome-2api-project-82-1
[p083-1]: https://github.com/Mag1cFall/AIStudio2API#awesome-2api-project-83-1
[p084-1]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-project-84-1
[p085-1]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-85-1
[p086-1]: https://github.com/cchking/merlin2api#awesome-2api-project-86-1
[p087-1]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-87-1
[p088-1]: https://github.com/SimonUTD/monica2api#awesome-2api-project-88-1
[p089-1]: https://github.com/lza6/notion-2api#awesome-2api-project-89-1
[p090-1]: https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/__init__.py#awesome-2api-project-90-1
[p091-1]: https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/PROVIDER_REFERENCE.md#awesome-2api-project-91-1
[p092-1]: https://github.com/xxxbrian/raycast2api#awesome-2api-project-92-1
[p093-1]: https://github.com/yeuxuan/sider2api#awesome-2api-project-93-1

## Contributing

Add one row only when a public implementation or provider declaration clearly wraps a web, app, browser, desktop, or coding-assistant session into a reusable generic chat API. Keep the evidence level honest and do not submit cookies, tokens, private endpoints, personal data, or bypass instructions. See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).

Related implementation: [Clash of Tokens](https://github.com/dajiaohuang/clash_of_tokens). This repository is the index and does not bundle upstream credentials.
