from fastmcp import FastMCP
from src.models import Document, AnalysisResult
from src.analyzer import analyze_sentiment, extract_keywords, calculate_readability, get_basic_stats
from src.storage import DocumentStorage
from typing import List, Dict

# Initialize MCP and document storage
app = FastMCP("Document MCP")
storage = DocumentStorage()

@app.tool()
async def analyze_document(document_id: str) -> AnalysisResult:
    """Perform full analysis on a document."""
    document = storage.get_document(document_id)
    if not document:
        raise ValueError(f"Document with ID {document_id} not found")

    # Perform analysis
    sentiment = analyze_sentiment(document.content)
    keywords = await extract_keywords_tool(document.content)
    readability = calculate_readability(document.content)
    word_count, sentence_count = get_basic_stats(document.content)

    return AnalysisResult(
        sentiment=sentiment,
        keywords=keywords,
        readability_score=readability,
        word_count=word_count,
        sentence_count=sentence_count,
        document_id=document_id
    )

@app.tool()
async def get_sentiment(text: str) -> str:
    """Get sentiment analysis for any text."""
    return analyze_sentiment(text)

@app.tool()
async def extract_keywords_tool(text: str, limit: int = 10) -> List[str]:
    """Extract top keywords from text."""
    return extract_keywords(text, limit)

@app.tool()
async def add_document(title: str, content: str, metadata: Dict[str, str] = {}) -> str:
    """Add a new document to the storage."""
    return storage.add_document(title, content, metadata)

@app.tool()
async def search_documents(query: str) -> List[Document]:
    """Search for documents by content."""
    return storage.search_documents(query)

if __name__ == "__main__":
    app.run()
