#!/usr/bin/env python3
"""
Generate chapter 02 SVGs (TradeOff replacement + 7-layer prompt anatomy).
Writes with explicit UTF-8 encoding so CJK glyphs survive on Windows.
"""
from pathlib import Path

PUBLIC = Path("public/diagrams")

TRADEOFF_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480" role="img"
     aria-label="四家 Agent Loop 在执行自由度 × 可验证性 两条轴上的位置">
  <defs>
    <filter id="wobble02">
      <feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="2" />
      <feDisplacementMap in="SourceGraphic" scale="2" />
    </filter>
    <marker id="arr02" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#1e293b" />
    </marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .ax   { font: 600 12px sans-serif; fill: #1e293b; }
      .t    { font: 11.5px sans-serif; fill: #334155; }
      .t-s  { font: 10.5px sans-serif; fill: #64748b; }
      .pin  { font: 700 12.5px sans-serif; fill: #fff; }
      .note { font: italic 10.5px sans-serif; fill: #475569; }
    </style>
  </defs>

  <rect x="0" y="0" width="760" height="480" fill="transparent" />

  <text x="380" y="26" class="h" text-anchor="middle">Agent Loop：执行自由度 × 可验证性</text>
  <text x="380" y="44" class="note" text-anchor="middle">同一个 Observe-Plan-Act-Verify 闭环，四家的取舍连成一片，但没有一家在右上角</text>

  <g filter="url(#wobble02)">
    <rect x="100" y="80" width="280" height="160" fill="#fef9c3" opacity="0.45" />
    <rect x="380" y="80" width="280" height="160" fill="#dcfce7" opacity="0.45" />
    <rect x="100" y="240" width="280" height="160" fill="#fee2e2" opacity="0.45" />
    <rect x="380" y="240" width="280" height="160" fill="#dbeafe" opacity="0.45" />

    <text x="120" y="100" class="t-s">紧但难外推</text>
    <text x="640" y="100" class="t-s" text-anchor="end">理想：自由 + 可验证</text>
    <text x="120" y="260" class="t-s">死板 + 黑盒</text>
    <text x="640" y="260" class="t-s" text-anchor="end">自由 + 黑盒</text>

    <line x1="100" y1="400" x2="660" y2="400" stroke="#1e293b" stroke-width="2.5" marker-end="url(#arr02)" />
    <line x1="100" y1="400" x2="100" y2="70" stroke="#1e293b" stroke-width="2.5" marker-end="url(#arr02)" />
    <line x1="380" y1="80" x2="380" y2="400" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />
    <line x1="100" y1="240" x2="660" y2="240" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />

    <text x="660" y="420" class="ax" text-anchor="end">执行自由度 →</text>
    <text x="105" y="68" class="ax">↑ 可验证性</text>
    <text x="100" y="420" class="t-s" text-anchor="middle">少</text>
    <text x="660" y="420" class="t-s" text-anchor="end">多</text>

    <circle cx="200" cy="125" r="14" fill="#2563eb" stroke="#1e293b" stroke-width="2" />
    <text x="200" y="129" class="pin" text-anchor="middle">CX</text>
    <line x1="200" y1="125" x2="200" y2="170" stroke="#2563eb" stroke-width="1" stroke-dasharray="2 2" />
    <text x="200" y="184" class="t" text-anchor="middle">Codex</text>
    <text x="200" y="200" class="t-s" text-anchor="middle">goals.rs + execpolicy</text>
    <text x="200" y="214" class="t-s" text-anchor="middle">4 段串联 verifier</text>

    <circle cx="350" cy="180" r="14" fill="#7c3aed" stroke="#1e293b" stroke-width="2" />
    <text x="350" y="184" class="pin" text-anchor="middle">CC</text>
    <line x1="350" y1="180" x2="350" y2="125" stroke="#7c3aed" stroke-width="1" stroke-dasharray="2 2" />
    <text x="350" y="115" class="t" text-anchor="middle">Claude Code</text>
    <text x="350" y="98" class="t-s" text-anchor="middle">7 种 transition.reason</text>
    <text x="350" y="84" class="t-s" text-anchor="middle">TOKEN_BUDGET 软退</text>

    <circle cx="500" cy="220" r="14" fill="#16a34a" stroke="#1e293b" stroke-width="2" />
    <text x="500" y="224" class="pin" text-anchor="middle">OC</text>
    <line x1="500" y1="220" x2="500" y2="270" stroke="#16a34a" stroke-width="1" stroke-dasharray="2 2" />
    <text x="500" y="285" class="t" text-anchor="middle">OpenClaw</text>
    <text x="500" y="301" class="t-s" text-anchor="middle">十几个 plugin hook</text>
    <text x="500" y="315" class="t-s" text-anchor="middle">toolloop / 兜底 verifier</text>

    <circle cx="600" cy="310" r="14" fill="#f97316" stroke="#1e293b" stroke-width="2" />
    <text x="600" y="314" class="pin" text-anchor="middle">HM</text>
    <line x1="600" y1="310" x2="600" y2="355" stroke="#f97316" stroke-width="1" stroke-dasharray="2 2" />
    <text x="600" y="370" class="t" text-anchor="middle">Hermes</text>
    <text x="600" y="386" class="t-s" text-anchor="middle">IterationBudget 90/50</text>
    <text x="600" y="400" class="t-s" text-anchor="middle">skill 自评 / memory 长跑</text>

    <text x="595" y="120" class="note" text-anchor="middle">没人能同时拿满</text>
    <text x="595" y="138" class="note" text-anchor="middle">两条轴有取舍</text>
  </g>

  <text x="20" y="465" class="t-s">CX = Codex · CC = Claude Code · OC = OpenClaw · HM = Hermes</text>
  <text x="740" y="465" class="t-s" text-anchor="end">越靠右越敢让 loop 自由跑；越靠上越能在外部判这一步对错</text>
</svg>
"""

PROMPT_LAYERS_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 460" role="img"
     aria-label="四家 Agent system prompt 共有的 7 层骨架">
  <defs>
    <filter id="wb02p">
      <feTurbulence type="fractalNoise" baseFrequency="0.022" numOctaves="2" seed="11" />
      <feDisplacementMap in="SourceGraphic" scale="1.6" />
    </filter>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .lbl  { font: 700 12.5px sans-serif; fill: #1e293b; }
      .t    { font: 11.5px sans-serif; fill: #334155; }
      .t-s  { font: 10.5px sans-serif; fill: #475569; }
      .num  { font: 700 14px sans-serif; fill: #f97316; }
    </style>
  </defs>

  <text x="380" y="28" class="h" text-anchor="middle">通用结构：4 系统都在拼这 7 层</text>
  <text x="380" y="46" class="t-s" text-anchor="middle">差异在「分几个文件 / 哪几层 cached / 谁来注入」，不在层本身</text>

  <g filter="url(#wb02p)">
    <rect x="60" y="70" width="640" height="40" rx="6" fill="#fef9c3" stroke="#1e293b" stroke-width="1.8" />
    <text x="78" y="95" class="num">0</text>
    <text x="110" y="89" class="lbl">身份 · Identity</text>
    <text x="110" y="104" class="t-s">「你是谁」——一句话定模型角色（Codex agent / Claude Code / Hermes 等）</text>
    <text x="680" y="95" class="t-s" text-anchor="end">静态，必 cache</text>

    <rect x="60" y="118" width="640" height="40" rx="6" fill="#fde68a" stroke="#1e293b" stroke-width="1.8" />
    <text x="78" y="143" class="num">1</text>
    <text x="110" y="137" class="lbl">任务态势 · Task framing</text>
    <text x="110" y="152" class="t-s">「现在在干嘛」——交互模式 / agent 模式 / review 模式</text>
    <text x="680" y="143" class="t-s" text-anchor="end">半静态</text>

    <rect x="60" y="166" width="640" height="40" rx="6" fill="#fed7aa" stroke="#1e293b" stroke-width="1.8" />
    <text x="78" y="191" class="num">2</text>
    <text x="110" y="185" class="lbl">工具行为 · Tool guidance</text>
    <text x="110" y="200" class="t-s">「工具怎么用」——并行 / 串行、确认时机、危险操作规约</text>
    <text x="680" y="191" class="t-s" text-anchor="end">静态，cache 命中率高</text>

    <rect x="60" y="214" width="640" height="40" rx="6" fill="#fecaca" stroke="#1e293b" stroke-width="1.8" />
    <text x="78" y="239" class="num">3</text>
    <text x="110" y="233" class="lbl">长期记忆 · Memory</text>
    <text x="110" y="248" class="t-s">「之前发生过什么」——上一次 session 的摘要 / SOUL.md / Memory facts</text>
    <text x="680" y="239" class="t-s" text-anchor="end">动态，cache 边界</text>

    <rect x="60" y="262" width="640" height="40" rx="6" fill="#fce7f3" stroke="#1e293b" stroke-width="1.8" />
    <text x="78" y="287" class="num">4</text>
    <text x="110" y="281" class="lbl">上下文文件 · Context files</text>
    <text x="110" y="296" class="t-s">「项目本地约定」——AGENTS.md / CLAUDE.md / .claude/system-prompt.md</text>
    <text x="680" y="287" class="t-s" text-anchor="end">动态，命中本地</text>

    <rect x="60" y="310" width="640" height="40" rx="6" fill="#e9d5ff" stroke="#1e293b" stroke-width="1.8" />
    <text x="78" y="335" class="num">5</text>
    <text x="110" y="329" class="lbl">环境提示 · Env hints</text>
    <text x="110" y="344" class="t-s">「时间 / 平台 / 权限」——OS、cwd、sandbox 状态、当前 model 限制</text>
    <text x="680" y="335" class="t-s" text-anchor="end">每 turn 都可能变</text>

    <rect x="60" y="358" width="640" height="40" rx="6" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.8" />
    <text x="78" y="383" class="num">6</text>
    <text x="110" y="377" class="lbl">输出风格 · Output style</text>
    <text x="110" y="392" class="t-s">「怎么说话」——是否 markdown、引用规约、思考链是否暴露</text>
    <text x="680" y="383" class="t-s" text-anchor="end">静态，最末层</text>
  </g>

  <text x="20" y="430" class="t-s">cache 边界（一般在层 2-3 之间或 3-4 之间）：上面越静态越宜 cache，下面越动态越 ephemeral。</text>
  <text x="20" y="446" class="t-s">Codex 一份大 markdown 没有分界；Claude Code 显式 SYSTEM_PROMPT_DYNAMIC_BOUNDARY；OpenClaw 用 PromptMode 三档近似；Hermes 用 10 层 + skip_* 开关。</text>
</svg>
"""


def write(slug: str, svg: str) -> None:
    out = PUBLIC / f"{slug}.svg"
    out.write_text(svg, encoding="utf-8")
    size = out.stat().st_size
    print(f"wrote {out} ({size} bytes)")


if __name__ == "__main__":
    PUBLIC.mkdir(parents=True, exist_ok=True)
    write("02-tradeoff", TRADEOFF_SVG)
    write("02-prompt-layers", PROMPT_LAYERS_SVG)
