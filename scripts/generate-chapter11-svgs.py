#!/usr/bin/env python3
"""Chapter 11 SVGs: TradeOff (存储深度 × 生命周期颗粒度) + 四种 session 流程并列图."""
from pathlib import Path

PUBLIC = Path("public/diagrams")

TRADEOFF_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 480" role="img"
     aria-label="四家 session 模型在存储深度 × 生命周期颗粒度上的位置">
  <defs>
    <filter id="wb11"><feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="93" /><feDisplacementMap in="SourceGraphic" scale="2" /></filter>
    <marker id="ar11" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .ax   { font: 600 12.5px sans-serif; fill: #1e293b; }
      .t    { font: 11.5px sans-serif; fill: #334155; }
      .t-s  { font: 10.5px sans-serif; fill: #64748b; }
      .pin  { font: 700 12.5px sans-serif; fill: #fff; }
      .note { font: italic 10.5px sans-serif; fill: #475569; }
    </style>
  </defs>

  <text x="390" y="26" class="h" text-anchor="middle">Session 生命周期：存储工程化 × 生命周期颗粒度</text>
  <text x="390" y="44" class="t-s" text-anchor="middle">越往右存储越重；越往上 hook 颗粒越细；选哪种取决于产品定位</text>

  <g filter="url(#wb11)">
    <rect x="100" y="80" width="280" height="160" fill="#fef9c3" opacity="0.4" />
    <rect x="380" y="80" width="280" height="160" fill="#dcfce7" opacity="0.4" />
    <rect x="100" y="240" width="280" height="160" fill="#dbeafe" opacity="0.4" />
    <rect x="380" y="240" width="280" height="160" fill="#fee2e2" opacity="0.4" />

    <text x="120" y="100" class="t-s">极简 · 细颗粒 hook</text>
    <text x="640" y="100" class="t-s" text-anchor="end">重持久 · 细颗粒 hook</text>
    <text x="120" y="260" class="t-s">极简 · 无 hook</text>
    <text x="640" y="260" class="t-s" text-anchor="end">重持久 · 无 hook</text>

    <line x1="100" y1="400" x2="660" y2="400" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar11)" />
    <line x1="100" y1="400" x2="100" y2="70" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar11)" />
    <line x1="380" y1="80" x2="380" y2="400" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />
    <line x1="100" y1="240" x2="660" y2="240" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />

    <text x="660" y="420" class="ax" text-anchor="end">session 存储 / 索引深度 →</text>
    <text x="110" y="68" class="ax">↑ 生命周期事件颗粒度</text>

    <!-- OpenClaw bottom-left -->
    <circle cx="180" cy="320" r="14" fill="#16a34a" stroke="#1e293b" stroke-width="2" />
    <text x="180" y="324" class="pin" text-anchor="middle">OC</text>
    <text x="180" y="351" class="t" text-anchor="middle">OpenClaw</text>
    <text x="180" y="366" class="t-s" text-anchor="middle">UUID 正则一行</text>
    <text x="180" y="379" class="t-s" text-anchor="middle">怎么存交给上层</text>

    <!-- Codex right-middle -->
    <circle cx="600" cy="220" r="14" fill="#2563eb" stroke="#1e293b" stroke-width="2" />
    <text x="600" y="224" class="pin" text-anchor="middle">CX</text>
    <text x="600" y="251" class="t" text-anchor="middle">Codex</text>
    <text x="600" y="266" class="t-s" text-anchor="middle">JSONL + SQLite</text>
    <text x="600" y="279" class="t-s" text-anchor="middle">5 RolloutItem 类型</text>

    <!-- Claude Code top-right -->
    <circle cx="570" cy="120" r="14" fill="#7c3aed" stroke="#1e293b" stroke-width="2" />
    <text x="570" y="124" class="pin" text-anchor="middle">CC</text>
    <text x="570" y="151" class="t" text-anchor="middle">Claude Code</text>
    <text x="570" y="166" class="t-s" text-anchor="middle">22 工具 + 4 hook</text>
    <text x="570" y="179" class="t-s" text-anchor="middle">startup/resume/clear/compact</text>

    <!-- Hermes mid-upper-mid -->
    <circle cx="385" cy="170" r="14" fill="#f97316" stroke="#1e293b" stroke-width="2" />
    <text x="385" y="174" class="pin" text-anchor="middle">HM</text>
    <text x="385" y="201" class="t" text-anchor="middle">Hermes</text>
    <text x="385" y="216" class="t-s" text-anchor="middle">多平台 SessionSource</text>
    <text x="385" y="229" class="t-s" text-anchor="middle">+ 4 reset 模式</text>
  </g>

  <text x="20" y="465" class="t-s">CX = Codex · CC = Claude Code · OC = OpenClaw · HM = Hermes</text>
</svg>
"""

FLOWS_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 620" role="img"
     aria-label="四种 session 模型流程并列">
  <defs>
    <filter id="wb11F"><feTurbulence type="fractalNoise" baseFrequency="0.022" numOctaves="2" seed="103" /><feDisplacementMap in="SourceGraphic" scale="1.5" /></filter>
    <marker id="ar11F" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .col  { font: 700 13px sans-serif; fill: #1e293b; }
      .lbl  { font: 700 11px sans-serif; fill: #1e293b; }
      .t-s  { font: 10.5px sans-serif; fill: #475569; }
      .note { font: italic 10.5px sans-serif; fill: #b45309; }
    </style>
  </defs>

  <text x="440" y="24" class="h" text-anchor="middle">四种 session 模型流程并列</text>
  <text x="440" y="42" class="t-s" text-anchor="middle">JSONL 持久（Codex）· 多 hook IDE（Claude Code）· 极简 id（OpenClaw）· 多平台路由（Hermes）</text>

  <g filter="url(#wb11F)">
    <!-- Codex column -->
    <text x="120" y="70" class="col" text-anchor="middle">Codex · JSONL + SQLite</text>
    <rect x="40" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="103" class="lbl" text-anchor="middle">创建 session</text>

    <line x1="120" y1="116" x2="120" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar11F)" />

    <rect x="40" y="138" width="160" height="48" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="158" class="lbl" text-anchor="middle">rollout-{ts}-{uuid}.jsonl</text>
    <text x="120" y="174" class="t-s" text-anchor="middle">line 1: SessionMeta</text>

    <line x1="120" y1="186" x2="120" y2="205" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar11F)" />

    <rect x="40" y="208" width="160" height="60" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="228" class="lbl" text-anchor="middle">每 turn 追加</text>
    <text x="120" y="244" class="t-s" text-anchor="middle">ResponseItem · EventMsg</text>
    <text x="120" y="258" class="t-s" text-anchor="middle">Compacted · TurnContext</text>

    <line x1="120" y1="268" x2="120" y2="287" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar11F)" />

    <rect x="40" y="290" width="160" height="48" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="310" class="lbl" text-anchor="middle">state.db 索引</text>
    <text x="120" y="326" class="t-s" text-anchor="middle">thread list 快速查</text>

    <line x1="120" y1="338" x2="120" y2="357" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar11F)" />

    <rect x="40" y="360" width="160" height="48" rx="8" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="380" class="lbl" text-anchor="middle">resume</text>
    <text x="120" y="396" class="t-s" text-anchor="middle">SessionMeta → 元数据</text>

    <text x="120" y="430" class="note" text-anchor="middle">append-only JSONL</text>
    <text x="120" y="445" class="note" text-anchor="middle">崩溃也能恢复</text>

    <!-- Claude Code column -->
    <text x="330" y="70" class="col" text-anchor="middle">Claude Code · 4 hook + 22 工具</text>
    <rect x="250" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="103" class="lbl" text-anchor="middle">source: startup/resume/...</text>

    <line x1="330" y1="116" x2="330" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar11F)" />

    <rect x="250" y="138" width="160" height="48" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="158" class="lbl" text-anchor="middle">loadPluginHooks</text>
    <text x="330" y="174" class="t-s" text-anchor="middle">managed-only 时跳过</text>

    <line x1="330" y1="186" x2="330" y2="205" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar11F)" />

    <rect x="250" y="208" width="160" height="48" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="228" class="lbl" text-anchor="middle">processSessionStartHooks</text>
    <text x="330" y="244" class="t-s" text-anchor="middle">注入 CLAUDE.md 上下文</text>

    <line x1="330" y1="256" x2="330" y2="275" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar11F)" />

    <rect x="250" y="278" width="160" height="72" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="298" class="lbl" text-anchor="middle">sessionRestore</text>
    <text x="330" y="314" class="t-s" text-anchor="middle">cost / attribution / files</text>
    <text x="330" y="328" class="t-s" text-anchor="middle">todos / model / worktree</text>
    <text x="330" y="342" class="t-s" text-anchor="middle">+ systemPrompt</text>

    <line x1="330" y1="350" x2="330" y2="369" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar11F)" />

    <rect x="250" y="372" width="160" height="36" rx="8" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="395" class="lbl" text-anchor="middle">主对话开始</text>

    <text x="330" y="430" class="note" text-anchor="middle">禁令：不准 warmup</text>
    <text x="330" y="445" class="note" text-anchor="middle">启动路径上的额外工作长期失控</text>

    <!-- OpenClaw column -->
    <text x="540" y="70" class="col" text-anchor="middle">OpenClaw · 极简 id</text>
    <rect x="460" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="103" class="lbl" text-anchor="middle">user 发送消息</text>

    <line x1="540" y1="116" x2="540" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar11F)" />

    <rect x="460" y="138" width="160" height="48" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="158" class="lbl" text-anchor="middle">SESSION_ID_RE 校验</text>
    <text x="540" y="174" class="t-s" text-anchor="middle">UUID 正则一行</text>

    <line x1="540" y1="186" x2="540" y2="205" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar11F)" />

    <rect x="460" y="208" width="160" height="48" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="228" class="lbl" text-anchor="middle">session-key 拼接</text>
    <text x="540" y="244" class="t-s" text-anchor="middle">{agentId}:{sessionId}</text>

    <line x1="540" y1="256" x2="540" y2="275" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar11F)" />

    <rect x="460" y="278" width="160" height="48" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="298" class="lbl" text-anchor="middle">transcript 事件序列化</text>
    <text x="540" y="314" class="t-s" text-anchor="middle">存哪交给上层</text>

    <line x1="540" y1="326" x2="540" y2="345" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar11F)" />

    <rect x="460" y="348" width="160" height="36" rx="8" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="371" class="lbl" text-anchor="middle">router 路由到 agent</text>

    <text x="540" y="410" class="note" text-anchor="middle">12 文件 vs CC 的 22 工具</text>
    <text x="540" y="425" class="note" text-anchor="middle">平台型 agent 最薄选择</text>

    <!-- Hermes column -->
    <text x="760" y="70" class="col" text-anchor="middle">Hermes · 多平台 + reset</text>
    <rect x="680" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="103" class="lbl" text-anchor="middle">Slack/TG/Discord 消息</text>

    <line x1="760" y1="116" x2="760" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar11F)" />

    <rect x="680" y="138" width="160" height="60" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="158" class="lbl" text-anchor="middle">SessionSource</text>
    <text x="760" y="174" class="t-s" text-anchor="middle">platform + chat_id</text>
    <text x="760" y="188" class="t-s" text-anchor="middle">+ user / chat 元数据</text>

    <line x1="760" y1="198" x2="760" y2="217" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar11F)" />

    <rect x="680" y="220" width="160" height="60" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="240" class="lbl" text-anchor="middle">SessionResetPolicy</text>
    <text x="760" y="256" class="t-s" text-anchor="middle">daily / idle / both / none</text>
    <text x="760" y="270" class="t-s" text-anchor="middle">at_hour=4 · idle=1440min</text>

    <line x1="760" y1="280" x2="760" y2="299" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar11F)" />

    <rect x="680" y="302" width="160" height="60" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="322" class="lbl" text-anchor="middle">build_session_context</text>
    <text x="760" y="338" class="t-s" text-anchor="middle">注入 system prompt</text>
    <text x="760" y="352" class="t-s" text-anchor="middle">PII redact for safe platforms</text>

    <line x1="760" y1="362" x2="760" y2="381" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar11F)" />

    <rect x="680" y="384" width="160" height="36" rx="8" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="407" class="lbl" text-anchor="middle">home_channels 路由</text>

    <text x="760" y="440" class="note" text-anchor="middle">6+ 平台 · 跨平台 reset</text>
    <text x="760" y="455" class="note" text-anchor="middle">cron 输出 → home channel</text>
  </g>

  <text x="440" y="495" class="t-s" text-anchor="middle">从左到右：文件级持久 → 子系统分层 → 极简 ID → 多平台路由。四种思路各有最适合的产品形态。</text>

  <g>
    <rect x="40" y="510" width="800" height="80" rx="8" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1" />
    <text x="60" y="530" class="lbl">共同点：</text>
    <text x="60" y="548" class="t-s">· session_id 全用 UUID 或 timestamp+UUID 防碰撞</text>
    <text x="60" y="564" class="t-s">· session 跟 user / scope 绑定（agent_path / worktree / agentId / platform:chat_id）</text>
    <text x="60" y="580" class="t-s">· resume 要恢复元数据（cwd / model / approval mode）而不止重放消息</text>
  </g>
</svg>
"""


def write(slug, svg):
    out = PUBLIC / f"{slug}.svg"
    out.write_text(svg, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    PUBLIC.mkdir(parents=True, exist_ok=True)
    write("11-tradeoff", TRADEOFF_SVG)
    write("11-session-flows", FLOWS_SVG)
