#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import html
import re
import shutil
import subprocess
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import unquote, unquote_to_bytes, urlparse

try:
    from PIL import Image
except Exception:  # pragma: no cover - optional local helper
    Image = None


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "lecture-media"
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}
SKIP_DIRS = {".git", ".claude", "_yt-cache", "lecture-media", "__pycache__"}
HTML_IMG_RE = re.compile(r"<img\b[^>]*>", re.I)
ATTR_RE = re.compile(r"([\w:-]+)\s*=\s*(\"[^\"]*\"|'[^']*'|[^\s>]+)")
SOURCE_RE = re.compile(r"<!--\s*source:\s*([^>]+?)\s*-->")
TITLE_RE = re.compile(r"^#\s+(.+)$", re.M)
DATA_RE = re.compile(r"^data:image/([a-zA-Z0-9.+-]+)(;base64)?,(.*)$", re.S)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def skipped(path: Path) -> bool:
    try:
        parts = path.relative_to(ROOT).parts
    except ValueError:
        parts = path.parts
    return any(part in SKIP_DIRS for part in parts)


def safe_name(value: str) -> str:
    value = unquote(value).split("?")[0].split("#")[0]
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-._")
    return value[:120] or "asset"


def sha_bytes(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()


def clean(value: str) -> str:
    value = html.unescape(value or "")
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def file_meta(path: Path) -> dict[str, str]:
    try:
        text = path.read_text(errors="ignore")
    except Exception:
        text = ""
    source = ""
    if m := SOURCE_RE.search(text[:500]):
        source = clean(m.group(1))
    title = ""
    if m := TITLE_RE.search(text):
        title = clean(m.group(1).strip("# "))
    return {"source_url": source, "title": title}


def markdown_images(text: str) -> list[tuple[str, str]]:
    refs: list[tuple[str, str]] = []
    i = 0
    while True:
        start = text.find("![", i)
        if start == -1:
            break
        alt_end = text.find("]", start + 2)
        if alt_end == -1 or alt_end + 1 >= len(text) or text[alt_end + 1] != "(":
            i = start + 2
            continue
        depth = 0
        dest = []
        j = alt_end + 2
        while j < len(text):
            char = text[j]
            if char == "\\" and j + 1 < len(text):
                dest.append(text[j + 1])
                j += 2
                continue
            if char == "(":
                depth += 1
            elif char == ")":
                if depth == 0:
                    break
                depth -= 1
            dest.append(char)
            j += 1
        raw = "".join(dest).strip()
        target = raw[1 : raw.find(">")] if raw.startswith("<") and ">" in raw else raw.split()[0] if raw else ""
        if target:
            refs.append((clean(text[start + 2 : alt_end]), target))
        i = j + 1
    for tag in HTML_IMG_RE.findall(text):
        attrs = {}
        for key, value in ATTR_RE.findall(tag):
            attrs[key.lower()] = value.strip("\"'")
        if attrs.get("src"):
            refs.append((clean(attrs.get("alt", "")), attrs["src"]))
    return refs


def row(rows: dict[str, dict], key: str, kind: str, target: str) -> dict:
    if key not in rows:
        rows[key] = {
            "key": key,
            "kind": kind,
            "target": target,
            "asset_path": "",
            "preview": "",
            "description": "",
            "topic_hints": "",
            "source_paths": [],
            "source_urls": [],
            "alt_texts": [],
            "occurrences": 0,
            "width": "",
            "height": "",
            "download_error": "",
        }
    rows[key]["occurrences"] += 1
    return rows[key]


def add_unique(values: list[str], value: str) -> None:
    if value and value not in values:
        values.append(value)


def local_asset(path: Path, subdir: str = "local") -> tuple[str, str, str]:
    data = path.read_bytes()
    digest = sha_bytes(data)[:12]
    dest = OUT / "assets" / subdir / f"{digest}-{safe_name(path.name)}"
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not dest.exists() or dest.stat().st_size != len(data):
        shutil.copy2(path, dest)
    width = height = ""
    if Image and path.suffix.lower() != ".svg":
        try:
            with Image.open(path) as im:
                width, height = map(str, im.size)
        except Exception:
            pass
    return rel(dest), width, height


def data_asset(target: str) -> tuple[str, str, str]:
    match = DATA_RE.match(target)
    if not match:
        return "", "", ""
    kind = match.group(1).lower()
    ext = "jpg" if kind == "jpeg" else "svg" if kind == "svg+xml" else kind.split("+", 1)[0]
    data = base64.b64decode(match.group(3), validate=False) if match.group(2) else unquote_to_bytes(match.group(3))
    digest = sha_bytes(data)[:12]
    dest = OUT / "assets" / "data" / f"{digest}.{ext}"
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not dest.exists():
        dest.write_bytes(data)
    width = height = ""
    if Image:
        try:
            with Image.open(dest) as im:
                width, height = map(str, im.size)
        except Exception:
            pass
    return rel(dest), width, height


def remote_asset(url: str) -> tuple[str, str]:
    parsed = urlparse(url)
    suffix = Path(unquote(parsed.path)).suffix.lower()
    ext = suffix if suffix in IMAGE_EXTS else ".img"
    name = safe_name(Path(parsed.path).name or parsed.netloc) + ext
    dest = OUT / "assets" / "remote" / safe_name(parsed.netloc) / f"{sha_bytes(url.encode())[:12]}-{name}"
    if dest.exists() and dest.stat().st_size:
        return rel(dest), ""
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 lecture-media-catalog"})
    try:
        with urllib.request.urlopen(req, timeout=20) as res:
            data = res.read()
        if not data:
            return "", "empty response"
        tmp = dest.with_suffix(dest.suffix + ".tmp")
        tmp.write_bytes(data)
        tmp.replace(dest)
        return rel(dest), ""
    except Exception as exc:
        return "", str(exc).replace("\t", " ")[:200]


def download_remote_assets(rows: dict[str, dict], workers: int = 10) -> None:
    items = [item for item in rows.values() if item["kind"] == "remote_ref"]
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(remote_asset, item["target"]): item for item in items}
        for future in as_completed(futures):
            item = futures[future]
            asset_path, error = future.result()
            if asset_path:
                item["asset_path"] = asset_path
                item["preview"] = asset_path
            elif error:
                item["download_error"] = error


