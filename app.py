import google.generativeai as genai
import os
import streamlit as st
from PyPDF2 import PdfReader
from PIL import Image
from dotenv import load_dotenv
from docx import Document

# Load environment variables from .env file
load_dotenv()

# Access the API key from environment variables
google_api_key = os.getenv('GOOGLE_API_KEY')

# Configure the generative AI with the API key
genai.configure(api_key=google_api_key)

# Create a model instance (double-check model ID in API docs)
model = genai.GenerativeModel('gemini-1.0-pro-latest')

# Define the input prompt
input_prompt = """
You are an Applicant Tracking System (ATS) designed to evaluate resumes against job descriptions in a competitive job market.

Your task is to assess the provided resume based on the following expertise areas:
- Software Engineering
- Data Science
- Machine Learning
- Cloud Computing

Please analyze the resume and provide a structured response with the following sections:

1. **Percentage Match:** Calculate and provide a percentage indicating how closely the resume matches the job description. This should reflect how well the resume aligns with the required expertise areas.

2. **List of Missing Keywords:** Identify and list any important keywords or phrases from the job description that are missing in the resume.

3. **Profile Summary:** Summarize the resume, highlighting key details such as:
   - **Education:** Degree, institution, GPA, and graduation year.
   - **Professional Experience:** Roles, responsibilities, and achievements.
   - **Skills:** Technical and soft skills relevant to the job description.
   - **Additional Information:** Languages, certifications, and interests if relevant.

Ensure that your response is clearly divided into these three sections.
"""

# Function to generate a response using the Gemini model
def get_gemini_response(input_text):
    try:
        # Use the `generate_content` method to generate the response
        response = model.generate_content(input_prompt + "\n\n" + input_text)
        return response.text  # Access the response text
    except AttributeError as e:
        st.error(f"AttributeError: {e}")
        return None
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Function to extract text from PDF
def input_pdf_text(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to extract text from DOCX
def input_docx_text(docx_file):
    doc = Document(docx_file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

# Streamlit UI
st.set_page_config(page_title="Resume ATS Tracker", layout="wide")

# Introduction Section
col1, col2 = st.columns([3, 2])
with col1:
    st.title("CareerCraft")
    st.header("Navigate the Job Market with Confidence!")
    st.markdown("""<p style='text-align: justify;'>
    Introducing CareerCraft, an ATS-Optimized Resume Analyzer your ultimate solution for optimizing job applications and accelerating career growth. Our innovative platform leverages advanced ATS technology to provide job seekers with valuable insights into their resumes' compatibility with job descriptions. From resume optimization and skill enhancement to career progression guidance, CareerCraft empowers users to stand out in today's competitive job market. Streamline your job application process, enhance your skills, and navigate your career path with confidence. Join CareerCraft today and unlock new opportunities for professional success! </p>""", unsafe_allow_html=True)
with col2:
    st.image('https://i.imgur.com/RoBAGZf.jpg', use_column_width=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Offerings Section
col1, col2 = st.columns([3, 2])
with col2:
    st.header("Wide Range of Offerings")
    st.write('ATS-Optimized Resume Analysis')
    st.write('Resume Optimization')
    st.write('Skill Enhancement')
    st.write('Career Progression Guidance')
    st.write('Tailored Profile Summaries')
    st.write('Streamlined Application Process')
    st.write('Personalized Recommendations')
    st.write('Efficient Career Navigation')
with col1:
    st.image('https://i.imgur.com/UDioJyj.jpg', use_column_width=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Resume ATS Tracking Application
col1, col2 = st.columns([3, 2])
with col1:
    st.markdown("<h1 style='text-align: center;'>Embark on Your Career Adventure</h1>", unsafe_allow_html=True)
    jd = st.text_area("Paste the Job Description")
    uploaded_file = st.file_uploader("Upload Your Resume", type=["pdf", "docx"], help="Please upload a PDF or DOCX file")
    submit = st.button("Submit")
    if submit:
        if uploaded_file is not None:
            if uploaded_file.name.endswith('.pdf'):
                text = input_pdf_text(uploaded_file)
            elif uploaded_file.name.endswith('.docx'):
                text = input_docx_text(uploaded_file)
            else:
                st.error("Unsupported file format")
                text = None

            if text:
                response = get_gemini_response(jd + "\n\n" + text)
                st.subheader("Gemini Response:")
                st.write(response)
with col2:
    st.image('https://i.imgur.com/x7stH1a.jpg', use_column_width=True)
st.markdown("<hr>", unsafe_allow_html=True)

# FAQ Section
col1, col2 = st.columns([2, 3])
with col2:
    st.markdown("<h1 style='text-align: center;'>FAQ</h1>", unsafe_allow_html=True)
    st.write("Question: How does CareerCraft analyze resumes and job descriptions?")
    st.write("""Answer: CareerCraft uses advanced algorithms to analyze resumes and job descriptions, identifying key keywords and assessing compatibility between the two.""")
    st.write("Question: Can CareerCraft suggest improvements for my resume?")
    st.write("""Answer: Yes, CareerCraft provides personalized recommendations to optimize your resume for specific job openings, including suggestions for missing keywords and alignment with desired job roles.""")
    st.write("Question: Is CareerCraft suitable for both entry-level and experienced professionals?")
    st.write("""Answer: Absolutely! CareerCraft caters to job seekers at all career stages, offering tailored insights and guidance to enhance their resumes and advance their careers.""")
with col1:
    st.image('https://i.imgur.com/1AnHxkx.jpg', use_column_width=True)
