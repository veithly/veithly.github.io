#!/usr/bin/env python3
"""Chapter 14 SVGs: TradeOff (通道数量 x 生态开放度) + 四种入口拓扑并列图."""
from pathlib import Path

PUBLIC = Path("public/diagrams")

TRADEOFF_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 480" role="img"
     aria-label="四家多通道入口在通道数量 x 生态开放度上的位置">
  <defs>
    <filter id="wb14"><feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="141" /><feDisplacementMap in="SourceGraphic" scale="2" /></filter>
    <marker id="ar14" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .ax   { font: 600 12.5px sans-serif; fill: #1e293b; }
      .t    { font: 11.5px sans-serif; fill: #334155; }
      .t-s  { font: 10.5px sans-serif; fill: #64748b; }
      .pin  { font: 700 12.5px sans-serif; fill: #fff; }
      .note { font: italic 10.5px sans-serif; fill: #475569; }
    </style>
  </defs>

  <text x="390" y="26" class="h" text-anchor="middle">多通道入口：通道数量 x 生态开放度</text>
  <text x="390" y="44" class="t-s" text-anchor="middle">越往右通道越多；越往上第三方越容易接新通道；选哪种取决于 agent 形态</text>

  <g filter="url(#wb14)">
    <rect x="100" y="80" width="280" height="160" fill="#fef9c3" opacity="0.4" />
    <rect x="380" y="80" width="280" height="160" fill="#dcfce7" opacity="0.4" />
    <rect x="100" y="240" width="280" height="160" fill="#dbeafe" opacity="0.4" />
    <rect x="380" y="240" width="280" height="160" fill="#fee2e2" opacity="0.4" />

    <text x="120" y="100" class="t-s">少通道 · 开放</text>
    <text x="640" y="100" class="t-s" text-anchor="end">多通道 · 开放</text>
    <text x="120" y="260" class="t-s">少通道 · 封闭</text>
    <text x="640" y="260" class="t-s" text-anchor="end">多通道 · 封闭</text>

    <line x1="100" y1="400" x2="660" y2="400" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar14)" />
    <line x1="100" y1="400" x2="100" y2="70" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar14)" />
    <line x1="380" y1="80" x2="380" y2="400" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />
    <line x1="100" y1="240" x2="660" y2="240" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />

    <text x="660" y="420" class="ax" text-anchor="end">通道数量 →</text>
    <text x="110" y="68" class="ax">↑ 生态开放度（第三方接新通道难度低=高）</text>

    <!-- Claude Code: bottom-left (8 子命令 一个 binary) -->
    <circle cx="220" cy="290" r="14" fill="#7c3aed" stroke="#1e293b" stroke-width="2" />
    <text x="220" y="294" class="pin" text-anchor="middle">CC</text>
    <text x="220" y="321" class="t" text-anchor="middle">Claude Code</text>
    <text x="220" y="336" class="t-s" text-anchor="middle">单 binary + 8 subcommand</text>
    <text x="220" y="349" class="t-s" text-anchor="middle">commander.js</text>

    <!-- Codex: middle-left (8 个 binary 多入口但封闭) -->
    <circle cx="280" cy="200" r="14" fill="#2563eb" stroke="#1e293b" stroke-width="2" />
    <text x="280" y="204" class="pin" text-anchor="middle">CX</text>
    <text x="280" y="231" class="t" text-anchor="middle">Codex</text>
    <text x="280" y="246" class="t-s" text-anchor="middle">multi-binary</text>
    <text x="280" y="259" class="t-s" text-anchor="middle">tui/exec/mcp/app-server</text>

    <!-- OpenClaw: top-middle (19 sub-CLI + channels-plugins 最开放) -->
    <circle cx="500" cy="130" r="14" fill="#16a34a" stroke="#1e293b" stroke-width="2" />
    <text x="500" y="134" class="pin" text-anchor="middle">OC</text>
    <text x="500" y="161" class="t" text-anchor="middle">OpenClaw</text>
    <text x="500" y="176" class="t-s" text-anchor="middle">19 sub-CLI + plugins</text>
    <text x="500" y="189" class="t-s" text-anchor="middle">ACP + channels-plugins</text>

    <!-- Hermes: right-middle (17 platform 多但内置) -->
    <circle cx="620" cy="270" r="14" fill="#f97316" stroke="#1e293b" stroke-width="2" />
    <text x="620" y="274" class="pin" text-anchor="middle">HM</text>
    <text x="620" y="301" class="t" text-anchor="middle">Hermes</text>
    <text x="620" y="316" class="t-s" text-anchor="middle">17 platform adapter</text>
    <text x="620" y="329" class="t-s" text-anchor="middle">主仓库内置</text>
  </g>

  <text x="20" y="465" class="t-s">CX = Codex · CC = Claude Code · OC = OpenClaw · HM = Hermes</text>
</svg>
"""

FLOWS_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 600" role="img"
     aria-label="四种入口拓扑并列对照">
  <defs>
    <filter id="wb14F"><feTurbulence type="fractalNoise" baseFrequency="0.022" numOctaves="2" seed="143" /><feDisplacementMap in="SourceGraphic" scale="1.5" /></filter>
    <marker id="ar14F" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .col  { font: 700 13px sans-serif; fill: #1e293b; }
      .lbl  { font: 700 11px sans-serif; fill: #1e293b; }
      .t-s  { font: 10.5px sans-serif; fill: #475569; }
      .note { font: italic 10.5px sans-serif; fill: #b45309; }
    </style>
  </defs>

  <text x="440" y="24" class="h" text-anchor="middle">四种入口拓扑并列</text>
  <text x="440" y="42" class="t-s" text-anchor="middle">多 binary（Codex）· 单 binary + subcommand（Claude Code）· 19 sub-CLI + plugin（OpenClaw）· 17 platform（Hermes）</text>

  <g filter="url(#wb14F)">
    <!-- Codex column -->
    <text x="120" y="70" class="col" text-anchor="middle">Codex · multi-binary</text>
    <rect x="40" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="103" class="lbl" text-anchor="middle">codex (TUI ratatui)</text>

    <rect x="40" y="124" width="160" height="36" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="147" class="lbl" text-anchor="middle">codex exec (脚本)</text>

    <rect x="40" y="168" width="160" height="36" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="191" class="lbl" text-anchor="middle">codex mcp-server</text>

    <rect x="40" y="212" width="160" height="36" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="235" class="lbl" text-anchor="middle">codex app-server</text>
    <text x="120" y="249" class="t-s" text-anchor="middle">axum HTTP1 + WS</text>

    <rect x="40" y="262" width="160" height="48" rx="8" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="282" class="lbl" text-anchor="middle">stdio-to-uds 桥</text>
    <text x="120" y="298" class="t-s" text-anchor="middle">IDE stdio ↔ daemon UDS</text>

    <rect x="40" y="316" width="160" height="36" rx="8" fill="#fce7f3" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="339" class="lbl" text-anchor="middle">codex app (桌面 GUI)</text>

    <rect x="40" y="358" width="160" height="36" rx="8" fill="#ecfccb" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="381" class="lbl" text-anchor="middle">codex cloud</text>

    <text x="120" y="420" class="note" text-anchor="middle">每入口独立 binary</text>
    <text x="120" y="435" class="note" text-anchor="middle">可单独升级 / 分发</text>

    <!-- Claude Code column -->
    <text x="330" y="70" class="col" text-anchor="middle">Claude Code · single binary</text>
    <rect x="250" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="103" class="lbl" text-anchor="middle">claude (REPL ink)</text>

    <rect x="250" y="124" width="160" height="36" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="147" class="lbl" text-anchor="middle">claude -p (脚本)</text>

    <rect x="250" y="168" width="160" height="36" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="191" class="lbl" text-anchor="middle">claude --bare</text>
    <text x="330" y="204" class="t-s" text-anchor="middle">CI / SDK 干净入口</text>

    <rect x="250" y="218" width="160" height="36" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="241" class="lbl" text-anchor="middle">claude mcp serve</text>

    <rect x="250" y="262" width="160" height="36" rx="8" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="285" class="lbl" text-anchor="middle">claude server (HTTP/UDS)</text>

    <rect x="250" y="306" width="160" height="36" rx="8" fill="#fce7f3" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="329" class="lbl" text-anchor="middle">claude auth/plugin/doctor</text>

    <text x="330" y="420" class="note" text-anchor="middle">commander.js dispatch</text>
    <text x="330" y="435" class="note" text-anchor="middle">main.tsx 万行单文件</text>

    <!-- OpenClaw column -->
    <text x="540" y="70" class="col" text-anchor="middle">OpenClaw · 19 sub-CLI + plugin</text>
    <rect x="460" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="103" class="lbl" text-anchor="middle">gateway daemon</text>

    <line x1="540" y1="116" x2="540" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar14F)" />

    <rect x="460" y="138" width="160" height="36" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="161" class="lbl" text-anchor="middle">RPC / WS</text>

    <line x1="540" y1="174" x2="540" y2="193" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar14F)" />

    <rect x="460" y="196" width="160" height="48" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="216" class="lbl" text-anchor="middle">19 sub-CLI (lazy)</text>
    <text x="540" y="232" class="t-s" text-anchor="middle">acp/tui/channels/sandbox</text>

    <line x1="540" y1="244" x2="540" y2="263" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar14F)" />

    <rect x="460" y="266" width="160" height="48" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="286" class="lbl" text-anchor="middle">ACP server</text>
    <text x="540" y="302" class="t-s" text-anchor="middle">@agentclientprotocol/sdk</text>

    <line x1="540" y1="314" x2="540" y2="333" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar14F)" />

    <rect x="460" y="336" width="160" height="48" rx="8" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="356" class="lbl" text-anchor="middle">channels-plugins</text>
    <text x="540" y="372" class="t-s" text-anchor="middle">npm 包 catalog</text>

    <text x="540" y="420" class="note" text-anchor="middle">每 sub-CLI 一个文件</text>
    <text x="540" y="435" class="note" text-anchor="middle">用到才 import</text>

    <!-- Hermes column -->
    <text x="760" y="70" class="col" text-anchor="middle">Hermes · 17 platform adapter</text>
    <rect x="680" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="103" class="lbl" text-anchor="middle">GatewayRunner (单进程)</text>

    <line x1="760" y1="116" x2="760" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar14F)" />

    <rect x="680" y="138" width="160" height="60" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="158" class="lbl" text-anchor="middle">BasePlatformAdapter</text>
    <text x="760" y="174" class="t-s" text-anchor="middle">6 abstract method</text>
    <text x="760" y="188" class="t-s" text-anchor="middle">connect/send/disconnect</text>

    <line x1="760" y1="198" x2="760" y2="217" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar14F)" />

    <rect x="680" y="220" width="160" height="60" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="240" class="lbl" text-anchor="middle">17 platform 实现</text>
    <text x="760" y="256" class="t-s" text-anchor="middle">TG/Discord/Slack/...</text>
    <text x="760" y="270" class="t-s" text-anchor="middle">Email/SMS/HA/Matrix</text>

    <line x1="760" y1="280" x2="760" y2="299" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar14F)" />

    <rect x="680" y="302" width="160" height="48" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="322" class="lbl" text-anchor="middle">check_xxx_requirements</text>
    <text x="760" y="338" class="t-s" text-anchor="middle">缺依赖优雅降级</text>

    <line x1="760" y1="350" x2="760" y2="369" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar14F)" />

    <rect x="680" y="372" width="160" height="48" rx="8" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="392" class="lbl" text-anchor="middle">API_SERVER + WEBHOOK</text>
    <text x="760" y="408" class="t-s" text-anchor="middle">也建模为 platform</text>

    <text x="760" y="445" class="note" text-anchor="middle">主包带所有 adapter</text>
    <text x="760" y="460" class="note" text-anchor="middle">extra deps 才装 SDK</text>
  </g>

  <text x="440" y="490" class="t-s" text-anchor="middle">用户怎么进来？四种回答给四种 agent 形态</text>

  <g>
    <rect x="40" y="505" width="800" height="80" rx="8" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1" />
    <text x="60" y="525" class="lbl">共同点：</text>
    <text x="60" y="543" class="t-s">· 都给 MCP server 入口（Codex/Claude/Hermes）或 ACP（OpenClaw）</text>
    <text x="60" y="559" class="t-s">· CLI 跟 daemon 分两层（OpenClaw 最显式，Codex 通过 stdio-to-uds）</text>
    <text x="60" y="575" class="t-s">· 入口要能力探测，缺依赖优雅降级</text>
  </g>
</svg>
"""

def write(slug, svg):
    out = PUBLIC / f"{slug}.svg"
    out.write_text(svg, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    PUBLIC.mkdir(parents=True, exist_ok=True)
    write("14-tradeoff", TRADEOFF_SVG)
    write("14-entry-topologies", FLOWS_SVG)
