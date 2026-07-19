import unittest
from main import extract_title

class TestTextNode(unittest.TestCase):

    def test_extract_title(self):
        markdown = "# Header\n\nSome text"
        title = extract_title(markdown)
        self.assertEqual(title, "Header")


if __name__ == "__main__":
    unittest.main()