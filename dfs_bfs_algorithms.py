class Node(object):
    def __init__(self, id):
        self.id = id
        self.parent = None
        self.children = set()

    def add_children(self, children):
        for child in children:
            self.add_child(child)

    def add_child(self, child):
        child.parent = self
        self.children.add(child)

def create_graph():
    graph = set()
    return graph

def depth_first_search():
    graph = create_graph()

def breadth_first_search():
    graph = create_graph()
