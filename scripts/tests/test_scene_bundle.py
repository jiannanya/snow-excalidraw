"""test_scene_bundle.py — Unit tests for scripts/scene_bundle.py."""

import json
import sys
from pathlib import Path

import pytest

# Make the scripts/ directory importable
sys.path.insert(0, str(Path(__file__).parent.parent))
from scene_bundle import (
    encode_bundle,
    decode_bundle,
    bundle_from_files,
    build_local_audit_url,
    build_local_animate_url,
)


class TestEncodeDecode:
    def test_roundtrip_diagram_only(self, minimal_excalidraw):
        encoded = encode_bundle(minimal_excalidraw)
        result = decode_bundle(encoded)
        assert result["diagram"] == minimal_excalidraw
        assert "animation" not in result

    def test_roundtrip_with_animseq(self, minimal_excalidraw, animseq_data):
        encoded = encode_bundle(minimal_excalidraw, animseq_data)
        result = decode_bundle(encoded)
        assert result["diagram"] == minimal_excalidraw
        assert result["animation"] == animseq_data

    def test_encoded_is_str(self, minimal_excalidraw):
        encoded = encode_bundle(minimal_excalidraw)
        assert isinstance(encoded, str)

    def test_encoded_is_url_safe(self, minimal_excalidraw):
        encoded = encode_bundle(minimal_excalidraw)
        # URL-safe base64 must not contain +, /, or =
        assert "+" not in encoded
        assert "/" not in encoded
        assert "=" not in encoded

    def test_decode_handles_missing_padding(self, minimal_excalidraw):
        """decode_bundle must restore dropped base64 padding."""
        encoded = encode_bundle(minimal_excalidraw)
        # Ensure padding is stripped (should already be the case but be explicit)
        stripped = encoded.rstrip("=")
        result = decode_bundle(stripped)
        assert result["diagram"] == minimal_excalidraw

    def test_large_diagram_roundtrip(self):
        """Verify that a large element list survives encode/decode."""
        elements = [
            {"type": "rectangle", "id": f"r{i}", "x": i * 10, "y": 0,
             "width": 100, "height": 50}
            for i in range(200)
        ]
        diagram = {"type": "excalidraw", "version": 2, "elements": elements}
        result = decode_bundle(encode_bundle(diagram))
        assert len(result["diagram"]["elements"]) == 200


class TestBundleFromFiles:
    def test_reads_excalidraw_file(self, excalidraw_file, minimal_excalidraw):
        encoded = bundle_from_files(excalidraw_file)
        result = decode_bundle(encoded)
        assert result["diagram"] == minimal_excalidraw

    def test_auto_discovers_animseq(self, tmp_path, minimal_excalidraw, animseq_data):
        ex_file = tmp_path / "diagram.excalidraw"
        an_file = tmp_path / "diagram.animseq.json"
        ex_file.write_text(json.dumps(minimal_excalidraw), encoding="utf-8")
        an_file.write_text(json.dumps(animseq_data), encoding="utf-8")

        encoded = bundle_from_files(ex_file)
        result = decode_bundle(encoded)
        assert result["animation"] == animseq_data

    def test_explicit_animseq_path(self, tmp_path, minimal_excalidraw, animseq_data):
        ex_file = tmp_path / "diagram.excalidraw"
        an_file = tmp_path / "custom.animseq.json"
        ex_file.write_text(json.dumps(minimal_excalidraw), encoding="utf-8")
        an_file.write_text(json.dumps(animseq_data), encoding="utf-8")

        encoded = bundle_from_files(ex_file, an_file)
        result = decode_bundle(encoded)
        assert result["animation"] == animseq_data


class TestUrlBuilders:
    def test_audit_url_contains_hash(self, excalidraw_file):
        url = build_local_audit_url(excalidraw_file)
        assert "#" in url
        assert "audit.html" in url

    def test_animate_url_contains_hash(self, excalidraw_file):
        url = build_local_animate_url(excalidraw_file)
        assert "#" in url
        assert "animate.html" in url

    def test_audit_url_is_file_scheme(self, excalidraw_file):
        url = build_local_audit_url(excalidraw_file)
        assert url.startswith("file:///")

    def test_urls_differ(self, excalidraw_file):
        audit_url   = build_local_audit_url(excalidraw_file)
        animate_url = build_local_animate_url(excalidraw_file)
        # Both share the same encoded bundle but point to different pages
        assert "audit.html" in audit_url
        assert "animate.html" in animate_url
        # The encoded payloads should be the same
        edit_bundle    = audit_url.split("#", 1)[1]
        animate_bundle = animate_url.split("#", 1)[1]
        assert edit_bundle == animate_bundle
