import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def process_query(query):
    tokens = word_tokenize(query)
    pos = pos_tag(tokens)