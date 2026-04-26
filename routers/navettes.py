from fastapi import APIRouter, HTTPException, Depends
from database.supabase_client import supabase
from models.navette import Navette
from middleware.auth_middleware import get_current_user

router = APIRouter()

@router.get("/prochaines")
async def prochaines_navettes():
    # Retourne les 5 prochaines navettes
    response = supabase.table("navettes").select("*").order("heure_depart", desc=False).limit(5).execute()
    return response.data

@router.get("/{id}/trajet")
async def trajet_navette(id: str):
    response = supabase.table("navettes").select("id, nom, lat_depart, lng_depart, lat_arrivee, lng_arrivee").eq("id", id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Navette non trouvée")
    return response.data[0]

@router.post("/{id}/reserver")
async def reserver_navette(id: str, user_id: str = Depends(get_current_user)):
    # Vérification places
    navette = supabase.table("navettes").select("places_restantes").eq("id", id).execute()
    if not navette.data or navette.data[0]["places_restantes"] <= 0:
        raise HTTPException(status_code=400, detail="Plus de places disponibles")
    
    # Décrémentation
    new_places = navette.data[0]["places_restantes"] - 1
    supabase.table("navettes").update({"places_restantes": new_places}).eq("id", id).execute()
    
    # Ajout points Teranga (+50)
    user = supabase.table("utilisateurs").select("teranga_points").eq("id", user_id).execute()
    if user.data:
        new_points = user.data[0]["teranga_points"] + 50
        supabase.table("utilisateurs").update({"teranga_points": new_points}).eq("id", user_id).execute()
    
    return {"message": "Réservation confirmée ✅", "points_gagnes": 50}
