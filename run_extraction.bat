@echo off
echo PDF Text Extraction Script
echo =========================
echo.
echo Installing dependencies...
uv sync
echo.
echo Running text extraction...
uv run python extract_pdf_text.py
echo.
echo Press any key to exit...
pause >nul

