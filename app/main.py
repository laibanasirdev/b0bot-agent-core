from fastapi import FastAPI
from app.agent.graph import app_brain # Import our compiled brain
from app.models.schemas import SearchResult # Importing your Blueprint
from app.services.search_service import SearchWorker # Importing your Specialist

app = FastAPI(title="B0Bot Agent Core")
worker = SearchWorker()

@app.get("/")
async def home():
    return {"message": "B0Bot is learning structure!"}

@app.get("/test-search")
async def test_search(query: str):
    # We ask our specialist to do the work
    results = await worker.search_trends(query)
    return {"results": results}

@app.get("/analyze")
async def analyze(topic: str, thread_id: str = "default_user"):
    # We create a config object to tell LangGraph which memory 'thread' to use
    config = {"configurable": {"thread_id": thread_id}}
    
    initial_state = {"topic": topic, "results": [], "analysis": ""}
    
    # We pass the config into ainvoke
    final_output = await app_brain.ainvoke(initial_state, config=config)
    
    return {
        "status": "success",
        "thread_id": thread_id,
        "analysis_report": {
            "summary": final_output["analysis"],
            "sources": len(final_output["results"])
        }
    }


    @app.get("/download-docs")
async def download_docs():
    pdf_buffer = generate_project_pdf()
    return StreamingResponse(
        pdf_buffer, 
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=B0Bot_Documentation.pdf"}
    )