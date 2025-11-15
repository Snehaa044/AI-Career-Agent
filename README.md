 🚀 AI Career Agent

An intelligent Streamlit application that helps job seekers analyze resumes, match job descriptions, prepare for interviews, and track job applications — all powered by the latest **Google Gemini AI models**.

This project is designed to be clean, beginner-friendly, and fully production-ready.  
Perfect for showcasing on GitHub, LinkedIn, or as a portfolio project.

---

## 🌟 Features

### 🔍 **Resume Analyzer**
Upload a PDF resume and get:
- A professional summary  
- Strengths & weaknesses  
- Missing or weak skills  
- Improvement suggestions  
- Best matching job roles  
- ATS score & readability  

---

### 📝 **Job Description Matcher**
Paste any job description and instantly see:
- Match percentage  
- Required vs. existing skills  
- Gaps to fix  
- Tailored advice to improve resume alignment  

---

### 🎤 **AI Interview Preparation**
Enter any job role and the AI will generate:
- Technical questions  
- Behavioral questions  
- Ideal sample answers  
- Difficulty levels  

---

### 📊 **Job Application Tracker**
Track your job hunt inside the app:
- Role  
- Company  
- Status (Applied / Interviewing / Offer / Rejected)  
- View your entire job log anytime  

---

## 🛠️ Tech Stack

- **Python 3.10+**  
- **Streamlit** – Web UI  
- **Google Generative AI (Gemini)**  
- **PyPDF2** – Resume text extraction  
- **dotenv** – Secure API key handling  

---

## 📁 Project Structure

ai-career-agent/
│
├── app.py
├── resume_tools.py
├── jd_tools.py
├── interview_tools.py
├── tracker.py
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md


## 🔧 Installation & Setup

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository
git clone https://github.com/Snehaa044/AI-Career-Agent.git

cd ai-career-agent


### 2️⃣ Create and Activate Virtual Environment

**Windows**
python -m venv venv
venv\Scripts\activate


**Mac/Linux**
python3 -m venv venv
source venv/bin/activate

### 3️⃣ Install Dependencies
pip install -r requirements.txt

## 🔑 Add Your API Key

Create a `.env` file in the project root:

GOOGLE_API_KEY=YOUR_API_KEY_HERE


Get your key from:  
➡ https://ai.google.dev


## ▶ Run the Application

streamlit run app.py


Once it starts, Streamlit will show something like:

Local URL: http://localhost:8501


Open the link in your browser and enjoy the app.

---

## ☁️ Deployment Guide

You can deploy this app **for FREE** using either Streamlit Cloud or HuggingFace Spaces.

---

### 🌐 Option 1 — Streamlit Cloud (Recommended)

1. Push your project to GitHub  
2. Go to https://share.streamlit.io  
3. Connect your GitHub repository  
4. Add your environment variable:
   - `GOOGLE_API_KEY`

Click "Deploy" — done.

---

### 🤗 Option 2 — HuggingFace Spaces

1. Go to https://huggingface.co/spaces  
2. Create **New Space → Streamlit**  
3. Upload all project files  
4. Add secret key in **Settings → Variables**:
   - `GOOGLE_API_KEY`

App will auto-deploy and run.

---

## 🧪 Example Outputs

### ✔ Resume Analysis  
- 78% ATS score  
- Missing skills: SQL, REST APIs  
- Suggested roles: Backend Developer, Java Engineer  

### ✔ JD Match  
- 82% match  
- Missing: Cloud basics, CI/CD  
- Recommendation: highlight project experience  

---

## ❤️ Contributing

Pull requests are welcome.  
If you'd like to add features, improve UI, or enhance accuracy, feel free to contribute.

---

## 📄 License

This project is open-source under the **MIT License**.

---

## 👩‍💻 Author

Created with love and curiosity using Python + Gemini AI.  
Perfect for students, job seekers, and AI enthusiasts.
