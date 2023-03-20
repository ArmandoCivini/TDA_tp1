import unittest
from matches import find_max_matching, pretty_print_matches, is_dominant
from parser import parser

class TestMatching(unittest.TestCase):

    def test_one_point_two_dominants(self):
        A, B = parser('tests/example1.txt')
        self.assertEqual(len(find_max_matching(A, B)), 1)
        
    def test_first_two_dom_second_one_dom_extra_points(self):
        A, B = parser('tests/example2.txt')
        self.assertEqual(len(find_max_matching(A, B)), 2)

    def test_first_one_dom_second_two_dom(self):
        A, B = parser('tests/example3.txt')
        self.assertEqual(len(find_max_matching(A, B)), 2)

    def test_first_two_dom_second_one_dom(self):
        A, B = parser('tests/example4.txt')
        self.assertEqual(len(find_max_matching(A, B)), 2)

    def test_two_points_both_match(self):
        A, B = parser('tests/example5.txt')
        self.assertEqual(len(find_max_matching(A, B)), 2)

    def test_two_points_two_doms_one_point_3_doms(self):
        A, B = parser('tests/example6.txt')
        self.assertEqual(len(find_max_matching(A, B)), 3)

    def test_force_empty_set(self):
        A, B = parser('tests/example7.txt')
        self.assertEqual(len(find_max_matching(A, B)), 6)
    
    def test_3_by_3(self):
        A, B = parser('tests/example8.txt')
        self.assertEqual(len(find_max_matching(A, B)), 3)

    def test_double_repeated_pairs(self):
        A, B = parser('tests/example9.txt')
        self.assertEqual(len(find_max_matching(A, B)), 3)

    def test_x_and_y_0(self):
        A, B = parser('tests/example10.txt')
        self.assertEqual(len(find_max_matching(A, B)), 2)

    def test_matching_x_values(self):
        A, B = parser('tests/example11.txt')
        self.assertEqual(len(find_max_matching(A, B)), 3)

if __name__ == '__main__':
    unittest.main()