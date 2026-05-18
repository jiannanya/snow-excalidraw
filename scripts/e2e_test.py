#!/usr/bin/env python3
"""
e2e_test.py - End-to-end browser validation for standalone launcher HTML.

Checks that a launcher page renders successfully:
- overlay disappears
- a canvas element is mounted
- reports browser console/runtime errors

Usage:
    python e2e_test.py /path/to/launch-audit.html
    python e2e_test.py /path/to/diagram-preview.html
"""

import argparse
import sys
from pathlib import Path


def run_e2e_test(html_path: Path) -> bool:
    try:
        from playwright.sync_api import sync_playwright  # type: ignore
    except ImportError:
        print(
            "Warning: playwright not installed; skip e2e browser check.\n"
            "Install with: uv pip install playwright && uv run playwright install chromium"
        )
        return True

    url = html_path.as_uri()
    print(f"E2E test : {url}")

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page()

        runtime_errors: list[str] = []
        page.on("pageerror", lambda exc: runtime_errors.append(str(exc)))

        def on_console(msg):
            if msg.type == "error":
                runtime_errors.append(f"[console.error] {msg.text}")

        page.on("console", on_console)
        page.goto(url)

        try:
            page.wait_for_selector("#overlay", state="detached", timeout=30000)
            print("OK: overlay removed")
        except Exception:
            overlay = page.query_selector("#overlay")
            txt = overlay.inner_text() if overlay else "(overlay not found)"
            print(f"FAIL: overlay still visible: {txt[:300]}", file=sys.stderr)
            browser.close()
            return False

        canvas = page.query_selector("canvas")
        if not canvas:
            print("FAIL: no canvas element mounted", file=sys.stderr)
            browser.close()
            return False

        print("OK: canvas mounted")
        if runtime_errors:
            print("Warnings from browser runtime:")
            for err in runtime_errors:
                print(f"  {err}")

        browser.close()

    print("E2E passed")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Snow-Excalidraw e2e browser validation")
    parser.add_argument("path", help="Path to launcher html file")
    args = parser.parse_args()

    html_path = Path(args.path)
    if not html_path.exists():
        print(f"Error: file not found: {html_path}", file=sys.stderr)
        sys.exit(1)

    ok = run_e2e_test(html_path)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
