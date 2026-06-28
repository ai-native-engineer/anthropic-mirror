#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "lecture-media" / "images.tsv"
CURATED = ROOT / "lecture-media" / "curated" / "images.tsv"
REVIEW = ROOT / "lecture-media" / "curated" / "semantic-review.tsv"
MD = ROOT / "lecture-media" / "curated" / "images.md"
ASSETS = ROOT / "lecture-media" / "curated" / "assets"
GENERIC = ("문서에 포함된 이미지", "관련 이미지", "시각 자료.", "visual inspection pending")


def read(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f, dialect="excel-tab"))


def fail(msg: str) -> int:
    print(msg, file=sys.stderr)
    return 1


def validate(final: bool) -> int:
    required = [RAW, CURATED, REVIEW, MD, ASSETS]
    missing = [str(p.relative_to(ROOT)) for p in required if not p.exists()]
    if missing:
        return fail("missing: " + ", ".join(missing))

    raw = read(RAW)
    curated = read(CURATED)
    review = read(REVIEW)
    raw_keys = {r["key"] for r in raw}
    by_key = {r["key"]: r for r in curated}
    if raw_keys != set(by_key):
        return fail(f"key mismatch: raw={len(raw_keys)} curated={len(by_key)} missing={len(raw_keys - set(by_key))} extra={len(set(by_key) - raw_keys)}")

    decisions = {"keep", "duplicate", "drop"}
    bad_decision = [r["key"] for r in curated if r.get("decision") not in decisions]
    kept = [r for r in curated if r.get("decision") == "keep"]
    dup = [r for r in curated if r.get("decision") == "duplicate"]
    drop = [r for r in curated if r.get("decision") == "drop"]
    bad_dup = [r["key"] for r in dup if not r.get("canonical_key") or by_key.get(r.get("canonical_key"), {}).get("decision") != "keep"]
    bad_drop = [r["key"] for r in drop if not r.get("curation_reason")]
    bad_keep = [
        r["key"]
        for r in kept
        if not r.get("curated_asset_path")
        or not (ROOT / r["curated_asset_path"]).exists()
        or not r.get("curated_description")
        or not r.get("source_context")
    ]
    if bad_decision or bad_dup or bad_drop or bad_keep:
        return fail(f"bad_decision={len(bad_decision)} bad_dup={len(bad_dup)} bad_drop={len(bad_drop)} bad_keep={len(bad_keep)}")

    if not final:
        print(f"draft ok: raw={len(raw)} keep={len(kept)} duplicate={len(dup)} drop={len(drop)} reviewed={len(review)}")
        return 0

    unreviewed = [r["key"] for r in kept if r.get("reviewed") != "yes" or r.get("context_checked") != "yes"]
    generic = [
        r["key"]
        for r in kept
        if any(g in (r.get("curated_description", "") + " " + r.get("visual_note", "")) for g in GENERIC)
        or len(r.get("visual_note", "")) < 12
    ]
    reviewed_decisions = {r.get("decision") for r in review}
    if unreviewed or generic or not {"keep", "duplicate", "drop"}.issubset(reviewed_decisions):
        return fail(f"unreviewed_keep={len(unreviewed)} generic_keep={len(generic)} review_decisions={sorted(reviewed_decisions)}")
    print(f"check ok: raw={len(raw)} keep={len(kept)} duplicate={len(dup)} drop={len(drop)} reviewed={len(review)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--draft-check", action="store_true")
    args = parser.parse_args()
    return validate(final=args.check and not args.draft_check)


if __name__ == "__main__":
    raise SystemExit(main())
