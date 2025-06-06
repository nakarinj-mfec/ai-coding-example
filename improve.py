from typing import List, Dict, Any
from collections import Counter
import matplotlib.pyplot as plt # type: ignore
import os


def calculate_statistics(number_list: List[int]) -> Dict[str, Any]:
    if not number_list:
        return {
            "median": 0.0,
            "mode": [],
            "range": 0,
            "mean": 0.0,
            "count": 0,
            "sum": 0,
            "min": 0,
            "max": 0
        }
    
    # median
    sorted_list = sorted(number_list)
    n = len(sorted_list)
    mid_index = n // 2

    if n % 2 == 1:
        result_median = float(sorted_list[mid_index])
    else:
        result_median = (sorted_list[mid_index - 1] + sorted_list[mid_index]) / 2.0


    # mode
    counts = Counter(number_list)
    max_count = max(counts.values())
    result_mode = sorted([num for num, count in counts.items() if count == max_count])


    # range
    result_range = max(number_list) - min(number_list)
    result_mean = sum(number_list) / len(number_list) if number_list else 0.0
    
    return {
        "median": result_median,
        "mode": result_mode,
        "range": result_range,
        "mean": result_mean,
        "count": len(number_list),
        "sum": sum(number_list),
        "min": min(number_list) if number_list else 0,
        "max": max(number_list) if number_list else 0
    }


def generate_matplotlib_graph(number_list: List[int], filename: str = "bar_chart.png") -> str:
    if not number_list:
        return "No data to display"

    plt.figure(figsize=(10, 6))
    # Using indices for x-axis to represent position in the list
    x_values = range(len(number_list))
    plt.bar(x_values, number_list, color='skyblue')
    
    plt.xlabel("Index in List")
    plt.ylabel("Value")
    plt.title("Bar Chart of Numbers")
    plt.xticks(x_values, [str(i) for i in x_values]) # Label x-axis with indices
    
    # Ensure the 'charts' directory exists
    charts_dir = "charts"
    if not os.path.exists(charts_dir):
        os.makedirs(charts_dir)
    
    filepath = os.path.join(charts_dir, filename)
    
    try:
        plt.savefig(filepath)
        plt.close() # Close the plot to free memory
        return f"Graph saved to {filepath}"
    except Exception as e:
        plt.close()
        return f"Error saving graph: {e}"
