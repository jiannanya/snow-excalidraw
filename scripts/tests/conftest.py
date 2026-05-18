"""conftest.py — Shared fixtures for Snow-Excalidraw test suite."""

import json
import pytest
from pathlib import Path


@pytest.fixture
def minimal_excalidraw():
    """Return a minimal valid .excalidraw document dict."""
    return {
        "type": "excalidraw",
        "version": 2,
        "source": "https://excalidraw.com",
        "elements": [
            {
                "type": "rectangle",
                "id": "rect-1",
                "x": 80, "y": 120,
                "width": 220, "height": 80,
                "angle": 0,
                "strokeColor": "#1e1e1e",
                "backgroundColor": "transparent",
                "fillStyle": "hachure",
                "strokeWidth": 2,
                "strokeStyle": "solid",
                "roughness": 1,
                "opacity": 100,
                "seed": 10001, "version": 1, "versionNonce": 1,
                "isDeleted": False,
                "groupIds": [], "frameId": None,
                "boundElements": [{"id": "txt-1", "type": "text"}],
                "updated": 1700000000000,
                "link": None, "locked": False, "index": None,
            },
            {
                "type": "text",
                "id": "txt-1",
                "x": 90, "y": 148,
                "width": 200, "height": 24,
                "angle": 0,
                "strokeColor": "#1e1e1e",
                "backgroundColor": "transparent",
                "fillStyle": "solid",
                "strokeWidth": 1,
                "strokeStyle": "solid",
                "roughness": 1,
                "opacity": 100,
                "text": "Hello",
                "originalText": "Hello",
                "fontSize": 16,
                "fontFamily": 1,
                "textAlign": "center",
                "verticalAlign": "middle",
                "containerId": "rect-1",
                "autoResize": True,
                "lineHeight": 1.25,
                "seed": 10002, "version": 1, "versionNonce": 2,
                "isDeleted": False,
                "groupIds": [], "frameId": None,
                "boundElements": None,
                "updated": 1700000000000,
                "link": None, "locked": False, "index": None,
            },
        ],
        "appState": {"viewBackgroundColor": "#ffffff"},
        "files": {},
    }


@pytest.fixture
def excalidraw_file(tmp_path, minimal_excalidraw):
    """Write minimal_excalidraw to a temp .excalidraw file and return the Path."""
    p = tmp_path / "test.excalidraw"
    p.write_text(json.dumps(minimal_excalidraw), encoding="utf-8")
    return p


@pytest.fixture
def animseq_data():
    """Return a minimal animseq dict matching sequence-spec.md format."""
    return {
        "startMs": 400,
        "defaultDuration": 400,
        "elements": [
            {"id": "rect-1", "order": 1, "duration": 300},
            {"id": "txt-1",  "order": 1, "duration": 200},
        ],
    }
