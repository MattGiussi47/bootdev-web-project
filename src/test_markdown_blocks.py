import unittest
from markdown_blocks import markdown_to_blocks

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
# My Heading

This is a paragraph.

- First item
- Second item
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            ["# My Heading",
                "This is a paragraph.",
                "- First item\n- Second item"],
        )
