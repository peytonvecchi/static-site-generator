from enum import Enum

class BlockType (Enum):
    PARAGRAH = "paragragh"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block_of_mardown_text: str) -> BlockType:
    if "#" in block_of_mardown_text[0]:
        return BlockType.HEADING
    elif "```" in block_of_mardown_text[:4] and "```" in block_of_mardown_text[-3:]:
        return BlockType.CODE
    elif ">" in block_of_mardown_text[0]:
        list_of_mardown_text = block_of_mardown_text.splitlines()
        for line in list_of_mardown_text:
            if line[0] == ">":
                continue
            else:
                return BlockType.PARAGRAH
        return BlockType.QUOTE
    elif "- " in block_of_mardown_text[:2]:
        list_of_mardown_text = block_of_mardown_text.splitlines()
        for line in list_of_mardown_text:
            if line[:2] == "- ":
                continue
            else: 
                return BlockType.PARAGRAH
        return BlockType.UNORDERED_LIST
    elif "1. " in block_of_mardown_text[:3]:
        origin = 1
        list_of_mardown_text = block_of_mardown_text.splitlines()
        del list_of_mardown_text[0]
        for line in list_of_mardown_text:
            if line[1] == ".":
                current = int(line[0])
            else:
                return BlockType.PARAGRAH

            if current == origin + 1:
                origin = current
            else:
                return BlockType.PARAGRAH
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAH
    
# md = """1. hi
# 2. hey
# 3. wow
# """

# block_to_block_type(md)
    
