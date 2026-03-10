from openai import OpenAI
from app.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def ask_chatbot(question: str) -> str:
    """
    Gửi câu hỏi tới OpenAI và nhận câu trả lời
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content