from backend.graph.router_graph import build_router_graph
from backend.memory.conversation import save_message, load_conversation

# Fake session
session_id = "router-test"

# Seed conversation memory
save_message(session_id, "user", "What is pgvector?")
save_message(session_id, "assistant", "pgvector is a Postgres extension.")

# Load memory
history = load_conversation(session_id)

# Build graph
graph = build_router_graph()

# Test queries
queries = [
    "How does it compare to Pinecone?",
    "Explain vector databases",
    "What does our security policy say about PII?",
    "What happened in OpenAI yesterday?"
]

for q in queries:
    print("\n============================")
    print(f"Query: {q}")

    result = graph.invoke({
        "query": q,
        "history": history,
        "route": None,
        "reasoning": None
    })

    print("Route:", result["route"])
    print("Reasoning:", result["reasoning"])