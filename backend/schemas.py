from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Notes(BaseModel):
    title:str
    description:str
    created_At = datetime
    