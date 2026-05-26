#!/usr/bin/env python3
"""Chapter 06 SVGs: TradeOff (一轮规模 × 可审计/回滚) + V4A vs str_replace 两路对照."""
from pathlib import Path

PUBLIC = Path("public/diagrams")

TRADEOFF_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 480" role="img"
     aria-label="四家文件编辑系统在 一轮可改规模 × 可审计/可回滚 两条轴上的位置">
  <defs>
    <filter id="wb06"><feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="29" /><feDisplacementMap in="SourceGraphic" scale="2" /></filter>
    <marker id="ar06" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .ax   { font: 600 12.5px sans-serif; fill: #1e293b; }
      .t    { font: 11.5px sans-serif; fill: #334155; }
      .t-s  { font: 10.5px sans-serif; fill: #64748b; }
      .pin  { font: 700 12.5px sans-serif; fill: #fff; }
      .note { font: italic 10.5px sans-serif; fill: #475569; }
    </style>
  </defs>

  <text x="390" y="26" class="h" text-anchor="middle">文件编辑：一轮规模 × 可审计/可回滚</text>
  <text x="390" y="44" class="t-s" text-anchor="middle">V4A 一次性多文件、str_replace 单点最小；两条路在两条轴上分得很开</text>

  <g filter="url(#wb06)">
    <rect x="100" y="80" width="280" height="160" fill="#fef9c3" opacity="0.4" />
    <rect x="380" y="80" width="280" height="160" fill="#dcfce7" opacity="0.4" />
    <rect x="100" y="240" width="280" height="160" fill="#fee2e2" opacity="0.4" />
    <rect x="380" y="240" width="280" height="160" fill="#dbeafe" opacity="0.4" />

    <text x="120" y="100" class="t-s">小 + 易审 · str_replace 区</text>
    <text x="640" y="100" class="t-s" text-anchor="end">大 + 易审 · 圣杯</text>
    <text x="120" y="260" class="t-s">小 + 难审（最差）</text>
    <text x="640" y="260" class="t-s" text-anchor="end">大 + 难审</text>

    <line x1="100" y1="400" x2="660" y2="400" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar06)" />
    <line x1="100" y1="400" x2="100" y2="70" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar06)" />
    <line x1="380" y1="80" x2="380" y2="400" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />
    <line x1="100" y1="240" x2="660" y2="240" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />

    <text x="660" y="420" class="ax" text-anchor="end">单轮可改的规模（行数 / 文件数）→</text>
    <text x="110" y="68" class="ax">↑ 可审计 / 可回滚（reviewer 体验）</text>

    <!-- Claude Code: left top (small + auditable) -->
    <circle cx="235" cy="115" r="15" fill="#7c3aed" stroke="#1e293b" stroke-width="2" />
    <text x="235" y="119" class="pin" text-anchor="middle">CC</text>
    <text x="235" y="148" class="t" text-anchor="middle">Claude Code</text>
    <text x="235" y="163" class="t-s" text-anchor="middle">str_replace 单点</text>
    <text x="235" y="176" class="t-s" text-anchor="middle">unique + mtime · 每步可审</text>

    <!-- Codex: right top (big + auditable) -->
    <circle cx="595" cy="125" r="15" fill="#2563eb" stroke="#1e293b" stroke-width="2" />
    <text x="595" y="129" class="pin" text-anchor="middle">CX</text>
    <text x="595" y="158" class="t" text-anchor="middle">Codex (V4A)</text>
    <text x="595" y="173" class="t-s" text-anchor="middle">inline DSL · rollout 落盘</text>
    <text x="595" y="186" class="t-s" text-anchor="middle">原子多文件 · 易回滚</text>

    <!-- Hermes: right, slightly lower (V4A but function arg) -->
    <circle cx="555" cy="195" r="15" fill="#f97316" stroke="#1e293b" stroke-width="2" />
    <text x="555" y="199" class="pin" text-anchor="middle">HM</text>
    <text x="555" y="227" class="t" text-anchor="middle">Hermes (V4A)</text>
    <text x="555" y="242" class="t-s" text-anchor="middle">V4A 当 function arg</text>
    <text x="555" y="255" class="t-s" text-anchor="middle">受 token 上限</text>

    <!-- OpenClaw: middle, lower (medium + low audit) -->
    <circle cx="400" cy="310" r="15" fill="#16a34a" stroke="#1e293b" stroke-width="2" />
    <text x="400" y="314" class="pin" text-anchor="middle">OC</text>
    <text x="400" y="342" class="t" text-anchor="middle">OpenClaw (fs)</text>
    <text x="400" y="357" class="t-s" text-anchor="middle">通用工具栈 · 无 DSL</text>
    <text x="400" y="370" class="t-s" text-anchor="middle">无多文件原子语义</text>

    <text x="540" y="290" class="note" text-anchor="middle">V4A 路线集中右上</text>
    <text x="240" y="290" class="note" text-anchor="middle">str_replace 路线集中左上</text>
  </g>

  <text x="20" y="465" class="t-s">CX = Codex · CC = Claude Code · OC = OpenClaw · HM = Hermes</text>
</svg>
"""

ROADS_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 480" role="img"
     aria-label="V4A 内嵌 DSL vs str_replace 调用：两条路线的取舍">
  <defs>
    <filter id="wb06p"><feTurbulence type="fractalNoise" baseFrequency="0.022" numOctaves="2" seed="33" /><feDisplacementMap in="SourceGraphic" scale="1.5" /></filter>
    <marker id="ar06p" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .lane { font: 700 13px sans-serif; fill: #1e293b; }
      .lbl  { font: 700 11.5px sans-serif; fill: #1e293b; }
      .t    { font: 11.5px sans-serif; fill: #334155; }
      .t-s  { font: 10.5px sans-serif; fill: #475569; }
      .gate { font: italic 11px sans-serif; fill: #b91c1c; }
    </style>
  </defs>

  <text x="410" y="26" class="h" text-anchor="middle">两条路线的取舍</text>
  <text x="410" y="44" class="t-s" text-anchor="middle">两边都不让模型「盲改」——一边靠 parser 当门神，一边靠唯一匹配 + mtime 当门神</text>

  <!-- Lane A: V4A -->
  <text x="30" y="90" class="lane">Codex / Hermes · V4A 内嵌 DSL</text>

  <g filter="url(#wb06p)">
    <rect x="30" y="100" width="180" height="80" rx="10" fill="#fef9c3" stroke="#1e293b" stroke-width="1.8" />
    <text x="120" y="125" class="lbl" text-anchor="middle">模型一次输出</text>
    <text x="120" y="143" class="t-s" text-anchor="middle">*** Begin Patch</text>
    <text x="120" y="156" class="t-s" text-anchor="middle">Update / Add / Delete</text>
    <text x="120" y="169" class="t-s" text-anchor="middle">*** End Patch</text>

    <line x1="210" y1="140" x2="250" y2="140" stroke="#1e293b" stroke-width="2" marker-end="url(#ar06p)" />

    <rect x="250" y="100" width="180" height="80" rx="10" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.8" />
    <text x="340" y="125" class="lbl" text-anchor="middle">parser 一次校验</text>
    <text x="340" y="143" class="t-s" text-anchor="middle">Lark grammar · 5 markers</text>
    <text x="340" y="156" class="gate" text-anchor="middle">任一失败 → 整段 reject</text>
    <text x="340" y="170" class="t-s" text-anchor="middle">seek_sequence 找锚点</text>

    <line x1="430" y1="140" x2="470" y2="140" stroke="#1e293b" stroke-width="2" marker-end="url(#ar06p)" />

    <rect x="470" y="100" width="180" height="80" rx="10" fill="#dcfce7" stroke="#1e293b" stroke-width="1.8" />
    <text x="560" y="125" class="lbl" text-anchor="middle">磁盘一次落盘</text>
    <text x="560" y="143" class="t-s" text-anchor="middle">Update 3 files</text>
    <text x="560" y="156" class="t-s" text-anchor="middle">Add 1 file</text>
    <text x="560" y="170" class="t-s" text-anchor="middle">全部 atomic</text>

    <line x1="650" y1="140" x2="685" y2="140" stroke="#1e293b" stroke-width="2" marker-end="url(#ar06p)" />
    <rect x="685" y="115" width="115" height="50" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.8" />
    <text x="742" y="135" class="lbl" text-anchor="middle">rollout 存档</text>
    <text x="742" y="152" class="t-s" text-anchor="middle">可 replay</text>
  </g>

  <line x1="30" y1="220" x2="800" y2="220" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 3" />

  <!-- Lane B: str_replace -->
  <text x="30" y="250" class="lane">Claude Code · str_replace 拆原子</text>

  <g filter="url(#wb06p)">
    <rect x="30" y="260" width="180" height="80" rx="10" fill="#fef9c3" stroke="#1e293b" stroke-width="1.8" />
    <text x="120" y="285" class="lbl" text-anchor="middle">tool_use #1</text>
    <text x="120" y="303" class="t-s" text-anchor="middle">old_string A</text>
    <text x="120" y="316" class="t-s" text-anchor="middle">new_string B</text>
    <text x="120" y="330" class="t-s" text-anchor="middle">replace_all? bool</text>

    <line x1="210" y1="300" x2="250" y2="300" stroke="#1e293b" stroke-width="2" marker-end="url(#ar06p)" />

    <rect x="250" y="260" width="180" height="80" rx="10" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.8" />
    <text x="340" y="285" class="lbl" text-anchor="middle">工具校验</text>
    <text x="340" y="303" class="t-s" text-anchor="middle">unique match</text>
    <text x="340" y="316" class="t-s" text-anchor="middle">mtime 未变</text>
    <text x="340" y="330" class="gate" text-anchor="middle">FILE_UNEXPECTEDLY_MODIFIED</text>

    <line x1="430" y1="300" x2="470" y2="300" stroke="#1e293b" stroke-width="2" marker-end="url(#ar06p)" />

    <rect x="470" y="260" width="180" height="80" rx="10" fill="#dcfce7" stroke="#1e293b" stroke-width="1.8" />
    <text x="560" y="285" class="lbl" text-anchor="middle">落盘 + 副作用</text>
    <text x="560" y="303" class="t-s" text-anchor="middle">LSP diagnostics 失效</text>
    <text x="560" y="316" class="t-s" text-anchor="middle">fileHistory 追踪</text>
    <text x="560" y="330" class="t-s" text-anchor="middle">VS Code SDK 通知</text>

    <line x1="650" y1="300" x2="685" y2="300" stroke="#1e293b" stroke-width="2" marker-end="url(#ar06p)" />
    <rect x="685" y="275" width="115" height="50" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.8" />
    <text x="742" y="295" class="lbl" text-anchor="middle">tool_use #2</text>
    <text x="742" y="312" class="t-s" text-anchor="middle">重复 N 次</text>
  </g>

  <text x="30" y="400" class="t-s">关键差别：V4A 让模型一次说完所有改动，DSL parser 是门神；str_replace 让模型每次只改一处，唯一匹配 + mtime 是门神。</text>
  <text x="30" y="420" class="t-s">V4A 适合大 patch + 多文件原子；str_replace 适合 reviewer 体验 + LSP 同步。OpenClaw 走通用 fs 工具，Hermes 复用 V4A 但当 function arg。</text>
  <text x="30" y="450" class="t-s">不要让模型用 bash 的 sed / awk 直改文件——没有 diff 反馈，错了找不到。</text>
</svg>
"""


def write(slug, svg):
    out = PUBLIC / f"{slug}.svg"
    out.write_text(svg, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    PUBLIC.mkdir(parents=True, exist_ok=True)
    write("06-tradeoff", TRADEOFF_SVG)
    write("06-edit-roads", ROADS_SVG)
