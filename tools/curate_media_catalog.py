#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import html
import re
import shutil
from pathlib import Path

try:
    from PIL import Image, ImageDraw
except Exception:  # pragma: no cover
    Image = ImageDraw = None


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "lecture-media" / "images.tsv"
OUT = ROOT / "lecture-media" / "curated"
MANUAL = OUT / "manual-review.tsv"
GENERIC = ("문서에 포함된 이미지", "관련 이미지", "Anthropic/Claude 미러 문서에 포함된 이미지")
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg", ".avif"}


def clean(value: str) -> str:
    value = html.unescape(value or "")
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def parts(value: str) -> list[str]:
    return [p.strip() for p in (value or "").split(" | ") if p.strip()]


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f, dialect="excel-tab"))


def write_tsv(path: Path, data: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore", dialect="excel-tab")
        w.writeheader()
        w.writerows(data)


def asset_path(row: dict[str, str]) -> Path | None:
    value = row.get("asset_path") or row.get("preview")
    if not value or value.startswith(("http://", "https://")):
        return None
    path = ROOT / value
    return path if path.exists() and path.is_file() else None


def image_suffix(path: Path, data: bytes | None = None) -> str:
    suffix = path.suffix.lower()
    if suffix in IMAGE_SUFFIXES:
        return suffix
    head = (data if data is not None else path.read_bytes())[:64]
    if head.startswith(b"\x89PNG\r\n\x1a\n"):
        return ".png"
    if head.startswith(b"\xff\xd8\xff"):
        return ".jpg"
    if head[:4] == b"RIFF" and head[8:12] == b"WEBP":
        return ".webp"
    if head[4:8] == b"ftyp" and head[8:12] in {b"avif", b"avis"}:
        return ".avif"
    if head.lstrip().startswith((b"<svg", b"<?xml")):
        return ".svg"
    return suffix or ".img"


def asset_name(path: Path) -> str:
    suffix = image_suffix(path)
    if path.name.lower().endswith(suffix):
        return path.name
    base = path.with_suffix("").name if path.suffix.lower() == ".img" else path.name
    return base if base.lower().endswith(suffix) else f"{base}{suffix}"


def asset_meta(path: Path | None) -> tuple[str, str, str]:
    if not path:
        return "", "", ""
    data = path.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    suffix = image_suffix(path, data)
    width = height = ""
    if Image and suffix not in {".svg", ".avif", ".img"}:
        try:
            with Image.open(path) as im:
                width, height = map(str, im.size)
        except Exception:
            pass
    if not width and suffix == ".svg":
        text = data[:4000].decode("utf-8", "ignore")
        m = re.search(r"<svg[^>]*\bwidth=[\"']?([0-9.]+).*?\bheight=[\"']?([0-9.]+)", text)
        if m:
            width, height = str(int(float(m.group(1)))), str(int(float(m.group(2))))
        elif m := re.search(r"\bviewBox=[\"'][^\"']*?\s+([0-9.]+)\s+([0-9.]+)", text):
            width, height = str(int(float(m.group(1)))), str(int(float(m.group(2))))
    return digest, width, height


def title_and_context(source_paths: str, target: str) -> str:
    for rel in parts(source_paths)[:3]:
        path = ROOT / rel
        if not path.exists() or path.suffix != ".md":
            continue
        text = path.read_text(errors="ignore")
        title = next((clean(line[2:]) for line in text.splitlines() if line.startswith("# ")), path.stem)
        needles = [target, Path(target.split("#", 1)[0]).name]
        idx = next((text.find(n) for n in needles if n and text.find(n) != -1), -1)
        if idx == -1:
            return f"{title}: {clean(text[:500])[:220]}"
        before = text[:idx].splitlines()[-4:]
        after = text[idx:].splitlines()[:5]
        return f"{title}: {clean(' '.join(before + after))[:260]}"
    if source_paths:
        return parts(source_paths)[0]
    return "source context missing"


def drop_reason(row: dict[str, str], path: Path | None, width: str, height: str, context: str = "") -> str:
    hay = " ".join([row.get("target", ""), row.get("description", ""), row.get("alt_texts", ""), row.get("source_paths", ""), context]).lower()
    if row.get("download_error"):
        return "broken download"
    if not path:
        return "no usable local asset"
    if row.get("kind") == "data_uri":
        return "inline map/control artifact"
    if "anthropic-logo" in hay:
        return "repeated brand logo"
    if any(token in hay for token in ["hqdefault", "img.youtube.com", "thumbnail", "livestream", "webinar"]):
        return "youtube thumbnail handled in video catalog"
    if any(token in hay for token in ["cs-logo", "company-logo", "logo", "favicon", "brand-mark", "wordmark"]):
        return "standalone logo or brand mark"
    if "placeholder" in hay:
        return "placeholder asset"
    if any(word in hay for word in ["pegman", "street view", "maps.googleapis.com", "google 이미지"]):
        return "map control or UI chrome"
    if "img.youtube.com/vi//" in hay:
        return "broken youtube thumbnail"
    try:
        w, h = int(float(width or row.get("width") or 0)), int(float(height or row.get("height") or 0))
    except ValueError:
        w = h = 0
    if w and h and (w <= 32 or h <= 32 or w * h <= 2500):
        return "tiny icon or page furniture"
    if re.search(r"\b(badge|favicon|tracking|spinner)\b", hay):
        return "low-value page furniture"
    return ""


def draft_description(row: dict[str, str], context: str) -> str:
    alt = next((p for p in parts(row.get("alt_texts", "")) if p.lower() not in {"image", "img", "logo"}), "")
    current = row.get("description", "")
    if alt:
        return f"{alt}를 보여주는 이미지."
    if current and not any(g in current for g in GENERIC):
        return current
    topic = context.split(":", 1)[0].strip()
    return f"「{topic}」 문맥에서 쓰인 시각 자료."


def source_link(row: dict[str, str]) -> str:
    if urls := parts(row.get("source_urls", "")):
        return f"[원문](<{urls[0]}>)"
    if paths := parts(row.get("source_paths", "")):
        return f"[미러](../../{paths[0]})"
    return ""


def manual_overrides() -> dict[str, dict[str, str]]:
    if not MANUAL.exists():
        return {}
    return {r["key"]: r for r in rows(MANUAL) if r.get("key")}


def copy_asset(src: Path | None, key: str) -> str:
    if not src:
        return ""
    dest = OUT / "assets" / f"{hashlib.sha1(key.encode()).hexdigest()[:12]}-{asset_name(src)}"
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not dest.exists() or dest.stat().st_size != src.stat().st_size:
        shutil.copy2(src, dest)
    return dest.relative_to(ROOT).as_posix()


def make_contact_sheet(data: list[dict[str, str]], limit: int = 60) -> None:
    if not Image or not ImageDraw:
        return
    candidates = [r for r in data if r["decision"] == "keep" and r["reviewed"] != "yes" and r["curated_asset_path"]]
    candidates = candidates[:limit]
    if not candidates:
        return
    thumb_w, thumb_h, label_h, cols = 220, 150, 52, 4
    rows_n = (len(candidates) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * thumb_w, rows_n * (thumb_h + label_h)), "white")
    draw = ImageDraw.Draw(sheet)
    for i, item in enumerate(candidates):
        x, y = (i % cols) * thumb_w, (i // cols) * (thumb_h + label_h)
        path = ROOT / item["curated_asset_path"]
        try:
            with Image.open(path) as im:
                im.thumbnail((thumb_w - 12, thumb_h - 12))
                sheet.paste(im.convert("RGB"), (x + 6, y + 6))
        except Exception:
            draw.rectangle((x + 6, y + 6, x + thumb_w - 6, y + thumb_h - 6), outline="red")
            draw.text((x + 10, y + 30), "unrenderable")
        label = f"{i+1}. {item['key'][:34]}\n{item['source_context'][:70]}"
        draw.text((x + 6, y + thumb_h + 4), label, fill="black")
    out = OUT / "review-sheets" / "candidate-001.jpg"
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out, quality=88)


