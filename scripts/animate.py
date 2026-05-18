#!/usr/bin/env python3
"""
animate.py — Animated SVG generator for Snow-Excalidraw diagrams.

Generates an animated SVG from a .excalidraw file + optional .animseq.json
using the excalidraw-animate library.

Usage:
    uv run python animate.py /path/to/diagram.excalidraw /path/to/output.animated.svg
    uv run python animate.py /path/to/diagram.excalidraw /path/to/output.animated.svg --animseq /path/to/diagram.animseq.json
"""

import argparse
import gzip
import base64
import json
import subprocess
import sys
import tempfile
from pathlib import Path


def encode_scene(data: dict) -> str:
    raw = json.dumps(data, separators=(",", ":")).encode("utf-8")
    compressed = gzip.compress(raw)
    return base64.urlsafe_b64encode(compressed).decode("ascii")


def render_via_playwright(excalidraw_path: Path, animseq_path: Path | None, output_path: Path) -> bool:
    """Render animated SVG via Playwright using excalidraw-animate hosted service."""
    data = json.loads(excalidraw_path.read_text(encoding="utf-8"))
    payload = {"diagram": data}
    if animseq_path and animseq_path.exists():
        payload["animation"] = json.loads(animseq_path.read_text(encoding="utf-8"))

    encoded = encode_scene(payload)
    animate_url = f"https://excalidraw-animate.vercel.app/#json={encoded}"

    script = f"""
import asyncio
from playwright.async_api import async_playwright

async def render():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={{"width": 1600, "height": 900}})
        await page.goto({json.dumps(animate_url)}, wait_until="networkidle", timeout=30000)
        await page.wait_for_timeout(5000)

        # Try to trigger SVG download button
        try:
            await page.click('button[aria-label="Download SVG"]', timeout=5000)
            await page.wait_for_timeout(2000)
            print("SVG download triggered")
        except Exception:
            print("Could not find download button — check page structure")

        await browser.close()

asyncio.run(render())
"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write(script)
        script_path = f.name

    try:
        result = subprocess.run(
            ["python", script_path],
            capture_output=True, text=True, timeout=60
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False
    finally:
        Path(script_path).unlink(missing_ok=True)


def write_animate_url_file(excalidraw_path: Path, animseq_path: Path | None, output_path: Path) -> None:
    """Write a text file with the animation URL as a fallback."""
    data = json.loads(excalidraw_path.read_text(encoding="utf-8"))
    payload = {"diagram": data}
    if animseq_path and animseq_path.exists():
        payload["animation"] = json.loads(animseq_path.read_text(encoding="utf-8"))
    encoded = encode_scene(payload)
    url = f"https://excalidraw-animate.vercel.app/#json={encoded}"
    
    url_file = output_path.with_suffix(".url.txt")
    url_file.write_text(f"Animation URL:\n{url}\n", encoding="utf-8")
    print(f"Animation URL saved to: {url_file}")
    print(f"Open in browser: {url[:80]}...")


def main() -> None:
    parser = argparse.ArgumentParser(description="Snow-Excalidraw animation renderer")
    parser.add_argument("diagram", help="Path to .excalidraw file")
    parser.add_argument("output", help="Path to output .animated.svg file")
    parser.add_argument("--animseq", help="Path to .animseq.json sequence file", default=None)
    args = parser.parse_args()

    excalidraw_path = Path(args.diagram)
    output_path = Path(args.output)
    animseq_path = Path(args.animseq) if args.animseq else None

    if not excalidraw_path.exists():
        print(f"Error: file not found: {excalidraw_path}", file=sys.stderr)
        sys.exit(1)

    # Auto-detect animseq if not specified
    if not animseq_path:
        auto = excalidraw_path.parent / (excalidraw_path.stem + ".animseq.json")
        if auto.exists():
            animseq_path = auto

    print(f"Generating animation: {excalidraw_path} → {output_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    success = render_via_playwright(excalidraw_path, animseq_path, output_path)
    if success and output_path.exists():
        print(f"Saved: {output_path}")
        sys.exit(0)

    # Fallback: write URL file
    print("Playwright animation render unavailable. Writing URL fallback.")
    write_animate_url_file(excalidraw_path, animseq_path, output_path)
    sys.exit(1)


if __name__ == "__main__":
    main()
