from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class EventBase(BaseModel):
    summary: str = Field(..., description="Título do evento")
    description: Optional[str] = Field(None, description="Descrição do evento")
    location: Optional[str] = Field(None, description="Local do evento")
    start_datetime: datetime = Field(..., description="Data/hora de início")
    end_datetime: datetime = Field(..., description="Data/hora de fim")
    timezone: str = Field(default="America/Sao_Paulo", description="Fuso horário")

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    summary: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    start_datetime: Optional[datetime] = None
    end_datetime: Optional[datetime] = None
    timezone: Optional[str] = None

class EventResponse(EventBase):
    id: str
    html_link: str
    status: str
    created: datetime
    updated: datetime

class AuthResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_uri: str
    client_id: str
    client_secret: str