#!/usr/bin/env python3
"""Chapter 09 SVGs: TradeOff (reviewer 隔离度 × 上手成本) + 四种 review 模型对照流程图."""
from pathlib import Path

PUBLIC = Path("public/diagrams")

TRADEOFF_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 480" role="img"
     aria-label="四家 code review 在 reviewer 隔离度 × 上手成本 两条轴上的位置">
  <defs>
    <filter id="wb09"><feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="61" /><feDisplacementMap in="SourceGraphic" scale="2" /></filter>
    <marker id="ar09" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .ax   { font: 600 12.5px sans-serif; fill: #1e293b; }
      .t    { font: 11.5px sans-serif; fill: #334155; }
      .t-s  { font: 10.5px sans-serif; fill: #64748b; }
      .pin  { font: 700 12.5px sans-serif; fill: #fff; }
      .note { font: italic 10.5px sans-serif; fill: #475569; }
    </style>
  </defs>

  <text x="390" y="26" class="h" text-anchor="middle">Code Review：reviewer 隔离度 × 上手成本</text>
  <text x="390" y="44" class="t-s" text-anchor="middle">隔离度越高，reviewer 越像独立 agent；但上手 / 配置成本就越高</text>

  <g filter="url(#wb09)">
    <rect x="100" y="80" width="280" height="160" fill="#fef9c3" opacity="0.4" />
    <rect x="380" y="80" width="280" height="160" fill="#dcfce7" opacity="0.4" />
    <rect x="100" y="240" width="280" height="160" fill="#dbeafe" opacity="0.4" />
    <rect x="380" y="240" width="280" height="160" fill="#fee2e2" opacity="0.4" />

    <text x="120" y="100" class="t-s">轻量 · 同对话塞 prompt</text>
    <text x="640" y="100" class="t-s" text-anchor="end">轻量 · 独立 agent（圣杯）</text>
    <text x="120" y="260" class="t-s">重 · 同对话（最不值）</text>
    <text x="640" y="260" class="t-s" text-anchor="end">重 · 独立 agent · 工程上限</text>

    <line x1="100" y1="400" x2="660" y2="400" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar09)" />
    <line x1="100" y1="400" x2="100" y2="70" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar09)" />
    <line x1="380" y1="80" x2="380" y2="400" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />
    <line x1="100" y1="240" x2="660" y2="240" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />

    <text x="660" y="420" class="ax" text-anchor="end">reviewer 跟主 agent 的隔离深度 →</text>
    <text x="110" y="68" class="ax">↑ 用户 / 开发者上手成本（越低越好）</text>

    <!-- Hermes: top-left (无隔离 + 极轻) -->
    <circle cx="155" cy="120" r="14" fill="#f97316" stroke="#1e293b" stroke-width="2" />
    <text x="155" y="124" class="pin" text-anchor="middle">HM</text>
    <text x="155" y="151" class="t" text-anchor="middle">Hermes</text>
    <text x="155" y="166" class="t-s" text-anchor="middle">terminal-only</text>
    <text x="155" y="179" class="t-s" text-anchor="middle">零基础设施</text>

    <!-- Claude Code /review local -->
    <circle cx="245" cy="135" r="14" fill="#7c3aed" stroke="#1e293b" stroke-width="2" />
    <text x="245" y="139" class="pin" text-anchor="middle">CC</text>
    <text x="245" y="166" class="t" text-anchor="middle">CC /review (local)</text>
    <text x="245" y="181" class="t-s" text-anchor="middle">一段内嵌 prompt</text>
    <text x="245" y="194" class="t-s" text-anchor="middle">同对话塞回主 agent</text>

    <!-- OpenClaw plugin (middle, somewhat isolated) -->
    <circle cx="425" cy="265" r="14" fill="#16a34a" stroke="#1e293b" stroke-width="2" />
    <text x="425" y="269" class="pin" text-anchor="middle">OC</text>
    <text x="425" y="296" class="t" text-anchor="middle">OpenClaw plugin</text>
    <text x="425" y="311" class="t-s" text-anchor="middle">tool-policy after hook</text>
    <text x="425" y="324" class="t-s" text-anchor="middle">中等隔离 · 中等成本</text>

    <!-- Codex sub-agent (right, high isolation, medium ease) -->
    <circle cx="585" cy="195" r="14" fill="#2563eb" stroke="#1e293b" stroke-width="2" />
    <text x="585" y="199" class="pin" text-anchor="middle">CX</text>
    <text x="585" y="226" class="t" text-anchor="middle">Codex sub-agent</text>
    <text x="585" y="241" class="t-s" text-anchor="middle">受约束 config · 4 种 target</text>
    <text x="585" y="254" class="t-s" text-anchor="middle">+ guardian 双层</text>

    <!-- Claude Code /ultrareview (far right + lower) -->
    <circle cx="620" cy="320" r="14" fill="#a855f7" stroke="#1e293b" stroke-width="2" />
    <text x="620" y="324" class="pin" text-anchor="middle">UR</text>
    <text x="620" y="351" class="t" text-anchor="middle">CC /ultrareview</text>
    <text x="620" y="366" class="t-s" text-anchor="middle">远程 CCR session</text>
    <text x="620" y="379" class="t-s" text-anchor="middle">10-20 分钟 pipeline</text>
  </g>

  <text x="20" y="465" class="t-s">CX = Codex · CC = Claude Code · OC = OpenClaw · HM = Hermes · UR = Ultrareview</text>
</svg>
"""

FLOWS_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 660" role="img"
     aria-label="四种 review 模型并列流程图">
  <defs>
    <filter id="wb09F"><feTurbulence type="fractalNoise" baseFrequency="0.022" numOctaves="2" seed="71" /><feDisplacementMap in="SourceGraphic" scale="1.5" /></filter>
    <marker id="ar09F" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .col  { font: 700 13px sans-serif; fill: #1e293b; }
      .lbl  { font: 700 11px sans-serif; fill: #1e293b; }
      .t-s  { font: 10.5px sans-serif; fill: #475569; }
      .note { font: italic 10.5px sans-serif; fill: #b45309; }
    </style>
  </defs>

  <text x="430" y="24" class="h" text-anchor="middle">四种 code review 流程并列</text>
  <text x="430" y="42" class="t-s" text-anchor="middle">从「同对话塞 prompt」到「独立 sub-agent」到「远程 pipeline」到「pipeline hook」</text>

  <g filter="url(#wb09F)">
    <!-- Codex column -->
    <text x="120" y="70" class="col" text-anchor="middle">Codex · 双层 sub-agent</text>
    <rect x="40" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="103" class="lbl" text-anchor="middle">user /review</text>

    <line x1="120" y1="116" x2="120" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar09F)" />

    <rect x="40" y="138" width="160" height="60" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="158" class="lbl" text-anchor="middle">fork sub-agent</text>
    <text x="120" y="174" class="t-s" text-anchor="middle">web_search=off · Spawn=off</text>
    <text x="120" y="189" class="t-s" text-anchor="middle">approval=Never</text>

    <line x1="120" y1="198" x2="120" y2="217" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar09F)" />

    <rect x="40" y="220" width="160" height="48" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="240" class="lbl" text-anchor="middle">跑 REVIEW_PROMPT</text>
    <text x="120" y="256" class="t-s" text-anchor="middle">4 种 target 模板</text>

    <line x1="120" y1="268" x2="120" y2="287" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar09F)" />

    <rect x="40" y="290" width="160" height="36" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="313" class="lbl" text-anchor="middle">parse_review_output</text>

    <line x1="120" y1="326" x2="120" y2="345" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar09F)" />

    <rect x="40" y="348" width="160" height="36" rx="8" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="371" class="lbl" text-anchor="middle">主 agent 继续</text>

    <!-- Guardian flow (Codex's second review system) -->
    <rect x="40" y="420" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="443" class="lbl" text-anchor="middle">主 agent tool_call</text>

    <line x1="120" y1="456" x2="120" y2="475" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar09F)" />

    <rect x="40" y="478" width="160" height="48" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="498" class="lbl" text-anchor="middle">guardian reviewer</text>
    <text x="120" y="514" class="t-s" text-anchor="middle">risk + 5s timeout</text>

    <line x1="120" y1="526" x2="120" y2="545" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar09F)" />

    <rect x="40" y="548" width="160" height="36" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="571" class="lbl" text-anchor="middle">allow / deny / timeout</text>

    <text x="120" y="610" class="note" text-anchor="middle">两套 reviewer agent</text>
    <text x="120" y="625" class="note" text-anchor="middle">一审代码 · 一审审批</text>

    <!-- Claude Code /review local column -->
    <text x="330" y="70" class="col" text-anchor="middle">Claude Code · 本地 prompt</text>
    <rect x="250" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="103" class="lbl" text-anchor="middle">user /review #123</text>

    <line x1="330" y1="116" x2="330" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar09F)" />

    <rect x="250" y="138" width="160" height="48" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="158" class="lbl" text-anchor="middle">LOCAL_REVIEW_PROMPT</text>
    <text x="330" y="174" class="t-s" text-anchor="middle">塞回主 agent context</text>

    <line x1="330" y1="186" x2="330" y2="205" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar09F)" />

    <rect x="250" y="208" width="160" height="60" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="228" class="lbl" text-anchor="middle">主 agent 跑 gh</text>
    <text x="330" y="244" class="t-s" text-anchor="middle">gh pr view → gh pr diff</text>
    <text x="330" y="258" class="t-s" text-anchor="middle">→ 分析 + 5 个 section</text>

    <line x1="330" y1="268" x2="330" y2="287" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar09F)" />

    <rect x="250" y="290" width="160" height="36" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="313" class="lbl" text-anchor="middle">markdown findings</text>

    <text x="330" y="360" class="note" text-anchor="middle">无独立 reviewer agent</text>
    <text x="330" y="375" class="note" text-anchor="middle">同对话切角色</text>

    <!-- Claude Code /ultrareview remote column -->
    <text x="540" y="70" class="col" text-anchor="middle">CC · /ultrareview 远程</text>
    <rect x="460" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="103" class="lbl" text-anchor="middle">user /ultrareview</text>

    <line x1="540" y1="116" x2="540" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar09F)" />

    <rect x="460" y="138" width="160" height="36" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="161" class="lbl" text-anchor="middle">quota / billing gate</text>

    <line x1="540" y1="174" x2="540" y2="193" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar09F)" />

    <rect x="460" y="196" width="160" height="48" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="216" class="lbl" text-anchor="middle">teleport → CCR Web</text>
    <text x="540" y="232" class="t-s" text-anchor="middle">GitHub app 拉代码</text>

    <line x1="540" y1="244" x2="540" y2="263" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar09F)" />

    <rect x="460" y="266" width="160" height="60" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="286" class="lbl" text-anchor="middle">bug-hunter pipeline</text>
    <text x="540" y="302" class="t-s" text-anchor="middle">10-20 分钟</text>
    <text x="540" y="316" class="t-s" text-anchor="middle">sandbox + quota</text>

    <line x1="540" y1="326" x2="540" y2="345" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar09F)" />

    <rect x="460" y="348" width="160" height="36" rx="8" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="371" class="lbl" text-anchor="middle">task-notification 回写</text>

    <text x="540" y="410" class="note" text-anchor="middle">独立远程 session</text>
    <text x="540" y="425" class="note" text-anchor="middle">深度最高 · 成本最高</text>

    <!-- OpenClaw / Hermes column -->
    <text x="750" y="70" class="col" text-anchor="middle">OpenClaw / Hermes</text>
    <rect x="670" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="750" y="103" class="lbl" text-anchor="middle">OC: 主 agent fs.write</text>

    <line x1="750" y1="116" x2="750" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar09F)" />

    <rect x="670" y="138" width="160" height="48" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="750" y="158" class="lbl" text-anchor="middle">after_tool_call hook</text>
    <text x="750" y="174" class="t-s" text-anchor="middle">user plugin 接 reviewer</text>

    <line x1="750" y1="186" x2="750" y2="205" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar09F)" />

    <rect x="670" y="208" width="160" height="36" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="750" y="231" class="lbl" text-anchor="middle">findings → system msg</text>

    <text x="750" y="280" class="note" text-anchor="middle">分隔线 ↓ Hermes</text>
    <line x1="670" y1="290" x2="830" y2="290" stroke="#94a3b8" stroke-dasharray="4 3" stroke-width="1" />

    <rect x="670" y="298" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="750" y="321" class="lbl" text-anchor="middle">HM: 「review 一下」</text>

    <line x1="750" y1="334" x2="750" y2="353" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar09F)" />

    <rect x="670" y="356" width="160" height="36" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="750" y="379" class="lbl" text-anchor="middle">terminal git diff</text>

    <line x1="750" y1="392" x2="750" y2="411" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar09F)" />

    <rect x="670" y="414" width="160" height="36" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="750" y="437" class="lbl" text-anchor="middle">主 agent 直接输出</text>

    <text x="750" y="475" class="note" text-anchor="middle">OC = pipeline hook</text>
    <text x="750" y="490" class="note" text-anchor="middle">HM = 零基础设施</text>
  </g>

  <text x="430" y="640" class="t-s" text-anchor="middle">隔离深度从右到左递减；上手成本从左到右递增。选哪种取决于 agent 定位 + review 重要性</text>
</svg>
"""

def write(slug, svg):
    out = PUBLIC / f"{slug}.svg"
    out.write_text(svg, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size} bytes)")

if __name__ == "__main__":
    PUBLIC.mkdir(parents=True, exist_ok=True)
    write("09-tradeoff", TRADEOFF_SVG)
    write("09-review-flows", FLOWS_SVG)
