from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.children = children
        self.props = props
        
    def to_html(self):
        if not self.tag:
            raise  #how to properly raise a value error
        

# class LeafNode(HTMLNode):
#     def __init__(self, tag, value, props=None):
#         super().__init__(tag, value, props)
#         self.tag = tag
#         self.value = value
#         self.props = props