def resolve_ref(source: Path, target: str) -> Path | None:
    if target.startswith(("http://", "https://", "data:")):
        return None
    clean_target = unquote(target.split("#", 1)[0].split("?", 1)[0])
    return (source.parent / clean_target).resolve()


def slug_words(value: str) -> str:
    parsed = urlparse(value)
    name = Path(unquote(parsed.path)).stem if parsed.scheme else Path(value).stem
    name = re.sub(r"^[0-9a-f]{8,}[-_]*", "", name, flags=re.I)
    name = re.sub(r"[-_]+", " ", name).strip()
    return clean(name)


def topic_hints(text: str) -> str:
    hay = text.lower()
    pairs = [
        ("prompt", "prompting"),
        ("agent", "agents"),
        ("mcp", "MCP"),
        ("model context protocol", "MCP"),
        ("claude code", "Claude Code"),
        ("interpret", "interpretability"),
        ("alignment", "alignment"),
        ("safety", "AI safety"),
        ("jailbreak", "AI safety"),
        ("tool", "tool use"),
        ("skill", "skills"),
        ("education", "education"),
        ("health", "healthcare"),
        ("finance", "financial services"),
        ("enterprise", "enterprise AI"),
        ("computer use", "computer use"),
        ("model", "models"),
    ]
    found = [label for needle, label in pairs if needle in hay]
    return ", ".join(dict.fromkeys(found))


