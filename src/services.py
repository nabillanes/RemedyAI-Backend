from src.database import DBTextMessage, SessionLocal
from typing import List, Optional

# TODO: ini contoh, tolong dihapus nanti

class TextService:

    def create_message(self, text: str) -> dict:
        db = SessionLocal()
        try:
            db_message = DBTextMessage(
                original_text=text,
                processed_text=None,
                operation="raw"
            )
            db.add(db_message)
            db.commit()
            db.refresh(db_message)
            return {
                "id": db_message.id,
                "original_text": db_message.original_text,
                "processed_text": db_message.processed_text,
                "operation": db_message.operation,
                "created_at": db_message.created_at.isoformat()
            }
        finally:
            db.close()

    def delete_message(self, message_id: int) -> bool:
        db = SessionLocal()
        try:
            message = db.query(DBTextMessage).filter(DBTextMessage.id == message_id).first()
            if not message:
                return False
            db.delete(message)
            db.commit()
            return True
        finally:
            db.close()
        
    def make_greeting(self, name: str) -> str:
        greeting = f"Hello, {name}!"
        self._save_to_db(name, greeting, "greeting")
        return greeting
    
    def _save_to_db(self, original: str, processed: str, operation: str):
        db = SessionLocal()
        try:
            db_message = DBTextMessage(
                original_text=original,
                processed_text=processed,
                operation=operation
            )
            db.add(db_message)
            db.commit()
        finally:
            db.close()
    
    def get_all_messages(self) -> List[dict]:
        db = SessionLocal()
        try:
            messages = db.query(DBTextMessage).order_by(DBTextMessage.created_at.desc()).all()
            return [
                {
                    "id": msg.id,
                    "original_text": msg.original_text,
                    "processed_text": msg.processed_text,
                    "operation": msg.operation,
                    "created_at": msg.created_at.isoformat()
                }
                for msg in messages
            ]
        finally:
            db.close()
    
    def get_message_by_id(self, message_id: int) -> Optional[dict]:
        db = SessionLocal()
        try:
            message = db.query(DBTextMessage).filter(DBTextMessage.id == message_id).first()
            if message:
                return {
                    "id": message.id,
                    "original_text": message.original_text,
                    "processed_text": message.processed_text,
                    "operation": message.operation,
                    "created_at": message.created_at.isoformat()
                }
            return None
        finally:
            db.close()

text_service = TextService()

# TODO: mulai tulis kode dari sini
