import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

url: str = os.environ.get("SUPABASE_URL", "")
key: str = os.environ.get("SUPABASE_SERVICE_KEY") or os.environ.get("SUPABASE_ANON_KEY", "")

# Initialisation du client Supabase (lazy — échoue proprement par requête)
supabase: Client = None

def get_supabase() -> Client:
    """Retourne le client Supabase, initialisé à la demande."""
    global supabase
    if supabase is None:
        if not url or not key:
            raise ValueError("SUPABASE_URL et SUPABASE_KEY doivent être définis dans les variables d'environnement")
        supabase = create_client(url, key)
    return supabase

# Tentative d'initialisation immédiate (non bloquante)
try:
    if url and key:
        supabase = create_client(url, key)
        print("✅ Supabase connecté avec succès")
    else:
        print("⚠️  Variables Supabase manquantes — client non initialisé")
except Exception as e:
    print(f"⚠️  Supabase init échouée : {e} — l'app démarre quand même")
    supabase = None