def describe_image(item: dict, titles: dict[str, str]) -> str:
    alt = next((a for a in item["alt_texts"] if a.lower() not in {"image", "img", "thumbnail"}), "")
    source_title = next((titles.get(p, "") for p in item["source_paths"] if titles.get(p, "")), "")
    target_words = slug_words(item["target"])
    hay = " ".join([alt, source_title, target_words, item["target"], item["kind"]]).lower()

    if "placeholder" in hay:
        return "페이지에 포함된 자리표시자 이미지."
    if alt:
        if "headshot" in alt.lower():
            return f"{alt.replace('headshot', '').strip()} 인물 사진."
        if alt.lower() == "logo" or " logo" in alt.lower():
            return f"{source_title or target_words or '관련'} 로고 이미지."
        return f"{alt} 이미지."
    if "img.youtube.com/vi/" in item["target"]:
        return f"「{source_title or target_words or 'YouTube 영상'}」 썸네일 이미지."
    if item["kind"].startswith("pdf"):
        page = item["target"].split("#page=", 1)[-1] if "#page=" in item["target"] else ""
        return f"PDF 「{source_title or target_words or Path(item['target']).name}」 {page}쪽에서 추출한 이미지."
    if "transformer-circuits.pub" in " ".join(item["source_paths"] + [item["target"]]):
        return f"「{source_title or target_words or 'Transformer Circuits'}」 글에 포함된 해석가능성 도식/시각화."
    if source_title:
        return f"「{source_title}」 문서에 포함된 이미지."
    if target_words:
        return f"{target_words} 관련 이미지."
    return "Anthropic/Claude 미러 문서에 포함된 이미지."


def pdf_rows(rows: dict[str, dict], extract: bool) -> None:
    if not shutil.which("pdfimages"):
        return
    for pdf in sorted(p for p in ROOT.rglob("*.pdf") if not skipped(p)):
        pdf_rel = rel(pdf)
        out_dir = OUT / "assets" / "pdf" / f"{safe_name(pdf.stem)}-{sha_bytes(pdf_rel.encode())[:10]}"
        try:
            listed = subprocess.run(
                ["pdfimages", "-list", str(pdf)],
                cwd=ROOT,
                text=True,
                capture_output=True,
                timeout=60,
                check=False,
            ).stdout.splitlines()[2:]
        except Exception:
            listed = []
        if extract and listed:
            out_dir.mkdir(parents=True, exist_ok=True)
            done = out_dir / ".done"
            if not done.exists():
                for old in out_dir.glob("img-*"):
                    old.unlink()
                subprocess.run(["pdfimages", "-png", str(pdf), str(out_dir / "img")], cwd=ROOT, check=False, timeout=300)
                done.write_text(pdf_rel + "\n")
        extracted = sorted(p for p in out_dir.glob("img-*") if p.is_file()) if out_dir.exists() else []
        for idx, line in enumerate(l for l in listed if l.strip()):
            parts = line.split()
            page = parts[0] if parts else "?"
            width = parts[3] if len(parts) > 3 else ""
            height = parts[4] if len(parts) > 4 else ""
            item = row(rows, f"pdf:{pdf_rel}:{idx}", "pdf_image", f"{pdf_rel}#page={page}#image={idx}")
            add_unique(item["source_paths"], pdf_rel)
            item["width"], item["height"] = width, height
            if idx < len(extracted):
                item["asset_path"] = rel(extracted[idx])
                item["preview"] = item["asset_path"]


