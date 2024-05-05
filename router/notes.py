from fastapi import FastAPI,Depends,status,HTTPException
from core.config import settings
from sqlalchemy.orm import Session
from database import session
from database.session import Base,engine
import schemas,models
from models import Notes


router = APIRouter(
    tags = ['NOTES']
)


get_db = session.get_db


@router.post("/",status_code=status.HTTP_201_CREATED)

def create(request:schemas.Notes,db:Session = Depends(get_db)):
    new_notes = models.Notes(title = request.title, description = request.description , created_At = request.created_At)
    
    db.add(new_notes)
    db.commit()
    db.refresh(new_notes)
    return new_notes


@router.get('/notes' , status_code= status.HTTP_200_OK)

def getData(db:Session = Depends(get_db)):
    notes = db.query(models.Notes).all()
    return notes

@router.get('/notes/{id}' , status_code=status.HTTP_200_OK)

def getData_by_id(id:int , db:Session = Depends(get_db)):
    note = db.query(models.Notes).filter(models.Notes.id == id).first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Detail of {id} not found")
    return note


@router.put('/update/{id}' , status_code=status.HTTP_202_ACCEPTED)

def update(id:int, request:schemas.Notes , db:Session = Depends(get_db)):

    note = db.query(models.Notes).filter(models.Notes.id == id)
    if not note.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Detail of {id} not found")
    note.update(request)
    db.commit()
    return 'updated'

@router.delete('/del/{id}' , status_code=status.HTTP_204_NO_CONTENT)

def destroy(id:int,db:Session = Depends(get_db)):
    note = db.query(models.Notes).filter(models.Notes.id == id)
    if not note.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Detail of {id} not found")
    note.delete(synchronize_session=False)
    db.commit()
    return
    