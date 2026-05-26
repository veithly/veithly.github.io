# Agent Harness Architecture · Docs Site

> Public bilingual documentation site for Agent Harness Architecture Patterns.
>
> Live site: <https://agent-architecture-patterns.pages.dev>
>
> **Harness 释义**：指 LLM 之外那一整套支撑——loop、上下文、工具、沙箱、verifier、memory、observability。本书横向拆 4 个真实 Harness，作为自己做 Agent 的参考蓝本。

## Positioning

This site is written for engineers building real agent runtimes. It compares Codex, Claude Code, OpenClaw, and Hermes at the harness layer: loop, context, tools, verification, sandboxing, memory, skills, background tasks, security, todo/task progress, and execution-state routing.

The public surface is intentionally bilingual:

- Chinese is the default reading path.
- English mirrors the same structure for international sharing.
- Every pattern chapter keeps source trails to concrete files and line ranges under the studied systems.

## 技术栈

- **Astro 6** + **Starlight 0.39** — 静态站点 + 文档骨架
- **MDX** — 章节内嵌 Astro 组件
- **Pagefind** — 全文搜索（61 页索引）
- **Sharp** — 图片优化

## 开发

```bash
pnpm install
pnpm dev          # http://localhost:4321
```

## 校验与构建

| 命令 | 用途 |
|------|------|
| `pnpm check` | astro check（TypeScript + content schema） |
| `pnpm check:template` | 每章 10 段模板齐 |
| `pnpm check:i18n` | 中英文章节 1:1 对齐 |
| `pnpm check:all` | 上面三件套 |
| `pnpm build` | SSG 输出到 `dist/`（61 pages） |
| `pnpm preview` | 本地预览 build 产物 |

## Deploy

This repository is designed for Cloudflare Pages as the public project site:

- Repository: `veithly/agent-architecture-patterns`
- Domain: `https://agent-architecture-patterns.pages.dev`
- Cloudflare Pages project: `agent-architecture-patterns`
- Manual deploy command: `pnpm deploy:cloudflare`

The GitHub workflow validates every push with:

```bash
pnpm install --frozen-lockfile
pnpm check:all
pnpm build
```

Publishing runs the same build and uploads `dist/` to Cloudflare Pages.

## 目录约定

```text
src/content/docs/             # 中文（默认 locale = root）
├── index.mdx                 # 首页
├── interview.mdx             # 220 道面试题索引
├── skill.mdx                 # 配套 build-your-own-agent skill
├── preview.mdx               # 组件预览（dev only）
├── patterns/                 # 22 章工程模块
└── systems/                  # 4 个系统画像
src/content/docs/en/          # 英文镜像（i18n parity 由 CI 校验）
src/content/i18n/             # UI 字符串翻译
src/components/               # 9 个 MVP Astro 组件
src/styles/                   # tokens + handdrawn 主题
diagrams/                     # Excalidraw 源文件（入仓）
public/diagrams/              # 导出的 SVG/PNG（部署用）
scripts/                      # 模板与 i18n 校验脚本
```

## 章节模板

每章固定 10 段（CI 强制校验），新增章节请参考 `src/content/docs/patterns/02-agent-loop.mdx`。模板规则见 [CONTRIBUTING.md](./CONTRIBUTING.md)。

| § | 段落 | 用途 |
|---|------|------|
| §1 | Verdict（30 秒结论） | 直接表态 |
| §2 | CompareTable（对照表） | 四家横向对照 |
| §3 | 深度剖析 | 关键设计来龙去脉 |
| §4 | 共同点 | 最小公约数 |
| §5 | 不同点 | 取舍背后的分歧 |
| §6 | BuildRecipe（复刻方案） | MVP / Advanced / Don't 三档 |
| §7 | 架构图 | AgentLoopSVG / Diagram |
| §8 | 设计点评 | 评审视角建议 |
| §9 | SourceTrail（源码路线） | 关键文件 + 行号 |
| §10 | 小练习 | 一道动手题 |

## 视觉与组件

- **组件预览**：dev 模式访问 [`/preview/`](http://localhost:4321/preview/)
- **字体**：`Excalifont` / `Virgil`（手绘）+ `Source Han Sans SC`（中文）
- **主题**：`src/styles/tokens.css` + `src/styles/handdrawn.css`

## 写新章节的最短路径

1. 复制 `src/content/docs/patterns/02-agent-loop.mdx` 改 frontmatter
2. 按 10 段模板填内容
3. 同步建一份 `src/content/docs/en/patterns/<同名>.mdx`
4. 跑 `pnpm check:all` 确认通过
5. PR 时附 `pnpm build` 输出（61 pages 全绿）

---

Companion skill: <https://github.com/veithly/build-your-own-agent>
