import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

url: str = os.environ.get("SUPABASE_URL", "")
key: str = os.environ.get("SUPABASE_SERVICE_KEY") or os.environ.get("SUPABASE_ANON_KEY", "")

if not url or not key:
    print("⚠️  Variables Supabase manquantes. Assurez-vous de définir SUPABASE_URL et SUPABASE_ANON_KEY/SUPABASE_SERVICE_KEY.")
    print("Si vous êtes sur Render, ajoutez ces variables dans l'onglet Environment de votre service.")

class DummySupabase:
    """Classe de remplacement pour lancer une erreur claire si Supabase n'est pas initialisé."""
    def __getattr__(self, name):
        raise ValueError(
            "🛑 ERREUR CRITIQUE: Supabase n'est pas initialisé.\n"
            "Vos variables d'environnement (SUPABASE_URL et SUPABASE_ANON_KEY ou SUPABASE_SERVICE_KEY) "
            "sont manquantes. Si vous avez déployé sur Render, allez dans le Dashboard Render -> "
            "votre Web Service -> Onglet 'Environment' et ajoutez vos variables."
        )

# Initialisation du client Supabase
try:
    if url and key:
        supabase: Client = create_client(url, key)
        print("✅ Supabase connecté avec succès")
    else:
        supabase = DummySupabase()
except Exception as e:
    print(f"⚠️  Supabase init échouée : {e} — l'app démarre quand même mais crashera aux appels DB")
    supabase = DummySupabase()

def get_supabase() -> Client:
    """Retourne le client Supabase."""
    return supabase
