import unittest

from splitnode import split_nodes_image, split_nodes_link, text_to_textnodes

from textnode import TextNode, TextType


class TestSplitNode(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("This is text with an ", TextType.PLAIN_TEXT),
            TextNode("image", TextType.IMAGE_TEXT, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.PLAIN_TEXT),
            TextNode("second image", TextType.IMAGE_TEXT, "https://i.imgur.com/3elNhQu.png"),
        ]

        self.assertListEqual(expected, new_nodes)

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.PLAIN_TEXT
        )
        new_nodes = split_nodes_link([node])
        expected = [TextNode("This is text with a link ", TextType.PLAIN_TEXT),
                    TextNode("to boot dev", TextType.LINK_TEXT,"https://www.boot.dev"),
                    TextNode(" and ", TextType.PLAIN_TEXT),
                    TextNode("to youtube", TextType.LINK_TEXT, "https://www.youtube.com/@bootdotdev")
                    ]

        self.assertListEqual(expected, new_nodes)

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expexted = [
            TextNode("This is ", TextType.PLAIN_TEXT),
            TextNode("text", TextType.BOLD_TEXT),
            TextNode(" with an ", TextType.PLAIN_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" word and a ", TextType.PLAIN_TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" and an ", TextType.PLAIN_TEXT),
            TextNode("obi wan image", TextType.IMAGE_TEXT, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.PLAIN_TEXT),
            TextNode("link", TextType.LINK_TEXT, "https://boot.dev"),
        ]

        self.assertListEqual(expexted, nodes)
