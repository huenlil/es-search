# es-search

A Codex skill for fast, read-only Windows file and folder discovery using Voidtools Everything's `es.exe` client.

It routes exact paths to direct checks, known project searches to `rg` (or CodeGraph for indexed code), and unknown or computer-wide discovery to Everything. Listings include full paths, file sizes, and modification timestamps.

## Prerequisites

- Windows
- [Everything](https://www.voidtools.com/) running and indexing the locations you want to search
- `es.exe` available on `PATH`

## Install in Codex

Clone the repository, then run this from the clone's parent directory to copy the repository folder into your Codex skills directory as `es-search`:

```powershell
Copy-Item -Recurse -Force .\es-search "$env:USERPROFILE\.codex\skills\es-search"
```

Restart or refresh Codex so it discovers the skill. Invoke it explicitly as `$es-search`, or let Codex select it for applicable file-discovery tasks.
