from fastapi import APIRouter
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

router = APIRouter()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    dates: str

@router.get("/")
def home():
    return{"message": "LegalEase Backend is Running"}

@router.post("/generate") 
def generate_document(request: DocumentRequest):
    prompt = f"""
    Create a professional legal document.

    Document Type:
    {request.document_type}

    parties:
    {request:parties}

    terms:
    {request:terms}
    
    dates:
    {request:dates}

    Write the document clearly with proper sections.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return{"document: response.text"}
