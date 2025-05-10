import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Utilities.Global_Variables as gv
from matplotlib.figure import Figure
import pandas as pd

def show_graph(algorithm):


    graph_window = tk.Toplevel(gv.Main_Window)
    graph_window.title("Sorting Algorithm Performance")
    graph_window.geometry("800x600")  


    fig = Figure(figsize=(8, 6), dpi=100)
    ax = fig.add_subplot(111)
    
    # Clear previous plot if exists
    ax.clear()

    data = gv.performance_data.get(algorithm, [])
    print("Performance Data:", data)

    if len(data) < 2:
        ax.text(0.5, 0.5, 'Not enough data points\nRun with different array sizes', 
                ha='center', va='center', fontsize=12)
    else:
        # Convert to DataFrame and sort by Number of Elements
        df = pd.DataFrame(data, 
                          columns=["Number of Elements", "Number of Operations"])
        df = df.sort_values("Number of Elements")
        
        # Plot using matplotlib directly (more reliable)
        ax.plot(df["Number of Elements"], df["Number of Operations"], 
                marker='o', linestyle='-', color='blue')
        
        # Formatting
        ax.set_xlabel("Number of Elements", fontsize=12)
        ax.set_ylabel("Number of Opreations", fontsize=12)
        ax.set_title("Sorting Algorithm Performance: " + algorithm, fontsize=14)
        ax.grid(True)

    # Display the graph
    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    data.clear()
