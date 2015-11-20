import unittest
from topsort import topological_sort

class TestDfsBfsAlgorithms(unittest.TestCase):

    def test_topological_sort(self):
        topsorted = topological_sort()
        import ipdb; ipdb.set_trace()
