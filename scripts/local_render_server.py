#!/usr/bin/env python3
"""
local_render_server.py — Minimal HTTP server for Snow-Excalidraw Playwright rendering.

Serves the sites/ directory on a random localhost port so that Playwright can load
sites/audit.html without file:// CORS restrictions.

Usage (as a context manager):
    from local_render_server import RenderServer

    with RenderServer() as srv:
        url = srv.edit_url(encoded_bundle)
        # use url with Playwright
"""

import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os
import socket


_SITES_DIR = Path(__file__).parent.parent / "sites"


class _QuietHandler(SimpleHTTPRequestHandler):
    """SimpleHTTPRequestHandler with logging suppressed."""

    def log_message(self, format, *args) -> None:  # noqa: A002
        pass  # silence access logs during rendering


class RenderServer:
    """Context manager that serves sites/ on an ephemeral localhost port."""

    def __init__(self, sites_dir: Path = _SITES_DIR) -> None:
        self.sites_dir = sites_dir.resolve()
        self._server: HTTPServer | None = None
        self._thread: threading.Thread | None = None
        self.port: int = 0

    # ── lifecycle ──────────────────────────────────────────────────────────────

    def start(self) -> "RenderServer":
        """Start the server and return self."""
        # Find a free port
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("127.0.0.1", 0))
            self.port = s.getsockname()[1]

        # HTTPServer needs the working directory set to serve files
        original_dir = os.getcwd()
        os.chdir(str(self.sites_dir))

        handler = _QuietHandler
        self._server = HTTPServer(("127.0.0.1", self.port), handler)

        self._thread = threading.Thread(
            target=self._server.serve_forever, daemon=True
        )
        self._thread.start()

        os.chdir(original_dir)
        return self

    def stop(self) -> None:
        if self._server is not None:
            self._server.shutdown()
            self._server = None

    def __enter__(self) -> "RenderServer":
        return self.start()

    def __exit__(self, *_args) -> None:
        self.stop()

    # ── URL builders ──────────────────────────────────────────────────────────

    def edit_url(self, encoded_bundle: str) -> str:
        return f"http://127.0.0.1:{self.port}/audit.html#{encoded_bundle}"

    def animate_url(self, encoded_bundle: str) -> str:
        return f"http://127.0.0.1:{self.port}/animate.html#{encoded_bundle}"
