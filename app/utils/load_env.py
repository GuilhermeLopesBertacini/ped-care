import os
from dotenv import load_dotenv
from app.utils.logger_class import LoggerClass

def load_env(file_path: str = ".env"):
    full_path = os.path.abspath(file_path)
    if os.path.exists(full_path):
        load_dotenv(dotenv_path=full_path, override=True)
    else:
        LoggerClass.error(f"Arquivo .env não encontrado em {full_path}.")