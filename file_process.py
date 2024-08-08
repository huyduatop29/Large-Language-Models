import os
import fitz  # PyMuPDF để xử lý file .pdf
import docx  # python-docx để xử lý file .docx
from sentence_transformers import SentenceTransformer
from pyvi.ViTokenizer import tokenize

# Hàm đọc file .txt
def read_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Hàm đọc file .pdf
def read_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Hàm đọc file .docx
def read_docx(file_path):
    doc = docx.Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

# Hàm xử lý các loại file
def process_file(file_path):
    if file_path.endswith('.txt'):
        return read_txt(file_path)
    elif file_path.endswith('.pdf'):
        return read_pdf(file_path)
    elif file_path.endswith('.docx'):
        return read_docx(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_path}")
