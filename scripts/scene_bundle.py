#!/usr/bin/env python3
"""
scene_bundle.py — Snow-Excalidraw scene encoding utilities.

Bundles a diagram and optional animation into a compact, URL-safe payload:
    { "diagram": {...excalidraw JSON...}, "animation": {...animseq JSON...} }
Encoding: gzip → URL-safe base64

The encoded string can be appended as a URL fragment to the local viewer pages:
    file:///absolute/path/to/sites/audit.html#<encoded>
    file:///absolute/path/to/sites/animate.html#<encoded>

Public API:
    encode_bundle(diagram, animseq=None) -> str
    decode_bundle(encoded) -> dict
    bundle_from_files(excalidraw_path, animseq_path=None) -> str
    build_local_audit_url(excalidraw_path, animseq_path=None) -> str
    build_local_animate_url(excalidraw_path, animseq_path=None) -> str
"""

import base64
import gzip
import json
from pathlib import Path

_SCRIPT_DIR = Path(__file__).parent
_SKILL_ROOT = _SCRIPT_DIR.parent
_SITES_DIR = _SKILL_ROOT / "sites"


# ─────────────────────────────────────────────
# Core encode / decode
# ─────────────────────────────────────────────

def encode_bundle(diagram_data: dict, animseq_data: dict | None = None) -> str:
    """Compress and base64-encode a diagram (+ optional animseq) into a URL fragment."""
    payload: dict = {"diagram": diagram_data}
    if animseq_data is not None:
        payload["animation"] = animseq_data
    raw = json.dumps(payload, separators=(",", ":")).encode("utf-8")
    compressed = gzip.compress(raw, compresslevel=9)
    return base64.urlsafe_b64encode(compressed).decode("ascii")


def decode_bundle(encoded: str) -> dict:
    """Decode a bundle string back to a dict with 'diagram' and optional 'animation'."""
    # URL-safe base64 may have dropped padding; restore before decoding.
    padding = "=" * (-len(encoded) % 4)
    compressed = base64.urlsafe_b64decode(encoded + padding)
    return json.loads(gzip.decompress(compressed))


# ─────────────────────────────────────────────
# File-based helpers
# ─────────────────────────────────────────────

def bundle_from_files(
    excalidraw_path: Path,
    animseq_path: Path | None = None,
) -> str:
    """Read a .excalidraw file (and optional .animseq.json) and return encoded bundle."""
    excalidraw_path = Path(excalidraw_path)
    diagram_data = json.loads(excalidraw_path.read_text(encoding="utf-8"))

    anim_data: dict | None = None

    # Auto-discover sibling .animseq.json when not explicitly provided
    if animseq_path is None:
        candidate = excalidraw_path.parent / (excalidraw_path.stem + ".animseq.json")
        if candidate.exists():
            animseq_path = candidate

    if animseq_path is not None:
        animseq_path = Path(animseq_path)
        if animseq_path.exists():
            anim_data = json.loads(animseq_path.read_text(encoding="utf-8"))

    return encode_bundle(diagram_data, anim_data)


# ─────────────────────────────────────────────
# URL builders
# ─────────────────────────────────────────────

def build_local_audit_url(
    excalidraw_path: Path,
    animseq_path: Path | None = None,
) -> str:
    """Return a file:// URL that opens the diagram in the local audit viewer."""
    encoded = bundle_from_files(excalidraw_path, animseq_path)
    viewer = (_SITES_DIR / "audit.html").resolve()
    return viewer.as_uri() + "#" + encoded


def build_local_animate_url(
    excalidraw_path: Path,
    animseq_path: Path | None = None,
) -> str:
    """Return a file:// URL that opens the diagram in the local animation viewer."""
    encoded = bundle_from_files(excalidraw_path, animseq_path)
    viewer = (_SITES_DIR / "animate.html").resolve()
    return viewer.as_uri() + "#" + encoded
