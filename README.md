# PDF Text Extraction Script

This Python script extracts text from scanned PDFs using OCR (Optical Character Recognition) and saves the extracted text to a markdown file.

## Project Structure

```
ImageTextExtraction/
├── pdfs/                    # Place your PDF files here
├── conversions/             # Extracted markdown files are saved here
├── extract_pdf_text.py      # Main extraction script
├── run_extraction.bat       # Windows batch file to run the script
├── pyproject.toml           # Project configuration and dependencies
└── README.md               # This file
```

## Features

- Extracts text from both regular PDFs and scanned PDFs
- Uses OCR when direct text extraction fails
- Saves output in markdown format with page separators
- Handles multiple pages automatically
- Organized folder structure for PDFs and conversions

## Prerequisites

### 1. Install uv (Python Package Manager)

**Windows:**
```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Alternative (using pip):**
```bash
pip install uv
```

### 2. Install Tesseract OCR

**Windows:**
- Download and install Tesseract from: https://github.com/UB-Mannheim/tesseract/wiki
- Add Tesseract to your system PATH
- Default installation path: `C:\Program Files\Tesseract-OCR\tesseract.exe`

### 3. Install Python Dependencies

```bash
uv sync
```

## Usage

1. Place your PDF file in the `pdfs/` folder
2. Install dependencies:
   ```bash
   uv sync
   ```
3. Run the script:
   ```bash
   uv run python extract_pdf_text.py
   ```

   **Or use the Windows batch file:**
   ```bash
   run_extraction.bat
   ```

The script will:
- Look for PDFs in the `pdfs/` folder
- Process each page of the PDF
- Extract text directly if possible
- Use OCR for scanned pages if needed
- Save the extracted text to a markdown file in the `conversions/` folder

## Output

The script creates a markdown file in the `conversions/` folder with:
- Page headers for each page
- Extracted text content
- Page separators
- Original filename reference

## Troubleshooting

- **OCR not working**: Make sure Tesseract is installed and in your PATH
- **Missing dependencies**: Run `uv sync`
- **File not found**: Ensure the PDF file is in the `pdfs/` folder

## Dependencies

- `PyMuPDF`: PDF processing
- `pytesseract`: OCR text extraction
- `Pillow`: Image processing

## Virtual Environment

`uv` automatically creates and manages a virtual environment for your project. You can:

- **Activate the environment**: `uv shell`
- **Run commands in the environment**: `uv run <command>`
- **Install additional packages**: `uv add <package-name>`
- **Remove packages**: `uv remove <package-name>`
