from textblob import TextBlob
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from readability import Readability
from typing import List

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

def analyze_sentiment(text: str) -> str:
    """Analyze the sentiment of given text."""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"

def extract_keywords(text: str, limit: int = 10) -> List[str]:
    """Extract top keywords from the text."""
    # Tokenize and convert to lower case
    words = word_tokenize(text.lower())
    
    # Remove stopwords and non-alphabetic tokens
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalpha() and word not in stop_words]
    
    # Get frequency distribution
    freq_dist = FreqDist(words)
    
    # Return top N keywords
    return [word for word, _ in freq_dist.most_common(limit)]

def calculate_readability(text: str) -> float:
    """Calculate readability score using Flesch Reading Ease."""
    try:
        r = Readability(text)
        return round(r.flesch().score, 2)
    except:
        return 0.0

def get_basic_stats(text: str) -> tuple[int, int]:
    """Get word count and sentence count."""
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    
    return len(words), len(sentences) 