# src/agent.py
import spacy
import requests
from datetime import datetime

class TheaterAssistant:
    def __init__(self, database_api_url):
        self.database_api_url = database_api_url
        self.nlp = spacy.load("ru_core_news_md")

    def analyze_intent(self, text):
        if "расписание" in text or "когда" in text:
            return "schedule"
        elif "рекомендация" in text or "посоветуй" in text:
            return "recommendation"
        return "unknown"

    def get_schedule(self, date=None):
        params = {"date": date} if date else {}
        response = requests.get(f"{self.database_api_url}/schedule", params=params)
        return response.json() if response.status_code == 200 else "Ошибка при получении расписания."

    def recommend_show(self, preferences):
        response = requests.get(f"{self.database_api_url}/recommend", params=preferences)
        return response.json() if response.status_code == 200 else "Ошибка при получении рекомендаций."

