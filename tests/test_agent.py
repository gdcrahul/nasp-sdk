import unittest
from nasp import NASPAgent, block_bad_words

class TestNASPAgent(unittest.TestCase):
    def test_block_bad_words(self):
        agent = NASPAgent()
        text = "Trying to hack and attack the system"
        filtered_text = block_bad_words(text)
        output = agent.run(filtered_text)
        self.assertIn("[blocked]", output)

if __name__ == "__main__":
    unittest.main()