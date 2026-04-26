import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_SERVICE_KEY") or os.environ.get("SUPABASE_ANON_KEY")

if not url or not key:
    raise ValueError("SUPABASE_URL et SUPABASE_KEY doivent être définis dans le fichier .env")

# Initialisation du client Supabase
supabase: Client = create_client(url, key)
