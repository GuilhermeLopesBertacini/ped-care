import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.utils.logger_class import LoggerClass
from app.core.router import api_router
from app.core.database import init_db, has_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    if not await has_tables():
        await init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(api_router)

LoggerClass.configure("ped-care", debug=True)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)