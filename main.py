import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from dotenv import load_dotenv

from database import db
from vistas import router as vistas_router

load_dotenv()


def get_database_url() -> str:
    db_url = os.getenv("DATABASE_URL", "").strip()

    if not db_url:
        raise RuntimeError(
            "Falta la variable DATABASE_URL en el archivo .env. "
            "Ejemplo: DATABASE_URL=\"postgresql://usuario:password@host:5432/basedatos\""
        )

    return db_url


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Al arrancar la aplicación se crea el pool de conexiones a PostgreSQL.
    await db.connect(get_database_url())
    yield
    # Al apagar la aplicación, el pool se cierra para liberar las conexiones.
    await db.close()


app = FastAPI(lifespan=lifespan)

app.include_router(vistas_router)