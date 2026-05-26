#!/usr/bin/env python3
"""Chapter 02 - convert 8 ASCII diagrams to hand-drawn SVGs.

1. 02-hermes-10-layer.svg          — Hermes 10 层 prompt assembly + cache 边界
2. 02-compression-decisions.svg    — 上下文压缩 4 个核心决策
3. 02-claude-compact-pipeline.svg  — Claude Code 4 道流水线
4. 02-error-recovery-angles.svg    — 出错恢复 3 个角度
5. 02-openclaw-hook-flow.svg       — OpenClaw before/after hook flow
6. 02-tool-dispatch-questions.svg  — 工具 dispatch 4 个关键问题
7. 02-claude-tool-use-parallel.svg — Claude Code tool_use block 并行 dispatch
8. 02-verifier-types.svg           — Verifier 3 种类型
"""
from pathlib import Path

PUBLIC = Path("public/diagrams")

# --- shared style ---
DEFS = """  <defs>
    <filter id="wb02"><feTurbulence type="fractalNoise" baseFrequency="0.022" numOctaves="2" seed="221" /><feDisplacementMap in="SourceGraphic" scale="1.5" /></filter>
    <marker id="ar02" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .col  { font: 700 13px sans-serif; fill: #1e293b; }
      .lbl  { font: 700 11.5px sans-serif; fill: #1e293b; }
      .t    { font: 11.5px sans-serif; fill: #334155; }
      .t-s  { font: 10.5px sans-serif; fill: #475569; }
      .note { font: italic 10.5px sans-serif; fill: #b45309; }
      .num  { font: 700 12.5px sans-serif; fill: #fff; }
    </style>
  </defs>"""

# 1. Hermes 10-layer prompt assembly
HERMES_10_LAYER = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 620" role="img"
     aria-label="Hermes 10 层 prompt assembly with cache boundary">
{DEFS}
  <text x="380" y="26" class="h" text-anchor="middle">Hermes · 10 层 prompt 装配（含 cache 边界）</text>
  <text x="380" y="44" class="t-s" text-anchor="middle">layer 1-7 落在 cache 边界之前；timestamp / platform 每次都新，落在边界之后</text>

  <g filter="url(#wb02)">"""

# layers data: (idx, label, source/comment)
LAYERS = [
    (1,  "agent identity",       "SOUL.md / DEFAULT_AGENT_IDENTITY"),
    (2,  "tool-aware behavior",  "save durable facts via memory tool"),
    (3,  "honcho static block",  "optional personality data"),
    (4,  "optional system msg",  "config / API override"),
    (5,  "frozen MEMORY snap",   "## Persistent Memory ..."),
    (6,  "frozen USER profile",  "## User Profile / Name: Alice"),
    (7,  "skills index",         "## Skills (mandatory)"),
    (8,  "context files",        "AGENTS.md / .cursorrules / *.mdc"),
    (9,  "timestamp + session",  "Current time: 2026-03-30T14:30..."),
    (10, "platform hint",        "You are a CLI AI Agent..."),
]

y0 = 70
row_h = 44
for i, (n, lbl, comment) in enumerate(LAYERS):
    y = y0 + i * row_h
    color = "#bfdbfe" if i < 7 else "#fed7aa"
    # cache boundary between layer 7 and 8
    HERMES_10_LAYER += (
        f"\n    <rect x=\"80\" y=\"{y}\" width=\"600\" height=\"34\" rx=\"7\" fill=\"{color}\" stroke=\"#1e293b\" stroke-width=\"1.5\" />"
        f"\n    <circle cx=\"108\" cy=\"{y+17}\" r=\"13\" fill=\"#1e293b\" />"
        f"\n    <text x=\"108\" y=\"{y+21}\" class=\"num\" text-anchor=\"middle\">{n}</text>"
        f"\n    <text x=\"135\" y=\"{y+15}\" class=\"lbl\">{lbl}</text>"
        f"\n    <text x=\"135\" y=\"{y+28}\" class=\"t-s\">{comment}</text>"
    )

# cache boundary line between 7 and 8 (at y = y0 + 7*row_h = 70 + 308 = 378)
cache_y = y0 + 7 * row_h - 4
HERMES_10_LAYER += f"""
    <line x1="60" y1="{cache_y}" x2="700" y2="{cache_y}" stroke="#dc2626" stroke-width="2" stroke-dasharray="6 4" />
    <text x="690" y="{cache_y - 5}" class="lbl" text-anchor="end" fill="#dc2626">↑ cached （命中 prefix cache）</text>
    <text x="690" y="{cache_y + 14}" class="lbl" text-anchor="end" fill="#dc2626">↓ ephemeral （每次重算）</text>
  </g>
  <text x="380" y="595" class="t-s" text-anchor="middle">改 prompt 不止改文本，还要看「改的是缓存上面还是下面」</text>
