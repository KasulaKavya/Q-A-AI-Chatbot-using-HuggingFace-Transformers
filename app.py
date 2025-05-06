import streamlit as st
from process_resume import extract_email, ask_question  # Import functions from process_resume.py
from pdf_loader import load_pdf
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit app title
st.title("📄 Chat with PDF")

# Upload PDF
pdf = st.file_uploader("Upload a PDF", type=["pdf"])
if pdf:
    # Save the uploaded PDF temporarily
    with open("temp.pdf", "wb") as f:
        f.write(pdf.read())

    # Load the PDF and extract text
    pages = load_pdf("temp.pdf")
    pdf_text = " ".join([page.page_content.strip() for page in pages])
    pdf_text = pdf_text.replace("\n", " ").strip()  # Preprocess the text

    # Extract email addresses
    emails = extract_email(pdf_text)
    st.write("### Email(s) found in the PDF:")
    st.write(emails)

    # Ask a question
    question = st.text_input("Ask a question about the PDF")
    if question:
        response = ask_question(pdf_text, question)
        st.write("### Answer:")
        st.write(response)