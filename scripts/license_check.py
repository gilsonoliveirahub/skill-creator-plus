#!/usr/bin/env python3
"""Classify a license (file or name) as verde/amarelo/vermelho before cloning a third-party skill."""

import sys
from pathlib import Path

# Windows consoles default to cp1252; force UTF-8 so accents and symbols never crash output.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")


GREEN = ("mit", "apache-2.0", "apache 2.0", "apache license", "bsd-2-clause", "bsd-3-clause",
         "bsd license", "isc license", "cc0", "cc0-1.0", "unlicense")
YELLOW = ("mpl-2.0", "mozilla public license", "lgpl-2.1", "lgpl-3.0", "lesser general public")
RED = ("gpl-2.0", "gpl-3.0", "gnu general public license", "agpl", "affero", "proprietary",
       "proprietaria", "all rights reserved")

ACTIONS = {
    "verde": "Pode copiar e adaptar livremente. So falta escrever o attribution.md.",
    "amarelo": "Pode adaptar, mas confirmar antes e avisar sobre reciprocidade a nivel de ficheiro.",
    "vermelho": "NAO copiar sem aprovacao explicita e por escrito do usuario.",
}


def classify_text(text: str) -> dict:
    """Classify raw license text (or a bare license name) into verde/amarelo/vermelho."""
    lowered = text.lower()

    for name in RED:
        if name in lowered:
            return {"bucket": "vermelho", "matched": name, "action": ACTIONS["vermelho"]}
    for name in YELLOW:
        if name in lowered:
            return {"bucket": "amarelo", "matched": name, "action": ACTIONS["amarelo"]}
    for name in GREEN:
        if name in lowered:
            return {"bucket": "verde", "matched": name, "action": ACTIONS["verde"]}

    if not lowered.strip():
        return {"bucket": "vermelho", "matched": "(sem licenca)", "action": ACTIONS["vermelho"]}

    return {"bucket": "amarelo", "matched": "(nao reconhecida, verificar manualmente)", "action": ACTIONS["amarelo"]}


def classify_path(path: str) -> dict:
    """Classify a LICENSE file on disk. Missing file counts as 'no license' (vermelho)."""
    p = Path(path)
    if not p.exists():
        return classify_text("")
    try:
        text = p.read_text(encoding="utf-8-sig", errors="replace")
    except OSError:
        return classify_text("")
    return classify_text(text[:4000])


if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Classifica uma licenca antes de clonar skill externa (CLONE EXTERNA)")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--path", help="Caminho para o ficheiro LICENSE")
    source.add_argument("--name", help="Nome da licenca, se nao houver ficheiro (ex: MIT, GPL-3.0)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    result = classify_path(args.path) if args.path else classify_text(args.name)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        icon = {"verde": "[OK]", "amarelo": "[!]", "vermelho": "[X]"}[result["bucket"]]
        print(f"{icon} {result['bucket'].upper()} (match: {result['matched']})")
        print(result["action"])
        if result["bucket"] == "vermelho":
            sys.exit(1)
