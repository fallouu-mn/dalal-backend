from fastapi import APIRouter, HTTPException, Depends
from database.supabase_client import supabase
from middleware.auth_middleware import get_current_user
from services.qr_service import generer_qr
import json

router = APIRouter()

@router.get("/mon-pass")
async def mon_pass(user_id: str = Depends(get_current_user)):
    response = supabase.table("pass_joj").select("*").eq("utilisateur_id", user_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Pass non trouvé")
    
    pass_info = response.data[0]
    # Génération du QR code en base64
    qr_data = {
        "pass_id": pass_info["id"],
        "user_id": user_id,
        "zones": pass_info["zones_acces"],
        "expire": pass_info["valide_jusqu_au"]
    }
    pass_info["qr_base64"] = generer_qr(json.dumps(qr_data))
    
    return pass_info

@router.get("/historique")
async def historique_pass(user_id: str = Depends(get_current_user)):
    response = supabase.table("historique_entrees").select("*").eq("utilisateur_id", user_id).order("entree_at", desc=True).limit(10).execute()
    return response.data

@router.post("/valider/{code_qr}")
async def valider_pass(code_qr: str):
    # Vérification validité
    response = supabase.table("pass_joj").select("*, utilisateurs(*)").eq("code_qr", code_qr).eq("actif", True).execute()
    
    if not response.data:
        return {"valide": False, "message": "QR Code invalide ou inactif"}
    
    pass_obj = response.data[0]
    
    # Enregistrement historique (simulation lieu: 'Check-point JOJ')
    entree = {
        "utilisateur_id": pass_obj["utilisateur_id"],
        "lieu": "Check-point Officiel JOJ",
        "zone": pass_obj["zones_acces"][0] if pass_obj["zones_acces"] else "Standard"
    }
    supabase.table("historique_entrees").insert(entree).execute()
    
    return {
        "valide": True,
        "utilisateur": pass_obj["utilisateurs"],
        "zones": pass_obj["zones_acces"]
    }
