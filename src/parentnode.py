from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=""):
        self.tag = tag
        self.children = children
        self.props = props
        
    def to_html(self):
        if not self.tag:raise ValueError("tag is None")
        if not self.children: raise ValueError ("children is None")
        else:
            str=""
            if isinstance(self.children, list):
                for child in self.children:
                    str += child.to_html()
            else:
                str += self.children.to_html()
            return f"<{self.tag}{self.props}>{str}</{self.tag}>".replace("\n", "")
        
    def __repr__(self):
        return f"ParentNode, tag: {self.tag}, children: {self.children}, props {self.props}"