def collect_images(extract_pdf: bool, download_remote: bool = False) -> dict[str, dict]:
    rows: dict[str, dict] = {}
    for image in sorted(p for p in ROOT.rglob("*") if p.is_file() and p.suffix.lower() in IMAGE_EXTS and not skipped(p)):
        image_rel = rel(image)
        item = row(rows, f"local:{image_rel}", "local_file", image_rel)
        add_unique(item["source_paths"], image_rel)
        item["asset_path"], item["width"], item["height"] = local_asset(image)
        item["preview"] = item["asset_path"]

    md_files = sorted(p for p in ROOT.rglob("*.md") if p.is_file() and not skipped(p))
    meta = {rel(p): file_meta(p) for p in md_files}
    for md in md_files:
        md_rel = rel(md)
        try:
            refs = markdown_images(md.read_text(errors="ignore"))
        except Exception:
            refs = []
        for alt, target in refs:
            resolved = resolve_ref(md, target)
            if target.startswith(("http://", "https://")):
                key, kind, display = f"remote:{target.split('#', 1)[0]}", "remote_ref", target.split("#", 1)[0]
            elif target.startswith("data:"):
                key, kind, display = f"data:{sha_bytes(target.encode())[:16]}", "data_uri", "data:image"
            elif resolved and resolved.exists() and resolved.is_relative_to(ROOT):
                display = rel(resolved)
                key, kind = f"local:{display}", "local_file"
            else:
                key, kind, display = f"missing:{md_rel}:{target}", "missing_local_ref", target
            item = row(rows, key, kind, display)
            add_unique(item["source_paths"], md_rel)
            add_unique(item["source_urls"], meta[md_rel]["source_url"])
            add_unique(item["alt_texts"], alt)
            if kind == "local_file" and resolved and resolved.exists():
                item["asset_path"], item["width"], item["height"] = local_asset(resolved)
                item["preview"] = item["asset_path"]
            elif kind == "data_uri" and not item["asset_path"]:
                item["asset_path"], item["width"], item["height"] = data_asset(target)
                item["preview"] = item["asset_path"]
            elif kind == "remote_ref":
                item["preview"] = display

    pdf_rows(rows, extract_pdf)
    if download_remote:
        download_remote_assets(rows)
    titles = {path: info["title"] for path, info in meta.items()}
    for item in rows.values():
        item["description"] = describe_image(item, titles)
        item["topic_hints"] = topic_hints(" ".join([item["target"], item["description"], *item["source_paths"]]))
        if not item["preview"]:
            item["preview"] = item["asset_path"] or item["target"]
    return dict(sorted(rows.items()))


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    data = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"')
    return data


def duration_seconds(value: str) -> int | None:
    if not value:
        return None
    try:
        total = 0
        for part in value.split(":"):
            total = total * 60 + int(part)
        return total
    except ValueError:
        return None


def video_topic(title: str) -> str:
    lower = title.lower()
    if "trailer" in lower or "conclusion" in lower:
        return ""
    if "ai fluency" in lower or lower.startswith("lesson "):
        return "AI Fluency"
    if "sycophancy" in lower or "reward hacking" in lower:
        return "모델 행동"
    if "interpretability" in lower:
        return "해석가능성"
    if "model context protocol" in lower or lower == "mcp in claude code":
        return "MCP"
    if "prompting tips" in lower or lower.startswith("prompting 101") or lower == "your first claude code prompt":
        return "프롬프트"
    if lower in {"tips for building ai agents", "building more effective ai agents", "claude agent skills explained", "what is claude managed agents?"}:
        return "에이전트"
    if "tool use with" in lower or lower.startswith("claude | computer use"):
        return "도구 사용"
    if lower.startswith("getting started with "):
        return "Claude 시작하기"
    if lower == "what is claude code?":
        return "Claude Code"
    if lower == "keep thinking with claude":
        return "확장 사고"
    return ""


def concept_score(title: str) -> int:
    topic = video_topic(title)
    if topic == "AI Fluency":
        return 3
    if topic in {"MCP", "프롬프트", "에이전트", "모델 행동", "해석가능성"}:
        return 2
    return 1 if topic else 0


def keep_video(title: str, meta: dict[str, str]) -> bool:
    if not video_topic(title):
        return False
    if meta.get("captions") == "none":
        return False
    seconds = duration_seconds(meta.get("duration", ""))
    return seconds is not None and seconds <= 20 * 60


