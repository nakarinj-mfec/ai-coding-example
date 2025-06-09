import unittest

from code.util import import_module

implement_module = import_module("implement", "01_implement.py")
calculate_statistics = implement_module.calculate_statistics
generate_graph = implement_module.generate_graph


class TestImplement(unittest.TestCase):

    def test_calculate_statistics_empty_list(self):
        self.assertIsNone(calculate_statistics([]))

    def test_calculate_statistics_single_element(self):
        self.assertIsNone(calculate_statistics([5]))

    def test_calculate_statistics_odd_length(self):
        self.assertIsNone(calculate_statistics([1, 2, 3, 4, 5]))

    def test_calculate_statistics_even_length(self):
        self.assertIsNone(calculate_statistics([1, 2, 3, 4, 5, 6]))

    def test_calculate_statistics_with_duplicates_single_mode(self):
        self.assertIsNone(calculate_statistics([1, 2, 2, 3, 4]))

    def test_calculate_statistics_with_duplicates_multiple_modes(self):
        self.assertIsNone(calculate_statistics([1, 1, 2, 2, 3]))

    def test_calculate_statistics_negative_numbers(self):
        self.assertIsNone(calculate_statistics([-1, -2, -3, -4, -5]))

    def test_generate_graph_empty_list(self):
        self.assertIsNone(generate_graph([]))

    def test_generate_graph_positive_values(self):
        self.assertIsNone(generate_graph([3, 5, 2]))

    def test_generate_graph_with_zero_value(self):
        self.assertIsNone(generate_graph([3, 0, 2]))

    def test_generate_graph_with_negative_value(self):
        self.assertIsNone(generate_graph([3, -5, 2]))

    def test_generate_graph_single_value(self):
        self.assertIsNone(generate_graph([4]))

if __name__ == '__main__':
    unittest.main()
