from fastapi import APIRouter
from pydantic import BaseModel

from chatbot.services.chatbot_service import ask_chatbot

router = APIRouter(prefix="/chatbot", tags=["chatbot"])


class ChatRequest(BaseModel):
    question: str


@router.post("/ask")
def ask_ai(data: ChatRequest):
    """
    API hỏi chatbot
    """

    answer = ask_chatbot(data.question)

    return {
        "question": data.question,
        "answer": answer
    }