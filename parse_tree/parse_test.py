from parse_tree import *
import unittest


class TestParseTree(unittest.TestCase):  # Testing binary searching with no slicing
    def setUp(self) -> None:
        pass

    def test_split(self):
        self.assertEqual(split_expression("( (100 + 5) *3 )"),
                         ['(', '(', '100', '+', '5', ')', '*', '3', ')'])
        self.assertEqual(split_expression("((10+5)*300)"),
                         ['(', '(', '10', '+', '5', ')', '*', '300', ')'])
