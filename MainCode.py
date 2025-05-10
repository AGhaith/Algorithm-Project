from Utilities.Start_Up import *
from Utilities.Global_Variables import *
def main():
    Main_Window.title("Sorting Visualizer")

    # --- Center the Main_Window window ---/
    Main_Window.update_idletasks()
    x = (Main_Window.winfo_screenwidth() // 2) - (MAIN_WINDOW_WIDTH // 2)
    y = (Main_Window.winfo_screenheight() // 2) - (MAIN_WINDOW_HEIGHT // 2)
    Main_Window.geometry(f"{MAIN_WINDOW_WIDTH}x{MAIN_WINDOW_HEIGHT}+{x}+{y}")

    canvas.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    selected_algorithm = tk.StringVar(value="Select")
    tk.OptionMenu(Main_Window, selected_algorithm, *ALGORITHM_OPTIONS).grid(row=1, column=0, padx=10, pady=10)

    label_n = tk.Label(Main_Window, text="Enter number of elements (N):")
    label_n.grid(row=1, column=1, padx=10, pady=5)
    n_entry.grid(row=1, column=2, padx=10, pady=5)
    n_entry.insert(0, "10")

 
    tk.Button(Main_Window, text="Start Sorting",
        command=lambda: start_sort(selected_algorithm.get())
        ).grid(row=1, column=3, padx=10, pady=10)

    Main_Window.mainloop()


if __name__ == "__main__":
    main()