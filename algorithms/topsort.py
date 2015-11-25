from graphviz import Digraph
from collections import defaultdict


class Node(object):
    count = 1

    def __init__(self):
        self.id = Node.count
        Node.count += 1
        self.requires = set()

    def __repr__(self):
        return self.name

    @property
    def name(self):
        return 'node {0}'.format(self.id)


def topological_sort():
    graph = create_directed_graph()

    # Count incoming edges of each node
    incoming = defaultdict(int)
    for node in graph:
        for dependency in node.requires:
            incoming[dependency] += 1

    # Start with the node(s) that have no incoming edges
    start_nodes = [node for node in graph if incoming[node] == 0]

    topsorted = list()
    while start_nodes:
        node = start_nodes.pop()
        topsorted.append(node)

        for dependency in node.requires:
            incoming[dependency] -= 1 # Decrement no of incoming edges
            if incoming[dependency] == 0: # If that was the last one, its next
                start_nodes.append(dependency)

    return topsorted

def create_directed_graph():
    node1 = Node()
    node2 = Node()
    node3 = Node()

    node1.requires.add(node2)
    node3.requires.add(node2)
    return set([node1, node2, node3])

def render_graph(graph):
    dot = Digraph('directed_graph')
    for node in graph:
        dot.node(node.name)
        for dependency in node.requires:
            dot.edge(node.name, dependency.name)
    dot.render()
