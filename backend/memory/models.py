import uuid
from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ConversationMemory(Base):
    __tablename__ = "conversation_memory"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id = Column(String(100), index=True)
    role = Column(String(20))  # user / assistant
    content = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())