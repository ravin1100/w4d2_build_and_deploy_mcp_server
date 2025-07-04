# Document Analyzer MCP Server

A powerful Message Control Protocol (MCP) server that provides comprehensive text analysis capabilities for documents. This server enables document storage, retrieval, and advanced text analysis including sentiment analysis, keyword extraction, and readability metrics.

## 🌟 Features

### Document Management
- In-memory document storage with unique IDs
- Metadata support for document categorization
- Full-text search capabilities
- Sample documents included for testing

### Text Analysis
- **Sentiment Analysis**: Determines if text is positive, negative, or neutral
- **Keyword Extraction**: Identifies most important terms using NLP
- **Readability Scoring**: Calculates Flesch Reading Ease score
- **Text Statistics**: Provides word count and sentence count
- **Metadata Management**: Support for custom document metadata

## 🛠️ Technical Requirements

- Python >= 3.12
- Operating System: Windows/Linux/MacOS

## 📦 Dependencies

Core Dependencies:
- `fastmcp`: MCP server framework
- `textblob`: Natural language processing and sentiment analysis
- `nltk`: Advanced text processing and analysis
- `py-readability-metrics`: Text readability scoring
- `pydantic`: Data validation and serialization

## 🚀 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd document-analyzer-mcp
```

2. Install dependencies using uv (recommended):
```bash
uv pip install .
```

## 🏃‍♂️ Running the Server

Start the server:
```bash
python main.py
```

The server will initialize with sample documents and be ready to accept MCP requests.

## 📚 Available MCP Tools

### 1. Document Management Tools

#### `add_document`
- **Purpose**: Adds a new document to the storage system
- **Functionality**: 
  - Creates a unique ID for the document
  - Stores document content, title, and metadata
  - Supports custom metadata for categorization
  - Returns the document ID for future reference

#### `search_documents`
- **Purpose**: Searches through stored documents
- **Functionality**:
  - Performs case-insensitive search
  - Searches both content and title
  - Returns matching documents with all metadata
  - Supports partial word matches

### 2. Text Analysis Tools

#### `analyze_document`
- **Purpose**: Comprehensive document analysis
- **Functionality**:
  - Sentiment analysis (positive/negative/neutral)
  - Keyword extraction
  - Readability scoring
  - Word and sentence counting
  - Returns complete analysis results

#### `get_sentiment`
- **Purpose**: Standalone sentiment analysis
- **Functionality**:
  - Analyzes emotional tone of text
  - Returns sentiment classification
  - Works with any text input
  - Quick analysis without storage

#### `extract_keywords`
- **Purpose**: Key term extraction
- **Functionality**:
  - Identifies important words and phrases
  - Removes common stop words
  - Configurable number of keywords
  - Frequency-based analysis

## 📁 Project Structure

```
document-analyzer-mcp/
├── main.py              # Server entry point and MCP tools
├── src/
│   ├── analyzer.py      # Text analysis functions
│   ├── models.py        # Data models
│   ├── storage.py       # Document storage
│   └── data/
│       └── samples/     # Sample documents
├── tests/               # Test files
├── pyproject.toml       # Project configuration
└── README.md           # Documentation
```

## 🔍 Use Cases

### Content Analysis
- Analyze customer feedback sentiment
- Extract key topics from articles
- Assess content readability
- Generate document insights

### Document Management
- Organize documents with metadata
- Build searchable document collections
- Track document metrics
- Maintain document categories

### Text Processing
- Quick sentiment checks
- Automated keyword tagging
- Content optimization
- Readability assessment

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

[Add your license information here]
