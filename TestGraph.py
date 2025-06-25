import unittest
from Graph import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        
    def test_add_node(self):
        self.graph.add_node('A')
        self.assertIn('A', self.graph.adj_list)
        self.assertEqual(self.graph.adj_list['A'], [])
        
    def test_add_edge(self):
        self.graph.add_edge('A', 'B')
        self.assertIn('B', self.graph.adj_list['A'])
        self.assertIn('A', self.graph.adj_list['B'])
        
    def test_get_nodes(self):
        self.graph.add_edge('A', 'B')
        self.assertCountEqual(self.graph.get_nodes(), ['A', 'B'])