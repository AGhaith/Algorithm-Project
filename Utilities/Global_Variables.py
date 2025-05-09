import tkinter as tk
import random
import time

# Dimensions
CANVAS_HEIGHT = 500
CANVAS_WIDTH = 775
MAIN_WINDOW_WIDTH = 800
MAIN_WINDOW_HEIGHT = 600

# Algorithm Options
ALGORITHM_OPTIONS = ["Bubble Sort", "Quick Sort", "Merge Sort", "Selection Sort", "Insertion Sort"]
performance_data = {
    "Bubble Sort": [],
    "Quick Sort": [],
    "Merge Sort": [],
    "Selection Sort": [],
    "Insertion Sort": []
}
# Tkinter Widgets
Main_Window = tk.Tk()
canvas = tk.Canvas(Main_Window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
n_entry = tk.Entry(Main_Window)

# Variables for Sorting
NUMBER_OF_OPERATIONS = 0
TIME_TAKEN = 0.0
arr = []
LENGTH_OF_ARRAY = 0
TEMPN = 0
