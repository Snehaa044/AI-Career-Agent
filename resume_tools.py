import fitz  # PyMuPDF
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

# Configure API key from environment
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def extract_resume_text(file_path):
    """Extract text from a PDF resume."""
    pdf = fitz.open(file_path)
    text = ""
    for page in pdf:
        text += page.get_text()
    return text


def analyze_resume(resume_text):
    """Analyze resume with Gemini."""

    # Use a currently available model
    model = genai.GenerativeModel("models/gemini-2.5-flash")

    prompt = f"""
    Analyze this resume and provide:
    1. A short professional summary
    2. Key strengths
    3. Weaknesses or missing skills
    4. Job roles that fit the candidate
    5. ATS score (0–100) with justification

    Resume content:
    {resume_text}
    """

    response = model.generate_content(prompt)
    return response.text
