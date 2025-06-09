from typing import List
import requests
import matplotlib.pyplot as plt


# TODO: Implement function to get sales chart for each productfrom API get sales order data and plot bar chart
# API_URL: https://68458248fc51878754db82d7.mockapi.io/api/salesOrderList
def get_sales_chart_data():
    pass


def plot_bar_chart(product_names: List[str], quantities: List[int]):
    """
    Plots a bar chart of product quantities.

    Args:
        product_names: A list of strings representing the product names.
        quantities: A list of numbers representing the quantity of each product.
    """
    plt.figure(figsize=(10, 6))

    plt.bar(product_names, quantities)
    
    plt.xlabel("Product Name")
    plt.ylabel("Quantity")
    
    plt.title("Product Quantities")
    
    plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    
    plt.show()


get_sales_chart_data()