# Installation Guide

## Requirements

| Requirement | Minimum version | Notes |
|-------------|----------------|-------|
| Python | 3.11 | For `|` union type hints and `tomllib` |
| uv | latest | Fast Python package manager |
| Chromium | via Playwright | For headless PNG rendering |

---

## Quick Install

### Windows

```cmd
scripts\install.cmd
```

### macOS / Linux

```bash
chmod +x scripts/install.sh
scripts/install.sh
```

---

## Manual Installation

If the scripts above don't work, follow these steps:

### 1. Install uv

```bash
pip install uv
```

Or via the official installer (recommended):

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows PowerShell
irm https://astral.sh/uv/install.ps1 | iex
```

### 2. Install Python packages

```bash
cd snow-excalidraw/scripts
uv pip install -r pyproject.toml
```

To also install test dependencies:

```bash
uv pip install -r pyproject.toml --extra dev
```

### 3. Install Playwright Chromium

```bash
uv run playwright install chromium
```

On Linux you may also need system dependencies:

```bash
uv run playwright install-deps chromium
```

### 4. Verify

```bash
uv run python -c "from playwright.async_api import async_playwright; print('OK')"
```

---

## Running the Scripts

All scripts are in `scripts/` and invoked via `uv run`:

| Command | Description |
|---------|-------------|
| `uv run python open.py diagram.excalidraw --mode audit` | Open in local browser editor |
| `uv run python open.py diagram.excalidraw --mode animate` | Open animation player |
| `uv run python open.py diagram.excalidraw --mode save-image --dest ./out` | Render PNG to `./out/` |
| `uv run python open.py diagram.excalidraw --mode save-animation --dest ./out` | Save animated SVG |
| `uv run python validate.py diagram.excalidraw` | Validate diagram JSON |
| `uv run python render.py diagram.excalidraw output.png` | Render PNG directly |
| `uv run python e2e_test.py launch-audit.html` | Browser e2e validation of launcher page |

### Running tests

```bash
cd scripts
uv run pytest tests/ -v
```

---

## Viewer Pages (sites/)

The `sites/` directory contains self-contained HTML pages. They load Excalidraw from the `jsDelivr` CDN, so **an internet connection is required** for the first render.

| Page | Description |
|------|-------------|
| `sites/index.html` | Landing page |
| `sites/audit.html` | Full Excalidraw editor |
| `sites/animate.html` | Step-by-step animation player |

Open `sites/index.html` directly in a browser to explore the viewer pages.

---

## Troubleshooting

**`ModuleNotFoundError: playwright`**  
Run `uv pip install playwright` then `uv run playwright install chromium`.

**`DecompressionStream is not defined`** in browser  
Your browser doesn't support the native DecompressionStream API. Update to Chrome 109+, Firefox 113+, or Safari 16.4+.

**Excalidraw CDN fails to load in `audit.html`**  
Check your internet connection. If esm.sh is blocked, download the `.excalidraw` file via the fallback button and drag it to [excalidraw.com](https://excalidraw.com).

**PNG render timeout**  
Increase the timeout: `uv run python render.py diagram.excalidraw output.png --timeout 60`
