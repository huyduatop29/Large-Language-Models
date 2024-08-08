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


# Load embedding model
model = SentenceTransformer('dangvantuan/vietnamese-embedding')

# Đường dẫn tới thư mục chứa các file dữ liệu
data_folder = 'path_to_data_folder'

# Xử lý và chuyển đổi dữ liệu từ nhiều loại file
for file_name in os.listdir(data_folder):
    file_path = os.path.join(data_folder, file_name)
    try:
        text = process_file(file_path)
        tokenized_text = tokenize(text)  # Tokenize văn bản
        embeddings = model.encode([tokenized_text])  # Sinh ra vector embeddings
        print(f"Embeddings for {file_name}: {embeddings}")
    except Exception as e:
        print(f"Error processing {file_name}: {e}")


from vector_database import VectorDatabase  # Giả sử bạn có một lớp cho vector database

# Khởi tạo vector database
vector_db = VectorDatabase('path_to_vector_database')

# Xử lý và chuyển đổi dữ liệu từ nhiều loại file
for file_name in os.listdir(data_folder):
    file_path = os.path.join(data_folder, file_name)
    try:
        text = process_file(file_path)
        tokenized_text = tokenize(text)  # Tokenize văn bản
        embeddings = model.encode([tokenized_text])  # Sinh ra vector embeddings
        vector_db.add_vector(embeddings[0], {'file_name': file_name, 'text': text})
        print(f"Embeddings for {file_name} stored in database")
    except Exception as e:
        print(f"Error processing {file_name}: {e}")
