#!/usr/bin/env python3
"""
Generate the 4-system swim-lane SVG for 02 · Agent Loop.
Writes via explicit UTF-8 to avoid Windows codepage encoding issues.
"""
from pathlib import Path

SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 560" role="img" aria-label="Agent Loop swim lanes across four systems">
  <defs>
    <filter id="lanes-wobble">
      <feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="7" />
      <feDisplacementMap in="SourceGraphic" scale="2" />
    </filter>
    <marker id="lanes-arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#1e293b" />
    </marker>
    <style>
      .h { font: 600 14px sans-serif; fill: #1e293b; }
      .t { font: 11px sans-serif; fill: #1e293b; }
      .t-sub { font: 10.5px sans-serif; fill: #475569; }
      .sys { font: 700 13px sans-serif; fill: #fdf6e3; }
      .sys-sub { font: 10.5px sans-serif; fill: #fdf6e3; }
      .stage { font: 600 12px sans-serif; fill: #1e293b; }
    </style>
  </defs>

  <text x="20" y="24" class="h">Agent Loop \u00b7 \u56db\u4e2a\u7cfb\u7edf\u7684\u6cf3\u9053\u5bf9\u6bd4</text>
  <text x="20" y="42" class="t-sub">\u540c\u4e00\u4e2a\u5faa\u73af\uff0c\u56db\u79cd\u5de5\u7a0b\u53d6\u820d\uff1a\u505c\u6b62\u6761\u4ef6\u3001verifier\u3001\u53ef\u91cd\u5165\u4e0e\u5e76\u53d1\u6a21\u578b\u5404\u4e0d\u76f8\u540c\u3002</text>

  <g transform="translate(0, 70)">
    <rect x="178" y="0" width="180" height="30" rx="6" fill="#fdf6e3" stroke="#16a34a" stroke-width="2" />
    <text x="268" y="20" class="stage" text-anchor="middle" fill="#16a34a">Observe / Intake</text>
    <rect x="368" y="0" width="180" height="30" rx="6" fill="#fdf6e3" stroke="#f97316" stroke-width="2" />
    <text x="458" y="20" class="stage" text-anchor="middle" fill="#f97316">Plan / Reason</text>
    <rect x="558" y="0" width="180" height="30" rx="6" fill="#fdf6e3" stroke="#7c3aed" stroke-width="2" />
    <text x="648" y="20" class="stage" text-anchor="middle" fill="#7c3aed">Act / Tool Call</text>
    <rect x="748" y="0" width="210" height="30" rx="6" fill="#fdf6e3" stroke="#dc2626" stroke-width="2" />
    <text x="853" y="20" class="stage" text-anchor="middle" fill="#dc2626">Verify / Stop?</text>
  </g>

  <g filter="url(#lanes-wobble)" transform="translate(0, 115)">
    <!-- Codex (blue) -->
    <g>
      <rect x="20" y="10" width="140" height="80" rx="10" fill="#2563eb" stroke="#1e293b" stroke-width="2" />
      <text x="90" y="38" class="sys" text-anchor="middle">Codex</text>
      <text x="90" y="58" class="sys-sub" text-anchor="middle">submit(Op)</text>
      <text x="90" y="74" class="sys-sub" text-anchor="middle">next_event()</text>
      <rect x="178" y="10" width="180" height="80" rx="8" fill="#fdf6e3" stroke="#1e293b" stroke-width="2" />
      <text x="268" y="34" class="t" text-anchor="middle">new_default_turn()</text>
      <text x="268" y="52" class="t-sub" text-anchor="middle">TurnContext / Goal</text>
      <text x="268" y="74" class="t-sub" text-anchor="middle">rollout \u6301\u4e45\u5316</text>
      <rect x="368" y="10" width="180" height="80" rx="8" fill="#fdf6e3" stroke="#1e293b" stroke-width="2" />
      <text x="458" y="34" class="t" text-anchor="middle">Responses API</text>
      <text x="458" y="52" class="t-sub" text-anchor="middle">function_tool \u8c03\u7528</text>
      <text x="458" y="74" class="t-sub" text-anchor="middle">codex_delegate (subagent)</text>
      <rect x="558" y="10" width="180" height="80" rx="8" fill="#fdf6e3" stroke="#1e293b" stroke-width="2" />
      <text x="648" y="34" class="t" text-anchor="middle">exec / apply_patch</text>
      <text x="648" y="52" class="t-sub" text-anchor="middle">execpolicy \u5ba1\u6279</text>
      <text x="648" y="74" class="t-sub" text-anchor="middle">sandbox \u9694\u79bb</text>
      <rect x="748" y="10" width="210" height="80" rx="8" fill="#fdf6e3" stroke="#1e293b" stroke-width="2" />
      <text x="853" y="34" class="t" text-anchor="middle">run tests / lint</text>
      <text x="853" y="52" class="t-sub" text-anchor="middle">goals.rs \u6536\u655b\u5224\u65ad</text>
      <text x="853" y="74" class="t-sub" text-anchor="middle">flush_rollout \u2192 \u53ef\u6062\u590d</text>
    </g>

    <!-- Claude Code (purple) -->
    <g transform="translate(0, 100)">
      <rect x="20" y="10" width="140" height="80" rx="10" fill="#7c3aed" stroke="#1e293b" stroke-width="2" />
      <text x="90" y="34" class="sys" text-anchor="middle">Claude Code</text>
      <text x="90" y="54" class="sys-sub" text-anchor="middle">queryLoop()</text>
      <text x="90" y="70" class="sys-sub" text-anchor="middle">query.ts:241</text>
      <rect x="178" y="10" width="180" height="80" rx="8" fill="#fdf6e3" stroke="#1e293b" stroke-width="2" />
      <text x="268" y="34" class="t" text-anchor="middle">4 \u9053\u4e0a\u4e0b\u6587\u538b\u7f29</text>
      <text x="268" y="52" class="t-sub" text-anchor="middle">snip / micro / collapse / auto</text>
      <text x="268" y="74" class="t-sub" text-anchor="middle">using memory prefetch</text>
      <rect x="368" y="10" width="180" height="80" rx="8" fill="#fdf6e3" stroke="#1e293b" stroke-width="2" />
      <text x="458" y="34" class="t" text-anchor="middle">Anthropic API \u6d41\u5f0f</text>
      <text x="458" y="52" class="t-sub" text-anchor="middle">transition.reason \u6807\u7b7e</text>
      <text x="458" y="74" class="t-sub" text-anchor="middle">skill prefetch \u5e76\u884c</text>
      <rect x="558" y="10" width="180" height="80" rx="8" fill="#fdf6e3" stroke="#1e293b" stroke-width="2" />
      <text x="648" y="34" class="t" text-anchor="middle">tool_use block dispatch</text>
      <text x="648" y="52" class="t-sub" text-anchor="middle">TaskType 7 \u79cd</text>
      <text x="648" y="74" class="t-sub" text-anchor="middle">queryTracking.depth</text>
      <rect x="748" y="10" width="210" height="80" rx="8" fill="#fdf6e3" stroke="#1e293b" stroke-width="2" />
      <text x="853" y="34" class="t" text-anchor="middle">\u65e0 tool_use \u5219\u9000\u51fa</text>
      <text x="853" y="52" class="t-sub" text-anchor="middle">stopHooks \u62e6\u622a / TOKEN_BUDGET 90%</text>
      <text x="853" y="74" class="t-sub" text-anchor="middle">maxTurns \u786c\u4e0a\u9650</text>
    </g>

    <!-- OpenClaw (green) -->
    <g transform="translate(0, 200)">
      <rect x="20" y="10" width="140" height="80" rx="10" fill="#16a34a" stroke="#1e293b" stroke-width="2" />
      <text x="90" y="38" class="sys" text-anchor="middle">OpenClaw</text>
      <text x="90" y="58" class="sys-sub" text-anchor="middle">agent RPC</text>
      <text x="90" y="74" class="sys-sub" text-anchor="middle">agent.wait</text>
      <rect x="178" y="10" width="180" height="80" rx="8" fill="#fdf6e3" stroke="#1e293b" stroke-width="2" />
      <text x="268" y="34" class="t" text-anchor="middle">session \u9501 + \u5de5\u4f5c\u533a</text>
      <text x="268" y="52" class="t-sub" text-anchor="middle">skills \u6ce8\u5165 prompt</text>
      <text x="268" y="74" class="t-sub" text-anchor="middle">bootstrap files</text>
      <rect x="368" y="10" width="180" height="80" rx="8" fill="#fdf6e3" stroke="#1e293b" stroke-width="2" />
      <text x="458" y="34" class="t" text-anchor="middle">runEmbeddedPiAgent</text>
      <text x="458" y="52" class="t-sub" text-anchor="middle">3 stream: assistant/tool/lifecycle</text>
      <text x="458" y="74" class="t-sub" text-anchor="middle">session lane \u4e32\u884c\u5316</text>
      <rect x="558" y="10" width="180" height="80" rx="8" fill="#fdf6e3" stroke="#1e293b" stroke-width="2" />
      <text x="648" y="34" class="t" text-anchor="middle">tool plugins</text>
      <text x="648" y="52" class="t-sub" text-anchor="middle">before/after_tool_call hook</text>
      <text x="648" y="74" class="t-sub" text-anchor="middle">sandbox \u591a\u901a\u9053</text>
      <rect x="748" y="10" width="210" height="80" rx="8" fill="#fdf6e3" stroke="#1e293b" stroke-width="2" />
      <text x="853" y="34" class="t" text-anchor="middle">lifecycle:end / error</text>
      <text x="853" y="52" class="t-sub" text-anchor="middle">auto-compaction + retry</text>
      <text x="853" y="74" class="t-sub" text-anchor="middle">timeout abort</text>
    </g>

    <!-- Hermes (orange) -->
    <g transform="translate(0, 300)">
      <rect x="20" y="10" width="140" height="80" rx="10" fill="#f97316" stroke="#1e293b" stroke-width="2" />
      <text x="90" y="34" class="sys" text-anchor="middle">Hermes</text>
      <text x="90" y="54" class="sys-sub" text-anchor="middle">run_conversation</text>
      <text x="90" y="70" class="sys-sub" text-anchor="middle">while iter &lt; 90</text>
      <rect x="178" y="10" width="180" height="80" rx="8" fill="#fdf6e3" stroke="#1e293b" stroke-width="2" />
      <text x="268" y="34" class="t" text-anchor="middle">memory.prefetch_all</text>
      <text x="268" y="52" class="t-sub" text-anchor="middle">\u8de8\u4f1a\u8bdd\u7528\u6237\u6a21\u578b + \u641c\u7d22</text>
      <text x="268" y="74" class="t-sub" text-anchor="middle">SubdirectoryHintTracker</text>
      <rect x="368" y="10" width="180" height="80" rx="8" fill="#fdf6e3" stroke="#1e293b" stroke-width="2" />
      <text x="458" y="34" class="t" text-anchor="middle">OpenAI \u534f\u8bae</text>
      <text x="458" y="52" class="t-sub" text-anchor="middle">subagent (max_iter=50)</text>
      <text x="458" y="74" class="t-sub" text-anchor="middle">trajectory \u4e8b\u4ef6\u6d41</text>
      <rect x="558" y="10" width="180" height="80" rx="8" fill="#fdf6e3" stroke="#1e293b" stroke-width="2" />
      <text x="648" y="34" class="t" text-anchor="middle">tool dispatch</text>
      <text x="648" y="52" class="t-sub" text-anchor="middle">checkpoint_mgr.new_turn</text>
      <text x="648" y="74" class="t-sub" text-anchor="middle">interrupt \u53ef\u4e2d\u65ad</text>
      <rect x="748" y="10" width="210" height="80" rx="8" fill="#fdf6e3" stroke="#1e293b" stroke-width="2" />
      <text x="853" y="34" class="t" text-anchor="middle">IterationBudget + grace</text>
      <text x="853" y="52" class="t-sub" text-anchor="middle">skill insights \u81ea\u8bc4</text>
      <text x="853" y="74" class="t-sub" text-anchor="middle">memory commit \u2192 \u6301\u4e45\u5316</text>
    </g>

    <!-- loop-back arrows -->
    <path d="M 958 50 C 1010 50, 1010 -10, 178 -10 C 90 -10, 60 30, 90 50" fill="none" stroke="#1e293b" stroke-width="1.5" stroke-dasharray="5 3" marker-end="url(#lanes-arrow)" opacity="0.55" />
    <path d="M 958 150 C 1010 150, 1010 90, 178 90 C 90 90, 60 130, 90 150" fill="none" stroke="#1e293b" stroke-width="1.5" stroke-dasharray="5 3" marker-end="url(#lanes-arrow)" opacity="0.55" />
    <path d="M 958 250 C 1010 250, 1010 190, 178 190 C 90 190, 60 230, 90 250" fill="none" stroke="#1e293b" stroke-width="1.5" stroke-dasharray="5 3" marker-end="url(#lanes-arrow)" opacity="0.55" />
    <path d="M 958 350 C 1010 350, 1010 290, 178 290 C 90 290, 60 330, 90 350" fill="none" stroke="#1e293b" stroke-width="1.5" stroke-dasharray="5 3" marker-end="url(#lanes-arrow)" opacity="0.55" />
  </g>

  <text x="20" y="545" class="t-sub">
    \u2022 \u5171\u540c\u70b9\uff1a\u6bcf\u4e00\u884c\u90fd\u8d70 Observe \u2192 Plan \u2192 Act \u2192 Verify  \u00b7  \u2022 \u5dee\u5f02\u70b9\uff1a\u6bcf\u4e00\u683c\u7684\u5de5\u7a0b\u53d6\u820d\u4e0d\u540c  \u00b7  \u2022 \u70b9\u8bc4\u89c1 \u00a76
  </text>
</svg>
"""

out = Path("public/diagrams/02-agent-loop-lanes.svg")
out.write_text(SVG, encoding="utf-8")
print(f"wrote {out} ({len(SVG)} chars)")
