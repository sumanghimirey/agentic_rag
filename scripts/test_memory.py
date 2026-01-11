import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from backend.db import engine
from backend.memory.models import Base
from backend.memory.conversation import save_message, load_conversation

# Initialize database tables (only creates if they don't exist)
Base.metadata.create_all(bind=engine)

save_message("test-session", "user", "What is pgvector?")
save_message("test-session", "assistant", "pgvector is a Postgres extension.")

print(load_conversation("test-session"))