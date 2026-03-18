import os
import fitz # PyMuPDF
import re

def is_transaction(line):
    return bool(re.search(r"\d{2}/\d{2}", line) and re.search(r"-?\d+\.\d{2}", line))

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        text += page.get_text()

    return text


if __name__ == "__main__":
    pdf_rel_path = "ML/training_assets/wisely/2025-07_eStmt_7487.pdf"
    text = extract_text(pdf_path=pdf_rel_path)

    print(text)
    print("hello world")