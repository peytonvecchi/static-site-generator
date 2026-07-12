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
        
def text_to_children(text: str) -> list:
    text_nodes = text_to_textnodes(text)
    children = []
    for i in range(0, len(text_nodes)):
        child_html_node = text_node_to_html_node(text_nodes[i])
        children.append(child_html_node)
    return children


def markdown_to_html_node(markdown: str) -> HTMLNode:
    markdown_blocks = markdown_to_blocks(markdown)
    print("markdown block:", markdown_blocks)
    html = ""
    for block in markdown_blocks:

        block_type = block_to_block_type(block)
        print("block type:", block_type)
        match block_type:
            case BlockType.HEADING:
                html_value = get_value(block_string=block, block_type=block_type) 
                html_heading_num = get_heading_num(block)
                html_children = text_to_children(html_value)
                print("val:", html_value)
                print("head", html_heading_num)
                html_node = ParentNode(tag=f"h{html_heading_num}", children=html_children, props=None)

        
            
        


md = """# Header

Paragraph

- List item
- List item

[link](https://link)

![image](https://image)

_italics_

**bold**"""

md1 = "# Header **this** is _italic_"

markdown_to_html_node(md1)