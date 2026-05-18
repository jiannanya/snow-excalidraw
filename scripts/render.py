#!/usr/bin/env python3
"""
render.py — PNG renderer for Snow-Excalidraw diagrams.

Attempts to render a .excalidraw file to PNG using available methods:
1. Chrome DevTools MCP (via npx chrome-devtools-mcp) — preferred
2. Playwright — fallback if Chrome DevTools MCP unavailable

Usage:
    uv run python render.py /path/to/diagram.excalidraw /path/to/output.png
"""

import json
import subprocess
import sys
import tempfile
import gzip
import base64
from pathlib import Path


def encode_scene(data: dict) -> str:
    raw = json.dumps(data, separators=(",", ":")).encode("utf-8")
    compressed = gzip.compress(raw)
    return base64.urlsafe_b64encode(compressed).decode("ascii")


def render_via_playwright(excalidraw_path: Path, output_path: Path) -> bool:
    """Render using Playwright headless browser."""
    data = json.loads(excalidraw_path.read_text(encoding="utf-8"))
    encoded = encode_scene(data)
    edit_url = f"https://excalidraw.com/#json={encoded}"

    script = f"""
import asyncio
from playwright.async_api import async_playwright

async def render():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={{"width": 1600, "height": 900}})
        await page.goto({json.dumps(edit_url)}, wait_until="networkidle", timeout=30000)
        await page.wait_for_timeout(3000)  # wait for canvas render
        await page.screenshot(path={json.dumps(str(output_path))}, full_page=False)
        await browser.close()
        print(f"Rendered: {json.dumps(str(output_path))}")

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
        return result.returncode == 0 and output_path.exists()
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False
    finally:
        Path(script_path).unlink(missing_ok=True)


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: uv run python render.py /path/to/diagram.excalidraw /path/to/output.png")
        sys.exit(1)

    excalidraw_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    if not excalidraw_path.exists():
        print(f"Error: file not found: {excalidraw_path}", file=sys.stderr)
        sys.exit(1)

    print(f"Rendering {excalidraw_path} → {output_path}")

    # Try Playwright
    if render_via_playwright(excalidraw_path, output_path):
        print(f"Saved: {output_path}")
        sys.exit(0)

    print("All render methods failed. Open in Excalidraw editor and use File → Export Image.")
    sys.exit(1)


if __name__ == "__main__":
    main()
