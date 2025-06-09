import unittest
import os
import shutil

from code.util import import_module
improve_module = import_module("improve", "02_improve.py")
plot_line_graph_func = improve_module.plot_line_graph
find_exp_func = improve_module.find_exp

class TestImprove(unittest.TestCase):

    def setUp(self):
        self.charts_dir = "charts"
        # Ensure charts directory exists. While current functions in 02_improve.py
        # don't save files, this setup is kept for consistency or future use.
        if not os.path.exists(self.charts_dir):
            os.makedirs(self.charts_dir, exist_ok=True)

    def tearDown(self):
        # Clean up the charts directory if it exists.
        # This primarily targets the directory itself if it's empty,
        # as the tested functions currently don't create files.
        if os.path.exists(self.charts_dir):
            # Hypothetical files that tests might check for non-existence
            # or that future versions of the code might create.
            hypothetical_files_to_check_and_remove = [
                "empty_line_chart.png", 
                "test_line_chart.png",
                "exp_chart_empty.png"
            ]
            for f_name in hypothetical_files_to_check_and_remove:
                f_path = os.path.join(self.charts_dir, f_name)
                if os.path.exists(f_path):
                    os.remove(f_path)
            
            # Attempt to remove the directory if it's empty
            if not os.listdir(self.charts_dir):
                try:
                    os.rmdir(self.charts_dir)
                except OSError:
                    # Directory not empty or other issue, leave it.
                    pass

    def test_plot_line_graph_empty_list(self):
        # plot_line_graph returns None if data is empty and should not raise an error.
        # With 'Agg' backend, plt.show() is a no-op.
        try:
            self.assertIsNone(plot_line_graph_func([]), 
                              "plot_line_graph with empty list should return None.")
        except Exception as e:
            self.fail(f"plot_line_graph_func([]) raised an unexpected exception: {e}")
        
        # Verify no file is created (as plot_line_graph uses plt.show())
        test_filename = "empty_line_chart.png" 
        filepath = os.path.join(self.charts_dir, test_filename)
        self.assertFalse(os.path.exists(filepath), 
                         f"File {filepath} should not be created by plot_line_graph for empty data.")

    def test_plot_line_graph_with_data(self):
        # plot_line_graph with data calls plt.show() (no-op with 'Agg') and returns None.
        # It should execute without error and not save any file.
        try:
            self.assertIsNone(plot_line_graph_func([1, 2, 3]),
                              "plot_line_graph with data should return None.")
        except Exception as e:
            self.fail(f"plot_line_graph_func([1, 2, 3]) raised an unexpected exception: {e}")

        # Verify no file is created
        test_filename = "test_line_chart.png"
        filepath = os.path.join(self.charts_dir, test_filename)
        self.assertFalse(os.path.exists(filepath), 
                         f"File {filepath} should not be created by plot_line_graph as it uses plt.show().")

    def test_find_exp_empty_list(self):
        # find_exp returns [] for an empty list.
        self.assertEqual(find_exp_func([]), [])
        
        # Verify no plot file is created as find_exp does not currently plot.
        test_filename = "exp_chart_empty.png" # Hypothetical name from original test
        filepath = os.path.join(self.charts_dir, test_filename)
        self.assertFalse(os.path.exists(filepath), 
                         f"Plot file {filepath} should not be created by find_exp for empty data.")

    def test_find_exp_calculates_correctly(self):
        # This test remains valid as it checks the calculation logic.
        self.assertEqual(find_exp_func([1, 2, 3]), [2, 4, 8])
        self.assertEqual(find_exp_func([0, 1, 5]), [1, 2, 32])
        # No file creation to check here as find_exp only calculates.

if __name__ == '__main__':
    unittest.main()
