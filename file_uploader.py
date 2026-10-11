import os
import time
import json
from pathlib import Path
from google import genai
from google_ai_key import load_key

load_key()

def upload_course_materials(data_dir: str = "data", file_list: str = "file_list.json"):
    client = genai.Client()
    data_path = Path(data_dir)
    
    if not data_path.exists():
        print(f"Error: Directory '{data_dir}' not found.")
        return -1

    uploaded_files = {}

    print(f"Uploading files from '{data_dir}'.")
    for filepath in data_path.iterdir():
        if filepath.is_file() and filepath.suffix in ['.md', '.pdf', '.txt']:
            print(f"Uploading {filepath.name}")
            
            # Upload to Gemini
            gemini_file = client.files.upload(file=str(filepath))
            
            # Wait for processing to complete
            while gemini_file.state.name == "PROCESSING":
                print(".", end="", flush=True)
                time.sleep(2)
                gemini_file = client.files.get(name=gemini_file.name)
            print("Done.")
            
            # Store the file reference
            uploaded_files[filepath.name] = gemini_file.name

    with open(file_list, "w") as f:
        json.dump(uploaded_files, f, indent=4)
    
    print(f"\nSuccessfully uploaded {len(uploaded_files)} files. List saved as {file_list}.")

if __name__ == "__main__":
    upload_course_materials()
    input("Press any key to exit.\n") 