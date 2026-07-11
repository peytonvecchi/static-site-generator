from enum import Enum

class BlockType (Enum):
    PARAGRAH = "paragragh"
    HEADING = "heading"
    CODE = "code"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block_of_mardown_text: str) -> BlockType:
    if "#" in block_of_mardown_text[0]:
        print(BlockType.HEADING)
        return BlockType.HEADING
    if "```\n" and "```" in block_of_mardown_text[:4]:
        print(BlockType.CODE)
        return BlockType.CODE
    elif ">" in block_of_mardown_text[0]:
        print(BlockType.UNORDERED_LIST)
        return BlockType.UNORDERED_LIST
    elif "- " in block_of_mardown_text[:2]:
        print(BlockType.UNORDERED_LIST)
        return BlockType.UNORDERED_LIST
    elif "1. " in block_of_mardown_text[:3]:
        origin = 1
        list_of_mardown_text = block_of_mardown_text.splitlines()
        del list_of_mardown_text[0]
        print(list_of_mardown_text) # <-- debug
        for line in list_of_mardown_text:
            if line[1] == ".":
                current = int(line[0])
                pass
            else:
                break

            if current == origin + 1:
                origin = current
            else:
                break
        print(BlockType.ORDERED_LIST)
        return BlockType.ORDERED_LIST
    else:
        print(BlockType.PARAGRAH)
        return BlockType.PARAGRAH
    
# md = """1. hi
# 2. hey
# 3. wow
# """

# block_to_block_type(md)
    
