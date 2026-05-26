# 写作贡献指南

## 章节强制模板（10 段）

每个 `src/content/docs/patterns/NN-*.mdx` 必须包含以下 10 个二级标题，**缺一节即不能上线**（CI 会拒）：

```
## §1 · 30 秒结论
## §2 · 基础架构图
## §3 · 四系统怎么做
## §4 · 共同点（模式提炼）
## §5 · 差异点（取舍解释）
## §6 · 我的点评
## §7 · 自己实现怎么选
## §8 · 动画图解
## §9 · 延伸阅读 / 源码入口
## §10 · 小练习
```

母版参考：`src/content/docs/patterns/02-agent-loop.mdx`。

## 必备组件

| 段位 | 组件                | 用途                |
| ---- | ------------------- | ------------------- |
| §1   | `<Verdict>`         | 一句话结论          |
| §2   | `<Diagram>` / `<AgentLoopSVG>` | 静态或动态图 |
| §3   | `<CompareTable>`    | 四系统横向比较      |
| §5   | `<TradeOff>`        | 二维取舍图          |
| §6   | `<ScoreCard>`       | 评分卡（4 行）      |
| §7   | `<BuildRecipe>`     | 抄作业建议三段卡    |
| §9   | `<SourceTrail>`     | 源码入口            |

import 路径全用 `@components/*`：

```mdx
import Verdict from '@components/Verdict.astro';
import CompareTable from '@components/CompareTable.astro';
...
```

## 视觉规则

- 所有架构图都用 **Excalidraw** 画。源文件放 `docs-site/diagrams/NN-*.excalidraw`，导出 SVG 到 `docs-site/public/diagrams/NN-*.svg`。
- 不允许在 MDX 里手写大型 SVG（除非用 `<AgentLoopSVG>` 这类复用组件）。
- 颜色编码遵循 `src/styles/tokens.css`：
  - 🟢 共同点（绿）
  - 🟠 差异点（橙）
  - 🟣 点评（紫）
  - 🔴 风险（红）
  - 🔵 源码（蓝）

## i18n 流程

1. 先用中文写完整章（中文 = 源）
2. 跑 `pnpm check:template` 确认 10 段齐
3. 在 `src/content/docs/en/<相同路径>` 复写英文（**作者复写，不机器翻译**）
4. 跑 `pnpm check:i18n` 确认中英文件 1:1 对齐
5. 英文未完成时允许 stub（顶部一行 `🚧 WIP — see Chinese version` + 中文链接）

## 引用规范

- 所有"评价类断言"必须挂引用：`REF/...` 路径或官方文档外链。
- 闭源系统（Claude Code）章节顶部必须出现：
  > 以下基于公开文档 + sourcemap 解包做行为推断，非源码逐行。

## 提交前 checklist

```bash
pnpm check:all   # = astro check + template check + i18n parity check
pnpm build       # 确认能 SSG 通过
pnpm preview     # 本地预览
```
