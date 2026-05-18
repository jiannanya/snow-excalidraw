#!/usr/bin/env python3
"""
open.py — Snow-Excalidraw diagram launcher and exporter.

Encodes diagrams via scene_bundle.py and opens them in the local sites/ viewers.
Handles edit, animate, save-excalidraw, save-animation, save-image, open-image modes.

Usage:
    uv run python open.py /path/to/diagram.excalidraw --mode edit
    uv run python open.py /path/to/diagram.excalidraw --mode animate
    uv run python open.py /path/to/diagram.excalidraw --mode save-excalidraw --dest /project/dir
    uv run python open.py /path/to/diagram.excalidraw --mode save-image --dest /project/dir
    uv run python open.py /path/to/diagram.excalidraw --mode open-image --dest /project/dir
    uv run python open.py /path/to/diagram.excalidraw --mode save-animation --dest /project/dir
"""

import argparse
import json
import os
import platform
import shutil
import subprocess
import sys
import webbrowser
from pathlib import Path

# scene_bundle lives in the same directory
sys.path.insert(0, str(Path(__file__).parent))
from scene_bundle import build_local_audit_url, build_local_animate_url


def load_diagram(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_launcher(url: str, launcher_path: Path, title: str) -> None:
    """Write a tiny HTML redirect page that bounces to the target viewer URL."""
    escaped = json.dumps(url)
    html = (
        "<!DOCTYPE html>\n"
        "<html><head><meta charset='utf-8'>\n"
        f"<title>{title}</title>\n"
        f"<script>window.location.replace({escaped});</script>\n"
        "</head><body>\n"
        f"<p>Redirecting… <a href='{url}'>click here if not redirected</a></p>\n"
        "</body></html>\n"
    )
    launcher_path.write_text(html, encoding="utf-8")


def open_in_browser(path: Path) -> None:
    url = path.as_uri()
    webbrowser.open(url)
    print(f"Opened: {url}")


def open_with_system(path: Path) -> None:
    system = platform.system()
    if system == "Windows":
        os.startfile(str(path))
    elif system == "Darwin":
        subprocess.run(["open", str(path)])
    else:
        subprocess.run(["xdg-open", str(path)])
    print(f"Opened: {path}")


def render_png(excalidraw_path: Path, dest: Path) -> Path | None:
    """Render PNG via render.py (Playwright)."""
    png_path = dest / (excalidraw_path.stem + ".png")
    render_script = Path(__file__).parent / "render.py"
    if render_script.exists():
        result = subprocess.run(
            ["uv", "run", "python", str(render_script), str(excalidraw_path), str(png_path)],
            capture_output=True, text=True,
        )
        if result.returncode == 0 and png_path.exists():
            return png_path
    print("Warning: render.py unavailable or rendering failed.")
    print("Open the edit URL in a browser and use File → Export Image.")
    return None


def render_animation(excalidraw_path: Path, animseq_path: Path | None, dest: Path) -> Path | None:
    """Render animated SVG via animate.py."""
    svg_path = dest / (excalidraw_path.stem + ".animated.svg")
    animate_script = Path(__file__).parent / "animate.py"
    if animate_script.exists():
        args = ["uv", "run", "python", str(animate_script), str(excalidraw_path), str(svg_path)]
        if animseq_path and animseq_path.exists():
            args += ["--animseq", str(animseq_path)]
        result = subprocess.run(args, capture_output=True, text=True)
        if result.returncode == 0 and svg_path.exists():
            return svg_path
    print("Warning: animate.py unavailable or rendering failed.")
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description="Snow-Excalidraw diagram launcher")
    parser.add_argument("diagram", help="Path to .excalidraw file")
    parser.add_argument(
        "--mode",
        choices=["edit", "animate", "save-excalidraw", "save-image", "open-image", "save-animation"],
        default="edit",
        help="Delivery mode",
    )
    parser.add_argument("--dest", help="Destination directory for save modes")
    args = parser.parse_args()

    diagram_path = Path(args.diagram)
    if not diagram_path.exists():
        print(f"Error: file not found: {diagram_path}", file=sys.stderr)
        sys.exit(1)

    diagram_dir = diagram_path.parent
    animseq_path: Path | None = diagram_dir / (diagram_path.stem + ".animseq.json")
    if not animseq_path.exists():
        animseq_path = None

    dest_dir = Path(args.dest) if args.dest else diagram_dir
    dest_dir.mkdir(parents=True, exist_ok=True)

    mode = args.mode

    if mode == "edit":
        url = build_local_audit_url(diagram_path, animseq_path)
        launcher = diagram_dir / "launch-edit.html"
        write_launcher(url, launcher, "Snow-Excalidraw — Edit Diagram")
        print(f"Launcher : {launcher}")
        print(f"Viewer   : {url[:80]}…")
        open_in_browser(launcher)

    elif mode == "animate":
        url = build_local_animate_url(diagram_path, animseq_path)
        launcher = diagram_dir / "launch-animate.html"
        write_launcher(url, launcher, "Snow-Excalidraw — Animated Diagram")
        print(f"Launcher : {launcher}")
        open_in_browser(launcher)

    elif mode == "save-excalidraw":
        dest_excalidraw = dest_dir / diagram_path.name
        shutil.copy2(diagram_path, dest_excalidraw)
        print(f"Saved: {dest_excalidraw}")
        if animseq_path:
            dest_anim = dest_dir / animseq_path.name
            shutil.copy2(animseq_path, dest_anim)
            print(f"Saved: {dest_anim}")

    elif mode == "save-image":
        result = render_png(diagram_path, dest_dir)
        if result:
            print(f"Saved: {result}")
        else:
            url = build_local_audit_url(diagram_path, animseq_path)
            launcher = diagram_dir / "launch-edit.html"
            write_launcher(url, launcher, "Snow-Excalidraw — Export Image")
            print(f"PNG unavailable. Open editor to export: {launcher}")
            open_in_browser(launcher)

    elif mode == "open-image":
        result = render_png(diagram_path, dest_dir)
        if result:
            print(f"Saved: {result}")
            open_with_system(result)
        else:
            url = build_local_audit_url(diagram_path, animseq_path)
            launcher = diagram_dir / "launch-edit.html"
            write_launcher(url, launcher, "Snow-Excalidraw — Export Image")
            print(f"PNG unavailable. Open editor to export: {launcher}")
            open_in_browser(launcher)

    elif mode == "save-animation":
        result = render_animation(diagram_path, animseq_path, dest_dir)
        if result:
            print(f"Saved: {result}")
        else:
            url = build_local_animate_url(diagram_path, animseq_path)
            launcher = diagram_dir / "launch-animate.html"
            write_launcher(url, launcher, "Snow-Excalidraw — Animated Diagram")
            print(f"Animation unavailable. View at: {launcher}")
            open_in_browser(launcher)


if __name__ == "__main__":
    main()
