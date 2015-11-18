import unittest
from dfs_bfs_algorithms import depth_first_search, breadth_first_search, \
        create_balanced_tree, Node

class TestDfsBfsAlgorithms(unittest.TestCase):

    def test_depth_first_search(self):
        depth_first_search(1)

    def test_breadth_first_search(self):
        breadth_first_search(1)

    def test_create_balanced_tree(self):
        root = create_balanced_tree()
        self.assertTrue(type(root) is Node)
        for child in root.children:
            self.assertTrue(root.id < child.id)

    # TODO: Test new important functions
