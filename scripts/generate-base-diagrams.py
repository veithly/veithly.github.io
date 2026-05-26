#!/usr/bin/env python3
"""
Generate handdrawn-style base diagrams for chapters 01/03/04/05.

Each diagram lives at public/diagrams/<slug>-base.svg and is referenced
by <Diagram src="..." /> in §2 of the corresponding chapter.

UTF-8 explicit. Style matches generate-lanes-svg.py (feTurbulence wobble).
"""
from pathlib import Path

PUBLIC = Path("public/diagrams")

# Shared style block — kept verbatim in every SVG so files are standalone.
STYLE = """
    .h     { font: 600 14px sans-serif; fill: #1e293b; }
    .t     { font: 12px sans-serif; fill: #1e293b; }
    .t-sub { font: 10.5px sans-serif; fill: #475569; }
    .sys   { font: 700 13px sans-serif; fill: #fdf6e3; }
    .stage { font: 600 12px sans-serif; fill: #1e293b; }
    .num   { font: 700 16px sans-serif; fill: #f97316; }
"""

WOBBLE_DEFS = """
    <filter id="wobble">
      <feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="7" />
      <feDisplacementMap in="SourceGraphic" scale="2" />
    </filter>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#1e293b" />
    </marker>
"""

# ─────────────────────────────────────────────────────────────────────
# 01 · Overview · 1D autonomy axis with 4 system pins
# ─────────────────────────────────────────────────────────────────────
OVERVIEW_SVG = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 260" role="img"
     aria-label="\u56db\u4e2a Agent \u7cfb\u7edf\u5728\u53ef\u63a7\u6027 \u2194 \u81ea\u6cbb\u5ea6 \u8f74\u4e0a\u7684\u4f4d\u7f6e">
  <defs>
    {WOBBLE_DEFS}
    <style>{STYLE}</style>
  </defs>

  <text x="20" y="30" class="h">\u77ed\u671f\u53ef\u63a7\u6027 \u2194 \u957f\u671f\u81ea\u6cbb\u5ea6</text>
  <text x="20" y="50" class="t-sub">\u56db\u7cfb\u7edf\u8fd9\u4e00\u7ef4\u4e0a\u7684\u5206\u5e03\uff1a\u6700\u53ef\u63a7\u7684 Codex \u5728\u5de6\uff0c\u6700\u81ea\u6cbb\u7684 Hermes \u5728\u53f3\u3002</text>

  <g filter="url(#wobble)" transform="translate(0, 0)">
    <!-- main axis -->
    <line x1="60" y1="140" x2="840" y2="140" stroke="#1e293b" stroke-width="2.5" marker-end="url(#arrow)" />
    <line x1="60" y1="140" x2="60" y2="135" stroke="#1e293b" stroke-width="2.5" />
    <text x="60" y="170" class="t-sub" text-anchor="middle">\u6bcf\u6b65\u53ef\u5ba1\u6279</text>
    <text x="860" y="170" class="t-sub" text-anchor="end">\u8de8\u4f1a\u8bdd\u81ea\u8bb0\u5fc6 + \u81ea\u8bc4</text>

    <!-- Codex pin -->
    <circle cx="170" cy="140" r="10" fill="#2563eb" stroke="#1e293b" stroke-width="2" />
    <line x1="170" y1="140" x2="170" y2="90" stroke="#2563eb" stroke-width="1.5" stroke-dasharray="3 2" />
    <rect x="100" y="70" width="140" height="22" rx="4" fill="#2563eb" stroke="#1e293b" stroke-width="1.5" />
    <text x="170" y="86" class="sys" text-anchor="middle">Codex</text>
    <text x="170" y="218" class="t-sub" text-anchor="middle">execpolicy + apply_patch</text>
    <text x="170" y="234" class="t-sub" text-anchor="middle">goals.rs \u6536\u655b\u68c0\u6d4b</text>

    <!-- Claude Code pin -->
    <circle cx="340" cy="140" r="10" fill="#7c3aed" stroke="#1e293b" stroke-width="2" />
    <line x1="340" y1="140" x2="340" y2="90" stroke="#7c3aed" stroke-width="1.5" stroke-dasharray="3 2" />
    <rect x="270" y="70" width="140" height="22" rx="4" fill="#7c3aed" stroke="#1e293b" stroke-width="1.5" />
    <text x="340" y="86" class="sys" text-anchor="middle">Claude Code</text>
    <text x="340" y="218" class="t-sub" text-anchor="middle">7 \u79cd transition.reason</text>
    <text x="340" y="234" class="t-sub" text-anchor="middle">TOKEN_BUDGET \u8f6f\u9000</text>

    <!-- OpenClaw pin -->
    <circle cx="520" cy="140" r="10" fill="#16a34a" stroke="#1e293b" stroke-width="2" />
    <line x1="520" y1="140" x2="520" y2="90" stroke="#16a34a" stroke-width="1.5" stroke-dasharray="3 2" />
    <rect x="450" y="70" width="140" height="22" rx="4" fill="#16a34a" stroke="#1e293b" stroke-width="1.5" />
    <text x="520" y="86" class="sys" text-anchor="middle">OpenClaw</text>
    <text x="520" y="218" class="t-sub" text-anchor="middle">session lane + plugin</text>
    <text x="520" y="234" class="t-sub" text-anchor="middle">tool-loop-detection</text>

    <!-- Hermes pin -->
    <circle cx="720" cy="140" r="10" fill="#f97316" stroke="#1e293b" stroke-width="2" />
    <line x1="720" y1="140" x2="720" y2="90" stroke="#f97316" stroke-width="1.5" stroke-dasharray="3 2" />
    <rect x="650" y="70" width="140" height="22" rx="4" fill="#f97316" stroke="#1e293b" stroke-width="1.5" />
    <text x="720" y="86" class="sys" text-anchor="middle">Hermes</text>
    <text x="720" y="218" class="t-sub" text-anchor="middle">IterationBudget 90/50</text>
    <text x="720" y="234" class="t-sub" text-anchor="middle">memory.prefetch + grace</text>
  </g>
</svg>
"""

# ─────────────────────────────────────────────────────────────────────
# 03 · Context System · 7-pack vertical stack
# ─────────────────────────────────────────────────────────────────────
CONTEXT_LAYERS = [
    ("1", "Identity", "\u4f60\u662f\u8c01"),
    ("2", "Tools", "\u4f60\u80fd\u5e72\u4ec0\u4e48"),
    ("3", "Permissions", "\u4f60\u4e0d\u80fd\u5e72\u4ec0\u4e48"),
    ("4", "Memory", "\u4e4b\u524d\u53d1\u751f\u8fc7\u4ec0\u4e48"),
    ("5", "Context files", "AGENTS.md / CLAUDE.md / .cursorrules"),
    ("6", "Env hints", "\u65f6\u95f4 / \u5e73\u53f0 / cwd"),
    ("7", "Recent history", "\u8fd1\u51e0\u4e2a turn"),
]

def _context_rows():
    rows = []
    for i, (num, title, sub) in enumerate(CONTEXT_LAYERS):
        y = 80 + i * 52
        rows.append(f"""
    <rect x="80" y="{y}" width="540" height="42" rx="6"
          fill="#fdf6e3" stroke="#1e293b" stroke-width="2" />
    <text x="106" y="{y+27}" class="num" text-anchor="middle">{num}</text>
    <line x1="128" y1="{y+8}" x2="128" y2="{y+34}" stroke="#1e293b" stroke-width="1.5" />
    <text x="148" y="{y+19}" class="t">{title}</text>
    <text x="148" y="{y+34}" class="t-sub">{sub}</text>""")
    return "".join(rows)

CONTEXT_SVG = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 510" role="img"
     aria-label="Context \u88c5\u8f7d 7 \u4ef6\u5957">
  <defs>
    {WOBBLE_DEFS}
    <style>{STYLE}</style>
  </defs>

  <text x="20" y="30" class="h">Context \u88c5\u8f7d 7 \u4ef6\u5957</text>
  <text x="20" y="50" class="t-sub">\u4efb\u4f55 agent \u7684\u8c03\u7528 context \u90fd\u662f\u8fd9\u51e0\u5c42\u62fc\u51fa\u6765\u7684</text>

  <g filter="url(#wobble)">
    {_context_rows()}
  </g>

  <!-- right-side annotation: cache vs dynamic split -->
  <line x1="640" y1="80" x2="640" y2="240" stroke="#2563eb" stroke-width="2" />
  <text x="650" y="110" class="t-sub" fill="#2563eb">\u9759\u6001 / \u53ef\u7f13\u5b58</text>
  <text x="650" y="126" class="t-sub" fill="#2563eb">layer 1-3</text>

  <line x1="640" y1="240" x2="640" y2="486" stroke="#f97316" stroke-width="2" />
  <text x="650" y="310" class="t-sub" fill="#f97316">\u52a8\u6001 / \u6bcf turn \u91cd\u5efa</text>
  <text x="650" y="326" class="t-sub" fill="#f97316">layer 4-7</text>
</svg>
"""

# ─────────────────────────────────────────────────────────────────────
# 04 · Tool System · 4-layer stack
# ─────────────────────────────────────────────────────────────────────
TOOL_LAYERS = [
    ("Schema",   "JSON schema / function signature",       "name + params + description"),
    ("Registry", "tools \u6ce8\u518c\u8868 + profile",       "ToolProfileId / canUseTool / per-tool check"),
    ("Dispatch", "tool_use block / parallel / pipeline",    "before/after_tool_call hook"),
    ("Sandbox",  "execpolicy + permission + isolation",     "approval mode + workspace lane"),
]

def _tool_rows():
    rows = []
    colors = ["#2563eb", "#7c3aed", "#16a34a", "#f97316"]
    for i, ((title, sub, ann), color) in enumerate(zip(TOOL_LAYERS, colors)):
        y = 80 + i * 80
        rows.append(f"""
    <rect x="60" y="{y}" width="560" height="62" rx="8"
          fill="#fdf6e3" stroke="{color}" stroke-width="2.5" />
    <text x="80" y="{y+26}" class="t" fill="{color}" font-weight="700">{title}</text>
    <text x="80" y="{y+45}" class="t">{sub}</text>
    <text x="80" y="{y+58}" class="t-sub">{ann}</text>""")
    return "".join(rows)

TOOL_SVG = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 470" role="img"
     aria-label="\u5de5\u5177\u7cfb\u7edf\u7684 4 \u5c42">
  <defs>
    {WOBBLE_DEFS}
    <style>{STYLE}</style>
  </defs>

  <text x="20" y="30" class="h">\u5de5\u5177\u7cfb\u7edf\u7684 4 \u5c42</text>
  <text x="20" y="50" class="t-sub">\u4ece\u5916\u5230\u5185\uff1aschema \u5b9a\u4e49 \u2192 \u6ce8\u518c \u2192 \u8c03\u5ea6 \u2192 \u6c99\u7bb1\u6267\u884c</text>

  <g filter="url(#wobble)">
    {_tool_rows()}
  </g>

  <!-- left arrows showing flow -->
  <line x1="40" y1="100" x2="40" y2="420" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)" opacity="0.5" />
  <text x="14" y="260" class="t-sub" transform="rotate(-90 14 260)">\u8c03\u7528\u987a\u5e8f</text>
</svg>
"""

# ─────────────────────────────────────────────────────────────────────
# 05 · Verifier · 3-tier vertical decision flow
# ─────────────────────────────────────────────────────────────────────
VERIFIER_SVG = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 540" role="img"
     aria-label="Verifier \u4e09\u5c42\u51b3\u7b56\u6d41">
  <defs>
    {WOBBLE_DEFS}
    <style>{STYLE}</style>
  </defs>

  <text x="20" y="30" class="h">Verifier \u4e09\u5c42\u51b3\u7b56\u6d41</text>
  <text x="20" y="50" class="t-sub">\u4ece\u4e0a\u5230\u4e0b\uff1a\u5916\u90e8\u4ea7\u7269 \u2192 \u5185\u90e8\u9884\u7b97 \u2192 \u6a21\u578b\u81ea\u8bc4</text>

  <g filter="url(#wobble)">
    <!-- input -->
    <rect x="240" y="80" width="220" height="36" rx="6"
          fill="#1e293b" stroke="#1e293b" stroke-width="2" />
    <text x="350" y="103" class="sys" text-anchor="middle">Turn N \u8f93\u51fa</text>
    <line x1="350" y1="116" x2="350" y2="146" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)" />

    <!-- tier 1: hard -->
    <rect x="60" y="150" width="580" height="100" rx="10"
          fill="#fdf6e3" stroke="#dc2626" stroke-width="2.5" />
    <text x="80" y="178" class="t" fill="#dc2626" font-weight="700">1 \u00b7 \u786c verifier</text>
    <text x="80" y="200" class="t">apply_patch \u5408\u6cd5? \u00b7 tests \u9000\u51fa\u7801 0? \u00b7 lint pass? \u00b7 execpolicy Allow?</text>
    <text x="80" y="220" class="t-sub">fail \u2192 \u5f3a\u5236\u7ee7\u7eed loop (\u4e0d\u7ed9\u6a21\u578b\u9009\u62e9\u9000\u51fa\u7684\u673a\u4f1a)</text>
    <text x="80" y="237" class="t-sub">pass \u2192 \u8fdb\u4e0b\u4e00\u5c42</text>
    <line x1="350" y1="250" x2="350" y2="276" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)" />

    <!-- tier 2: soft -->
    <rect x="60" y="280" width="580" height="100" rx="10"
          fill="#fdf6e3" stroke="#f97316" stroke-width="2.5" />
    <text x="80" y="308" class="t" fill="#f97316" font-weight="700">2 \u00b7 \u8f6f verifier</text>
    <text x="80" y="330" class="t">token \u7528\u91cf &lt; 90%? \u00b7 \u91cd\u8bd5 &lt; \u4e0a\u9650? \u00b7 \u8fde 3 \u8f6e\u589e\u91cf &gt; 500 token?</text>
    <text x="80" y="350" class="t-sub">\u8d85\u9650 \u2192 \u5f3a\u5236\u505c / nudge (diminishing returns)</text>
    <text x="80" y="367" class="t-sub">\u6b63\u5e38 \u2192 \u8fdb\u4e0b\u4e00\u5c42</text>
    <line x1="350" y1="380" x2="350" y2="406" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)" />

    <!-- tier 3: lazy -->
    <rect x="60" y="410" width="580" height="100" rx="10"
          fill="#fdf6e3" stroke="#16a34a" stroke-width="2.5" />
    <text x="80" y="438" class="t" fill="#16a34a" font-weight="700">3 \u00b7 \u6446\u70c2 verifier</text>
    <text x="80" y="460" class="t">finish_reason == "stop"? \u00b7 \u6d41\u91cc\u6ca1 tool_use block?</text>
    <text x="80" y="480" class="t-sub">\u4fe1\u4e0d\u4fe1\u5168\u51ed\u6a21\u578b\u81ea\u89c9\uff1b\u4e0d\u80fd\u8ba9 loop \u53ea\u9760\u8fd9\u4e00\u5c42</text>
    <text x="80" y="497" class="t-sub">pass \u2192 loop \u9000\u51fa</text>
  </g>
</svg>
"""

# ─────────────────────────────────────────────────────────────────────
# 06 · File Edit / Patch · two roads + 4-step pipeline
# ─────────────────────────────────────────────────────────────────────
PATCH_SVG = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 480" role="img"
     aria-label="\u6587\u4ef6\u7f16\u8f91\u4e24\u6761\u8def\u7ebf">
  <defs>
    {WOBBLE_DEFS}
    <style>{STYLE}</style>
  </defs>

  <text x="20" y="30" class="h">\u6587\u4ef6\u7f16\u8f91\u4e24\u6761\u8def\u7ebf</text>
  <text x="20" y="50" class="t-sub">V4A \u5185\u5d4c DSL\uff08Codex / Hermes\uff09vs str_replace \u8c03\u7528\uff08Claude Code\uff09</text>

  <g filter="url(#wobble)">
    <!-- left lane: V4A -->
    <rect x="20" y="80" width="360" height="380" rx="12"
          fill="#fdf6e3" stroke="#2563eb" stroke-width="2.5" />
    <text x="200" y="108" class="t" text-anchor="middle" fill="#2563eb" font-weight="700">V4A \u5185\u5d4c DSL</text>

    <rect x="50" y="130" width="300" height="58" rx="8" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.8" />
    <text x="200" y="152" class="t" text-anchor="middle">1. \u6a21\u578b\u8f93\u51fa\u4e00\u6574\u6bb5 patch</text>
    <text x="200" y="170" class="t-sub" text-anchor="middle">*** Begin Patch ... *** End Patch</text>
    <text x="200" y="184" class="t-sub" text-anchor="middle">5 \u79cd marker: Update / Add / Delete / Move / EOF</text>

    <line x1="200" y1="188" x2="200" y2="208" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)" />

    <rect x="50" y="212" width="300" height="58" rx="8" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.8" />
    <text x="200" y="234" class="t" text-anchor="middle">2. Lark grammar parser</text>
    <text x="200" y="252" class="t-sub" text-anchor="middle">apply-patch/src/parser.rs</text>
    <text x="200" y="266" class="t-sub" text-anchor="middle">\u4efb\u4e00 hunk \u4e0d\u5408\u6cd5 \u2192 reject \u6574\u6bb5</text>

    <line x1="200" y1="270" x2="200" y2="290" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)" />

    <rect x="50" y="294" width="300" height="58" rx="8" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.8" />
    <text x="200" y="316" class="t" text-anchor="middle">3. \u539f\u5b50\u63d0\u4ea4\u591a\u6587\u4ef6</text>
    <text x="200" y="334" class="t-sub" text-anchor="middle">Update + Add + Delete + Move</text>
    <text x="200" y="348" class="t-sub" text-anchor="middle">\u4e00\u8f6e\u4e00\u6b21\u8c03\u7528</text>

    <line x1="200" y1="352" x2="200" y2="372" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)" />

    <rect x="50" y="376" width="300" height="58" rx="8" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.8" />
    <text x="200" y="398" class="t" text-anchor="middle">4. rollout / execpolicy</text>
    <text x="200" y="416" class="t-sub" text-anchor="middle">patch \u6587\u672c\u5373\u5ba1\u8ba1\u65e5\u5fd7</text>
    <text x="200" y="430" class="t-sub" text-anchor="middle">replay \u4e00\u5b57\u4e0d\u6539</text>

    <!-- right lane: str_replace -->
    <rect x="400" y="80" width="340" height="380" rx="12"
          fill="#fdf6e3" stroke="#7c3aed" stroke-width="2.5" />
    <text x="570" y="108" class="t" text-anchor="middle" fill="#7c3aed" font-weight="700">str_replace \u8c03\u7528</text>

    <rect x="430" y="130" width="280" height="58" rx="8" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.8" />
    <text x="570" y="152" class="t" text-anchor="middle">1. tool_use #N</text>
    <text x="570" y="170" class="t-sub" text-anchor="middle">old_string / new_string / replace_all</text>
    <text x="570" y="184" class="t-sub" text-anchor="middle">\u4e00\u6b21\u4e00\u6539</text>

    <line x1="570" y1="188" x2="570" y2="208" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)" />

    <rect x="430" y="212" width="280" height="58" rx="8" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.8" />
    <text x="570" y="234" class="t" text-anchor="middle">2. \u552f\u4e00\u5339\u914d + mtime</text>
    <text x="570" y="252" class="t-sub" text-anchor="middle">old_string \u91cd\u590d \u2192 \u62a5\u9519</text>
    <text x="570" y="266" class="t-sub" text-anchor="middle">FILE_UNEXPECTEDLY_MODIFIED_ERROR</text>

    <line x1="570" y1="270" x2="570" y2="290" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)" />

    <rect x="430" y="294" width="280" height="58" rx="8" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.8" />
    <text x="570" y="316" class="t" text-anchor="middle">3. \u539f\u5b50\u5199\u5355\u70b9</text>
    <text x="570" y="334" class="t-sub" text-anchor="middle">writeTextContent</text>
    <text x="570" y="348" class="t-sub" text-anchor="middle">\u591a\u70b9 = \u591a\u6b21 tool_use</text>

    <line x1="570" y1="352" x2="570" y2="372" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)" />

    <rect x="430" y="376" width="280" height="58" rx="8" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.8" />
    <text x="570" y="398" class="t" text-anchor="middle">4. LSP / fileHistory / SDK</text>
    <text x="570" y="416" class="t-sub" text-anchor="middle">clearDiagnostics + trackEdit</text>
    <text x="570" y="430" class="t-sub" text-anchor="middle">notifyVscodeFileUpdated</text>
  </g>
