import httpx
import os
from dotenv import load_dotenv

load_dotenv()

LIBRE_TRANSLATE_URL = os.getenv("LIBRE_TRANSLATE_URL", "https://libretranslate.com/translate")

PHRASES_WOLOF = {
    "Bienvenue": "Dalal ak jamm",
    "Bonjour": "Salaam aleekum",
    "Merci": "Jërejëf",
    "Où est": "Fan la nekk",
    "Stade": "Stade bi",
    "Transport": "Transport bi",
    "Navette": "Car bi",
    "Restaurant": "Restorant bi",
}

async def traduire(texte: str, langue_source: str, langue_cible: str):
    # Gestion Wolof et Mandingue via dictionnaire (simulation)
    if langue_cible in ["wo", "man"]:
        # Retourne la phrase du dictionnaire si elle existe, sinon le texte original
        return PHRASES_WOLOF.get(texte, texte)
    
    # Appel à LibreTranslate pour les autres langues
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                LIBRE_TRANSLATE_URL,
                data={
                    "q": texte,
                    "source": langue_source,
                    "target": langue_cible,
                    "format": "text"
                }
            )
            if response.status_code == 200:
                return response.json().get("translatedText", texte)
    except Exception as e:
        print(f"Erreur traduction: {e}")
    
    return texte
