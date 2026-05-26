#!/usr/bin/env python3
"""Chapter 10 SVGs: TradeOff (抽象厚度 × 并发自由度) + 四种 subagent 模型并列流程图."""
from pathlib import Path

PUBLIC = Path("public/diagrams")

TRADEOFF_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 480" role="img"
     aria-label="四家 subagent 模型在抽象厚度 × 并发自由度两条轴上的位置">
  <defs>
    <filter id="wb10"><feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="73" /><feDisplacementMap in="SourceGraphic" scale="2" /></filter>
    <marker id="ar10" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .ax   { font: 600 12.5px sans-serif; fill: #1e293b; }
      .t    { font: 11.5px sans-serif; fill: #334155; }
      .t-s  { font: 10.5px sans-serif; fill: #64748b; }
      .pin  { font: 700 12.5px sans-serif; fill: #fff; }
      .note { font: italic 10.5px sans-serif; fill: #475569; }
    </style>
  </defs>

  <text x="390" y="26" class="h" text-anchor="middle">Subagent：抽象厚度 × 并发自由度</text>
  <text x="390" y="44" class="t-s" text-anchor="middle">越往右抽象越重；越往上并发自由度越大；选哪种取决于业务场景</text>

  <g filter="url(#wb10)">
    <rect x="100" y="80" width="280" height="160" fill="#fef9c3" opacity="0.4" />
    <rect x="380" y="80" width="280" height="160" fill="#dcfce7" opacity="0.4" />
    <rect x="100" y="240" width="280" height="160" fill="#dbeafe" opacity="0.4" />
    <rect x="380" y="240" width="280" height="160" fill="#fee2e2" opacity="0.4" />

    <text x="120" y="100" class="t-s">轻量 · 并发自由</text>
    <text x="640" y="100" class="t-s" text-anchor="end">重型 · 并发自由</text>
    <text x="120" y="260" class="t-s">轻量 · 并发受限</text>
    <text x="640" y="260" class="t-s" text-anchor="end">重型 · 并发受限</text>

    <line x1="100" y1="400" x2="660" y2="400" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar10)" />
    <line x1="100" y1="400" x2="100" y2="70" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar10)" />
    <line x1="380" y1="80" x2="380" y2="400" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />
    <line x1="100" y1="240" x2="660" y2="240" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />

    <text x="660" y="420" class="ax" text-anchor="end">subagent 子系统的工程化深度 →</text>
    <text x="110" y="68" class="ax">↑ 用户拿到的并发自由度</text>

    <!-- Hermes: bottom-left (函数式 · 同步阻塞) -->
    <circle cx="200" cy="320" r="14" fill="#f97316" stroke="#1e293b" stroke-width="2" />
    <text x="200" y="324" class="pin" text-anchor="middle">HM</text>
    <text x="200" y="351" class="t" text-anchor="middle">Hermes</text>
    <text x="200" y="366" class="t-s" text-anchor="middle">delegate_task 函数</text>
    <text x="200" y="379" class="t-s" text-anchor="middle">同步 + 5 工具硬禁</text>

    <!-- Codex: middle-right (类型化 · 中等并发) -->
    <circle cx="520" cy="195" r="14" fill="#2563eb" stroke="#1e293b" stroke-width="2" />
    <text x="520" y="199" class="pin" text-anchor="middle">CX</text>
    <text x="520" y="226" class="t" text-anchor="middle">Codex</text>
    <text x="520" y="241" class="t-s" text-anchor="middle">SubAgentSource 5 种</text>
    <text x="520" y="254" class="t-s" text-anchor="middle">服务全继承父</text>

    <!-- Claude Code: top-right (Task 抽象 · 高并发自由度) -->
    <circle cx="500" cy="120" r="14" fill="#7c3aed" stroke="#1e293b" stroke-width="2" />
    <text x="500" y="124" class="pin" text-anchor="middle">CC</text>
    <text x="500" y="151" class="t" text-anchor="middle">Claude Code</text>
    <text x="500" y="166" class="t-s" text-anchor="middle">Task 7 种 + isConcurrencySafe</text>

    <!-- OpenClaw: bottom-right (全功能平台 · 中等并发，按 session 限流) -->
    <circle cx="610" cy="280" r="14" fill="#16a34a" stroke="#1e293b" stroke-width="2" />
    <text x="610" y="284" class="pin" text-anchor="middle">OC</text>
    <text x="610" y="311" class="t" text-anchor="middle">OpenClaw</text>
    <text x="610" y="326" class="t-s" text-anchor="middle">完整 subagent 平台</text>
    <text x="610" y="339" class="t-s" text-anchor="middle">push-based + 持久化 depth</text>
  </g>

  <text x="20" y="465" class="t-s">CX = Codex · CC = Claude Code · OC = OpenClaw · HM = Hermes</text>
</svg>
"""

FLOWS_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 620" role="img"
     aria-label="四种 subagent 模型流程并列">
  <defs>
    <filter id="wb10F"><feTurbulence type="fractalNoise" baseFrequency="0.022" numOctaves="2" seed="83" /><feDisplacementMap in="SourceGraphic" scale="1.5" /></filter>
    <marker id="ar10F" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .col  { font: 700 13px sans-serif; fill: #1e293b; }
      .lbl  { font: 700 11px sans-serif; fill: #1e293b; }
      .t-s  { font: 10.5px sans-serif; fill: #475569; }
      .note { font: italic 10.5px sans-serif; fill: #b45309; }
    </style>
  </defs>

  <text x="440" y="24" class="h" text-anchor="middle">四种 subagent 模型并列</text>
  <text x="440" y="42" class="t-s" text-anchor="middle">从函数式（Hermes）→ 类型化（Codex）→ 任务抽象（Claude Code）→ 完整平台（OpenClaw）</text>

  <g filter="url(#wb10F)">
    <!-- Hermes: function-style -->
    <text x="120" y="70" class="col" text-anchor="middle">Hermes · delegate_task</text>
    <rect x="40" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="103" class="lbl" text-anchor="middle">delegate_task(goal, ctx)</text>

    <line x1="120" y1="116" x2="120" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar10F)" />

    <rect x="40" y="138" width="160" height="48" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="158" class="lbl" text-anchor="middle">if depth ≥ MAX_DEPTH</text>
    <text x="120" y="174" class="t-s" text-anchor="middle">parent(0)→child(1)→reject</text>

    <line x1="120" y1="186" x2="120" y2="205" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar10F)" />

    <rect x="40" y="208" width="160" height="60" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="228" class="lbl" text-anchor="middle">硬禁 5 工具</text>
    <text x="120" y="244" class="t-s" text-anchor="middle">delegate · clarify · memory</text>
    <text x="120" y="258" class="t-s" text-anchor="middle">send_message · execute_code</text>

    <line x1="120" y1="268" x2="120" y2="287" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar10F)" />

    <rect x="40" y="290" width="160" height="48" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="310" class="lbl" text-anchor="middle">ThreadPoolExecutor</text>
    <text x="120" y="326" class="t-s" text-anchor="middle">默认 3 并发</text>

    <line x1="120" y1="338" x2="120" y2="357" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar10F)" />

    <rect x="40" y="360" width="160" height="36" rx="8" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="383" class="lbl" text-anchor="middle">as_completed 阻塞</text>

    <text x="120" y="420" class="note" text-anchor="middle">函数式 · 同步阻塞</text>
    <text x="120" y="435" class="note" text-anchor="middle">最小可用 · 边界清晰</text>

    <!-- Codex: typed -->
    <text x="330" y="70" class="col" text-anchor="middle">Codex · SubAgentSource</text>
    <rect x="250" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="103" class="lbl" text-anchor="middle">Codex::spawn(args)</text>

    <line x1="330" y1="116" x2="330" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar10F)" />

    <rect x="250" y="138" width="160" height="60" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="158" class="lbl" text-anchor="middle">SubAgentSource 5 种</text>
    <text x="330" y="174" class="t-s" text-anchor="middle">Review · Compact</text>
    <text x="330" y="188" class="t-s" text-anchor="middle">ThreadSpawn · Memory · Other</text>

    <line x1="330" y1="198" x2="330" y2="217" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar10F)" />

    <rect x="250" y="220" width="160" height="60" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="240" class="lbl" text-anchor="middle">继承父 7 类 service</text>
    <text x="330" y="256" class="t-s" text-anchor="middle">exec_policy · plugins · mcp</text>
    <text x="330" y="270" class="t-s" text-anchor="middle">skills · environment · ...</text>

    <line x1="330" y1="280" x2="330" y2="299" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar10F)" />

    <rect x="250" y="302" width="160" height="48" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="322" class="lbl" text-anchor="middle">AskForApproval=Never</text>
    <text x="330" y="338" class="t-s" text-anchor="middle">审批永远路由回父</text>

    <line x1="330" y1="350" x2="330" y2="369" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar10F)" />

    <rect x="250" y="372" width="160" height="36" rx="8" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="395" class="lbl" text-anchor="middle">receiver 推 TurnComplete</text>

    <text x="330" y="430" class="note" text-anchor="middle">类型化继承</text>
    <text x="330" y="445" class="note" text-anchor="middle">子永远 ≤ 父的能力集</text>

    <!-- Claude Code: Task abstraction -->
    <text x="540" y="70" class="col" text-anchor="middle">Claude Code · Task</text>
    <rect x="460" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="103" class="lbl" text-anchor="middle">TaskCreateTool 调用</text>

    <line x1="540" y1="116" x2="540" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar10F)" />

    <rect x="460" y="138" width="160" height="72" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="158" class="lbl" text-anchor="middle">TaskType 7 种</text>
    <text x="540" y="174" class="t-s" text-anchor="middle">local_bash · local_agent</text>
    <text x="540" y="188" class="t-s" text-anchor="middle">remote_agent · teammate</text>
    <text x="540" y="202" class="t-s" text-anchor="middle">workflow · monitor · dream</text>

    <line x1="540" y1="210" x2="540" y2="229" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar10F)" />

    <rect x="460" y="232" width="160" height="48" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="252" class="lbl" text-anchor="middle">FSM 状态</text>
    <text x="540" y="268" class="t-s" text-anchor="middle">pending→running→done/fail/killed</text>

    <line x1="540" y1="280" x2="540" y2="299" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar10F)" />

    <rect x="460" y="302" width="160" height="48" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="322" class="lbl" text-anchor="middle">isConcurrencySafe()</text>
    <text x="540" y="338" class="t-s" text-anchor="middle">dispatcher 自动决定并发</text>

    <line x1="540" y1="350" x2="540" y2="369" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar10F)" />

    <rect x="460" y="372" width="160" height="36" rx="8" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="395" class="lbl" text-anchor="middle">outputFile 持久化</text>

    <text x="540" y="430" class="note" text-anchor="middle">任务抽象</text>
    <text x="540" y="445" class="note" text-anchor="middle">subagent 只是其中一种</text>

    <!-- OpenClaw: full platform -->
    <text x="760" y="70" class="col" text-anchor="middle">OpenClaw · subagent 平台</text>
    <rect x="680" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="103" class="lbl" text-anchor="middle">spawn_subagent(13 字段)</text>

    <line x1="760" y1="116" x2="760" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar10F)" />

    <rect x="680" y="138" width="160" height="60" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="158" class="lbl" text-anchor="middle">registry 注册 run</text>
    <text x="760" y="174" class="t-s" text-anchor="middle">mode (run / session)</text>
    <text x="760" y="188" class="t-s" text-anchor="middle">sandbox (inherit / require)</text>

    <line x1="760" y1="198" x2="760" y2="217" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar10F)" />

    <rect x="680" y="220" width="160" height="48" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="240" class="lbl" text-anchor="middle">spawnDepth → session 存储</text>
    <text x="760" y="256" class="t-s" text-anchor="middle">跨进程重启保留</text>

    <line x1="760" y1="268" x2="760" y2="287" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar10F)" />

    <rect x="680" y="290" width="160" height="60" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="310" class="lbl" text-anchor="middle">返回值塞硬警告</text>
    <text x="760" y="326" class="t-s" text-anchor="middle">「不要 poll，等 push event」</text>
    <text x="760" y="340" class="t-s" text-anchor="middle">写进 tool result</text>

    <line x1="760" y1="350" x2="760" y2="369" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar10F)" />

    <rect x="680" y="372" width="160" height="48" rx="8" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="392" class="lbl" text-anchor="middle">subagent-announce</text>
    <text x="760" y="408" class="t-s" text-anchor="middle">push 完成 → user message</text>

    <text x="760" y="445" class="note" text-anchor="middle">完整平台</text>
    <text x="760" y="460" class="note" text-anchor="middle">企业级 · 跨会话恢复</text>
  </g>

  <!-- Bottom comparison -->
  <g>
    <rect x="40" y="490" width="800" height="100" rx="8" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1" />
    <text x="60" y="510" class="lbl">共同点（四家都同意的事）：</text>
    <text x="60" y="528" class="t-s">· 深度要管：MAX_DEPTH / spawnDepth / ThreadSpawn.depth 总要有一个</text>
    <text x="60" y="544" class="t-s">· 递归 spawn 必禁：子 agent 不能再开同类子 agent，要么工具级硬禁，要么 feature flag</text>
    <text x="60" y="560" class="t-s">· 子工具是父子集：永远不允许子比父更宽松（exec_policy 继承）</text>
    <text x="60" y="576" class="t-s">· 完成靠 push / future：从不 polling 拉子 agent 状态</text>
  </g>

  <text x="440" y="608" class="t-s" text-anchor="middle">从左到右抽象越重；从上到下并发自由度递减。选哪种取决于业务复杂度</text>
</svg>
"""


def write(slug, svg):
    out = PUBLIC / f"{slug}.svg"
    out.write_text(svg, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    PUBLIC.mkdir(parents=True, exist_ok=True)
    write("10-tradeoff", TRADEOFF_SVG)
    write("10-subagent-flows", FLOWS_SVG)
