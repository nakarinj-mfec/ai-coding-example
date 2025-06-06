import unittest
import os
import shutil
from improve import calculate_statistics, generate_matplotlib_graph

class TestImprove(unittest.TestCase):

    def test_calculate_statistics_empty_list(self):
        expected_stats = {
            "median": 0.0,
            "mode": [],
            "range": 0,
            "mean": 0.0,
            "count": 0,
            "sum": 0,
            "min": 0,
            "max": 0
        }
        self.assertEqual(calculate_statistics([]), expected_stats)

    def test_calculate_statistics_single_element(self):
        expected_stats = {
            "median": 5.0,
            "mode": [5],
            "range": 0,
            "mean": 5.0,
            "count": 1,
            "sum": 5,
            "min": 5,
            "max": 5
        }
        self.assertEqual(calculate_statistics([5]), expected_stats)

    def test_calculate_statistics_odd_length(self):
        stats = calculate_statistics([1, 2, 3, 4, 5])
        self.assertEqual(stats["median"], 3.0)
        self.assertEqual(stats["mode"], [1, 2, 3, 4, 5]) # All elements appear once
        self.assertEqual(stats["range"], 4) # 5 - 1
        self.assertEqual(stats["mean"], 3.0)
        self.assertEqual(stats["count"], 5)
        self.assertEqual(stats["sum"], 15)
        self.assertEqual(stats["min"], 1)
        self.assertEqual(stats["max"], 5)

    def test_calculate_statistics_even_length(self):
        stats = calculate_statistics([1, 2, 3, 4, 5, 6])
        self.assertEqual(stats["median"], 3.5) # (3 + 4) / 2
        self.assertEqual(stats["mode"], [1, 2, 3, 4, 5, 6])
        self.assertEqual(stats["range"], 5) # 6 - 1
        self.assertEqual(stats["mean"], 3.5)
        self.assertEqual(stats["count"], 6)
        self.assertEqual(stats["sum"], 21)
        self.assertEqual(stats["min"], 1)
        self.assertEqual(stats["max"], 6)

    def test_calculate_statistics_with_duplicates_single_mode(self):
        stats = calculate_statistics([1, 2, 2, 3, 4])
        self.assertEqual(stats["median"], 2.0)
        self.assertEqual(stats["mode"], [2])
        self.assertEqual(stats["range"], 3) # 4 - 1
        self.assertEqual(stats["mean"], 2.4) # 12 / 5
        self.assertEqual(stats["count"], 5)
        self.assertEqual(stats["sum"], 12)
        self.assertEqual(stats["min"], 1)
        self.assertEqual(stats["max"], 4)

    def test_calculate_statistics_with_duplicates_multiple_modes(self):
        stats = calculate_statistics([1, 1, 2, 2, 3])
        self.assertEqual(stats["median"], 2.0)
        self.assertEqual(stats["mode"], [1, 2]) # Sorted modes
        self.assertEqual(stats["range"], 2) # 3 - 1
        self.assertEqual(stats["mean"], 1.8) # 9 / 5
        self.assertEqual(stats["count"], 5)
        self.assertEqual(stats["sum"], 9)
        self.assertEqual(stats["min"], 1)
        self.assertEqual(stats["max"], 3)

    def test_calculate_statistics_negative_numbers(self):
        stats = calculate_statistics([-1, -2, -3, -4, -5])
        self.assertEqual(stats["median"], -3.0)
        self.assertEqual(stats["mode"], [-5, -4, -3, -2, -1])
        self.assertEqual(stats["range"], 4) # -1 - (-5)
        self.assertEqual(stats["mean"], -3.0)
        self.assertEqual(stats["count"], 5)
        self.assertEqual(stats["sum"], -15)
        self.assertEqual(stats["min"], -5)
        self.assertEqual(stats["max"], -1)

    def test_generate_matplotlib_graph_empty_list(self):
        self.assertEqual(generate_matplotlib_graph([]), "No data to display")

    def test_generate_matplotlib_graph_creates_file(self):
        charts_dir = "charts"
        test_filename = "test_chart.png"
        filepath = os.path.join(charts_dir, test_filename)

        # Clean up before test
        if os.path.exists(filepath):
            os.remove(filepath)
        if os.path.exists(charts_dir) and not os.listdir(charts_dir): # remove dir if empty
             os.rmdir(charts_dir)
        elif os.path.exists(charts_dir) and os.listdir(charts_dir) and test_filename in os.listdir(charts_dir): # specific file removal
            pass # file will be overwritten or handled by os.remove above

        result = generate_matplotlib_graph([1, 2, 3], filename=test_filename)
        self.assertEqual(result, f"Graph saved to {filepath}")
        self.assertTrue(os.path.exists(filepath))

        # Clean up after test
        if os.path.exists(filepath):
            os.remove(filepath)
        # Attempt to remove charts_dir only if it's empty
        if os.path.exists(charts_dir) and not os.listdir(charts_dir):
            os.rmdir(charts_dir)
        # If other files are in charts_dir, leave it.

    def test_generate_matplotlib_graph_creates_directory(self):
        charts_dir = "charts"
        test_filename = "test_dir_chart.png"
        filepath = os.path.join(charts_dir, test_filename)

        # Ensure directory does not exist before test
        if os.path.exists(filepath):
            os.remove(filepath)
        if os.path.exists(charts_dir):
            # If other files exist, just remove the test file if it's there
            if test_filename in os.listdir(charts_dir):
                 os.remove(filepath)
            # If only the test file was there, or it's now empty, remove the dir
            if not os.listdir(charts_dir):
                shutil.rmtree(charts_dir) # Use shutil to remove dir and its contents if necessary
        
        self.assertFalse(os.path.exists(charts_dir)) # Check dir is gone

        result = generate_matplotlib_graph([1, 2, 3], filename=test_filename)
        self.assertEqual(result, f"Graph saved to {filepath}")
        self.assertTrue(os.path.exists(charts_dir))
        self.assertTrue(os.path.exists(filepath))

        # Clean up after test
        if os.path.exists(filepath):
            os.remove(filepath)
        if os.path.exists(charts_dir) and not os.listdir(charts_dir):
            os.rmdir(charts_dir)

if __name__ == '__main__':
    unittest.main()
