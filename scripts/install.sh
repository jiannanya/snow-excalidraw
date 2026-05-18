#!/usr/bin/env bash
# Snow-Excalidraw — Unix/macOS install script
# Installs Python dependencies and Playwright Chromium browser.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPTS_DIR="$SCRIPT_DIR/scripts"

echo ""
echo "================================================"
echo " Snow-Excalidraw — dependency installer (Unix)"
echo "================================================"
echo ""

# ── 1. Check Python 3.11+ ───────────────────────────────────────────────────
if ! command -v python3 &>/dev/null; then
    echo "[ERROR] python3 not found. Install Python 3.11+ and re-run."
    exit 1
fi

PY_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo "[INFO] Python version: $PY_VERSION"

# ── 2. Check / install uv ───────────────────────────────────────────────────
if ! command -v uv &>/dev/null; then
    echo "[INFO] uv not found — installing via pip..."
    pip3 install uv
fi

# ── 3. Install Python packages ──────────────────────────────────────────────
echo "[1/3] Installing Python packages via uv..."
cd "$SCRIPTS_DIR"
uv pip install -r pyproject.toml

# ── 4. Install Playwright Chromium ──────────────────────────────────────────
echo "[2/3] Installing Playwright Chromium browser..."
if uv run playwright install chromium; then
    echo "      Chromium installed."
else
    echo "[WARNING] Playwright browser install failed."
    echo "          Run manually: uv run playwright install chromium"
fi

# ── 5. Verify ───────────────────────────────────────────────────────────────
echo "[3/3] Verifying installation..."
if uv run python -c "import playwright; print('playwright ok')"; then
    echo "      playwright import successful."
else
    echo "[WARNING] Playwright import check failed."
fi

echo ""
echo "================================================"
echo " Installation complete."
echo " Usage:  uv run python open.py diagram.excalidraw --mode edit"
echo "================================================"
echo ""
