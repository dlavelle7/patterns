class Node(object):
    count = 1

    def __init__(self):
        self.id = Node.count
        self.parent = None
        self.children = set()
        Node.count += 1

    def __repr__(self):
        return "Node: {0}".format(self.id)

    def add_children(self, children):
        for child in children:
            self.add_child(child)

    def add_child(self, child):
        child.parent = self
        self.children.add(child)

def create_balanced_tree(levels=4, node=None):
    root = None
    if not node:
        node = Node()
        root = node
    if levels > 0:
        node.add_children(set([Node(), Node()]))
        for child in node.children:
            create_balanced_tree(levels - 1, child)
    return root

def depth_first_search(find_node):
    import ipdb; ipdb.set_trace()
    root = create_balanced_tree()

def breadth_first_search(find_node):
    import ipdb; ipdb.set_trace()
    root = create_balanced_tree()

# TODO: pygraphviz
