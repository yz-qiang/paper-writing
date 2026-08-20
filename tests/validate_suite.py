#!/usr/bin/env python3
"""Validate the local paper-writing skill suite."""

from __future__ import annotations

import re
import sys
from pathlib import Path


SUITE = Path(__file__).resolve().parents[1]


def read(path: Path, failures: list[str]) -> str:
    if not path.is_file():
        failures.append(f"missing file: {path.relative_to(SUITE)}")
        return ""
    return path.read_text(encoding="utf-8")


def require(text: str, needle: str, label: str, failures: list[str]) -> None:
    if needle not in text:
        failures.append(f"{label}: missing required text {needle!r}")


def validate_skill(name: str, failures: list[str]) -> str:
    root = SUITE / name
    skill = read(root / "SKILL.md", failures)
    metadata = read(root / "agents" / "openai.yaml", failures)
    if not skill:
        return ""

    match = re.match(r"\A---\n(.*?)\n---\n", skill, re.DOTALL)
    if not match:
        failures.append(f"{name}: invalid or missing YAML frontmatter")
        return skill

    frontmatter = match.group(1)
    require(frontmatter, f"name: {name}", name, failures)
    require(frontmatter, "description: Use when", name, failures)
    require(metadata, f"$${name}".replace("$$", "$"), f"{name} metadata", failures)
    return skill


def main() -> int:
    failures: list[str] = []

    core = validate_skill("paper-writing-core", failures)
    reasoning = validate_skill("paper-reasoning", failures)
    drafting = validate_skill("paper-drafting", failures)
    polish = validate_skill("paper-polish", failures)

    standards = read(
        SUITE / "paper-writing-core" / "references" / "writing-standards.md",
        failures,
    )
    contract = read(
        SUITE / "paper-writing-core" / "references" / "section-contract.md",
        failures,
    )

    for phrase in (
        "Author clarification",
        "Implementation is evidence, not the paper outline",
        "Progressive disclosure",
        "many-to-many",
        "one semantic job",
        "Dynamic regression testing",
    ):
        require(standards, phrase, "writing standards", failures)

    for field in (
        "Section:",
        "Profile:",
        "Status: proposed | approved",
        "Question answered:",
        "Main claim:",
        "Evidence and source files:",
        "Necessary qualifiers:",
        "Claims that must not be made:",
        "Paragraph plan:",
    ):
        require(contract, field, "section contract", failures)

    profiles = {
        "introduction.md": ("study-driven", "technique-driven", "required capability"),
        "approach.md": ("local problem", "stage output", "next stage"),
        "empirical-study.md": ("research question", "frozen", "later sections"),
        "results.md": ("quantitative evidence", "bounded answer", "Discussion"),
        "experimental-setup.md": ("environment", "baselines", "reproduction"),
        "discussion.md": ("supported interpretation", "prior work", "limitations"),
        "threats.md": ("threat source", "mitigation", "remaining boundary"),
    }
    for filename, phrases in profiles.items():
        text = read(
            SUITE / "paper-writing-core" / "references" / "profiles" / filename,
            failures,
        )
        for phrase in phrases:
            require(text, phrase, filename, failures)

    for phrase in (
        "paper-writing-core",
        "Status: proposed",
        "Do not draft complete manuscript prose",
        "author-designated",
        "reviewer audit",
    ):
        require(reasoning, phrase, "paper-reasoning", failures)

    for phrase in (
        "paper-writing-core",
        "Status: approved",
        "guided mode",
        "full-section mode",
        "Do not change",
    ):
        require(drafting, phrase, "paper-drafting", failures)

    for phrase in (
        "one item subsumes another",
        "apostrophe-s possessives",
    ):
        require(polish, phrase, "paper-polish", failures)

    for path in SUITE.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".yaml"}:
            text = path.read_text(encoding="utf-8")
            if re.search(r"\b(?:TODO|TBD|FIXME)\b", text):
                failures.append(f"placeholder marker found: {path.relative_to(SUITE)}")

    if failures:
        print("FAIL: paper-writing suite validation")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("PASS: paper-writing suite validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
