from fastapi import FastAPI
import google.generativeai as genai
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Define request body schema
class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_text(req: PromptRequest):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")  # or gemini-1.5-pro
        response = model.generate_content(req.prompt)
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    