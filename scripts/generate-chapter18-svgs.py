#!/usr/bin/env python3
"""Chapter 18 SVGs: TradeOff (本地能力 x 云端能力) + 四种 cron 子系统并列图."""
from pathlib import Path

PUBLIC = Path("public/diagrams")

TRADEOFF_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 480" role="img"
     aria-label="四家 cron 系统在本地能力 x 云端能力上的位置">
  <defs>
    <filter id="wb18"><feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="181" /><feDisplacementMap in="SourceGraphic" scale="2" /></filter>
    <marker id="ar18" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .ax   { font: 600 12.5px sans-serif; fill: #1e293b; }
      .t    { font: 11.5px sans-serif; fill: #334155; }
      .t-s  { font: 10.5px sans-serif; fill: #64748b; }
      .pin  { font: 700 12.5px sans-serif; fill: #fff; }
      .note { font: italic 10.5px sans-serif; fill: #475569; }
    </style>
  </defs>

  <text x="390" y="26" class="h" text-anchor="middle">Cron 系统：本地能力 x 云端能力</text>
  <text x="390" y="44" class="t-s" text-anchor="middle">越往右云端越强；越往上本地越完整；本地强适合断网，云端强适合大任务</text>

  <g filter="url(#wb18)">
    <rect x="100" y="80" width="280" height="160" fill="#fef9c3" opacity="0.4" />
    <rect x="380" y="80" width="280" height="160" fill="#dcfce7" opacity="0.4" />
    <rect x="100" y="240" width="280" height="160" fill="#dbeafe" opacity="0.4" />
    <rect x="380" y="240" width="280" height="160" fill="#fee2e2" opacity="0.4" />

    <text x="120" y="100" class="t-s">本地强 · 弱云</text>
    <text x="640" y="100" class="t-s" text-anchor="end">本地强 · 强云</text>
    <text x="120" y="260" class="t-s">本地弱 · 弱云</text>
    <text x="640" y="260" class="t-s" text-anchor="end">本地弱 · 强云</text>

    <line x1="100" y1="400" x2="660" y2="400" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar18)" />
    <line x1="100" y1="400" x2="100" y2="70" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar18)" />
    <line x1="380" y1="80" x2="380" y2="400" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />
    <line x1="100" y1="240" x2="660" y2="240" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />

    <text x="660" y="420" class="ax" text-anchor="end">云端能力 →</text>
    <text x="110" y="68" class="ax">↑ 本地 cron 完整度</text>

    <circle cx="180" cy="100" r="14" fill="#16a34a" stroke="#1e293b" stroke-width="2" />
    <text x="180" y="104" class="pin" text-anchor="middle">OC</text>
    <text x="180" y="131" class="t" text-anchor="middle">OpenClaw</text>
    <text x="180" y="146" class="t-s" text-anchor="middle">教科书级 cron</text>
    <text x="180" y="159" class="t-s" text-anchor="middle">+ delivery + failure</text>

    <circle cx="220" cy="180" r="14" fill="#7c3aed" stroke="#1e293b" stroke-width="2" />
    <text x="220" y="184" class="pin" text-anchor="middle">CC</text>
    <text x="220" y="211" class="t" text-anchor="middle">Claude Code</text>
    <text x="220" y="226" class="t-s" text-anchor="middle">1s tick + chokidar</text>
    <text x="220" y="239" class="t-s" text-anchor="middle">scheduler lock</text>

    <circle cx="280" cy="270" r="14" fill="#f97316" stroke="#1e293b" stroke-width="2" />
    <text x="280" y="274" class="pin" text-anchor="middle">HM</text>
    <text x="280" y="301" class="t" text-anchor="middle">Hermes</text>
    <text x="280" y="316" class="t-s" text-anchor="middle">croniter + jobs.json</text>
    <text x="280" y="329" class="t-s" text-anchor="middle">+ 10 威胁扫描</text>

    <circle cx="600" cy="320" r="14" fill="#2563eb" stroke="#1e293b" stroke-width="2" />
    <text x="600" y="324" class="pin" text-anchor="middle">CX</text>
    <text x="600" y="351" class="t" text-anchor="middle">Codex</text>
    <text x="600" y="366" class="t-s" text-anchor="middle">cloud-tasks 独立 binary</text>
    <text x="600" y="379" class="t-s" text-anchor="middle">bestOf 并行</text>
  </g>

  <text x="20" y="465" class="t-s">CX = Codex · CC = Claude Code · OC = OpenClaw · HM = Hermes</text>
</svg>
"""

FLOWS_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 620" role="img"
     aria-label="四种 cron 子系统并列对照">
  <defs>
    <filter id="wb18F"><feTurbulence type="fractalNoise" baseFrequency="0.022" numOctaves="2" seed="187" /><feDisplacementMap in="SourceGraphic" scale="1.5" /></filter>
    <marker id="ar18F" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .col  { font: 700 13px sans-serif; fill: #1e293b; }
      .lbl  { font: 700 11px sans-serif; fill: #1e293b; }
      .t-s  { font: 10.5px sans-serif; fill: #475569; }
      .note { font: italic 10.5px sans-serif; fill: #b45309; }
    </style>
  </defs>

  <text x="440" y="24" class="h" text-anchor="middle">四种 cron 子系统并列</text>
  <text x="440" y="42" class="t-s" text-anchor="middle">cloud-tasks（Codex）· 1s tick + scheduler lock（Claude Code）· at/every/cron + isolated-agent（OpenClaw）· croniter + jobs.json（Hermes）</text>

  <g filter="url(#wb18F)">
    <text x="120" y="70" class="col" text-anchor="middle">Codex · cloud-tasks</text>
    <rect x="40" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="103" class="lbl" text-anchor="middle">独立 binary</text>

    <line x1="120" y1="116" x2="120" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar18F)" />

    <rect x="40" y="138" width="160" height="48" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="158" class="lbl" text-anchor="middle">TaskSummary 远端</text>
    <text x="120" y="174" class="t-s" text-anchor="middle">客户端轮询列表</text>

    <line x1="120" y1="186" x2="120" y2="205" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar18F)" />

    <rect x="40" y="208" width="160" height="60" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="228" class="lbl" text-anchor="middle">EnvironmentRow</text>
    <text x="120" y="244" class="t-s" text-anchor="middle">pinned env + repo_hints</text>
    <text x="120" y="258" class="t-s" text-anchor="middle">每任务独立环境</text>

    <line x1="120" y1="268" x2="120" y2="287" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar18F)" />

    <rect x="40" y="290" width="160" height="60" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="310" class="lbl" text-anchor="middle">BestOfModalState</text>
    <text x="120" y="326" class="t-s" text-anchor="middle">N 并行多分支</text>
    <text x="120" y="340" class="t-s" text-anchor="middle">UI 选最优 apply</text>

    <line x1="120" y1="350" x2="120" y2="369" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar18F)" />

    <rect x="40" y="372" width="160" height="48" rx="8" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="392" class="lbl" text-anchor="middle">ApplyResultLevel</text>
    <text x="120" y="408" class="t-s" text-anchor="middle">Success/Partial/Error</text>

    <text x="120" y="450" class="note" text-anchor="middle">本地无 cron</text>
    <text x="120" y="465" class="note" text-anchor="middle">长任务全推云</text>

    <text x="330" y="70" class="col" text-anchor="middle">Claude Code · cron tool</text>
    <rect x="250" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="103" class="lbl" text-anchor="middle">CronCreateTool</text>

    <line x1="330" y1="116" x2="330" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar18F)" />

    <rect x="250" y="138" width="160" height="48" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="158" class="lbl" text-anchor="middle">5-field cron expr</text>
    <text x="330" y="174" class="t-s" text-anchor="middle">本地 timezone</text>

    <line x1="330" y1="186" x2="330" y2="205" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar18F)" />

    <rect x="250" y="208" width="160" height="60" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="228" class="lbl" text-anchor="middle">cronScheduler</text>
    <text x="330" y="244" class="t-s" text-anchor="middle">1s tick + chokidar 监听</text>
    <text x="330" y="258" class="t-s" text-anchor="middle">scheduler lock 跨进程</text>

    <line x1="330" y1="268" x2="330" y2="287" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar18F)" />

    <rect x="250" y="290" width="160" height="60" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="310" class="lbl" text-anchor="middle">recurring vs one-shot</text>
    <text x="330" y="326" class="t-s" text-anchor="middle">durable vs session-only</text>
    <text x="330" y="340" class="t-s" text-anchor="middle">permanent flag</text>

    <line x1="330" y1="350" x2="330" y2="369" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar18F)" />

    <rect x="250" y="372" width="160" height="48" rx="8" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="392" class="lbl" text-anchor="middle">onFire(prompt)</text>
    <text x="330" y="408" class="t-s" text-anchor="middle">注入当前 session queue</text>

    <text x="330" y="450" class="note" text-anchor="middle">IDE 风格 cron</text>

    <text x="540" y="70" class="col" text-anchor="middle">OpenClaw · cron 子系统</text>
    <rect x="460" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="103" class="lbl" text-anchor="middle">cron service</text>

    <line x1="540" y1="116" x2="540" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar18F)" />

    <rect x="460" y="138" width="160" height="60" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="158" class="lbl" text-anchor="middle">CronSchedule 3 种</text>
    <text x="540" y="174" class="t-s" text-anchor="middle">at / every / cron</text>
    <text x="540" y="188" class="t-s" text-anchor="middle">+ tz + staggerMs</text>

    <line x1="540" y1="198" x2="540" y2="217" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar18F)" />

    <rect x="460" y="220" width="160" height="60" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="240" class="lbl" text-anchor="middle">isolated-agent</text>
    <text x="540" y="256" class="t-s" text-anchor="middle">独立 session</text>
    <text x="540" y="270" class="t-s" text-anchor="middle">skills-snapshot 冻结</text>

    <line x1="540" y1="280" x2="540" y2="299" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar18F)" />

    <rect x="460" y="302" width="160" height="60" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="322" class="lbl" text-anchor="middle">failure-alert</text>
    <text x="540" y="338" class="t-s" text-anchor="middle">after + cooldownMs</text>
    <text x="540" y="352" class="t-s" text-anchor="middle">独立 destination</text>

    <line x1="540" y1="362" x2="540" y2="381" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar18F)" />

    <rect x="460" y="384" width="160" height="48" rx="8" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="404" class="lbl" text-anchor="middle">CronDelivery 4 模式</text>
    <text x="540" y="420" class="t-s" text-anchor="middle">none/announce/webhook</text>

    <text x="540" y="450" class="note" text-anchor="middle">13 个 regression test</text>
    <text x="540" y="465" class="note" text-anchor="middle">教科书级</text>

    <text x="760" y="70" class="col" text-anchor="middle">Hermes · croniter</text>
    <rect x="680" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="103" class="lbl" text-anchor="middle">~/.hermes/cron/jobs.json</text>

    <line x1="760" y1="116" x2="760" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar18F)" />

    <rect x="680" y="138" width="160" height="48" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="158" class="lbl" text-anchor="middle">croniter 解析</text>
    <text x="760" y="174" class="t-s" text-anchor="middle">标准 cron 语法</text>

    <line x1="760" y1="186" x2="760" y2="205" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar18F)" />

    <rect x="680" y="208" width="160" height="60" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="228" class="lbl" text-anchor="middle">scheduler.py</text>
    <text x="760" y="244" class="t-s" text-anchor="middle">asyncio 循环</text>
    <text x="760" y="258" class="t-s" text-anchor="middle">ONESHOT_GRACE=120s</text>

    <line x1="760" y1="268" x2="760" y2="287" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar18F)" />

    <rect x="680" y="290" width="160" height="60" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="310" class="lbl" text-anchor="middle">_scan_cron_prompt</text>
    <text x="760" y="326" class="t-s" text-anchor="middle">10 critical 威胁</text>
    <text x="760" y="340" class="t-s" text-anchor="middle">+ 10 invisible unicode</text>

    <line x1="760" y1="350" x2="760" y2="369" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar18F)" />

    <rect x="680" y="372" width="160" height="48" rx="8" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="392" class="lbl" text-anchor="middle">output md 落盘</text>
    <text x="760" y="408" class="t-s" text-anchor="middle">{job_id}/{ts}.md</text>

    <text x="760" y="450" class="note" text-anchor="middle">最克制</text>
  </g>

  <text x="440" y="490" class="t-s" text-anchor="middle">「让 agent 在你不在的时候也跑」的四种姿态</text>

  <g>
    <rect x="40" y="505" width="800" height="95" rx="8" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1" />
    <text x="60" y="525" class="lbl">共同点：</text>
    <text x="60" y="543" class="t-s">· 都需要持久化 schedule 定义（jobs.json / cron 表 / cloud-tasks 表）</text>
    <text x="60" y="559" class="t-s">· 都需要触发循环（1s tick / asyncio / backend push）</text>
    <text x="60" y="575" class="t-s">· 失败要有退避（OpenClaw 最显式：consecutiveErrors + scheduleErrorCount + failureAlert）</text>
    <text x="60" y="591" class="t-s">· 长任务要隔离（cloud env / isolated-agent / subagent / fork）</text>
  </g>
</svg>
"""

def write(slug, svg):
    out = PUBLIC / f"{slug}.svg"
    out.write_text(svg, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    PUBLIC.mkdir(parents=True, exist_ok=True)
    write("18-tradeoff", TRADEOFF_SVG)
    write("18-cron-systems", FLOWS_SVG)
