// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import mdx from '@astrojs/mdx';
import react from '@astrojs/react';

// https://astro.build/config
export default defineConfig({
  site: 'https://agent-architecture-patterns.pages.dev',
  integrations: [
    starlight({
      title: {
        'zh-CN': 'Agent Harness 架构设计',
        en: 'Agent Harness Architecture',
      },
      description: 'Source-grounded architecture notes on Codex, Claude Code, OpenClaw, and Hermes for engineers building agent harnesses.',
      defaultLocale: 'root',
      locales: {
        root: { label: '中文', lang: 'zh-CN' },
        en: { label: 'English', lang: 'en' },
      },
      social: [
        { icon: 'github', label: 'GitHub', href: 'https://github.com/veithly/agent-architecture-patterns' },
      ],
      customCss: ['./src/styles/tokens.css', './src/styles/handdrawn.css'],
      head: [
        {
          tag: 'meta',
          attrs: {
            property: 'og:title',
            content: 'Agent Harness Architecture Patterns',
          },
        },
        {
          tag: 'meta',
          attrs: {
            property: 'og:description',
            content: 'Bilingual source-grounded notes on Codex, Claude Code, OpenClaw, and Hermes for engineers building agent harnesses.',
          },
        },
        {
          tag: 'meta',
          attrs: { property: 'og:type', content: 'website' },
        },
        {
          tag: 'meta',
          attrs: { property: 'og:url', content: 'https://agent-architecture-patterns.pages.dev' },
        },
        {
          tag: 'meta',
          attrs: { name: 'twitter:card', content: 'summary_large_image' },
        },
        {
          tag: 'meta',
          attrs: { name: 'twitter:title', content: 'Agent Harness Architecture Patterns' },
        },
        {
          tag: 'meta',
          attrs: {
            name: 'twitter:description',
            content: 'A bilingual field guide to real agent harness architecture.',
          },
        },
        {
          tag: 'link',
          attrs: { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        },
        {
          tag: 'link',
          attrs: {
            rel: 'preconnect',
            href: 'https://fonts.gstatic.com',
            crossorigin: '',
          },
        },
        {
          tag: 'link',
          attrs: {
            rel: 'stylesheet',
            href: 'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap',
          },
        },
      ],
      sidebar: [
        {
          label: '第一组 · Agent 基础设计',
          translations: { en: 'Group 1 · Agent Fundamentals' },
          items: [
            { slug: 'patterns/01-overview' },
            { slug: 'patterns/02-agent-loop' },
            { slug: 'patterns/03-context-system' },
            { slug: 'patterns/04-tool-system' },
            { slug: 'patterns/05-verifier' },
          ],
        },
        {
          label: '第二组 · Coding Agent 工程',
          translations: { en: 'Group 2 · Coding Agent Engineering' },
          items: [
            { slug: 'patterns/06-file-edit-patch' },
            { slug: 'patterns/07-shell-execution' },
            { slug: 'patterns/08-git-workflow' },
            { slug: 'patterns/09-code-review' },
          ],
        },
        {
          label: '第三组 · 并发与运行时',
          translations: { en: 'Group 3 · Concurrency & Runtime' },
          items: [
            { slug: 'patterns/10-subagents' },
            { slug: 'patterns/11-session-lifecycle' },
            { slug: 'patterns/12-permissions-approvals' },
            { slug: 'patterns/13-sandbox-execution' },
            { slug: 'patterns/14-multi-channel-entry' },
          ],
        },
        {
          label: '第四组 · 演化与安全',
          translations: { en: 'Group 4 · Evolution & Safety' },
          items: [
            { slug: 'patterns/15-observability-cost' },
            { slug: 'patterns/16-memory' },
            { slug: 'patterns/17-skills' },
            { slug: 'patterns/18-cron-background' },
            { slug: 'patterns/19-self-improvement' },
            { slug: 'patterns/20-security' },
            { slug: 'patterns/21-todo-list' },
            { slug: 'patterns/22-execution-state-surfaces' },
          ],
        },
        {
          label: '系统画像',
          translations: { en: 'System Profiles' },
          collapsed: true,
          items: [
            { slug: 'systems/codex' },
            { slug: 'systems/claude-code' },
            { slug: 'systems/openclaw' },
            { slug: 'systems/hermes' },
          ],
        },
        {
          label: '面试题索引',
          translations: { en: 'Interview index' },
          items: [{ slug: 'interview' }],
        },
        {
          label: '配套 Skill',
          translations: { en: 'Companion Skill' },
          items: [{ slug: 'skill' }],
        },
        {
          label: '组件预览（dev）',
          translations: { en: 'Component preview (dev)' },
          collapsed: true,
          items: [{ slug: 'preview' }],
        },
      ],
      lastUpdated: true,
      pagination: true,
      tableOfContents: { minHeadingLevel: 2, maxHeadingLevel: 3 },
    }),
    react(),
    mdx(),
  ],
});
