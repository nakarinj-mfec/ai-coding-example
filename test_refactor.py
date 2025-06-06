import unittest
import copy # To avoid modifying the original test data
from refactor import calculate_average_and_status, refactor_calculate_average_and_status, square_if_even, refactor_square_if_even

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

    def test_refactor_calculate_average_and_status_normal(self):
        students_copy = copy.deepcopy(self.students_data)
        refactor_calculate_average_and_status(students_copy)
        # The refactored function initializes "is_passed" to "Fail" (string)
        # then updates to boolean. Let's adjust expected for this specific function if needed,
        # or ensure the final state matches. The current expected_results use booleans.
        # The refactored function's logic:
        # student["is_passed"] = "Fail"
        # ...
        # student["is_passed"] = average >= 70 (This will be a boolean)
        # So the final "is_passed" should be boolean.
        self.assertStudentDataAlmostEqual(students_copy, self.expected_results)


    def test_refactor_calculate_average_and_status_empty_list(self):
        students_empty = []
        refactor_calculate_average_and_status(students_empty)
        self.assertEqual(students_empty, [])

    def test_both_functions_produce_same_results(self):
        students_original_func = copy.deepcopy(self.students_data)
        calculate_average_and_status(students_original_func)

        students_refactored_func = copy.deepcopy(self.students_data)
        refactor_calculate_average_and_status(students_refactored_func)

        self.assertStudentDataAlmostEqual(students_original_func, students_refactored_func)

    # Tests for square_if_even and refactor_square_if_even

    def test_square_if_even_current_behavior(self):
        # The current square_if_even function in refactor.py:
        # - Ignores its input parameter.
        # - Uses a global list: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # - Does not have a return statement, so it returns None.
        # The parameter type hint (num: int) is also incorrect for its intended list processing.
        # We test its actual behavior, which is returning None.
        self.assertIsNone(square_if_even([2, 4, 6]), "square_if_even should return None due to missing return statement")
        self.assertIsNone(square_if_even([]), "square_if_even should return None")
        # Note: Testing that it uses the global 'numbers' list internally is more complex
        # and would typically involve mocking or inspecting side effects if it modified a global.
        # Since it only builds a local list and doesn't return it, we focus on the None return.

    def test_refactor_square_if_even_normal(self):
        self.assertEqual(refactor_square_if_even([1, 2, 3, 4, 5, 6]), [4, 16, 36])

    def test_refactor_square_if_even_empty_list(self):
        self.assertEqual(refactor_square_if_even([]), [])

    def test_refactor_square_if_even_no_even_numbers(self):
        self.assertEqual(refactor_square_if_even([1, 3, 5, 7]), [])

    def test_refactor_square_if_even_all_even_numbers(self):
        self.assertEqual(refactor_square_if_even([2, 4, 6, 8]), [4, 16, 36, 64])

    def test_refactor_square_if_even_mixed_numbers(self):
        # Using the global numbers list from refactor.py as an example input
        # refactor.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # Expected output: [4, 16, 36, 64, 100]
        self.assertEqual(refactor_square_if_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [4, 16, 36, 64, 100])


if __name__ == '__main__':
    unittest.main()
