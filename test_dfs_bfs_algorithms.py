import unittest
from dfs_bfs_algorithms import depth_first_search, breadth_first_search, \
        create_balanced_tree, Node

class TestDfsBfsAlgorithms(unittest.TestCase):

    def test_depth_first_search(self):
        Node.count = 1
        result = depth_first_search(1)
        self.assertTrue(type(result) is Node)
        Node.count = 1
        result = depth_first_search(7)
        self.assertTrue(type(result) is Node)
        Node.count = 1
        result = depth_first_search(12)
        self.assertTrue(type(result) is Node)
        Node.count = 1
        result = depth_first_search(15)
        self.assertTrue(type(result) is Node)
        Node.count = 1
        result = depth_first_search(0)
        self.assertEqual(result, None)
        Node.count = 1
        result = depth_first_search(16)
        self.assertEqual(result, None)

    def test_breadth_first_search(self):
        Node.count = 1
        result = breadth_first_search(1)
        self.assertTrue(type(result) is Node)
        Node.count = 1
        result = breadth_first_search(7)
        self.assertTrue(type(result) is Node)
        Node.count = 1
        result = breadth_first_search(12)
        self.assertTrue(type(result) is Node)
        Node.count = 1
        result = breadth_first_search(15)
        self.assertTrue(type(result) is Node)
        Node.count = 1
        result = breadth_first_search(0)
        self.assertEqual(result, None)
        Node.count = 1
        result = breadth_first_search(16)
        self.assertEqual(result, None)

    def test_create_balanced_tree(self):
        root = create_balanced_tree()
        self.assertTrue(type(root) is Node)
        for child in root.children:
            self.assertTrue(root.id < child.id)