</svg>
"""

# 2. Context compression 4 decisions
COMPRESSION_DECISIONS = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 360" role="img"
     aria-label="上下文压缩 4 个核心决策">
{DEFS}
  <text x="360" y="26" class="h" text-anchor="middle">上下文压缩的 4 个核心决策</text>
  <text x="360" y="44" class="t-s" text-anchor="middle">每个 agent 都要回答这四个问题，回答不同 = 系统不同</text>

  <g filter="url(#wb02)">
    <rect x="60" y="70"  width="600" height="60" rx="10" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <circle cx="92" cy="100" r="16" fill="#1e293b" />
    <text x="92" y="105" class="num" text-anchor="middle">1</text>
    <text x="120" y="93" class="lbl">什么时候压？</text>
    <text x="120" y="112" class="t">被动（OOM 后重试） vs 主动（到阈值就压）</text>
    <text x="120" y="125" class="t-s">代价：早压浪费、晚压崩溃</text>

    <rect x="60" y="140" width="600" height="60" rx="10" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <circle cx="92" cy="170" r="16" fill="#1e293b" />
    <text x="92" y="175" class="num" text-anchor="middle">2</text>
    <text x="120" y="163" class="lbl">压谁？</text>
    <text x="120" y="182" class="t">最老消息 / 工具结果 / 中间历史 / 多策略联动</text>
    <text x="120" y="195" class="t-s">护住关键证据 vs 让长跑能继续</text>

    <rect x="60" y="210" width="600" height="60" rx="10" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <circle cx="92" cy="240" r="16" fill="#1e293b" />
    <text x="92" y="245" class="num" text-anchor="middle">3</text>
    <text x="120" y="233" class="lbl">怎么压？</text>
    <text x="120" y="252" class="t">丢掉 / 折叠 / 摘要（辅助模型） / 文件式存档</text>
    <text x="120" y="265" class="t-s">操作越复杂越贵，越简单越易丢上下文</text>

    <rect x="60" y="280" width="600" height="60" rx="10" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <circle cx="92" cy="310" r="16" fill="#1e293b" />
    <text x="92" y="315" class="num" text-anchor="middle">4</text>
    <text x="120" y="303" class="lbl">压出来还在不在 context 里？</text>
    <text x="120" y="322" class="t">替换全部 / 替换中段保头尾 / 持久化到 JSONL</text>
    <text x="120" y="335" class="t-s">决定能不能事后审计 / 跨 session 回看</text>
  </g>
</svg>
"""

