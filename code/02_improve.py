from typing import List, Dict, Any
from collections import Counter
import matplotlib.pyplot as plt # type: ignore
import os


# TODO: Improve plot_line_graph function to change the graph to bar chart
def plot_line_graph(data: List[int]) -> None:
    if not data:
        return

    plt.figure(figsize=(8, 5))
    plt.plot(range(1, len(data) + 1), data, marker='o', linestyle='-', color='b')
    plt.title("Line Graph of Data")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

plot_line_graph([1, 2, 3, 4, 5])

# TODO: Improve find_exp function by plot graph of exponential values
def find_exp(number_list: List[int]) -> List[int]:
    if not number_list:
        return []
        
    return [2 ** x for x in number_list]


# find_exp([1, 2, 3, 4, 5])