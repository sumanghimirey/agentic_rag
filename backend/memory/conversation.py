from typing import List
from backend.db import SessionLocal
from backend.memory.models import ConversationMemory

def save_message(session_id: str, role: str, content: str):
    db = SessionLocal()
    try:
        msg = ConversationMemory(
            session_id=session_id,
            role=role,
            content=content
        )
        db.add(msg)
        db.commit()
    finally:
        db.close()


def load_conversation(session_id: str, limit: int = 10) -> List[str]:
    db = SessionLocal()
    try:
        messages = (
            db.query(ConversationMemory)
            .filter(ConversationMemory.session_id == session_id)
            .order_by(ConversationMemory.created_at.asc())
            .limit(limit)
            .all()
        )

        return [f"{m.role}: {m.content}" for m in messages]
    finally:
        db.close()