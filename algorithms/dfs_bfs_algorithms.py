from collections import deque

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

def create_balanced_tree(levels=3, node=None):
    if not node:
        Node.count = 1
        node = Node()
    if levels > 0:
        node.add_children(set([Node(), Node()]))
        for child in node.children:
            create_balanced_tree(levels - 1, child)
    return node

def depth_first_search(find_node):
    root = create_balanced_tree()

    def recursive_search(node):
        if node.id == find_node:
            return node
        for child in node.children:
            result = recursive_search(child)
            if result:
                return result

    return recursive_search(root)

def breadth_first_search(find_node):
    root = create_balanced_tree()
    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        if node.id == find_node:
            return node
        for child in node.children:
            queue.append(child)

# TODO: Select tree levels from dfs/bfs functions
# TODO: pygraphviz
# TODO: timing (timeit) comparison
