from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
METADATA = ROOT / "agents" / "openai.yaml"


def fail(message: str) -> None:
    print(f"Validation failed: {message}", file=sys.stderr)
    raise SystemExit(1)


if not SKILL.is_file():
    fail("SKILL.md is missing")
if not METADATA.is_file():
    fail("agents/openai.yaml is missing")

contents = SKILL.read_text(encoding="utf-8")
if not contents.startswith("---\n"):
    fail("SKILL.md must start with YAML frontmatter")

try:
    frontmatter, _ = contents[4:].split("\n---\n", 1)
except ValueError:
    fail("SKILL.md frontmatter is not closed")

if not re.search(r"^name:\s*es-search\s*$", frontmatter, re.MULTILINE):
    fail("SKILL.md frontmatter name must be es-search")
if not re.search(r"^description:\s*\S", frontmatter, re.MULTILINE):
    fail("SKILL.md frontmatter needs a description")
if "TODO" in contents:
    fail("SKILL.md contains an unfinished TODO")

print("Skill package is valid.")
