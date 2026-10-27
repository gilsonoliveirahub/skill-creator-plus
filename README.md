# skill-creator-plus

A [Claude Code](https://claude.com/claude-code) skill that creates, clones and improves other Claude Code skills. This is an **independent fork**, adapted and expanded by **Gilson Gomes de Oliveira**, built on top of two separate MIT-licensed sources:

- **Base project**: [`ojuliocouto/skill-creator-v2`](https://github.com/ojuliocouto/skill-creator-v2) by Júlio Couto — the 3-mode workflow (CREATE/CLONE/IMPROVE), the 5 category templates, the 6-criterion adversarial audit, and all original scripts and tests.
- **Ported ideas**: the `skillify` skill from [`coreyhaines31/makerskills`](https://github.com/coreyhaines31/makerskills) by Corey Haines — the license-check-and-attribution approach for adapting external skills, and the cross-skill learning-propagation / skill-vs-memory triage idea.

Neither original author is affiliated with or endorses this fork. Full copyright notices, license text, source commits and an itemized list of what was reused from each project are in [`THIRD-PARTY-NOTICES.md`](./THIRD-PARTY-NOTICES.md).

The skill body is in Portuguese.

## What's new in this fork

On top of everything the base project already did, this fork adds:

1. **CLONE EXTERNA** — a second path inside CLONE mode, for cloning a skill from *outside* `~/.claude/skills/` (a GitHub repo, agentskills.io, or a local path). Before copying anything, it runs a license check (green/yellow/red by license family), classifies the source into 3 buckets (keep verbatim / adapt / add) for approval, and writes an `attribution.md` into the new skill.
2. **Learning propagation in IMPROVE mode** — when an improvement request comes from a concrete learning in conversation (a correction, a validation, a gap found) rather than a routine audit request, the skill searches other installed skills for the same issue (confidence-tiered: high/medium/low) and decides, per learning, whether it belongs in that one skill, in the user's own long-term memory system, or both — approving changes file by file, never in bulk.
3. A new script, `scripts/license_check.py`, and a new reference guide per addition (`references/license-check.md`, `references/propagacao-e-memoria.md`).

Everything else — the CREATE workflow, the 5 templates, the audit criteria, the other 6 scripts, the test suite, the CI — is unchanged from the base project.

## What this is, and what it is not

**It is:**

- A **3-mode workflow** in `SKILL.md`:
  - **CREATE**: 6 phases. Research, architecture, build, description plus collision check, adversarial audit, delivery.
  - **CLONE**: LOCAL copies the structure of an installed skill and adapts it to a new domain. EXTERNA clones a third-party skill (GitHub, agentskills.io, local path) with a license-bucket check and an `attribution.md` before anything is copied.
  - **IMPROVE**: audits an installed skill, proposes fixes for every criterion under 8, applies the approved ones. When triggered by a concrete learning (not a routine audit), also searches other installed skills for the same issue and decides, per learning, whether it's skill-specific or belongs in long-term memory.
- **5 category templates** in `references/templates/`: `api-integration`, `workflow`, `analysis`, `creative`, `utility`.
- **7 reference guides** in `references/`: frontmatter, description, writing style, recurring patterns, a command cheat sheet, license-check buckets for CLONE EXTERNA, and learning-propagation/memory triage for IMPROVE. `patterns.md` ships with aggregate statistics only. `analyze_skills.py --generate-patterns` rewrites it with the catalog of your own installed skills.
- **7 working Python scripts** in `scripts/` (stdlib only, no `pip install`).
- **One HTML audit report template** in `assets/audit-report.html`.

**It is not:**

- A skill marketplace or installer. To find and install published skills, use `find-skills`.
- An eval runner. The audit is a static check of structure and content. It does not run the new skill against test prompts and it does not measure pass rates.
- A replacement for reading the skill it creates. A score of 45/60 means the structure is sound. It does not mean the domain content is correct.

## How it works

1. Claude Code loads `SKILL.md` when the user asks to create, clone or improve a skill ("cria uma skill de X", "melhora minha skill Y", `/skill-creator-plus`).
2. The skill detects the mode from the request.
3. In CREATE mode it asks 3 to 5 clarifying questions, researches the APIs and libraries, and runs `analyze_skills.py --search` to find similar installed skills.
4. It picks a category, reads the matching template and asks for approval of the structure and frontmatter.
5. `scaffold.py` creates the folder, `SKILL.md`, `scripts/` and `references/`. Claude then writes the real content.
6. `collision_check.py` compares the new description and triggers with every installed skill. A HIGH collision blocks delivery until the description or triggers change.
7. `audit_skill.py` scores 6 criteria from 0 to 10. The skill passes with 7 or more on each criterion and 45 or more in total. On a fail, Claude fixes the weak criteria and audits again, up to 3 attempts.

In CLONE EXTERNA or in a learning-driven IMPROVE, the extra steps from "What's new in this fork" run before or alongside this core flow — see `SKILL.md` for exactly where.

## Scripts

| Script | What it does |
|---|---|
| `analyze_skills.py` | Lists and searches installed skills (`--search "topic"`). |
| `collision_check.py` | Scores trigger and description overlap between a draft and installed skills. |
| `scaffold.py` | Creates the folder and files of a new skill from a category template. |
| `audit_skill.py` | Runs the 6-criterion audit and writes an optional HTML report (`--html <file>`). |
| `extract_frontmatter.py` | Prints the frontmatter (and optionally the body) of a `SKILL.md` as JSON. |
| `test_triggers.py` | Measures trigger precision and recall of a description against should-trigger and should-not-trigger queries, with Wilson score confidence bounds. |
| `license_check.py` | *(new in this fork)* Classifies a LICENSE file or name as verde/amarelo/vermelho before CLONE EXTERNA copies anything; exits 1 on vermelho. |

## Audit criteria

| # | Criterion | What it checks |
|---|---|---|
| 1 | Completeness | Full workflow, error handling, examples. |
| 2 | Trigger accuracy | Valid frontmatter, specific description. |
| 3 | Script quality | Working scripts with argparse, no stubs. |
| 4 | Documentation | Logical sections, adequate size, references. |
| 5 | Edge cases | Errors, config check, fallbacks. |
| 6 | Progressive disclosure | Focused `SKILL.md`, detail moved to `references/`. |

Self-audit of this fork on 2026-10-27: **57/60 (PASS)**, the same score as the base project before this fork's additions. The 3 lost points are in progressive disclosure: the audit does not find a clear, actionable first step — pre-existing in the base project, not introduced by this fork.

## Onboarding and prerequisites

Before installing, make sure you have:

- **Claude Code** (CLI, desktop app or IDE extension).
- **Python 3.9 or later.** The scripts use the standard library only. On Windows, install it from python.org and tick "Add python.exe to PATH". `SKILL.md` tells Claude to fall back to `py -3` or `python` when `python3` does not exist.

## Supported systems

The skill runs on **macOS, Linux and Windows**, inside the Claude Code CLI or the Claude desktop app. On Windows, Claude Code runs commands in Git Bash, so `~/.claude/skills/...` paths and `cat` work the same way.

The scripts handle the 3 things that usually break on Windows:

- **Console encoding.** Windows consoles default to cp1252. Every script switches its output to UTF-8, so accents and symbols never crash a run.
- **BOM.** Notepad can save `SKILL.md` and JSON files with a UTF-8 BOM. Every script reads with `utf-8-sig`.
- **Line endings.** `.gitattributes` keeps every file in LF. The scripts also read CRLF files correctly.

GitHub Actions proves this on every push (inherited from the base project's CI config): `ubuntu-latest`, `macos-latest` and `windows-latest`, each with Python 3.10 and 3.13. Each job runs the unit tests and then a smoke test that installs the skill under the real home and runs it from bash, the same way Claude Code does.

**No credentials, no API key, no account.** The skill only reads and writes local files. Phase 1 uses Claude Code's own WebSearch and WebFetch tools for research. `license_check.py` makes no network calls either — it only reads a local LICENSE file or a license name you pass it.

## Installation

**macOS and Linux (Terminal), or Windows in Git Bash:**

```bash
git clone https://github.com/gilsonoliveirahub/skill-creator-plus.git ~/.claude/skills/skill-creator-plus
```

**Windows in PowerShell:**

```powershell
git clone https://github.com/gilsonoliveirahub/skill-creator-plus.git "$env:USERPROFILE\.claude\skills\skill-creator-plus"
```

Do not use `~` in PowerShell: PowerShell does not expand it for `git`, and the clone goes to a folder named `~`.

**Without git:** on the repository page, click **Code**, then **Download ZIP**. Extract the ZIP and rename the folder to `skill-creator-plus`. Move it to `~/.claude/skills/` (on Windows: `C:\Users\<your user>\.claude\skills\`).

Restart Claude Code or open a new session. The skill must live at exactly `~/.claude/skills/skill-creator-plus/`, because `SKILL.md` calls its scripts and templates by that absolute path.

To verify the install:

```bash
python3 ~/.claude/skills/skill-creator-plus/scripts/audit_skill.py --skill-path ~/.claude/skills/skill-creator-plus/
```

On Windows in PowerShell:

```powershell
py -3 "$env:USERPROFILE\.claude\skills\skill-creator-plus\scripts\audit_skill.py" --skill-path "$env:USERPROFILE\.claude\skills\skill-creator-plus"
```

The last line must read `[PASS]` with a score of 45/60 or more.

## Author-specific conventions

Phase 5 contains 2 rules carried over from the base project's author:

- The HTML audit report goes to `$SCRATCHPAD`, a session-scoped scratch directory, and never to a loose `/tmp` path.
- The report is not opened automatically. It is only opened if the user asks, and then through whatever dedicated tooling that user's own setup provides — not the system's default browser.

On any machine, replace `$SCRATCHPAD` with any writable directory and open the report with any browser.

## Tests

```bash
python3 -m unittest discover -s tests -v
```

`tests/test_portabilidade.py` installs a copy of the skill under a fake home whose path has an accent and a space (`Usuário Teste`). It forces the console to cp1252 and feeds a `SKILL.md` saved with a BOM, CRLF line endings and an emoji. Then it runs all 7 scripts, including `license_check.py`.

## Repository layout

```
skill-creator-plus/
├── SKILL.md
├── README.md
├── LICENSE
├── THIRD-PARTY-NOTICES.md
├── .gitattributes
├── .github/workflows/ci.yml
├── tests/test_portabilidade.py
├── assets/audit-report.html
├── references/
│   ├── commands.md
│   ├── description-guide.md
│   ├── frontmatter-guide.md
│   ├── license-check.md
│   ├── patterns.md
│   ├── propagacao-e-memoria.md
│   ├── writing-guide.md
│   └── templates/ (analysis, api-integration, creative, utility, workflow)
└── scripts/ (7 Python scripts)
```

## Security

The repository contains no token, key, password or infrastructure ID. The scripts make no network calls.

## License

MIT. See [`LICENSE`](./LICENSE) and [`THIRD-PARTY-NOTICES.md`](./THIRD-PARTY-NOTICES.md) for the full copyright history of this fork.
