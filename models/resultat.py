from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ResultatBase(BaseModel):
    sport: str
    epreuve: str
    equipe1: Optional[str] = None
    equipe2: Optional[str] = None
    score1: int = 0
    score2: int = 0
    statut: str = "a_venir"
    phase: Optional[str] = None
    heure_debut: Optional[datetime] = None

class Resultat(ResultatBase):
    id: str
    created_at: datetime

    class Config:
        from_attributes = True
