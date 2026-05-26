#!/usr/bin/env python3
"""Chapter 03 SVGs: TradeOff (装配灵活度 × cache 命中率) + 注入流水线."""
from pathlib import Path

PUBLIC = Path("public/diagrams")

TRADEOFF_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 480" role="img"
     aria-label="四家 Context System 在装配灵活度 × cache 命中率 两条轴上的位置">
  <defs>
    <filter id="wb03"><feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="5" /><feDisplacementMap in="SourceGraphic" scale="2" /></filter>
    <marker id="ar03" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .ax   { font: 600 12.5px sans-serif; fill: #1e293b; }
      .t    { font: 11.5px sans-serif; fill: #334155; }
      .t-s  { font: 10.5px sans-serif; fill: #64748b; }
      .pin  { font: 700 12.5px sans-serif; fill: #fff; }
      .note { font: italic 10.5px sans-serif; fill: #475569; }
    </style>
  </defs>

  <text x="390" y="26" class="h" text-anchor="middle">Context System：装配灵活度 × cache 命中率</text>
  <text x="390" y="44" class="t-s" text-anchor="middle">cache 友好和能动态拼装是天然矛盾。Claude Code 用魔法字符串切两段，Hermes 直接放弃 cache</text>

  <g filter="url(#wb03)">
    <rect x="100" y="80" width="280" height="160" fill="#dcfce7" opacity="0.4" />
    <rect x="380" y="80" width="280" height="160" fill="#fef9c3" opacity="0.4" />
    <rect x="100" y="240" width="280" height="160" fill="#fee2e2" opacity="0.4" />
    <rect x="380" y="240" width="280" height="160" fill="#dbeafe" opacity="0.4" />

    <text x="120" y="100" class="t-s">死板 + 高命中</text>
    <text x="640" y="100" class="t-s" text-anchor="end">灵活 + 高命中 · 圣杯</text>
    <text x="120" y="260" class="t-s">死板 + 低命中（最差）</text>
    <text x="640" y="260" class="t-s" text-anchor="end">灵活 + 低命中</text>

    <line x1="100" y1="400" x2="660" y2="400" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar03)" />
    <line x1="100" y1="400" x2="100" y2="70" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar03)" />
    <line x1="380" y1="80" x2="380" y2="400" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />
    <line x1="100" y1="240" x2="660" y2="240" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />

    <text x="660" y="420" class="ax" text-anchor="end">装配灵活度（运行时能动态拼多少）→</text>
    <text x="110" y="68" class="ax">↑ cache 命中率（一份 prompt 跑多次）</text>

    <!-- Claude Code: top-left-ish (high cache, mid flex) -->
    <circle cx="310" cy="125" r="15" fill="#7c3aed" stroke="#1e293b" stroke-width="2" />
    <text x="310" y="129" class="pin" text-anchor="middle">CC</text>
    <text x="310" y="158" class="t" text-anchor="middle">Claude Code</text>
    <text x="310" y="173" class="t-s" text-anchor="middle">DYNAMIC_BOUNDARY 显式</text>
    <text x="310" y="186" class="t-s" text-anchor="middle">5 优先级 · cache 天花板</text>

    <!-- Codex: mid-left -->
    <circle cx="250" cy="200" r="15" fill="#2563eb" stroke="#1e293b" stroke-width="2" />
    <text x="250" y="204" class="pin" text-anchor="middle">CX</text>
    <text x="250" y="232" class="t" text-anchor="middle">Codex</text>
    <text x="250" y="247" class="t-s" text-anchor="middle">24 fragment · marker</text>
    <text x="250" y="260" class="t-s" text-anchor="middle">可压缩、可 diff</text>

    <!-- OpenClaw: middle -->
    <circle cx="460" cy="240" r="15" fill="#16a34a" stroke="#1e293b" stroke-width="2" />
    <text x="460" y="244" class="pin" text-anchor="middle">OC</text>
    <text x="460" y="272" class="t" text-anchor="middle">OpenClaw</text>
    <text x="460" y="287" class="t-s" text-anchor="middle">buildXxxSection + 3 档</text>
    <text x="460" y="300" class="t-s" text-anchor="middle">主子 prompt 易污染</text>

    <!-- Hermes: bottom-right (high flex, low cache) -->
    <circle cx="580" cy="335" r="15" fill="#f97316" stroke="#1e293b" stroke-width="2" />
    <text x="580" y="339" class="pin" text-anchor="middle">HM</text>
    <text x="580" y="368" class="t" text-anchor="middle">Hermes</text>
    <text x="580" y="383" class="t-s" text-anchor="middle">10 层 + skip_* 开关</text>
    <text x="580" y="396" class="t-s" text-anchor="middle">SOUL.md 改人格 · 弃 cache</text>

    <!-- annotation: right-top quadrant empty -->
    <text x="530" y="125" class="note" text-anchor="middle">右上角无人</text>
    <text x="530" y="142" class="note" text-anchor="middle">cache 与动态相斥</text>
  </g>

  <text x="20" y="465" class="t-s">CX = Codex · CC = Claude Code · OC = OpenClaw · HM = Hermes</text>
</svg>
"""

PIPELINE_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 380" role="img"
     aria-label="Claude Code 注入流水线：splitSysPromptPrefix + DYNAMIC_BOUNDARY + appendDynamicContext">
  <defs>
    <filter id="wb03p"><feTurbulence type="fractalNoise" baseFrequency="0.022" numOctaves="2" seed="8" /><feDisplacementMap in="SourceGraphic" scale="1.5" /></filter>
    <marker id="ar03p" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .lbl  { font: 700 12.5px sans-serif; fill: #1e293b; }
      .t    { font: 11.5px sans-serif; fill: #334155; }
      .t-s  { font: 10.5px sans-serif; fill: #475569; }
      .cache { font: italic 11px sans-serif; fill: #1e293b; }
      .dyn  { font: italic 11px sans-serif; fill: #b91c1c; }
    </style>
  </defs>

  <text x="390" y="28" class="h" text-anchor="middle">运行时一次推理的注入流水线（以 Claude Code 为例）</text>
  <text x="390" y="46" class="t-s" text-anchor="middle">上半段全 cached、下半段全 ephemeral，分界是一根硬编码的字符串</text>

  <g filter="url(#wb03p)">
    <!-- left static block -->
    <rect x="40" y="80" width="160" height="40" rx="6" fill="#fef9c3" stroke="#1e293b" stroke-width="1.8" />
    <text x="120" y="105" class="lbl" text-anchor="middle">Identity</text>

    <rect x="40" y="130" width="160" height="40" rx="6" fill="#fef9c3" stroke="#1e293b" stroke-width="1.8" />
    <text x="120" y="155" class="lbl" text-anchor="middle">Tools</text>

    <rect x="40" y="180" width="160" height="40" rx="6" fill="#fef9c3" stroke="#1e293b" stroke-width="1.8" />
    <text x="120" y="205" class="lbl" text-anchor="middle">Skills</text>

    <!-- splitSysPromptPrefix -->
    <rect x="240" y="125" width="180" height="50" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="2" />
    <text x="330" y="148" class="lbl" text-anchor="middle">splitSysPromptPrefix()</text>
    <text x="330" y="166" class="t-s" text-anchor="middle">把三层合并为可缓存前缀</text>

    <line x1="200" y1="100" x2="240" y2="140" stroke="#1e293b" stroke-width="1.8" marker-end="url(#ar03p)" />
    <line x1="200" y1="150" x2="240" y2="150" stroke="#1e293b" stroke-width="1.8" marker-end="url(#ar03p)" />
    <line x1="200" y1="200" x2="240" y2="165" stroke="#1e293b" stroke-width="1.8" marker-end="url(#ar03p)" />

    <!-- BOUNDARY divider -->
    <line x1="430" y1="80" x2="430" y2="320" stroke="#dc2626" stroke-width="3" stroke-dasharray="6 4" />
    <text x="430" y="70" class="cache" text-anchor="middle" fill="#dc2626">SYSTEM_PROMPT_DYNAMIC_BOUNDARY</text>
    <text x="430" y="335" class="t-s" text-anchor="middle">cached ↑   ↓ ephemeral</text>

    <!-- right dynamic block -->
    <rect x="460" y="80" width="160" height="40" rx="6" fill="#fce7f3" stroke="#1e293b" stroke-width="1.8" />
    <text x="540" y="105" class="lbl" text-anchor="middle">Env</text>

    <rect x="460" y="130" width="160" height="40" rx="6" fill="#fce7f3" stroke="#1e293b" stroke-width="1.8" />
    <text x="540" y="155" class="lbl" text-anchor="middle">Cwd</text>

    <rect x="460" y="180" width="160" height="40" rx="6" fill="#fce7f3" stroke="#1e293b" stroke-width="1.8" />
    <text x="540" y="205" class="lbl" text-anchor="middle">Memory</text>

    <!-- appendDynamicContext -->
    <rect x="640" y="125" width="120" height="50" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="2" />
    <text x="700" y="148" class="lbl" text-anchor="middle">appendDynamic</text>
    <text x="700" y="164" class="lbl" text-anchor="middle">Context()</text>

    <line x1="620" y1="100" x2="640" y2="140" stroke="#1e293b" stroke-width="1.8" marker-end="url(#ar03p)" />
    <line x1="620" y1="150" x2="640" y2="150" stroke="#1e293b" stroke-width="1.8" marker-end="url(#ar03p)" />
    <line x1="620" y1="200" x2="640" y2="165" stroke="#1e293b" stroke-width="1.8" marker-end="url(#ar03p)" />

    <!-- final merge to model -->
    <rect x="280" y="260" width="220" height="50" rx="10" fill="#fdf6e3" stroke="#1e293b" stroke-width="2.5" />
    <text x="390" y="282" class="lbl" text-anchor="middle">最终 prompt</text>
    <text x="390" y="299" class="t-s" text-anchor="middle">发送给模型</text>

    <line x1="330" y1="175" x2="380" y2="260" stroke="#1e293b" stroke-width="1.8" marker-end="url(#ar03p)" />
    <line x1="700" y1="175" x2="410" y2="260" stroke="#1e293b" stroke-width="1.8" marker-end="url(#ar03p)" />
  </g>

  <text x="20" y="365" class="t-s">关键点：BOUNDARY 之上整段进 cache，之下每 turn 重算。Codex 没有 boundary（全 cache 或全不 cache），Hermes 用 skip_* 开关近似。</text>
</svg>
"""


def write(slug, svg):
    out = PUBLIC / f"{slug}.svg"
    out.write_text(svg, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    PUBLIC.mkdir(parents=True, exist_ok=True)
    write("03-tradeoff", TRADEOFF_SVG)
    write("03-prompt-pipeline", PIPELINE_SVG)
