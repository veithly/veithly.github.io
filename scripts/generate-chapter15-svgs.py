#!/usr/bin/env python3
"""Chapter 15 SVGs: TradeOff (观测投入 x 价格表精度) + 四种观测栈并列图."""
from pathlib import Path

PUBLIC = Path("public/diagrams")

TRADEOFF_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 480" role="img"
     aria-label="四家观测栈在观测投入 x 价格表精度上的位置">
  <defs>
    <filter id="wb15"><feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="151" /><feDisplacementMap in="SourceGraphic" scale="2" /></filter>
    <marker id="ar15" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .ax   { font: 600 12.5px sans-serif; fill: #1e293b; }
      .t    { font: 11.5px sans-serif; fill: #334155; }
      .t-s  { font: 10.5px sans-serif; fill: #64748b; }
      .pin  { font: 700 12.5px sans-serif; fill: #fff; }
      .note { font: italic 10.5px sans-serif; fill: #475569; }
    </style>
  </defs>

  <text x="390" y="26" class="h" text-anchor="middle">观测栈：观测投入 x 价格表精度</text>
  <text x="390" y="44" class="t-s" text-anchor="middle">越往右观测代码越多；越往上「成本估算可信度」越高；不同 agent 形态需求不同</text>

  <g filter="url(#wb15)">
    <rect x="100" y="80" width="280" height="160" fill="#fef9c3" opacity="0.4" />
    <rect x="380" y="80" width="280" height="160" fill="#dcfce7" opacity="0.4" />
    <rect x="100" y="240" width="280" height="160" fill="#dbeafe" opacity="0.4" />
    <rect x="380" y="240" width="280" height="160" fill="#fee2e2" opacity="0.4" />

    <text x="120" y="100" class="t-s">观测少 · 价格准</text>
    <text x="640" y="100" class="t-s" text-anchor="end">观测多 · 价格准</text>
    <text x="120" y="260" class="t-s">观测少 · 价格糙</text>
    <text x="640" y="260" class="t-s" text-anchor="end">观测多 · 价格糙</text>

    <line x1="100" y1="400" x2="660" y2="400" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar15)" />
    <line x1="100" y1="400" x2="100" y2="70" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar15)" />
    <line x1="380" y1="80" x2="380" y2="400" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />
    <line x1="100" y1="240" x2="660" y2="240" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />

    <text x="660" y="420" class="ax" text-anchor="end">观测代码量 →</text>
    <text x="110" y="68" class="ax">↑ 成本估算的「我有多确定」</text>

    <!-- Hermes: top-left (5 source 高精度 + 中等观测) -->
    <circle cx="320" cy="100" r="14" fill="#f97316" stroke="#1e293b" stroke-width="2" />
    <text x="320" y="104" class="pin" text-anchor="middle">HM</text>
    <text x="320" y="131" class="t" text-anchor="middle">Hermes</text>
    <text x="320" y="146" class="t-s" text-anchor="middle">CanonicalUsage</text>
    <text x="320" y="159" class="t-s" text-anchor="middle">+ 5 CostSource 优先级</text>

    <!-- Claude Code: top-middle (硬编码 5 tier 高精度 + 中等观测) -->
    <circle cx="450" cy="160" r="14" fill="#7c3aed" stroke="#1e293b" stroke-width="2" />
    <text x="450" y="164" class="pin" text-anchor="middle">CC</text>
    <text x="450" y="191" class="t" text-anchor="middle">Claude Code</text>
    <text x="450" y="206" class="t-s" text-anchor="middle">modelCost 5 tier</text>
    <text x="450" y="219" class="t-s" text-anchor="middle">+ /insights 命令</text>

    <!-- Codex: right-middle (3 crate 大量观测 + 中等精度) -->
    <circle cx="620" cy="240" r="14" fill="#2563eb" stroke="#1e293b" stroke-width="2" />
    <text x="620" y="244" class="pin" text-anchor="middle">CX</text>
    <text x="620" y="271" class="t" text-anchor="middle">Codex</text>
    <text x="620" y="286" class="t-s" text-anchor="middle">3 个独立 crate</text>
    <text x="620" y="299" class="t-s" text-anchor="middle">otel/analytics/trace</text>

    <!-- OpenClaw: bottom-middle (13 事件类型，cost 留空) -->
    <circle cx="430" cy="320" r="14" fill="#16a34a" stroke="#1e293b" stroke-width="2" />
    <text x="430" y="324" class="pin" text-anchor="middle">OC</text>
    <text x="430" y="351" class="t" text-anchor="middle">OpenClaw</text>
    <text x="430" y="366" class="t-s" text-anchor="middle">13 类 DiagnosticEvent</text>
    <text x="430" y="379" class="t-s" text-anchor="middle">cost 留空给上游填</text>
  </g>

  <text x="20" y="465" class="t-s">CX = Codex · CC = Claude Code · OC = OpenClaw · HM = Hermes</text>
</svg>
"""

FLOWS_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 600" role="img"
     aria-label="四种观测栈并列对照">
  <defs>
    <filter id="wb15F"><feTurbulence type="fractalNoise" baseFrequency="0.022" numOctaves="2" seed="157" /><feDisplacementMap in="SourceGraphic" scale="1.5" /></filter>
    <marker id="ar15F" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .col  { font: 700 13px sans-serif; fill: #1e293b; }
      .lbl  { font: 700 11px sans-serif; fill: #1e293b; }
      .t-s  { font: 10.5px sans-serif; fill: #475569; }
      .note { font: italic 10.5px sans-serif; fill: #b45309; }
    </style>
  </defs>

  <text x="440" y="24" class="h" text-anchor="middle">四种观测栈并列</text>
  <text x="440" y="42" class="t-s" text-anchor="middle">3 crate（Codex）· modelCost + /insights（Claude Code）· DiagnosticEvent 13 类（OpenClaw）· CanonicalUsage + 5 CostSource（Hermes）</text>

  <g filter="url(#wb15F)">
    <!-- Codex column -->
    <text x="120" y="70" class="col" text-anchor="middle">Codex · 3 crate</text>
    <rect x="40" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="103" class="lbl" text-anchor="middle">hot path writer API</text>

    <line x1="120" y1="116" x2="120" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar15F)" />

    <rect x="40" y="138" width="160" height="60" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="158" class="lbl" text-anchor="middle">codex-otel</text>
    <text x="120" y="174" class="t-s" text-anchor="middle">4 exporter: None / Statsig</text>
    <text x="120" y="188" class="t-s" text-anchor="middle">OtlpGrpc / OtlpHttp</text>

    <line x1="120" y1="198" x2="120" y2="217" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar15F)" />

    <rect x="40" y="220" width="160" height="60" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="240" class="lbl" text-anchor="middle">codex-analytics</text>
    <text x="120" y="256" class="t-s" text-anchor="middle">TrackEventRequest 20+</text>
    <text x="120" y="270" class="t-s" text-anchor="middle">AcceptedLineFingerprints</text>

    <line x1="120" y1="280" x2="120" y2="299" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar15F)" />

    <rect x="40" y="302" width="160" height="60" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="322" class="lbl" text-anchor="middle">codex-rollout-trace</text>
    <text x="120" y="338" class="t-s" text-anchor="middle">trace.jsonl + manifest</text>
    <text x="120" y="352" class="t-s" text-anchor="middle">reducer 离线 replay</text>

    <text x="120" y="395" class="note" text-anchor="middle">debug 默认关上报</text>
    <text x="120" y="410" class="note" text-anchor="middle">cfg!(debug_assertions)</text>

    <!-- Claude Code column -->
    <text x="330" y="70" class="col" text-anchor="middle">Claude Code · modelCost + insights</text>
    <rect x="250" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="103" class="lbl" text-anchor="middle">hot path usage</text>

    <line x1="330" y1="116" x2="330" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar15F)" />

    <rect x="250" y="138" width="160" height="60" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="158" class="lbl" text-anchor="middle">modelCost.ts</text>
    <text x="330" y="174" class="t-s" text-anchor="middle">5 cost tier 硬编码</text>
    <text x="330" y="188" class="t-s" text-anchor="middle">tokensToUSDCost(usage)</text>

    <line x1="330" y1="198" x2="330" y2="217" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar15F)" />

    <rect x="250" y="220" width="160" height="60" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="240" class="lbl" text-anchor="middle">未知模型 fallback</text>
    <text x="330" y="256" class="t-s" text-anchor="middle">默认值 + 告警</text>
    <text x="330" y="270" class="t-s" text-anchor="middle">tengu_unknown_model_cost</text>

    <line x1="330" y1="280" x2="330" y2="299" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar15F)" />

    <rect x="250" y="302" width="160" height="60" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="322" class="lbl" text-anchor="middle">sessionStorage</text>
    <text x="330" y="338" class="t-s" text-anchor="middle">~/.claude/projects/</text>
    <text x="330" y="352" class="t-s" text-anchor="middle">sessions/*.json</text>

    <line x1="330" y1="362" x2="330" y2="381" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar15F)" />

    <rect x="250" y="384" width="160" height="48" rx="8" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="404" class="lbl" text-anchor="middle">/insights 命令</text>
    <text x="330" y="420" class="t-s" text-anchor="middle">Opus x 2 terminal 报表</text>

    <!-- OpenClaw column -->
    <text x="540" y="70" class="col" text-anchor="middle">OpenClaw · DiagnosticEvent 13 类</text>
    <rect x="460" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="103" class="lbl" text-anchor="middle">hot path</text>

    <line x1="540" y1="116" x2="540" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar15F)" />

    <rect x="460" y="138" width="160" height="48" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="158" class="lbl" text-anchor="middle">emitDiagnosticEvent</text>
    <text x="540" y="174" class="t-s" text-anchor="middle">seq++, ts, dispatchDepth</text>

    <line x1="540" y1="186" x2="540" y2="205" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar15F)" />

    <rect x="460" y="208" width="160" height="72" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="226" class="lbl" text-anchor="middle">13 类事件</text>
    <text x="540" y="240" class="t-s" text-anchor="middle">model.usage / webhook x3</text>
    <text x="540" y="254" class="t-s" text-anchor="middle">message x2 / session x2</text>
    <text x="540" y="268" class="t-s" text-anchor="middle">queue x2 / run / heartbeat</text>

    <line x1="540" y1="280" x2="540" y2="299" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar15F)" />

    <rect x="460" y="302" width="160" height="48" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="322" class="lbl" text-anchor="middle">tool.loop 检测器</text>
    <text x="540" y="338" class="t-s" text-anchor="middle">repeat / poll / circuit / ping-pong</text>

    <line x1="540" y1="350" x2="540" y2="369" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar15F)" />

    <rect x="460" y="372" width="160" height="48" rx="8" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="392" class="lbl" text-anchor="middle">listener 模式</text>
    <text x="540" y="408" class="t-s" text-anchor="middle">落哪儿由部署方决定</text>

    <text x="540" y="440" class="note" text-anchor="middle">cost 字段留空</text>

    <!-- Hermes column -->
    <text x="760" y="70" class="col" text-anchor="middle">Hermes · CanonicalUsage + 5 source</text>
    <rect x="680" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="103" class="lbl" text-anchor="middle">usage 数据</text>

    <line x1="760" y1="116" x2="760" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar15F)" />

    <rect x="680" y="138" width="160" height="48" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="158" class="lbl" text-anchor="middle">CanonicalUsage</text>
    <text x="760" y="174" class="t-s" text-anchor="middle">input/output/cache_r/w/reasoning</text>

    <line x1="760" y1="186" x2="760" y2="205" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar15F)" />

    <rect x="680" y="208" width="160" height="48" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="228" class="lbl" text-anchor="middle">BillingRoute</text>
    <text x="760" y="244" class="t-s" text-anchor="middle">provider + model + base_url</text>

    <line x1="760" y1="256" x2="760" y2="275" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar15F)" />

    <rect x="680" y="278" width="160" height="72" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="296" class="lbl" text-anchor="middle">5 CostSource 优先级</text>
    <text x="760" y="310" class="t-s" text-anchor="middle">provider_cost_api 最高</text>
    <text x="760" y="324" class="t-s" text-anchor="middle">generation / models / docs</text>
    <text x="760" y="338" class="t-s" text-anchor="middle">override / contract 最低</text>

    <line x1="760" y1="350" x2="760" y2="369" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar15F)" />

    <rect x="680" y="372" width="160" height="48" rx="8" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="392" class="lbl" text-anchor="middle">CostResult 4 status</text>
    <text x="760" y="408" class="t-s" text-anchor="middle">actual/estimated/included/unknown</text>

    <text x="760" y="445" class="note" text-anchor="middle">SQLite + 终端 InsightsEngine</text>
  </g>

  <text x="440" y="475" class="t-s" text-anchor="middle">观测投入 + 成本精度，四家对四种场景的权衡</text>

  <g>
    <rect x="40" y="490" width="800" height="95" rx="8" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1" />
    <text x="60" y="510" class="lbl">共同点：</text>
    <text x="60" y="528" class="t-s">· 都至少分 4 维 token（input / output / cache_read / cache_write）</text>
    <text x="60" y="544" class="t-s">· 都把 hot path 跟 telemetry 解耦（writer API / emit / queue）</text>
    <text x="60" y="560" class="t-s">· 未知模型 fallback（不 crash 不算 0）</text>
    <text x="60" y="576" class="t-s">· 调试 / 测试环境默认不上报</text>
  </g>
</svg>
"""

def write(slug, svg):
    out = PUBLIC / f"{slug}.svg"
    out.write_text(svg, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    PUBLIC.mkdir(parents=True, exist_ok=True)
    write("15-tradeoff", TRADEOFF_SVG)
    write("15-observability-flows", FLOWS_SVG)
