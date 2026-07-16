from htmlnode import HTMLNode
from functions import markdown_to_blocks, text_to_textnodes
from block import BlockType, block_to_block_type
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
from textnode import TextNode, TextType, text_node_to_html_node 

def get_heading_num(heading: str) -> int:
    if "######" in heading: return 6
    elif "#####" in heading: return 5
    elif "####" in heading: return 4
    elif "###" in heading: return 3
    elif "##" in heading: return 2
    elif "#" in heading: return 1
    else: raise Exception("# not in string provided to get_heading_num")

def get_value(block_string: str, block_type: BlockType) -> str:
    match block_type:
        case BlockType.HEADING:
            return block_string.replace("#", "").strip()
        case BlockType.QUOTE:
            return block_string.replace(">", "").strip()
        case BlockType.UNORDERED_LIST:
            return block_string.replace("- ", "").strip()
        case BlockType.ORDERED_LIST:
            return block_string[2:].strip()
        case BlockType.CODE:
            return block_string.replace("```", "").strip()
        
def text_to_children(text: str) -> list:
    print("INPUT STRING FOR TEXT NODES", text)
    text_nodes = text_to_textnodes(text)
    print("TEXT NODES", text_nodes)
    children = []
    for i in range(0, len(text_nodes)):
        child_html_node = text_node_to_html_node(text_nodes[i])
        children.append(child_html_node)
    print("children:", children)
    return children


def markdown_to_html_node(markdown: str) -> HTMLNode:
    markdown_blocks = markdown_to_blocks(markdown)
    for i in range(0, len(markdown_blocks)):
        markdown_blocks[i] = markdown_blocks[i].replace("\n", "")

    print("markdown block:", markdown_blocks)
    html_child_blocks = []
    for block in markdown_blocks:

        block_type = block_to_block_type(block)
        print("block type:", block_type)
        match block_type:
            case BlockType.HEADING:
                html_value = get_value(block_string=block, block_type=block_type) 
                html_heading_num = get_heading_num(block)
                html_children = text_to_children(html_value)
                html_node = ParentNode(tag=f"h{html_heading_num}", children=html_children)
            case BlockType.PARAGRAH:
                html_children = text_to_children(block)
                html_node = ParentNode(tag="p", children=html_children)
            case BlockType.QUOTE:
                html_value = get_value(block_string=block, block_type=block_type)
                html_children = text_to_children(block)
                html_node = ParentNode(tag="blockquote", children=html_children)
            case BlockType.UNORDERED_LIST | BlockType.ORDERED_LIST as list_type:
                list_children = block.splitlines()
                num_of_li_nodes = len(list_children)
                li_nodes = []
                for i in range(0, num_of_li_nodes):
                    list_children[i] = get_value(block_string=list_children[i], block_type=block_type)
                    list_children[i] = text_to_children(list_children[i])
                for i in range(0, num_of_li_nodes):
                    li_node = ParentNode(tag="li", children=list_children[i])
                    li_nodes.append(li_node)
                if list_type is BlockType.UNORDERED_LIST:
                    parent_node_tag = "ul"
                elif list_type is BlockType.ORDERED_LIST:
                    parent_node_tag = "ol"
                html_node = ParentNode(tag=parent_node_tag, children=li_nodes)
            case BlockType.CODE:
                print(r"%%%%%%%%%%%%%%%%%%%%%%%")
                html_value = get_value(block_string=block, block_type=block_type)
                text_node = TextNode(text=html_value, text_type=TextType.CODE)
                text_to_html = text_node_to_html_node(text_node)
                pre_html_node = ParentNode(tag="pre", children=text_to_html)
                html_node = ParentNode(tag="code", children=pre_html_node)
        html_child_blocks.append(html_node)
    html_parent_block = ParentNode(tag="div", children=html_child_blocks)
    print("HTML PARENT BLOCK\n\n", html_parent_block.to_html())

# TODO: MAKE MD8 PRINT OUT ALL NICE AND AS IT SHOULD BE, IT IS CURRENTLY WRONG!!!!!!!!!!!!!!!!!


md = """# Header

Paragraph

- List item
- List item

[link](https://link)

![image](https://image)

_italics_

**bold**"""

md1 = "# Header **this** is _italic_"

md2 = "paragraph is yeah plus **bold**"

md3 = "> Quote is _italic_"

md4 = "[link](https://link.net)"

md5 = "![image](https://image.com)"

md6 = "1. This\n2. That\n3. And the **bold**"

md7 = "```this is some _code_ **block**```"

md8 = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text `code` here

"""

markdown_to_html_node(md8)