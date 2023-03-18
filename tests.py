import unittest
from matches import find_max_matching, pretty_print_matches, is_dominant
from parser import parser

class TestMatching(unittest.TestCase):

    def test_one_point_two_dominants(self):
        A, B = parser('example1.txt')
        self.assertEqual(len(find_max_matching(A, B)), 1)
        
    def test_first_two_dom_second_one_dom_extra_points(self):
        A, B = parser('example2.txt')
        self.assertEqual(len(find_max_matching(A, B)), 2)

    def test_first_one_dom_second_two_dom(self):
        A, B = parser('example3.txt')
        self.assertEqual(len(find_max_matching(A, B)), 2)

    def test_first_two_dom_second_one_dom(self):
        A, B = parser('example4.txt')
        self.assertEqual(len(find_max_matching(A, B)), 2)

    def test_two_points_both_match(self):
        A, B = parser('example5.txt')
        self.assertEqual(len(find_max_matching(A, B)), 2)

    def test_two_points_two_doms_one_point_3_doms(self):
        A, B = parser('example6.txt')
        self.assertEqual(len(find_max_matching(A, B)), 3)

    def test_force_empty_set(self):
        A, B = parser('example7.txt')
        self.assertEqual(len(find_max_matching(A, B)), 6)


if __name__ == '__main__':
    unittest.main()