from fastapi import APIRouter
import google.generativeai as genai

from app.core.config import settings
from app.models.prompt import PromptRequest

router = APIRouter(prefix="/gemini", tags=["gemini"])
genai.configure(api_key=settings.GEMINI_API_KEY)

@router.post("/generate")
async def generate_text(req: PromptRequest):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")  # or gemini-1.5-pro
        prompt = "Agora você é uma agenda eletrônica automática, invente horários e a clínica se chama PedCare. Você agenda consultas para a doutora Juliana " + req.prompt
        response = model.generate_content(prompt)
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}
