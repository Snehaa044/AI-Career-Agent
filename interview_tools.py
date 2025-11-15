import google.generativeai as genai

def generate_interview_questions(role):
    prompt = f"Generate 10 interview questions for a {role} role."
    return genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt).text
