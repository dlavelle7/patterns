import unittest
from topsort import topological_sort, Node

class TestDfsBfsAlgorithms(unittest.TestCase):

    def test_topological_sort(self):
        # node 2 first, then node 1 or 3
        topsorted = topological_sort()
        first = topsorted[-1]
        self.assertTrue(isinstance(first, Node))
        self.assertEqual(first.name, "node 2")
