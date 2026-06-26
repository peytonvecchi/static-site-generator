import unittest
from textnode import TextNode, TextType
from functions import text_to_nodes

class TestTextNode(unittest.TestCase):
    def test_text_to_nodes(self):
        text_node = TextNode("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)", text_type=TextType.TEXT)
        result = text_to_nodes(text_node)
        self.assertEqual(result, result)