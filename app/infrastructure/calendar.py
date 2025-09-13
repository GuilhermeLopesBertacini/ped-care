from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timezone
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build

from models.event import EventCreate, EventUpdate
from utils.logger_class import LoggerClass

security = HTTPBearer()

SCOPES = ['https://www.googleapis.com/auth/calendar']
CLIENT_SECRETS_FILE = "credentials.json"  # Baixe do Google Cloud Console
REDIRECT_URI = "http://localhost:8000/auth/callback"

# Classe para gerenciar credenciais
class GoogleCalendarManager:
    def __init__(self):
        self.credentials = None
        self.service = None

    def get_auth_url(self):
        """Gera URL para autenticação OAuth2"""
        flow = Flow.from_client_secrets_file(
            CLIENT_SECRETS_FILE, 
            scopes=SCOPES,
            redirect_uri=REDIRECT_URI
        )
        auth_url, _ = flow.authorization_url(prompt='consent')
        return auth_url

    def exchange_code_for_tokens(self, authorization_code: str):
        """Troca o código de autorização por tokens"""
        flow = Flow.from_client_secrets_file(
            CLIENT_SECRETS_FILE,
            scopes=SCOPES,
            redirect_uri=REDIRECT_URI
        )
        flow.fetch_token(code=authorization_code)
        
        self.credentials = flow.credentials
        self.service = build('calendar', 'v3', credentials=self.credentials)
        
        return {
            "access_token": self.credentials.token,
            "refresh_token": self.credentials.refresh_token,
            "token_uri": self.credentials.token_uri,
            "client_id": self.credentials.client_id,
            "client_secret": self.credentials.client_secret,
        }

    def load_credentials_from_token(self, token_data: dict):
        """Carrega credenciais a partir dos dados do token"""
        self.credentials = Credentials(
            token=token_data.get('access_token'),
            refresh_token=token_data.get('refresh_token'),
            token_uri=token_data.get('token_uri'),
            client_id=token_data.get('client_id'),
            client_secret=token_data.get('client_secret'),
            scopes=SCOPES
        )
        
        # Refresh token se necessário
        if self.credentials.expired:
            self.credentials.refresh(Request())
        
        self.service = build('calendar', 'v3', credentials=self.credentials)

    def create_event(self, event_data: EventCreate, calendar_id: str = 'primary'):
        """Cria um novo evento no calendário"""
        if not self.service:
            raise HTTPException(status_code=401, detail="Não autenticado")

        event = {
            'summary': event_data.summary,
            'description': event_data.description,
            'location': event_data.location,
            'start': {
                'dateTime': event_data.start_datetime.isoformat(),
                'timeZone': event_data.timezone,
            },
            'end': {
                'dateTime': event_data.end_datetime.isoformat(),
                'timeZone': event_data.timezone,
            },
        }

        try:
            result = self.service.events().insert(calendarId=calendar_id, body=event).execute()
            return result
        except Exception as e:
            LoggerClass.error(f"Erro ao criar evento: {str(e)}")
            raise HTTPException(status_code=400, detail=f"Erro ao criar evento: {str(e)}")

    def get_events(self, calendar_id: str = 'primary', max_results: int = 10):
        """Lista eventos do calendário"""
        if not self.service:
            raise HTTPException(status_code=401, detail="Não autenticado")

        try:
            events_result = self.service.events().list(
                calendarId=calendar_id,
                maxResults=max_results,
                singleEvents=True,
                orderBy='startTime',
                timeMin=datetime.now(timezone.utc).isoformat()
            ).execute()
            
            return events_result.get('items', [])
        except Exception as e:
            LoggerClass.error(f"Erro ao buscar eventos: {str(e)}")
            raise HTTPException(status_code=400, detail=f"Erro ao buscar eventos: {str(e)}")

    def get_event(self, event_id: str, calendar_id: str = 'primary'):
        """Busca um evento específico"""
        if not self.service:
            raise HTTPException(status_code=401, detail="Não autenticado")

        try:
            event = self.service.events().get(calendarId=calendar_id, eventId=event_id).execute()
            return event
        except Exception as e:
            LoggerClass.error(f"Erro ao buscar evento: {str(e)}")
            raise HTTPException(status_code=404, detail="Evento não encontrado")

    def update_event(self, event_id: str, event_data: EventUpdate, calendar_id: str = 'primary'):
        """Atualiza um evento existente"""
        if not self.service:
            raise HTTPException(status_code=401, detail="Não autenticado")

        try:
            # Busca o evento atual
            event = self.service.events().get(calendarId=calendar_id, eventId=event_id).execute()
            
            # Atualiza apenas os campos fornecidos
            if event_data.summary is not None:
                event['summary'] = event_data.summary
            if event_data.description is not None:
                event['description'] = event_data.description
            if event_data.location is not None:
                event['location'] = event_data.location
            if event_data.start_datetime is not None:
                event['start']['dateTime'] = event_data.start_datetime.isoformat()
                if event_data.timezone:
                    event['start']['timeZone'] = event_data.timezone
            if event_data.end_datetime is not None:
                event['end']['dateTime'] = event_data.end_datetime.isoformat()
                if event_data.timezone:
                    event['end']['timeZone'] = event_data.timezone

            updated_event = self.service.events().update(
                calendarId=calendar_id, 
                eventId=event_id, 
                body=event
            ).execute()
            
            return updated_event
        except Exception as e:
            LoggerClass.error(f"Erro ao atualizar evento: {str(e)}")
            raise HTTPException(status_code=400, detail=f"Erro ao atualizar evento: {str(e)}")

    def delete_event(self, event_id: str, calendar_id: str = 'primary'):
        """Deleta um evento"""
        if not self.service:
            raise HTTPException(status_code=401, detail="Não autenticado")

        try:
            self.service.events().delete(calendarId=calendar_id, eventId=event_id).execute()
            return {"message": "Evento deletado com sucesso"}
        except Exception as e:
            LoggerClass.error(f"Erro ao deletar evento: {str(e)}")
            raise HTTPException(status_code=400, detail=f"Erro ao deletar evento: {str(e)}")

# Instância global do gerenciador
calendar_manager = GoogleCalendarManager()

# Dependency para verificar autenticação
async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Verifica se o usuário está autenticado"""
    token = credentials.credentials
    # Aqui você pode implementar validação mais robusta do token
    # Por simplicidade, assumimos que o token é válido se existir
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token de acesso não fornecido"
        )
    return token
