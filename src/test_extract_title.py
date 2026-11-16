import unittest
from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_h1(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_whitespace(self):
        self.assertEqual(extract_title("#   Tolkien Fan Club   "), "Tolkien Fan Club")

    def test_no_h1(self):
        with self.assertRaises(Exception):
            extract_title("## Subtitle\nJust a paragraph")


if __name__ == "__main__":
    unittest.main()
