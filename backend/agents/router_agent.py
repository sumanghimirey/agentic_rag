import json
from typing import TypedDict, Optional, List
from langchain_openai import ChatOpenAI
from backend.prompts.router import ROUTER_PROMPT
from backend.config import settings


class AgentState(TypedDict):
    query: str
    history: List[str]
    route: Optional[str]
    reasoning: Optional[str]


llm = ChatOpenAI(
    model=settings.ROUTER_MODEL,
    temperature=0,
    api_key=settings.OPENAI_API_KEY
)


def router_node(state: AgentState) -> AgentState:
    prompt = ROUTER_PROMPT.replace("{query}", state["query"]).replace("{history}", "\n".join(state["history"]))


    response = llm.invoke(prompt)

    try:
        parsed = json.loads(response.content)
    except Exception as e:
        raise ValueError(f"Router output not valid JSON: {response.content}")

    return {
        **state,
        "route": parsed["route"],
        "reasoning": parsed["reasoning"]
    }