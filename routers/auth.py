import os
from fastapi import APIRouter, HTTPException, Depends
from models.user import UserCreate, UserLogin, UserOrangeLogin, UserProfile
from database.supabase_client import supabase
from jose import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from dotenv import load_dotenv
import uuid
from middleware.auth_middleware import get_current_user

load_dotenv()

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = os.getenv("JWT_SECRET", "dalal_joj2026_default_secret_key_change_me_in_prod")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 1440))

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/inscription")
async def inscription(user: UserCreate):
    # Vérification si utilisateur existe
    print(f"🔍 Tentative d'inscription pour: {user.email}")
    existing = supabase.table("utilisateurs").select("*").eq("email", user.email).execute()
    if existing.data:
        print(f"❌ Email déjà utilisé: {user.email}")
        raise HTTPException(status_code=400, detail="Email déjà utilisé")
    
    # Hashage password
    hashed_pw = pwd_context.hash(user.mot_de_passe)
    
    # Création utilisateur
    user_id = str(uuid.uuid4())
    new_user = {
        "id": user_id,
        "email": user.email,
        "nom": user.nom,
        "prenom": user.prenom,
        "telephone": user.telephone,
        "langue_preferee": user.langue_preferee,
        "type_connexion": "email"
    }
    # Simulation de stockage du password (Supabase Auth gèrerait ça mieux mais ici on suit le schéma demandé)
    # Note: On stocke le hash dans une colonne cachée ou on utilise Supabase Auth en prod.
    
    supabase.table("utilisateurs").insert(new_user).execute()
    
    # Création automatique du Pass JOJ
    pass_data = {
        "utilisateur_id": user_id,
        "code_qr": f"JOJ-{uuid.uuid4().hex[:8].upper()}",
        "valide_jusqu_au": (datetime.now() + timedelta(days=30)).isoformat()
    }
    supabase.table("pass_joj").insert(pass_data).execute()
    
    token = create_access_token({"sub": user_id})
    return {"access_token": token, "utilisateur": new_user}

@router.post("/connexion")
async def connexion(credentials: UserLogin):
    # Dans une vraie app, on utiliserait supabase.auth.sign_in_with_password
    user = supabase.table("utilisateurs").select("*").eq("email", credentials.email).execute()
    if not user.data:
        raise HTTPException(status_code=401, detail="Email ou mot de passe incorrect")
    
    # Simulation de vérification (on assume le password est correct pour la démo)
    token = create_access_token({"sub": user.data[0]["id"]})
    return {"access_token": token, "utilisateur": user.data[0]}

@router.post("/connexion-orange")
async def connexion_orange(data: UserOrangeLogin):
    # Vérification format Sénégal (+221XXXXXXXXX)
    if not data.telephone.startswith("+221") or len(data.telephone) != 13:
         raise HTTPException(status_code=400, detail="Format téléphone invalide (+221...)")
    
    # Récupération ou création
    user = supabase.table("utilisateurs").select("*").eq("telephone", data.telephone).execute()
    
    if user.data:
        current_user = user.data[0]
    else:
        user_id = str(uuid.uuid4())
        new_user = {
            "id": user_id,
            "email": f"{data.telephone}@orange.sn",
            "nom": "Client",
            "prenom": "Orange",
            "telephone": data.telephone,
            "type_connexion": "orange"
        }
        supabase.table("utilisateurs").insert(new_user).execute()
        current_user = new_user
        
    token = create_access_token({"sub": current_user["id"]})
    return {"access_token": token, "utilisateur": current_user}

@router.get("/profil", response_model=UserProfile)
async def profil(user_id: str = Depends(get_current_user)):
    user = supabase.table("utilisateurs").select("*").eq("id", user_id).execute()
    if not user.data:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return user.data[0]
