from typing import List

# example: [5, 10, 15, 20, 25]
def find_median(number_list: List[int]) -> int:
    if not number_list:
        return 0
    
    sorted_list = sorted(number_list)
    n = len(sorted_list)
    mid_index = n // 2
    
    if n % 2 == 1:
        return sorted_list[mid_index]
    else:
        return (sorted_list[mid_index - 1] + sorted_list[mid_index]) // 2


def generate_graph(number_list: List[int]) -> str:
    if not number_list:
        return "No data to display"

    graph_lines = []
    for index, value in enumerate(number_list):
        if value < 0:
            bar = "(negative value)" 
        else:
            bar = '*' * value
        graph_lines.append(f"{index+1}: {bar}")
    
    return "\n".join(graph_lines)