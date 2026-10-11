import json
from google import genai
from google.genai import types
from google_ai_key import load_key

load_key()

def math_tutor_agent(question: str, file_list: str = "file_list.json") -> str:
    client = genai.Client()

    try:
        with open(file_list, "r") as f:
            file_registry = json.load(f)
    except FileNotFoundError:
        return "Files not uploaded yet. Run file_uploader.py first."

    # Retrieve the Gemini files using their saved names
    document_list = [client.files.get(name=file_name) for file_name in file_registry.values()]

    prompt = """
    You are a Teaching Assistant for DTU Mathematics 1a course.
    Help students who get stuck on the problem.
    Show the underlying theory from the documents first, then solve the problem using ONLY material from the notes.
    """
    # Pass the documents and the question to the model
    response = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=document_list + [question],
        config=types.GenerateContentConfig(
            system_instruction=prompt,
            temperature=0.2, # the lover number to get more "objective" answears
        )

    )
    
    return response.text

if __name__ == "__main__":
    print("RAG supported AI agent:")
    print("Type 'EXIT' to quit the chat.")
    while True:
        query = input().strip()
        if query == "EXIT":
            break
        print(math_tutor_agent(query))
    
    input("Press any key to exit.\n")  # Stop unvanted closage of the window upon quitting the loop