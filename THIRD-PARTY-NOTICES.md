# Third-Party Notices

This project (`skill-creator-plus`) is an independent fork that combines code and ideas from two separate MIT-licensed sources. Both are reproduced below in full, as required by the MIT License ("The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software"). Neither original author endorses or is affiliated with this fork.

---

## 1. Base project: `skill-creator-v2`

- **Repository**: https://github.com/ojuliocouto/skill-creator-v2
- **Author**: Júlio Couto
- **License**: MIT
- **Commit used as the base of this fork**: `515687de0a4dcab9a1899b728bda04e7de666c37`
- **What was used**: the entire original project — `SKILL.md` (CREATE/CLONE/IMPROVE workflow, 6-criterion audit), all 5 category templates, all original writing guides, all 6 original Python scripts (`analyze_skills.py`, `collision_check.py`, `scaffold.py`, `audit_skill.py`, `extract_frontmatter.py`, `test_triggers.py`), the HTML audit report template, the portability test suite, and the CI workflow. This fork keeps all of it unchanged except where noted in section 3 below.

### License text

```
MIT License

Copyright (c) 2026 Júlio Couto

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 2. Ported ideas: `skillify` (from the `makerskills` pack)

- **Repository**: https://github.com/coreyhaines31/makerskills
- **Skill path within that repository**: `skills/skillify/SKILL.md`
- **Author**: Corey Haines
- **License**: MIT
- **Commit used when porting**: `ea7dd78515839ff11fc24e79ba0c53db2d5fff6c`
- **What was used**: `skillify` has no Python scripts — what was ported is its *process design*, translated into Portuguese and adapted to this project's conventions, specifically:
  1. The license-bucket classification scheme for adapting external skills (green/yellow/red by license family) — reproduced in `references/license-check.md` and implemented as new original code in `scripts/license_check.py` (this script itself was written from scratch for this fork; only the classification scheme/table structure comes from `skillify`).
  2. The three-bucket change classification for adapting external material ("keep verbatim" / "adapt" / "add") — reproduced in `references/license-check.md`.
  3. The `attribution.md` template shape (source, repository, author, commit SHA, license, date, what was kept/adapted/added, upgrade check via `git ls-remote`) — reproduced (translated) in `references/license-check.md`.
  4. The cross-skill learning-propagation idea (grep for affected skills, classify by confidence: high/medium/low) and the skill-vs-memory triage question — reproduced (translated and adapted) in `references/propagacao-e-memoria.md`.

None of `skillify`'s own text was kept verbatim in English; the above elements were translated into Portuguese and rewritten to fit this project's existing structure and tone. This notice exists because MIT requires the original copyright notice to travel with substantial portions of the licensed work, and the structural/template elements above count as such.

### License text

```
MIT License

Copyright (c) 2026 Corey Haines

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 3. What this fork (`skill-creator-plus`) adds on top of both

- **Author of these additions**: Gilson Gomes de Oliveira
- **New mode**: CLONE EXTERNA — clone a skill from outside `~/.claude/skills/` (GitHub, agentskills.io, local path) with a mandatory license check, three-bucket classification for approval, and a generated `attribution.md` before anything is copied. (`SKILL.md`, `references/license-check.md`, `scripts/license_check.py`)
- **New step**: learning propagation inside IMPROVE mode — when a change request comes from a concrete learning rather than a routine audit, search other installed skills for the same issue (confidence-tiered: high/medium/low) and decide, per learning, whether it belongs in that one skill or in the user's own long-term memory system, approving changes file by file. (`SKILL.md`, `references/propagacao-e-memoria.md`)
- **New script**: `scripts/license_check.py` — classifies a LICENSE file or bare license name into green/yellow/red, stdlib-only, following the same code style as the 6 original scripts.
- **New test**: one portability test for `license_check.py`, added to the existing `tests/test_portabilidade.py` in the same style as the original 6.

All of the above is released under the same MIT License as the rest of this repository (see `LICENSE`).
