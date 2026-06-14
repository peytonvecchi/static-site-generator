class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        str = ''
        for key, value in self.props.items():
            str += f' {key}="{value}"'
        print(str)
        return str

    def __repr__(self):
        print(f"HTMLNode, tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}")

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
