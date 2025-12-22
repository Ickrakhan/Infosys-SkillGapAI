import streamlit as st
from txt_parser import parse_txt


st.title("Document Upload & Parsing")

uploaded_file = st.file_uploader(
    "Upload Resume or Job Description",
    type=["txt"]
)

if uploaded_file:
    parsed_text = parse_txt(uploaded_file)

    st.success("TXT file parsed successfully")

    st.subheader("Parsed Document Preview")
    st.text_area("Content", parsed_text, height=300)
