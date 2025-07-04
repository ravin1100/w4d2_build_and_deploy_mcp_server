from datetime import datetime
import uuid
from typing import List, Optional, Dict
from .models import Document

class DocumentStorage:
    def __init__(self):
        self.documents: Dict[str, Document] = {}
        self._initialize_sample_documents()

    def add_document(self, title: str, content: str, metadata: Optional[Dict[str, str]] = None) -> str:
        """Add a new document and return its ID."""
        doc_id = str(uuid.uuid4())
        self.documents[doc_id] = Document(
            id=doc_id,
            title=title,
            content=content,
            created_at=datetime.now(),
            metadata=metadata or {}
        )
        return doc_id

    def get_document(self, doc_id: str) -> Optional[Document]:
        """Get a document by ID."""
        return self.documents.get(doc_id)

    def search_documents(self, query: str) -> List[Document]:
        """Search documents by content."""
        query = query.lower()
        return [
            doc for doc in self.documents.values()
            if query in doc.content.lower() or query in doc.title.lower()
        ]

    def _initialize_sample_documents(self):
        """Initialize with sample documents."""
        samples = [
            {
                "title": "The Benefits of AI",
                "content": """Artificial Intelligence has revolutionized various industries, from healthcare to transportation. 
                AI systems can process vast amounts of data quickly and accurately, leading to better decision-making and improved efficiency. 
                Machine learning algorithms continue to evolve, making AI more sophisticated and capable.""",
                "metadata": {"category": "technology", "author": "John Smith"}
            },
            {
                "title": "Climate Change Impact",
                "content": """Global temperatures continue to rise at an alarming rate, causing severe weather patterns and environmental damage. 
                The melting of polar ice caps threatens coastal regions and wildlife. Immediate action is required to reduce carbon emissions 
                and prevent further damage to our planet.""",
                "metadata": {"category": "environment", "author": "Sarah Johnson"}
            },
            {
                "title": "Healthy Living Guide",
                "content": """Regular exercise and a balanced diet are essential for maintaining good health. 
                Studies show that 30 minutes of daily physical activity can significantly reduce the risk of chronic diseases. 
                Additionally, consuming a variety of fruits and vegetables provides necessary nutrients for optimal health.""",
                "metadata": {"category": "health", "author": "Dr. Michael Brown"}
            }
        ]

        for sample in samples:
            self.add_document(
                title=sample["title"],
                content=sample["content"],
                metadata=sample["metadata"]
            ) 