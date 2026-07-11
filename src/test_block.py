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

    # def test_eq(self):
    #     node = TextNode("This is a text node", TextType.TEXT)
    #     node2 = TextNode("This is a text node", TextType.TEXT)
    #     self.assertEqual(node, node2)
    
    # def test_not_eq(self):
    #     node = TextNode("This is a bold node", TextType.BOLD)
    #     node2 = TextNode("This is an italic node", TextType.ITALIC)
    #     self.assertNotEqual(node, node2)

    # def test_url_none_default(self):
    #     node = TextNode("This is a text node", TextType.TEXT)
    #     self.assertIs(node.url, "none")

    # def test_text(self):
    #     node = TextNode("This is a text node", TextType.TEXT)
    #     html_node = text_node_to_html_node(node)
    #     self.assertEqual(html_node.tag, None)
    #     self.assertEqual(html_node.value, "This is a text node")

    # def test_img(self):
    #     node = TextNode(text="alt text", text_type=TextType.IMAGE, url="assets/images")
    #     html_node = text_node_to_html_node(node)
    #     self.assertEqual(html_node.tag, "img")
    #     self.assertEqual(html_node.value, "")


if __name__ == "__main__":
    unittest.main()