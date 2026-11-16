from markdown_blocks import markdown_to_blocks

from blocktype import block_to_block_type, BlockType

from htmlnode import ParentNode, LeafNode

from textnode import text_node_to_html_node

from splitnode import text_to_textnodes

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []

    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)

    return children


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            block = block.replace("\n", " ")
            paragraph_children = text_to_children(block)
            paragraph = ParentNode("p", paragraph_children)
            children.append(paragraph)

        elif block_type == BlockType.HEADING:
            level = len(block) - len(block.lstrip("#"))
            tag = f"h{level}"
            content = block[level + 1:]
            heading_children = text_to_children(content)
            heading = ParentNode(tag, heading_children)
            children.append(heading)

        elif block_type == BlockType.CODE:
            content = block[4:-3]
            code_node = LeafNode("code", content)
            pre_node = ParentNode("pre",[code_node])
            children.append(pre_node)

        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            quote_lines = []

            for line in lines:
                cleaned_line = line.lstrip(">").strip()
                quote_lines.append(cleaned_line)

            content = " ".join(quote_lines)

            quote_children = text_to_children(content)

            quote = ParentNode("blockquote", quote_children)
            children.append(quote)

        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            list_items = []

            for line in lines:
                content = line[2:]
                item_children = text_to_children(content)

                li = ParentNode("li", item_children)
                list_items.append(li)

            ul = ParentNode("ul", list_items)
            children.append(ul)

        elif block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            list_items = []

            for line in lines:
                content = line.split(". ",1)[1]
                text_nodes = text_to_textnodes(content)
                item_children = []

                for node in text_nodes:
                    html_node = text_node_to_html_node(node)
                    item_children.append(html_node)

                li = ParentNode("li", item_children)
                list_items.append(li)

            ol = ParentNode("ol", list_items)
            children.append(ol)



    return ParentNode("div", children)
