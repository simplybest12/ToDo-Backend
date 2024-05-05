from pydantic import BaseModel
from datetime import datetime

class Notes(BaseModel):
    title: str
    description: str
    created_At: datetime  # Add type annotation here
