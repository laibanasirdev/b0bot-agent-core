from pydantic import BaseModel, Field
from typing import List, Optional

# This is the "Blueprint" for a search result
class SearchResult(BaseModel):
    title: str
    url: str
    snippet: str

# This is the "Blueprint" for the final AI Analysis
class TrendAnalysis(BaseModel):
    topic: str
    summary: str = Field(description="A 2-sentence overview of the trend")
    key_points: List[str] = Field(description="List of 3 main takeaways")
    confidence_score: float = Field(default=0.0, ge=0.0, le=1.0)