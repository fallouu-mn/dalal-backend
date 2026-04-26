from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    nom: str
    prenom: str
    telephone: Optional[str] = None
    langue_preferee: str = "fr"

class UserCreate(UserBase):
    mot_de_passe: str

class UserLogin(BaseModel):
    email: EmailStr
    mot_de_passe: str

class UserOrangeLogin(BaseModel):
    telephone: str

class UserProfile(UserBase):
    id: str
    teranga_points: int
    created_at: datetime

    class Config:
        from_attributes = True
