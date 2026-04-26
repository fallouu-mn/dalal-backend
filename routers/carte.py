from fastapi import APIRouter, Query
from database.supabase_client import supabase
from typing import Optional
import math

router = APIRouter()

@router.get("/lieux")
async def lister_lieux(
    type: str = "all", 
    lat: Optional[float] = None, 
    lng: Optional[float] = None
):
    query = supabase.table("lieux").select("*")
    if type != "all":
        query = query.eq("type", type)
    
    response = query.execute()
    lieux = response.data

    # Calcul de distance si coordonnées fournies
    if lat is not None and lng is not None:
        for lieu in lieux:
            # Simplification: distance euclidienne (à remplacer par Haversine en prod)
            dist = math.sqrt((lieu["latitude"] - lat)**2 + (lieu["longitude"] - lng)**2)
            lieu["distance_km"] = round(dist * 111.12, 2) # Approximation degrés -> km
    
    return lieux

@router.get("/recherche")
async def rechercher_lieux(q: str):
    # Recherche simple sur le nom ou description
    response = supabase.table("lieux").select("*").or_(f"nom.ilike.%{q}%,description.ilike.%{q}%").execute()
    return response.data

@router.get("/proximite")
async def lieux_proximite(lat: float, lng: float, rayon: int = 1000):
    # 1 degré ~= 111.12 km
    delta = rayon / 111120.0
    
    response = supabase.table("lieux").select("*")\
        .gte("latitude", lat - delta)\
        .lte("latitude", lat + delta)\
        .gte("longitude", lng - delta)\
        .lte("longitude", lng + delta)\
        .execute()
    
    return response.data
