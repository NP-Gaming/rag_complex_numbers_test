# Mathematics RAG AI tutor

## Overview
This application was created to familiarize myself with the RAG (Retrieval-Augmented Generation) concept and its practical implementation. I used the topic of complex numbers as it is one of my favorites to work with. 
The project acts as a proof-of-concept. It is built on the Google GenAI SDK and the AI Studio File Search API (documentation available [here](https://aistudio.google.com/docs/file-search)).

## Features
- **Data Injection (`file_uploader.py`):** Automatically uploads Markdown/PDF/Text files (i.e. notes) to Google AI Studio and saves a local file registry.
- **Curriculum Guardrails (`rag.py`):** Strict prompt engineering ensures the AI tutor only uses course-approved notation and theorems (e.g., using the Identity Theorem instead of advanced complex logarithms).
- **Quarto-rendered demo (`demo.qmd`):** shows a static HTML demonstrating the AI's output with parsed LaTeX formatting.

## Prerequisites
- Python 3.9+
- Google Gemini API Key
- [Quarto CLI](https://quarto.org/docs/get-started/) (Only for rendering `demo.qmd`)

## Dependencies
Install the required external packages using pip:
```bash
pip install google-genai python-dotenv
```

## Usage:
1. Upload your files into the `/data` folder, or use the provided example `01_complex_numbers.md`.
2. Run python `file_uploader.py` to upload the documents. On the first run, the program will ask for your Google AI API key.
3. Run python `rag.py` to launch the interactive AI tutor in your terminal.
4. Optionally, run `quarto render demo.qmd` to render the demo file, which can also be seen pre-rendered in `demo.html`.