def build() -> None:
    for generated_dir in [OUT / "assets", OUT / "review-sheets"]:
        if generated_dir.exists():
            shutil.rmtree(generated_dir)

    raw = rows(RAW)
    overrides = manual_overrides()
    out_rows: list[dict[str, str]] = []
    by_hash: dict[str, str] = {}

    for row in raw:
        path = asset_path(row)
        digest, width, height = asset_meta(path)
        context = title_and_context(row.get("source_paths", ""), row.get("target", ""))
        reason = drop_reason(row, path, width, height, context)
        decision = "drop" if reason else "keep"
        canonical = row["key"]
        if decision == "keep" and digest in by_hash:
            decision, canonical, reason = "duplicate", by_hash[digest], "exact duplicate asset"
        elif decision == "keep" and digest:
            by_hash[digest] = row["key"]

        item = dict(row)
        item.update(
            {
                "decision": decision,
                "canonical_key": canonical if decision == "duplicate" else "",
                "curation_reason": reason,
                "source_context": context,
                "visual_note": "draft: visual inspection pending" if decision == "keep" else "",
                "reviewed": "no",
                "context_checked": "auto",
                "asset_sha256": digest,
                "asset_width": width or row.get("width", ""),
                "asset_height": height or row.get("height", ""),
                "curated_description": draft_description(row, context) if decision == "keep" else "",
                "curated_asset_path": "",
            }
        )
        out_rows.append(item)

    by_key = {r["key"]: r for r in out_rows}
    for key, manual in overrides.items():
        if key not in by_key:
            continue
        item = by_key[key]
        for field in ["decision", "canonical_key", "curation_reason", "curated_description", "source_context", "visual_note", "reviewed", "context_checked"]:
            if manual.get(field):
                item[field] = manual[field]

    for item in out_rows:
        if item["decision"] != "duplicate":
            continue
        seen = {item["key"]}
        while True:
            canonical_key = item["canonical_key"]
            canonical_item = by_key.get(canonical_key)
            if (
                not canonical_item
                or canonical_item["decision"] != "duplicate"
                or not canonical_item.get("canonical_key")
                or canonical_key in seen
            ):
                break
            seen.add(canonical_key)
            item["canonical_key"] = canonical_item["canonical_key"]
        canonical_item = by_key.get(item["canonical_key"])
        if canonical_item and canonical_item["decision"] == "drop":
            item["decision"] = "drop"
            item["canonical_key"] = ""
            item["curation_reason"] = canonical_item.get("curation_reason") or "duplicate of dropped low-value asset"

    for item in out_rows:
        if item["decision"] == "keep":
            item["curated_asset_path"] = copy_asset(asset_path(item), item["key"])
        else:
            item["curated_asset_path"] = ""
            item["curated_description"] = ""

    fields = list(raw[0].keys()) + [
        "decision",
        "canonical_key",
        "curation_reason",
        "source_context",
        "visual_note",
        "reviewed",
        "context_checked",
        "asset_sha256",
        "asset_width",
        "asset_height",
        "curated_description",
        "curated_asset_path",
    ]
    write_tsv(OUT / "images.tsv", out_rows, fields)

    reviewed = [r for r in out_rows if r["reviewed"] == "yes"]
    write_tsv(OUT / "semantic-review.tsv", reviewed, fields)

    lines = ["# Curated Lecture Media Images", "", "| Image | 설명 | 맥락 | 출처 |", "|---|---|---|---|"]
    for item in out_rows:
        if item["decision"] != "keep" or not item["curated_asset_path"]:
            continue
        src = item["curated_asset_path"].removeprefix("lecture-media/curated/")
        lines.append(
            f"| <img src=\"{html.escape(src)}\" width=\"180\"> | {html.escape(item['curated_description'])} | {html.escape(item['source_context'][:180])} | {source_link(item)} |"
        )
    (OUT / "images.md").write_text("\n".join(lines) + "\n")
    make_contact_sheet(out_rows)
    print(f"raw={len(raw)} curated_rows={len(out_rows)} keep={sum(r['decision']=='keep' for r in out_rows)} duplicate={sum(r['decision']=='duplicate' for r in out_rows)} drop={sum(r['decision']=='drop' for r in out_rows)} reviewed={len(reviewed)}")


if __name__ == "__main__":
    build()
