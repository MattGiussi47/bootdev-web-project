import unittest
from blocktype import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):
    def test_heading(self):
        block = "# Hello World"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_code(self):
        block = "```\nprint('Hello')\n```"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.CODE)

    def test_quote(self):
        block = "> Hello World\n> This is a quote"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- Apples\n- Bananas\n- Oranges"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = "1. Apples\n2. Bananas\n3. Oranges"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.ORDERED_LIST)

    def test_paragraph(self):
        block = "normal paragraph"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)