# 3. Claude Code 4 pipeline
CLAUDE_PIPELINE = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 480" role="img"
     aria-label="Claude Code 4 道压缩流水线">
{DEFS}
  <text x="390" y="26" class="h" text-anchor="middle">Claude Code · 4 道串联流水线（queryLoop line 379-468）</text>
  <text x="390" y="44" class="t-s" text-anchor="middle">每道独立判断要不要触发；前两道便宜，后两道贵</text>

  <g filter="url(#wb02)">
    <rect x="200" y="70" width="380" height="56" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="390" y="93" class="lbl" text-anchor="middle">① applyToolResultBudget</text>
    <text x="390" y="111" class="t-s" text-anchor="middle">按工具上限砍当前 tool_use_result（最便宜，几乎不丢信息）</text>

    <line x1="390" y1="126" x2="390" y2="155" stroke="#1e293b" stroke-width="2" marker-end="url(#ar02)" />

    <rect x="200" y="158" width="380" height="56" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="390" y="181" class="lbl" text-anchor="middle">② snipCompact + microCompact</text>
    <text x="390" y="199" class="t-s" text-anchor="middle">把「显然没用」的工具结果切短（局部 LLM 调用）</text>

    <line x1="390" y1="214" x2="390" y2="243" stroke="#1e293b" stroke-width="2" marker-end="url(#ar02)" />

    <rect x="200" y="246" width="380" height="68" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="390" y="269" class="lbl" text-anchor="middle">③ contextCollapse</text>
    <text x="390" y="287" class="t-s" text-anchor="middle">把「committed」历史折叠到 collapse-store 视图</text>
    <text x="390" y="301" class="t-s" text-anchor="middle">REPL 数组不动，apiQuery 看到的是 collapsed view</text>

    <line x1="390" y1="314" x2="390" y2="343" stroke="#1e293b" stroke-width="2" marker-end="url(#ar02)" />

    <rect x="200" y="346" width="380" height="68" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="390" y="369" class="lbl" text-anchor="middle">④ autoCompact (forked agent)</text>
    <text x="390" y="387" class="t-s" text-anchor="middle">整段总结，replace REPL 数组</text>
    <text x="390" y="401" class="t-s" text-anchor="middle">触发：context_window − AUTOCOMPACT_BUFFER_TOKENS (13k)</text>
  </g>

  <text x="390" y="450" class="note" text-anchor="middle">连续 3 次 autocompact 失败 → 断路器（MAX_CONSECUTIVE_AUTOCOMPACT_FAILURES=3）</text>
</svg>
"""

# 4. Error recovery 3 angles
ERROR_ANGLES = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 320" role="img"
     aria-label="出错恢复 3 个角度">
{DEFS}
  <text x="360" y="26" class="h" text-anchor="middle">出错恢复的 3 个角度</text>
  <text x="360" y="44" class="t-s" text-anchor="middle">同一轮、跨 session、用户主动中断，三类问题不同处理</text>

  <g filter="url(#wb02)">
    <rect x="60" y="70" width="600" height="64" rx="10" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <circle cx="92" cy="102" r="16" fill="#1e293b" />
    <text x="92" y="107" class="num" text-anchor="middle">1</text>
    <text x="120" y="93" class="lbl">同一轮里出错怎么办？</text>
    <text x="120" y="112" class="t">立刻抛 vs 注入错误再让模型自我修正 vs 退一步压缩重试</text>
    <text x="120" y="127" class="t-s">Claude Code 走「错误转 transition.reason」，Codex 直接 backoff retry</text>

    <rect x="60" y="144" width="600" height="64" rx="10" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <circle cx="92" cy="176" r="16" fill="#1e293b" />
    <text x="92" y="181" class="num" text-anchor="middle">2</text>
    <text x="120" y="167" class="lbl">会话中断 / 崩溃后能不能续？</text>
    <text x="120" y="186" class="t">rollout replay / session 持久化 / 完全无状态</text>
    <text x="120" y="201" class="t-s">Codex JSONL 事件流最完整，Hermes checkpoint 软回滚</text>

    <rect x="60" y="218" width="600" height="64" rx="10" fill="#fee2e2" stroke="#1e293b" stroke-width="1.6" />
    <circle cx="92" cy="250" r="16" fill="#1e293b" />
    <text x="92" y="255" class="num" text-anchor="middle">3</text>
    <text x="120" y="241" class="lbl">用户主动中断怎么处理？</text>
    <text x="120" y="260" class="t">forget / checkpoint / inject 「你被打断了」</text>
    <text x="120" y="275" class="t-s">AbortController vs interrupt RPC vs _interrupt_requested flag</text>
  </g>
</svg>
"""