</svg>
"""

# ─────────────────────────────────────────────────────────────────────
# 07 · Shell Execution · 4 pipelines for one `git push --force`
# ─────────────────────────────────────────────────────────────────────
SHELL_SVG = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" role="img"
     aria-label="\u56db\u7cfb\u7edf\u7684 shell \u6267\u884c\u62e6\u622a\u6808">
  <defs>
    {WOBBLE_DEFS}
    <style>{STYLE}</style>
  </defs>

  <text x="20" y="28" class="h">\u4e00\u6761 `git push --force` \u8d70\u8fc7 4 \u4e2a\u4e0d\u540c pipeline</text>
  <text x="20" y="48" class="t-sub">\u62e6\u622a\u70b9\u4e0d\u91cd\u53e0\uff1aDSL / \u89e3\u6790\u5c42 / \u4e8c\u7ef4\u77e9\u9635 / \u6362\u6267\u884c\u73af\u5883</text>

  <g filter="url(#wobble)">
    <!-- common input -->
    <rect x="370" y="64" width="220" height="34" rx="6"
          fill="#1e293b" stroke="#1e293b" stroke-width="2" />
    <text x="480" y="86" class="sys" text-anchor="middle">tool_call: git push --force</text>

    <line x1="160" y1="98" x2="160" y2="120" stroke="#1e293b" stroke-width="1.5" />
    <line x1="370" y1="98" x2="370" y2="120" stroke="#1e293b" stroke-width="1.5" />
    <line x1="590" y1="98" x2="590" y2="120" stroke="#1e293b" stroke-width="1.5" />
    <line x1="800" y1="98" x2="800" y2="120" stroke="#1e293b" stroke-width="1.5" />
    <line x1="160" y1="120" x2="800" y2="120" stroke="#1e293b" stroke-width="1.5" />
    <line x1="160" y1="120" x2="160" y2="135" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)" />
    <line x1="370" y1="120" x2="370" y2="135" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)" />
    <line x1="590" y1="120" x2="590" y2="135" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)" />
    <line x1="800" y1="120" x2="800" y2="135" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)" />

    <!-- Codex lane -->
    <rect x="60" y="140" width="200" height="370" rx="12"
          fill="#fdf6e3" stroke="#2563eb" stroke-width="2.5" />
    <text x="160" y="164" class="t" text-anchor="middle" fill="#2563eb" font-weight="700">Codex</text>
    <text x="160" y="180" class="t-sub" text-anchor="middle">execpolicy + sandbox</text>

    <rect x="80" y="196" width="160" height="40" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="160" y="212" class="t" text-anchor="middle">shlex \u5206\u8bcd</text>
    <text x="160" y="226" class="t-sub" text-anchor="middle">[git, push, --force]</text>

    <rect x="80" y="248" width="160" height="56" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="160" y="266" class="t" text-anchor="middle">prefix_rule \u5339\u914d</text>
    <text x="160" y="282" class="t-sub" text-anchor="middle">Starlark .codexpolicy</text>
    <text x="160" y="296" class="t-sub" text-anchor="middle">decision: prompt</text>

    <rect x="80" y="316" width="160" height="40" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="160" y="332" class="t" text-anchor="middle">TUI \u5ba1\u6279</text>
    <text x="160" y="346" class="t-sub" text-anchor="middle">approval_policy</text>

    <rect x="80" y="368" width="160" height="48" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="160" y="386" class="t" text-anchor="middle">sandbox_mode</text>
    <text x="160" y="400" class="t-sub" text-anchor="middle">Landlock + seccomp</text>

    <rect x="80" y="430" width="160" height="64" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="160" y="450" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">fork \u2192 exec</text>
    <text x="160" y="466" class="t-sub" text-anchor="middle">\u5728 sandbox \u91cc\u8dd1</text>
    <text x="160" y="482" class="t-sub" text-anchor="middle">\u8fdb\u7a0b\u9694\u79bb</text>

    <!-- Claude Code lane -->
    <rect x="270" y="140" width="200" height="370" rx="12"
          fill="#fdf6e3" stroke="#7c3aed" stroke-width="2.5" />
    <text x="370" y="164" class="t" text-anchor="middle" fill="#7c3aed" font-weight="700">Claude Code</text>
    <text x="370" y="180" class="t-sub" text-anchor="middle">23 \u68c0\u67e5 + sandbox</text>

    <rect x="290" y="196" width="160" height="40" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="370" y="212" class="t" text-anchor="middle">tree-sitter \u89e3\u6790</text>
    <text x="370" y="226" class="t-sub" text-anchor="middle">+ shell-quote</text>

    <rect x="290" y="248" width="160" height="56" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="370" y="266" class="t" text-anchor="middle">23 \u9879 ID \u5316\u68c0\u67e5</text>
    <text x="370" y="282" class="t-sub" text-anchor="middle">#5 / #8 / #19 ...</text>
    <text x="370" y="296" class="t-sub" text-anchor="middle">ZSH_DANGEROUS?</text>

    <rect x="290" y="316" width="160" height="40" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="370" y="332" class="t" text-anchor="middle">permission mode</text>
    <text x="370" y="346" class="t-sub" text-anchor="middle">canUseTool hook</text>

    <rect x="290" y="368" width="160" height="48" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="370" y="386" class="t" text-anchor="middle">SandboxManager</text>
    <text x="370" y="400" class="t-sub" text-anchor="middle">sandbox-exec / bwrap</text>

    <rect x="290" y="430" width="160" height="64" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="370" y="450" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">fork \u2192 exec</text>
    <text x="370" y="466" class="t-sub" text-anchor="middle">sandbox by default</text>
    <text x="370" y="482" class="t-sub" text-anchor="middle">LSP / fileHistory \u8054\u52a8</text>

    <!-- OpenClaw lane -->
    <rect x="480" y="140" width="220" height="370" rx="12"
          fill="#fdf6e3" stroke="#16a34a" stroke-width="2.5" />
    <text x="590" y="164" class="t" text-anchor="middle" fill="#16a34a" font-weight="700">OpenClaw</text>
    <text x="590" y="180" class="t-sub" text-anchor="middle">security \u00d7 ask \u77e9\u9635</text>

    <rect x="500" y="196" width="180" height="40" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="590" y="212" class="t" text-anchor="middle">splitCommand</text>
    <text x="590" y="226" class="t-sub" text-anchor="middle">+ obfuscation-detect</text>

    <rect x="500" y="248" width="180" height="56" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="590" y="266" class="t" text-anchor="middle">security == allowlist?</text>
    <text x="590" y="282" class="t-sub" text-anchor="middle">shell wrapper \u2192 deny</text>
    <text x="590" y="296" class="t-sub" text-anchor="middle">safe-bin profile?</text>

    <rect x="500" y="316" width="180" height="40" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="590" y="332" class="t" text-anchor="middle">ask == on-miss?</text>
    <text x="590" y="346" class="t-sub" text-anchor="middle">JSONL socket \u2192 UI</text>

    <rect x="500" y="368" width="180" height="48" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="590" y="386" class="t" text-anchor="middle">ExecHost \u9009\u62e9</text>
    <text x="590" y="400" class="t-sub" text-anchor="middle">sandbox / gateway / node</text>

    <rect x="500" y="430" width="180" height="64" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="590" y="450" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">spawn</text>
    <text x="590" y="466" class="t-sub" text-anchor="middle">sandbox / node fork</text>
    <text x="590" y="482" class="t-sub" text-anchor="middle">\u4e8b\u4ef6\u6d41\u63a8 lane</text>

    <!-- Hermes lane -->
    <rect x="720" y="140" width="200" height="370" rx="12"
          fill="#fdf6e3" stroke="#f97316" stroke-width="2.5" />
    <text x="820" y="164" class="t" text-anchor="middle" fill="#f97316" font-weight="700">Hermes</text>
    <text x="820" y="180" class="t-sub" text-anchor="middle">\u6362\u6267\u884c\u73af\u5883</text>

    <rect x="740" y="196" width="160" height="40" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="820" y="212" class="t" text-anchor="middle">workdir allowlist</text>
    <text x="820" y="226" class="t-sub" text-anchor="middle">_WORKDIR_SAFE_RE</text>

    <rect x="740" y="248" width="160" height="56" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="820" y="266" class="t" text-anchor="middle">_check_all_guards</text>
    <text x="820" y="282" class="t-sub" text-anchor="middle">tirith \u68c0\u6d4b</text>
    <text x="820" y="296" class="t-sub" text-anchor="middle">dangerous cmd \u62a5\u8b66</text>

    <rect x="740" y="316" width="160" height="40" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="820" y="332" class="t" text-anchor="middle">approval_callback</text>
    <text x="820" y="346" class="t-sub" text-anchor="middle">once/session/always/deny</text>

    <rect x="740" y="368" width="160" height="48" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="820" y="386" class="t" text-anchor="middle">TERMINAL_ENV</text>
    <text x="820" y="400" class="t-sub" text-anchor="middle">local/docker/modal/...</text>

    <rect x="740" y="430" width="160" height="64" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="820" y="450" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">spawn / docker run</text>
    <text x="820" y="466" class="t-sub" text-anchor="middle">\u9694\u79bb\u5728\u73af\u5883\u5c42</text>
    <text x="820" y="482" class="t-sub" text-anchor="middle">\u4e0d\u62e6\u547d\u4ee4\u672c\u8eab</text>
  </g>

  <text x="480" y="528" class="t-sub" text-anchor="middle">4 \u4e2a\u62e6\u622a\u70b9\u4e0d\u91cd\u53e0\uff1aDSL \u5916\u7f6e \u00b7 \u89e3\u6790\u7a77\u4e3e \u00b7 \u4e8c\u7ef4\u77e9\u9635 \u00b7 \u6362\u73af\u5883\u3002\u5b9e\u9645\u6784\u5efa\u53ef\u4ee5\u6311\u4e24\u5230\u4e09\u5c42\u53e0\u7528\u3002</text>
</svg>
"""

# ─────────────────────────────────────────────────────────────────────
# 08 · Git Workflow · abstraction-depth gradient
# ─────────────────────────────────────────────────────────────────────
GIT_SVG = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" role="img"
     aria-label="\u56db\u7cfb\u7edf\u7684 git \u62bd\u8c61\u5c42\u6df1\u5ea6\u68af\u5ea6">
  <defs>
    {WOBBLE_DEFS}
    <style>{STYLE}</style>
  </defs>

  <text x="20" y="28" class="h">\u56db\u4e2a agent \u770b\u540c\u4e00\u4e2a repo \u770b\u5230\u4e0d\u540c\u7684\u4e1c\u897f</text>
  <text x="20" y="48" class="t-sub">\u62bd\u8c61\u5c42\u5382\u5ea6\u5dee\u4e00\u4e2a\u6570\u91cf\u7ea7\uff1a\u4ece\u4e00\u4e2a\u7368\u7acb crate \u5230\u4e00\u884c subprocess</text>

  <g filter="url(#wobble)">
    <!-- common repo at top -->
    <rect x="340" y="64" width="220" height="36" rx="6"
          fill="#1e293b" stroke="#1e293b" stroke-width="2" />
    <text x="450" y="86" class="sys" text-anchor="middle">git repo (.git/HEAD, refs, ...)</text>

    <line x1="120" y1="100" x2="120" y2="125" stroke="#1e293b" stroke-width="1.5" />
    <line x1="340" y1="100" x2="340" y2="125" stroke="#1e293b" stroke-width="1.5" />
    <line x1="560" y1="100" x2="560" y2="125" stroke="#1e293b" stroke-width="1.5" />
    <line x1="780" y1="100" x2="780" y2="125" stroke="#1e293b" stroke-width="1.5" />
    <line x1="120" y1="125" x2="780" y2="125" stroke="#1e293b" stroke-width="1.5" />
    <line x1="120" y1="125" x2="120" y2="140" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)" />
    <line x1="340" y1="125" x2="340" y2="140" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)" />
    <line x1="560" y1="125" x2="560" y2="140" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)" />
    <line x1="780" y1="125" x2="780" y2="140" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)" />

    <!-- Codex column: thickest -->
    <rect x="20" y="148" width="200" height="270" rx="12"
          fill="#fdf6e3" stroke="#2563eb" stroke-width="2.5" />
    <text x="120" y="170" class="t" text-anchor="middle" fill="#2563eb" font-weight="700">Codex</text>
    <text x="120" y="186" class="t-sub" text-anchor="middle">git-utils crate</text>

    <rect x="38" y="200" width="164" height="22" rx="4" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.2" />
    <text x="120" y="216" class="t-sub" text-anchor="middle">GitInfo \u5f3a\u7c7b\u578b</text>

    <rect x="38" y="228" width="164" height="22" rx="4" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.2" />
    <text x="120" y="244" class="t-sub" text-anchor="middle">GitSha + 5s timeout</text>

    <rect x="38" y="256" width="164" height="22" rx="4" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.2" />
    <text x="120" y="272" class="t-sub" text-anchor="middle">apply_git_patch</text>

    <rect x="38" y="284" width="164" height="22" rx="4" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.2" />
    <text x="120" y="300" class="t-sub" text-anchor="middle">baseline \u5feb\u7167</text>

    <rect x="38" y="312" width="164" height="22" rx="4" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.2" />
    <text x="120" y="328" class="t-sub" text-anchor="middle">recent_commits</text>

    <rect x="38" y="340" width="164" height="22" rx="4" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.2" />
    <text x="120" y="356" class="t-sub" text-anchor="middle">git_diff_to_remote</text>

    <rect x="38" y="368" width="164" height="22" rx="4" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.2" />
    <text x="120" y="384" class="t-sub" text-anchor="middle">merge_base_with_head</text>

    <text x="120" y="406" class="t" text-anchor="middle" fill="#2563eb" font-weight="700">30+ \u4e2a public fn</text>

    <!-- Claude Code column: thick -->
    <rect x="240" y="148" width="200" height="220" rx="12"
          fill="#fdf6e3" stroke="#7c3aed" stroke-width="2.5" />
    <text x="340" y="170" class="t" text-anchor="middle" fill="#7c3aed" font-weight="700">Claude Code</text>
    <text x="340" y="186" class="t-sub" text-anchor="middle">utils/git.ts + cache + safety</text>

    <rect x="258" y="200" width="164" height="22" rx="4" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.2" />
    <text x="340" y="216" class="t-sub" text-anchor="middle">findGitRoot LRU(50)</text>

    <rect x="258" y="228" width="164" height="22" rx="4" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.2" />
    <text x="340" y="244" class="t-sub" text-anchor="middle">gitFilesystem \u7f13\u5b58</text>

    <rect x="258" y="256" width="164" height="22" rx="4" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.2" />
    <text x="340" y="272" class="t-sub" text-anchor="middle">gitSafety: bare-repo</text>

    <rect x="258" y="284" width="164" height="22" rx="4" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.2" />
    <text x="340" y="300" class="t-sub" text-anchor="middle">/review prompt</text>

    <rect x="258" y="312" width="164" height="22" rx="4" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.2" />
    <text x="340" y="328" class="t-sub" text-anchor="middle">/pr_comments</text>

    <text x="340" y="356" class="t" text-anchor="middle" fill="#7c3aed" font-weight="700">~1000 \u884c\u4ee3\u7801</text>

    <!-- OpenClaw column: thin -->
    <rect x="460" y="148" width="200" height="160" rx="12"
          fill="#fdf6e3" stroke="#16a34a" stroke-width="2.5" />
    <text x="560" y="170" class="t" text-anchor="middle" fill="#16a34a" font-weight="700">OpenClaw</text>
    <text x="560" y="186" class="t-sub" text-anchor="middle">infra/git-root.ts</text>

    <rect x="478" y="200" width="164" height="22" rx="4" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.2" />
    <text x="560" y="216" class="t-sub" text-anchor="middle">findGitRoot walk-up</text>

    <rect x="478" y="228" width="164" height="22" rx="4" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.2" />
    <text x="560" y="244" class="t-sub" text-anchor="middle">\u8bfb .git/HEAD \u62ff SHA</text>

    <text x="560" y="280" class="t" text-anchor="middle" fill="#16a34a" font-weight="700">\u7248\u672c\u6233 only</text>
    <text x="560" y="298" class="t-sub" text-anchor="middle">~30 \u884c\u4ee3\u7801</text>

    <!-- Hermes column: thinnest -->
    <rect x="680" y="148" width="200" height="100" rx="12"
          fill="#fdf6e3" stroke="#f97316" stroke-width="2.5" />
    <text x="780" y="170" class="t" text-anchor="middle" fill="#f97316" font-weight="700">Hermes</text>
    <text x="780" y="186" class="t-sub" text-anchor="middle">banner.py</text>

    <rect x="698" y="200" width="164" height="22" rx="4" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.2" />
    <text x="780" y="216" class="t-sub" text-anchor="middle">upstream/local/ahead</text>

    <text x="780" y="240" class="t" text-anchor="middle" fill="#f97316" font-weight="700">~25 \u884c</text>

    <!-- bottom gradient -->
    <text x="20" y="438" class="t-sub">\u539a</text>
    <line x1="50" y1="436" x2="850" y2="436" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)" />
    <text x="864" y="438" class="t-sub" text-anchor="end">\u8584</text>
    <text x="450" y="452" class="t-sub" text-anchor="middle">\u62bd\u8c61\u539a\u5ea6\uff1aCodex \u00bb Claude Code \u00bb OpenClaw \u00bb Hermes</text>
  </g>
