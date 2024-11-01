# tests/test_agent.py
import unittest
from src.agent import TheaterAssistant
from src.config import DATABASE_API_URL

class TestTheaterAssistant(unittest.TestCase):
    def setUp(self):
        self.agent = TheaterAssistant(DATABASE_API_URL)

    def test_analyze_intent(self):
        intent = self.agent.analyze_intent("Когда будет спектакль?")
        self.assertEqual(intent, "schedule")

    def test_get_schedule(self):
        result = self.agent.get_schedule("2023-11-02")
        self.assertTrue(isinstance(result, dict))  # Предполагается, что ответ будет JSON

if __name__ == "__main__":
    unittest.main()

