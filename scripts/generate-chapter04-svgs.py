#!/usr/bin/env python3
"""Chapter 04 SVGs: TradeOff (协议直白度 × 中间件能力) + tool round-trip pipeline."""
from pathlib import Path

PUBLIC = Path("public/diagrams")

TRADEOFF_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 480" role="img"
     aria-label="四家 Tool System 在协议直白度 × 中间件能力 两条轴上的位置">
  <defs>
    <filter id="wb04"><feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="11" /><feDisplacementMap in="SourceGraphic" scale="2" /></filter>
    <marker id="ar04" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .ax   { font: 600 12.5px sans-serif; fill: #1e293b; }
      .t    { font: 11.5px sans-serif; fill: #334155; }
      .t-s  { font: 10.5px sans-serif; fill: #64748b; }
      .pin  { font: 700 12.5px sans-serif; fill: #fff; }
      .note { font: italic 10.5px sans-serif; fill: #475569; }
    </style>
  </defs>

  <text x="390" y="26" class="h" text-anchor="middle">Tool System：协议直白度 × 中间件能力</text>
  <text x="390" y="44" class="t-s" text-anchor="middle">协议越贴近官方就越直白，但中间件能力天花板就越低；OpenClaw 反其道而行</text>

  <g filter="url(#wb04)">
    <rect x="100" y="80" width="280" height="160" fill="#dbeafe" opacity="0.4" />
    <rect x="380" y="80" width="280" height="160" fill="#fef9c3" opacity="0.4" />
    <rect x="100" y="240" width="280" height="160" fill="#fee2e2" opacity="0.4" />
    <rect x="380" y="240" width="280" height="160" fill="#dcfce7" opacity="0.4" />

    <text x="120" y="100" class="t-s">抽象厚 + 中间件强</text>
    <text x="640" y="100" class="t-s" text-anchor="end">直白 + 中间件强 · 圣杯</text>
    <text x="120" y="260" class="t-s">抽象厚 + 钩子少（最差）</text>
    <text x="640" y="260" class="t-s" text-anchor="end">直白 + 钩子少</text>

    <line x1="100" y1="400" x2="660" y2="400" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar04)" />
    <line x1="100" y1="400" x2="100" y2="70" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar04)" />
    <line x1="380" y1="80" x2="380" y2="400" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />
    <line x1="100" y1="240" x2="660" y2="240" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />

    <text x="660" y="420" class="ax" text-anchor="end">协议直白度（越右越贴近一种官方 API）→</text>
    <text x="110" y="68" class="ax">↑ 中间件能力（before/after_tool_call 钩子层数）</text>

    <!-- OpenClaw: top-left -->
    <circle cx="240" cy="120" r="15" fill="#16a34a" stroke="#1e293b" stroke-width="2" />
    <text x="240" y="124" class="pin" text-anchor="middle">OC</text>
    <text x="240" y="153" class="t" text-anchor="middle">OpenClaw</text>
    <text x="240" y="168" class="t-s" text-anchor="middle">tool-policy-pipeline</text>
    <text x="240" y="181" class="t-s" text-anchor="middle">5-6 层中间件 · 抽象最厚</text>

    <!-- Claude Code: middle, slight upper right -->
    <circle cx="430" cy="180" r="15" fill="#7c3aed" stroke="#1e293b" stroke-width="2" />
    <text x="430" y="184" class="pin" text-anchor="middle">CC</text>
    <text x="430" y="212" class="t" text-anchor="middle">Claude Code</text>
    <text x="430" y="227" class="t-s" text-anchor="middle">tool_use 并行 + canUseTool</text>
    <text x="430" y="240" class="t-s" text-anchor="middle">协议直白、钩子点有限</text>

    <!-- Hermes: middle, slightly to right -->
    <circle cx="490" cy="240" r="15" fill="#f97316" stroke="#1e293b" stroke-width="2" />
    <text x="490" y="244" class="pin" text-anchor="middle">HM</text>
    <text x="490" y="272" class="t" text-anchor="middle">Hermes</text>
    <text x="490" y="287" class="t-s" text-anchor="middle">registry → adapter 三协议</text>
    <text x="490" y="300" class="t-s" text-anchor="middle">skills_guard · 权限分散</text>

    <!-- Codex: bottom-right -->
    <circle cx="590" cy="320" r="15" fill="#2563eb" stroke="#1e293b" stroke-width="2" />
    <text x="590" y="324" class="pin" text-anchor="middle">CX</text>
    <text x="590" y="352" class="t" text-anchor="middle">Codex</text>
    <text x="590" y="367" class="t-s" text-anchor="middle">Responses + apply_patch DSL</text>
    <text x="590" y="380" class="t-s" text-anchor="middle">execpolicy 三维 · 钩子止于此</text>

    <text x="540" y="125" class="note" text-anchor="middle">右上角空白</text>
    <text x="540" y="142" class="note" text-anchor="middle">直白和钩子层数互相挤压</text>
  </g>

  <text x="20" y="465" class="t-s">CX = Codex · CC = Claude Code · OC = OpenClaw · HM = Hermes</text>
</svg>
"""

PIPELINE_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 420" role="img"
     aria-label="Tool 调用一次完整往返：model → before → execute → after → tool_result">
  <defs>
    <filter id="wb04p"><feTurbulence type="fractalNoise" baseFrequency="0.022" numOctaves="2" seed="13" /><feDisplacementMap in="SourceGraphic" scale="1.5" /></filter>
    <marker id="ar04p" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <marker id="ar04p-r" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#dc2626" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .lbl  { font: 700 12.5px sans-serif; fill: #1e293b; }
      .t    { font: 11.5px sans-serif; fill: #334155; }
      .t-s  { font: 10.5px sans-serif; fill: #475569; }
      .hook { font: italic 10.5px sans-serif; fill: #b45309; }
      .deny { font: italic 10.5px sans-serif; fill: #b91c1c; }
    </style>
  </defs>

  <text x="410" y="26" class="h" text-anchor="middle">工具调用一次完整往返（OpenClaw 风格 4 个钩子点为例）</text>
  <text x="410" y="44" class="t-s" text-anchor="middle">每一层都有机会拦截、改写、记录；deny 走红色短路通道</text>

  <g filter="url(#wb04p)">
    <!-- model node -->
    <rect x="40" y="80" width="140" height="60" rx="10" fill="#fef9c3" stroke="#1e293b" stroke-width="2" />
    <text x="110" y="105" class="lbl" text-anchor="middle">model</text>
    <text x="110" y="123" class="t-s" text-anchor="middle">发起 tool_use(args)</text>

    <line x1="180" y1="110" x2="225" y2="110" stroke="#1e293b" stroke-width="2" marker-end="url(#ar04p)" />

    <!-- before_tool_call -->
    <rect x="225" y="80" width="170" height="60" rx="10" fill="#bfdbfe" stroke="#1e293b" stroke-width="2" />
    <text x="310" y="103" class="lbl" text-anchor="middle">before_tool_call</text>
    <text x="310" y="121" class="t-s" text-anchor="middle">权限 · 改写 · 拦截</text>
    <text x="310" y="64" class="hook" text-anchor="middle">钩子点 #1</text>

    <line x1="395" y1="110" x2="440" y2="110" stroke="#1e293b" stroke-width="2" marker-end="url(#ar04p)" />

    <!-- execute -->
    <rect x="440" y="80" width="160" height="60" rx="10" fill="#dcfce7" stroke="#1e293b" stroke-width="2" />
    <text x="520" y="103" class="lbl" text-anchor="middle">execute</text>
    <text x="520" y="121" class="t-s" text-anchor="middle">sandbox · exec policy</text>
    <text x="520" y="64" class="hook" text-anchor="middle">钩子点 #2</text>

    <line x1="600" y1="110" x2="645" y2="110" stroke="#1e293b" stroke-width="2" marker-end="url(#ar04p)" />

    <!-- after_tool_call -->
    <rect x="645" y="80" width="160" height="60" rx="10" fill="#fed7aa" stroke="#1e293b" stroke-width="2" />
    <text x="725" y="103" class="lbl" text-anchor="middle">after_tool_call</text>
    <text x="725" y="121" class="t-s" text-anchor="middle">log · mutate · persist</text>
    <text x="725" y="64" class="hook" text-anchor="middle">钩子点 #3</text>

    <!-- return path -->
    <path d="M725,140 Q725,225 410,225 Q110,225 110,150" stroke="#1e293b" stroke-width="2" fill="none" marker-end="url(#ar04p)" />
    <text x="410" y="218" class="t-s" text-anchor="middle">tool_result → 下一轮 message</text>

    <!-- deny short circuit -->
    <path d="M310,140 Q310,300 110,300 Q110,250 110,150" stroke="#dc2626" stroke-width="2" stroke-dasharray="6 4" fill="none" marker-end="url(#ar04p-r)" />
    <text x="220" y="295" class="deny">deny → 把 deny tool_result 喂回 model</text>

    <!-- middleware annotation -->
    <rect x="225" y="335" width="580" height="55" rx="8" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="4 3" />
    <text x="515" y="355" class="t" text-anchor="middle">OpenClaw 的 tool-policy-pipeline = before / after / persist / mutation 链</text>
    <text x="515" y="372" class="t-s" text-anchor="middle">Codex 走 execpolicy 静态规则；Claude Code 给 canUseTool 一个钩子；Hermes 在工具函数内部分散判断</text>
  </g>

  <text x="20" y="408" class="t-s">钩子点 #4（tool_result_persist）在 OpenClaw 里负责长期事件流；其他三家用 trajectory / event stream 等价物</text>
</svg>
"""


def write(slug, svg):
    out = PUBLIC / f"{slug}.svg"
    out.write_text(svg, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    PUBLIC.mkdir(parents=True, exist_ok=True)
    write("04-tradeoff", TRADEOFF_SVG)
    write("04-tool-pipeline", PIPELINE_SVG)
