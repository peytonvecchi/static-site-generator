import unittest
from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="a", value="test3", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_none_values(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_not_eq(self):
        node = HTMLNode(tag="p")
        node2 = HTMLNode(tag="h1")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()