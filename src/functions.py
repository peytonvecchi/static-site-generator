import re
from textnode import TextNode, TextType

#delimiter = **, text_type = TextType.BOLD
def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    return_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            return_list.append(node)
        else:
            split_words = node.text.split(delimiter)
            if len(split_words) % 2 == 0:
                raise Exception("Invalid Markdown syntax. Make sure to have an opening and closing delimiter.")
            for i in range(0, len(split_words)):
                if i % 2 == 1:
                    split_words[i] = TextNode(split_words[i], text_type)
                else:
                    split_words[i] = TextNode(split_words[i], TextType.TEXT)
            return_list.extend(split_words)
    return return_list

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return matches

# old_nodes = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", text_type=TextType.TEXT)
def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        images = extract_markdown_images(original_text)

        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        links = extract_markdown_links(original_text)

        if len(links) == 0:
            new_nodes.append(old_node)
            continue

        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes

def text_to_textnodes(text):
    text_node = TextNode(text, text_type=TextType.TEXT)
    nodes = split_nodes_delimiter([text_node], delimiter="**", text_type=TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, delimiter="```", text_type=TextType.CODE)
    nodes = split_nodes_delimiter(nodes, delimiter="_", text_type=TextType.ITALIC)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    if nodes[len(nodes) - 1].text == "":
        nodes.pop()

    return nodes

def markdown_to_blocks(markdown):
    blocks = []
    blocks = markdown.split("\n\n")
    for i in range(0, len(blocks)):
        blocks[i] = blocks[i].strip()
        if blocks[i] == '':
            blocks.remove(blocks[i])
    return blocks