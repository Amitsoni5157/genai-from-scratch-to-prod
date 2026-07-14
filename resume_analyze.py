from http import client
import streamlit as st
import PyPDF2
import os
import io
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Resume Critiquer", page_icon="🔍",layout="centered")

st.title("AI Resume Crittiquer 🤖")
st.markdown("Upload your resume and get AI-powerd feedback tailored to your needs!")


GROQ_API_KEY= os.getenv("GROQ_API_KEY")

upload_file = st.file_uploader("Upload your resume (PDF or TXT files)", type=["pdf","txt"])
job_role = st.text_input("Enter the job role you are targetting (optional)")

analyze = st.button("Analyze Resume")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_file(upload_file):
    if upload_file.type == "application/pdf":
        # reading the PDF file
        return extract_text_from_pdf(io.BytesIO(upload_file.read()))
    return upload_file.read().decode("utf-8")


if analyze and upload_file:
    try:
        file_content = extract_text_from_file(upload_file)    

        if not file_content.strip():
            st.error("File does not have any content....")
            st.stop()

        prompt = f""" 
        You are a strict, professional career coach and resume expert.
        Critique the following resume text based on the user's target job role.

        Target Job Role: {job_role if job_role else "Not specified (analyze generally)"}

        Resume Text:
        {file_content}

        Your critique must be extremely detailed, actionable, and formatted in Markdown with the following structure:

        # Resume Critique
        
        ## Overall Impression
        - Strongest aspects of the resume
        - Weakest aspects and areas needing immediate attention
        
        ## Strength-by-Strength Analysis
        1. **Summary/Objective**: Is it compelling? Quantifiable? Tailored?
        2. **Experience Section**: Are the bullet points action-oriented? Do they show impact?
        3. **Quantification**: Are numbers, metrics, and percentages used effectively?
        4. **Keywords**: Are industry-specific keywords present?
        5. **Formatting**: Is it clean, readable, and professional?
        6. **Tailoring**: How well does it match the target role?
        
        ## Specific Recommendations
        For each area needing improvement, provide: 
        - What to change
        - Why it needs to change
        - Example of a stronger version
        
        ## Action Plan
        A prioritized list of what the user should do next (3-5 steps)
        
        ## Final Verdict
        - Would you recommend this resume for the target role?
        - What's the biggest weakness holding it back?

        Be honest, be specific, and don't sugarcoat anything. The goal is to make this resume top-tier.
        """

        client = Groq(api_key=GROQ_API_KEY)
        response = client.chat.completions.create(
            model= "llama-3.3-70b-versatile",
            messages=[
                {
                    "role":"system",
                    "content": "you are a strict, professional career coach and resume expert."
                },
                {
                    "role":"user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=1000
        )
        st.markdown("### Analysis Result")
        # printing the response in markdown format
        st.markdown(response.choices[0].message.content)

    except Exception as e:
        st.error(f"Error analyzing resume: {str(e)}")

