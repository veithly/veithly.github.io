#!/usr/bin/env node
/**
 * 校验 src/content/docs/patterns/*.mdx 是否包含 10 段模板标题。
 * 缺一节即报错。仅对正式章节（不是 stub）生效。
 */
import { readFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const REQUIRED_SECTIONS = [
  '## §1 · 30 秒结论',
  '## §2 · 基础架构图',
  '## §3 · 四系统怎么做',
  '## §4 · 共同点',
  '## §5 · 差异点',
  '## §6 · 我的点评',
  '## §7 · 自己实现怎么选',
  '## §8 · 动画图解',
  '## §9 · 延伸阅读',
  '## §10 · 小练习',
];

const PATTERNS_DIR = 'src/content/docs/patterns';

function listMdx(dir) {
  return readdirSync(dir)
    .filter((f) => f.endsWith('.mdx'))
    .map((f) => join(dir, f));
}

function isStub(content) {
  return /^🚧\s*WIP/m.test(content) && !content.includes('## §1');
}

let failures = 0;
for (const file of listMdx(PATTERNS_DIR)) {
  const content = readFileSync(file, 'utf8');
  if (isStub(content)) {
    console.log(`⏭  ${file} — stub, skipped`);
    continue;
  }
  const missing = REQUIRED_SECTIONS.filter(
    (h) => !content.includes(h.split(' · ')[0]) // 至少匹配 ## §N
  );
  if (missing.length) {
    console.error(`❌ ${file}`);
    missing.forEach((m) => console.error(`   missing: ${m}`));
    failures++;
  } else {
    console.log(`✅ ${file} — all 10 sections present`);
  }
}

if (failures > 0) {
  console.error(`\n${failures} chapter(s) failed template check.`);
  process.exit(1);
}
console.log('\nAll chapters pass template check.');
