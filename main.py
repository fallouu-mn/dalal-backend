# Point d'entrée principal de l'API DALAL
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

# Ajout du dossier courant au sys.path pour les imports relatifs
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from routers import auth, navettes, carte, pass_joj, resultats, assistant

# Initialisation de l'application FastAPI
app = FastAPI(
    title="DALAL API — JOJ Dakar 2026",
    description="Backend officiel de l'app visiteurs DALAL",
    version="1.0.0"
)

# Configuration CORS pour le frontend React (local + production Vercel + Render)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        # Développement local
        "http://localhost:5173", 
        "http://localhost:8080", 
        "http://localhost:8081",
        "http://127.0.0.1:5173", 
        "http://127.0.0.1:8080",
        "http://127.0.0.1:8081",
        # Production Vercel — Frontend DALAL
        "https://dakar-journey-companion-main.vercel.app",
        "https://dakar-journey-companion-main-fp86jhqeh.vercel.app",
        "https://dalal-joj.vercel.app",
        "https://dalal-joj2026.vercel.app",
        "https://dakar-journey-companion-main-dhz54p714.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusion des routers
app.include_router(auth.router, prefix="/api/auth", tags=["Authentification"])
app.include_router(navettes.router, prefix="/api/navettes", tags=["Navettes"])
app.include_router(carte.router, prefix="/api/carte", tags=["Carte & POI"])
app.include_router(pass_joj.router, prefix="/api/pass", tags=["Pass JOJ"])
app.include_router(resultats.router, prefix="/api/resultats", tags=["Résultats"])
app.include_router(assistant.router, prefix="/api/assistant", tags=["Dalal AI"])

@app.get("/")
async def racine():
    # Endpoint de vérification que l'API tourne
    return {
        "app": "DALAL API",
        "version": "1.0.0",
        "statut": "En ligne ✅",
        "event": "JOJ Dakar 2026"
    }
