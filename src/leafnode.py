from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)
        self.tag = tag
        self.value = value
        self.props = props
    
    def to_html(self):
        props_in_html = ""
        if self.value == None: raise ValueError
        if self.tag == None: return self.value
        else: 
            if self.props:
                props_in_html += self.props_to_html()
        return f"<{self.tag}{props_in_html}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        print(f"LeafNode, tag: {self.tag}, value: {self.value}, props {self.props}")