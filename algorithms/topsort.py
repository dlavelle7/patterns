from collections import deque
from graphviz import Digraph


class Node(object):
    count = 1

    def __init__(self):
        self.id = Node.count
        Node.count += 1
        self.requires = set()

    @property
    def name(self):
        return 'node {0}'.format(self.id)


def topological_sort():
    pass

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
