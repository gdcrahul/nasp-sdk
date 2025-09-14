# tests/test_agent.py
import unittest
from nasp import NASPAgent, block_bad_words

class TestNASPAgent(unittest.TestCase):
    def setUp(self):
        self.agent = NASPAgent()

    def test_block_bad_words(self):
        # profanity should be blocked
        text = "Trying to hack and attack the system"
        response = self.agent.safe_ask(text)
        self.assertIn("[blocked]", response)

    def test_block_sensitive(self):
        # sensitive (password) should be blocked
        text2 = "My password is 1234"
        response2 = self.agent.safe_ask(text2)
        self.assertIn("[blocked]", response2)

    def test_allows_safe(self):
        # safe text should pass
        safe = "Tell me a fun fact about space."
        resp = self.agent.safe_ask(safe)
        self.assertIn("safe response", resp.lower())

    def test_legacy_function(self):
        # ensure block_bad_words legacy helper works
        self.assertTrue(block_bad_words("contact me at user@example.com"))
        self.assertFalse(block_bad_words("hello how are you"))

if __name__ == "__main__":
    unittest.main()
