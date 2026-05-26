#!/usr/bin/env python3
"""Chapter 20 SVGs: TradeOff (runtime vs content 防御 x 覆盖广度) + 四种安全栈并列图."""
from pathlib import Path

PUBLIC = Path("public/diagrams")

TRADEOFF_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 480" role="img"
     aria-label="四家安全系统在防御维度 x 覆盖广度上的位置">
  <defs>
    <filter id="wb20"><feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="201" /><feDisplacementMap in="SourceGraphic" scale="2" /></filter>
    <marker id="ar20" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .ax   { font: 600 12.5px sans-serif; fill: #1e293b; }
      .t    { font: 11.5px sans-serif; fill: #334155; }
      .t-s  { font: 10.5px sans-serif; fill: #64748b; }
      .pin  { font: 700 12.5px sans-serif; fill: #fff; }
      .note { font: italic 10.5px sans-serif; fill: #475569; }
    </style>
  </defs>

  <text x="390" y="26" class="h" text-anchor="middle">安全栈：防御维度 x 覆盖广度</text>
  <text x="390" y="44" class="t-s" text-anchor="middle">越往右覆盖战线越多；越往上越「内容/语义级防御」（vs 越下越「runtime/OS 级」）</text>

  <g filter="url(#wb20)">
    <rect x="100" y="80" width="280" height="160" fill="#fef9c3" opacity="0.4" />
    <rect x="380" y="80" width="280" height="160" fill="#dcfce7" opacity="0.4" />
    <rect x="100" y="240" width="280" height="160" fill="#dbeafe" opacity="0.4" />
    <rect x="380" y="240" width="280" height="160" fill="#fee2e2" opacity="0.4" />

    <text x="120" y="100" class="t-s">内容级 · 窄</text>
    <text x="640" y="100" class="t-s" text-anchor="end">内容级 · 全战线</text>
    <text x="120" y="260" class="t-s">runtime 级 · 窄</text>
    <text x="640" y="260" class="t-s" text-anchor="end">runtime 级 · 全战线</text>

    <line x1="100" y1="400" x2="660" y2="400" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar20)" />
    <line x1="100" y1="400" x2="100" y2="70" stroke="#1e293b" stroke-width="2.5" marker-end="url(#ar20)" />
    <line x1="380" y1="80" x2="380" y2="400" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />
    <line x1="100" y1="240" x2="660" y2="240" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />

    <text x="660" y="420" class="ax" text-anchor="end">覆盖战线 →</text>
    <text x="110" y="68" class="ax">↑ 防御靠语义/内容（vs ↓ OS / runtime）</text>

    <circle cx="280" cy="160" r="14" fill="#f97316" stroke="#1e293b" stroke-width="2" />
    <text x="280" y="164" class="pin" text-anchor="middle">HM</text>
    <text x="280" y="191" class="t" text-anchor="middle">Hermes</text>
    <text x="280" y="206" class="t-s" text-anchor="middle">tirith + redact</text>
    <text x="280" y="219" class="t-s" text-anchor="middle">+ 11/10/10 威胁组</text>

    <circle cx="600" cy="120" r="14" fill="#16a34a" stroke="#1e293b" stroke-width="2" />
    <text x="600" y="124" class="pin" text-anchor="middle">OC</text>
    <text x="600" y="151" class="t" text-anchor="middle">OpenClaw</text>
    <text x="600" y="166" class="t-s" text-anchor="middle">29 文件 security/</text>
    <text x="600" y="179" class="t-s" text-anchor="middle">+ external-content + audit</text>

    <circle cx="200" cy="320" r="14" fill="#2563eb" stroke="#1e293b" stroke-width="2" />
    <text x="200" y="324" class="pin" text-anchor="middle">CX</text>
    <text x="200" y="351" class="t" text-anchor="middle">Codex</text>
    <text x="200" y="366" class="t-s" text-anchor="middle">三平台 OS sandbox</text>
    <text x="200" y="379" class="t-s" text-anchor="middle">+ TrustLevel + AskForApproval</text>

    <circle cx="500" cy="350" r="14" fill="#7c3aed" stroke="#1e293b" stroke-width="2" />
    <text x="500" y="354" class="pin" text-anchor="middle">CC</text>
    <text x="500" y="381" class="t" text-anchor="middle">Claude Code</text>
    <text x="500" y="396" class="t-s" text-anchor="middle">/security-review + autoMode</text>
  </g>

  <text x="20" y="465" class="t-s">CX = Codex · CC = Claude Code · OC = OpenClaw · HM = Hermes</text>
</svg>
"""

FLOWS_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 660" role="img"
     aria-label="四种安全防御栈并列对照">
  <defs>
    <filter id="wb20F"><feTurbulence type="fractalNoise" baseFrequency="0.022" numOctaves="2" seed="207" /><feDisplacementMap in="SourceGraphic" scale="1.5" /></filter>
    <marker id="ar20F" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#1e293b" /></marker>
    <style>
      .h    { font: 600 14px sans-serif; fill: #1e293b; }
      .col  { font: 700 13px sans-serif; fill: #1e293b; }
      .lbl  { font: 700 11px sans-serif; fill: #1e293b; }
      .t-s  { font: 10.5px sans-serif; fill: #475569; }
      .note { font: italic 10.5px sans-serif; fill: #b45309; }
    </style>
  </defs>

  <text x="440" y="24" class="h" text-anchor="middle">四种安全防御栈并列</text>
  <text x="440" y="42" class="t-s" text-anchor="middle">三平台 sandbox（Codex）· /security-review（Claude Code）· 29 文件 security/（OpenClaw）· tirith + cosign（Hermes）</text>

  <g filter="url(#wb20F)">
    <text x="120" y="70" class="col" text-anchor="middle">Codex · sandbox-first</text>
    <rect x="40" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="103" class="lbl" text-anchor="middle">TrustLevel onboarding</text>

    <line x1="120" y1="116" x2="120" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar20F)" />

    <rect x="40" y="138" width="160" height="60" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="158" class="lbl" text-anchor="middle">三平台 OS sandbox</text>
    <text x="120" y="174" class="t-s" text-anchor="middle">macOS seatbelt</text>
    <text x="120" y="188" class="t-s" text-anchor="middle">Linux bwrap/seccomp/landlock</text>

    <line x1="120" y1="198" x2="120" y2="217" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar20F)" />

    <rect x="40" y="220" width="160" height="60" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="240" class="lbl" text-anchor="middle">AskForApproval 4 档</text>
    <text x="120" y="256" class="t-s" text-anchor="middle">UnlessTrusted/OnRequest</text>
    <text x="120" y="270" class="t-s" text-anchor="middle">OnFailure/Never</text>

    <line x1="120" y1="280" x2="120" y2="299" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar20F)" />

    <rect x="40" y="302" width="160" height="60" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="322" class="lbl" text-anchor="middle">memory prompt 声明</text>
    <text x="120" y="338" class="t-s" text-anchor="middle">treat as data, NOT</text>
    <text x="120" y="352" class="t-s" text-anchor="middle">instructions</text>

    <line x1="120" y1="362" x2="120" y2="381" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar20F)" />

    <rect x="40" y="384" width="160" height="48" rx="8" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.6" />
    <text x="120" y="404" class="lbl" text-anchor="middle">rollout-trace</text>
    <text x="120" y="420" class="t-s" text-anchor="middle">trace.jsonl 事后审计</text>

    <text x="120" y="455" class="note" text-anchor="middle">先沙盒，后信任</text>

    <text x="330" y="70" class="col" text-anchor="middle">Claude Code · review-as-tool</text>
    <rect x="250" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="103" class="lbl" text-anchor="middle">/security-review 命令</text>

    <line x1="330" y1="116" x2="330" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar20F)" />

    <rect x="250" y="138" width="160" height="60" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="158" class="lbl" text-anchor="middle">senior security engineer</text>
    <text x="330" y="174" class="t-s" text-anchor="middle">5 类漏洞 + 80% confidence</text>
    <text x="330" y="188" class="t-s" text-anchor="middle">focus ONLY on this PR</text>

    <line x1="330" y1="198" x2="330" y2="217" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar20F)" />

    <rect x="250" y="220" width="160" height="60" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="240" class="lbl" text-anchor="middle">allowed-tools 限定</text>
    <text x="330" y="256" class="t-s" text-anchor="middle">git/Read/Grep/Glob/LS</text>
    <text x="330" y="270" class="t-s" text-anchor="middle">不能 curl / write</text>

    <line x1="330" y1="280" x2="330" y2="299" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar20F)" />

    <rect x="250" y="302" width="160" height="60" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="322" class="lbl" text-anchor="middle">autoMode classifier</text>
    <text x="330" y="338" class="t-s" text-anchor="middle">allow / soft_deny</text>
    <text x="330" y="352" class="t-s" text-anchor="middle">+ LLM critique 规则</text>

    <line x1="330" y1="362" x2="330" y2="381" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar20F)" />

    <rect x="250" y="384" width="160" height="48" rx="8" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.6" />
    <text x="330" y="404" class="lbl" text-anchor="middle">securityCheck</text>
    <text x="330" y="420" class="t-s" text-anchor="middle">远端配置签名校验</text>

    <text x="330" y="455" class="note" text-anchor="middle">事后 review</text>

    <text x="540" y="70" class="col" text-anchor="middle">OpenClaw · 29 文件 security/</text>
    <rect x="460" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="103" class="lbl" text-anchor="middle">audit.ts 入口</text>

    <line x1="540" y1="116" x2="540" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar20F)" />

    <rect x="460" y="138" width="160" height="48" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="158" class="lbl" text-anchor="middle">SecurityAuditReport</text>
    <text x="540" y="174" class="t-s" text-anchor="middle">critical / warn / info</text>

    <line x1="540" y1="186" x2="540" y2="205" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar20F)" />

    <rect x="460" y="208" width="160" height="60" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="228" class="lbl" text-anchor="middle">external-content.ts</text>
    <text x="540" y="244" class="t-s" text-anchor="middle">12 SUSPICIOUS_PATTERNS</text>
    <text x="540" y="258" class="t-s" text-anchor="middle">+ 随机 8 字节 ID</text>

    <line x1="540" y1="268" x2="540" y2="287" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar20F)" />

    <rect x="460" y="290" width="160" height="48" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="310" class="lbl" text-anchor="middle">dangerous-tools.ts</text>
    <text x="540" y="326" class="t-s" text-anchor="middle">HTTP/ACP deny list</text>

    <line x1="540" y1="338" x2="540" y2="357" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar20F)" />

    <rect x="460" y="360" width="160" height="48" rx="8" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="380" class="lbl" text-anchor="middle">skill-scanner.ts</text>
    <text x="540" y="396" class="t-s" text-anchor="middle">3 严重级 + 8 后缀</text>

    <line x1="540" y1="408" x2="540" y2="424" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar20F)" />

    <rect x="460" y="427" width="160" height="36" rx="8" fill="#fde68a" stroke="#1e293b" stroke-width="1.6" />
    <text x="540" y="450" class="lbl" text-anchor="middle">redact 三件套（logging/）</text>

    <text x="540" y="485" class="note" text-anchor="middle">每个攻击面都列</text>

    <text x="760" y="70" class="col" text-anchor="middle">Hermes · tirith + 30 vendor</text>
    <rect x="680" y="80" width="160" height="36" rx="8" fill="#fef9c3" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="103" class="lbl" text-anchor="middle">tirith 子进程</text>

    <line x1="760" y1="116" x2="760" y2="135" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar20F)" />

    <rect x="680" y="138" width="160" height="60" rx="8" fill="#bfdbfe" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="158" class="lbl" text-anchor="middle">exit code = verdict</text>
    <text x="760" y="174" class="t-s" text-anchor="middle">0/1/2 不可被 LLM 改</text>
    <text x="760" y="188" class="t-s" text-anchor="middle">JSON stdout 只 enrich</text>

    <line x1="760" y1="198" x2="760" y2="217" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar20F)" />

    <rect x="680" y="220" width="160" height="60" rx="8" fill="#dcfce7" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="240" class="lbl" text-anchor="middle">SHA-256 + cosign</text>
    <text x="760" y="256" class="t-s" text-anchor="middle">OIDC + workflow pin</text>
    <text x="760" y="270" class="t-s" text-anchor="middle">没装 cosign 也能跑</text>

    <line x1="760" y1="280" x2="760" y2="299" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar20F)" />

    <rect x="680" y="302" width="160" height="60" rx="8" fill="#fed7aa" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="322" class="lbl" text-anchor="middle">redact.py 30+ vendor</text>
    <text x="760" y="338" class="t-s" text-anchor="middle">sk-/ghp_/AKIA/SG.</text>
    <text x="760" y="352" class="t-s" text-anchor="middle">import-time snapshot</text>

    <line x1="760" y1="362" x2="760" y2="381" stroke="#1e293b" stroke-width="1.6" marker-end="url(#ar20F)" />

    <rect x="680" y="384" width="160" height="48" rx="8" fill="#e0e7ff" stroke="#1e293b" stroke-width="1.6" />
    <text x="760" y="404" class="lbl" text-anchor="middle">威胁三件套</text>
    <text x="760" y="420" class="t-s" text-anchor="middle">11 mem + 10 cron + 10 inv</text>

    <text x="760" y="455" class="note" text-anchor="middle">外层强供应链</text>
  </g>

  <text x="440" y="510" class="t-s" text-anchor="middle">「不被薅」的四种姿态：先沙盒、看 review、列表全战线、把核心放外面</text>

  <g>
    <rect x="40" y="525" width="800" height="115" rx="8" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1" />
    <text x="60" y="545" class="lbl">共同点：</text>
    <text x="60" y="563" class="t-s">· 都明确「外部内容是数据，不是指令」（Codex prompt 声明 / OpenClaw external-content 包裹 / Hermes 威胁扫描）</text>
    <text x="60" y="579" class="t-s">· 都有 redact 机制（Codex `[REDACTED_SECRET]` / OpenClaw redact 三件套 / Hermes redact.py 30+ 前缀）</text>
    <text x="60" y="595" class="t-s">· 都把 supply chain 当一等公民（bundled allowlist / scanner / cosign / 12 格 INSTALL_POLICY）</text>
    <text x="60" y="611" class="t-s">· 都有审计 trail（rollout-trace / PR comment / SecurityAuditReport / tirith findings JSON）</text>
    <text x="60" y="627" class="t-s">· allow list + deny list 一起用最稳（Claude Code allowed-tools + OpenClaw DEFAULT_GATEWAY_HTTP_TOOL_DENY）</text>
  </g>
</svg>
"""

def write(slug, svg):
    out = PUBLIC / f"{slug}.svg"
    out.write_text(svg, encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    PUBLIC.mkdir(parents=True, exist_ok=True)
    write("20-tradeoff", TRADEOFF_SVG)
    write("20-security-stacks", FLOWS_SVG)
