import streamlit as st
from resume_tools import extract_resume_text, analyze_resume
from jd_tools import match_resume
from interview_tools import generate_interview_questions
from tracker import add_application, list_applications

st.set_page_config(page_title="AI Career Agent", page_icon="🤖")

st.title("🤖 AI Career Agent")
st.write("Upload your resume and get an intelligent analysis, madam.")

# ===== RESUME UPLOAD & ANALYSIS =====
uploaded_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])
resume_text = ""

if uploaded_file:
    with open("uploaded_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✔ Resume uploaded successfully")
    resume_text = extract_resume_text("uploaded_resume.pdf")

    if resume_text.strip() == "":
        st.error("Could not read text from PDF. Try another file.")
    else:
        st.subheader("📄 Extracted Resume Text")
        st.text_area("Resume Content", resume_text, height=300)

        if st.button("Analyze Resume"):
            with st.spinner("Analyzing with Gemini…"):
                analysis = analyze_resume(resume_text)
            st.subheader("🔍 AI Resume Assessment")
            st.write(analysis)


# ===== JOB DESCRIPTION MATCH =====
st.header("Job Description Match")
jd = st.text_area("Paste Job Description here:")

if st.button("Match Resume to JD"):
    if resume_text.strip() == "":
        st.warning("Upload a resume first")
    else:
        with st.spinner("Matching resume to JD…"):
            jd_result = match_resume(resume_text, jd)
        st.write(jd_result)


# ===== INTERVIEW PREPARATION =====
st.header("Interview Prep")
role = st.text_input("Job Role for Interview:")

if st.button("Generate Interview Questions"):
    with st.spinner("Generating questions…"):
        questions = generate_interview_questions(role)
    st.subheader("💡 Interview Questions")
    st.write(questions)


# ===== APPLICATION TRACKER =====
st.header("Application Tracker")
role2 = st.text_input("Role Title for Application Tracker")
company = st.text_input("Company Name")
status = st.text_input("Status (Applied/Interviewed/etc)")

if st.button("Add Application"):
    add_application(role2, company, status)
    st.success("Application added!")

if st.button("Show All Applications"):
    apps = list_applications()
    st.table(apps)
