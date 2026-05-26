#!/usr/bin/env python3
"""Translate Chinese SVG diagrams to English.

Reads each .svg from public/diagrams/ and writes a translated copy to
public/diagrams/en/. Uses a translation dictionary that maps the most common
Chinese phrases to English, and falls back to keeping any string that has no
match (so the script can be re-run after dictionary updates without losing
manual fixes).

Run from docs-site/ directory:
  python scripts/translate-svgs.py

Optional args:
  --only <ch>     only translate files whose names start with <ch>, e.g. 02
  --report-only   only report untranslated phrases, don't write files
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SRC_DIR = Path("public/diagrams")
DST_DIR = Path("public/diagrams/en")
DST_DIR.mkdir(parents=True, exist_ok=True)

# Translation dictionary. Phrases are matched as plain substring replacements;
# order matters — longer/more specific phrases must come first.
TRANSLATIONS: dict[str, str] = {
    # ----- aria-label & headers -----
    "四个 Agent 系统在可控性 ↔ 自治度 轴上的位置": "Four agent systems on the controllability vs. autonomy axis",
    "四家 Agent 在短期可控性 × 长期自治度 两条轴上的分布与场景映射": "Four agents plotted across short-term controllability and long-term autonomy",
    "短期可控性 ↔ 长期自治度": "Short-term controllability vs. long-term autonomy",
    "四家位置：短期可控性 ↔ 长期自治度": "Four agents: short-term control vs. long-term autonomy",
    "同一份 Agent 工程，4 个分布在对角线上的取舍点：不是优劣，是场景适配": "One agent stack, four diagonal trade-off points -- not a ranking, scenario fits",
    "同一份 Agent 工程，给你 4 个分布在对角线上的取舍点，不是优劣，是场景适配": "One agent stack, four diagonal trade-off points -- not a ranking, scenario fits",
    "四系统这一维上的分布：最可控的 Codex 在左，最自治的 Hermes 在右。": "Four systems on a single axis: most controlled Codex on the left, most autonomous Hermes on the right.",

    # ----- common quadrant labels -----
    "短期严控 · 不自跑": "tight control - no auto-run",
    "短期严控 · 长跑也行": "tight control - long-running OK",
    "每步审批 · 不自跑": "approve every step - no auto-run",
    "放手让它跑": "let it run on its own",

    # ----- axis labels -----
    "短期可控性（每步审批的难度）→": "short-term controllability (how easy is per-step approval) ->",
    "↑ 长期自治度（自跑 + 自学）": "^ long-term autonomy (self-running + self-learning)",
    "每步可审批": "approve every step",
    "跨会话自记忆 + 自评": "cross-session memory + self-eval",
    "短期可控性": "short-term control",
    "长期自治度": "long-term autonomy",

    # ----- system name pins -----
    "Codex": "Codex",
    "Claude Code": "Claude Code",
    "OpenClaw": "OpenClaw",
    "Hermes": "Hermes",

    # ----- common annotations on system pins -----
    "execpolicy 每步审 + rollout 可恢复": "execpolicy per-step + rollout recovery",
    "execpolicy + apply_patch": "execpolicy + apply_patch",
    "goals.rs 收敛检测": "goals.rs convergence check",
    "5 优先级 + 7 transition": "5 priorities + 7 transition",
    "7 种 transition.reason": "7 transition.reason values",
    "TOKEN_BUDGET 软退": "TOKEN_BUDGET soft exit",
    "plugin 主导 + lane 并发": "plugin-driven + lane concurrency",
    "session lane + plugin": "session lane + plugin",
    "tool-loop-detection": "tool-loop-detection",
    "memory + self-eval": "memory + self-eval",
    "IterationBudget 90/50": "IterationBudget 90/50",
    "memory.prefetch + grace": "memory.prefetch + grace",

    # ----- scenario captions -----
    "「改一个 repo · 每步 review」": "edit one repo - review every step",
    "「IDE coding · 渐进自动化」": "IDE coding - gradual automation",
    "「Slack bot · 多用户并发」": "Slack bot - multi-user concurrent",
    "「私人助理 · 长跑跨会话」": "personal assistant - cross-session long-running",
    "没有「最好」，只有「适配场景」：改 repo 选左下、IDE coding 选中间、做 server 选右上、长跑助理选最右上": "No \"best\" -- only scenario fit: edit a repo? bottom-left. IDE coding? middle. Build a server? upper-middle. Long-running assistant? upper-right.",
    "没有「最好」，只有「适配场景」：改 repo 选左下、IDE coding 选中间、做 server 选右中、长跑助理选最右上": "No \"best\" -- only scenario fit: edit a repo? bottom-left. IDE coding? middle. Build a server? upper-middle. Long-running assistant? upper-right.",

    # ----- chapter 02 (agent loop) -----
    "四家 Agent 都跑相同的最小循环：感知 → 计划 → 执行 → 验证 → 回到感知": "All four agents run the same minimal cycle: Observe -> Plan -> Act -> Verify -> back to Observe",
    "感知": "Observe",
    "计划": "Plan",
    "执行": "Act",
    "验证": "Verify",
    "回到感知": "back to Observe",
    "终止条件": "termination conditions",
    "压缩点": "compression point",
    "停止条件": "stop conditions",
    "停止机制": "stop mechanism",
    "上下文压缩": "context compression",
    "上下文超限": "context overflow",
    "工具调用": "tool call",
    "工具失败": "tool failure",
    "重试": "retry",
    "等待": "wait",
    "崩溃后恢复": "post-crash recovery",
    "断点续传": "resume from breakpoint",
    "回放": "replay",
    "事件流": "event stream",
    "事件机": "event machine",
    "状态机": "state machine",
    "硬约束": "hard constraint",
    "软约束": "soft constraint",
    "校验": "verifier",
    "硬校验": "hard verifier",
    "软校验": "soft verifier",
    "放任型校验": "lazy verifier",
    "硬验证": "hard verification",
    "软验证": "soft verification",
    "失败路径": "failure paths",
    "成功路径": "success path",
    "压缩策略": "compression strategy",
    "断点": "checkpoint",
    "迭代上限": "iteration limit",
    "迭代预算": "iteration budget",
    "运行预算": "run budget",
    "兜底": "fallback",
    "最后兜底": "final fallback",
    "兜底机制": "fallback mechanism",
    "压缩流水线": "compression pipeline",
    "并行调度": "parallel dispatch",
    "并行执行": "parallel execution",
    "同轮并行": "same-turn parallel",

    # ----- chapter 03 (context) -----
    "上下文加载": "context loading",
    "上下文系统": "context system",
    "系统提示": "system prompt",
    "用户消息": "user message",
    "工具描述": "tool descriptions",
    "项目规则": "project rules",
    "可缓存": "cacheable",
    "不可缓存": "uncacheable",
    "缓存边界": "cache boundary",
    "缓存分界": "cache boundary",
    "静态部分": "static part",
    "动态部分": "dynamic part",
    "每轮重算": "recompute each turn",
    "片段注册表": "fragment registry",
    "层级装配": "layered assembly",
    "提示拼接": "prompt assembly",

    # ----- chapter 04 (tools) -----
    "工具系统": "tool system",
    "工具定义": "tool definition",
    "工具注册": "tool registration",
    "工具路由": "tool routing",
    "工具调度": "tool dispatch",
    "工具流水线": "tool pipeline",
    "权限层": "permission layer",
    "权限拦截": "permission interception",
    "审批": "approval",
    "审批门": "approval gate",
    "拒绝": "deny",
    "允许": "allow",
    "询问": "ask",
    "沙箱": "sandbox",
    "沙箱模式": "sandbox mode",
    "审批模式": "approval mode",

    # ----- chapter 05 (verifier) -----
    "三层校验器": "three-tier verifier",
    "退出码": "exit code",
    "外部事实": "external fact",
    "测试通过": "tests pass",
    "lint 通过": "lint passes",
    "补丁合法": "patch is valid",
    "命令成功": "command succeeded",
    "预算耗尽": "budget exhausted",
    "重复工具调用": "repeated tool calls",
    "收敛慢": "slow convergence",
    "模型说完成": "model says done",
    "信号回退": "signal fallback",
    "ping_pong": "ping_pong",
    "circuit_breaker": "circuit breaker",
    "loop detector": "loop detector",
    "失败诊断": "failure diagnostics",
    "失败路线": "failure paths",
    "失败兜底": "fallback on failure",

    # ----- chapter 06 (file edit) -----
    "文件编辑": "file editing",
    "补丁": "patch",
    "补丁应用": "patch apply",
    "原子性": "atomicity",
    "原子提交": "atomic commit",
    "回滚": "rollback",
    "一键回滚": "one-button rollback",
    "原始文件": "original file",
    "新文件": "new file",
    "写入前检查": "pre-write check",
    "文件被改动": "file was modified",
    "时间戳检查": "timestamp check",
    "并发写入": "concurrent write",
    "字符串替换": "string replace",

    # ----- chapter 07 (shell) -----
    "命令解析": "command parsing",
    "命令拦截": "command interception",
    "AST 解析": "AST parsing",
    "tree-sitter 解析": "tree-sitter parsing",
    "敏感命令": "sensitive command",
    "危险命令": "dangerous command",
    "23 个检查器": "23 checkers",
    "shell 命令": "shell command",
    "命令白名单": "command allowlist",
    "命令黑名单": "command denylist",
    "二进制白名单": "binary allowlist",
    "参数白名单": "argument allowlist",
    "环境隔离": "environment isolation",

    # ----- chapter 08 (git) -----
    "工作区": "workspace",
    "工作目录": "working directory",
    "干净状态": "clean state",
    "干净快照": "clean snapshot",
    "基线": "baseline",
    "基线仓库": "baseline repository",
    "应用补丁": "apply patch",
    "暂存": "stage",
    "提交": "commit",
    "分支": "branch",
    "拉取请求": "pull request",
    "代码审查": "code review",

    # ----- chapter 09 (review) -----
    "审查目标": "review target",
    "审查代理": "reviewer agent",
    "守护代理": "guardian agent",
    "本地审查": "local review",
    "远程审查": "remote review",
    "结构化输出": "structured output",

    # ----- chapter 10 (subagent) -----
    "子代理": "subagent",
    "子代理生成": "subagent spawn",
    "递归": "recursion",
    "递归生成": "recursive spawn",
    "权限继承": "permission inheritance",
    "权限提升": "privilege escalation",
    "深度限制": "depth limit",
    "硬阻止": "hard block",
    "工具白名单": "tool whitelist",
    "异步执行": "async execution",

    # ----- chapter 11 (session) -----
    "会话": "session",
    "会话生命周期": "session lifecycle",
    "会话状态": "session state",
    "会话恢复": "session resume",
    "会话重置": "session reset",
    "持久化": "persist",
    "消息历史": "message history",
    "文件变更": "file changes",
    "成本追踪": "cost tracker",
    "代办列表": "todo list",
    "todo 列表": "todo list",
    "线程": "thread",
    "线程索引": "thread index",

    # ----- chapter 12 (permissions) -----
    "权限": "permissions",
    "审批弹窗": "approval dialog",
    "一次性通过": "one-shot pass",
    "整个会话": "entire session",
    "永久通过": "permanent pass",
    "升级权限": "escalate permission",
    "规则修订": "rule amendment",
    "矩阵": "matrix",
    "三维矩阵": "3D matrix",

    # ----- chapter 13 (sandbox) -----
    "文件系统隔离": "filesystem isolation",
    "网络隔离": "network isolation",
    "系统调用隔离": "syscall isolation",
    "权限继承隔离": "privilege inheritance isolation",
    "防越权": "privilege escalation prevention",
    "本地无隔离": "local no isolation",
    "本地容器": "local container",
    "云沙箱": "cloud sandbox",
    "远程机器": "remote machine",
    "Docker 容器": "Docker container",

    # ----- chapter 14 (multi-channel) -----
    "多通道入口": "multi-channel entry",
    "入口拓扑": "entry topology",
    "Telegram": "Telegram",
    "Slack": "Slack",
    "Discord": "Discord",
    "Web": "Web",
    "WhatsApp": "WhatsApp",
    "CLI": "CLI",
    "IDE": "IDE",

    # ----- chapter 15 (observability) -----
    "可观测性": "observability",
    "成本统计": "cost tracking",
    "日志": "logs",
    "事件总线": "event bus",
    "三模块拆分": "three-module split",
    "信心等级": "confidence level",
    "六级置信度": "six-level confidence",
    "OpenTelemetry": "OpenTelemetry",
    "Datadog": "Datadog",
    "Honeycomb": "Honeycomb",

    # ----- chapter 16 (memory) -----
    "记忆": "memory",
    "短期记忆": "short-term memory",
    "长期记忆": "long-term memory",
    "项目级记忆": "project-level memory",
    "用户级记忆": "user-level memory",
    "记忆栈": "memory stack",
    "记忆冷冻快照": "frozen memory snapshot",
    "向量检索": "vector retrieval",
    "全文检索": "full-text retrieval",
    "时间衰减": "temporal decay",
    "多样性约束": "diversity constraint",

    # ----- chapter 17 (skills) -----
    "技能": "skill",
    "技能调用": "skill invocation",
    "技能注册": "skill registry",
    "技能供应链": "skill supply chain",
    "渐进披露": "progressive disclosure",
    "信任级别": "trust level",
    "签名验证": "signature verification",
    "供应链": "supply chain",

    # ----- chapter 18 (cron) -----
    "定时任务": "cron task",
    "后台任务": "background task",
    "周期任务": "periodic task",
    "一次性任务": "one-shot task",
    "调度器": "scheduler",
    "调度器锁": "scheduler lock",
    "宽限时间": "grace window",

    # ----- chapter 19 (self-improvement) -----
    "自我提升": "self-improvement",
    "自我评估": "self-evaluation",
    "经验沉淀": "experience capture",
    "经验提炼": "experience distillation",
    "改进流水线": "improvement pipeline",
    "两阶段流水线": "two-phase pipeline",

    # ----- chapter 20 (security) -----
    "安全": "security",
    "提示注入": "prompt injection",
    "工具中毒": "tool poisoning",
    "凭据泄露": "credential leak",
    "供应链攻击": "supply chain attack",
    "外部内容包裹": "external content wrap",
    "防御层": "defense layer",
    "防御纵深": "defense in depth",
    "信任边界": "trust boundary",
    "安全栈": "security stack",

    # ----- generic words and connectors -----
    "四家": "four systems",
    "四种": "four kinds",
    "四个": "four",
    "三家": "three systems",
    "三种": "three kinds",
    "三个": "three",
    "两家": "two systems",
    "两种": "two kinds",
    "两个": "two",
    "一家": "one system",
    "一种": "one kind",
    "一个": "one",
    "系统": "system",
    "实现": "implementation",
    "对比": "comparison",
    "差异": "difference",
    "取舍": "trade-off",
    "权衡": "trade-off",
    "维度": "dimension",
    "层级": "layer",
    "结构": "structure",
    "流程": "flow",
    "管道": "pipeline",
    "流水线": "pipeline",
    "拓扑": "topology",
    "失败": "failure",
    "成功": "success",
    "继续": "continue",
    "退出": "exit",
    "重启": "restart",
    "崩溃": "crash",
    "超时": "timeout",
    "完成": "done",
    "未完成": "not done",
    "用户": "user",
    "模型": "model",
    "调用": "call",
    "调度": "dispatch",
    "请求": "request",
    "返回": "return",
    "结果": "result",
    "错误": "error",
    "日志": "log",
    "事件": "event",
    "消息": "message",
    "工具": "tool",
    "工具集": "toolset",
    "命令": "command",
    "代码": "code",
    "测试": "tests",
    "代理": "agent",
    "主代理": "main agent",
    "子代理": "subagent",
    "协调者": "coordinator",
    "服务": "service",
    "插件": "plugin",
    "插件钩子": "plugin hook",
    "钩子": "hook",
    "中间件": "middleware",
    "中间件链": "middleware chain",

    # ----- punctuation -----
    "「": "&quot;",
    "」": "&quot;",
    "（": " (",
    "）": ")",
    "，": ", ",
    "。": ".",
    "：": ": ",
    "；": "; ",
    "？": "?",
    "！": "!",
    "→": "&#x2192;",
    "←": "&#x2190;",
    "↑": "&#x2191;",
    "↓": "&#x2193;",
    "↔": "&#x2194;",
    "×": "&#x00D7;",
    "·": "&#x00B7;",
    "—": "&#x2014;",
    "–": "&#x2013;",
}


CN_CHAR_RE = re.compile(r"[\u4e00-\u9fff]+")


def translate_text(text: str) -> tuple[str, list[str]]:
    """Apply dictionary substitutions to text. Returns (translated, untranslated_remaining)."""
    out = text
    for cn, en in TRANSLATIONS.items():
        if cn in out:
            out = out.replace(cn, en)
    untranslated = CN_CHAR_RE.findall(out)
    return out, untranslated


def translate_file(path: Path, dst: Path) -> tuple[bool, list[str]]:
    src_text = path.read_text(encoding="utf-8")
    out, missing = translate_text(src_text)
    if missing:
        return False, missing
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(out, encoding="utf-8")
    return True, []


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default=None)
    ap.add_argument("--report-only", action="store_true")
    args = ap.parse_args()

    sources = sorted(SRC_DIR.glob("*.svg"))
    sources = [s for s in sources if s.name != "placeholder.svg"]
    if args.only:
        sources = [s for s in sources if s.name.startswith(args.only)]

    print(f"Translating {len(sources)} SVGs...")
    all_missing: dict[str, list[str]] = {}
    written = 0
    for src in sources:
        rel = src.relative_to(SRC_DIR)
        dst = DST_DIR / rel.name
        if dst.exists():
            print(f"  skip (exists): {dst.relative_to(SRC_DIR)}")
            continue
        success, missing = translate_file(src, dst)
        if success:
            print(f"  wrote: {dst.relative_to(SRC_DIR)}")
            written += 1
        else:
            uniq = sorted(set(missing))
            all_missing[src.name] = uniq
            print(f"  partial: {src.name} ({len(uniq)} untranslated phrases)")
            if not args.report_only:
                # Write the partially translated version anyway so the user can
                # see which phrases still need translation.
                dst.parent.mkdir(parents=True, exist_ok=True)
                partial, _ = translate_text(src.read_text(encoding="utf-8"))
                dst.write_text(partial, encoding="utf-8")

    print(f"\n=== Summary ===")
    print(f"Written cleanly: {written}/{len(sources)}")
    print(f"Files with untranslated phrases: {len(all_missing)}")
    if all_missing:
        print("\nUntranslated phrases per file (sorted by frequency):")
        all_phrases: dict[str, int] = {}
        for phrases in all_missing.values():
            for p in phrases:
                all_phrases[p] = all_phrases.get(p, 0) + 1
        for phrase, count in sorted(all_phrases.items(), key=lambda x: -x[1])[:50]:
            print(f"  ({count:3d}) {phrase}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
