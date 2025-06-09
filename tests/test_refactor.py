import unittest
import copy # To avoid modifying the original test data

from code.util import import_module
refactor_module = import_module("refactor", "03_refactor.py")
calculate_average_and_status = refactor_module.calculate_average_and_status
square_if_even = refactor_module.square_if_even


class TestRefactor(unittest.TestCase):

    def setUp(self):
        self.students_data = [
            {"name": "Alice", "scores": [80, 75, 90]},  # Avg: 81.67, Passed: True
            {"name": "Bob", "scores": [60, 65, 70]},    # Avg: 65.0, Passed: False
            {"name": "Charlie", "scores": [95, 90, 85]},# Avg: 90.0, Passed: True
            {"name": "Daisy", "scores": [40, 50, 45]},  # Avg: 45.0, Passed: False
            {"name": "Eve", "scores": []},              # Avg: 0, Passed: False
            {"name": "Frank", "scores": [70, 70, 70]}, # Avg: 70.0, Passed: True
            {"name": "Grace", "scores": [69, 69, 69]}  # Avg: 69.0, Passed: False
        ]
        self.expected_results = [
            {"name": "Alice", "scores": [80, 75, 90], "average": 81.66666666666667, "is_passed": True},
            {"name": "Bob", "scores": [60, 65, 70], "average": 65.0, "is_passed": False},
            {"name": "Charlie", "scores": [95, 90, 85], "average": 90.0, "is_passed": True},
            {"name": "Daisy", "scores": [40, 50, 45], "average": 45.0, "is_passed": False},
            {"name": "Eve", "scores": [], "average": 0, "is_passed": False},
            {"name": "Frank", "scores": [70, 70, 70], "average": 70.0, "is_passed": True},
            {"name": "Grace", "scores": [69, 69, 69], "average": 69.0, "is_passed": False}
        ]

    def assertStudentDataAlmostEqual(self, students1, students2):
        self.assertEqual(len(students1), len(students2))
        for s1, s2 in zip(students1, students2):
            self.assertEqual(s1["name"], s2["name"])
            self.assertEqual(s1["scores"], s2["scores"])
            self.assertAlmostEqual(s1["average"], s2["average"], places=5)
            self.assertEqual(s1["is_passed"], s2["is_passed"])

    def test_calculate_average_and_status_normal(self):
        students_copy = copy.deepcopy(self.students_data)
        calculate_average_and_status(students_copy)
        self.assertStudentDataAlmostEqual(students_copy, self.expected_results)

    def test_calculate_average_and_status_empty_list(self):
        students_empty = []
        calculate_average_and_status(students_empty)
        self.assertEqual(students_empty, [])

    def test_square_if_even(self):
        self.assertEqual(square_if_even([]), [], "Empty list should return empty list")
        self.assertEqual(square_if_even([2, 4, 6]), [4, 16, 36], "List with only even numbers")
        self.assertEqual(square_if_even([1, 3, 5]), [], "List with only odd numbers")
        self.assertEqual(square_if_even([1, 2, 3, 4, 5, 6]), [4, 16, 36], "List with mixed numbers")
        self.assertEqual(square_if_even([-2, -4, 0]), [4, 16, 0], "List with negative evens and zero")

if __name__ == '__main__':
    unittest.main()
