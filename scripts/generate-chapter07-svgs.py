#!/usr/bin/env python3
"""Chapter 07 SVGs: TradeOff (默认安全度 × 使用流畅度) + git push --force 四 pipeline 命运对照."""
from pathlib import Path

PUBLIC = Path("public/diagrams")

TRADEOFF_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 480" role="img"
     aria-label="四家 Shell 系统在 默认安全度 × 日常使用流畅度 两条轴上的位置">
  <defs>
    <filter id="wb07"><feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="41" /><feDisplacementMap in="SourceGraphic" scale="2" /></filter>
    <marker id="ar07" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .ax   { font: 600 12.5px sans-serif; fill: #1e293b; }
      .t    { font: 11.5px sans-serif; fill: #334155; }
      .t-s  { font: 10.5px sans-serif; fill: #64748b; }
      .pin  { font: 700 12.5px sans-serif; fill: #fff; }
      .note { font: italic 10.5px sans-serif; fill: #475569; }
    </style>
  </defs>

  <text x="390" y="26" class="h" text-anchor="middle">Shell 执行：默认安全度 × 日常使用流畅度</text>
  <text x="390" y="44" class="t-s" text-anchor="middle">默认安全度越高，往往日常每条命令都要等审批；Hermes 反其道而行，靠隔离换流畅</text>

  <g filter="url(#wb07)">
    <rect x="100" y="80" width="280" height="160" fill="#fef9c3" opacity="0.4" />
    <rect x="380" y="80" width="280" height="160" fill="#dcfce7" opacity="0.4" />
    <rect x="100" y="240" width="280" height="160" fill="#fee2e2" opacity="0.4" />
    <rect x="380" y="240" width="280" height="160" fill="#dbeafe" opacity="0.4" />

    <text x="120" y="100" class="t-s">流畅 + 默认松（最危险）</text>
    <text x="640" y="100" class="t-s" text-anchor="end">流畅 + 默认严 · 圣杯</text>
    <text x="120" y="260" class="t-s">磕磕绊绊 + 默认松</text>
    <text x="640" y="260" class="t-s" text-anchor="end">磕磕绊绊 + 默认严</text>

    <line x1="100" y1="400" x2="660" y2="400" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar07)" />
    <line x1="100" y1="400" x2="100" y2="70" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar07)" />
    <line x1="380" y1="80" x2="380" y2="400" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />
    <line x1="100" y1="240" x2="660" y2="240" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />

    <text x="660" y="420" class="ax" text-anchor="end">默认情况下能挡住多少危险命令 →</text>
    <text x="110" y="68" class="ax">↑ 日常使用流畅度（不被审批打断）</text>

    <!-- Hermes: top, slightly left of center (env isolation: medium safe + very smooth) -->
    <circle cx="350" cy="125" r="15" fill="#f97316" stroke="#1e293b" stroke-width="2" />
    <text x="350" y="129" class="pin" text-anchor="middle">HM</text>
    <text x="350" y="158" class="t" text-anchor="middle">Hermes</text>
    <text x="350" y="173" class="t-s" text-anchor="middle">7 种 TERMINAL_ENV 后端</text>
    <text x="350" y="186" class="t-s" text-anchor="middle">命令层放行 · 环境层挡</text>

    <!-- Codex: middle right (high safe + medium smooth) -->
    <circle cx="555" cy="225" r="15" fill="#2563eb" stroke="#1e293b" stroke-width="2" />
    <text x="555" y="229" class="pin" text-anchor="middle">CX</text>
    <text x="555" y="258" class="t" text-anchor="middle">Codex</text>
    <text x="555" y="273" class="t-s" text-anchor="middle">execpolicy Starlark · sandbox</text>
    <text x="555" y="286" class="t-s" text-anchor="middle">规则可 git diff</text>

    <!-- Claude Code: bottom right (very high safe + lower smooth) -->
    <circle cx="620" cy="295" r="15" fill="#7c3aed" stroke="#1e293b" stroke-width="2" />
    <text x="620" y="299" class="pin" text-anchor="middle">CC</text>
    <text x="620" y="328" class="t" text-anchor="middle">Claude Code</text>
    <text x="620" y="343" class="t-s" text-anchor="middle">23 项 ID 检查 · sandbox-default</text>
    <text x="620" y="356" class="t-s" text-anchor="middle">tree-sitter 每条命令解析</text>

    <!-- OpenClaw: right side, between Codex and Claude Code -->
    <circle cx="585" cy="345" r="15" fill="#16a34a" stroke="#1e293b" stroke-width="2" />
    <text x="585" y="349" class="pin" text-anchor="middle">OC</text>
    <text x="585" y="378" class="t" text-anchor="middle">OpenClaw</text>
    <text x="585" y="393" class="t-s" text-anchor="middle">3×3 矩阵 · safe-bin profile</text>

    <text x="245" y="290" class="note" text-anchor="middle">左上角空白</text>
    <text x="245" y="307" class="note" text-anchor="middle">"流畅+默认严" 互相挤压</text>
  </g>

  <text x="20" y="465" class="t-s">CX = Codex · CC = Claude Code · OC = OpenClaw · HM = Hermes</text>
</svg>
"""

PIPELINES_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 580" role="img"
     aria-label="一条 git push --force 在四家 Shell pipeline 里的命运">
  <defs>
    <filter id="wb07p"><feTurbulence type="fractalNoise" baseFrequency="0.022" numOctaves="2" seed="47" /><feDisplacementMap in="SourceGraphic" scale="1.5" /></filter>
    <marker id="ar07p" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .col  { font: 700 13px sans-serif; fill: #1e293b; }
      .lbl  { font: 700 11px sans-serif; fill: #1e293b; }
      .t-s  { font: 10.5px sans-serif; fill: #475569; }
      .gate { font: italic 10.5px sans-serif; fill: #b91c1c; }
    </style>
  </defs>

  <text x="410" y="24" class="h" text-anchor="middle">一条 git push --force 进四个 pipeline 的命运</text>
  <text x="410" y="42" class="t-s" text-anchor="middle">四家拦的地方完全不重叠——做自己的 shell 拦截可以挑两到三层组合</text>

  <g filter="url(#wb07p)">
    <!-- Column headers -->
    <text x="105" y="75" class="col" text-anchor="middle">Codex</text>
    <text x="305" y="75" class="col" text-anchor="middle">Claude Code</text>
    <text x="505" y="75" class="col" text-anchor="middle">OpenClaw</text>
    <text x="705" y="75" class="col" text-anchor="middle">Hermes</text>

    <line x1="200" y1="55" x2="200" y2="540" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="3 3" />
    <line x1="400" y1="55" x2="400" y2="540" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="3 3" />
    <line x1="600" y1="55" x2="600" y2="540" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="3 3" />

    <!-- Codex pipeline -->
    <rect x="35" y="90" width="140" height="42" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.5" />
    <text x="105" y="107" class="lbl" text-anchor="middle">1. shlex 分词</text>
    <text x="105" y="122" class="t-s" text-anchor="middle">["git","push","--force"]</text>

    <line x1="105" y1="132" x2="105" y2="152" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar07p)" />

    <rect x="35" y="155" width="140" height="50" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.5" />
    <text x="105" y="172" class="lbl" text-anchor="middle">2. execpolicy</text>
    <text x="105" y="187" class="t-s" text-anchor="middle">prefix_rule 命中</text>
    <text x="105" y="200" class="t-s" text-anchor="middle">→ Prompt</text>

    <line x1="105" y1="205" x2="105" y2="225" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar07p)" />

    <rect x="35" y="228" width="140" height="42" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.5" />
    <text x="105" y="245" class="lbl" text-anchor="middle">3. TUI 审批</text>
    <text x="105" y="260" class="t-s" text-anchor="middle">justification 弹窗</text>

    <line x1="105" y1="270" x2="105" y2="290" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar07p)" />

    <rect x="35" y="293" width="140" height="50" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.5" />
    <text x="105" y="310" class="lbl" text-anchor="middle">4. sandbox_mode</text>
    <text x="105" y="325" class="t-s" text-anchor="middle">workspace-write?</text>
    <text x="105" y="338" class="t-s" text-anchor="middle">Landlock + seccomp</text>

    <line x1="105" y1="343" x2="105" y2="363" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar07p)" />

    <rect x="35" y="366" width="140" height="36" rx="8" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.5" />
    <text x="105" y="389" class="lbl" text-anchor="middle">5. fork + exec</text>

    <!-- Claude Code pipeline -->
    <rect x="235" y="90" width="140" height="42" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.5" />
    <text x="305" y="107" class="lbl" text-anchor="middle">1. tree-sitter</text>
    <text x="305" y="122" class="t-s" text-anchor="middle">+ shell-quote 双解析</text>

    <line x1="305" y1="132" x2="305" y2="152" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar07p)" />

    <rect x="235" y="155" width="140" height="50" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.5" />
    <text x="305" y="172" class="lbl" text-anchor="middle">2. 23 项安全 ID</text>
    <text x="305" y="187" class="t-s" text-anchor="middle">#5 metachars · #8 cmdsub</text>
    <text x="305" y="200" class="t-s" text-anchor="middle">#20 ZSH_DANGEROUS</text>

    <line x1="305" y1="205" x2="305" y2="225" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar07p)" />

    <rect x="235" y="228" width="140" height="42" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.5" />
    <text x="305" y="245" class="lbl" text-anchor="middle">3. bashPermission</text>
    <text x="305" y="260" class="t-s" text-anchor="middle">prefix / exact / wildcard</text>

    <line x1="305" y1="270" x2="305" y2="290" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar07p)" />

    <rect x="235" y="293" width="140" height="42" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.5" />
    <text x="305" y="310" class="lbl" text-anchor="middle">4. permission mode</text>
    <text x="305" y="325" class="t-s" text-anchor="middle">+ canUseTool hook</text>

    <line x1="305" y1="335" x2="305" y2="355" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar07p)" />

    <rect x="235" y="358" width="140" height="50" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.5" />
    <text x="305" y="375" class="lbl" text-anchor="middle">5. SandboxManager</text>
    <text x="305" y="390" class="t-s" text-anchor="middle">sandbox-exec /</text>
    <text x="305" y="403" class="t-s" text-anchor="middle">bubblewrap</text>

    <line x1="305" y1="408" x2="305" y2="428" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar07p)" />

    <rect x="235" y="431" width="140" height="36" rx="8" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.5" />
    <text x="305" y="454" class="lbl" text-anchor="middle">6. fork</text>

    <!-- OpenClaw pipeline -->
    <rect x="435" y="90" width="140" height="42" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.5" />
    <text x="505" y="107" class="lbl" text-anchor="middle">1. splitCommand</text>
    <text x="505" y="122" class="t-s" text-anchor="middle">+ obfuscation-detect</text>

    <line x1="505" y1="132" x2="505" y2="152" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar07p)" />

    <rect x="435" y="155" width="140" height="50" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.5" />
    <text x="505" y="172" class="lbl" text-anchor="middle">2. security 模式?</text>
    <text x="505" y="187" class="gate" text-anchor="middle">deny → 拒</text>
    <text x="505" y="200" class="t-s" text-anchor="middle">allowlist? full?</text>

    <line x1="505" y1="205" x2="505" y2="225" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar07p)" />

    <rect x="435" y="228" width="140" height="50" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.5" />
    <text x="505" y="245" class="lbl" text-anchor="middle">3. safe-bin profile</text>
    <text x="505" y="260" class="t-s" text-anchor="middle">git --force 黑名单?</text>
    <text x="505" y="273" class="t-s" text-anchor="middle">GNU long-flag 缩写</text>

    <line x1="505" y1="278" x2="505" y2="298" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar07p)" />

    <rect x="435" y="301" width="140" height="42" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.5" />
    <text x="505" y="318" class="lbl" text-anchor="middle">4. ask 模式?</text>
    <text x="505" y="333" class="t-s" text-anchor="middle">JSONL → UI / Discord</text>

    <line x1="505" y1="343" x2="505" y2="363" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar07p)" />

    <rect x="435" y="366" width="140" height="42" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.5" />
    <text x="505" y="383" class="lbl" text-anchor="middle">5. ExecHost?</text>
    <text x="505" y="398" class="t-s" text-anchor="middle">sandbox / gateway / node</text>

    <line x1="505" y1="408" x2="505" y2="428" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar07p)" />

    <rect x="435" y="431" width="140" height="36" rx="8" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.5" />
    <text x="505" y="454" class="lbl" text-anchor="middle">6. spawn</text>

    <!-- Hermes pipeline -->
    <rect x="635" y="90" width="140" height="42" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.5" />
    <text x="705" y="107" class="lbl" text-anchor="middle">1. workdir 校验</text>
    <text x="705" y="122" class="t-s" text-anchor="middle">字符 allowlist 正则</text>

    <line x1="705" y1="132" x2="705" y2="152" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar07p)" />

    <rect x="635" y="155" width="140" height="50" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.5" />
    <text x="705" y="172" class="lbl" text-anchor="middle">2. _check_all_guards</text>
    <text x="705" y="187" class="t-s" text-anchor="middle">tirith 危险命令</text>
    <text x="705" y="200" class="t-s" text-anchor="middle">+ approval_callback</text>

    <line x1="705" y1="205" x2="705" y2="225" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar07p)" />

    <rect x="635" y="228" width="140" height="42" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.5" />
    <text x="705" y="245" class="lbl" text-anchor="middle">3. 决策</text>
    <text x="705" y="260" class="t-s" text-anchor="middle">once / session / always / deny</text>

    <line x1="705" y1="270" x2="705" y2="290" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar07p)" />

    <rect x="635" y="293" width="140" height="50" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.5" />
    <text x="705" y="310" class="lbl" text-anchor="middle">4. TERMINAL_ENV?</text>
    <text x="705" y="325" class="t-s" text-anchor="middle">local / docker / modal</text>
    <text x="705" y="338" class="t-s" text-anchor="middle">ssh / singularity / daytona</text>

    <line x1="705" y1="343" x2="705" y2="363" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar07p)" />

    <rect x="635" y="366" width="140" height="42" rx="8" fill="#e2e8f0" stroke="#1e293b" stroke-width="1.5" />
    <text x="705" y="383" class="lbl" text-anchor="middle">5. 选定后端 run</text>
    <text x="705" y="398" class="t-s" text-anchor="middle">docker run / modal sandbox</text>
  </g>

  <text x="20" y="510" class="t-s">关键差别：</text>
  <text x="20" y="528" class="t-s">· Codex 把决策外置成 Starlark DSL，规则 git 化 · Claude Code 在 bash 解析层穷举 23 类风险 pattern</text>
  <text x="20" y="546" class="t-s">· OpenClaw 走 security × ask 矩阵 + per-binary safe-bin profile · Hermes 不挡命令本体，挡执行环境</text>
  <text x="20" y="564" class="t-s">做自己的 shell 拦截系统：从 allowlist 起步，按需加 DSL（Codex 风）、深度解析（Claude Code 风）、执行隔离（Hermes 风）</text>
</svg>
"""

def write(slug, svg):
    out = PUBLIC / f"{slug}.svg"
    out.write_text(svg, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size} bytes)")

if __name__ == "__main__":
    PUBLIC.mkdir(parents=True, exist_ok=True)
    write("07-tradeoff", TRADEOFF_SVG)
    write("07-pipelines", PIPELINES_SVG)
