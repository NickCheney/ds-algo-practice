from anytree import Node, RenderTree
from anytree.exporter import UniqueDotExporter

class TreePlotter:
    def __init__(self, root: Node):
        self.root = root
    
    def print_tree(self):
        print(RenderTree(self.root))

    def plot_tree(self, name: str):
        UniqueDotExporter(self.root).to_picture(name)