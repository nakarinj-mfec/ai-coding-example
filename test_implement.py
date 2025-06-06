import unittest
from implement import find_median, generate_graph

class TestImplement(unittest.TestCase):

    def test_find_median(self):
        self.assertEqual(find_median([5, 10, 15, 20, 25]), 15)
        self.assertEqual(find_median([5, 10, 15, 20]), 12) # (10 + 15) // 2 = 12
        self.assertEqual(find_median([10]), 10)
        self.assertEqual(find_median([]), 0)
        self.assertEqual(find_median([1, 2, 3, 4, 5, 6]), 3) # (3+4)//2 = 3
        self.assertEqual(find_median([3, 1, 4, 1, 5, 9, 2, 6]), 3) # sorted: [1,1,2,3,4,5,6,9] -> (3+4)//2 = 3

    def test_generate_graph_empty_list(self):
        self.assertEqual(generate_graph([]), "No data to display")

    def test_generate_graph_positive_values(self):
        expected_graph = "1: ***\n2: *****\n3: **"
        self.assertEqual(generate_graph([3, 5, 2]), expected_graph)

    def test_generate_graph_with_zero_value(self):
        expected_graph = "1: ***\n2: \n3: **"
        self.assertEqual(generate_graph([3, 0, 2]), expected_graph)

    def test_generate_graph_with_negative_value(self):
        expected_graph = "1: ***\n2: (negative value)\n3: **"
        self.assertEqual(generate_graph([3, -5, 2]), expected_graph)

    def test_generate_graph_single_value(self):
        expected_graph = "1: ****"
        self.assertEqual(generate_graph([4]), expected_graph)

if __name__ == '__main__':
    unittest.main()
