from pydantic import BaseModel
from typing import Optional

# TODO: ini contoh, tolong dihapus nanti

class TextMessage(BaseModel):
    text: str

class TextResponse(BaseModel):
    message: str
    original_text: Optional[str] = None
    processed_text: Optional[str] = None

# TODO: mulai tulis kode dari sini
