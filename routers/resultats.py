from fastapi import APIRouter
from database.supabase_client import supabase
from typing import Optional

router = APIRouter()

@router.get("/")
async def lister_resultats(statut: str = "all"):
    query = supabase.table("resultats").select("*").order("heure_debut", desc=False)
    
    if statut != "all":
        query = query.eq("statut", statut)
    
    response = query.execute()
    # On met les 'en_cours' en premier manuellement pour plus de flexibilité
    data = response.data
    sorted_data = sorted(data, key=lambda x: 0 if x["statut"] == "en_cours" else 1)
    
    return sorted_data

@router.get("/live")
async def resultats_live():
    response = supabase.table("resultats").select("*").eq("statut", "en_cours").execute()
    # Simulation de mise à jour des scores
    data = response.data
    for match in data:
        # Petite touche dynamique pour la démo
        import random
        if random.random() > 0.7:
            match["score1"] += 1
    return data
