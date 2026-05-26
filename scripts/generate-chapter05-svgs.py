#!/usr/bin/env python3
"""Chapter 05 SVGs: TradeOff (严格度 × 可扩展性) + verifier 失败两路径."""
from pathlib import Path

PUBLIC = Path("public/diagrams")

TRADEOFF_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 480" role="img"
     aria-label="四家 Verifier 在严格度 × 可扩展性 两条轴上的位置">
  <defs>
    <filter id="wb05"><feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="17" /><feDisplacementMap in="SourceGraphic" scale="2" /></filter>
    <marker id="ar05" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .ax   { font: 600 12.5px sans-serif; fill: #1e293b; }
      .t    { font: 11.5px sans-serif; fill: #334155; }
      .t-s  { font: 10.5px sans-serif; fill: #64748b; }
      .pin  { font: 700 12.5px sans-serif; fill: #fff; }
      .note { font: italic 10.5px sans-serif; fill: #475569; }
    </style>
  </defs>

  <text x="390" y="26" class="h" text-anchor="middle">Verifier：严格度 × 可扩展性</text>
  <text x="390" y="44" class="t-s" text-anchor="middle">硬 verifier 越多 loop 越被外部信任；可扩展性高就能让第三方挂自己的检查</text>

  <g filter="url(#wb05)">
    <rect x="100" y="80" width="280" height="160" fill="#fef9c3" opacity="0.4" />
    <rect x="380" y="80" width="280" height="160" fill="#dcfce7" opacity="0.4" />
    <rect x="100" y="240" width="280" height="160" fill="#fee2e2" opacity="0.4" />
    <rect x="380" y="240" width="280" height="160" fill="#dbeafe" opacity="0.4" />

    <text x="120" y="100" class="t-s">松 + 可扩展</text>
    <text x="640" y="100" class="t-s" text-anchor="end">严 + 可扩展 · 圣杯</text>
    <text x="120" y="260" class="t-s">松 + 不可扩展（最差）</text>
    <text x="640" y="260" class="t-s" text-anchor="end">严 + 不可扩展</text>

    <line x1="100" y1="400" x2="660" y2="400" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar05)" />
    <line x1="100" y1="400" x2="100" y2="70" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar05)" />
    <line x1="380" y1="80" x2="380" y2="400" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />
    <line x1="100" y1="240" x2="660" y2="240" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />

    <text x="660" y="420" class="ax" text-anchor="end">单 loop verifier 严格度（外部产物 → 放任型）→</text>
    <text x="110" y="68" class="ax">↑ 可扩展性（外部能挂多少 verifier）</text>

    <!-- OpenClaw: top-left -->
    <circle cx="240" cy="120" r="15" fill="#16a34a" stroke="#1e293b" stroke-width="2" />
    <text x="240" y="124" class="pin" text-anchor="middle">OC</text>
    <text x="240" y="153" class="t" text-anchor="middle">OpenClaw</text>
    <text x="240" y="168" class="t-s" text-anchor="middle">中间件 + 4 种 detector</text>
    <text x="240" y="181" class="t-s" text-anchor="middle">可扩展性封顶</text>

    <!-- Codex: bottom-right (highest strictness, low extensibility) -->
    <circle cx="610" cy="320" r="15" fill="#2563eb" stroke="#1e293b" stroke-width="2" />
    <text x="610" y="324" class="pin" text-anchor="middle">CX</text>
    <text x="610" y="352" class="t" text-anchor="middle">Codex</text>
    <text x="610" y="367" class="t-s" text-anchor="middle">硬 verifier 4 件套</text>
    <text x="610" y="380" class="t-s" text-anchor="middle">execpolicy 三态 · 最严</text>

    <!-- Claude Code: middle, lower -->
    <circle cx="430" cy="345" r="15" fill="#7c3aed" stroke="#1e293b" stroke-width="2" />
    <text x="430" y="349" class="pin" text-anchor="middle">CC</text>
    <text x="430" y="377" class="t" text-anchor="middle">Claude Code</text>
    <text x="430" y="392" class="t-s" text-anchor="middle">tokenBudget 0.9/500/3</text>
    <text x="430" y="305" class="t-s" text-anchor="middle">无 hard verifier hook</text>

    <!-- Hermes: bottom-left -->
    <circle cx="220" cy="290" r="15" fill="#f97316" stroke="#1e293b" stroke-width="2" />
    <text x="220" y="294" class="pin" text-anchor="middle">HM</text>
    <text x="220" y="322" class="t" text-anchor="middle">Hermes</text>
    <text x="220" y="337" class="t-s" text-anchor="middle">IterationBudget + grace</text>
    <text x="220" y="350" class="t-s" text-anchor="middle">运行时几乎无硬 verifier</text>

    <text x="540" y="135" class="note" text-anchor="middle">右上角无人</text>
    <text x="540" y="152" class="note" text-anchor="middle">严格 + 高可插互相挤压</text>
  </g>

  <text x="20" y="465" class="t-s">CX = Codex · CC = Claude Code · OC = OpenClaw · HM = Hermes</text>
</svg>
"""

FAILURE_PATHS_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 420" role="img"
     aria-label="Verifier 失败的两种典型路径：硬 verifier 卡住 vs 软 verifier 卡住">
  <defs>
    <filter id="wb05p"><feTurbulence type="fractalNoise" baseFrequency="0.022" numOctaves="2" seed="22" /><feDisplacementMap in="SourceGraphic" scale="1.5" /></filter>
    <marker id="ar05p" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <marker id="ar05p-r" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#dc2626" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .label{ font: 700 13px sans-serif; fill: #1e293b; }
      .lbl  { font: 700 11.5px sans-serif; fill: #1e293b; }
      .t    { font: 11.5px sans-serif; fill: #334155; }
      .t-s  { font: 10.5px sans-serif; fill: #475569; }
      .sig  { font: italic 11px sans-serif; fill: #b91c1c; }
      .sig2 { font: italic 11px sans-serif; fill: #b45309; }
    </style>
  </defs>

  <text x="410" y="26" class="h" text-anchor="middle">Verifier 失败的两种典型路径</text>
  <text x="410" y="44" class="t-s" text-anchor="middle">硬 verifier 卡住 = 任务没完成；软 verifier 卡住 = token 耗尽但任务也没完成</text>

  <!-- Path A label -->
  <text x="30" y="90" class="label">Path A · 硬 verifier 卡住</text>
  <text x="30" y="108" class="t-s">外部判官给 fail 信号</text>

  <g filter="url(#wb05p)">
    <!-- Path A boxes -->
    <rect x="180" y="80" width="100" height="40" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.8" />
    <text x="230" y="105" class="lbl" text-anchor="middle">Turn N</text>

    <rect x="310" y="80" width="120" height="40" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="2" />
    <text x="370" y="98" class="lbl" text-anchor="middle">tests fail</text>
    <text x="370" y="113" class="sig" text-anchor="middle">exit != 0</text>

    <rect x="460" y="80" width="140" height="40" rx="8" fill="#fee2e2" stroke="#dc2626" stroke-width="2" />
    <text x="530" y="98" class="lbl" text-anchor="middle">goal 不收敛</text>
    <text x="530" y="113" class="sig" text-anchor="middle">GoalRuntimeEvent</text>

    <rect x="630" y="80" width="140" height="40" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.8" />
    <text x="700" y="98" class="lbl" text-anchor="middle">强制继续</text>
    <text x="700" y="113" class="t-s" text-anchor="middle">→ Turn N+1</text>

    <line x1="280" y1="100" x2="310" y2="100" stroke="#1e293b" stroke-width="2" marker-end="url(#ar05p)" />
    <line x1="430" y1="100" x2="460" y2="100" stroke="#dc2626" stroke-width="2" marker-end="url(#ar05p-r)" />
    <line x1="600" y1="100" x2="630" y2="100" stroke="#1e293b" stroke-width="2" marker-end="url(#ar05p)" />

    <!-- Divider -->
    <line x1="30" y1="180" x2="790" y2="180" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 3" />
  </g>

  <!-- Path B label -->
  <text x="30" y="220" class="label">Path B · 软 verifier 卡住</text>
  <text x="30" y="238" class="t-s">预算耗尽 + 收敛减速</text>

  <g filter="url(#wb05p)">
    <!-- Path B boxes -->
    <rect x="180" y="210" width="100" height="40" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.8" />
    <text x="230" y="235" class="lbl" text-anchor="middle">Turn N</text>

    <rect x="310" y="210" width="160" height="40" rx="8" fill="#fed7aa" stroke="#b45309" stroke-width="2" />
    <text x="390" y="228" class="lbl" text-anchor="middle">token ≥ 90% 预算</text>
    <text x="390" y="243" class="sig2" text-anchor="middle">COMPLETION_THRESHOLD</text>

    <rect x="500" y="210" width="180" height="40" rx="8" fill="#fed7aa" stroke="#b45309" stroke-width="2" />
    <text x="590" y="228" class="lbl" text-anchor="middle">连续 3 轮 &lt;500 token</text>
    <text x="590" y="243" class="sig2" text-anchor="middle">DIMINISHING_THRESHOLD</text>

    <line x1="280" y1="230" x2="310" y2="230" stroke="#1e293b" stroke-width="2" marker-end="url(#ar05p)" />
    <line x1="470" y1="230" x2="500" y2="230" stroke="#b45309" stroke-width="2" marker-end="url(#ar05p)" />

    <!-- Path B verdict -->
    <rect x="280" y="290" width="320" height="50" rx="10" fill="#fef3c7" stroke="#1e293b" stroke-width="2.2" />
    <text x="440" y="312" class="label" text-anchor="middle">判定 diminishing returns</text>
    <text x="440" y="329" class="t-s" text-anchor="middle">强制停 + 暴露 transition.reason</text>

    <path d="M590,250 Q590,275 440,290" stroke="#b45309" stroke-width="2" fill="none" marker-end="url(#ar05p)" />
  </g>

  <text x="30" y="380" class="t-s">关键洞察：三层 verifier 必须各司其职。把它们坍缩为一个 boolean，监控就分不清「在干活」「在打转」「该停了」。</text>
  <text x="30" y="398" class="t-s">硬 verifier 看外部产物 · 软 verifier 看预算与启发式 · 放任型 verifier 兜底，从来不是主力。</text>
</svg>
"""


def write(slug, svg):
    out = PUBLIC / f"{slug}.svg"
    out.write_text(svg, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    PUBLIC.mkdir(parents=True, exist_ok=True)
    write("05-tradeoff", TRADEOFF_SVG)
    write("05-failure-paths", FAILURE_PATHS_SVG)
