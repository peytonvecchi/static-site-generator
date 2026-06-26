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
        return str

    def __repr__(self):
        print(f"HTMLNode, tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}")