</svg>
"""

# ─────────────────────────────────────────────────────────────────────
# 09 · Code Review · four review models compared
# ─────────────────────────────────────────────────────────────────────
REVIEW_SVG = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 580" role="img"
     aria-label="\u56db\u79cd code review \u6a21\u5f0f\u5bf9\u6bd4">
  <defs>
    {WOBBLE_DEFS}
    <style>{STYLE}</style>
  </defs>

  <text x="20" y="28" class="h">\u540c\u6837\u662f"\u53e6\u4e00\u4e2a agent \u6765\u68c0\u67e5"\uff0c\u56db\u5bb6\u5305\u88c5\u65b9\u5f0f\u4e0d\u4e00\u6837</text>
  <text x="20" y="48" class="t-sub">\u4ece"\u53d7\u7ea6\u675f\u5b50 agent" \u5230"\u540c\u4e0a\u4e0b\u6587 prompt" \u5230"\u8fdc\u7a0b pipeline" \u5230"\u4e0d\u5185\u5efa"</text>

  <g filter="url(#wobble)">
    <!-- Codex lane -->
    <rect x="20" y="68" width="430" height="240" rx="12"
          fill="#fdf6e3" stroke="#2563eb" stroke-width="2.5" />
    <text x="40" y="92" class="t" fill="#2563eb" font-weight="700">Codex \u00b7 \u53cc\u5c42</text>
    <text x="40" y="110" class="t-sub">code review sub-agent + guardian sub-agent</text>

    <!-- code review sub-agent -->
    <rect x="40" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="130" y="142" class="t" text-anchor="middle">/review \u89e6\u53d1</text>
    <text x="130" y="158" class="t-sub" text-anchor="middle">fork sub-agent</text>
    <text x="130" y="172" class="t-sub" text-anchor="middle">web_search=Disabled</text>
    <text x="130" y="186" class="t-sub" text-anchor="middle">Spawn/Collab=Disabled</text>
    <text x="130" y="200" class="t-sub" text-anchor="middle">approval=Never</text>

    <!-- 4 targets -->
    <rect x="40" y="216" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="130" y="234" class="t" text-anchor="middle">4 \u79cd target</text>
    <text x="130" y="250" class="t-sub" text-anchor="middle">uncommitted</text>
    <text x="130" y="264" class="t-sub" text-anchor="middle">base-branch</text>
    <text x="130" y="278" class="t-sub" text-anchor="middle">commit</text>
    <text x="130" y="292" class="t-sub" text-anchor="middle">custom</text>

    <!-- guardian -->
    <rect x="240" y="124" width="190" height="172" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="335" y="142" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">guardian/review.rs</text>
    <text x="335" y="160" class="t-sub" text-anchor="middle">\u4e3b agent tool_call</text>
    <text x="335" y="174" class="t-sub" text-anchor="middle">\u2192 guardian sub-agent \u5ba1</text>
    <text x="335" y="188" class="t-sub" text-anchor="middle">risk level + decision</text>
    <text x="335" y="206" class="t-sub" text-anchor="middle">rejection workaround</text>
    <text x="335" y="220" class="t-sub" text-anchor="middle">\u9632\u5fa1 + timeout</text>
    <text x="335" y="234" class="t-sub" text-anchor="middle">circuit breaker</text>
    <text x="335" y="258" class="t-sub" text-anchor="middle">"agent \u5ba1 agent"</text>

    <!-- Claude Code lane -->
    <rect x="470" y="68" width="410" height="240" rx="12"
          fill="#fdf6e3" stroke="#7c3aed" stroke-width="2.5" />
    <text x="490" y="92" class="t" fill="#7c3aed" font-weight="700">Claude Code \u00b7 \u672c\u5730 + \u8fdc\u7a0b</text>
    <text x="490" y="110" class="t-sub">/review prompt-as-command + /ultrareview teleport</text>

    <rect x="490" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="580" y="142" class="t" text-anchor="middle">/review (\u672c\u5730)</text>
    <text x="580" y="158" class="t-sub" text-anchor="middle">\u4e00\u6bb5\u5199\u597d\u7684 prompt</text>
    <text x="580" y="172" class="t-sub" text-anchor="middle">\u5851\u8fdb\u4e3b agent</text>
    <text x="580" y="186" class="t-sub" text-anchor="middle">gh pr view / diff</text>
    <text x="580" y="200" class="t-sub" text-anchor="middle">5 section \u8f93\u51fa</text>

    <rect x="690" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="780" y="142" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">/ultrareview</text>
    <text x="780" y="158" class="t-sub" text-anchor="middle">teleport \u2192 CCR Web</text>
    <text x="780" y="172" class="t-sub" text-anchor="middle">10-20 \u5206\u949f</text>
    <text x="780" y="186" class="t-sub" text-anchor="middle">quota / billing gate</text>
    <text x="780" y="200" class="t-sub" text-anchor="middle">task-notification \u56de\u5199</text>

    <rect x="490" y="216" width="380" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="680" y="234" class="t" text-anchor="middle">\u5171\u540c\u70b9</text>
    <text x="680" y="250" class="t-sub" text-anchor="middle">prompt \u91cc\u5f3a\u5236 reviewer \u89d2\u8272</text>
    <text x="680" y="264" class="t-sub" text-anchor="middle">/pr_comments \u8865\u52a9\u547d\u4ee4\u5904\u7406\u8bc4\u8bba\u56de\u5199</text>
    <text x="680" y="278" class="t-sub" text-anchor="middle">2.1.88 \u7248\u672c\u8d70 prompt-as-command \u4e0d\u5f00 sub-thread</text>

    <!-- OpenClaw lane -->
    <rect x="20" y="320" width="430" height="200" rx="12"
          fill="#fdf6e3" stroke="#16a34a" stroke-width="2.5" />
    <text x="40" y="344" class="t" fill="#16a34a" font-weight="700">OpenClaw \u00b7 plugin hook</text>
    <text x="40" y="362" class="t-sub">\u4e0d\u5185\u5efa\uff0c\u7559\u7ed9 tool-policy-pipeline</text>

    <rect x="40" y="376" width="390" height="130" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="235" y="396" class="t" text-anchor="middle">after_tool_call hook</text>
    <text x="235" y="416" class="t-sub" text-anchor="middle">\u7528\u6237 plugin \u53ef\u5728\u8fd9\u91cc\u6302 reviewer middleware</text>
    <text x="235" y="436" class="t-sub" text-anchor="middle">\u6bcf\u6b21 fs.write \u540e\u8df0 reviewer prompt</text>
    <text x="235" y="456" class="t-sub" text-anchor="middle">findings \u4f5c\u4e3a system message \u6ce8\u5165\u4e0b\u4e00\u8f6e</text>
    <text x="235" y="480" class="t-sub" text-anchor="middle">\u63a7\u5236\u9762\u5b9a\u4f4d\u4e0b\u7684\u6b63\u786e\u514b\u5236</text>

    <!-- Hermes lane -->
    <rect x="470" y="320" width="410" height="200" rx="12"
          fill="#fdf6e3" stroke="#f97316" stroke-width="2.5" />
    <text x="490" y="344" class="t" fill="#f97316" font-weight="700">Hermes \u00b7 \u96f6\u57fa\u7840\u8bbe\u65bd</text>
    <text x="490" y="362" class="t-sub">\u4e0d\u5185\u5efa\uff0c\u8d70 terminal + \u7528\u6237 prompt</text>

    <rect x="490" y="376" width="370" height="130" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="675" y="396" class="t" text-anchor="middle">user: "review \u4ee3\u7801"</text>
    <text x="675" y="416" class="t-sub" text-anchor="middle">\u2193</text>
    <text x="675" y="430" class="t-sub" text-anchor="middle">terminal_tool \u8dd1 git diff</text>
    <text x="675" y="446" class="t-sub" text-anchor="middle">\u2193</text>
    <text x="675" y="460" class="t-sub" text-anchor="middle">\u4e3b\u5bf9\u8bdd\u91cc\u8f93\u51fa review</text>
    <text x="675" y="484" class="t-sub" text-anchor="middle">\u6ca1 reviewer \u89d2\u8272\u9694\u79bb\uff0c\u5bb9\u6613\u8dd1\u504f</text>
  </g>

  <text x="450" y="558" class="t-sub" text-anchor="middle">\u9694\u79bb\u5ea6\uff1aCodex sub-agent \u00bb /ultrareview \u00bb OpenClaw hook \u00bb /review (local) \u00bb Hermes terminal-only</text>
</svg>
"""

