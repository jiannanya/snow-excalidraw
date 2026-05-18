@echo off
REM Snow-Excalidraw — Windows install script
REM Installs Python dependencies and Playwright Chromium browser.

SETLOCAL
SET SCRIPT_DIR=%~dp0
SET SCRIPTS_DIR=%SCRIPT_DIR%scripts

echo.
echo ================================================
echo  Snow-Excalidraw — dependency installer (Windows)
echo ================================================
echo.

REM Check Python 3.11+
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python is not found in PATH.
    echo         Install Python 3.11+ from https://python.org and re-run.
    exit /b 1
)

REM Check uv
uv --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [INFO] uv not found — installing via pip...
    pip install uv
    IF %ERRORLEVEL% NEQ 0 (
        echo [ERROR] Failed to install uv.
        exit /b 1
    )
)

echo [1/3] Installing Python packages via uv...
cd "%SCRIPTS_DIR%"
uv pip install -r pyproject.toml
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] uv pip install failed.
    exit /b 1
)

echo [2/3] Installing Playwright browsers...
uv run playwright install chromium
IF %ERRORLEVEL% NEQ 0 (
    echo [WARNING] Playwright browser install failed.
    echo           Run manually: uv run playwright install chromium
)

echo [3/3] Verifying installation...
uv run python -c "import playwright; print('playwright ok')"
IF %ERRORLEVEL% NEQ 0 (
    echo [WARNING] Playwright Python package check failed.
)

echo.
echo ================================================
echo  Installation complete.
echo  Usage:  uv run python open.py diagram.excalidraw --mode audit
echo ================================================
echo.

ENDLOCAL
