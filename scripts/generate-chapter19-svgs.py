#!/usr/bin/env python3
"""Chapter 19 SVGs: TradeOff (学习时机 x 谁写) + 四种自我改进 pipeline 并列图."""
from pathlib import Path

PUBLIC = Path("public/diagrams")

TRADEOFF_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 480" role="img"
     aria-label="四家自我改进系统在学习时机 x 写入主体上的位置">
  <defs>
    <filter id="wb19"><feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="191" /><feDisplacementMap in="SourceGraphic" scale="2" /></filter>
    <marker id="ar19" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .ax   { font: 600 12.5px sans-serif; fill: #1e293b; }
      .t    { font: 11.5px sans-serif; fill: #334155; }
      .t-s  { font: 10.5px sans-serif; fill: #64748b; }
      .pin  { font: 700 12.5px sans-serif; fill: #fff; }
      .note { font: italic 10.5px sans-serif; fill: #475569; }
    </style>
  </defs>

  <text x="390" y="26" class="h" text-anchor="middle">自我改进：学习时机 x 写入主体</text>
  <text x="390" y="44" class="t-s" text-anchor="middle">越往右越「turn 外」；越往上越「自动化」；选哪种取决于谁拍板</text>

  <g filter="url(#wb19)">
    <rect x="100" y="80" width="280" height="160" fill="#fef9c3" opacity="0.4" />
    <rect x="380" y="80" width="280" height="160" fill="#dcfce7" opacity="0.4" />
    <rect x="100" y="240" width="280" height="160" fill="#dbeafe" opacity="0.4" />
    <rect x="380" y="240" width="280" height="160" fill="#fee2e2" opacity="0.4" />

    <text x="120" y="100" class="t-s">turn 内 · 自动</text>
    <text x="640" y="100" class="t-s" text-anchor="end">turn 外 · 自动</text>
    <text x="120" y="260" class="t-s">turn 内 · 用户驱动</text>
    <text x="640" y="260" class="t-s" text-anchor="end">turn 外 · 用户驱动</text>

    <line x1="100" y1="400" x2="660" y2="400" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar19)" />
    <line x1="100" y1="400" x2="100" y2="70" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar19)" />
    <line x1="380" y1="80" x2="380" y2="400" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />
    <line x1="100" y1="240" x2="660" y2="240" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />

    <text x="660" y="420" class="ax" text-anchor="end">学习时机：turn 外 →</text>
    <text x="110" y="68" class="ax">↑ 自动化程度</text>

    <circle cx="200" cy="170" r="14" fill="#16a34a" stroke="#1e293b" stroke-width="2" />
    <text x="200" y="174" class="pin" text-anchor="middle">OC</text>
    <text x="200" y="201" class="t" text-anchor="middle">OpenClaw</text>
    <text x="200" y="216" class="t-s" text-anchor="middle">被动索引 + decay</text>
    <text x="200" y="229" class="t-s" text-anchor="middle">「学」=「查」</text>

    <circle cx="240" cy="280" r="14" fill="#f97316" stroke="#1e293b" stroke-width="2" />
    <text x="240" y="284" class="pin" text-anchor="middle">HM</text>
    <text x="240" y="311" class="t" text-anchor="middle">Hermes</text>
    <text x="240" y="326" class="t-s" text-anchor="middle">turn 内 agent 主动写</text>
    <text x="240" y="339" class="t-s" text-anchor="middle">+ 11 条威胁扫描</text>

    <circle cx="580" cy="120" r="14" fill="#2563eb" stroke="#1e293b" stroke-width="2" />
    <text x="580" y="124" class="pin" text-anchor="middle">CX</text>
    <text x="580" y="151" class="t" text-anchor="middle">Codex</text>
    <text x="580" y="166" class="t-s" text-anchor="middle">Phase 1 + Phase 2</text>
    <text x="580" y="179" class="t-s" text-anchor="middle">800 行 LLM job</text>

    <circle cx="540" cy="320" r="14" fill="#7c3aed" stroke="#1e293b" stroke-width="2" />
    <text x="540" y="324" class="pin" text-anchor="middle">CC</text>
    <text x="540" y="351" class="t" text-anchor="middle">Claude Code</text>
    <text x="540" y="366" class="t-s" text-anchor="middle">skillify + /insights</text>
    <text x="540" y="379" class="t-s" text-anchor="middle">用户显式触发</text>
  </g>

  <text x="20" y="465" class="t-s">CX = Codex · CC = Claude Code · OC = OpenClaw · HM = Hermes</text>
</svg>
"""

FLOWS_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 620" role="img"
     aria-label="四种自我改进 pipeline 并列对照">
  <defs>
    <filter id="wb19F"><feTurbulence type="fractalNoise" baseFrequency="0.022" numOctaves="2" seed="197" /><feDisplacementMap in="SourceGraphic" scale="1.5" /></filter>
    <marker id="ar19F" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .col  { font: 700 13px sans-serif; fill: #1e293b; }
      .lbl  { font: 700 11px sans-serif; fill: #1e293b; }
      .t-s  { font: 10.5px sans-serif; fill: #475569; }
      .note { font: italic 10.5px sans-serif; fill: #b45309; }
    </style>
  </defs>

  <text x="440" y="24" class="h" text-anchor="middle">四种自我改进 pipeline 并列</text>
  <text x="440" y="42" class="t-s" text-anchor="middle">Phase 1+2 后台 LLM（Codex）· skillify 用户驱动（Claude Code）· 被动索引（OpenClaw）· turn 内显式写（Hermes）</text>

  <g filter="url(#wb19F)">
    <text x="120" y="70" class="col" text-anchor="middle">Codex · Phase 1 + Phase 2</text>
    <rect x="40" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="103" class="lbl" text-anchor="middle">turn 完成</text>

    <line x1="120" y1="116" x2="120" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar19F)" />

    <rect x="40" y="138" width="160" height="60" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="158" class="lbl" text-anchor="middle">Phase 1 per-turn</text>
    <text x="120" y="174" class="t-s" text-anchor="middle">stage1_outputs 抽取</text>
    <text x="120" y="188" class="t-s" text-anchor="middle">cwd + git_branch</text>

    <line x1="120" y1="198" x2="120" y2="217" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar19F)" />

    <rect x="40" y="220" width="160" height="60" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="240" class="lbl" text-anchor="middle">Phase 2 global</text>
    <text x="120" y="256" class="t-s" text-anchor="middle">800 行 LLM prompt</text>
    <text x="120" y="270" class="t-s" text-anchor="middle">6h cooldown</text>

    <line x1="120" y1="280" x2="120" y2="299" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar19F)" />

    <rect x="40" y="302" width="160" height="48" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="322" class="lbl" text-anchor="middle">wording preservation</text>
    <text x="120" y="338" class="t-s" text-anchor="middle">保留原话给 grep 留 hook</text>

    <line x1="120" y1="350" x2="120" y2="369" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar19F)" />

    <rect x="40" y="372" width="160" height="60" rx="8" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="392" class="lbl" text-anchor="middle">输出三件套</text>
    <text x="120" y="408" class="t-s" text-anchor="middle">MEMORY.md + memory_summary</text>
    <text x="120" y="422" class="t-s" text-anchor="middle">+ skills/&lt;name&gt;/</text>

    <text x="120" y="455" class="note" text-anchor="middle">最完整 self-improve</text>

    <text x="330" y="70" class="col" text-anchor="middle">Claude Code · 用户驱动</text>
    <rect x="250" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="103" class="lbl" text-anchor="middle">用户按按钮</text>

    <line x1="330" y1="116" x2="330" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar19F)" />

    <rect x="250" y="138" width="160" height="60" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="158" class="lbl" text-anchor="middle">skillify (4 round)</text>
    <text x="330" y="174" class="t-s" text-anchor="middle">disableModelInvocation</text>
    <text x="330" y="188" class="t-s" text-anchor="middle">必须用户主动调</text>

    <line x1="330" y1="198" x2="330" y2="217" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar19F)" />

    <rect x="250" y="220" width="160" height="60" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="240" class="lbl" text-anchor="middle">/insights</text>
    <text x="330" y="256" class="t-s" text-anchor="middle">Opus × 2 跑 facet+narrative</text>
    <text x="330" y="270" class="t-s" text-anchor="middle">在 *.jsonl 上跑</text>

    <line x1="330" y1="280" x2="330" y2="299" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar19F)" />

    <rect x="250" y="302" width="160" height="48" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="322" class="lbl" text-anchor="middle">autoMode critique</text>
    <text x="330" y="338" class="t-s" text-anchor="middle">LLM 审用户写的规则</text>

    <line x1="330" y1="350" x2="330" y2="369" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar19F)" />

    <rect x="250" y="372" width="160" height="48" rx="8" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="392" class="lbl" text-anchor="middle">用户预览 SKILL.md</text>
    <text x="330" y="408" class="t-s" text-anchor="middle">最后一道闸</text>

    <text x="330" y="450" class="note" text-anchor="middle">「不偷偷学」哲学</text>

    <text x="540" y="70" class="col" text-anchor="middle">OpenClaw · 被动索引</text>
    <rect x="460" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="103" class="lbl" text-anchor="middle">session JSONL 落盘</text>

    <line x1="540" y1="116" x2="540" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar19F)" />

    <rect x="460" y="138" width="160" height="48" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="158" class="lbl" text-anchor="middle">redactSensitiveText</text>
    <text x="540" y="174" class="t-s" text-anchor="middle">secrets 不进索引</text>

    <line x1="540" y1="186" x2="540" y2="205" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar19F)" />

    <rect x="460" y="208" width="160" height="60" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="228" class="lbl" text-anchor="middle">chunk + embed</text>
    <text x="540" y="244" class="t-s" text-anchor="middle">FTS5 + sqlite-vec</text>
    <text x="540" y="258" class="t-s" text-anchor="middle">写入索引</text>

    <line x1="540" y1="268" x2="540" y2="287" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar19F)" />

    <rect x="460" y="290" width="160" height="60" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="310" class="lbl" text-anchor="middle">temporal decay</text>
    <text x="540" y="326" class="t-s" text-anchor="middle">halfLife=30d</text>
    <text x="540" y="340" class="t-s" text-anchor="middle">evergreen 例外</text>

    <line x1="540" y1="350" x2="540" y2="369" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar19F)" />

    <rect x="460" y="372" width="160" height="60" rx="8" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="392" class="lbl" text-anchor="middle">retrieval 时混合</text>
    <text x="540" y="408" class="t-s" text-anchor="middle">semantic + lexical + MMR</text>
    <text x="540" y="422" class="t-s" text-anchor="middle">+ decay 排序</text>

    <text x="540" y="455" class="note" text-anchor="middle">「学」=「查」</text>

    <text x="760" y="70" class="col" text-anchor="middle">Hermes · turn 内显式写</text>
    <rect x="680" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="103" class="lbl" text-anchor="middle">agent turn 中</text>

    <line x1="760" y1="116" x2="760" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar19F)" />

    <rect x="680" y="138" width="160" height="48" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="158" class="lbl" text-anchor="middle">memory_tool 4 action</text>
    <text x="760" y="174" class="t-s" text-anchor="middle">add/replace/remove/read</text>

    <line x1="760" y1="186" x2="760" y2="205" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar19F)" />

    <rect x="680" y="208" width="160" height="60" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="228" class="lbl" text-anchor="middle">11 _MEMORY_THREAT</text>
    <text x="760" y="244" class="t-s" text-anchor="middle">+ 10 invisible unicode</text>
    <text x="760" y="258" class="t-s" text-anchor="middle">写入前阻断</text>

    <line x1="760" y1="268" x2="760" y2="287" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar19F)" />

    <rect x="680" y="290" width="160" height="60" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="310" class="lbl" text-anchor="middle">char limit 硬约束</text>
    <text x="760" y="326" class="t-s" text-anchor="middle">MEMORY.md 2200</text>
    <text x="760" y="340" class="t-s" text-anchor="middle">USER.md 1375</text>

    <line x1="760" y1="350" x2="760" y2="369" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar19F)" />

    <rect x="680" y="372" width="160" height="60" rx="8" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="392" class="lbl" text-anchor="middle">frozen snapshot</text>
    <text x="760" y="408" class="t-s" text-anchor="middle">mid-session 不动 prompt</text>
    <text x="760" y="422" class="t-s" text-anchor="middle">保 prefix cache</text>

    <text x="760" y="455" class="note" text-anchor="middle">最安全 + 最克制</text>
  </g>

  <text x="440" y="490" class="t-s" text-anchor="middle">「agent 什么时候学」的四种回答</text>

  <g>
    <rect x="40" y="505" width="800" height="95" rx="8" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1" />
    <text x="60" y="525" class="lbl">共同点：</text>
    <text x="60" y="543" class="t-s">· 都承认 raw session 可能含注入 / secret，必须 sanitize</text>
    <text x="60" y="559" class="t-s">· 都有 forgetting 机制（Codex workspace diff / OpenClaw decay / Hermes char limit / Claude Code 用户删除）</text>
    <text x="60" y="575" class="t-s">· 都把 user preference 跟 reusable knowledge 分开（要么物理分文件，要么 prompt 块分隔）</text>
    <text x="60" y="591" class="t-s">· consolidation prompt 都要明确「promote 什么」「不要 promote 什么」</text>
  </g>
</svg>
"""

def write(slug, svg):
    out = PUBLIC / f"{slug}.svg"
    out.write_text(svg, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    PUBLIC.mkdir(parents=True, exist_ok=True)
    write("19-tradeoff", TRADEOFF_SVG)
    write("19-improvement-pipelines", FLOWS_SVG)