# ─────────────────────────────────────────────────────────────────────
# write everything
# ─────────────────────────────────────────────────────────────────────
SUBAGENT_SVG = r"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 580" width="100%" font-family="'Kalam','Comic Neue',sans-serif">
  <defs>
    <filter id="r10">
      <feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="20" />
      <feDisplacementMap in="SourceGraphic" scale="1.3" />
    </filter>
    <style>
      .t { font-size: 14px; fill: #1e293b; }
      .t-sm { font-size: 12px; fill: #1e293b; }
      .t-sub { font-size: 11px; fill: #475569; }
      .head { font-size: 18px; fill: #1e293b; font-weight: 700; }
    </style>
  </defs>

  <rect width="900" height="580" fill="#fffef7" />

  <text x="450" y="34" class="head" text-anchor="middle">Subagent\uff1a\u56db\u79cd\u62bd\u8c61\u5c42\u7684\u5b50 agent \u6a21\u578b</text>
  <text x="450" y="54" class="t-sub" text-anchor="middle">\u51fd\u6570 \u2192 \u7c7b\u578b\u5316\u679a\u4e3e \u2192 \u4efb\u52a1\u62bd\u8c61 \u2192 \u5b8c\u6574\u5e73\u53f0</text>

  <g filter="url(#r10)">
    <rect x="20" y="68" width="430" height="240" rx="12" fill="#fdf6e3" stroke="#0ea5e9" stroke-width="2.5" />
    <text x="40" y="92" class="t" fill="#0ea5e9" font-weight="700">Codex \u00b7 SubAgentSource \u679a\u4e3e</text>
    <text x="40" y="110" class="t-sub">5 \u79cd\u6765\u6e90 + service \u7ee7\u627f</text>

    <rect x="40" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="130" y="142" class="t" text-anchor="middle">5 \u79cd source</text>
    <text x="130" y="158" class="t-sub" text-anchor="middle">Review</text>
    <text x="130" y="172" class="t-sub" text-anchor="middle">Compact</text>
    <text x="130" y="186" class="t-sub" text-anchor="middle">ThreadSpawn{depth}</text>
    <text x="130" y="200" class="t-sub" text-anchor="middle">MemoryConsolidation / Other</text>

    <rect x="240" y="124" width="190" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="335" y="142" class="t" text-anchor="middle">7 \u7c7b service \u7ee7\u627f</text>
    <text x="335" y="158" class="t-sub" text-anchor="middle">exec_policy \u00b7 plugins</text>
    <text x="335" y="172" class="t-sub" text-anchor="middle">mcp \u00b7 skills \u00b7 env</text>
    <text x="335" y="186" class="t-sub" text-anchor="middle">auth \u00b7 models</text>
    <text x="335" y="200" class="t-sub" text-anchor="middle">\u5b50\u4e0d\u53ef\u6bd4\u7236\u5bbd\u677e</text>

    <rect x="40" y="216" width="390" height="80" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="235" y="234" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">approval \u8def\u7531\u56de\u7236</text>
    <text x="235" y="252" class="t-sub" text-anchor="middle">\u5b50 agent AskForApproval = Never</text>
    <text x="235" y="266" class="t-sub" text-anchor="middle">event \u63a8\u5230\u7236 session</text>
    <text x="235" y="280" class="t-sub" text-anchor="middle">\u5b50\u6c38\u8fdc\u4e0d\u5f39 UI</text>

    <rect x="470" y="68" width="410" height="240" rx="12" fill="#fdf6e3" stroke="#7c3aed" stroke-width="2.5" />
    <text x="490" y="92" class="t" fill="#7c3aed" font-weight="700">Claude Code \u00b7 Task \u62bd\u8c61</text>
    <text x="490" y="110" class="t-sub">7 \u79cd TaskType + status FSM</text>

    <rect x="490" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="580" y="142" class="t" text-anchor="middle">TaskType x7</text>
    <text x="580" y="158" class="t-sub" text-anchor="middle">local_bash / local_agent</text>
    <text x="580" y="172" class="t-sub" text-anchor="middle">remote_agent / teammate</text>
    <text x="580" y="186" class="t-sub" text-anchor="middle">local_workflow / monitor_mcp</text>
    <text x="580" y="200" class="t-sub" text-anchor="middle">dream</text>

    <rect x="690" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="780" y="142" class="t" text-anchor="middle">TaskStatus FSM</text>
    <text x="780" y="158" class="t-sub" text-anchor="middle">pending \u2192 running</text>
    <text x="780" y="172" class="t-sub" text-anchor="middle">\u2192 completed/failed/killed</text>
    <text x="780" y="186" class="t-sub" text-anchor="middle">outputFile \u843d\u76d8</text>
    <text x="780" y="200" class="t-sub" text-anchor="middle">isConcurrencySafe()</text>

    <rect x="490" y="216" width="380" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="680" y="234" class="t" text-anchor="middle">5 \u4ef6\u5957 task tool</text>
    <text x="680" y="250" class="t-sub" text-anchor="middle">TaskCreate \u00b7 TaskList \u00b7 TaskUpdate</text>
    <text x="680" y="264" class="t-sub" text-anchor="middle">TaskGet \u00b7 TaskStop</text>
    <text x="680" y="278" class="t-sub" text-anchor="middle">\u6a21\u578b\u4e3b\u52a8\u7ba1\u7406 task \u5217\u8868</text>

    <rect x="20" y="320" width="430" height="240" rx="12" fill="#fdf6e3" stroke="#16a34a" stroke-width="2.5" />
    <text x="40" y="344" class="t" fill="#16a34a" font-weight="700">OpenClaw \u00b7 \u5b50 agent \u5e73\u53f0</text>
    <text x="40" y="362" class="t-sub">spawn / registry / depth / announce / attachments / lifecycle</text>

    <rect x="40" y="376" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="130" y="394" class="t" text-anchor="middle">13 \u5b57\u6bb5 spawn</text>
    <text x="130" y="410" class="t-sub" text-anchor="middle">task / label / agentId</text>
    <text x="130" y="424" class="t-sub" text-anchor="middle">model / mode / sandbox</text>
    <text x="130" y="438" class="t-sub" text-anchor="middle">cleanup / attachments</text>
    <text x="130" y="452" class="t-sub" text-anchor="middle">thread / timeout / ...</text>

    <rect x="240" y="376" width="190" height="80" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="335" y="394" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">push-based + \u53cd polling</text>
    <text x="335" y="412" class="t-sub" text-anchor="middle">SPAWN_ACCEPTED_NOTE</text>
    <text x="335" y="426" class="t-sub" text-anchor="middle">\u5199\u5728\u5de5\u5177\u8fd4\u56de\u503c\u91cc</text>
    <text x="335" y="440" class="t-sub" text-anchor="middle">"do NOT poll"</text>

    <rect x="40" y="468" width="390" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="235" y="486" class="t" text-anchor="middle">spawnDepth \u6301\u4e45\u5316</text>
    <text x="235" y="504" class="t-sub" text-anchor="middle">session store \u8de8\u8fdb\u7a0b\u4fdd\u7559</text>
    <text x="235" y="518" class="t-sub" text-anchor="middle">DEFAULT_SUBAGENT_MAX_SPAWN_DEPTH \u53ef\u914d</text>
    <text x="235" y="532" class="t-sub" text-anchor="middle">subagent-announce push \u4e8b\u4ef6</text>

    <rect x="470" y="320" width="410" height="240" rx="12" fill="#fdf6e3" stroke="#f97316" stroke-width="2.5" />
    <text x="490" y="344" class="t" fill="#f97316" font-weight="700">Hermes \u00b7 delegate_task</text>
    <text x="490" y="362" class="t-sub">\u51fd\u6570\u5f0f + MAX_DEPTH=2 + 5 \u5de5\u5177\u786c\u7981</text>

    <rect x="490" y="376" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="580" y="394" class="t" text-anchor="middle">delegate_task()</text>
    <text x="580" y="410" class="t-sub" text-anchor="middle">goal / context</text>
    <text x="580" y="424" class="t-sub" text-anchor="middle">toolset / max_iter</text>
    <text x="580" y="438" class="t-sub" text-anchor="middle">\u9ed8\u8ba4 3 \u5e76\u53d1</text>
    <text x="580" y="452" class="t-sub" text-anchor="middle">parent \u963b\u585e\u7b49\u5168\u90e8</text>

    <rect x="690" y="376" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="780" y="394" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">5 \u4e2a\u786c\u7981\u5de5\u5177</text>
    <text x="780" y="408" class="t-sub" text-anchor="middle">delegate_task</text>
    <text x="780" y="420" class="t-sub" text-anchor="middle">clarify</text>
    <text x="780" y="432" class="t-sub" text-anchor="middle">memory</text>
    <text x="780" y="444" class="t-sub" text-anchor="middle">send_message</text>
    <text x="780" y="456" class="t-sub" text-anchor="middle">execute_code</text>

    <rect x="490" y="468" width="380" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="680" y="486" class="t" text-anchor="middle">MAX_DEPTH = 2 \u5199\u6b7b</text>
    <text x="680" y="504" class="t-sub" text-anchor="middle">parent(0) \u2192 child(1) \u2192 grandchild reject</text>
    <text x="680" y="518" class="t-sub" text-anchor="middle">ThreadPoolExecutor \u540c\u6b65\u5e76\u53d1</text>
    <text x="680" y="532" class="t-sub" text-anchor="middle">30s heartbeat \u9632 UI \u5361\u6b7b</text>
  </g>
</svg>
"""

SESSION_SVG = r"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 580" width="100%" font-family="'Kalam','Comic Neue',sans-serif">
  <defs>
    <filter id="r11">
      <feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="21" />
      <feDisplacementMap in="SourceGraphic" scale="1.3" />
    </filter>
    <style>
      .t { font-size: 14px; fill: #1e293b; }
      .t-sm { font-size: 12px; fill: #1e293b; }
      .t-sub { font-size: 11px; fill: #475569; }
      .head { font-size: 18px; fill: #1e293b; font-weight: 700; }
    </style>
  </defs>

  <rect width="900" height="580" fill="#fffef7" />

  <text x="450" y="34" class="head" text-anchor="middle">Session \u751f\u547d\u5468\u671f\uff1a\u4ece\u6587\u4ef6\u6301\u4e45\u5316\u5230\u591a\u5e73\u53f0\u8def\u7531</text>
  <text x="450" y="54" class="t-sub" text-anchor="middle">JSONL+SQLite \u00b7 4 hook+22 \u5de5\u5177 \u00b7 \u6781\u7b80 id \u00b7 \u591a\u5e73\u53f0+4 reset</text>

  <g filter="url(#r11)">
    <rect x="20" y="68" width="430" height="240" rx="12" fill="#fdf6e3" stroke="#0ea5e9" stroke-width="2.5" />
    <text x="40" y="92" class="t" fill="#0ea5e9" font-weight="700">Codex \u00b7 JSONL + SQLite</text>
    <text x="40" y="110" class="t-sub">rollout-{ts}-{uuid}.jsonl + state.db</text>

    <rect x="40" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="130" y="142" class="t" text-anchor="middle">5 \u79cd RolloutItem</text>
    <text x="130" y="158" class="t-sub" text-anchor="middle">SessionMeta</text>
    <text x="130" y="172" class="t-sub" text-anchor="middle">ResponseItem</text>
    <text x="130" y="186" class="t-sub" text-anchor="middle">Compacted</text>
    <text x="130" y="200" class="t-sub" text-anchor="middle">TurnContext / EventMsg</text>

    <rect x="240" y="124" width="190" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="335" y="142" class="t" text-anchor="middle">SessionMeta \u5b57\u6bb5</text>
    <text x="335" y="158" class="t-sub" text-anchor="middle">cwd / model / agent</text>
    <text x="335" y="172" class="t-sub" text-anchor="middle">git_sha / cli_version</text>
    <text x="335" y="186" class="t-sub" text-anchor="middle">timestamp / source</text>
    <text x="335" y="200" class="t-sub" text-anchor="middle">approval_mode / sandbox</text>

    <rect x="40" y="216" width="390" height="80" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="235" y="234" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">at most 1 turn at a time</text>
    <text x="235" y="252" class="t-sub" text-anchor="middle">Mutex&lt;SessionState&gt; + Mutex&lt;active_turn&gt;</text>
    <text x="235" y="266" class="t-sub" text-anchor="middle">Mailbox \u63a5\u53d7 out-of-band input</text>
    <text x="235" y="280" class="t-sub" text-anchor="middle">ThreadId \u2260 SessionId</text>

    <rect x="470" y="68" width="410" height="240" rx="12" fill="#fdf6e3" stroke="#7c3aed" stroke-width="2.5" />
    <text x="490" y="92" class="t" fill="#7c3aed" font-weight="700">Claude Code \u00b7 4 hook + 22 \u5de5\u5177</text>
    <text x="490" y="110" class="t-sub">startup / resume / clear / compact</text>

    <rect x="490" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="580" y="142" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">4 source hook</text>
    <text x="580" y="158" class="t-sub" text-anchor="middle">startup \u2192 inject CLAUDE.md</text>
    <text x="580" y="172" class="t-sub" text-anchor="middle">resume \u2192 rebuild watcher</text>
    <text x="580" y="186" class="t-sub" text-anchor="middle">clear \u2192 \u6e05\u72b6\u6001</text>
    <text x="580" y="200" class="t-sub" text-anchor="middle">compact \u2192 snapshot</text>

    <rect x="690" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="780" y="142" class="t" text-anchor="middle">22 session \u5de5\u5177</text>
    <text x="780" y="158" class="t-sub" text-anchor="middle">Start / Restore / Storage</text>
    <text x="780" y="172" class="t-sub" text-anchor="middle">Memory / Compact / Activity</text>
    <text x="780" y="186" class="t-sub" text-anchor="middle">EnvVars / Tracing / Hooks</text>
    <text x="780" y="200" class="t-sub" text-anchor="middle">WebSocket / Ingress / ...</text>

    <rect x="490" y="216" width="380" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="680" y="234" class="t" text-anchor="middle">resume \u8de8 7 \u5b50\u7cfb\u7edf</text>
    <text x="680" y="250" class="t-sub" text-anchor="middle">cost / attribution / fileHistory</text>
    <text x="680" y="264" class="t-sub" text-anchor="middle">todos / model / worktree / systemPrompt</text>
    <text x="680" y="278" class="t-sub" text-anchor="middle">"do not add ANY warmup"</text>

    <rect x="20" y="320" width="430" height="240" rx="12" fill="#fdf6e3" stroke="#16a34a" stroke-width="2.5" />
    <text x="40" y="344" class="t" fill="#16a34a" font-weight="700">OpenClaw \u00b7 \u6781\u7b80 session-id</text>
    <text x="40" y="362" class="t-sub">\u4e0a\u5c42\u8c03\u7528\u65b9\u51b3\u5b9a\u600e\u4e48\u5b58</text>

    <rect x="40" y="376" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="130" y="394" class="t" text-anchor="middle">UUID \u6b63\u5219</text>
    <text x="130" y="414" class="t-sub" text-anchor="middle">SESSION_ID_RE</text>
    <text x="130" y="428" class="t-sub" text-anchor="middle">looksLikeSessionId()</text>
    <text x="130" y="442" class="t-sub" text-anchor="middle">\u4e00\u884c\u4ee3\u7801</text>

    <rect x="240" y="376" width="190" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="335" y="394" class="t" text-anchor="middle">session-key-utils</text>
    <text x="335" y="410" class="t-sub" text-anchor="middle">{agentId}:{sessionId}</text>
    <text x="335" y="424" class="t-sub" text-anchor="middle">agent scope \u9694\u79bb</text>
    <text x="335" y="438" class="t-sub" text-anchor="middle">default-agent / sub-agent</text>

    <rect x="40" y="468" width="390" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="235" y="486" class="t" text-anchor="middle">\u5176\u4ed6 12 \u4e2a\u5c0f\u6587\u4ef6</text>
    <text x="235" y="504" class="t-sub" text-anchor="middle">label / transcript-events</text>
    <text x="235" y="518" class="t-sub" text-anchor="middle">model-overrides / send-policy</text>
    <text x="235" y="532" class="t-sub" text-anchor="middle">\u6ca1 rollout, \u6ca1 hook</text>

    <rect x="470" y="320" width="410" height="240" rx="12" fill="#fdf6e3" stroke="#f97316" stroke-width="2.5" />
    <text x="490" y="344" class="t" fill="#f97316" font-weight="700">Hermes \u00b7 \u591a\u5e73\u53f0 + 4 reset</text>
    <text x="490" y="362" class="t-sub">SessionContext + SessionResetPolicy</text>

    <rect x="490" y="376" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="580" y="394" class="t" text-anchor="middle">SessionSource</text>
    <text x="580" y="410" class="t-sub" text-anchor="middle">platform / chat_id</text>
    <text x="580" y="424" class="t-sub" text-anchor="middle">user / chat_name</text>
    <text x="580" y="438" class="t-sub" text-anchor="middle">DM / group / channel / thread</text>
    <text x="580" y="452" class="t-sub" text-anchor="middle">6+ platforms</text>

    <rect x="690" y="376" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="780" y="394" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">ResetPolicy</text>
    <text x="780" y="410" class="t-sub" text-anchor="middle">daily / idle</text>
    <text x="780" y="424" class="t-sub" text-anchor="middle">both / none</text>
    <text x="780" y="438" class="t-sub" text-anchor="middle">at_hour=4</text>
    <text x="780" y="452" class="t-sub" text-anchor="middle">idle_minutes=1440</text>

    <rect x="490" y="468" width="380" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="680" y="486" class="t" text-anchor="middle">PII redaction \u5b89\u5168\u5e73\u53f0</text>
    <text x="680" y="504" class="t-sub" text-anchor="middle">whatsapp / signal / telegram / bluebubbles</text>
    <text x="680" y="518" class="t-sub" text-anchor="middle">discord \u6392\u9664\uff08mention \u9700\u539f id\uff09</text>
    <text x="680" y="532" class="t-sub" text-anchor="middle">notify_exclude_platforms</text>
  </g>
</svg>
"""

PERMISSION_SVG = r"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 580" width="100%" font-family="'Kalam','Comic Neue',sans-serif">
  <defs>
    <filter id="r12">
      <feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="22" />
      <feDisplacementMap in="SourceGraphic" scale="1.3" />
    </filter>
    <style>
      .t { font-size: 14px; fill: #1e293b; }
      .t-sm { font-size: 12px; fill: #1e293b; }
      .t-sub { font-size: 11px; fill: #475569; }
      .head { font-size: 18px; fill: #1e293b; font-weight: 700; }
    </style>
  </defs>

  <rect width="900" height="580" fill="#fffef7" />

  <text x="450" y="34" class="head" text-anchor="middle">\u6743\u9650\u4e0e\u5ba1\u6279\uff1a\u679a\u4e3e\u5316 \u00b7 IDE \u98ce\u683c \u00b7 27 \u77e9\u9635 \u00b7 \u5b50\u8fdb\u7a0b verdict</text>
  <text x="450" y="54" class="t-sub" text-anchor="middle">5x5x6x5 \u00b7 5x3x8 \u00b7 3x3x3 \u00b7 exit code 0/1/2</text>

  <g filter="url(#r12)">
    <rect x="20" y="68" width="430" height="240" rx="12" fill="#fdf6e3" stroke="#0ea5e9" stroke-width="2.5" />
    <text x="40" y="92" class="t" fill="#0ea5e9" font-weight="700">Codex \u00b7 \u679a\u4e3e\u77e9\u9635</text>
    <text x="40" y="110" class="t-sub">AskForApproval x Granular x Action x Decision</text>

    <rect x="40" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="130" y="142" class="t" text-anchor="middle">AskForApproval (5)</text>
    <text x="130" y="158" class="t-sub" text-anchor="middle">UnlessTrusted</text>
    <text x="130" y="172" class="t-sub" text-anchor="middle">OnRequest (default)</text>
    <text x="130" y="186" class="t-sub" text-anchor="middle">Granular(cfg)</text>
    <text x="130" y="200" class="t-sub" text-anchor="middle">Never / OnFailure</text>

    <rect x="240" y="124" width="190" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="335" y="142" class="t" text-anchor="middle">Action (6 \u7c7b)</text>
    <text x="335" y="158" class="t-sub" text-anchor="middle">Command / Execve</text>
    <text x="335" y="172" class="t-sub" text-anchor="middle">ApplyPatch / Network</text>
    <text x="335" y="186" class="t-sub" text-anchor="middle">McpToolCall</text>
    <text x="335" y="200" class="t-sub" text-anchor="middle">RequestPermissions</text>

    <rect x="40" y="216" width="390" height="80" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="235" y="234" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">default_available_decisions(ctx)</text>
    <text x="235" y="252" class="t-sub" text-anchor="middle">\u6309\u4e0a\u4e0b\u6587\u63a8\u65ad\u5f39\u7a97\u6309\u94ae</text>
    <text x="235" y="266" class="t-sub" text-anchor="middle">network \u8bf7\u6c42 \u2192 4 \u6309\u94ae</text>
    <text x="235" y="280" class="t-sub" text-anchor="middle">\u7eaf\u547d\u4ee4 \u2192 Approved + Abort</text>

    <rect x="470" y="68" width="410" height="240" rx="12" fill="#fdf6e3" stroke="#7c3aed" stroke-width="2.5" />
    <text x="490" y="92" class="t" fill="#7c3aed" font-weight="700">Claude Code \u00b7 IDE \u98ce\u683c</text>
    <text x="490" y="110" class="t-sub">5 Mode x 3 Behavior x 8 Source</text>

    <rect x="490" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="580" y="142" class="t" text-anchor="middle">PermissionMode (5)</text>
    <text x="580" y="158" class="t-sub" text-anchor="middle">default</text>
    <text x="580" y="172" class="t-sub" text-anchor="middle">acceptEdits</text>
    <text x="580" y="186" class="t-sub" text-anchor="middle">bypassPermissions</text>
    <text x="580" y="200" class="t-sub" text-anchor="middle">dontAsk / plan</text>

    <rect x="690" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="780" y="142" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">8 Source \u53e0\u52a0</text>
    <text x="780" y="158" class="t-sub" text-anchor="middle">user / project / local</text>
    <text x="780" y="172" class="t-sub" text-anchor="middle">flag / policy / cliArg</text>
    <text x="780" y="186" class="t-sub" text-anchor="middle">command / session</text>
    <text x="780" y="200" class="t-sub" text-anchor="middle">IDE \u914d\u7f6e\u5c42\u7ea7</text>

    <rect x="490" y="216" width="380" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="680" y="234" class="t" text-anchor="middle">PermissionRule</text>
    <text x="680" y="250" class="t-sub" text-anchor="middle">source + behavior + ruleValue</text>
    <text x="680" y="264" class="t-sub" text-anchor="middle">{ toolName, ruleContent? }</text>
    <text x="680" y="278" class="t-sub" text-anchor="middle">"Bash(git diff)" \u51c6 / "Bash(rm)" \u7981</text>

    <rect x="20" y="320" width="430" height="240" rx="12" fill="#fdf6e3" stroke="#16a34a" stroke-width="2.5" />
    <text x="40" y="344" class="t" fill="#16a34a" font-weight="700">OpenClaw \u00b7 27 \u77e9\u9635</text>
    <text x="40" y="362" class="t-sub">ExecHost x ExecSecurity x ExecAsk</text>

    <rect x="40" y="376" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="130" y="394" class="t" text-anchor="middle">ExecHost (3)</text>
    <text x="130" y="410" class="t-sub" text-anchor="middle">sandbox</text>
    <text x="130" y="424" class="t-sub" text-anchor="middle">gateway</text>
    <text x="130" y="438" class="t-sub" text-anchor="middle">node</text>

    <rect x="240" y="376" width="90" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="285" y="394" class="t" text-anchor="middle">Security (3)</text>
    <text x="285" y="410" class="t-sub" text-anchor="middle">deny</text>
    <text x="285" y="424" class="t-sub" text-anchor="middle">allowlist</text>
    <text x="285" y="438" class="t-sub" text-anchor="middle">full</text>

    <rect x="340" y="376" width="90" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="385" y="394" class="t" text-anchor="middle">Ask (3)</text>
    <text x="385" y="410" class="t-sub" text-anchor="middle">off</text>
    <text x="385" y="424" class="t-sub" text-anchor="middle">on-miss</text>
    <text x="385" y="438" class="t-sub" text-anchor="middle">always</text>

    <rect x="40" y="468" width="390" height="80" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="235" y="486" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">5-tuple binding</text>
    <text x="235" y="504" class="t-sub" text-anchor="middle">argv + cwd + agentId + sessionKey + envHash</text>
    <text x="235" y="518" class="t-sub" text-anchor="middle">envHash \u9632 env-swap \u653b\u51fb</text>
    <text x="235" y="532" class="t-sub" text-anchor="middle">cache hit / miss</text>

    <rect x="470" y="320" width="410" height="240" rx="12" fill="#fdf6e3" stroke="#f97316" stroke-width="2.5" />
    <text x="490" y="344" class="t" fill="#f97316" font-weight="700">Hermes \u00b7 exit-code verdict</text>
    <text x="490" y="362" class="t-sub">tirith \u5b50\u8fdb\u7a0b + 0/1/2</text>

    <rect x="490" y="376" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="580" y="394" class="t" text-anchor="middle">tirith binary</text>
    <text x="580" y="410" class="t-sub" text-anchor="middle">5s timeout</text>
    <text x="580" y="424" class="t-sub" text-anchor="middle">exit 0 = allow</text>
    <text x="580" y="438" class="t-sub" text-anchor="middle">exit 1 = block</text>
    <text x="580" y="452" class="t-sub" text-anchor="middle">exit 2 = warn</text>

    <rect x="690" y="376" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="780" y="394" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">fail_open \u5151\u5e95</text>
    <text x="780" y="410" class="t-sub" text-anchor="middle">spawn error / timeout</text>
    <text x="780" y="424" class="t-sub" text-anchor="middle">dev: fail_open=true</text>
    <text x="780" y="438" class="t-sub" text-anchor="middle">prod: fail_open=false</text>
    <text x="780" y="452" class="t-sub" text-anchor="middle">JSON \u53ea\u4e30\u5bcc findings</text>

    <rect x="490" y="468" width="380" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="680" y="486" class="t" text-anchor="middle">\u4f9b\u5e94\u94fe\u5b89\u5168</text>
    <text x="680" y="504" class="t-sub" text-anchor="middle">GitHub releases \u81ea\u52a8\u4e0b\u8f7d</text>
    <text x="680" y="518" class="t-sub" text-anchor="middle">SHA-256 \u5fc5\u9a8c</text>
    <text x="680" y="532" class="t-sub" text-anchor="middle">cosign provenance \u53ef\u9009</text>
  </g>
</svg>
"""

SANDBOX_SVG = r"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 580" width="100%" font-family="'Kalam','Comic Neue',sans-serif">
  <defs>
    <filter id="r13">
      <feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="23" />
      <feDisplacementMap in="SourceGraphic" scale="1.3" />
    </filter>
    <style>
      .t { font-size: 14px; fill: #1e293b; }
      .t-sub { font-size: 11px; fill: #475569; }
      .head { font-size: 18px; fill: #1e293b; font-weight: 700; }
    </style>
  </defs>

  <rect width="900" height="580" fill="#fffef7" />

  <text x="450" y="34" class="head" text-anchor="middle">\u6c99\u7bb1\u4e0e\u6267\u884c\u73af\u5883\uff1a\u4ece\u81ea\u7ba1\u4e09\u5c42\u5230 6 \u540e\u7aef</text>
  <text x="450" y="54" class="t-sub" text-anchor="middle">bwrap+seccomp+landlock \u00b7 schema \u914d\u7f6e \u00b7 ExecHost x3 \u00b7 TERMINAL_ENV x6</text>

  <g filter="url(#r13)">
    <rect x="20" y="68" width="430" height="240" rx="12" fill="#fdf6e3" stroke="#0ea5e9" stroke-width="2.5" />
    <text x="40" y="92" class="t" fill="#0ea5e9" font-weight="700">Codex \u00b7 \u4e09\u5e73\u53f0\u81ea\u7ba1</text>
    <text x="40" y="110" class="t-sub">Linux \u4e09\u4ef6\u5957 / macOS seatbelt / Windows crate</text>

    <rect x="40" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="130" y="142" class="t" text-anchor="middle">Linux \u4e09\u4ef6\u5957</text>
    <text x="130" y="158" class="t-sub" text-anchor="middle">bubblewrap (FS)</text>
    <text x="130" y="172" class="t-sub" text-anchor="middle">seccomp (network)</text>
    <text x="130" y="186" class="t-sub" text-anchor="middle">landlock (legacy)</text>
    <text x="130" y="200" class="t-sub" text-anchor="middle">PR_SET_NO_NEW_PRIVS</text>

    <rect x="240" y="124" width="190" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="335" y="142" class="t" text-anchor="middle">macOS</text>
    <text x="335" y="158" class="t-sub" text-anchor="middle">sandbox-exec</text>
    <text x="335" y="172" class="t-sub" text-anchor="middle">.sb \u914d\u7f6e\u6587\u4ef6</text>
    <text x="335" y="186" class="t-sub" text-anchor="middle">(seatbelt)</text>

    <rect x="40" y="216" width="390" height="80" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="235" y="234" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">thread-level apply</text>
    <text x="235" y="252" class="t-sub" text-anchor="middle">\u53ea\u6709\u5b50\u8fdb\u7a0b\u7ee7\u627f sandbox</text>
    <text x="235" y="266" class="t-sub" text-anchor="middle">PR_SET_NO_NEW_PRIVS \u6309\u9700\u542f\u7528</text>
    <text x="235" y="280" class="t-sub" text-anchor="middle">setuid vs seccomp trade-off</text>

    <rect x="470" y="68" width="410" height="240" rx="12" fill="#fdf6e3" stroke="#7c3aed" stroke-width="2.5" />
    <text x="490" y="92" class="t" fill="#7c3aed" font-weight="700">Claude Code \u00b7 schema \u914d\u7f6e</text>
    <text x="490" y="110" class="t-sub">network + filesystem 2 \u72ec\u7acb schema</text>

    <rect x="490" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="580" y="142" class="t" text-anchor="middle">network config</text>
    <text x="580" y="158" class="t-sub" text-anchor="middle">allowedDomains</text>
    <text x="580" y="172" class="t-sub" text-anchor="middle">allowUnixSockets (mac)</text>
    <text x="580" y="186" class="t-sub" text-anchor="middle">httpProxyPort</text>
    <text x="580" y="200" class="t-sub" text-anchor="middle">socksProxyPort</text>

    <rect x="690" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="780" y="142" class="t" text-anchor="middle">filesystem config</text>
    <text x="780" y="158" class="t-sub" text-anchor="middle">allowWrite / denyWrite</text>
    <text x="780" y="172" class="t-sub" text-anchor="middle">denyRead / allowRead</text>
    <text x="780" y="186" class="t-sub" text-anchor="middle">allowManaged*Only</text>

    <rect x="490" y="216" width="380" height="80" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="680" y="234" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">NVIDIA enterprise rollout</text>
    <text x="680" y="252" class="t-sub" text-anchor="middle">enabledPlatforms: ["macos"]</text>
    <text x="680" y="266" class="t-sub" text-anchor="middle">autoAllowBashIfSandboxed</text>
    <text x="680" y="280" class="t-sub" text-anchor="middle">enableWeakerNetworkIsolation ("Reduces security")</text>

    <rect x="20" y="320" width="430" height="240" rx="12" fill="#fdf6e3" stroke="#16a34a" stroke-width="2.5" />
    <text x="40" y="344" class="t" fill="#16a34a" font-weight="700">OpenClaw \u00b7 ExecHost x3</text>
    <text x="40" y="362" class="t-sub">\u6c99\u7bb1\u5b9e\u73b0\u4ea4\u7ed9 host</text>

    <rect x="40" y="376" width="125" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="102" y="394" class="t" text-anchor="middle">sandbox</text>
    <text x="102" y="412" class="t-sub" text-anchor="middle">\u5916\u90e8\u5bb9\u5668</text>
    <text x="102" y="426" class="t-sub" text-anchor="middle">Docker /</text>
    <text x="102" y="440" class="t-sub" text-anchor="middle">Firecracker</text>

    <rect x="170" y="376" width="125" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="232" y="394" class="t" text-anchor="middle">gateway</text>
    <text x="232" y="412" class="t-sub" text-anchor="middle">gateway \u8fdb\u7a0b</text>
    <text x="232" y="426" class="t-sub" text-anchor="middle">\u8f7b\u91cf fs</text>
    <text x="232" y="440" class="t-sub" text-anchor="middle">\u64cd\u4f5c</text>

    <rect x="300" y="376" width="125" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="362" y="394" class="t" text-anchor="middle">node</text>
    <text x="362" y="412" class="t-sub" text-anchor="middle">\u76f4\u63a5 host</text>
    <text x="362" y="426" class="t-sub" text-anchor="middle">\u4fe1\u4efb\u547d\u4ee4</text>
    <text x="362" y="440" class="t-sub" text-anchor="middle">git info</text>

    <rect x="40" y="468" width="390" height="80" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="235" y="486" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">\u6ca1\u81ea\u5e26 sandbox \u5b9e\u73b0</text>
    <text x="235" y="504" class="t-sub" text-anchor="middle">host \u4e0d\u8d70\u6c99\u7bb1 = \u6ca1\u6c99\u7bb1</text>
    <text x="235" y="518" class="t-sub" text-anchor="middle">\u4e0a\u5c42\u90e8\u7f72\u65b9\u6c89\u6dc0 sandbox</text>
    <text x="235" y="532" class="t-sub" text-anchor="middle">\u4ec5\u63d0\u4f9b\u62bd\u8c61</text>

    <rect x="470" y="320" width="410" height="240" rx="12" fill="#fdf6e3" stroke="#f97316" stroke-width="2.5" />
    <text x="490" y="344" class="t" fill="#f97316" font-weight="700">Hermes \u00b7 TERMINAL_ENV x6</text>
    <text x="490" y="362" class="t-sub">\u5916\u5305\u7ed9\u5bb9\u5668 / \u8fdc\u7a0b\u540e\u7aef</text>

    <rect x="490" y="376" width="180" height="170" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="580" y="394" class="t" text-anchor="middle">6 \u540e\u7aef</text>
    <text x="580" y="412" class="t-sub" text-anchor="middle">local (dev)</text>
    <text x="580" y="426" class="t-sub" text-anchor="middle">docker</text>
    <text x="580" y="440" class="t-sub" text-anchor="middle">singularity (HPC)</text>
    <text x="580" y="454" class="t-sub" text-anchor="middle">modal (serverless)</text>
    <text x="580" y="468" class="t-sub" text-anchor="middle">daytona (devenv)</text>
    <text x="580" y="482" class="t-sub" text-anchor="middle">ssh (remote VM)</text>

    <rect x="690" y="376" width="180" height="170" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="780" y="394" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">per-backend 5 \u7ef4\u5ea6</text>
    <text x="780" y="412" class="t-sub" text-anchor="middle">image</text>
    <text x="780" y="426" class="t-sub" text-anchor="middle">cpu / memory / disk</text>
    <text x="780" y="440" class="t-sub" text-anchor="middle">persistent (\u9ed8\u8ba4\u5f00)</text>
    <text x="780" y="454" class="t-sub" text-anchor="middle">timeout / lifetime</text>
    <text x="780" y="468" class="t-sub" text-anchor="middle">\u9ed8\u8ba4\u4e0d\u6302 host cwd</text>
    <text x="780" y="482" class="t-sub" text-anchor="middle">MOUNT_CWD opt-in</text>
  </g>
</svg>
"""

CHANNEL_SVG = r"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 600" width="100%" font-family="'Kalam','Comic Neue',sans-serif">
  <defs>
    <filter id="r14">
      <feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="29" />
      <feDisplacementMap in="SourceGraphic" scale="1.3" />
    </filter>
    <style>
      .t { font-size: 14px; fill: #1e293b; }
      .t-sub { font-size: 11px; fill: #475569; }
      .head { font-size: 18px; fill: #1e293b; font-weight: 700; }
    </style>
  </defs>

  <rect width="900" height="600" fill="#fffef7" />

  <text x="450" y="34" class="head" text-anchor="middle">\u591a\u901a\u9053\u5165\u53e3\uff1a\u4ece 5 \u4e2a binary \u5230 17 \u4e2a platform adapter</text>
  <text x="450" y="54" class="t-sub" text-anchor="middle">multi-binary \u00b7 commander \u5b50\u547d\u4ee4 \u00b7 channels-plugins \u00b7 17 platform adapter</text>

  <g filter="url(#r14)">
    <rect x="20" y="68" width="430" height="250" rx="12" fill="#fdf6e3" stroke="#0ea5e9" stroke-width="2.5" />
    <text x="40" y="92" class="t" fill="#0ea5e9" font-weight="700">Codex \u00b7 \u591a binary + UDS \u6865</text>
    <text x="40" y="110" class="t-sub">16+ \u5b50\u547d\u4ee4\uff0c\u6bcf\u79cd\u5165\u53e3\u72ec\u7acb\u5347\u7ea7</text>

    <rect x="40" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="130" y="142" class="t" text-anchor="middle">\u4ea4\u4e92\u578b</text>
    <text x="130" y="158" class="t-sub" text-anchor="middle">codex (TUI)</text>
    <text x="130" y="172" class="t-sub" text-anchor="middle">codex exec / e</text>
    <text x="130" y="186" class="t-sub" text-anchor="middle">codex review</text>
    <text x="130" y="200" class="t-sub" text-anchor="middle">codex resume / fork</text>

    <rect x="240" y="124" width="190" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="335" y="142" class="t" text-anchor="middle">\u670d\u52a1\u578b</text>
    <text x="335" y="158" class="t-sub" text-anchor="middle">codex mcp-server (stdio)</text>
    <text x="335" y="172" class="t-sub" text-anchor="middle">codex app-server (axum)</text>
    <text x="335" y="186" class="t-sub" text-anchor="middle">codex remote-control</text>
    <text x="335" y="200" class="t-sub" text-anchor="middle">codex exec-server</text>

    <rect x="40" y="216" width="390" height="90" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="235" y="234" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">stdio-to-uds \u6865</text>
    <text x="235" y="252" class="t-sub" text-anchor="middle">IDE \u542f\u5b50\u8fdb\u7a0b\u8d70 stdio \uff0c\u5b50\u8fdb\u7a0b\u5185\u90e8\u8d70 UDS</text>
    <text x="235" y="266" class="t-sub" text-anchor="middle">app-server \u5347\u7ea7\u4e0d\u9700\u91cd\u542f IDE</text>
    <text x="235" y="280" class="t-sub" text-anchor="middle">axum: HTTP1 + WebSocket \u5171\u5b58</text>
    <text x="235" y="294" class="t-sub" text-anchor="middle">+ codex app (desktop) + codex cloud</text>

    <rect x="470" y="68" width="410" height="250" rx="12" fill="#fdf6e3" stroke="#7c3aed" stroke-width="2.5" />
    <text x="490" y="92" class="t" fill="#7c3aed" font-weight="700">Claude Code \u00b7 \u5355 binary \u591a\u5b50\u547d\u4ee4</text>
    <text x="490" y="110" class="t-sub">main.tsx \u91cc\u585e\u6240\u6709 commander.command</text>

    <rect x="490" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="580" y="142" class="t" text-anchor="middle">\u4ea4\u4e92 / \u811a\u672c</text>
    <text x="580" y="158" class="t-sub" text-anchor="middle">claude (REPL ink)</text>
    <text x="580" y="172" class="t-sub" text-anchor="middle">claude -p / --print</text>
    <text x="580" y="186" class="t-sub" text-anchor="middle">claude --bare</text>
    <text x="580" y="200" class="t-sub" text-anchor="middle">claude --ide</text>

    <rect x="690" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="780" y="142" class="t" text-anchor="middle">\u5b50\u547d\u4ee4\u7ec4</text>
    <text x="780" y="158" class="t-sub" text-anchor="middle">claude mcp serve / list</text>
    <text x="780" y="172" class="t-sub" text-anchor="middle">claude server (HTTP+UDS)</text>
    <text x="780" y="186" class="t-sub" text-anchor="middle">claude auth / plugin</text>
    <text x="780" y="200" class="t-sub" text-anchor="middle">claude doctor / update</text>

    <rect x="490" y="216" width="380" height="90" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="680" y="234" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">--bare \u6781\u7b80\u6a21\u5f0f</text>
    <text x="680" y="252" class="t-sub" text-anchor="middle">\u8df3\u8fc7 hooks / LSP / plugin / attribution</text>
    <text x="680" y="266" class="t-sub" text-anchor="middle">\u8ba4\u8bc1\u53ea\u8d70 ANTHROPIC_API_KEY</text>
    <text x="680" y="280" class="t-sub" text-anchor="middle">CLAUDE_CODE_SIMPLE=1</text>
    <text x="680" y="294" class="t-sub" text-anchor="middle">\u7ed9 CI / SDK \u4e00\u4e2a\u5e72\u51c0\u5165\u53e3</text>

    <rect x="20" y="328" width="430" height="252" rx="12" fill="#fdf6e3" stroke="#16a34a" stroke-width="2.5" />
    <text x="40" y="352" class="t" fill="#16a34a" font-weight="700">OpenClaw \u00b7 sub-CLI + channels-plugins</text>
    <text x="40" y="370" class="t-sub">19 \u4e2a lazy-load sub-CLI + \u9891\u9053\u5373\u63d2\u4ef6</text>

    <rect x="40" y="384" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="130" y="402" class="t" text-anchor="middle">gateway daemon</text>
    <text x="130" y="418" class="t-sub" text-anchor="middle">\u957f\u8dd1 + WebSocket</text>
    <text x="130" y="432" class="t-sub" text-anchor="middle">hold session + state</text>
    <text x="130" y="446" class="t-sub" text-anchor="middle">RPC \u670d\u52a1\u7aef</text>
    <text x="130" y="460" class="t-sub" text-anchor="middle">openclaw gateway start</text>

    <rect x="240" y="384" width="190" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="335" y="402" class="t" text-anchor="middle">19 \u4e2a sub-CLI</text>
    <text x="335" y="418" class="t-sub" text-anchor="middle">acp / gateway / daemon</text>
    <text x="335" y="432" class="t-sub" text-anchor="middle">tui / logs / system</text>
    <text x="335" y="446" class="t-sub" text-anchor="middle">approvals / sandbox</text>
    <text x="335" y="460" class="t-sub" text-anchor="middle">channels / directory</text>

    <rect x="40" y="476" width="390" height="98" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="235" y="494" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">channels-plugins catalog</text>
    <text x="235" y="512" class="t-sub" text-anchor="middle">Telegram / Discord / Slack \u662f npm \u5305</text>
    <text x="235" y="526" class="t-sub" text-anchor="middle">openclaw plugins add @openclaw/channel-X</text>
    <text x="235" y="540" class="t-sub" text-anchor="middle">openclaw channels add X</text>
    <text x="235" y="554" class="t-sub" text-anchor="middle">+ ACP server (@agentclientprotocol/sdk)</text>
    <text x="235" y="568" class="t-sub" text-anchor="middle">\u751f\u6001\u505a\u65b0\u9891\u9053</text>

    <rect x="470" y="328" width="410" height="252" rx="12" fill="#fdf6e3" stroke="#f97316" stroke-width="2.5" />
    <text x="490" y="352" class="t" fill="#f97316" font-weight="700">Hermes \u00b7 17 platform adapter</text>
    <text x="490" y="370" class="t-sub">\u5168\u5185\u7f6e\u5728 gateway \u5355\u8fdb\u7a0b</text>

    <rect x="490" y="384" width="180" height="190" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="580" y="402" class="t" text-anchor="middle">17 platform</text>
    <text x="580" y="418" class="t-sub" text-anchor="middle">Telegram</text>
    <text x="580" y="432" class="t-sub" text-anchor="middle">Discord / Slack / Signal</text>
    <text x="580" y="446" class="t-sub" text-anchor="middle">WhatsApp / Matrix</text>
    <text x="580" y="460" class="t-sub" text-anchor="middle">Feishu / DingTalk / WeCom</text>
    <text x="580" y="474" class="t-sub" text-anchor="middle">Weixin / Mattermost</text>
    <text x="580" y="488" class="t-sub" text-anchor="middle">BlueBubbles / QQ</text>
    <text x="580" y="502" class="t-sub" text-anchor="middle">Email / SMS</text>
    <text x="580" y="516" class="t-sub" text-anchor="middle">HomeAssistant</text>
    <text x="580" y="530" class="t-sub" text-anchor="middle">API_SERVER (HTTP)</text>
    <text x="580" y="544" class="t-sub" text-anchor="middle">WEBHOOK (inbound)</text>
    <text x="580" y="558" class="t-sub" text-anchor="middle">+ TUI gateway + mcp_serve.py</text>

    <rect x="690" y="384" width="180" height="190" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="780" y="402" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">BasePlatformAdapter</text>
    <text x="780" y="418" class="t-sub" text-anchor="middle">6 abstract methods</text>
    <text x="780" y="432" class="t-sub" text-anchor="middle">connect / disconnect</text>
    <text x="780" y="446" class="t-sub" text-anchor="middle">send / send_typing</text>
    <text x="780" y="460" class="t-sub" text-anchor="middle">send_image / get_chat_info</text>
    <text x="780" y="478" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">check_X_requirements()</text>
    <text x="780" y="496" class="t-sub" text-anchor="middle">\u7f3a\u4f9d\u8d56\u6e29\u67d4\u8df3\u8fc7</text>
    <text x="780" y="510" class="t-sub" text-anchor="middle">\u8b66\u544a\u4e0d fatal</text>
    <text x="780" y="528" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">extras</text>
    <text x="780" y="544" class="t-sub" text-anchor="middle">hermes[slack]</text>
    <text x="780" y="558" class="t-sub" text-anchor="middle">hermes[discord]</text>
  </g>
</svg>
"""

OBSERVE_SVG = r"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 600" width="100%" font-family="'Kalam','Comic Neue',sans-serif">
  <defs>
    <filter id="r15">
      <feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="35" />
      <feDisplacementMap in="SourceGraphic" scale="1.3" />
    </filter>
    <style>
      .t { font-size: 14px; fill: #1e293b; }
      .t-sub { font-size: 11px; fill: #475569; }
      .head { font-size: 18px; fill: #1e293b; font-weight: 700; }
    </style>
  </defs>

  <rect width="900" height="600" fill="#fffef7" />

  <text x="450" y="34" class="head" text-anchor="middle">\u89c2\u6d4b\u3001\u6210\u672c\u4e0e\u65e5\u5fd7\uff1a\u4ece 3 crate \u5230 5 source \u4f18\u5148\u7ea7</text>
  <text x="450" y="54" class="t-sub" text-anchor="middle">OTEL+analytics+trace \u00b7 modelCost+insights \u00b7 DiagnosticEvent x13 \u00b7 CanonicalUsage+5 source</text>

  <g filter="url(#r15)">
    <rect x="20" y="68" width="430" height="250" rx="12" fill="#fdf6e3" stroke="#0ea5e9" stroke-width="2.5" />
    <text x="40" y="92" class="t" fill="#0ea5e9" font-weight="700">Codex \u00b7 3 \u4e2a\u72ec\u7acb crate</text>
    <text x="40" y="110" class="t-sub">\u5206\u5de5\u6e05\u6670\uff1ahot path \u53ea\u5199 raw event</text>

    <rect x="40" y="124" width="125" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="102" y="142" class="t" text-anchor="middle">codex-otel</text>
    <text x="102" y="158" class="t-sub" text-anchor="middle">OTLP HTTP / gRPC</text>
    <text x="102" y="172" class="t-sub" text-anchor="middle">Statsig default</text>
    <text x="102" y="186" class="t-sub" text-anchor="middle">None / runtime</text>
    <text x="102" y="200" class="t-sub" text-anchor="middle">metrics</text>

    <rect x="170" y="124" width="125" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="232" y="142" class="t" text-anchor="middle">codex-analytics</text>
    <text x="232" y="158" class="t-sub" text-anchor="middle">TrackEventRequest</text>
    <text x="232" y="172" class="t-sub" text-anchor="middle">x 20+ variants</text>
    <text x="232" y="186" class="t-sub" text-anchor="middle">SkillInvocation</text>
    <text x="232" y="200" class="t-sub" text-anchor="middle">AcceptedLine...</text>

    <rect x="300" y="124" width="125" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="362" y="142" class="t" text-anchor="middle">rollout-trace</text>
    <text x="362" y="158" class="t-sub" text-anchor="middle">trace.jsonl</text>
    <text x="362" y="172" class="t-sub" text-anchor="middle">+ manifest</text>
    <text x="362" y="186" class="t-sub" text-anchor="middle">reducer</text>
    <text x="362" y="200" class="t-sub" text-anchor="middle">offline replay</text>

    <rect x="40" y="216" width="390" height="90" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="235" y="234" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">debug build \u9ed8\u8ba4\u5173\u4e0a\u62a5</text>
    <text x="235" y="252" class="t-sub" text-anchor="middle">cfg!(debug_assertions) =&gt; OtelExporter::None</text>
    <text x="235" y="266" class="t-sub" text-anchor="middle">\u6d4b\u8bd5\u4e0d\u6c61\u67d3\u751f\u4ea7\u6307\u6807</text>
    <text x="235" y="280" class="t-sub" text-anchor="middle">+ AcceptedLineFingerprints</text>
    <text x="235" y="294" class="t-sub" text-anchor="middle">\u5ea6\u91cf\u6a21\u578b\u751f\u6210\u4ee3\u7801\u88ab\u63a5\u53d7\u7387</text>

    <rect x="470" y="68" width="410" height="250" rx="12" fill="#fdf6e3" stroke="#7c3aed" stroke-width="2.5" />
    <text x="490" y="92" class="t" fill="#7c3aed" font-weight="700">Claude Code \u00b7 modelCost + /insights</text>
    <text x="490" y="110" class="t-sub">\u786c\u7f16\u7801\u4ef7\u683c + Opus \u81ea\u6211\u5206\u6790</text>

    <rect x="490" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="580" y="142" class="t" text-anchor="middle">5 cost tier</text>
    <text x="580" y="158" class="t-sub" text-anchor="middle">TIER_3_15 (Sonnet)</text>
    <text x="580" y="172" class="t-sub" text-anchor="middle">TIER_15_75 (Opus 4)</text>
    <text x="580" y="186" class="t-sub" text-anchor="middle">TIER_5_25 (Opus 4.5)</text>
    <text x="580" y="200" class="t-sub" text-anchor="middle">TIER_30_150 (fast)</text>

    <rect x="690" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="780" y="142" class="t" text-anchor="middle">5 \u7ef4\u5ea6\u5355\u4ef7</text>
    <text x="780" y="158" class="t-sub" text-anchor="middle">input / output</text>
    <text x="780" y="172" class="t-sub" text-anchor="middle">cache_read</text>
    <text x="780" y="186" class="t-sub" text-anchor="middle">cache_write</text>
    <text x="780" y="200" class="t-sub" text-anchor="middle">web_search (per call)</text>

    <rect x="490" y="216" width="380" height="90" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="680" y="234" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">unknown \u6a21\u578b fallback</text>
    <text x="680" y="252" class="t-sub" text-anchor="middle">trackUnknownModelCost('tengu_unknown_model_cost')</text>
    <text x="680" y="266" class="t-sub" text-anchor="middle">fallback \u9ed8\u8ba4\u6a21\u578b\u5355\u4ef7</text>
    <text x="680" y="280" class="t-sub" text-anchor="middle">+ /insights (queryWithModel Opus x 2)</text>
    <text x="680" y="294" class="t-sub" text-anchor="middle">+ ~/.claude/projects/ sessionStorage</text>

    <rect x="20" y="328" width="430" height="252" rx="12" fill="#fdf6e3" stroke="#16a34a" stroke-width="2.5" />
    <text x="40" y="352" class="t" fill="#16a34a" font-weight="700">OpenClaw \u00b7 13 \u7c7b DiagnosticEvent</text>
    <text x="40" y="370" class="t-sub">global listener + \u9012\u5f52 guard 100</text>

    <rect x="40" y="384" width="180" height="100" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="130" y="402" class="t" text-anchor="middle">13 event types</text>
    <text x="130" y="418" class="t-sub" text-anchor="middle">model.usage</text>
    <text x="130" y="432" class="t-sub" text-anchor="middle">webhook.* (3)</text>
    <text x="130" y="446" class="t-sub" text-anchor="middle">message.* (2)</text>
    <text x="130" y="460" class="t-sub" text-anchor="middle">session.* (2)</text>
    <text x="130" y="474" class="t-sub" text-anchor="middle">queue.lane.* (2)</text>

    <rect x="240" y="384" width="190" height="100" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="335" y="402" class="t" text-anchor="middle">tool.loop detector</text>
    <text x="335" y="418" class="t-sub" text-anchor="middle">generic_repeat</text>
    <text x="335" y="432" class="t-sub" text-anchor="middle">known_poll_no_progress</text>
    <text x="335" y="446" class="t-sub" text-anchor="middle">global_circuit_breaker</text>
    <text x="335" y="460" class="t-sub" text-anchor="middle">ping_pong</text>
    <text x="335" y="474" class="t-sub" text-anchor="middle">level: warn / critical</text>

    <rect x="40" y="496" width="390" height="78" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="235" y="514" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">emitDiagnosticEvent</text>
    <text x="235" y="532" class="t-sub" text-anchor="middle">\u81ea\u52a8\u6ce8 seq + ts</text>
    <text x="235" y="546" class="t-sub" text-anchor="middle">try/catch \u9694\u79bb listener \u5f02\u5e38</text>
    <text x="235" y="560" class="t-sub" text-anchor="middle">depth &gt; 100 =&gt; drop event</text>

    <rect x="470" y="328" width="410" height="252" rx="12" fill="#fdf6e3" stroke="#f97316" stroke-width="2.5" />
    <text x="490" y="352" class="t" fill="#f97316" font-weight="700">Hermes \u00b7 5 \u4f18\u5148\u7ea7\u4ef7\u683c\u8868</text>
    <text x="490" y="370" class="t-sub">CanonicalUsage + PricingEntry + CostResult</text>

    <rect x="490" y="384" width="180" height="100" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="580" y="402" class="t" text-anchor="middle">CanonicalUsage</text>
    <text x="580" y="418" class="t-sub" text-anchor="middle">input_tokens</text>
    <text x="580" y="432" class="t-sub" text-anchor="middle">output_tokens</text>
    <text x="580" y="446" class="t-sub" text-anchor="middle">cache_read_tokens</text>
    <text x="580" y="460" class="t-sub" text-anchor="middle">cache_write_tokens</text>
    <text x="580" y="474" class="t-sub" text-anchor="middle">reasoning_tokens</text>

    <rect x="690" y="384" width="180" height="100" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="780" y="402" class="t" text-anchor="middle">5 CostSource</text>
    <text x="780" y="418" class="t-sub" text-anchor="middle">1. provider_cost_api</text>
    <text x="780" y="432" class="t-sub" text-anchor="middle">2. generation_api</text>
    <text x="780" y="446" class="t-sub" text-anchor="middle">3. models_api</text>
    <text x="780" y="460" class="t-sub" text-anchor="middle">4. docs_snapshot</text>
    <text x="780" y="474" class="t-sub" text-anchor="middle">5. user_override</text>

    <rect x="490" y="496" width="380" height="78" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="680" y="514" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">CostStatus 4 \u72b6\u6001</text>
    <text x="680" y="532" class="t-sub" text-anchor="middle">actual / estimated / included / unknown</text>
    <text x="680" y="546" class="t-sub" text-anchor="middle">+ pricing_version + source_url + fetched_at</text>
    <text x="680" y="560" class="t-sub" text-anchor="middle">SQLite + /insights (\u672c\u5730\u7ec8\u7aef\u62a5\u8868)</text>
  </g>
</svg>
"""

MEMORY_SVG = r"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 600" width="100%" font-family="'Kalam','Comic Neue',sans-serif">
  <defs>
    <filter id="r16">
      <feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="42" />
      <feDisplacementMap in="SourceGraphic" scale="1.3" />
    </filter>
    <style>
      .t { font-size: 14px; fill: #1e293b; }
      .t-sub { font-size: 11px; fill: #475569; }
      .head { font-size: 18px; fill: #1e293b; font-weight: 700; }
    </style>
  </defs>

  <rect width="900" height="600" fill="#fffef7" />

  <text x="450" y="34" class="head" text-anchor="middle">\u8bb0\u5fc6\u7cfb\u7edf\uff1a\u4ece AGENTS.md \u6ce8\u5165\u5230\u53cc\u7d22\u5f15 + \u65f6\u95f4\u8870\u51cf</text>
  <text x="450" y="54" class="t-sub" text-anchor="middle">stage1+phase2 \u00b7 4 type+2 mode \u00b7 FTS5+vec+decay \u00b7 2200/1375 char frozen snapshot</text>

  <g filter="url(#r16)">
    <rect x="20" y="68" width="430" height="250" rx="12" fill="#fdf6e3" stroke="#0ea5e9" stroke-width="2.5" />
    <text x="40" y="92" class="t" fill="#0ea5e9" font-weight="700">Codex \u00b7 AGENTS.md + \u540e\u53f0\u4e24\u9636\u6bb5</text>
    <text x="40" y="110" class="t-sub">\u6ce8\u5165 + LLM pipeline \u53cc\u8def</text>

    <rect x="40" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="130" y="142" class="t" text-anchor="middle">UserInstructions</text>
    <text x="130" y="158" class="t-sub" text-anchor="middle">AGENTS.md \u8bfb\u53d6</text>
    <text x="130" y="172" class="t-sub" text-anchor="middle">role=user</text>
    <text x="130" y="186" class="t-sub" text-anchor="middle">START_MARKER +</text>
    <text x="130" y="200" class="t-sub" text-anchor="middle">&lt;INSTRUCTIONS&gt;</text>

    <rect x="240" y="124" width="195" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="337" y="142" class="t" text-anchor="middle">stage1_outputs</text>
    <text x="337" y="158" class="t-sub" text-anchor="middle">thread \u7c92\u5ea6</text>
    <text x="337" y="172" class="t-sub" text-anchor="middle">+ cwd / git_branch</text>
    <text x="337" y="186" class="t-sub" text-anchor="middle">5 ClaimOutcome</text>
    <text x="337" y="200" class="t-sub" text-anchor="middle">lease + retry x3</text>

    <rect x="40" y="216" width="390" height="90" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="235" y="234" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">Phase2 \u5168\u5c40 consolidate</text>
    <text x="235" y="252" class="t-sub" text-anchor="middle">global lock + input_watermark</text>
    <text x="235" y="266" class="t-sub" text-anchor="middle">6h cooldown (PHASE2_SUCCESS_COOLDOWN_SECONDS)</text>
    <text x="235" y="280" class="t-sub" text-anchor="middle">+ MemoryCitation \u53cd\u67e5 thread</text>
    <text x="235" y="294" class="t-sub" text-anchor="middle">clear_memory_data \u4e00\u4e8b\u52a1\u6e05\u4e24\u8868</text>

    <rect x="470" y="68" width="410" height="250" rx="12" fill="#fdf6e3" stroke="#7c3aed" stroke-width="2.5" />
    <text x="490" y="92" class="t" fill="#7c3aed" font-weight="700">Claude Code \u00b7 4 MemoryType + 2 mode</text>
    <text x="490" y="110" class="t-sub">eval \u9a71\u52a8 prompt \u8bbe\u8ba1</text>

    <rect x="490" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="580" y="142" class="t" text-anchor="middle">4 MEMORY_TYPES</text>
    <text x="580" y="158" class="t-sub" text-anchor="middle">user (always private)</text>
    <text x="580" y="172" class="t-sub" text-anchor="middle">feedback (private/team)</text>
    <text x="580" y="186" class="t-sub" text-anchor="middle">project (team-biased)</text>
    <text x="580" y="200" class="t-sub" text-anchor="middle">reference (usually team)</text>

    <rect x="690" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="780" y="142" class="t" text-anchor="middle">2 prompt mode</text>
    <text x="780" y="158" class="t-sub" text-anchor="middle">COMBINED</text>
    <text x="780" y="172" class="t-sub" text-anchor="middle">(private + team)</text>
    <text x="780" y="186" class="t-sub" text-anchor="middle">INDIVIDUAL</text>
    <text x="780" y="200" class="t-sub" text-anchor="middle">(no scope)</text>

    <rect x="490" y="216" width="380" height="90" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="680" y="234" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">DRIFT_CAVEAT + Before recommending</text>
    <text x="680" y="252" class="t-sub" text-anchor="middle">file path =&gt; \u68c0\u67e5\u5b58\u5728</text>
    <text x="680" y="266" class="t-sub" text-anchor="middle">function/flag =&gt; grep</text>
    <text x="680" y="280" class="t-sub" text-anchor="middle">act on it =&gt; verify first</text>
    <text x="680" y="294" class="t-sub" text-anchor="middle">eval H1: 0/3 =&gt; 3/3 \u72ec\u7acb\u5206\u533a\u540e</text>

    <rect x="20" y="328" width="430" height="252" rx="12" fill="#fdf6e3" stroke="#16a34a" stroke-width="2.5" />
    <text x="40" y="352" class="t" fill="#16a34a" font-weight="700">OpenClaw \u00b7 \u53cc\u7d22\u5f15 + \u65f6\u95f4\u8870\u51cf</text>
    <text x="40" y="370" class="t-sub">\u68c0\u7d22\u4e0a\u9650\uff1aMEMORY.md + qmd scope</text>

    <rect x="40" y="384" width="180" height="100" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="130" y="402" class="t" text-anchor="middle">SQLite + 2 index</text>
    <text x="130" y="418" class="t-sub" text-anchor="middle">files / chunks</text>
    <text x="130" y="432" class="t-sub" text-anchor="middle">+ FTS5 virtual</text>
    <text x="130" y="446" class="t-sub" text-anchor="middle">+ sqlite-vec</text>
    <text x="130" y="460" class="t-sub" text-anchor="middle">+ embedding_cache</text>
    <text x="130" y="474" class="t-sub" text-anchor="middle">source: memory/sessions</text>

    <rect x="240" y="384" width="190" height="100" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="335" y="402" class="t" text-anchor="middle">temporal decay</text>
    <text x="335" y="418" class="t-sub" text-anchor="middle">halfLifeDays=30</text>
    <text x="335" y="432" class="t-sub" text-anchor="middle">lambda = ln2 / halfLife</text>
    <text x="335" y="446" class="t-sub" text-anchor="middle">memory/YYYY-MM-DD.md</text>
    <text x="335" y="460" class="t-sub" text-anchor="middle">=&gt; decay</text>
    <text x="335" y="474" class="t-sub" text-anchor="middle">MEMORY.md =&gt; evergreen</text>

    <rect x="40" y="496" width="390" height="78" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="235" y="514" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">qmd scope + hybrid retrieval</text>
    <text x="235" y="532" class="t-sub" text-anchor="middle">query-driven memory directory</text>
    <text x="235" y="546" class="t-sub" text-anchor="middle">semantic + lexical + MMR + decay</text>
    <text x="235" y="560" class="t-sub" text-anchor="middle">memory_search tool: Mandatory recall</text>

    <rect x="470" y="328" width="410" height="252" rx="12" fill="#fdf6e3" stroke="#f97316" stroke-width="2.5" />
    <text x="490" y="352" class="t" fill="#f97316" font-weight="700">Hermes \u00b7 \u53cc\u6587\u4ef6 + frozen snapshot</text>
    <text x="490" y="370" class="t-sub">2 \u6587\u4ef6 + 4 action + 11 \u626b\u63cf</text>

    <rect x="490" y="384" width="180" height="100" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="580" y="402" class="t" text-anchor="middle">MEMORY.md</text>
    <text x="580" y="418" class="t-sub" text-anchor="middle">2200 \u5b57\u7b26</text>
    <text x="580" y="432" class="t-sub" text-anchor="middle">USER.md</text>
    <text x="580" y="446" class="t-sub" text-anchor="middle">1375 \u5b57\u7b26</text>
    <text x="580" y="460" class="t-sub" text-anchor="middle">delimiter: \u00a7</text>
    <text x="580" y="474" class="t-sub" text-anchor="middle">char != token</text>

    <rect x="690" y="384" width="180" height="100" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="780" y="402" class="t" text-anchor="middle">_system_prompt</text>
    <text x="780" y="418" class="t-sub" text-anchor="middle">_snapshot frozen</text>
    <text x="780" y="432" class="t-sub" text-anchor="middle">at load_from_disk()</text>
    <text x="780" y="446" class="t-sub" text-anchor="middle">mid-session write</text>
    <text x="780" y="460" class="t-sub" text-anchor="middle">=&gt; disk only</text>
    <text x="780" y="474" class="t-sub" text-anchor="middle">prefix cache safe</text>

    <rect x="490" y="496" width="380" height="78" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="680" y="514" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">11 _MEMORY_THREAT_PATTERNS</text>
    <text x="680" y="532" class="t-sub" text-anchor="middle">prompt injection / role hijack / curl exfil</text>
    <text x="680" y="546" class="t-sub" text-anchor="middle">authorized_keys / ~/.ssh / hermes_env</text>
    <text x="680" y="560" class="t-sub" text-anchor="middle">+ 10 invisible unicode \u67e5\u6740</text>
  </g>
</svg>
"""

SKILLS_SVG = r"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 600" width="100%" font-family="'Kalam','Comic Neue',sans-serif">
  <defs>
    <filter id="r17">
      <feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="51" />
      <feDisplacementMap in="SourceGraphic" scale="1.3" />
    </filter>
    <style>
      .t { font-size: 14px; fill: #1e293b; }
      .t-sub { font-size: 11px; fill: #475569; }
      .head { font-size: 18px; fill: #1e293b; font-weight: 700; }
    </style>
  </defs>

  <rect width="900" height="600" fill="#fffef7" />

  <text x="450" y="34" class="head" text-anchor="middle">Skill \u7cfb\u7edf\uff1a\u4ece metadata schema \u5230\u5b8c\u6574 supply chain</text>
  <text x="450" y="54" class="t-sub" text-anchor="middle">8 crate + scope/policy \u00b7 17 bundled + skillify \u00b7 scanner + install \u00b7 4 trust x 3 verdict</text>

  <g filter="url(#r17)">
    <rect x="20" y="68" width="430" height="250" rx="12" fill="#fdf6e3" stroke="#0ea5e9" stroke-width="2.5" />
    <text x="40" y="92" class="t" fill="#0ea5e9" font-weight="700">Codex \u00b7 8 crate \u7ec6\u62c6</text>
    <text x="40" y="110" class="t-sub">SkillMetadata + Scope + Policy + Dependencies</text>

    <rect x="40" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="130" y="142" class="t" text-anchor="middle">SkillScope x 4</text>
    <text x="130" y="158" class="t-sub" text-anchor="middle">user / project</text>
    <text x="130" y="172" class="t-sub" text-anchor="middle">org / bundled</text>
    <text x="130" y="186" class="t-sub" text-anchor="middle">+ SkillPolicy</text>
    <text x="130" y="200" class="t-sub" text-anchor="middle">products gating</text>

    <rect x="240" y="124" width="195" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="337" y="142" class="t" text-anchor="middle">SkillDependencies</text>
    <text x="337" y="158" class="t-sub" text-anchor="middle">tools[]: type</text>
    <text x="337" y="172" class="t-sub" text-anchor="middle">+ transport</text>
    <text x="337" y="186" class="t-sub" text-anchor="middle">+ command / url</text>
    <text x="337" y="200" class="t-sub" text-anchor="middle">env var \u81ea\u52a8 RequestUserInput</text>

    <rect x="40" y="216" width="390" height="90" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="235" y="234" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">implicit invocation</text>
    <text x="235" y="252" class="t-sub" text-anchor="middle">allow_implicit_invocation \u9ed8\u8ba4 true</text>
    <text x="235" y="266" class="t-sub" text-anchor="middle">detect_implicit_skill_invocation_for_command</text>
    <text x="235" y="280" class="t-sub" text-anchor="middle">\u547d\u4ee4\u53cd\u5411\u5339\u914d skill</text>
    <text x="235" y="294" class="t-sub" text-anchor="middle">disabled_paths \u4e0d\u5220\u53ea\u9690</text>

    <rect x="470" y="68" width="410" height="250" rx="12" fill="#fdf6e3" stroke="#7c3aed" stroke-width="2.5" />
    <text x="490" y="92" class="t" fill="#7c3aed" font-weight="700">Claude Code \u00b7 17 bundled + skillify</text>
    <text x="490" y="110" class="t-sub">\u4ece session \u6c89\u6dc0 skill \u7684 meta-skill</text>

    <rect x="490" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="580" y="142" class="t" text-anchor="middle">17 bundled</text>
    <text x="580" y="158" class="t-sub" text-anchor="middle">loop / verify / stuck</text>
    <text x="580" y="172" class="t-sub" text-anchor="middle">remember / debug</text>
    <text x="580" y="186" class="t-sub" text-anchor="middle">batch / simplify</text>
    <text x="580" y="200" class="t-sub" text-anchor="middle">skillify (\u6c89\u6dc0)</text>

    <rect x="690" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="780" y="142" class="t" text-anchor="middle">skillify 4 round</text>
    <text x="780" y="158" class="t-sub" text-anchor="middle">R1: name + desc</text>
    <text x="780" y="172" class="t-sub" text-anchor="middle">R2: \u6b65\u9aa4 + arg</text>
    <text x="780" y="186" class="t-sub" text-anchor="middle">R3: \u6bcf\u6b65\u62c6\u89e3</text>
    <text x="780" y="200" class="t-sub" text-anchor="middle">R4: trigger \u7ec8\u5ba1</text>

    <rect x="490" y="216" width="380" height="90" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="680" y="234" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">frontmatter \u516c\u7ea6</text>
    <text x="680" y="252" class="t-sub" text-anchor="middle">when_to_use: "Use when..."</text>
    <text x="680" y="266" class="t-sub" text-anchor="middle">allowed-tools: Bash(gh:*)</text>
    <text x="680" y="280" class="t-sub" text-anchor="middle">context: inline | fork</text>
    <text x="680" y="294" class="t-sub" text-anchor="middle">success criteria \u6bcf\u6b65 required</text>

    <rect x="20" y="328" width="430" height="252" rx="12" fill="#fdf6e3" stroke="#16a34a" stroke-width="2.5" />
    <text x="40" y="352" class="t" fill="#16a34a" font-weight="700">OpenClaw \u00b7 scanner + install</text>
    <text x="40" y="370" class="t-sub">\u5b8c\u6574 supply chain</text>

    <rect x="40" y="384" width="180" height="100" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="130" y="402" class="t" text-anchor="middle">skill-scanner</text>
    <text x="130" y="418" class="t-sub" text-anchor="middle">3 severity</text>
    <text x="130" y="432" class="t-sub" text-anchor="middle">info / warn / critical</text>
    <text x="130" y="446" class="t-sub" text-anchor="middle">8 ext: js/ts/mjs...</text>
    <text x="130" y="460" class="t-sub" text-anchor="middle">FILE_SCAN_CACHE 5000</text>
    <text x="130" y="474" class="t-sub" text-anchor="middle">maxFileBytes 1MB</text>

    <rect x="240" y="384" width="190" height="100" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="335" y="402" class="t" text-anchor="middle">skills-install</text>
    <text x="335" y="418" class="t-sub" text-anchor="middle">download + tar verbose</text>
    <text x="335" y="432" class="t-sub" text-anchor="middle">+ brew \u68c0\u6d4b</text>
    <text x="335" y="446" class="t-sub" text-anchor="middle">+ workspace skill</text>
    <text x="335" y="460" class="t-sub" text-anchor="middle">vs bundled allowlist</text>
    <text x="335" y="474" class="t-sub" text-anchor="middle">+ pi-embedded runtime</text>

    <rect x="40" y="496" width="390" height="78" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="235" y="514" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">critical =&gt; WARNING blocking</text>
    <text x="235" y="532" class="t-sub" text-anchor="middle">warn =&gt; \u63d0\u793a audit --deep</text>
    <text x="235" y="546" class="t-sub" text-anchor="middle">scan \u5931\u8d25 =&gt; \u8b66\u544a\u4f46\u4e0d\u5835\u5b89\u88c5</text>
    <text x="235" y="560" class="t-sub" text-anchor="middle">audit trail \u53ef\u67e5</text>

    <rect x="470" y="328" width="410" height="252" rx="12" fill="#fdf6e3" stroke="#f97316" stroke-width="2.5" />
    <text x="490" y="352" class="t" fill="#f97316" font-weight="700">Hermes \u00b7 trust 4 x verdict 3</text>
    <text x="490" y="370" class="t-sub">12 \u683c INSTALL_POLICY</text>

    <rect x="490" y="384" width="180" height="100" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="580" y="402" class="t" text-anchor="middle">4 trust level</text>
    <text x="580" y="418" class="t-sub" text-anchor="middle">builtin (always)</text>
    <text x="580" y="432" class="t-sub" text-anchor="middle">trusted (openai/anth)</text>
    <text x="580" y="446" class="t-sub" text-anchor="middle">community</text>
    <text x="580" y="460" class="t-sub" text-anchor="middle">agent-created</text>
    <text x="580" y="474" class="t-sub" text-anchor="middle">=&gt; ask user</text>

    <rect x="690" y="384" width="180" height="100" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="780" y="402" class="t" text-anchor="middle">progressive disclosure</text>
    <text x="780" y="418" class="t-sub" text-anchor="middle">name \u2264 64</text>
    <text x="780" y="432" class="t-sub" text-anchor="middle">description \u2264 1024</text>
    <text x="780" y="446" class="t-sub" text-anchor="middle">list = metadata only</text>
    <text x="780" y="460" class="t-sub" text-anchor="middle">view = lazy load</text>
    <text x="780" y="474" class="t-sub" text-anchor="middle">agentskills.io compat</text>

    <rect x="490" y="496" width="380" height="78" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="680" y="514" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">platforms \u9650\u5b9a OS \u52a0\u8f7d</text>
    <text x="680" y="532" class="t-sub" text-anchor="middle">macos / linux / windows</text>
    <text x="680" y="546" class="t-sub" text-anchor="middle">prerequisites.env_vars / commands</text>
    <text x="680" y="560" class="t-sub" text-anchor="middle">~/.hermes/skills/ \u5355\u6839\u76ee\u5f55</text>
  </g>
</svg>
"""

CRON_SVG = r"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 600" width="100%" font-family="'Kalam','Comic Neue',sans-serif">
  <defs>
    <filter id="r18">
      <feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="60" />
      <feDisplacementMap in="SourceGraphic" scale="1.3" />
    </filter>
    <style>
      .t { font-size: 14px; fill: #1e293b; }
      .t-sub { font-size: 11px; fill: #475569; }
      .head { font-size: 18px; fill: #1e293b; font-weight: 700; }
    </style>
  </defs>

  <rect width="900" height="600" fill="#fffef7" />

  <text x="450" y="34" class="head" text-anchor="middle">Cron \u4e0e\u540e\u53f0\u4efb\u52a1\uff1a\u4ece cloud task \u8868\u5230\u672c\u5730 1s tick</text>
  <text x="450" y="54" class="t-sub" text-anchor="middle">cloud-tasks \u00b7 CronCreateTool + scheduler \u00b7 service + isolated-agent \u00b7 croniter + jobs.json</text>

  <g filter="url(#r18)">
    <rect x="20" y="68" width="430" height="250" rx="12" fill="#fdf6e3" stroke="#0ea5e9" stroke-width="2.5" />
    <text x="40" y="92" class="t" fill="#0ea5e9" font-weight="700">Codex \u00b7 cloud-tasks \u5355\u72ec binary</text>
    <text x="40" y="110" class="t-sub">\u672c\u5730\u4e0d\u505a cron\uff0c\u7ed9\u4e91</text>

    <rect x="40" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="130" y="142" class="t" text-anchor="middle">cloud-tasks</text>
    <text x="130" y="158" class="t-sub" text-anchor="middle">TaskSummary</text>
    <text x="130" y="172" class="t-sub" text-anchor="middle">TaskId</text>
    <text x="130" y="186" class="t-sub" text-anchor="middle">EnvironmentRow</text>
    <text x="130" y="200" class="t-sub" text-anchor="middle">is_pinned</text>

    <rect x="240" y="124" width="195" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="337" y="142" class="t" text-anchor="middle">best-of-N</text>
    <text x="337" y="158" class="t-sub" text-anchor="middle">BestOfModalState</text>
    <text x="337" y="172" class="t-sub" text-anchor="middle">\u591a\u5206\u652f\u5e76\u884c</text>
    <text x="337" y="186" class="t-sub" text-anchor="middle">UI \u9009\u6700\u4f18 apply</text>
    <text x="337" y="200" class="t-sub" text-anchor="middle">ApplyResultLevel x3</text>

    <rect x="40" y="216" width="390" height="90" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="235" y="234" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">\u8bbe\u8ba1\u4ec0\u4e48</text>
    <text x="235" y="252" class="t-sub" text-anchor="middle">\u672c\u5730 = \u5f00\u53d1\u5de5\u5177\uff08REPL\uff09</text>
    <text x="235" y="266" class="t-sub" text-anchor="middle">\u4e91 = \u957f\u8dd1\u4efb\u52a1 + best-of-N</text>
    <text x="235" y="280" class="t-sub" text-anchor="middle">ApplyModalState \u8bb0 conflict/skipped</text>
    <text x="235" y="294" class="t-sub" text-anchor="middle">EnvironmentRow pin \u9879\u76ee</text>

    <rect x="470" y="68" width="410" height="250" rx="12" fill="#fdf6e3" stroke="#7c3aed" stroke-width="2.5" />
    <text x="490" y="92" class="t" fill="#7c3aed" font-weight="700">Claude Code \u00b7 CronCreateTool + scheduler</text>
    <text x="490" y="110" class="t-sub">1s tick + chokidar + scheduler lock</text>

    <rect x="490" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="580" y="142" class="t" text-anchor="middle">CronTask</text>
    <text x="580" y="158" class="t-sub" text-anchor="middle">5-field cron</text>
    <text x="580" y="172" class="t-sub" text-anchor="middle">recurring vs one-shot</text>
    <text x="580" y="186" class="t-sub" text-anchor="middle">durable vs session</text>
    <text x="580" y="200" class="t-sub" text-anchor="middle">permanent \u9501</text>

    <rect x="690" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="780" y="142" class="t" text-anchor="middle">scheduler lock</text>
    <text x="780" y="158" class="t-sub" text-anchor="middle">\u8de8\u8fdb\u7a0b\u4e92\u65a5</text>
    <text x="780" y="172" class="t-sub" text-anchor="middle">PROBE 5s</text>
    <text x="780" y="186" class="t-sub" text-anchor="middle">\u63a5\u63a5\u638b\u5b50</text>
    <text x="780" y="200" class="t-sub" text-anchor="middle">recurringMaxAge 30d</text>

    <rect x="490" y="216" width="380" height="90" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="680" y="234" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">assistant mode \u96b1\u8eab\u4efb\u52a1</text>
    <text x="680" y="252" class="t-sub" text-anchor="middle">morning-checkin / dream / catch-up</text>
    <text x="680" y="266" class="t-sub" text-anchor="middle">permanent: true \u5165\u53e3</text>
    <text x="680" y="280" class="t-sub" text-anchor="middle">install.ts \u624d\u80fd\u521b\u5efa</text>
    <text x="680" y="294" class="t-sub" text-anchor="middle">CronCreateTool \u5199\u4e0d\u4e86\u8fd9\u4f4d</text>

    <rect x="20" y="328" width="430" height="252" rx="12" fill="#fdf6e3" stroke="#16a34a" stroke-width="2.5" />
    <text x="40" y="352" class="t" fill="#16a34a" font-weight="700">OpenClaw \u00b7 cron \u5b50\u7cfb\u7edf 100+ \u6587\u4ef6</text>
    <text x="40" y="370" class="t-sub">at/every/cron 3 \u6a21\u5f0f + isolated-agent</text>

    <rect x="40" y="384" width="180" height="100" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="130" y="402" class="t" text-anchor="middle">CronSchedule x3</text>
    <text x="130" y="418" class="t-sub" text-anchor="middle">at: \u67d0\u65f6\u70b9</text>
    <text x="130" y="432" class="t-sub" text-anchor="middle">every: ms</text>
    <text x="130" y="446" class="t-sub" text-anchor="middle">cron: tz + staggerMs</text>
    <text x="130" y="460" class="t-sub" text-anchor="middle">+ deterministic stagger</text>
    <text x="130" y="474" class="t-sub" text-anchor="middle">\u9632\u9f50\u53d1\u96ea\u5d29</text>

    <rect x="240" y="384" width="190" height="100" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="335" y="402" class="t" text-anchor="middle">isolated-agent</text>
    <text x="335" y="418" class="t-sub" text-anchor="middle">\u72ec\u7acb session</text>
    <text x="335" y="432" class="t-sub" text-anchor="middle">skills-snapshot \u51bb</text>
    <text x="335" y="446" class="t-sub" text-anchor="middle">subagent-followup</text>
    <text x="335" y="460" class="t-sub" text-anchor="middle">+ run.cron-model-override</text>
    <text x="335" y="474" class="t-sub" text-anchor="middle">+ 13 issue regression</text>

    <rect x="40" y="496" width="390" height="78" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="235" y="514" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">execution vs delivery \u5206\u79bb</text>
    <text x="235" y="532" class="t-sub" text-anchor="middle">lastRunStatus \u00b7 lastDeliveryStatus</text>
    <text x="235" y="546" class="t-sub" text-anchor="middle">consecutiveErrors backoff</text>
    <text x="235" y="560" class="t-sub" text-anchor="middle">scheduleErrorCount \u81ea disable</text>

    <rect x="470" y="328" width="410" height="252" rx="12" fill="#fdf6e3" stroke="#f97316" stroke-width="2.5" />
    <text x="490" y="352" class="t" fill="#f97316" font-weight="700">Hermes \u00b7 croniter + jobs.json</text>
    <text x="490" y="370" class="t-sub">\u6700\u7ecf\u5178\u65b9\u6848 + prompt \u626b\u63cf</text>

    <rect x="490" y="384" width="180" height="100" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="580" y="402" class="t" text-anchor="middle">~/.hermes/cron/</text>
    <text x="580" y="418" class="t-sub" text-anchor="middle">jobs.json (0o600)</text>
    <text x="580" y="432" class="t-sub" text-anchor="middle">output/{job_id}/</text>
    <text x="580" y="446" class="t-sub" text-anchor="middle">{ts}.md</text>
    <text x="580" y="460" class="t-sub" text-anchor="middle">dir 0o700</text>
    <text x="580" y="474" class="t-sub" text-anchor="middle">ONESHOT_GRACE 120s</text>

    <rect x="690" y="384" width="180" height="100" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="780" y="402" class="t" text-anchor="middle">_origin_from_env</text>
    <text x="780" y="418" class="t-sub" text-anchor="middle">SESSION_PLATFORM</text>
    <text x="780" y="432" class="t-sub" text-anchor="middle">SESSION_CHAT_ID</text>
    <text x="780" y="446" class="t-sub" text-anchor="middle">SESSION_THREAD_ID</text>
    <text x="780" y="460" class="t-sub" text-anchor="middle">\u8bb0\u4f4f\u89e6\u53d1\u6e90</text>
    <text x="780" y="474" class="t-sub" text-anchor="middle">\u51b3\u5b9a\u4ea4\u4ed8 chat</text>

    <rect x="490" y="496" width="380" height="78" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="680" y="514" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">_CRON_THREAT_PATTERNS x10</text>
    <text x="680" y="532" class="t-sub" text-anchor="middle">prompt injection / role hijack / curl exfil</text>
    <text x="680" y="546" class="t-sub" text-anchor="middle">/etc/sudoers / rm -rf / / authorized_keys</text>
    <text x="680" y="560" class="t-sub" text-anchor="middle">+ 10 invisible unicode \u67e5\u6740</text>
  </g>
</svg>
"""

SELFIMPROVE_SVG = r"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 600" width="100%" font-family="'Kalam','Comic Neue',sans-serif">
  <defs>
    <filter id="r19">
      <feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="69" />
      <feDisplacementMap in="SourceGraphic" scale="1.3" />
    </filter>
    <style>
      .t { font-size: 14px; fill: #1e293b; }
      .t-sub { font-size: 11px; fill: #475569; }
      .head { font-size: 18px; fill: #1e293b; font-weight: 700; }
    </style>
  </defs>

  <rect width="900" height="600" fill="#fffef7" />

  <text x="450" y="34" class="head" text-anchor="middle">\u81ea\u6211\u6539\u8fdb\uff1aagent \u4ec0\u4e48\u65f6\u5019\u5b66</text>
  <text x="450" y="54" class="t-sub" text-anchor="middle">Phase1+Phase2 \u00b7 skillify+insights+autoMode \u00b7 \u88ab\u52a8\u7d22\u5f15+decay \u00b7 turn \u5185+11 \u5a01\u80c1\u626b\u63cf</text>

  <g filter="url(#r19)">
    <rect x="20" y="68" width="430" height="250" rx="12" fill="#fdf6e3" stroke="#0ea5e9" stroke-width="2.5" />
    <text x="40" y="92" class="t" fill="#0ea5e9" font-weight="700">Codex \u00b7 Phase1 + Phase2</text>
    <text x="40" y="110" class="t-sub">turn \u5916\u72ec\u7acb LLM job\uff0c800 \u884c prompt</text>

    <rect x="40" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="130" y="142" class="t" text-anchor="middle">Phase 1 per-turn</text>
    <text x="130" y="158" class="t-sub" text-anchor="middle">stage1_outputs</text>
    <text x="130" y="172" class="t-sub" text-anchor="middle">thread \u7c92\u5ea6</text>
    <text x="130" y="186" class="t-sub" text-anchor="middle">+ cwd/git_branch</text>
    <text x="130" y="200" class="t-sub" text-anchor="middle">\u5ec9\u4ef7\u62bd\u53d6</text>

    <rect x="240" y="124" width="195" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="337" y="142" class="t" text-anchor="middle">Phase 2 global</text>
    <text x="337" y="158" class="t-sub" text-anchor="middle">global lock</text>
    <text x="337" y="172" class="t-sub" text-anchor="middle">+ input_watermark</text>
    <text x="337" y="186" class="t-sub" text-anchor="middle">+ 6h cooldown</text>
    <text x="337" y="200" class="t-sub" text-anchor="middle">\u91cd\u5199 MEMORY/skills</text>

    <rect x="40" y="216" width="390" height="90" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="235" y="234" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">consolidation prompt \u660e\u786e\u8bf4</text>
    <text x="235" y="252" class="t-sub" text-anchor="middle">"improve future agents' ability to..."</text>
    <text x="235" y="266" class="t-sub" text-anchor="middle">high-signal: user pref / decision trigger</text>
    <text x="235" y="280" class="t-sub" text-anchor="middle">failure shield / repo map / proven repro</text>
    <text x="235" y="294" class="t-sub" text-anchor="middle">+ wording-preservation rule</text>

    <rect x="470" y="68" width="410" height="250" rx="12" fill="#fdf6e3" stroke="#7c3aed" stroke-width="2.5" />
    <text x="490" y="92" class="t" fill="#7c3aed" font-weight="700">Claude Code \u00b7 \u7528\u6237\u9a71\u52a8\u4e09\u5165\u53e3</text>
    <text x="490" y="110" class="t-sub">disableModelInvocation: \u4e0d\u504f\u8bb0</text>

    <rect x="490" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="580" y="142" class="t" text-anchor="middle">skillify</text>
    <text x="580" y="158" class="t-sub" text-anchor="middle">4 \u8f6e AskUserQuestion</text>
    <text x="580" y="172" class="t-sub" text-anchor="middle">R1: name+desc</text>
    <text x="580" y="186" class="t-sub" text-anchor="middle">R2: step+arg</text>
    <text x="580" y="200" class="t-sub" text-anchor="middle">R3: \u62c6\u89e3 R4: trigger</text>

    <rect x="690" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="780" y="142" class="t" text-anchor="middle">/insights</text>
    <text x="780" y="158" class="t-sub" text-anchor="middle">Opus \u8dd1 jsonl</text>
    <text x="780" y="172" class="t-sub" text-anchor="middle">queryWithModel x2</text>
    <text x="780" y="186" class="t-sub" text-anchor="middle">facet + narrative</text>
    <text x="780" y="200" class="t-sub" text-anchor="middle">\u53ea\u5c55\u4e0d\u56de\u5199</text>

    <rect x="490" y="216" width="380" height="90" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="680" y="234" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">autoMode critique</text>
    <text x="680" y="252" class="t-sub" text-anchor="middle">LLM \u5ba1\u7528\u6237 allow / soft_deny / env</text>
    <text x="680" y="266" class="t-sub" text-anchor="middle">clarity / completeness / conflicts</text>
    <text x="680" y="280" class="t-sub" text-anchor="middle">\u9762\u5411\u7528\u6237\u7684\u89c4\u5219\u626b\u63cf</text>
    <text x="680" y="294" class="t-sub" text-anchor="middle">\u4e0d\u4f1a\u6539\u8fdb agent \u672c\u8eab</text>

    <rect x="20" y="328" width="430" height="252" rx="12" fill="#fdf6e3" stroke="#16a34a" stroke-width="2.5" />
    <text x="40" y="352" class="t" fill="#16a34a" font-weight="700">OpenClaw \u00b7 \u88ab\u52a8\u7d22\u5f15</text>
    <text x="40" y="370" class="t-sub">\u7ecf\u9a8c = \u7d22\u5f15\u8bed\u6599\uff0c\u65e0\u663e\u5f0f consolidation</text>

    <rect x="40" y="384" width="180" height="100" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="130" y="402" class="t" text-anchor="middle">session \u843d\u76d8\u81ea\u52a8\u5165</text>
    <text x="130" y="418" class="t-sub" text-anchor="middle">JSONL extract text</text>
    <text x="130" y="432" class="t-sub" text-anchor="middle">+ chunk</text>
    <text x="130" y="446" class="t-sub" text-anchor="middle">FTS5 + sqlite-vec</text>
    <text x="130" y="460" class="t-sub" text-anchor="middle">source: sessions</text>
    <text x="130" y="474" class="t-sub" text-anchor="middle">redactSensitiveText</text>

    <rect x="240" y="384" width="190" height="100" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="335" y="402" class="t" text-anchor="middle">temporal decay</text>
    <text x="335" y="418" class="t-sub" text-anchor="middle">halfLifeDays = 30</text>
    <text x="335" y="432" class="t-sub" text-anchor="middle">lambda = ln2/halfLife</text>
    <text x="335" y="446" class="t-sub" text-anchor="middle">YYYY-MM-DD.md</text>
    <text x="335" y="460" class="t-sub" text-anchor="middle">=> decay</text>
    <text x="335" y="474" class="t-sub" text-anchor="middle">MEMORY.md evergreen</text>

    <rect x="40" y="496" width="390" height="78" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="235" y="514" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">hybrid retrieval \u8865\u4f4d</text>
    <text x="235" y="532" class="t-sub" text-anchor="middle">semantic + lexical + MMR + decay</text>
    <text x="235" y="546" class="t-sub" text-anchor="middle">qmd-scope \u67e5\u8be2\u9a71\u52a8\u8303\u56f4</text>
    <text x="235" y="560" class="t-sub" text-anchor="middle">Mandatory recall: \u5e72\u4e8b\u524d grep</text>

    <rect x="470" y="328" width="410" height="252" rx="12" fill="#fdf6e3" stroke="#f97316" stroke-width="2.5" />
    <text x="490" y="352" class="t" fill="#f97316" font-weight="700">Hermes \u00b7 turn \u5185\u663e\u5f0f\u5199</text>
    <text x="490" y="370" class="t-sub">2 file + 4 action + 11 \u5a01\u80c1\u626b\u63cf</text>

    <rect x="490" y="384" width="180" height="100" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="580" y="402" class="t" text-anchor="middle">MEMORY.md</text>
    <text x="580" y="418" class="t-sub" text-anchor="middle">2200 \u5b57\u7b26</text>
    <text x="580" y="432" class="t-sub" text-anchor="middle">USER.md</text>
    <text x="580" y="446" class="t-sub" text-anchor="middle">1375 \u5b57\u7b26</text>
    <text x="580" y="460" class="t-sub" text-anchor="middle">delimiter: \u00a7</text>
    <text x="580" y="474" class="t-sub" text-anchor="middle">add/replace/remove/read</text>

    <rect x="690" y="384" width="180" height="100" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="780" y="402" class="t" text-anchor="middle">frozen snapshot</text>
    <text x="780" y="418" class="t-sub" text-anchor="middle">load_from_disk \u51bb\u7ed3</text>
    <text x="780" y="432" class="t-sub" text-anchor="middle">mid-session</text>
    <text x="780" y="446" class="t-sub" text-anchor="middle">=> disk only</text>
    <text x="780" y="460" class="t-sub" text-anchor="middle">prefix cache \u5b89\u5168</text>
    <text x="780" y="474" class="t-sub" text-anchor="middle">\u4e0b\u6b21\u4f1a\u8bdd\u91cd\u8f7d</text>

    <rect x="490" y="496" width="380" height="78" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="680" y="514" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">_MEMORY_THREAT_PATTERNS x11</text>
    <text x="680" y="532" class="t-sub" text-anchor="middle">prompt injection / role hijack</text>
    <text x="680" y="546" class="t-sub" text-anchor="middle">exfil_curl / read_secrets / ssh_backdoor</text>
    <text x="680" y="560" class="t-sub" text-anchor="middle">+ 10 invisible unicode</text>
  </g>
</svg>
"""

SECURITY_SVG = r"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 600" width="100%" font-family="'Kalam','Comic Neue',sans-serif">
  <defs>
    <filter id="r20">
      <feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="78" />
      <feDisplacementMap in="SourceGraphic" scale="1.3" />
    </filter>
    <style>
      .t { font-size: 14px; fill: #1e293b; }
      .t-sub { font-size: 11px; fill: #475569; }
      .head { font-size: 18px; fill: #1e293b; font-weight: 700; }
    </style>
  </defs>

  <rect width="900" height="600" fill="#fffef7" />

  <text x="450" y="34" class="head" text-anchor="middle">Security\uff1a\u6ce8\u5165 / \u6295\u6bd2 / \u5bc6\u94a5 / \u4f9b\u5e94\u94fe</text>
  <text x="450" y="54" class="t-sub" text-anchor="middle">sandbox+TrustLevel \u00b7 /security-review+autoMode \u00b7 29 file security/ \u00b7 tirith+cosign+redact</text>

  <g filter="url(#r20)">
    <rect x="20" y="68" width="430" height="250" rx="12" fill="#fdf6e3" stroke="#0ea5e9" stroke-width="2.5" />
    <text x="40" y="92" class="t" fill="#0ea5e9" font-weight="700">Codex \u00b7 sandbox-first + TrustLevel</text>
    <text x="40" y="110" class="t-sub">\u4e09\u5e73\u53f0\u539f\u751f\u6c99\u7bb1 + 4 \u6863\u5ba1\u6279</text>

    <rect x="40" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="130" y="142" class="t" text-anchor="middle">3 \u5e73\u53f0 sandbox</text>
    <text x="130" y="158" class="t-sub" text-anchor="middle">seatbelt (.sbpl)</text>
    <text x="130" y="172" class="t-sub" text-anchor="middle">bubblewrap+seccomp</text>
    <text x="130" y="186" class="t-sub" text-anchor="middle">+ landlock</text>
    <text x="130" y="200" class="t-sub" text-anchor="middle">windows-sandbox-rs</text>

    <rect x="240" y="124" width="195" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="337" y="142" class="t" text-anchor="middle">TrustLevel onboarding</text>
    <text x="337" y="158" class="t-sub" text-anchor="middle">TrustDirectoryWidget</text>
    <text x="337" y="172" class="t-sub" text-anchor="middle">Trust / Quit \u4e8c\u9009\u4e00</text>
    <text x="337" y="186" class="t-sub" text-anchor="middle">git auto-trust root</text>
    <text x="337" y="200" class="t-sub" text-anchor="middle">+ AskForApproval x4</text>

    <rect x="40" y="216" width="390" height="90" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="235" y="234" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">memory consolidation prompt</text>
    <text x="235" y="252" class="t-sub" text-anchor="middle">"treat as data, NOT instructions"</text>
    <text x="235" y="266" class="t-sub" text-anchor="middle">+ [REDACTED_SECRET] \u5f3a\u5236</text>
    <text x="235" y="280" class="t-sub" text-anchor="middle">rollout-trace.jsonl \u53ef\u91cd\u653e</text>
    <text x="235" y="294" class="t-sub" text-anchor="middle">core-skills bundled allowlist</text>

    <rect x="470" y="68" width="410" height="250" rx="12" fill="#fdf6e3" stroke="#7c3aed" stroke-width="2.5" />
    <text x="490" y="92" class="t" fill="#7c3aed" font-weight="700">Claude Code \u00b7 review-as-tool</text>
    <text x="490" y="110" class="t-sub">/security-review + autoMode + securityCheck</text>

    <rect x="490" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="580" y="142" class="t" text-anchor="middle">/security-review</text>
    <text x="580" y="158" class="t-sub" text-anchor="middle">senior security eng</text>
    <text x="580" y="172" class="t-sub" text-anchor="middle">5 \u7c7b\u6f0f\u6d1e</text>
    <text x="580" y="186" class="t-sub" text-anchor="middle">80% confidence</text>
    <text x="580" y="200" class="t-sub" text-anchor="middle">focus ONLY on PR</text>

    <rect x="690" y="124" width="180" height="80" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="780" y="142" class="t" text-anchor="middle">EXCLUSIONS</text>
    <text x="780" y="158" class="t-sub" text-anchor="middle">no DOS</text>
    <text x="780" y="172" class="t-sub" text-anchor="middle">no disk secrets</text>
    <text x="780" y="186" class="t-sub" text-anchor="middle">no rate limit</text>
    <text x="780" y="200" class="t-sub" text-anchor="middle">\u9632 review-bloat</text>

    <rect x="490" y="216" width="380" height="90" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="680" y="234" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">autoMode classifier + securityCheck</text>
    <text x="680" y="252" class="t-sub" text-anchor="middle">allow / soft_deny / environment</text>
    <text x="680" y="266" class="t-sub" text-anchor="middle">LLM critique \u7528\u6237\u89c4\u5219</text>
    <text x="680" y="280" class="t-sub" text-anchor="middle">remoteManagedSettings \u7b7e\u540d\u6821\u9a8c</text>
    <text x="680" y="294" class="t-sub" text-anchor="middle">disableModelInvocation</text>

    <rect x="20" y="328" width="430" height="252" rx="12" fill="#fdf6e3" stroke="#16a34a" stroke-width="2.5" />
    <text x="40" y="352" class="t" fill="#16a34a" font-weight="700">OpenClaw \u00b7 29 file security/</text>
    <text x="40" y="370" class="t-sub">\u6559\u79d1\u4e66\u7ea7\u591a\u5c42\u5ba1\u8ba1</text>

    <rect x="40" y="384" width="180" height="100" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="130" y="402" class="t" text-anchor="middle">audit.ts core</text>
    <text x="130" y="418" class="t-sub" text-anchor="middle">30+ check</text>
    <text x="130" y="432" class="t-sub" text-anchor="middle">SecurityAuditReport</text>
    <text x="130" y="446" class="t-sub" text-anchor="middle">critical/warn/info</text>
    <text x="130" y="460" class="t-sub" text-anchor="middle">+ deep gateway + fs</text>
    <text x="130" y="474" class="t-sub" text-anchor="middle">remediation \u63d0\u793a</text>

    <rect x="240" y="384" width="190" height="100" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="335" y="402" class="t" text-anchor="middle">external-content</text>
    <text x="335" y="418" class="t-sub" text-anchor="middle">SUSPICIOUS_PATTERNS x12</text>
    <text x="335" y="432" class="t-sub" text-anchor="middle">+ 8 byte random ID</text>
    <text x="335" y="446" class="t-sub" text-anchor="middle">\u9632\u8fb9\u754c\u4f2a\u9020</text>
    <text x="335" y="460" class="t-sub" text-anchor="middle">+ SECURITY NOTICE</text>
    <text x="335" y="474" class="t-sub" text-anchor="middle">XML \u5305\u88f9</text>

    <rect x="40" y="496" width="390" height="78" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="235" y="514" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">+ skill-scanner / dangerous-tools</text>
    <text x="235" y="532" class="t-sub" text-anchor="middle">redact-snapshot / redact-bounded</text>
    <text x="235" y="546" class="t-sub" text-anchor="middle">safe-regex (\u9632 ReDoS)</text>
    <text x="235" y="560" class="t-sub" text-anchor="middle">windows-acl / temp-path-guard</text>

    <rect x="470" y="328" width="410" height="252" rx="12" fill="#fdf6e3" stroke="#f97316" stroke-width="2.5" />
    <text x="490" y="352" class="t" fill="#f97316" font-weight="700">Hermes \u00b7 tirith \u5b50\u8fdb\u7a0b + redact</text>
    <text x="490" y="370" class="t-sub">verdict = exit code\uff0c\u4e0d\u4f9d\u8d56 LLM</text>

    <rect x="490" y="384" width="180" height="100" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="580" y="402" class="t" text-anchor="middle">tirith subprocess</text>
    <text x="580" y="418" class="t-sub" text-anchor="middle">exit 0/1/2</text>
    <text x="580" y="432" class="t-sub" text-anchor="middle">= verdict truth</text>
    <text x="580" y="446" class="t-sub" text-anchor="middle">JSON stdout enrich</text>
    <text x="580" y="460" class="t-sub" text-anchor="middle">fail_open default</text>
    <text x="580" y="474" class="t-sub" text-anchor="middle">+ \u540e\u53f0\u81ea\u5b89\u88c5</text>

    <rect x="690" y="384" width="180" height="100" rx="6" fill="#fdf6e3" stroke="#1e293b" stroke-width="1.5" />
    <text x="780" y="402" class="t" text-anchor="middle">cosign provenance</text>
    <text x="780" y="418" class="t-sub" text-anchor="middle">OIDC issuer pin</text>
    <text x="780" y="432" class="t-sub" text-anchor="middle">workflow regexp pin</text>
    <text x="780" y="446" class="t-sub" text-anchor="middle">+ SHA-256 \u5fc5\u9a8c</text>
    <text x="780" y="460" class="t-sub" text-anchor="middle">cosign \u4e0d\u88c5\u4e5f\u8dd1</text>
    <text x="780" y="474" class="t-sub" text-anchor="middle">HTTPS + checksum</text>

    <rect x="490" y="496" width="380" height="78" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="680" y="514" class="t" text-anchor="middle" fill="#dc2626" font-weight="700">redact.py: 30+ vendor token \u524d\u7f00</text>
    <text x="680" y="532" class="t-sub" text-anchor="middle">sk- / ghp_ / AKIA / xox / AIza / gAAAA</text>
    <text x="680" y="546" class="t-sub" text-anchor="middle">_REDACT_ENABLED import \u65f6 snapshot</text>
    <text x="680" y="560" class="t-sub" text-anchor="middle">+ _MEMORY/_CRON_THREAT_PATTERNS</text>
  </g>
</svg>
"""

import re as _re

_ESCAPE_RE = _re.compile(r"\\u([0-9a-fA-F]{4})")


def _decode_unicode_escapes(s: str) -> str:
    """Replace literal \\uXXXX sequences with the corresponding character.

    Raw-string SVG bodies (r\"\"\"...\"\"\") keep \\uXXXX as 6 chars; SVG renderers
    do not process JS-style escape sequences, so we expand them here.
    """
    return _ESCAPE_RE.sub(lambda m: chr(int(m.group(1), 16)), s)


def write(slug: str, svg: str) -> None:
    out = PUBLIC / f"{slug}-base.svg"
    svg = _decode_unicode_escapes(svg)
    out.write_text(svg, encoding="utf-8")
    print(f"wrote {out} ({len(svg)} chars)")

if __name__ == "__main__":
    PUBLIC.mkdir(parents=True, exist_ok=True)
    write("01-overview", OVERVIEW_SVG)
    write("03-context", CONTEXT_SVG)
    write("04-tool-system", TOOL_SVG)
    write("05-verifier", VERIFIER_SVG)
    write("06-file-edit-patch", PATCH_SVG)
    write("07-shell-execution", SHELL_SVG)
    write("08-git-workflow", GIT_SVG)
    write("09-code-review", REVIEW_SVG)
    write("10-subagents", SUBAGENT_SVG)
    write("11-session-lifecycle", SESSION_SVG)
    write("12-permissions-approvals", PERMISSION_SVG)
    write("13-sandbox-execution", SANDBOX_SVG)
    write("14-multi-channel-entry", CHANNEL_SVG)
    write("15-observability-cost", OBSERVE_SVG)
    write("16-memory", MEMORY_SVG)
    write("17-skills", SKILLS_SVG)
    write("18-cron-background", CRON_SVG)
    write("19-self-improvement", SELFIMPROVE_SVG)
    write("20-security", SECURITY_SVG)
