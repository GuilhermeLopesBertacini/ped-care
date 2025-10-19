from contextlib import asynccontextmanager
from typing import AsyncGenerator
from urllib.parse import quote_plus
from venv import create
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine
from sqlalchemy import inspect

from contextlib import asynccontextmanager

from sqlmodel import SQLModel

from app.core.config import settings

connection_url = f"mysql+aiomysql://{settings.DB_USER}:" \
                f"{quote_plus(settings.DB_PASSWORD.get_secret_value())}@" \
                f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
async_engine: AsyncEngine = create_async_engine(
  connection_url,
  pool_pre_ping=True, # Checks if the database is still active before accessing
  pool_recycle = 1800, # Recycle connections after 30 minutes
  echo = False, # Set to True to see the raw SQL queries being executed
)

@asynccontextmanager
async def get_async_session():
    """Provide a transactional scope around a series of operations."""
    async with AsyncSession(async_engine) as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

async def init_db():
    """Initialize the database instance"""
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def has_tables() -> bool:
    """
    Inspect the database schema and check if there are any tables present.
    Returns True if there are tables, False otherwise.
    """
    async with async_engine.connect() as conn:
        tables = await conn.run_sync( # transforms to synchronous connection
            lambda sync_conn: inspect(sync_conn).get_table_names()
        )
        return len(tables) > 0