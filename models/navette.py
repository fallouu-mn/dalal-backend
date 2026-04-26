from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class NavetteBase(BaseModel):
    nom: str
    depart: str
    arrivee: str
    lat_depart: Optional[float] = None
    lng_depart: Optional[float] = None
    lat_arrivee: Optional[float] = None
    lng_arrivee: Optional[float] = None
    heure_depart: datetime
    capacite: int = 50
    places_restantes: int = 50
    statut: str = "a_lheure"

class Navette(NavetteBase):
    id: str
    created_at: datetime

    class Config:
        from_attributes = True
