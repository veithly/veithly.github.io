#!/usr/bin/env python3
"""Chapter 12 SVGs: TradeOff (枚举深度 × 运维可配置度) + 四种权限决策流程并列图."""
from pathlib import Path

PUBLIC = Path("public/diagrams")

TRADEOFF_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 480" role="img"
     aria-label="四家权限模型在枚举深度 × 运维可配置度上的位置">
  <defs>
    <filter id="wb12"><feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="113" /><feDisplacementMap in="SourceGraphic" scale="2" /></filter>
    <marker id="ar12" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .ax   { font: 600 12.5px sans-serif; fill: #1e293b; }
      .t    { font: 11.5px sans-serif; fill: #334155; }
      .t-s  { font: 10.5px sans-serif; fill: #64748b; }
      .pin  { font: 700 12.5px sans-serif; fill: #fff; }
      .note { font: italic 10.5px sans-serif; fill: #475569; }
    </style>
  </defs>

  <text x="390" y="26" class="h" text-anchor="middle">权限与审批：枚举类型化深度 × 运维可配置度</text>
  <text x="390" y="44" class="t-s" text-anchor="middle">越往右枚举越细；越往上运维旋钮越多；选哪种取决于产品和部署方式</text>

  <g filter="url(#wb12)">
    <rect x="100" y="80" width="280" height="160" fill="#fef9c3" opacity="0.4" />
    <rect x="380" y="80" width="280" height="160" fill="#dcfce7" opacity="0.4" />
    <rect x="100" y="240" width="280" height="160" fill="#dbeafe" opacity="0.4" />
    <rect x="380" y="240" width="280" height="160" fill="#fee2e2" opacity="0.4" />

    <text x="120" y="100" class="t-s">弱枚举 · 多旋钮</text>
    <text x="640" y="100" class="t-s" text-anchor="end">强枚举 · 多旋钮</text>
    <text x="120" y="260" class="t-s">弱枚举 · 少旋钮</text>
    <text x="640" y="260" class="t-s" text-anchor="end">强枚举 · 少旋钮</text>

    <line x1="100" y1="400" x2="660" y2="400" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar12)" />
    <line x1="100" y1="400" x2="100" y2="70" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar12)" />
    <line x1="380" y1="80" x2="380" y2="400" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />
    <line x1="100" y1="240" x2="660" y2="240" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />

    <text x="660" y="420" class="ax" text-anchor="end">决策 / 操作 / 答案的枚举类型化深度 →</text>
    <text x="110" y="68" class="ax">↑ 运维 / 管理员可配置旋钮</text>

    <!-- Hermes: bottom-left (子进程 + fail_open) -->
    <circle cx="190" cy="290" r="14" fill="#f97316" stroke="#1e293b" stroke-width="2" />
    <text x="190" y="294" class="pin" text-anchor="middle">HM</text>
    <text x="190" y="321" class="t" text-anchor="middle">Hermes</text>
    <text x="190" y="336" class="t-s" text-anchor="middle">tirith 子进程</text>
    <text x="190" y="349" class="t-s" text-anchor="middle">exit code verdict</text>

    <!-- OpenClaw: top-middle (27 矩阵给运维) -->
    <circle cx="430" cy="120" r="14" fill="#16a34a" stroke="#1e293b" stroke-width="2" />
    <text x="430" y="124" class="pin" text-anchor="middle">OC</text>
    <text x="430" y="151" class="t" text-anchor="middle">OpenClaw</text>
    <text x="430" y="166" class="t-s" text-anchor="middle">3×3×3 = 27 组合</text>
    <text x="430" y="179" class="t-s" text-anchor="middle">5-tuple binding</text>

    <!-- Claude Code: top-right (8 source + 5 mode) -->
    <circle cx="580" cy="140" r="14" fill="#7c3aed" stroke="#1e293b" stroke-width="2" />
    <text x="580" y="144" class="pin" text-anchor="middle">CC</text>
    <text x="580" y="171" class="t" text-anchor="middle">Claude Code</text>
    <text x="580" y="186" class="t-s" text-anchor="middle">5 mode × 3 behavior</text>
    <text x="580" y="199" class="t-s" text-anchor="middle">× 8 rule source</text>

    <!-- Codex: right-middle (5x5x6x5 全枚举) -->
    <circle cx="620" cy="240" r="14" fill="#2563eb" stroke="#1e293b" stroke-width="2" />
    <text x="620" y="244" class="pin" text-anchor="middle">CX</text>
    <text x="620" y="271" class="t" text-anchor="middle">Codex</text>
    <text x="620" y="286" class="t-s" text-anchor="middle">5 mode × 5 granular</text>
    <text x="620" y="299" class="t-s" text-anchor="middle">× 6 op × 5 decision</text>
  </g>

  <text x="20" y="465" class="t-s">CX = Codex · CC = Claude Code · OC = OpenClaw · HM = Hermes</text>
</svg>
"""

FLOWS_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 600" role="img"
     aria-label="四种权限决策流程并列">
  <defs>
    <filter id="wb12F"><feTurbulence type="fractalNoise" baseFrequency="0.022" numOctaves="2" seed="119" /><feDisplacementMap in="SourceGraphic" scale="1.5" /></filter>
    <marker id="ar12F" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .col  { font: 700 13px sans-serif; fill: #1e293b; }
      .lbl  { font: 700 11px sans-serif; fill: #1e293b; }
      .t-s  { font: 10.5px sans-serif; fill: #475569; }
      .note { font: italic 10.5px sans-serif; fill: #b45309; }
    </style>
  </defs>

  <text x="440" y="24" class="h" text-anchor="middle">四种权限决策流程并列</text>
  <text x="440" y="42" class="t-s" text-anchor="middle">枚举决策（Codex）· IDE 规则（Claude Code）· 3 维矩阵（OpenClaw）· 子进程 verdict（Hermes）</text>

  <g filter="url(#wb12F)">
    <!-- Codex column -->
    <text x="120" y="70" class="col" text-anchor="middle">Codex · 5×5×6×5 枚举</text>
    <rect x="40" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="103" class="lbl" text-anchor="middle">模型请求 tool_call</text>

    <line x1="120" y1="116" x2="120" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar12F)" />

    <rect x="40" y="138" width="160" height="48" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="158" class="lbl" text-anchor="middle">AskForApproval 决策</text>
    <text x="120" y="174" class="t-s" text-anchor="middle">UnlessTrusted/OnRequest/...</text>

    <line x1="120" y1="186" x2="120" y2="205" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar12F)" />

    <rect x="40" y="208" width="160" height="60" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="228" class="lbl" text-anchor="middle">GuardianAction 分类</text>
    <text x="120" y="244" class="t-s" text-anchor="middle">Command / Execve / Patch</text>
    <text x="120" y="258" class="t-s" text-anchor="middle">Network / MCP / RequestPerm</text>

    <line x1="120" y1="268" x2="120" y2="287" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar12F)" />

    <rect x="40" y="290" width="160" height="60" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="310" class="lbl" text-anchor="middle">default_available_decisions</text>
    <text x="120" y="326" class="t-s" text-anchor="middle">按 context 推按钮列表</text>
    <text x="120" y="340" class="t-s" text-anchor="middle">弹窗 UI 不写死</text>

    <line x1="120" y1="350" x2="120" y2="369" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar12F)" />

    <rect x="40" y="372" width="160" height="48" rx="8" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="392" class="lbl" text-anchor="middle">ReviewDecision 答案</text>
    <text x="120" y="408" class="t-s" text-anchor="middle">5 种：Approved/Session/...</text>

    <text x="120" y="445" class="note" text-anchor="middle">每个 turn 一个 Constrained 上限</text>
    <text x="120" y="460" class="note" text-anchor="middle">session 配置 + per-command 升级</text>

    <!-- Claude Code column -->
    <text x="330" y="70" class="col" text-anchor="middle">Claude Code · 5×3×8 规则</text>
    <rect x="250" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="103" class="lbl" text-anchor="middle">tool 想要执行</text>

    <line x1="330" y1="116" x2="330" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar12F)" />

    <rect x="250" y="138" width="160" height="60" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="158" class="lbl" text-anchor="middle">PermissionMode 路由</text>
    <text x="330" y="174" class="t-s" text-anchor="middle">default/acceptEdits/plan/...</text>
    <text x="330" y="188" class="t-s" text-anchor="middle">bypassPermissions = YOLO</text>

    <line x1="330" y1="198" x2="330" y2="217" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar12F)" />

    <rect x="250" y="220" width="160" height="60" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="240" class="lbl" text-anchor="middle">规则叠加 8 source</text>
    <text x="330" y="256" class="t-s" text-anchor="middle">user/project/local/flag</text>
    <text x="330" y="270" class="t-s" text-anchor="middle">policy/cliArg/command/session</text>

    <line x1="330" y1="280" x2="330" y2="299" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar12F)" />

    <rect x="250" y="302" width="160" height="48" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="322" class="lbl" text-anchor="middle">canUseTool 回调</text>
    <text x="330" y="338" class="t-s" text-anchor="middle">behavior: allow/deny/ask</text>

    <line x1="330" y1="350" x2="330" y2="369" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar12F)" />

    <rect x="250" y="372" width="160" height="48" rx="8" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="392" class="lbl" text-anchor="middle">弹 UI 或自动决策</text>
    <text x="330" y="408" class="t-s" text-anchor="middle">用户答案存到指定 destination</text>

    <text x="330" y="445" class="note" text-anchor="middle">toolName + ruleContent 细粒度</text>
    <text x="330" y="460" class="note" text-anchor="middle">可写 Bash(git diff) 允许、Bash(rm) 禁</text>

    <!-- OpenClaw column -->
    <text x="540" y="70" class="col" text-anchor="middle">OpenClaw · 3×3×3 = 27</text>
    <rect x="460" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="103" class="lbl" text-anchor="middle">命令请求执行</text>

    <line x1="540" y1="116" x2="540" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar12F)" />

    <rect x="460" y="138" width="160" height="72" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="158" class="lbl" text-anchor="middle">ExecHost 路由</text>
    <text x="540" y="174" class="t-s" text-anchor="middle">sandbox · gateway · node</text>
    <text x="540" y="188" class="t-s" text-anchor="middle">每种走不同执行环境</text>
    <text x="540" y="202" class="t-s" text-anchor="middle">3 种 host × 3 安全策略</text>

    <line x1="540" y1="210" x2="540" y2="229" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar12F)" />

    <rect x="460" y="232" width="160" height="60" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="252" class="lbl" text-anchor="middle">ExecSecurity 判定</text>
    <text x="540" y="268" class="t-s" text-anchor="middle">deny / allowlist / full</text>
    <text x="540" y="282" class="t-s" text-anchor="middle">+ ExecAsk: off/on-miss/always</text>

    <line x1="540" y1="292" x2="540" y2="311" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar12F)" />

    <rect x="460" y="314" width="160" height="60" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="334" class="lbl" text-anchor="middle">5-tuple binding</text>
    <text x="540" y="350" class="t-s" text-anchor="middle">argv+cwd+agentId</text>
    <text x="540" y="364" class="t-s" text-anchor="middle">+sessionKey+envHash</text>

    <line x1="540" y1="374" x2="540" y2="393" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar12F)" />

    <rect x="460" y="396" width="160" height="36" rx="8" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="419" class="lbl" text-anchor="middle">cache hit / 弹 UI</text>

    <text x="540" y="455" class="note" text-anchor="middle">envHash 防 env-swap 攻击</text>

    <!-- Hermes column -->
    <text x="760" y="70" class="col" text-anchor="middle">Hermes · tirith 子进程</text>
    <rect x="680" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="103" class="lbl" text-anchor="middle">terminal_tool 调用</text>

    <line x1="760" y1="116" x2="760" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar12F)" />

    <rect x="680" y="138" width="160" height="60" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="158" class="lbl" text-anchor="middle">spawn tirith Go binary</text>
    <text x="760" y="174" class="t-s" text-anchor="middle">5s timeout</text>
    <text x="760" y="188" class="t-s" text-anchor="middle">不在 PATH 后台下载</text>

    <line x1="760" y1="198" x2="760" y2="217" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar12F)" />

    <rect x="680" y="220" width="160" height="60" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="240" class="lbl" text-anchor="middle">exit code verdict</text>
    <text x="760" y="256" class="t-s" text-anchor="middle">0 allow · 1 block · 2 warn</text>
    <text x="760" y="270" class="t-s" text-anchor="middle">JSON stdout 丰富 findings</text>

    <line x1="760" y1="280" x2="760" y2="299" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar12F)" />

    <rect x="680" y="302" width="160" height="48" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="322" class="lbl" text-anchor="middle">fail_open 兜底</text>
    <text x="760" y="338" class="t-s" text-anchor="middle">spawn 失败 / 超时</text>

    <line x1="760" y1="350" x2="760" y2="369" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar12F)" />

    <rect x="680" y="372" width="160" height="60" rx="8" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="392" class="lbl" text-anchor="middle">供应链校验</text>
    <text x="760" y="408" class="t-s" text-anchor="middle">SHA-256 + cosign</text>
    <text x="760" y="422" class="t-s" text-anchor="middle">GitHub Actions signature</text>

    <text x="760" y="455" class="note" text-anchor="middle">没有用户介入选项</text>
  </g>

  <text x="440" y="490" class="t-s" text-anchor="middle">用户 / 运维 / 安全工具 — 谁说了算？四种回答给四种 agent 形态</text>

  <g>
    <rect x="40" y="505" width="800" height="80" rx="8" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1" />
    <text x="60" y="525" class="lbl">共同点：</text>
    <text x="60" y="543" class="t-s">· 有"模式"概念，让用户一键切换默认行为（粗粒度）</text>
    <text x="60" y="559" class="t-s">· 有缓存 / per-session 机制，用户答应过一次的不再问</text>
    <text x="60" y="575" class="t-s">· 可审操作分类（不同操作走不同 UI / 不同决策路径）</text>
  </g>
</svg>
"""


def write(slug, svg):
    out = PUBLIC / f"{slug}.svg"
    out.write_text(svg, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    PUBLIC.mkdir(parents=True, exist_ok=True)
    write("12-tradeoff", TRADEOFF_SVG)
    write("12-permission-flows", FLOWS_SVG)