# 5. OpenClaw hook flow
OPENCLAW_HOOK = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 460" role="img"
     aria-label="OpenClaw before/after tool hook flow">
{DEFS}
  <text x="380" y="26" class="h" text-anchor="middle">OpenClaw · 工具调用的中间件链</text>
  <text x="380" y="44" class="t-s" text-anchor="middle">before / after / persist 三段 hook 让 verifier 中间件化</text>

  <g filter="url(#wb02)">
    <rect x="260" y="70" width="240" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="380" y="93" class="lbl" text-anchor="middle">tool.call</text>

    <line x1="380" y1="106" x2="380" y2="135" stroke="#1e293b" stroke-width="2" marker-end="url(#ar02)" />

    <rect x="220" y="138" width="320" height="48" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="380" y="158" class="lbl" text-anchor="middle">before_tool_call hook chain</text>
    <text x="380" y="175" class="t-s" text-anchor="middle">任一返回 {{ error }} → 立即发 tool 流 error 帧</text>

    <line x1="380" y1="186" x2="380" y2="215" stroke="#1e293b" stroke-width="2" marker-end="url(#ar02)" />

    <rect x="260" y="218" width="240" height="36" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="380" y="241" class="lbl" text-anchor="middle">执行 tool</text>

    <line x1="380" y1="254" x2="380" y2="283" stroke="#1e293b" stroke-width="2" marker-end="url(#ar02)" />

    <rect x="220" y="286" width="320" height="48" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="380" y="306" class="lbl" text-anchor="middle">after_tool_call hook chain</text>
    <text x="380" y="323" class="t-s" text-anchor="middle">subscribeEmbeddedPiSession 转 lifecycle:error</text>

    <line x1="380" y1="334" x2="380" y2="363" stroke="#1e293b" stroke-width="2" marker-end="url(#ar02)" />

    <rect x="220" y="366" width="320" height="48" rx="8" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.6" />
    <text x="380" y="386" class="lbl" text-anchor="middle">tool_result_persist hook</text>
    <text x="380" y="403" class="t-s" text-anchor="middle">通过则入 session JSONL（持久化）</text>

    <line x1="540" y1="162" x2="640" y2="162" stroke="#dc2626" stroke-width="2" stroke-dasharray="3 3" marker-end="url(#ar02)" />
    <text x="700" y="158" class="lbl" text-anchor="middle" fill="#dc2626">error 帧</text>
    <text x="700" y="172" class="t-s" text-anchor="middle" fill="#dc2626">agent.wait resolve</text>
  </g>
