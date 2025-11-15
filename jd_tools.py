import google.generativeai as genai

def match_resume(resume_text, jd_text):
    prompt = f"""
    Compare resume and JD.

    Provide:
    - Resume–JD Match %
    - Missing Skills
    - Overlapping Skills
    - Improvement Suggestions

    Resume:
    {resume_text}

    JD:
    {jd_text}
    """
    return genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt).text
