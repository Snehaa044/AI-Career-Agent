import google.generativeai as genai

def match_resume(resume_text, job_description):
    """Match resume to a job description using Gemini 2.5 Flash."""
    prompt = f"""
    Compare this resume with the job description and give:
    1. A match score (0–100)
    2. Key skills missing
    3. Recommendations to improve match

    Resume:
    {resume_text}

    Job Description:
    {job_description}
    """

    model = genai.GenerativeModel("models/gemini-2.5-flash")  # UPDATED model
    response = model.generate_content(prompt)
    return response.text
