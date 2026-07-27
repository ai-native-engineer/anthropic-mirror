#!/usr/bin/env python3
"""Add an invisible OCR text layer to mirrored PDFs in place."""

from __future__ import annotations

import argparse
import os
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path


EXCLUDED_PARTS = {".agents", ".claude", ".git", "_yt-cache"}
OCR_MARKER = "anthropic-mirror-ocr-v1"


def ensure_runtime() -> None:
    try:
        import pikepdf  # noqa: F401
        return
    except ImportError:
        pass
    if os.environ.get("ANTHROPIC_MIRROR_OCR_REEXEC"):
        raise RuntimeError("ocrmypdf Python environment is missing pikepdf")
    executable = shutil.which("ocrmypdf")
    python = Path(executable).resolve().parent / "python" if executable else None
    if not python or not python.is_file():
        raise RuntimeError("ocrmypdf with the Apple OCR plugin is required")
    env = os.environ.copy()
    env["ANTHROPIC_MIRROR_OCR_REEXEC"] = "1"
    os.execve(python, [str(python), str(Path(__file__).resolve()), *sys.argv[1:]], env)


def discover(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.pdf")
        if path.is_file()
        and not any(part in EXCLUDED_PARTS for part in path.relative_to(root).parts)
    )


def is_current(path: Path) -> bool:
    import pikepdf

    try:
        with pikepdf.open(path) as pdf:
            return str(pdf.docinfo.get("/AnthropicMirrorOCR", "")) == OCR_MARKER
    except pikepdf.PdfError:
        return False


def add_text_layer(path: Path) -> None:
    import pikepdf

    mode = stat.S_IMODE(path.stat().st_mode)
    fd, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".pdf", dir=path.parent)
    os.close(fd)
    temporary = Path(temporary_name)
    try:
        subprocess.run(
            [
                "ocrmypdf",
                "--plugin",
                "ocrmypdf_appleocr",
                "--redo-ocr",
                "--appleocr-recognition-mode",
                "accurate",
                "--output-type",
                "pdf",
                "--optimize",
                "0",
                "--tagged-pdf-mode",
                "ignore",
                "--invalidate-digital-signatures",
                "--quiet",
                str(path),
                str(temporary),
            ],
            check=True,
        )
        with pikepdf.open(temporary, allow_overwriting_input=True) as pdf:
            pdf.docinfo["/AnthropicMirrorOCR"] = OCR_MARKER
            pdf.save(temporary)
        os.chmod(temporary, mode)
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def check(root: Path, pdfs: list[Path]) -> int:
    stale = [path.relative_to(root).as_posix() for path in pdfs if not is_current(path)]
    print(f"PDF OCR coverage: {len(pdfs) - len(stale)}/{len(pdfs)} current")
    for relative in stale[:20]:
        print(f"  missing text layer: {relative}")
    return 1 if stale else 0


def self_test() -> None:
    from PIL import Image, ImageDraw, ImageFont

    with tempfile.TemporaryDirectory(prefix="anthropic-pdf-ocr-test-") as directory:
        root = Path(directory)
        image = root / "sample.png"
        pdf = root / "sample.pdf"
        canvas = Image.new("RGB", (1000, 240), "white")
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 96)
        ImageDraw.Draw(canvas).text((40, 50), "HELLO OCR 2026", fill="black", font=font)
        canvas.save(image, dpi=(144, 144))
        subprocess.run(
            [
                "ocrmypdf",
                "--plugin",
                "ocrmypdf_appleocr",
                "--image-dpi",
                "144",
                "--output-type",
                "pdf",
                "--optimize",
                "0",
                "--quiet",
                str(image),
                str(pdf),
            ],
            check=True,
        )
        add_text_layer(pdf)
        text = subprocess.run(
            ["pdftotext", str(pdf), "-"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout
        assert "HELLO" in text and "2026" in text, text
        assert is_current(pdf)
    print("self-test ok")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--asset", action="append", default=[], help="process one repo-relative PDF")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    ensure_runtime()
    if args.self_test:
        self_test()
        return 0

    root = Path(args.root).resolve()
    pdfs = [root / path for path in args.asset] if args.asset else discover(root)
    if any(path.suffix.lower() != ".pdf" for path in pdfs):
        raise RuntimeError("bitmap images cannot contain a selectable text layer; use a PDF container")
    if args.check:
        return check(root, pdfs)

    written = skipped = failed = 0
    for index, path in enumerate(pdfs, 1):
        relative = path.relative_to(root).as_posix()
        if not args.force and is_current(path):
            skipped += 1
            continue
        try:
            add_text_layer(path)
            written += 1
            print(f"[{index}/{len(pdfs)}] {relative}", flush=True)
        except Exception as error:
            failed += 1
            print(f"ERROR {relative}: {error}", file=sys.stderr, flush=True)
    print(f"PDF text layers: {written} written, {skipped} current, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
