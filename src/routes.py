from fastapi import APIRouter, HTTPException
from src.models import TextMessage, TextResponse
from src.services import text_service

router = APIRouter()

# TODO: ini contoh, tolong dihapus nanti

@router.post("/messages/create", response_model=TextResponse)
async def create_message(text_message: TextMessage):
    result = text_service.create_text(text_message.text)
    return TextResponse(
        message="Text added to database",
        original_text=result["original_text"],
        processed_text=result["processed_text"]
    )

@router.delete("/messages/{message_id}")
async def delete_message(message_id: int):
    success = text_service.delete_message(message_id)
    if not success:
        raise HTTPException(status_code=404, detail="Message not found")
    return {"message": f"Message with id {message_id} deleted successfully."}

@router.get("/messages")
async def get_all_messages():
    messages = text_service.get_all_messages()
    return {"messages": messages, "count": len(messages)}

@router.get("/messages/{message_id}")
async def get_message(message_id: int):
    message = text_service.get_message_by_id(message_id)
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    return message

# TODO: mulai tulis kode dari sini
