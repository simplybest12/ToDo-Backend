from fastapi import FastAPI,Depends,status,HTTPException
from core.config import settings
from database.session import Base,engine
# import schemas,models
import models
from models import Notes


def create_table():
    models.Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    create_table()
    return app

app=start_application()

@app.get('/')

def create_note():
    return {'Title' : 'title'}