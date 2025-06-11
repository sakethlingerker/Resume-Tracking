from dotenv import load_dotenv
load_dotenv()

import base64
import streamlit as st
import os
import io
import fitz  # <-- PyMuPDF
import google.generativeai as genai


genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

def get_gemini_response(input_text, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_text, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        pdf_bytes = uploaded_file.read()
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        page = doc.load_page(0)  # Load first page
        pix = page.get_pixmap()

        img_byte_arr = io.BytesIO(pix.tobytes("jpeg"))
        img_bytes = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_bytes).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# === Streamlit App ===
st.set_page_config(page_title="ATS Resume Expert")
st.header("🧠 ATS Resume Tracking System")

input_text = st.text_area("📋 Job Description:", key="input")
uploaded_file = st.file_uploader("📄 Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.success("✅ PDF Uploaded Successfully")

submit1 = st.button("📊 Tell Me About the Resume")
submit3 = st.button("📈 Percentage Match")

input_prompt1 = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description.
Please share your professional evaluation on whether the candidate's profile aligns with the role.
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality.
Your task is to evaluate the resume against the provided job description. 
Give me the percentage of match, then list the missing keywords, and finally your concluding thoughts.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("📝 Evaluation:")
        st.write(response)
    else:
        st.warning("⚠️ Please upload the resume.")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("📊 Match Results:")
        st.write(response)
    else:
        st.warning("⚠️ Please upload the resume.")
