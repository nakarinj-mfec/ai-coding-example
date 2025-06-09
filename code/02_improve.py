from typing import List, Dict, Any
from collections import Counter
import matplotlib.pyplot as plt # type: ignore
import os


# TODO: Improve function find_median to calculate various statistics from a list of numbers
# The function should return a dictionary with the following keys:
# - ค่ามัธยฐาน "median": the median of the list
# - ฐานนิยม "mode": the mode(s) of the list (if multiple modes, return a list)
# - ค่าพิสัย "range": the range of the list (max - min)
# - ค่าเฉลี่ย "mean": the mean (average) of the list
# - "count": the count of numbers in the list
# - "sum": the sum of the numbers in the list
# - "min": the minimum value in the list
# - "max": the maximum value in the list
# API_URL: https://68458248fc51878754db82d7.mockapi.io/api/statisticsList
def calculate_statistics(number_list: List[int]) -> Dict[str, Any]:
    pass


# TODO: Improve function generate_graph to generate a bar chart using matplotlib
# The function should save the graph as a PNG file in a directory named "charts".
# If the directory does not exist, it should be created.
# The graph should represent the numbers as bars, with the x-axis labeled with indices of the list.
# API_URL: https://68458248fc51878754db82d7.mockapi.io/api/barChartList
def generate_matplotlib_graph(
        number_list: List[int], 
        filename: str = "bar_chart.png"
    ) -> str:
    pass
