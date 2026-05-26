#!/usr/bin/env node
/**
 * 校验中英文 docs 1:1 对应：
 *   src/content/docs/<path>.mdx  必须有对应的  src/content/docs/en/<path>.mdx
 *   反之同理。
 * 允许英文版是 stub（"🚧 WIP"），但文件必须存在。
 */
import { existsSync, readdirSync, statSync } from 'node:fs';
import { join, relative } from 'node:path';

const ROOT = 'src/content/docs';
const EN_ROOT = 'src/content/docs/en';

function walk(dir, base = dir) {
  const out = [];
  for (const entry of readdirSync(dir)) {
    const p = join(dir, entry);
    if (statSync(p).isDirectory()) {
      if (entry === 'en') continue; // skip en when scanning root
      out.push(...walk(p, base));
    } else if (entry.endsWith('.mdx') || entry.endsWith('.md')) {
      out.push(relative(base, p));
    }
  }
  return out;
}

const zhFiles = walk(ROOT).filter((p) => !p.startsWith('en' + (process.platform === 'win32' ? '\\' : '/')));
const enFiles = existsSync(EN_ROOT) ? walk(EN_ROOT) : [];

const enSet = new Set(enFiles);
const zhSet = new Set(zhFiles);

let failures = 0;

for (const f of zhFiles) {
  if (!enSet.has(f)) {
    console.error(`❌ missing EN mirror: src/content/docs/en/${f}`);
    failures++;
  }
}
for (const f of enFiles) {
  if (!zhSet.has(f)) {
    console.error(`❌ missing ZH source: src/content/docs/${f}`);
    failures++;
  }
}

if (failures > 0) {
  console.error(`\n${failures} i18n parity issue(s).`);
  process.exit(1);
}
console.log(`✅ i18n parity OK (${zhFiles.length} pages × 2 locales).`);
