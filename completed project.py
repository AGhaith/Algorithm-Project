import tkinter as tk
import random
import time
import matplotlib.pyplot as plt

class SortVisualizer:
    def __init__(self, master):
        self.master = master
        master.title("Sorting Algorithm Visualizer")

        self.canvas = tk.Canvas(master, width=800, height=400, bg='white')
        self.canvas.pack()

        control_frame = tk.Frame(master)
        control_frame.pack()

        tk.Label(control_frame, text="Enter N:").grid(row=0, column=0)
        self.n_entry = tk.Entry(control_frame)
        self.n_entry.grid(row=0, column=1)

        tk.Label(control_frame, text="Choose Algorithm:").grid(row=0, column=2)
        self.algorithm_var = tk.StringVar()
        self.algorithm_menu = tk.OptionMenu(control_frame, self.algorithm_var, "Bubble Sort", "Selection Sort", "Insertion Sort")
        self.algorithm_menu.grid(row=0, column=3)

        self.start_button = tk.Button(control_frame, text="Start", command=self.start_sorting)
        self.start_button.grid(row=0, column=4)

        self.data = []
        self.operations = 0  # Count operations

        # Mapping algorithms to their complexities
        self.complexities = {
            "Bubble Sort": "O(n²)",
            "Selection Sort": "O(n²)",
            "Insertion Sort": "O(n²)"
        }

    def draw_data(self, colors=None):
        self.canvas.delete("all")
        c_height = 400
        c_width = 800
        x_width = c_width / (len(self.data) + 1)
        offset = 10

        normalized_data = [i / max(self.data) for i in self.data]

        for i, height in enumerate(normalized_data):
            x0 = i * x_width + offset
            y0 = c_height - height * 350
            x1 = (i + 1) * x_width
            y1 = c_height

            color = colors[i] if colors else "blue"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
            self.canvas.create_text(x0 + 2, y0, anchor=tk.SW, text=str(self.data[i]), font=("Arial", 8))

        self.master.update_idletasks()

    def start_sorting(self):
        try:
            N = int(self.n_entry.get())
            if N <= 0:
                raise ValueError
        except ValueError:
            print("Invalid N value")
            return

        self.data = [random.randint(10, 100) for _ in range(N)]
        self.operations = 0
        self.draw_data()

        algo = self.algorithm_var.get()

        if algo == "Bubble Sort":
            self.bubble_sort()
        elif algo == "Selection Sort":
            self.selection_sort()
        elif algo == "Insertion Sort":
            self.insertion_sort()
        else:
            print("Please select an algorithm.")
            return

        self.show_results(N)

    def bubble_sort(self):
        n = len(self.data)
        for i in range(n):
            for j in range(0, n - i - 1):
                self.operations += 1
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    self.draw_data(["red" if x == j or x == j+1 else "blue" for x in range(len(self.data))])
                    time.sleep(0.02)

    def selection_sort(self):
        n = len(self.data)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                self.operations += 1
                if self.data[min_idx] > self.data[j]:
                    min_idx = j
            self.data[i], self.data[min_idx] = self.data[min_idx], self.data[i]
            self.draw_data(["red" if x == i or x == min_idx else "blue" for x in range(len(self.data))])
            time.sleep(0.02)

    def insertion_sort(self):
        for i in range(1, len(self.data)):
            key = self.data[i]
            j = i - 1
            while j >= 0 and key < self.data[j]:
                self.operations += 1
                self.data[j + 1] = self.data[j]
                j -= 1
                self.draw_data(["red" if x == j or x == j+1 else "blue" for x in range(len(self.data))])
                time.sleep(0.02)
            self.data[j + 1] = key
            self.draw_data(["red" if x == i else "blue" for x in range(len(self.data))])
            time.sleep(0.02)

    def show_results(self, N):

        # Show time complexity
        result_window = tk.Toplevel(self.master)
        result_window.title("Results")
        tk.Label(result_window, text=f"Algorithm: {self.algorithm_var.get()}").pack()
        tk.Label(result_window, text=f"Time Complexity: {self.complexities[self.algorithm_var.get()]}").pack()
        tk.Label(result_window, text=f"Total Operations: {self.operations}").pack()

root = tk.Tk()
app = SortVisualizer(root)
root.mainloop()
