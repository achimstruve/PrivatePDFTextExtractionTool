#!/usr/bin/env python3
"""
PDF Text Extraction Script
Extracts text from scanned PDFs using OCR and saves to markdown format
"""

import os
import sys
from pathlib import Path
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

def extract_text_from_pdf(pdf_path, output_md_path=None):
    """
    Extract text from PDF using OCR for scanned documents
    
    Args:
        pdf_path (str): Path to the PDF file
        output_md_path (str): Path for output markdown file (optional)
    
    Returns:
        str: Path to the created markdown file
    """
    
    # Set output path if not provided
    if output_md_path is None:
        pdf_name = Path(pdf_path).stem
        # Create conversions folder if it doesn't exist
        conversions_dir = Path("conversions")
        conversions_dir.mkdir(exist_ok=True)
        output_md_path = conversions_dir / f"{pdf_name}_extracted.md"
    
    # Check if PDF exists
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    print(f"Processing PDF: {pdf_path}")
    print(f"Output will be saved to: {output_md_path}")
    
    # Open the PDF
    pdf_document = fitz.open(pdf_path)
    extracted_text = []
    
    # Process each page
    for page_num in range(len(pdf_document)):
        print(f"Processing page {page_num + 1}/{len(pdf_document)}...")
        
        page = pdf_document.load_page(page_num)
        
        # Try to extract text directly first (in case it's not scanned)
        text = page.get_text()
        
        # If no text found, use OCR
        if not text.strip():
            print(f"  Page {page_num + 1}: No text found, using OCR...")
            
            # Convert page to image
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # Higher resolution for better OCR
            img_data = pix.tobytes("png")
            img = Image.open(io.BytesIO(img_data))
            
            # Extract text using OCR
            try:
                text = pytesseract.image_to_string(img)
            except Exception as e:
                print(f"  OCR failed for page {page_num + 1}: {e}")
                text = f"[OCR failed for page {page_num + 1}]"
        else:
            print(f"  Page {page_num + 1}: Text extracted directly")
        
        # Add page header and text
        extracted_text.append(f"# Page {page_num + 1}\n\n")
        extracted_text.append(text)
        extracted_text.append("\n\n---\n\n")
    
    pdf_document.close()
    
    # Write to markdown file
    with open(output_md_path, 'w', encoding='utf-8') as md_file:
        md_file.write(f"# Extracted Text from: {os.path.basename(pdf_path)}\n\n")
        md_file.write("".join(extracted_text))
    
    print(f"\nText extraction completed!")
    print(f"Markdown file saved to: {output_md_path}")
    
    return output_md_path

def main():
    """Main function to run the script"""
    
    # Get PDF file path from pdfs folder
    pdf_file = Path("pdfs") / "OVOL Consultancy Agreement Dr Achim Struve  Outlier Ventures contract - signed compressed.pdf"
    
    if not pdf_file.exists():
        print(f"Error: PDF file '{pdf_file}' not found in pdfs folder.")
        print("Please make sure the PDF file is in the pdfs/ directory.")
        sys.exit(1)
    
    try:
        # Extract text
        output_file = extract_text_from_pdf(str(pdf_file))
        print(f"\nSuccess! Text extracted to: {output_file}")
        
    except Exception as e:
        print(f"Error during text extraction: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

