#!/usr/bin/env python3
"""Dependency-free release checks for the public research export."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()

REQUIRED = {
    "README.md",
    "PAPER.md",
    "CLAIM-EVIDENCE-LEDGER.csv",
    "SOURCE-AND-LICENSE-REGISTRY.csv",
    "LIMITATIONS-AND-NON-CLAIMS.md",
    "RELEASE-GATE.md",
    "PUBLICATION-SANITATION.md",
    "paper/index.html",
    "paper/governed-agent-organizations.pdf",
    "reviews/TECHNICAL-REVIEW.md",
    "reviews/CITATION-AND-LICENSE-REVIEW.md",
    "reviews/PRIVACY-AND-EDITORIAL-REVIEW.md",
}

ALLOWED_CLASSES = {
    "prior published result",
    "repository-statically-observed mechanism",
    "repository-test-covered mechanism",
    "implemented mechanism",
    "independently demonstrated behavior",
    "repeated operating result",
    "business outcome",
    "inference",
    "hypothesis",
    "UNKNOWN",
}

# These strings may appear inside this script's constants, so SELF is excluded.
FORBIDDEN_TEXT = {
    "aigent-os-private",
    "aigent-os-program",
    "gpt-grok-workbench",
    "issuecomment-",
    "C:\\Users\\",
}

UNRESOLVED_SOURCE_MARKERS = {
    "PIN_REQUIRED",
    "LICENSE_REVIEW_REQUIRED",
}

TEXT_SUFFIXES = {".md", ".csv", ".txt", ".yml", ".yaml", ".py", ".html"}
UUID_RE = re.compile(
    r"\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b",
    re.IGNORECASE,
)
EMAIL_RE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)


def check_required(errors: list[str]) -> None:
    for path in sorted(REQUIRED):
        target = ROOT / path
        if not target.is_file():
            errors.append(f"missing required file: {path}")
        elif target.stat().st_size == 0:
            errors.append(f"required file is empty: {path}")


def check_claim_classes(errors: list[str]) -> None:
    path = ROOT / "CLAIM-EVIDENCE-LEDGER.csv"
    if not path.is_file():
        return
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if "claim_class" not in (reader.fieldnames or []):
            errors.append("claim ledger lacks claim_class column")
            return
        seen: set[str] = set()
        for line, row in enumerate(reader, start=2):
            claim_id = (row.get("claim_id") or "").strip()
            if not claim_id:
                errors.append(f"{path.name}:{line}: missing claim_id")
            elif claim_id in seen:
                errors.append(f"{path.name}:{line}: duplicate claim_id {claim_id!r}")
            seen.add(claim_id)
            value = (row.get("claim_class") or "").strip()
            if value not in ALLOWED_CLASSES:
                errors.append(f"{path.name}:{line}: invalid claim_class {value!r}")


def check_sources(errors: list[str]) -> None:
    path = ROOT / "SOURCE-AND-LICENSE-REGISTRY.csv"
    if not path.is_file():
        return
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        needed = {"source_id", "version_or_pin", "license_or_terms", "release_status"}
        missing = needed - set(reader.fieldnames or [])
        if missing:
            errors.append(f"source registry lacks columns: {', '.join(sorted(missing))}")
            return
        seen: set[str] = set()
        for line, row in enumerate(reader, start=2):
            source_id = (row.get("source_id") or "").strip()
            if not source_id:
                errors.append(f"{path.name}:{line}: missing source_id")
            elif source_id in seen:
                errors.append(f"{path.name}:{line}: duplicate source_id {source_id!r}")
            seen.add(source_id)
            joined = " ".join(str(v) for v in row.values())
            for marker in UNRESOLVED_SOURCE_MARKERS:
                if marker in joined:
                    errors.append(f"{path.name}:{line}: unresolved marker {marker}")
            if (row.get("release_status") or "").strip() != "READY":
                errors.append(f"{path.name}:{line}: release_status is not READY")


def check_public_text(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if path.resolve() == SELF:
            continue
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if ".git" in path.parts or "_renders" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        rel = path.relative_to(ROOT)
        for needle in FORBIDDEN_TEXT:
            if needle in text:
                errors.append(f"{rel}: contains private/internal marker {needle!r}")
        if UUID_RE.search(text):
            errors.append(f"{rel}: contains UUID-like identifier")
        if EMAIL_RE.search(text):
            errors.append(f"{rel}: contains email address")


def check_rendered_pdf(errors: list[str]) -> None:
    path = ROOT / "paper" / "governed-agent-organizations.pdf"
    if not path.is_file():
        return
    raw = path.read_bytes()
    for needle in (b"will@", b"blindmonkeyproduced", b"aigent-os-private", b"gpt-grok-workbench"):
        if needle.lower() in raw.lower():
            errors.append(f"{path.relative_to(ROOT)}: binary contains forbidden metadata/text {needle!r}")


def main() -> int:
    errors: list[str] = []
    check_required(errors)
    check_claim_classes(errors)
    check_sources(errors)
    check_public_text(errors)
    check_rendered_pdf(errors)
    if errors:
        print("PUBLIC RELEASE CHECK: FAIL", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("PUBLIC RELEASE CHECK: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
