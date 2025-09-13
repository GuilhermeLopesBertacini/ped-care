from fastapi import FastAPI
from fastapi.security import HTTPBearer
import google.generativeai as genai
import uvicorn
import logging
from models.prompt import PromptRequest

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

security = HTTPBearer()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/generate")
async def generate_text(req: PromptRequest):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")  # or gemini-1.5-pro
        response = model.generate_content(req.prompt)
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
    