from fastapi import FastAPI, HTTPException, Depends
import google.generativeai as genai
import uvicorn
from app.models.prompt import PromptRequest
from utils.logger_class import LoggerClass


app = FastAPI()
LoggerClass.configure("ped-care", debug=True)

@app.get("/")
async def root():
    return {"message": "Hello World"}

genai.configure(api_key="your_api_key")
@app.post("/generate")
async def generate_text(req: PromptRequest):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")  # or gemini-1.5-pro
        prompt = "Agora você é uma agenda eletrônica automática, invente horários e a clínica se chama PedCare. Você agenda consultas para a doutora Juliana " + req.prompt
        response = model.generate_content(prompt)
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
    