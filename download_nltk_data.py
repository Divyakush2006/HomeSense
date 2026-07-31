"""One-time download of the NLTK corpora the intent parser depends on.

Run once after installing requirements:
    python download_nltk_data.py
"""

import nltk

nltk.download("stopwords")
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("wordnet")
