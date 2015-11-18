import unittest
from dfs_bfs_algorithms import Node, depth_first_search, breadth_first_search

class TestDfsBfsAlgorithms(unittest.TestCase):

    def test_depth_first_search(self):
        depth_first_search()

    def test_breadth_first_search(self):
        breadth_first_search()
