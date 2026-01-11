from langgraph.graph import StateGraph, END
from backend.agents.router_agent import router_node, AgentState


def build_router_graph():
    graph = StateGraph(AgentState)

    graph.add_node("router", router_node)

    graph.set_entry_point("router")

    graph.add_conditional_edges(
        "router",
        lambda state: state["route"],
        {
            "LLM_ONLY": END,
            "FOLLOW_UP": END,
            "INTERNAL_RAG": END,
            "WEB_SEARCH": END,
            "HYBRID": END,
        }
    )

    return graph.compile()