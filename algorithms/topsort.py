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
    incoming = defaultdict(int)
    for node in graph:
        incoming[node]
        for dependency in node.requires:
            incoming[dependency] += 1

    start_nodes = [node for node in incoming if not incoming[node]]

    topsorted = list()
    while start_nodes:
        node = start_nodes.pop()
        topsorted.append(node)

        for dependency in node.requires:
            incoming[dependency] -= 1
            if not incoming[dependency]:
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
