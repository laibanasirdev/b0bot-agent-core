import os
from tavily import TavilyClient
from dotenv import load_dotenv # <--- Add this
from app.models.schemas import SearchResult
from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class SearchWorker:
    def __init__(self):
        # We'll set this key in your environment variables shortly
        api_key = os.getenv("TAVILY_API_KEY")
        self.client = TavilyClient(api_key=api_key)

    async def search_trends(self, topic: str):
        print(f"--- FETCHING LIVE DATA FOR: {topic} ---")
        
        # We ask Tavily for the top 3 most relevant results
        response = self.client.search(query=topic, max_results=3)
        
        results = []
        for res in response['results']:
            results.append(SearchResult(
                title=res['title'],
                url=res['url'],
                snippet=res['content']
            ))
        return results