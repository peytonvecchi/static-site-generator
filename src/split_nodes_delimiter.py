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
                
            
            
        
    
