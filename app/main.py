from fastapi import FastAPI, HTTPException, Depends
import google.generativeai as genai
import uvicorn
from models.prompt import PromptRequest
from models.event import EventCreate, EventUpdate, AuthResponse
from infrastructure.calendar import calendar_manager, get_current_user
from typing import List
from utils.logger_class import LoggerClass


genai.configure(api_key="your_api_key")
app = FastAPI()
LoggerClass.configure("ped-care", debug=True)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/generate")
async def generate_text(req: PromptRequest):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")  # or gemini-1.5-pro
        prompt = "Agora você é uma agenda eletrônica automática, invente horários e a clínica se chama PedCare. Você agenda consultas para a doutora Juliana " + req.prompt
        response = model.generate_content(prompt)
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}

@app.get("/auth/login")
async def login():
    """Inicia o processo de autenticação OAuth2"""
    auth_url = calendar_manager.get_auth_url()
    return {"auth_url": auth_url, "message": "Acesse a URL para autorizar o acesso ao Google Calendar"}

@app.get("/auth/callback")
async def auth_callback(code: str):
    """Callback para receber o código de autorização"""
    try:
        tokens = calendar_manager.exchange_code_for_tokens(code)
        return {
            "message": "Autenticação realizada com sucesso",
            "tokens": tokens,
            "instructions": "Use o access_token no header Authorization: Bearer <token>"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro na autenticação: {str(e)}")

@app.post("/auth/set-credentials")
async def set_credentials(token_data: AuthResponse):
    """Define as credenciais manualmente (para testes)"""
    try:
        calendar_manager.load_credentials_from_token(token_data.dict())
        return {"message": "Credenciais configuradas com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao configurar credenciais: {str(e)}")

# CRUD Routes para Eventos
@app.post("/events/", response_model=dict)
async def create_event(
    event: EventCreate,
    calendar_id: str = 'primary',
    current_user: str = Depends(get_current_user)
):
    """Cria um novo evento no Google Calendar"""
    return calendar_manager.create_event(event, calendar_id)

@app.get("/events/", response_model=List[dict])
async def list_events(
    calendar_id: str = 'primary',
    max_results: int = 10,
    current_user: str = Depends(get_current_user)
):
    """Lista eventos do Google Calendar"""
    return calendar_manager.get_events(calendar_id, max_results)

@app.get("/events/{event_id}", response_model=dict)
async def get_event(
    event_id: str,
    calendar_id: str = 'primary',
    current_user: str = Depends(get_current_user)
):
    """Busca um evento específico"""
    return calendar_manager.get_event(event_id, calendar_id)

@app.put("/events/{event_id}", response_model=dict)
async def update_event(
    event_id: str,
    event_data: EventUpdate,
    calendar_id: str = 'primary',
    current_user: str = Depends(get_current_user)
):
    """Atualiza um evento existente"""
    return calendar_manager.update_event(event_id, event_data, calendar_id)

@app.delete("/events/{event_id}")
async def delete_event(
    event_id: str,
    calendar_id: str = 'primary',
    current_user: str = Depends(get_current_user)
):
    """Deleta um evento"""
    return calendar_manager.delete_event(event_id, calendar_id)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
    