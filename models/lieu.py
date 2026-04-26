from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LieuBase(BaseModel):
    nom: str
    type: str
    latitude: float
    longitude: float
    description: Optional[str] = None
    rating: Optional[float] = None
    distance_stade: Optional[int] = None
    horaires: Optional[str] = None
    telephone: Optional[str] = None
    premium: bool = False

class Lieu(LieuBase):
    id: str
    created_at: datetime

    class Config:
        from_attributes = True
