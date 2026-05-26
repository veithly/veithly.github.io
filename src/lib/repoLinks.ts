/**
 * Path display + GitHub-link resolution for source citations.
 *
 * Display rules:
 *   REF/codex/...                       → codex/...
 *   REF/openclaw/...                    → openclaw/...
 *   REF/hermes-agent/...                → hermes-agent/...
 *   REF/claude-code-2.1.88-expanded/... → claude-code/...   (kept as plain text, closed source)
 *
 * To repoint at a new snapshot:
 *   cd REF/<repo> && git rev-parse HEAD
 * then update the SHA below.
 */

interface RepoBinding {
  prefix: string;
  owner: string;
  name: string;
  sha: string;
  displayRoot: string;
}

const REPOS: RepoBinding[] = [
  {
    prefix: 'REF/codex/',
    owner: 'openai',
    name: 'codex',
    sha: 'f27cf9db0974d344d78e7e0b47e7c812776b1395',
    displayRoot: 'codex/',
  },
  {
    prefix: 'REF/openclaw/',
    owner: 'openclaw',
    name: 'openclaw',
    sha: 'f6d0712f508b1f926ad6fc42f7d07b1a60e62730',
    displayRoot: 'openclaw/',
  },
  {
    prefix: 'REF/hermes-agent/',
    owner: 'NousResearch',
    name: 'hermes-agent',
    sha: '2d59afd3da04812583ecbbf3be83539678a947c4',
    displayRoot: 'hermes-agent/',
  },
];

const CLAUDE_PREFIX_RE = /^REF\/claude-code(?:-[^/]+)?\//;
const CLAUDE_DISPLAY_ROOT = 'claude-code/';

export interface ResolvedLink {
  /** GitHub blob URL for the pinned SHA, or null when the repo is closed-source. */
  url: string | null;
  /** Path stripped of REF/ prefix and version suffix; safe to render as the visible label. */
  display: string;
}

/**
 * Resolve a REF/<repo>/path[:lines] into a display path + (optional) GitHub blob URL.
 *
 * `lines` accepts the formats the docs use:
 *   "120"           → #L120
 *   "120-180"       → #L120-L180
 *   "120,180,200"   → #L120 (we pick the first range; GitHub doesn't support disjoint highlights)
 */
export function resolveRepoLink(path: string, lines?: string): ResolvedLink {
  for (const repo of REPOS) {
    if (!path.startsWith(repo.prefix)) continue;
    const rel = path.slice(repo.prefix.length);
    const display = `${repo.displayRoot}${rel}${lines ? `:${lines}` : ''}`;
    if (!rel) {
      return { url: null, display };
    }
    let hash = '';
    if (lines) {
      const first = lines.split(',')[0]?.trim();
      if (first) {
        const m = first.match(/^(\d+)\s*-\s*(\d+)$/);
        if (m) hash = `#L${m[1]}-L${m[2]}`;
        else if (/^\d+$/.test(first)) hash = `#L${first}`;
      }
    }
    const url = `https://github.com/${repo.owner}/${repo.name}/blob/${repo.sha}/${rel}${hash}`;
    return { url, display };
  }

  const claudeMatch = path.match(CLAUDE_PREFIX_RE);
  if (claudeMatch) {
    const rel = path.slice(claudeMatch[0].length);
    return {
      url: null,
      display: `${CLAUDE_DISPLAY_ROOT}${rel}${lines ? `:${lines}` : ''}`,
    };
  }

  return {
    url: null,
    display: `${path}${lines ? `:${lines}` : ''}`,
  };
}

/** True for Claude Code's REF tree (kept as plain text — closed source). */
export function isClaudeRef(path: string): boolean {
  return CLAUDE_PREFIX_RE.test(path);
}