def describe_video(title: str) -> str:
    lower = title.lower()
    if "sycophancy" in lower:
        return "AI 모델이 사용자 의견에 과하게 맞장구치는 현상을 설명하는 영상."
    if "reward hacking" in lower:
        return "모델이 보상 신호를 우회해 목표를 잘못 최적화하는 문제를 설명하는 영상."
    if "mcp" in lower or "model context protocol" in lower:
        return "MCP로 모델과 도구/데이터를 연결하는 개념을 소개하는 영상."
    if "prompt" in lower:
        return "프롬프트 작성과 개선의 기본 원리를 설명하는 영상."
    if "claude code" in lower:
        return "Claude Code의 기본 사용 흐름을 짧게 소개하는 영상."
    if lower.startswith("claude | computer use for automating operations"):
        return "Claude의 computer use가 업무 도구를 조작해 운영 작업을 자동화하는 예시 영상."
    if lower.startswith("claude | computer use for coding"):
        return "Claude의 computer use가 개발 환경을 조작해 코딩 작업을 돕는 예시 영상."
    if lower.startswith("claude | computer use for orchestrating tasks"):
        return "Claude의 computer use가 여러 단계의 화면 작업을 이어서 수행하는 예시 영상."
    if "agent" in lower:
        return "AI 에이전트가 작업을 계획하고 도구를 쓰는 방식을 설명하는 영상."
    if "interpretability" in lower or "thought" in lower:
        return "모델 내부 작동과 해석가능성 개념을 설명하는 영상."
    if "ai fluency" in lower or "lesson" in lower:
        return "AI Fluency 수업에 바로 끼워 넣기 좋은 기초 개념 강의 영상."
    if "getting started" in lower:
        return "Claude 기능을 처음 소개할 때 쓰기 좋은 짧은 공식 튜토리얼."
    if "keep thinking" in lower:
        return "Claude의 확장 사고 흐름을 짧게 보여주는 공식 영상."
    if "tool use" in lower:
        return "Claude의 도구 사용/function calling 개념을 짧게 설명하는 영상."
    return f"「{title}」 개념을 강의에서 짧게 소개할 때 쓰기 좋은 공식 영상."


def collect_youtube() -> list[dict[str, str]]:
    rows = []
    for path in sorted((ROOT / "youtube.com").glob("*/*.md")):
        if skipped(path):
            continue
        text = path.read_text(errors="ignore")
        meta = parse_frontmatter(text)
        title = meta.get("title") or clean(TITLE_RE.search(text).group(1) if TITLE_RE.search(text) else path.stem)
        score = concept_score(title)
        if score <= 0 or not keep_video(title, meta):
            continue
        rows.append(
            {
                "path": rel(path),
                "title": title,
                "topic": video_topic(title),
                "channel": meta.get("channel", ""),
                "published": meta.get("published", ""),
                "duration": meta.get("duration", ""),
                "captions": meta.get("captions", ""),
                "url": meta.get("url", ""),
                "youtube_id": meta.get("youtube_id", ""),
                "score": str(score),
                "description": describe_video(title),
            }
        )
    return sorted(rows, key=lambda r: (-int(r["score"]), r["published"], r["title"]))


def write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore", dialect="excel-tab")
        writer.writeheader()
        writer.writerows(rows)


def media_src(item: dict) -> str:
    src = item["preview"]
    if src.startswith("lecture-media/"):
        return src.removeprefix("lecture-media/")
    if src.startswith(("http://", "https://", "data:")):
        return src
    return "../" + src


