#!/usr/bin/env python3
"""
validate.py — Snow-Excalidraw diagram validator.

Checks a .excalidraw file for structural correctness before delivery.
Exits 0 on success, non-zero on failure (prints all errors).

Usage:
    uv run python validate.py /path/to/diagram.excalidraw
"""

import json
import sys
from pathlib import Path


def validate(path: str) -> list[str]:
    errors: list[str] = []
    file = Path(path)

    if not file.exists():
        return [f"File not found: {path}"]
    if file.suffix != ".excalidraw":
        errors.append(f"Warning: file extension is '{file.suffix}', expected '.excalidraw'")

    try:
        data = json.loads(file.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"JSON parse error: {exc}"]

    # Top-level structure
    if data.get("type") != "excalidraw":
        errors.append(f"Invalid type field: expected 'excalidraw', got '{data.get('type')}'")
    if data.get("version") != 2:
        errors.append(f"Invalid version: expected 2, got {data.get('version')}")

    elements = data.get("elements", [])
    if not isinstance(elements, list):
        errors.append("'elements' field is not a list")
        return errors
    if len(elements) == 0:
        errors.append("'elements' array is empty — diagram has no content")
        return errors

    # Build ID index
    id_set: set[str] = set()
    id_map: dict[str, dict] = {}
    duplicates: list[str] = []
    for el in elements:
        el_id = el.get("id", "")
        if not el_id:
            errors.append(f"Element missing 'id' field: {el.get('type', '?')} at ({el.get('x', '?')},{el.get('y', '?')})")
            continue
        if el_id in id_set:
            duplicates.append(el_id)
        id_set.add(el_id)
        id_map[el_id] = el
    if duplicates:
        errors.append(f"Duplicate element IDs: {', '.join(duplicates)}")

    coords: list[tuple[float, float, str]] = []

    for el in elements:
        el_id = el.get("id", "?")
        el_type = el.get("type", "?")
        x = el.get("x", 0)
        y = el.get("y", 0)

        # isDeleted check
        if el.get("isDeleted", False):
            errors.append(f"Element '{el_id}' ({el_type}) has isDeleted=true — remove it or set to false")

        # Off-canvas check
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            errors.append(f"Element '{el_id}' has non-numeric coordinates: x={x}, y={y}")
        else:
            if x < -200 or x > 3000:
                errors.append(f"Element '{el_id}' ({el_type}) has x={x} — likely off-canvas")
            if y < -200 or y > 3000:
                errors.append(f"Element '{el_id}' ({el_type}) has y={y} — likely off-canvas")
            # Stacking check
            coord_key = (round(x), round(y))
            for cx, cy, cid in coords:
                if abs(cx - x) < 2 and abs(cy - y) < 2:
                    errors.append(f"Elements '{el_id}' and '{cid}' overlap at the same coordinates ({x},{y})")
            coords.append((x, y, el_id))

        # Text element checks
        if el_type == "text":
            text_val = el.get("text", "")
            if not text_val and not el.get("originalText", ""):
                errors.append(f"Text element '{el_id}' has empty text content")
            container_id = el.get("containerId")
            if container_id and container_id not in id_map:
                errors.append(f"Text '{el_id}' has containerId='{container_id}' which does not exist in elements")

        # Bound elements reference check
        bound = el.get("boundElements")
        if bound:
            for b in bound:
                ref_id = b.get("id", "")
                if ref_id and ref_id not in id_map:
                    errors.append(f"Element '{el_id}' boundElements references missing id='{ref_id}'")

        # Arrow binding checks
        if el_type == "arrow":
            start = el.get("startBinding")
            end = el.get("endBinding")
            if start and isinstance(start, dict):
                ref = start.get("elementId", "")
                if ref and ref not in id_map:
                    errors.append(f"Arrow '{el_id}' startBinding.elementId='{ref}' does not exist")
            if end and isinstance(end, dict):
                ref = end.get("elementId", "")
                if ref and ref not in id_map:
                    errors.append(f"Arrow '{el_id}' endBinding.elementId='{ref}' does not exist")
            points = el.get("points", [])
            if len(points) < 2:
                errors.append(f"Arrow '{el_id}' has fewer than 2 points — arrow cannot render")

        # Frame child check
        frame_id = el.get("frameId")
        if frame_id and frame_id not in id_map:
            errors.append(f"Element '{el_id}' has frameId='{frame_id}' which does not exist in elements")

    return errors


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: uv run python validate.py /path/to/diagram.excalidraw")
        sys.exit(1)

    path = sys.argv[1]
    errors = validate(path)

    if errors:
        print(f"\n❌ Validation FAILED — {len(errors)} error(s) found:\n")
        for i, err in enumerate(errors, 1):
            print(f"  {i}. {err}")
        print()
        sys.exit(1)
    else:
        print(f"\n✅ Validation PASSED — {path}\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
