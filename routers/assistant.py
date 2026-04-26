from fastapi import APIRouter, Body
from services.ai_service import demander_dalal
from pydantic import BaseModel

router = APIRouter()

class MessageRequest(BaseModel):
    message: str
    langue: str = "fr"
    historique: list = []

@router.post("/message")
async def assistant_message(req: MessageRequest):
    reponse = await demander_dalal(
        message=req.message,
        langue=req.langue,
        historique=req.historique
    )
    return {"reponse": reponse}
