from typing import Annotated, TypedDict, List
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver # <--- Add this
from app.services.search_service import SearchWorker
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# Initialize memory
memory = MemorySaver()
# 1. Define the State (The Notebook)
class AgentState(TypedDict):
    topic: str
    results: List[dict]
    analysis: str

# 2. Initialize Workers
search_worker = SearchWorker()
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 3. Researcher Node (The Senses)
async def research_node(state: AgentState):
    print(f"--- RESEARCHING: {state['topic']} ---")
    raw_results = await search_worker.search_trends(state['topic'])
    return {"results": [r.dict() for r in raw_results]}

# 4. Writer Node (The Brain)
async def writer_node(state: AgentState):
    print(f"--- BRAIN ANALYZING: {state['topic']} ---")
    
    context = "\n\n".join([f"Source: {r['title']}\nContent: {r['snippet']}" for r in state["results"]])
    
    system_prompt = (
        "You are B0Bot, a professional Research Assistant. "
        "Summarize the following search results into a concise, 3-sentence insight."
    )
    user_prompt = f"Topic: {state['topic']}\n\nSearch Results:\n{context}"
    
    response = await llm.ainvoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ])
    
    return {"analysis": response.content}

# 5. The Map (The Workflow)
workflow = StateGraph(AgentState)

workflow.add_node("researcher", research_node)
workflow.add_node("writer", writer_node)

workflow.add_edge(START, "researcher")
workflow.add_edge("researcher", "writer")
workflow.add_edge("writer", END)

app_brain = workflow.compile(checkpointer=memory)
