import os
from config import DATA_PATH, SUPPORTED_FORMATS


def load_documents():
    documents = []
    doc_id = 0

    # Traverse all files in data folder
    for filename in os.listdir(DATA_PATH):
        file_path = os.path.join(DATA_PATH, filename)

        # Check supported format
        if not any(filename.endswith(ext) for ext in SUPPORTED_FORMATS):
            continue

        # Read file
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read().strip()

                # Skip empty files
                if not content:
                    continue

                # Create structured document
                document = {
                    "id": doc_id,
                    "title": filename,
                    "content": content,
                    "path": file_path
                }

                documents.append(document)
                doc_id += 1

        except Exception as e:
            print(f"Error reading {filename}: {e}")

    return documents