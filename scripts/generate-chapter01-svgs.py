#!/usr/bin/env python3
"""Chapter 01 TradeOff replacement: 短期可控性 × 长期自治度 with scenario annotations."""
from pathlib import Path

PUBLIC = Path("public/diagrams")

TRADEOFF_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 500" role="img"
     aria-label="四家 Agent 在短期可控性 × 长期自治度 两条轴上的分布与场景映射">
  <defs>
    <filter id="wb01">
      <feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="3" />
      <feDisplacementMap in="SourceGraphic" scale="2" />
    </filter>
    <marker id="ar01" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#1e293b" />
    </marker>
    <marker id="ar01-thin" markerWidth="9" markerHeight="9" refX="8" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#64748b" />
    </marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .ax   { font: 600 12.5px sans-serif; fill: #1e293b; }
      .t    { font: 11.5px sans-serif; fill: #334155; }
      .t-s  { font: 10.5px sans-serif; fill: #64748b; }
      .pin  { font: 700 12.5px sans-serif; fill: #fff; }
      .case { font: italic 10.5px sans-serif; fill: #475569; }
    </style>
  </defs>

  <text x="390" y="26" class="h" text-anchor="middle">四家位置：短期可控性 ↔ 长期自治度</text>
  <text x="390" y="44" class="t-s" text-anchor="middle">同一份 Agent 工程，给你 4 个分布在对角线上的取舍点，不是优劣，是场景适配</text>

  <g filter="url(#wb01)">
    <!-- background quadrants -->
    <rect x="90" y="80" width="290" height="160" fill="#fef9c3" opacity="0.4" />
    <rect x="380" y="80" width="290" height="160" fill="#dcfce7" opacity="0.4" />
    <rect x="90" y="240" width="290" height="180" fill="#dbeafe" opacity="0.4" />
    <rect x="380" y="240" width="290" height="180" fill="#fee2e2" opacity="0.4" />

    <text x="105" y="100" class="t-s">短期严控 · 不自跑</text>
    <text x="660" y="100" class="t-s" text-anchor="end">短期严控 · 长跑也行</text>
    <text x="105" y="260" class="t-s">每步审批 · 不自跑</text>
    <text x="660" y="260" class="t-s" text-anchor="end">放手让它跑</text>

    <!-- axes -->
    <line x1="90" y1="420" x2="670" y2="420" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar01)" />
    <line x1="90" y1="420" x2="90" y2="70" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar01)" />
    <line x1="380" y1="80" x2="380" y2="420" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />
    <line x1="90" y1="240" x2="670" y2="240" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />

    <text x="670" y="440" class="ax" text-anchor="end">短期可控性（每步审批的难度）→</text>
    <text x="100" y="68" class="ax">↑ 长期自治度（自跑 + 自学）</text>

    <!-- Codex: bottom-left, high control low autonomy -->
    <circle cx="170" cy="345" r="15" fill="#2563eb" stroke="#1e293b" stroke-width="2" />
    <text x="170" y="349" class="pin" text-anchor="middle">CX</text>
    <text x="170" y="378" class="t" text-anchor="middle">Codex</text>
    <text x="170" y="393" class="t-s" text-anchor="middle">execpolicy 每步审</text>
    <text x="170" y="406" class="t-s" text-anchor="middle">rollout 可恢复</text>

    <!-- Claude Code: mid -->
    <circle cx="330" cy="260" r="15" fill="#7c3aed" stroke="#1e293b" stroke-width="2" />
    <text x="330" y="264" class="pin" text-anchor="middle">CC</text>
    <text x="330" y="293" class="t" text-anchor="middle">Claude Code</text>
    <text x="330" y="308" class="t-s" text-anchor="middle">5 优先级 + 7 transition</text>
    <text x="330" y="321" class="t-s" text-anchor="middle">短期细控、中期可</text>

    <!-- OpenClaw: middle-upper -->
    <circle cx="480" cy="190" r="15" fill="#16a34a" stroke="#1e293b" stroke-width="2" />
    <text x="480" y="194" class="pin" text-anchor="middle">OC</text>
    <text x="480" y="223" class="t" text-anchor="middle">OpenClaw</text>
    <text x="480" y="238" class="t-s" text-anchor="middle">plugin 主导 + lane 并发</text>
    <text x="480" y="251" class="t-s" text-anchor="middle">中长跑 + 多用户</text>

    <!-- Hermes: top-right, most autonomy -->
    <circle cx="600" cy="120" r="15" fill="#f97316" stroke="#1e293b" stroke-width="2" />
    <text x="600" y="124" class="pin" text-anchor="middle">HM</text>
    <text x="600" y="153" class="t" text-anchor="middle">Hermes</text>
    <text x="600" y="168" class="t-s" text-anchor="middle">memory + self-eval</text>
    <text x="600" y="181" class="t-s" text-anchor="middle">最适合长跑助理</text>

    <!-- scenario tags -->
    <text x="50" y="465" class="case">「改一个 repo · 每步 review」 →</text>
    <line x1="180" y1="462" x2="170" y2="360" stroke="#64748b" stroke-width="1" stroke-dasharray="3 2" marker-end="url(#ar01-thin)" />

    <text x="230" y="465" class="case">「Slack bot · 多用户并发」 →</text>
    <line x1="380" y1="462" x2="480" y2="205" stroke="#64748b" stroke-width="1" stroke-dasharray="3 2" marker-end="url(#ar01-thin)" />

    <text x="430" y="485" class="case">「私人助理 · 长跑跨会话」 →</text>
    <line x1="600" y1="482" x2="600" y2="135" stroke="#64748b" stroke-width="1" stroke-dasharray="3 2" marker-end="url(#ar01-thin)" />
  </g>

  <text x="20" y="20" class="t-s">没有「最好」，只有「适配场景」。看你的产品是改 repo、做 server、还是长跑助理。</text>
</svg>
"""


def write(slug, svg):
    out = PUBLIC / f"{slug}.svg"
    out.write_text(svg, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    PUBLIC.mkdir(parents=True, exist_ok=True)
    write("01-tradeoff", TRADEOFF_SVG)
