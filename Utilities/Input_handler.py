import Utilities.Global_Variables as gv
import Error_Handling as error

def get_input_array(algorithm, entry_array):
    if algorithm == "Merge Sort":
        try:
            arr = list(map(int, entry_array.get().split(',')))
            gv.MERGE_ARRAY= arr
        except ValueError:
            print("ERROR")
    else:
        try:
            gv.LENGTH_OF_ARRAY = int(gv.n_entry.get())
            gv.arr = _ = [gv.random.randint(1, 100) for _ in range(gv.LENGTH_OF_ARRAY)]
        except ValueError:
            error.show_error()
