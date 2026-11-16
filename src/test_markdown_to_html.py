from pydoc import html
import unittest

from markdown_to_html import markdown_to_html_node

class TestMarkdownToHtml(unittest.TestCase):
    def test_paragraph(self):
        md = "Hello world"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,"<div><p>Hello world</p></div>")

    def test_bold(self):
        md = "Hello **world**"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,"<div><p>Hello <b>world</b></p></div>")

    def test_multiline_paragraph(self):
        md = "Hello world\nThis is another line"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,"<div><p>Hello world This is another line</p></div>")

    def test_heading(self):
        md = "### Hello world"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,"<div><h3>Hello world</h3></div>")

    def test_code_block(self):
        md = "```\nHello world\n```"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><pre><code>Hello world\n</code></pre></div>")

    def test_quote(self):
        md = "> This is a quote"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,"<div><blockquote>This is a quote</blockquote></div>")

    def test_multiline_quote(self):
        md = "> This is the first line\n> This is the second line"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,"<div><blockquote>This is the first line This is the second line</blockquote></div>")

    def test_unordered_list(self):
        md = "- Apples\n- Bananas\n- Oranges"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,"<div><ul><li>Apples</li><li>Bananas</li><li>Oranges</li></ul></div>")

    def test_order_list(self):
        md = "1. Apples\n2. Bananas\n3. Oranges"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,"<div><ol><li>Apples</li><li>Bananas</li><li>Oranges</li></ol></div>")

    def test_full_document(self):
        md = "# My Website\n\nWelcome to my **website**.\n\n- Apples\n- Bananas"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,"<div><h1>My Website</h1><p>Welcome to my <b>website</b>.</p><ul><li>Apples</li><li>Bananas</li></ul></div>")
