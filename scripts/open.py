#!/usr/bin/env python3
"""
open.py — Snow-Excalidraw diagram launcher and exporter.

Generates hosted Excalidraw URLs and opens diagrams in various modes.
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
import gzip
import json
import os
import platform
import shutil
import subprocess
import sys
import tempfile
import webbrowser
from pathlib import Path
from urllib.parse import quote


EXCALIDRAW_EDIT_URL = "https://excalidraw.com/#json="
EXCALIDRAW_ANIMATE_URL = "https://excalidraw-animate.vercel.app/#json="


def encode_scene(data: dict) -> str:
    """Encode an Excalidraw scene dict to a URL-safe base64 gzip string."""
    import base64
    raw = json.dumps(data, separators=(",", ":")).encode("utf-8")
    compressed = gzip.compress(raw)
    b64 = base64.urlsafe_b64encode(compressed).decode("ascii")
    return b64


def load_diagram(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def get_edit_url(data: dict) -> str:
    encoded = encode_scene(data)
    return f"{EXCALIDRAW_EDIT_URL}{encoded}"


def get_animate_url(data: dict, animseq_path: Path | None) -> str:
    payload = {"diagram": data}
    if animseq_path and animseq_path.exists():
        anim_data = json.loads(animseq_path.read_text(encoding="utf-8"))
        payload["animation"] = anim_data
    encoded = encode_scene(payload)
    return f"{EXCALIDRAW_ANIMATE_URL}{encoded}"


def write_launcher(url: str, launcher_path: Path, title: str) -> None:
    html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{title}</title>
  <script>window.location.replace({json.dumps(url)});</script>
</head>
<body>
  <p>Redirecting to diagram... <a href="{url}">Click here if not redirected</a></p>
</body>
</html>
"""
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
    """Attempt to render PNG using available renderers."""
    png_path = dest / (excalidraw_path.stem + ".png")
    
    # Try Chrome DevTools MCP approach via node script
    render_script = Path(__file__).parent / "render.py"
    if render_script.exists():
        result = subprocess.run(
            ["uv", "run", "python", str(render_script), str(excalidraw_path), str(png_path)],
            capture_output=True, text=True
        )
        if result.returncode == 0 and png_path.exists():
            return png_path
    
    print("Warning: render.py not available or rendering failed.")
    print(f"To render PNG manually, open the edit URL in a browser and use File → Export Image.")
    return None


def render_animation(excalidraw_path: Path, animseq_path: Path | None, dest: Path) -> Path | None:
    """Attempt to render animated SVG."""
    svg_path = dest / (excalidraw_path.stem + ".animated.svg")
    
    animate_script = Path(__file__).parent / "animate.py"
    if animate_script.exists():
        args = ["uv", "run", "python", str(animate_script), str(excalidraw_path), str(svg_path)]
        if animseq_path and animseq_path.exists():
            args += ["--animseq", str(animseq_path)]
        result = subprocess.run(args, capture_output=True, text=True)
        if result.returncode == 0 and svg_path.exists():
            return svg_path
    
    print("Warning: animate.py not available or rendering failed.")
    print("To render animation, open the animate URL in a browser.")
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
    animseq_path = diagram_dir / (diagram_path.stem + ".animseq.json")
    if not animseq_path.exists():
        animseq_path = None

    dest_dir = Path(args.dest) if args.dest else diagram_dir
    dest_dir.mkdir(parents=True, exist_ok=True)

    data = load_diagram(diagram_path)
    mode = args.mode

    if mode == "edit":
        url = get_edit_url(data)
        launcher = diagram_dir / "launch-edit.html"
        write_launcher(url, launcher, "Excalidraw — Edit Diagram")
        print(f"Launcher: {launcher}")
        open_in_browser(launcher)

    elif mode == "animate":
        url = get_animate_url(data, animseq_path)
        launcher = diagram_dir / "launch-animate.html"
        write_launcher(url, launcher, "Excalidraw — Animated Diagram")
        print(f"Launcher: {launcher}")
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
            # Fallback: open edit URL so user can export manually
            url = get_edit_url(data)
            launcher = diagram_dir / "launch-edit.html"
            write_launcher(url, launcher, "Excalidraw — Export Image")
            print(f"PNG render unavailable. Open in editor to export: {launcher}")
            open_in_browser(launcher)

    elif mode == "open-image":
        result = render_png(diagram_path, dest_dir)
        if result:
            print(f"Saved: {result}")
            open_with_system(result)
        else:
            url = get_edit_url(data)
            launcher = diagram_dir / "launch-edit.html"
            write_launcher(url, launcher, "Excalidraw — Export Image")
            print(f"PNG render unavailable. Open in editor to export: {launcher}")
            open_in_browser(launcher)

    elif mode == "save-animation":
        result = render_animation(diagram_path, animseq_path, dest_dir)
        if result:
            print(f"Saved: {result}")
        else:
            url = get_animate_url(data, animseq_path)
            launcher = diagram_dir / "launch-animate.html"
            write_launcher(url, launcher, "Excalidraw — Animated Diagram")
            print(f"Animation render unavailable. View animation at: {launcher}")
            open_in_browser(launcher)


if __name__ == "__main__":
    main()
