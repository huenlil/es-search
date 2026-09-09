# es-search

A portable Agent Skill for fast, read-only Windows file and folder discovery using Voidtools Everything's `es.exe` client. It can be used by Codex, OpenCode, Claude-compatible agents, and other agents that load `SKILL.md` files.

It routes exact paths to direct checks, known project searches to `rg` (or CodeGraph for indexed code), and unknown or computer-wide discovery to Everything. Listings include full paths, file sizes, and modification timestamps.

## Prerequisites

- Windows
- [Everything](https://www.voidtools.com/) running and indexing the locations you want to search
- `es.exe` available on `PATH`

## Install

Clone the repository and copy the `SKILL.md` folder into the skill directory used by your agent. The folder must be named `es-search`.

For Codex:

```powershell
Copy-Item -Recurse -Force .\es-search "$env:USERPROFILE\.codex\skills\es-search"
```

For OpenCode, use either a project-local or global location:

```powershell
Copy-Item -Recurse -Force .\es-search ".opencode\skills\es-search"
Copy-Item -Recurse -Force .\es-search "$env:USERPROFILE\.config\opencode\skills\es-search"
```

OpenCode also supports the compatibility locations `.agents/skills/es-search` and `.claude/skills/es-search` (project-local or under your user profile). Other agents may use their own skill directory; preserve `SKILL.md` and its YAML frontmatter.

The `agents/openai.yaml` file is optional Codex UI metadata. Agents that do not use it can ignore it. Restart or refresh the agent after installation so it discovers the skill.
