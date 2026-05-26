#!/usr/bin/env python3
"""Chapter 16 SVGs: TradeOff (工程克制 x 检索能力) + 四种记忆栈并列图."""
from pathlib import Path

PUBLIC = Path("public/diagrams")

TRADEOFF_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 480" role="img"
     aria-label="四家记忆栈在工程克制 x 检索能力上的位置">
  <defs>
    <filter id="wb16"><feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="161" /><feDisplacementMap in="SourceGraphic" scale="2" /></filter>
    <marker id="ar16" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .ax   { font: 600 12.5px sans-serif; fill: #1e293b; }
      .t    { font: 11.5px sans-serif; fill: #334155; }
      .t-s  { font: 10.5px sans-serif; fill: #64748b; }
      .pin  { font: 700 12.5px sans-serif; fill: #fff; }
      .note { font: italic 10.5px sans-serif; fill: #475569; }
    </style>
  </defs>

  <text x="390" y="26" class="h" text-anchor="middle">记忆栈：工程克制 x 检索能力</text>
  <text x="390" y="44" class="t-s" text-anchor="middle">越往右检索越强；越往上工程越克制；两端都极致就要 trade-off</text>

  <g filter="url(#wb16)">
    <rect x="100" y="80" width="280" height="160" fill="#fef9c3" opacity="0.4" />
    <rect x="380" y="80" width="280" height="160" fill="#dcfce7" opacity="0.4" />
    <rect x="100" y="240" width="280" height="160" fill="#dbeafe" opacity="0.4" />
    <rect x="380" y="240" width="280" height="160" fill="#fee2e2" opacity="0.4" />

    <text x="120" y="100" class="t-s">弱检索 · 克制</text>
    <text x="640" y="100" class="t-s" text-anchor="end">强检索 · 克制</text>
    <text x="120" y="260" class="t-s">弱检索 · 重工程</text>
    <text x="640" y="260" class="t-s" text-anchor="end">强检索 · 重工程</text>

    <line x1="100" y1="400" x2="660" y2="400" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar16)" />
    <line x1="100" y1="400" x2="100" y2="70" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar16)" />
    <line x1="380" y1="80" x2="380" y2="400" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />
    <line x1="100" y1="240" x2="660" y2="240" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />

    <text x="660" y="420" class="ax" text-anchor="end">检索能力 →</text>
    <text x="110" y="68" class="ax">↑ 工程克制（代码 / 依赖越少越上）</text>

    <circle cx="160" cy="140" r="14" fill="#f97316" stroke="#1e293b" stroke-width="2" />
    <text x="160" y="144" class="pin" text-anchor="middle">HM</text>
    <text x="160" y="171" class="t" text-anchor="middle">Hermes</text>
    <text x="160" y="186" class="t-s" text-anchor="middle">2 文件 + 4 action</text>
    <text x="160" y="199" class="t-s" text-anchor="middle">frozen snapshot</text>

    <circle cx="290" cy="200" r="14" fill="#2563eb" stroke="#1e293b" stroke-width="2" />
    <text x="290" y="204" class="pin" text-anchor="middle">CX</text>
    <text x="290" y="231" class="t" text-anchor="middle">Codex</text>
    <text x="290" y="246" class="t-s" text-anchor="middle">AGENTS.md 注入</text>
    <text x="290" y="259" class="t-s" text-anchor="middle">+ stage1/phase2 后台 job</text>

    <circle cx="500" cy="270" r="14" fill="#7c3aed" stroke="#1e293b" stroke-width="2" />
    <text x="500" y="274" class="pin" text-anchor="middle">CC</text>
    <text x="500" y="301" class="t" text-anchor="middle">Claude Code</text>
    <text x="500" y="316" class="t-s" text-anchor="middle">4 MemoryType</text>
    <text x="500" y="329" class="t-s" text-anchor="middle">+ 2 prompt mode + drift</text>

    <circle cx="620" cy="350" r="14" fill="#16a34a" stroke="#1e293b" stroke-width="2" />
    <text x="620" y="354" class="pin" text-anchor="middle">OC</text>
    <text x="620" y="381" class="t" text-anchor="middle">OpenClaw</text>
    <text x="620" y="396" class="t-s" text-anchor="middle">FTS5 + sqlite-vec</text>
  </g>

  <text x="20" y="465" class="t-s">CX = Codex · CC = Claude Code · OC = OpenClaw · HM = Hermes</text>
</svg>
"""

FLOWS_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 620" role="img"
     aria-label="四种记忆栈并列对照">
  <defs>
    <filter id="wb16F"><feTurbulence type="fractalNoise" baseFrequency="0.022" numOctaves="2" seed="167" /><feDisplacementMap in="SourceGraphic" scale="1.5" /></filter>
    <marker id="ar16F" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .col  { font: 700 13px sans-serif; fill: #1e293b; }
      .lbl  { font: 700 11px sans-serif; fill: #1e293b; }
      .t-s  { font: 10.5px sans-serif; fill: #475569; }
      .note { font: italic 10.5px sans-serif; fill: #b45309; }
    </style>
  </defs>

  <text x="440" y="24" class="h" text-anchor="middle">四种记忆栈并列</text>
  <text x="440" y="42" class="t-s" text-anchor="middle">AGENTS.md + 后台两阶段（Codex）· 4 MemoryType + drift（Claude Code）· qmd + decay（OpenClaw）· MEMORY+USER + frozen（Hermes）</text>

  <g filter="url(#wb16F)">
    <text x="120" y="70" class="col" text-anchor="middle">Codex · AGENTS.md + stage1/phase2</text>
    <rect x="40" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="103" class="lbl" text-anchor="middle">AGENTS.md (cwd)</text>

    <line x1="120" y1="116" x2="120" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar16F)" />

    <rect x="40" y="138" width="160" height="48" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="158" class="lbl" text-anchor="middle">UserInstructions 注入</text>
    <text x="120" y="174" class="t-s" text-anchor="middle">role=user + INSTRUCTIONS</text>

    <line x1="120" y1="186" x2="120" y2="205" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar16F)" />

    <rect x="40" y="208" width="160" height="60" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="228" class="lbl" text-anchor="middle">stage1_outputs</text>
    <text x="120" y="244" class="t-s" text-anchor="middle">thread + cwd + git_branch</text>
    <text x="120" y="258" class="t-s" text-anchor="middle">lease + ownership_token</text>

    <line x1="120" y1="268" x2="120" y2="287" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar16F)" />

    <rect x="40" y="290" width="160" height="60" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="310" class="lbl" text-anchor="middle">phase2 global consolidate</text>
    <text x="120" y="326" class="t-s" text-anchor="middle">input_watermark 增量</text>
    <text x="120" y="340" class="t-s" text-anchor="middle">6h cooldown</text>

    <line x1="120" y1="350" x2="120" y2="369" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar16F)" />

    <rect x="40" y="372" width="160" height="48" rx="8" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="392" class="lbl" text-anchor="middle">MemoryCitation</text>
    <text x="120" y="408" class="t-s" text-anchor="middle">回查 thread_id</text>

    <text x="120" y="450" class="note" text-anchor="middle">后台 job 写</text>
    <text x="120" y="465" class="note" text-anchor="middle">不卡用户</text>

    <text x="330" y="70" class="col" text-anchor="middle">Claude Code · 4 type + drift</text>
    <rect x="250" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="103" class="lbl" text-anchor="middle">/memory 命令</text>

    <line x1="330" y1="116" x2="330" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar16F)" />

    <rect x="250" y="138" width="160" height="60" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="158" class="lbl" text-anchor="middle">4 MemoryType</text>
    <text x="330" y="174" class="t-s" text-anchor="middle">user / feedback</text>
    <text x="330" y="188" class="t-s" text-anchor="middle">project / reference</text>

    <line x1="330" y1="198" x2="330" y2="217" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar16F)" />

    <rect x="250" y="220" width="160" height="48" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="240" class="lbl" text-anchor="middle">2 prompt mode</text>
    <text x="330" y="256" class="t-s" text-anchor="middle">COMBINED / INDIVIDUAL</text>

    <line x1="330" y1="268" x2="330" y2="287" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar16F)" />

    <rect x="250" y="290" width="160" height="48" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="310" class="lbl" text-anchor="middle">MEMORY_DRIFT_CAVEAT</text>
    <text x="330" y="326" class="t-s" text-anchor="middle">提醒模型 verify</text>

    <line x1="330" y1="338" x2="330" y2="357" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar16F)" />

    <rect x="250" y="360" width="160" height="60" rx="8" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="380" class="lbl" text-anchor="middle">Before recommending</text>
    <text x="330" y="396" class="t-s" text-anchor="middle">file path → 检查 file 存在</text>
    <text x="330" y="410" class="t-s" text-anchor="middle">function → grep 验证</text>

    <text x="330" y="450" class="note" text-anchor="middle">eval 驱动 prompt 设计</text>

    <text x="540" y="70" class="col" text-anchor="middle">OpenClaw · qmd + decay</text>
    <rect x="460" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="103" class="lbl" text-anchor="middle">MEMORY.md + memory/*</text>

    <line x1="540" y1="116" x2="540" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar16F)" />

    <rect x="460" y="138" width="160" height="48" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="158" class="lbl" text-anchor="middle">SQLite + FTS5</text>
    <text x="540" y="174" class="t-s" text-anchor="middle">全文索引</text>

    <line x1="540" y1="186" x2="540" y2="205" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar16F)" />

    <rect x="460" y="208" width="160" height="48" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="228" class="lbl" text-anchor="middle">sqlite-vec</text>
    <text x="540" y="244" class="t-s" text-anchor="middle">embedding 向量</text>

    <line x1="540" y1="256" x2="540" y2="275" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar16F)" />

    <rect x="460" y="278" width="160" height="60" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="298" class="lbl" text-anchor="middle">hybrid + MMR + decay</text>
    <text x="540" y="314" class="t-s" text-anchor="middle">半衰期 30 天</text>
    <text x="540" y="328" class="t-s" text-anchor="middle">evergreen 例外</text>

    <line x1="540" y1="338" x2="540" y2="357" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar16F)" />

    <rect x="460" y="360" width="160" height="60" rx="8" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="380" class="lbl" text-anchor="middle">qmd scope</text>
    <text x="540" y="396" class="t-s" text-anchor="middle">query → 注入哪些 dir</text>
    <text x="540" y="410" class="t-s" text-anchor="middle">private / shared</text>

    <text x="540" y="450" class="note" text-anchor="middle">最完整检索栈</text>

    <text x="760" y="70" class="col" text-anchor="middle">Hermes · MEMORY + USER</text>
    <rect x="680" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="103" class="lbl" text-anchor="middle">memory 工具 4 action</text>

    <line x1="760" y1="116" x2="760" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar16F)" />

    <rect x="680" y="138" width="160" height="60" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="158" class="lbl" text-anchor="middle">11 _MEMORY_THREAT</text>
    <text x="760" y="174" class="t-s" text-anchor="middle">注入扫描 + 10 个 invisible</text>
    <text x="760" y="188" class="t-s" text-anchor="middle">unicode 拦截</text>

    <line x1="760" y1="198" x2="760" y2="217" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar16F)" />

    <rect x="680" y="220" width="160" height="48" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="240" class="lbl" text-anchor="middle">MEMORY.md 2200 char</text>
    <text x="760" y="256" class="t-s" text-anchor="middle">USER.md 1375 char</text>

    <line x1="760" y1="268" x2="760" y2="287" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar16F)" />

    <rect x="680" y="290" width="160" height="60" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="310" class="lbl" text-anchor="middle">frozen snapshot</text>
    <text x="760" y="326" class="t-s" text-anchor="middle">mid-session 写只落盘</text>
    <text x="760" y="340" class="t-s" text-anchor="middle">保住 prefix cache</text>

    <line x1="760" y1="350" x2="760" y2="369" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar16F)" />

    <rect x="680" y="372" width="160" height="48" rx="8" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="392" class="lbl" text-anchor="middle">_file_lock</text>
    <text x="760" y="408" class="t-s" text-anchor="middle">fcntl / msvcrt 跨平台</text>

    <text x="760" y="450" class="note" text-anchor="middle">最克制</text>
  </g>

  <text x="440" y="490" class="t-s" text-anchor="middle">让 agent 记住东西，四种姿态对四种场景</text>

  <g>
    <rect x="40" y="505" width="800" height="95" rx="8" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1" />
    <text x="60" y="525" class="lbl">共同点：</text>
    <text x="60" y="543" class="t-s">· 短期记忆都靠 turn 间数据结构（rollout / sessionStorage / session-files / MessageHistory）</text>
    <text x="60" y="559" class="t-s">· 长期记忆都要明确「写入是写入还是注入」（snapshot vs 动态拼装）</text>
    <text x="60" y="575" class="t-s">· 输入扫描 + drift 处理都是 production 必须（Hermes 走代码扫描，Claude Code 走 prompt 提醒）</text>
    <text x="60" y="591" class="t-s">· 都有 / 命令做手动入口（/memory add / list / clear）</text>
  </g>
</svg>
"""

def write(slug, svg):
    out = PUBLIC / f"{slug}.svg"
    out.write_text(svg, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    PUBLIC.mkdir(parents=True, exist_ok=True)
    write("16-tradeoff", TRADEOFF_SVG)
    write("16-memory-stacks", FLOWS_SVG)