def write_images(rows: dict[str, dict]) -> None:
    fields = [
        "key",
        "kind",
        "target",
        "asset_path",
        "preview",
        "description",
        "topic_hints",
        "source_paths",
        "source_urls",
        "alt_texts",
        "occurrences",
        "width",
        "height",
        "download_error",
    ]
    flat = []
    for item in rows.values():
        flat.append({k: " | ".join(map(str, item[k])) if isinstance(item.get(k), list) else item.get(k, "") for k in fields})
    write_tsv(OUT / "images.tsv", flat, fields)

    lines = [
        "# Lecture Media Image Catalog",
        "",
        f"총 {len(flat)}개 이미지 항목. 로컬 파일, Markdown 이미지 참조, data URI, PDF 내부 이미지 객체를 합친 목록입니다.",
        "",
        "| Image | 설명 | 출처 | 유형 | 힌트 |",
        "|---|---|---|---|---|",
    ]
    for item in rows.values():
        source = item["source_paths"][0] if item["source_paths"] else ""
        source_link = f"[{html.escape(source)}](../{source})" if source else ""
        img = f'<img src="{html.escape(media_src(item), quote=True)}" width="160">'
        lines.append(
            "| "
            + " | ".join(
                [
                    img,
                    html.escape(item["description"]).replace("|", "\\|"),
                    source_link,
                    item["kind"],
                    html.escape(item["topic_hints"]).replace("|", "\\|"),
                ]
            )
            + " |"
        )
    (OUT / "images.md").write_text("\n".join(lines) + "\n")


def write_youtube(rows: list[dict[str, str]]) -> None:
    fields = ["title", "topic", "description", "channel", "published", "duration", "captions", "url", "path", "youtube_id", "score"]
    write_tsv(OUT / "youtube.tsv", rows, fields)
    lines = [
        "# Lecture Concept YouTube Catalog",
        "",
        f"공식 Anthropic/Claude 미러에서 고른 간단 개념 설명 후보 {len(rows)}개입니다.",
        "",
        "| 영상 | 주제 | 설명 | 길이 | 날짜 | 자막 |",
        "|---|---|---|---|---|---|",
    ]
    for item in rows:
        title = html.escape(item["title"]).replace("|", "\\|")
        link = f"[{title}](../{item['path']})"
        lines.append(f"| {link} | {item['topic']} | {item['description']} | {item['duration']} | {item['published']} | {item['captions'] or '-'} |")
    (OUT / "youtube.md").write_text("\n".join(lines) + "\n")


def build(args: argparse.Namespace) -> int:
    rows = collect_images(extract_pdf=not args.no_extract_pdf, download_remote=args.download_remote)
    videos = collect_youtube()
    write_images(rows)
    write_youtube(videos)
    print(f"images={len(rows)} youtube={len(videos)} out={rel(OUT)}")
    return 0


def check() -> int:
    required = [OUT / "images.tsv", OUT / "images.md", OUT / "youtube.tsv", OUT / "youtube.md"]
    missing = [rel(p) for p in required if not p.exists()]
    if missing:
        print("missing: " + ", ".join(missing), file=sys.stderr)
        return 1
    expected = collect_images(extract_pdf=False)
    with (OUT / "images.tsv").open(newline="") as f:
        actual = list(csv.DictReader(f, dialect="excel-tab"))
    actual_keys = {r["key"] for r in actual}
    missing_keys = sorted(set(expected) - actual_keys)
    bad_rows = [r["key"] for r in actual if not r.get("description") or not r.get("source_paths")]
    with (OUT / "youtube.tsv").open(newline="") as f:
        videos = list(csv.DictReader(f, dialect="excel-tab"))
    bad_videos = [r.get("title", "") for r in videos if not r.get("description") or not r.get("url") or not (ROOT / r.get("path", "")).exists()]
    if missing_keys or bad_rows or bad_videos or not videos:
        print(f"missing_image_rows={len(missing_keys)} bad_image_rows={len(bad_rows)} bad_videos={len(bad_videos)} videos={len(videos)}", file=sys.stderr)
        return 1
    print(f"check ok: images={len(actual)} expected={len(expected)} youtube={len(videos)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="verify generated catalog coverage")
    parser.add_argument("--no-extract-pdf", action="store_true", help="list PDF image objects without extracting image files")
    parser.add_argument("--download-remote", action="store_true", help="download remote Markdown image URLs into lecture-media/assets/remote")
    args = parser.parse_args()
    if args.check:
        return check()
    return build(args)


if __name__ == "__main__":
    raise SystemExit(main())
