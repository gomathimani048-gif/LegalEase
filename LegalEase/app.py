import streamlit as st
import requests 
st.set_page_config(page_title ="LegalEase")
st.title("LegalEase")
st.write("AI-powered legal document Generator")
document_type =st.text_input("Document Type")
parties = st.text_area("parties Involved")
terms = st.text_area("Terms & Conditions")
effective_date = st.date_input("Effective Date")
if st.button("Generate document"):
    data = {"document_type":document_type,"parties":parties,"terms":terms,"dates":str(effective_date)}
    response = requests.post("http://127.0.0.1:8000/generate",json=data)
    st.write(response.json())
    
