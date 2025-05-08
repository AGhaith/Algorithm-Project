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
    try :
        if(int(gv.n_entry.get()) > 0):
            return True
        else:
            show_error("Please enter a valid number of elements.")
            return False
    except ValueError:
        show_error("Please enter a valid number of elements.")
        return False