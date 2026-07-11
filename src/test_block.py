import unittest
from block import BlockType, block_to_block_type

class TestBlock(unittest.TestCase):
    def test_heading(self):
        md = "#### heading"
        output = block_to_block_type(md)
        self.assertEqual(BlockType.HEADING, output)

    def test_ordered_list(self):
        ordered_list = "1. first\n2. second\n3. third\n4. fourth\n5. fifth"
        paragraph = "1. first\n3. second\n4. third"
        output = block_to_block_type(ordered_list)
        output1 = block_to_block_type(paragraph)
        self.assertEqual(BlockType.ORDERED_LIST, output)
        self.assertEqual(BlockType.PARAGRAH, output1)
    
    def test_unordered_list(self):
        md = "- first\n- second\n- third"
        output = block_to_block_type(md)
        self.assertEqual(BlockType.UNORDERED_LIST, output)

    def test_code(self):
        md = "```\n print('Hello World!')```"
        ouput = block_to_block_type(md)
        self.assertEqual(BlockType.CODE, ouput)

    def test_quote(self):
        md = ">first\n> second\n>third"
        output = block_to_block_type(md)
        self.assertEqual(BlockType.QUOTE, output)

    def test_paragraph(self):
        md = "This is a paragraph"
        output = block_to_block_type(md)
        self.assertEqual(BlockType.PARAGRAH, output)

if __name__ == "__main__":
    unittest.main()