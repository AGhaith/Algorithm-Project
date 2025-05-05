import tkinter as tk
import Utilities.Global_Variables as Global_Variables
def View_Results():
    result_window = tk.Toplevel(Global_Variables.Main_Window)
    result_window.title("Sorting Results")
    result_window.geometry("300x150")
    x = Global_Variables.Main_Window.winfo_x() + (Global_Variables.Main_Window.winfo_width() // 2) - 150
    y = Global_Variables.Main_Window.winfo_y() + (Global_Variables.Main_Window.winfo_height() // 2) - 75
    result_window.geometry(f"+{x}+{y}")
    result_window.grab_set()
    result_label = tk.Label(result_window, text=f"Time taken: {Global_Variables.TIME_TAKEN:.16f} seconds\nOperations: {Global_Variables.NUMBER_OF_OPERATIONS}")
    result_label.pack(padx=20, pady=20)
    close_button = tk.Button(result_window, text="Close", command=result_window.destroy)
    close_button.pack(pady=10)