</svg>
"""

# 6. Tool dispatch 4 questions
DISPATCH_QUESTIONS = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 360" role="img"
     aria-label="工具 dispatch 4 个关键问题">
{DEFS}
  <text x="360" y="26" class="h" text-anchor="middle">工具 dispatch 的 4 个关键问题</text>
  <text x="360" y="44" class="t-s" text-anchor="middle">协议形态 + 时机 + 并行度 + 副作用：四个轴决定 dispatch 长什么样</text>

  <g filter="url(#wb02)">
    <rect x="60" y="70" width="290" height="115" rx="10" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <circle cx="92" cy="100" r="16" fill="#1e293b" />
    <text x="92" y="105" class="num" text-anchor="middle">1</text>
    <text x="120" y="93" class="lbl">调用形式</text>
    <text x="120" y="112" class="t">function call / tool_use block / RPC？</text>
    <text x="120" y="130" class="t-s">Codex Responses</text>
    <text x="120" y="146" class="t-s">Claude Code Anthropic tool_use</text>
    <text x="120" y="162" class="t-s">OpenClaw pi-agent-core</text>
    <text x="120" y="178" class="t-s">Hermes 双协议适配</text>

    <rect x="370" y="70" width="290" height="115" rx="10" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <circle cx="402" cy="100" r="16" fill="#1e293b" />
    <text x="402" y="105" class="num" text-anchor="middle">2</text>
    <text x="430" y="93" class="lbl">调度时机</text>
    <text x="430" y="112" class="t">流式中开始 vs 等完整 turn？</text>
    <text x="430" y="130" class="t-s">流式：Codex / Claude Code</text>
    <text x="430" y="146" class="t-s">事件流：OpenClaw</text>
    <text x="430" y="162" class="t-s">turn 末：Hermes</text>
    <text x="430" y="178" class="t-s">流式越早响应越省 latency</text>

    <rect x="60" y="195" width="290" height="115" rx="10" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <circle cx="92" cy="225" r="16" fill="#1e293b" />
    <text x="92" y="230" class="num" text-anchor="middle">3</text>
    <text x="120" y="218" class="lbl">并行度</text>
    <text x="120" y="237" class="t">单工具串行 / 同 turn 多工具并行？</text>
    <text x="120" y="255" class="t-s">Claude Code dispatchToolUseBlocks 并行</text>
    <text x="120" y="271" class="t-s">Codex / Hermes 默认串行</text>
    <text x="120" y="287" class="t-s">OpenClaw session lane 串行同 session</text>
    <text x="120" y="303" class="t-s">并行省 latency 但要 reconcile</text>

    <rect x="370" y="195" width="290" height="115" rx="10" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <circle cx="402" cy="225" r="16" fill="#1e293b" />
    <text x="402" y="230" class="num" text-anchor="middle">4</text>
    <text x="430" y="218" class="lbl">副作用</text>
    <text x="430" y="237" class="t">直接 / sandbox / 权限层？</text>
    <text x="430" y="255" class="t-s">Codex execpolicy + sandbox</text>
    <text x="430" y="271" class="t-s">Claude Code canUseTool hook</text>
    <text x="430" y="287" class="t-s">OpenClaw before_tool_call</text>
    <text x="430" y="303" class="t-s">Hermes skills_guard</text>
  </g>
</svg>
"""

# 7. Claude Code parallel tool_use
PARALLEL_DISPATCH = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 460" role="img"
     aria-label="Claude Code tool_use block 并行 dispatch">
{DEFS}
  <text x="390" y="26" class="h" text-anchor="middle">Claude Code · tool_use block 并行 dispatch</text>
  <text x="390" y="44" class="t-s" text-anchor="middle">stop_reason='tool_use' 不可信，代码自己数 block</text>

  <g filter="url(#wb02)">
    <rect x="260" y="70" width="260" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="390" y="93" class="lbl" text-anchor="middle">assistant message</text>

    <line x1="390" y1="106" x2="390" y2="125" stroke="#1e293b" stroke-width="2" marker-end="url(#ar02)" />

    <rect x="60" y="128" width="240" height="40" rx="6" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.5" />
    <text x="180" y="153" class="t" text-anchor="middle">text block: "I'll edit foo.ts..."</text>

    <rect x="320" y="128" width="200" height="40" rx="6" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.5" />
    <text x="420" y="153" class="t" text-anchor="middle">tool_use [Edit foo.ts]</text>

    <rect x="540" y="128" width="200" height="40" rx="6" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.5" />
    <text x="640" y="153" class="t" text-anchor="middle">tool_use [Bash run tests]</text>

    <rect x="320" y="178" width="200" height="40" rx="6" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.5" />
    <text x="420" y="203" class="t" text-anchor="middle">tool_use [Read bar.ts]</text>

    <line x1="420" y1="168" x2="420" y2="240" stroke="#1e293b" stroke-width="2" stroke-dasharray="3 3" />
    <line x1="640" y1="168" x2="640" y2="240" stroke="#1e293b" stroke-width="2" stroke-dasharray="3 3" />
    <line x1="420" y1="218" x2="420" y2="240" stroke="#1e293b" stroke-width="2" stroke-dasharray="3 3" />

    <rect x="240" y="245" width="300" height="44" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="390" y="265" class="lbl" text-anchor="middle">dispatchToolUseBlocks 并行执行</text>
    <text x="390" y="281" class="t-s" text-anchor="middle">canUseTool hook 单工具门控</text>

    <line x1="390" y1="289" x2="390" y2="308" stroke="#1e293b" stroke-width="2" marker-end="url(#ar02)" />

    <rect x="240" y="311" width="300" height="40" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="390" y="336" class="t" text-anchor="middle">每个 tool_use → 一个 tool_result</text>

    <line x1="390" y1="351" x2="390" y2="370" stroke="#1e293b" stroke-width="2" marker-end="url(#ar02)" />

    <rect x="240" y="373" width="300" height="44" rx="8" fill="#fde68a" stroke="#1e293b" stroke-width="1.6" />
    <text x="390" y="393" class="lbl" text-anchor="middle">组合成下一轮 user message</text>
    <text x="390" y="409" class="t-s" text-anchor="middle">queryLoop 数 tool_use=0 → 退出</text>
  </g>
