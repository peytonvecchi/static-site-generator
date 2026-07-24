from htmlnode import HTMLNode
from functions import markdown_to_blocks, text_to_textnodes
from block import BlockType, block_to_block_type
from htmlnode import HTMLNode
from parentnode import ParentNode
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
    text_nodes = text_to_textnodes(text)
    children = []
    for i in range(0, len(text_nodes)):
        child_html_node = text_node_to_html_node(text_nodes[i])
        children.append(child_html_node)
    return children


def markdown_to_html_node(markdown: str) -> HTMLNode:
    markdown_blocks = markdown_to_blocks(markdown)
    html_child_blocks = []
    for block in markdown_blocks:

        block_type = block_to_block_type(block)
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
                html_children = text_to_children(html_value)
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
                html_value = get_value(block_string=block, block_type=block_type)
                text_node = TextNode(text=html_value, text_type=TextType.CODE)
                text_to_html = text_node_to_html_node(text_node)
                html_node = ParentNode(tag="pre", children=text_to_html)
        html_child_blocks.append(html_node)
    html_parent_block = ParentNode(tag="div", children=html_child_blocks)
    
    return html_parent_block