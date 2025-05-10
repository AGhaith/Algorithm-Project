import Utilities.Global_Variables as gv
from Utilities.Global_Variables import tk
def show_error(message):
    error = tk.Toplevel(gv.Main_Window)
    error.title("Error")
    error.geometry("300x150")
    gv.Main_Window.update_idletasks()

    x = gv.Main_Window.winfo_x() + (gv.Main_Window.winfo_width() // 2) - 150
    y = gv.Main_Window.winfo_y() + (gv.Main_Window.winfo_height() // 2) - 75
    error.geometry(f"+{x}+{y}")
    error.grab_set()

    tk.Label(error, text=message, fg="red").pack(padx=20, pady=20)
    tk.Button(error, text="Close", command=error.destroy).pack(pady=10)
def check_errors(algorithm):
    if algorithm not in gv.ALGORITHM_OPTIONS:
        show_error("Please select a valid algorithm.")
        return False
    if algorithm == "Merge Sort":
        try:
            input_text = gv.n_entry.get()
            for c in input_text:
                 if not (c.isdigit() or c == ','):
                    show_error("Please enter only integers and commas in the array.")
                    return False
            arr = list(map(int, gv.n_entry.get().split(',')))
            if len(arr) == 0:
                raise ValueError
            return True
        except ValueError:
            show_error("Please enter a valid array of integers separated by commas.")
            return False
    try :
        if(int(gv.n_entry.get()) > 0):
            return True
        else:
            show_error("Please enter a valid number of elements.")
            return False
    except ValueError:
        show_error("Please enter a valid number of elements.")
        return False