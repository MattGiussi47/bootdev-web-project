from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    for i in range(1, 7):
        if block.startswith("#" * i + " "):

            return BlockType.HEADING

    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE

    lines = block.split("\n")
    is_quote = True

    for line in lines:
        if not line.startswith(">"):
            is_quote = False

    if is_quote:
        return BlockType.QUOTE

    is_unordered = True

    for line in lines:
        if not line.startswith("- "):
            is_unordered = False

    if is_unordered:
        return BlockType.UNORDERED_LIST

    is_ordered = True

    for i, line in enumerate(lines, start=1):
        if not line.startswith(f"{i}. "):
            is_ordered = False

    if is_ordered:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
