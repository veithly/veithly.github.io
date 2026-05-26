#!/usr/bin/env python3
"""Chapter 08 SVGs: TradeOff (抽象深度 × 模型自由度) + 四家 git 视角差异图."""
from pathlib import Path

PUBLIC = Path("public/diagrams")

TRADEOFF_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 480" role="img"
     aria-label="四家 git workflow 在 抽象深度 × 模型自由度 两条轴上的位置">
  <defs>
    <filter id="wb08"><feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="53" /><feDisplacementMap in="SourceGraphic" scale="2" /></filter>
    <marker id="ar08" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .ax   { font: 600 12.5px sans-serif; fill: #1e293b; }
      .t    { font: 11.5px sans-serif; fill: #334155; }
      .t-s  { font: 10.5px sans-serif; fill: #64748b; }
      .pin  { font: 700 12.5px sans-serif; fill: #fff; }
      .note { font: italic 10.5px sans-serif; fill: #475569; }
    </style>
  </defs>

  <text x="390" y="26" class="h" text-anchor="middle">Git Workflow：抽象深度 × 模型自由度</text>
  <text x="390" y="44" class="t-s" text-anchor="middle">抽象越厚，模型越被框死；架构选型跟着 agent 定位走（coding agent vs 通用控制面）</text>

  <g filter="url(#wb08)">
    <rect x="100" y="80" width="280" height="160" fill="#dcfce7" opacity="0.4" />
    <rect x="380" y="80" width="280" height="160" fill="#fef9c3" opacity="0.4" />
    <rect x="100" y="240" width="280" height="160" fill="#fee2e2" opacity="0.4" />
    <rect x="380" y="240" width="280" height="160" fill="#dbeafe" opacity="0.4" />

    <text x="120" y="100" class="t-s">薄 + 自由 · 控制面区</text>
    <text x="640" y="100" class="t-s" text-anchor="end">厚 + 自由 · 矛盾区</text>
    <text x="120" y="260" class="t-s">薄 + 框死（最差）</text>
    <text x="640" y="260" class="t-s" text-anchor="end">厚 + 框死 · coding agent 区</text>

    <line x1="100" y1="400" x2="660" y2="400" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar08)" />
    <line x1="100" y1="400" x2="100" y2="70" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar08)" />
    <line x1="380" y1="80" x2="380" y2="400" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />
    <line x1="100" y1="240" x2="660" y2="240" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />

    <text x="660" y="420" class="ax" text-anchor="end">git 抽象进 agent 的深度 →</text>
    <text x="110" y="68" class="ax">↑ 模型自由用 git 的灵活度</text>

    <!-- Hermes: top-left (薄 + 自由) -->
    <circle cx="180" cy="130" r="15" fill="#f97316" stroke="#1e293b" stroke-width="2" />
    <text x="180" y="134" class="pin" text-anchor="middle">HM</text>
    <text x="180" y="162" class="t" text-anchor="middle">Hermes</text>
    <text x="180" y="177" class="t-s" text-anchor="middle">banner 一行字</text>
    <text x="180" y="190" class="t-s" text-anchor="middle">git 全交给 shell</text>

    <!-- OpenClaw: top-mid-left (轻抽象 + 自由) -->
    <circle cx="280" cy="175" r="15" fill="#16a34a" stroke="#1e293b" stroke-width="2" />
    <text x="280" y="179" class="pin" text-anchor="middle">OC</text>
    <text x="280" y="207" class="t" text-anchor="middle">OpenClaw</text>
    <text x="280" y="222" class="t-s" text-anchor="middle">git-root + 版本戳</text>
    <text x="280" y="235" class="t-s" text-anchor="middle">控制面定位的克制</text>

    <!-- Claude Code: bottom-right area (厚 + 较框死) -->
    <circle cx="555" cy="305" r="15" fill="#7c3aed" stroke="#1e293b" stroke-width="2" />
    <text x="555" y="309" class="pin" text-anchor="middle">CC</text>
    <text x="555" y="337" class="t" text-anchor="middle">Claude Code</text>
    <text x="555" y="352" class="t-s" text-anchor="middle">gitFilesystem 缓存 · /review</text>
    <text x="555" y="365" class="t-s" text-anchor="middle">gitSafety 双重防御</text>

    <!-- Codex: bottom-right (最厚 + 最框死) -->
    <circle cx="615" cy="370" r="15" fill="#2563eb" stroke="#1e293b" stroke-width="2" />
    <text x="615" y="374" class="pin" text-anchor="middle">CX</text>
    <text x="525" y="395" class="t" text-anchor="middle">Codex (git-utils crate · GitInfo · baseline snapshot)</text>
  </g>

  <text x="20" y="465" class="t-s">CX = Codex · CC = Claude Code · OC = OpenClaw · HM = Hermes</text>
</svg>
"""

LAYERS_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 460" role="img"
     aria-label="同一个仓库，四家把 git 抽象成完全不同形态">
  <defs>
    <filter id="wb08L"><feTurbulence type="fractalNoise" baseFrequency="0.022" numOctaves="2" seed="59" /><feDisplacementMap in="SourceGraphic" scale="1.5" /></filter>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .col  { font: 700 13px sans-serif; fill: #1e293b; }
      .lbl  { font: 700 11px sans-serif; fill: #1e293b; }
      .t-s  { font: 10.5px sans-serif; fill: #475569; }
      .axis { font: 600 12px sans-serif; fill: #1e293b; }
    </style>
  </defs>

  <text x="410" y="24" class="h" text-anchor="middle">同一个仓库，四家眼里"git"是不同的东西</text>
  <text x="410" y="42" class="t-s" text-anchor="middle">从结构化 crate 到一行 subprocess——抽象厚度差一个数量级</text>

  <g filter="url(#wb08L)">
    <text x="105" y="75" class="col" text-anchor="middle">Codex</text>
    <text x="305" y="75" class="col" text-anchor="middle">Claude Code</text>
    <text x="505" y="75" class="col" text-anchor="middle">OpenClaw</text>
    <text x="705" y="75" class="col" text-anchor="middle">Hermes</text>

    <line x1="200" y1="55" x2="200" y2="420" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="3 3" />
    <line x1="400" y1="55" x2="400" y2="420" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="3 3" />
    <line x1="600" y1="55" x2="600" y2="420" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="3 3" />

    <!-- Codex: tall structured stack -->
    <rect x="35" y="90" width="140" height="320" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="1.6" />
    <text x="105" y="110" class="lbl" text-anchor="middle">git-utils crate</text>

    <rect x="50" y="120" width="110" height="30" rx="5" fill="#fff" stroke="#1e293b" stroke-width="1" />
    <text x="105" y="139" class="t-s" text-anchor="middle">GitInfo 三件套</text>

    <rect x="50" y="155" width="110" height="30" rx="5" fill="#fff" stroke="#1e293b" stroke-width="1" />
    <text x="105" y="174" class="t-s" text-anchor="middle">GitSha 强类型</text>

    <rect x="50" y="190" width="110" height="30" rx="5" fill="#fff" stroke="#1e293b" stroke-width="1" />
    <text x="105" y="209" class="t-s" text-anchor="middle">baseline repo 快照</text>

    <rect x="50" y="225" width="110" height="30" rx="5" fill="#fff" stroke="#1e293b" stroke-width="1" />
    <text x="105" y="244" class="t-s" text-anchor="middle">apply_git_patch</text>

    <rect x="50" y="260" width="110" height="30" rx="5" fill="#fff" stroke="#1e293b" stroke-width="1" />
    <text x="105" y="279" class="t-s" text-anchor="middle">git_diff_to_remote</text>

    <rect x="50" y="295" width="110" height="30" rx="5" fill="#fff" stroke="#1e293b" stroke-width="1" />
    <text x="105" y="314" class="t-s" text-anchor="middle">recent_commits</text>

    <rect x="50" y="330" width="110" height="30" rx="5" fill="#fff" stroke="#1e293b" stroke-width="1" />
    <text x="105" y="349" class="t-s" text-anchor="middle">merge_base_with_head</text>

    <rect x="50" y="365" width="110" height="30" rx="5" fill="#fff" stroke="#1e293b" stroke-width="1" />
    <text x="105" y="384" class="t-s" text-anchor="middle">5s timeout · 并行</text>

    <!-- Claude Code: medium stack -->
    <rect x="235" y="90" width="140" height="260" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.6" />
    <text x="305" y="110" class="lbl" text-anchor="middle">IDE 基础设施</text>

    <rect x="250" y="120" width="110" height="30" rx="5" fill="#fff" stroke="#1e293b" stroke-width="1" />
    <text x="305" y="139" class="t-s" text-anchor="middle">findGitRoot LRU 50</text>

    <rect x="250" y="155" width="110" height="30" rx="5" fill="#fff" stroke="#1e293b" stroke-width="1" />
    <text x="305" y="174" class="t-s" text-anchor="middle">gitFilesystem 缓存</text>

    <rect x="250" y="190" width="110" height="30" rx="5" fill="#fff" stroke="#1e293b" stroke-width="1" />
    <text x="305" y="209" class="t-s" text-anchor="middle">gitSafety 双攻击防</text>

    <rect x="250" y="225" width="110" height="30" rx="5" fill="#fff" stroke="#1e293b" stroke-width="1" />
    <text x="305" y="244" class="t-s" text-anchor="middle">/review prompt</text>

    <rect x="250" y="260" width="110" height="30" rx="5" fill="#fff" stroke="#1e293b" stroke-width="1" />
    <text x="305" y="279" class="t-s" text-anchor="middle">/pr_comments 流程</text>

    <rect x="250" y="295" width="110" height="30" rx="5" fill="#fff" stroke="#1e293b" stroke-width="1" />
    <text x="305" y="314" class="t-s" text-anchor="middle">gh CLI 集成</text>

    <rect x="250" y="330" width="110" height="20" rx="5" fill="#fff" stroke="#1e293b" stroke-width="1" />
    <text x="305" y="344" class="t-s" text-anchor="middle">/ultrareview 远程</text>

    <!-- OpenClaw: tiny stack -->
    <rect x="435" y="90" width="140" height="120" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="1.6" />
    <text x="505" y="110" class="lbl" text-anchor="middle">最小集</text>

    <rect x="450" y="120" width="110" height="30" rx="5" fill="#fff" stroke="#1e293b" stroke-width="1" />
    <text x="505" y="139" class="t-s" text-anchor="middle">findGitRoot walk-up</text>

    <rect x="450" y="155" width="110" height="30" rx="5" fill="#fff" stroke="#1e293b" stroke-width="1" />
    <text x="505" y="174" class="t-s" text-anchor="middle">读 .git/HEAD 拿 SHA</text>

    <rect x="450" y="190" width="110" height="15" rx="5" fill="#fff" stroke="#1e293b" stroke-width="1" />
    <text x="505" y="201" class="t-s" text-anchor="middle">不走 git binary</text>

    <text x="505" y="245" class="t-s" text-anchor="middle">git 操作走 shell + tool-policy</text>
    <text x="505" y="262" class="t-s" text-anchor="middle">不进模型的 system context</text>

    <!-- Hermes: micro stack -->
    <rect x="635" y="90" width="140" height="80" rx="8" fill="#fed7aa" stroke="#f97316" stroke-width="1.6" />
    <text x="705" y="110" class="lbl" text-anchor="middle">banner 一行</text>

    <rect x="650" y="120" width="110" height="40" rx="5" fill="#fff" stroke="#1e293b" stroke-width="1" />
    <text x="705" y="137" class="t-s" text-anchor="middle">upstream · local</text>
    <text x="705" y="151" class="t-s" text-anchor="middle">+N carried commits</text>

    <text x="705" y="205" class="t-s" text-anchor="middle">25 行 banner.py</text>
    <text x="705" y="222" class="t-s" text-anchor="middle">git 全靠 terminal_tool</text>
  </g>

  <line x1="50" y1="440" x2="770" y2="440" stroke="#1e293b" stroke-width="2" />
  <text x="105" y="455" class="axis" text-anchor="middle">最厚</text>
  <text x="705" y="455" class="axis" text-anchor="middle">最薄</text>
</svg>
"""

def write(slug, svg):
    out = PUBLIC / f"{slug}.svg"
    out.write_text(svg, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size} bytes)")

if __name__ == "__main__":
    PUBLIC.mkdir(parents=True, exist_ok=True)
    write("08-tradeoff", TRADEOFF_SVG)
    write("08-layers", LAYERS_SVG)