</svg>
"""

# 8. Verifier 3 types
VERIFIER_TYPES = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 380" role="img"
     aria-label="Verifier 3 种类型">
{DEFS}
  <text x="380" y="26" class="h" text-anchor="middle">Verifier 的 3 种类型</text>
  <text x="380" y="44" class="t-s" text-anchor="middle">停得早 = 任务没完成；停得晚 = 烧 token / 死循环</text>

  <g filter="url(#wb02)">
    <rect x="60" y="70" width="640" height="80" rx="10" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="90" y="93" class="lbl">硬 verifier</text>
    <text x="90" y="111" class="t">外部规则 / 工具执行结果说话</text>
    <text x="90" y="128" class="t-s">run tests / lint / exit_code · 不通过 = 一定要继续</text>
    <text x="90" y="143" class="note">Codex 用这种最多（apply_patch + run tests + execpolicy）</text>

    <rect x="60" y="158" width="640" height="80" rx="10" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="90" y="181" class="lbl">软 verifier</text>
    <text x="90" y="199" class="t">内部状态 / 预算 / 启发式判断</text>
    <text x="90" y="216" class="t-s">token budget / 收敛率 / 重试次数 · 触发 = 软停或 nudge</text>
    <text x="90" y="231" class="note">Claude Code 90% 阈值 + 3 次 &lt; 500 token diminishing returns</text>

    <rect x="60" y="246" width="640" height="80" rx="10" fill="#fee2e2" stroke="#1e293b" stroke-width="1.6" />
    <text x="90" y="269" class="lbl">放任型 verifier</text>
    <text x="90" y="287" class="t">模型自己说停</text>
    <text x="90" y="304" class="t-s">finish_reason / 没有 tool_use · 信不信全凭模型自觉</text>
    <text x="90" y="319" class="note">兜底，所有系统都有，但单独用极不可靠</text>
  </g>

  <text x="380" y="355" class="t-s" text-anchor="middle">production 至少要硬 + 软双层；放任型作为兜底</text>
</svg>
"""

DIAGRAMS = [
    ("02-hermes-10-layer",          HERMES_10_LAYER),
    ("02-compression-decisions",    COMPRESSION_DECISIONS),
    ("02-claude-compact-pipeline",  CLAUDE_PIPELINE),
    ("02-error-recovery-angles",    ERROR_ANGLES),
    ("02-openclaw-hook-flow",       OPENCLAW_HOOK),
    ("02-tool-dispatch-questions",  DISPATCH_QUESTIONS),
    ("02-claude-tool-use-parallel", PARALLEL_DISPATCH),
    ("02-verifier-types",           VERIFIER_TYPES),
]


def write(slug, svg):
    out = PUBLIC / f"{slug}.svg"
    out.write_text(svg, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    PUBLIC.mkdir(parents=True, exist_ok=True)
    for slug, svg in DIAGRAMS:
        write(slug, svg)
