#!/usr/bin/env python3
"""
render.py — PNG renderer for Snow-Excalidraw diagrams.

Loads the diagram in a headless Chromium browser via the local sites/audit.html
viewer (served by local_render_server.py) and screenshots the Excalidraw canvas.

Requirements:
    uv pip install playwright
    playwright install chromium

Usage:
    uv run python render.py /path/to/diagram.excalidraw /path/to/output.png
    uv run python render.py /path/to/diagram.excalidraw /path/to/output.png --timeout 45
"""

import argparse
import asyncio
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from scene_bundle import bundle_from_files
from local_render_server import RenderServer

# Selector that becomes visible once Excalidraw has mounted and painted its canvas
_CANVAS_SELECTOR = ".excalidraw canvas"
# Extra settle time (ms) after the canvas appears — lets fonts and shapes finish rendering
_SETTLE_MS = 2500


async def _render_async(excalidraw_path: Path, output_path: Path, timeout_s: int) -> bool:
    from playwright.async_api import async_playwright

    encoded = bundle_from_files(excalidraw_path)

    with RenderServer() as srv:
        url = srv.edit_url(encoded)

        async with async_playwright() as pw:
            browser = await pw.chromium.launch(args=["--no-sandbox"])
            page = await browser.new_page(viewport={"width": 1800, "height": 1000})

            try:
                await page.goto(url, wait_until="domcontentloaded",
                                timeout=timeout_s * 1000)
                # Wait for the canvas element — indicates Excalidraw has mounted
                await page.wait_for_selector(_CANVAS_SELECTOR,
                                             timeout=timeout_s * 1000)
                await page.wait_for_timeout(_SETTLE_MS)

                # Attempt to export via Excalidraw's own exportToSvg JS API; fall
                # back to a full-page screenshot if the API is unavailable.
                canvas = await page.query_selector(_CANVAS_SELECTOR)
                if canvas:
                    await canvas.screenshot(path=str(output_path))
                else:
                    await page.screenshot(path=str(output_path), full_page=False)

                print(f"Rendered : {output_path}")
                return True

            except Exception as exc:
                print(f"Playwright render error: {exc}", file=sys.stderr)
                return False
            finally:
                await browser.close()


def render(excalidraw_path: Path, output_path: Path, timeout_s: int = 40) -> bool:
    return asyncio.run(_render_async(excalidraw_path, output_path, timeout_s))


def main() -> None:
    parser = argparse.ArgumentParser(description="Snow-Excalidraw PNG renderer")
    parser.add_argument("diagram", help="Path to .excalidraw file")
    parser.add_argument("output",  help="Output PNG path")
    parser.add_argument("--timeout", type=int, default=40,
                        help="Timeout in seconds (default: 40)")
    args = parser.parse_args()

    ok = render(Path(args.diagram), Path(args.output), timeout_s=args.timeout)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
