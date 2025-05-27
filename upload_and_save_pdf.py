import streamlit as st
import os
import pdfplumber

st.title("📥 Upload PDF and Convert to Text")

# Directories
pdf_dir = "uploaded_pdfs"
text_dir = "converted_txts"
os.makedirs(pdf_dir, exist_ok=True)
os.makedirs(text_dir, exist_ok=True)

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    pdf_path = os.path.join(pdf_dir, uploaded_file.name)
    
    # Save the uploaded file
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"✅ PDF saved to: {pdf_path}")

# Convert all PDFs in uploaded_pdfs
st.subheader("📄 Converting all PDFs to text...")

pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith(".pdf")]

if not pdf_files:
    st.info("No PDFs found in 'uploaded_pdfs' folder.")
else:
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_dir, pdf_file)
        txt_path = os.path.join(text_dir, pdf_file + ".txt")

        try:
            with pdfplumber.open(pdf_path) as pdf:
                text = "\n".join([page.extract_text() or "" for page in pdf.pages])
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(text)
            st.success(f"✅ Converted and saved: {txt_path}")
        except Exception as e:
            st.error(f"❌ Failed to process {pdf_file}: {e}")

