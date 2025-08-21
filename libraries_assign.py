# main.py
# This script demonstrates basic data handling and visualization tasks
# using popular Python libraries.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

def perform_numpy_operations():
    """
    Creates a NumPy array and calculates its mean.
    """
    print("--- 1. NumPy Operations ---")
    # Create a NumPy array of integers from 1 to 10
    num_array = np.arange(1, 11)
    print(f"NumPy Array: {num_array}")
    
    # Calculate the mean of the array
    mean_value = np.mean(num_array)
    print(f"Mean of the array: {mean_value}\n")

def perform_pandas_operations():
    """
    Loads a dataset into a pandas DataFrame and shows summary statistics.
    """
    print("--- 2. Pandas Operations ---")
    # Create a small dataset using a dictionary
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [25, 30, 35, 40, 28],
        'Score': [88, 92, 85, 95, 89]
    }
    
    # Load the dictionary into a pandas DataFrame
    df = pd.DataFrame(data)
    
    print("DataFrame:")
    print(df)
    
    # Display summary statistics for the numerical columns
    print("\nSummary Statistics:")
    print(df.describe())
    print("\n")

def fetch_api_data():
    """
    Fetches data from a public API and prints a specific item.
    """
    print("--- 3. API Data Fetching with Requests ---")
    # URL for a public API (JSONPlaceholder provides fake API for testing)
    api_url = "https://jsonplaceholder.typicode.com/posts/1"
    
    try:
        # Make a GET request to the API
        response = requests.get(api_url)
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        print(f"Successfully fetched data for post with ID: {data.get('id')}")
        # Print a key piece of information (the title of the post)
        print(f"Title of the post: '{data.get('title')}'\n")
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}\n")

def plot_data():
    """
    Plots a simple line graph using matplotlib.
    """
    print("--- 4. Data Visualization with Matplotlib ---")
    # A simple list of numbers to plot
    y_values = [10, 12, 15, 14, 18, 20, 22]
    x_values = range(len(y_values))
    
    # Create the plot
    plt.figure(figsize=(8, 5)) # Set the figure size
    plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')
    
    # Add a title and labels for the axes
    plt.title("Simple Line Graph")
    plt.xlabel("X-axis (Index)")
    plt.ylabel("Y-axis (Values)")
    
    # Add a grid for better readability
    plt.grid(True)
    
    # Save the plot to a file
    file_name = "simple_line_graph.png"
    plt.savefig(file_name)
    
    print(f"A line graph has been generated and saved as '{file_name}'.")
    # Use plt.show() if you want to display the plot in an interactive window
    # plt.show()


# Main execution block
if __name__ == "__main__":
    print("Running Python Data Handling Script...\n")
    perform_numpy_operations()
    perform_pandas_operations()
    fetch_api_data()
    plot_data()
    print("\nScript finished.")

