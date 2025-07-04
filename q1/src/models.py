from datetime import datetime
from typing import List, Dict, Optional
from pydantic import BaseModel

class Document(BaseModel):
    id: str
    content: str
    title: str
    created_at: datetime
    metadata: Dict[str, str]

class AnalysisResult(BaseModel):
    sentiment: str
    keywords: List[str]
    readability_score: float
    word_count: int
    sentence_count: int
    document_id: Optional[str] = None 