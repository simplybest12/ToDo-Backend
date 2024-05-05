from fastapi import FastAPI,Depends,status,HTTPException
from core.config import settings
from sqlalchemy.orm import Session
from database import session
from database.session import Base,engine
import schemas,models
from models import Notes
from router import notes


def create_table():
    models.Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    create_table()
    return app

app=start_application()

get_db = session.get_db

app.include_router(notes.router)
