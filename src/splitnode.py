

import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(old_node)
            continue

        split_text = old_node.text.split(delimiter)

        if len(split_text) % 2 == 0:
            raise ValueError("Invalid Markdown syntax")

        for i, section in enumerate(split_text):
            if i % 2 == 0:
                new_nodes.append(TextNode(section, TextType.PLAIN_TEXT))
            else:
                new_nodes.append(TextNode(section, text_type))

    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(old_node)
            continue

        images = extract_markdown_images(old_node.text)
        current_text = old_node.text

        for alt_text, url in images:
            image_markdown = f"![{alt_text}]({url})"
            sections = current_text.split(image_markdown, 1)
            new_nodes.append(TextNode(sections[0], TextType.PLAIN_TEXT))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE_TEXT, url))
            current_text = sections[1]

        if current_text:
            new_nodes.append(TextNode(current_text, TextType.PLAIN_TEXT))

    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(old_node)
            continue

        links = extract_markdown_links(old_node.text)
        current_text = old_node.text

        for anchor_text, url in links:
            link_markdown = f"[{anchor_text}]({url})"
            sections = current_text.split(link_markdown, 1)
            new_nodes.append(TextNode(sections[0], TextType.PLAIN_TEXT))
            new_nodes.append(TextNode(anchor_text, TextType.LINK_TEXT, url))
            current_text = sections[1]

        if current_text:
          new_nodes.append(TextNode(current_text, TextType.PLAIN_TEXT))

    return new_nodes

def text_to_textnodes(text: str) -> list[TextNode]:
    nodes = [TextNode(text, TextType.PLAIN_TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD_TEXT)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC_TEXT)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE_TEXT)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes
