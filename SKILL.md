---
name: es-search
description: Use Voidtools Everything's es.exe for fast Windows file and folder discovery outside a known project tree, including file sizes and modification timestamps. Do not use it for exact paths or content search.
---

# Everything Cli Search

Use this skill for fast, read-only Windows file and folder discovery through Voidtools Everything's command-line client, `es.exe`. Prefer it when the target location is unknown, outside the current workspace, computer-wide, or filtered by indexed name, path, extension, size, or date metadata.

## Availability

Resolve the executable from `PATH` at most once per session, or after a failed query:

```powershell
$es = Get-Command es.exe -ErrorAction SilentlyContinue
```

- If `$es` is absent, use a narrowly scoped fallback.
- If a call reports `Everything IPC not found`, Everything is not running or its service is unavailable. Report the limitation briefly and use a fallback; do not repeatedly retry the same command.
- Do not install, start, repair, reindex, or otherwise change Everything unless the user asks.

## File listings

Return the smallest sufficient set of exact paths. When listing results, always include file size and last-modified time. Prefer this PowerShell-safe form so the resolved executable path is used:

```powershell
& $es.Source -n 20 -full-path-and-name -size -date-modified -date-format 1 "<Everything query>"
```

Start with a narrow query and the default cap of 20; refine it before increasing `-n`. Use `/ad` for folders, `/a-d` for files, and `-path` to constrain a subtree. Quote paths and search terms containing spaces.

```powershell
& $es.Source -path 'C:\Work' /a-d -n 20 -full-path-and-name -size -dm -date-format 1 'ext:xlsx'
& $es.Source /ad -n 20 -full-path-and-name -size -dm -date-format 1 'report'
```

Use Everything search terms such as `ext:`, `size:`, `dm:`, and `dc:` to narrow a query. Request `-json` only when structured output is needed, and use `-get-result-count` only if the count matters or a capped result needs refinement. Do not export results to a file unless asked.

## Search routing

`es.exe` indexes names, paths, and Everything metadata; it does not replace direct path checks, code search, or content search.

- Use `Test-Path` or `Get-Item` for an exact known path.
- In a repository with a `.codegraph/` directory, use CodeGraph first when locating or understanding code. It can follow symbols and call paths that filename search cannot.
- Use `rg --files` for filename lookup within a known workspace and `rg` for text inside files. Avoid Everything's `content:` search for known project trees.
- Use `es.exe` for unknown, external, computer-wide, or metadata-filtered discovery and include `-size -date-modified` whenever listing results.
- If no result is found, state the query or scope. A zero-result search describes the current Everything index; it does not prove an unindexed location is empty.

## Read-only operation

Do not use state-changing ES options such as `-exit`, `-reindex`, `-save-db`, `-save-settings`, `-clear-settings`, or run-count setters. Do not delete, move, copy, or open a result unless separately requested.
