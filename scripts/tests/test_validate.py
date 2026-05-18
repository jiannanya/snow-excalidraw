"""test_validate.py — Unit tests for scripts/validate.py."""

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
from validate import validate, check_text_overflow, _estimate_text_px_width


# ─────────────────────────────────────────────
# _estimate_text_px_width
# ─────────────────────────────────────────────

class TestEstimateTextWidth:
    def test_empty_string(self):
        assert _estimate_text_px_width("", 16) == 0.0

    def test_single_line(self):
        # "Hello" = 5 chars, font 16 → 5 * 16 * 0.55 = 44.0
        result = _estimate_text_px_width("Hello", 16)
        assert abs(result - 44.0) < 0.01

    def test_multi_line_uses_longest(self):
        # Lines: "Hi" (2) and "Hello World" (11) → 11 * 16 * 0.55 = 96.8
        result = _estimate_text_px_width("Hi\nHello World", 16)
        assert abs(result - 96.8) < 0.01

    def test_larger_font(self):
        result = _estimate_text_px_width("ABCDE", 24)
        assert abs(result - 5 * 24 * 0.55) < 0.01


# ─────────────────────────────────────────────
# check_text_overflow
# ─────────────────────────────────────────────

class TestCheckTextOverflow:
    def _make_elements(self, container_width, text, font_size=16):
        container = {
            "type": "rectangle", "id": "c1",
            "x": 80, "y": 120, "width": container_width, "height": 80,
            "isDeleted": False,
        }
        text_el = {
            "type": "text", "id": "t1",
            "x": 80, "y": 130, "width": container_width - 20, "height": 24,
            "text": text, "fontSize": font_size,
            "containerId": "c1", "isDeleted": False,
        }
        id_map = {"c1": container, "t1": text_el}
        return [container, text_el], id_map

    def test_no_overflow(self):
        elements, id_map = self._make_elements(300, "Short label")
        warnings = check_text_overflow(elements, id_map)
        assert warnings == []

    def test_overflow_detected(self):
        # Container 100px wide, 20px padding → 80px available
        # Text "This is a very long label" at font 16 = 25 * 16 * 0.55 = 220px
        elements, id_map = self._make_elements(100, "This is a very long label", font_size=16)
        warnings = check_text_overflow(elements, id_map)
        assert len(warnings) == 1
        assert "t1" in warnings[0]
        assert "c1" in warnings[0]

    def test_no_container(self):
        """Free-floating text (containerId=None) should not be checked."""
        text_el = {
            "type": "text", "id": "free",
            "x": 80, "y": 80, "width": 200, "height": 24,
            "text": "A free label",
            "fontSize": 16, "containerId": None,
        }
        warnings = check_text_overflow([text_el], {"free": text_el})
        assert warnings == []

    def test_missing_container_id_skipped(self):
        """Text whose containerId is not in id_map should be silently skipped."""
        text_el = {
            "type": "text", "id": "t1",
            "x": 80, "y": 80, "width": 200, "height": 24,
            "text": "Some text", "fontSize": 16,
            "containerId": "does-not-exist",
        }
        warnings = check_text_overflow([text_el], {"t1": text_el})
        assert warnings == []


# ─────────────────────────────────────────────
# validate (integration)
# ─────────────────────────────────────────────

class TestValidate:
    def test_valid_file(self, excalidraw_file):
        errors = validate(str(excalidraw_file))
        assert errors == []

    def test_missing_file(self, tmp_path):
        errors = validate(str(tmp_path / "does-not-exist.excalidraw"))
        assert any("not found" in e for e in errors)

    def test_duplicate_ids(self, tmp_path, minimal_excalidraw):
        """Duplicate element IDs should be reported."""
        doc = dict(minimal_excalidraw)
        doc["elements"] = [doc["elements"][0], doc["elements"][0]]
        p = tmp_path / "dup.excalidraw"
        p.write_text(json.dumps(doc), encoding="utf-8")
        errors = validate(str(p))
        assert any("Duplicate" in e for e in errors)

    def test_missing_binding_target(self, tmp_path, minimal_excalidraw):
        """Arrow binding to a non-existent element should be reported."""
        doc = dict(minimal_excalidraw)
        arrow = {
            "type": "arrow", "id": "arr-1",
            "x": 300, "y": 160,
            "width": 100, "height": 0,
            "points": [[0, 0], [100, 0]],
            "strokeColor": "#1e1e1e",
            "startBinding": {"elementId": "ghost-id", "gap": 5, "focus": 0},
            "endBinding": None,
            "isDeleted": False, "groupIds": [], "frameId": None,
            "boundElements": None, "updated": 1700000000000,
            "seed": 9999, "version": 1, "versionNonce": 9999,
            "link": None, "locked": False, "index": None,
        }
        doc["elements"] = doc["elements"] + [arrow]
        p = tmp_path / "bad.excalidraw"
        p.write_text(json.dumps(doc), encoding="utf-8")
        errors = validate(str(p))
        assert any("ghost-id" in e for e in errors)

    def test_empty_elements(self, tmp_path):
        doc = {"type": "excalidraw", "version": 2, "elements": [], "appState": {}}
        p = tmp_path / "empty.excalidraw"
        p.write_text(json.dumps(doc), encoding="utf-8")
        errors = validate(str(p))
        assert any("empty" in e for e in errors)
