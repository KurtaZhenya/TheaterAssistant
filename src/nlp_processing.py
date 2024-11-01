# src/nlp_processing.py
import spacy

class NLPProcessor:
    def __init__(self):
        self.nlp = spacy.load("ru_core_news_md")

    def extract_entities(self, text):
        doc = self.nlp(text)
        return [(ent.text, ent.label_) for ent in doc.ents]

