import streamlit as st
from resume_tools import extract_resume_text, analyze_resume

st.set_page_config(page_title="AI Career Agent", page_icon="🤖")

st.title("🤖 AI Career Agent")
st.write("Upload your resume and get an intelligent analysis, madam.")

uploaded_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])

if uploaded_file:
    with open("uploaded_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✔ Resume uploaded successfully")

    # Extract text
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
