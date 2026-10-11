import os
from dotenv import load_dotenv

def load_key(print_key=False):
    """Loads google AI key, if keyfile missing, request Google AI Studio API key"""
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key and print_key:
          print(api_key)
    if not api_key:
        key = input(
"""Google AI Studio API key not found.
Please provide the keyfile, avaiable for free at: https://aistudio.google.com/api-keys
"""
            )
        with open(".env", "w") as file:
                    file.write(f"GEMINI_API_KEY={key}\n")
                    print(f"Saved {key} in the .env file.")
    
        os.environ["GEMINI_API_KEY"] = key #reload the key after inputting the new one

if __name__ == "__main__":
    load_key(print_key=True)
    input("Press any key to exit.\n") 