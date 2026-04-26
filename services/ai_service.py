# Service de simulation AI pour le Hackathon
# Pas besoin d'API Anthropic ou de clé API ici
import os

async def demander_dalal(message: str, langue: str = "fr", historique: list = []):
    """
    Simule une réponse de l'IA Dalal pour le hackathon.
    Analyse quelques mots clés pour donner une réponse 'intelligente'.
    """
    msg = message.lower()
    
    if "bonjour" in msg or "salut" in msg:
        return "Asalaa maalekum ! Je suis Dalal, votre assistant pour les JOJ Dakar 2026. Comment puis-je vous aider aujourd'hui ? 🇸🇳✨"
    
    if "stade" in msg or "diamniadio" in msg:
        return "Le Stade Abdoulaye Wade se situe à Diamniadio. Vous pouvez y aller via le TER ou avec les navettes officielles JOJ qui partent toutes les 15 minutes du centre-ville ! 🏟️🚌"
    
    if "manger" in msg or "restaurant" in msg:
        return "Je vous recommande vivement de goûter un bon Thiébou Djeun au marché Kermel ou aux Almadies. C'est le plat national ! 🥘🇸🇳"
    
    if "navette" in msg or "transport" in msg:
        return "Le réseau de navettes JOJ couvre tous les sites de compétition. Votre Pass numérique vous donne un accès gratuit illimité ! 🚌🎟️"
    
    # Réponse par défaut
    return f"C'est une excellente question concernant '{message}' ! En tant qu'assistant des JOJ Dakar 2026, je peux vous confirmer que tout est mis en œuvre pour votre confort. N'hésitez pas à consulter la carte pour plus de détails ! 🇸🇳✨"
