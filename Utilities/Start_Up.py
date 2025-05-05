from Sorting_Algorithms import bubble_sort, quick_sort, merge_sort, selection_sort, insertion_sort
from Utilities.Results_Finalization import View_Results
from Error_Handling.Error import check_errors
from Utilities.Global_Variables import Main_Window
import Utilities.Global_Variables as Global_Variables

def start_sort(algorithm):
    if ( not check_errors(algorithm) ):
        return
    # Set Global Varaible
    Global_Variables.LENGTH_OF_ARRAY = int(Global_Variables.n_entry.get())
    # Generate the random array
    Global_Variables.arr = _ = [Global_Variables.random.randint(1, 100) for _ in range(Global_Variables.LENGTH_OF_ARRAY)]
    # Start timer
    Start_time = Start_time = Global_Variables.time.perf_counter()

    print("Starting sorting...")
    print("Algorithm:", algorithm)
    if algorithm == "Bubble Sort":
        bubble_sort()
    elif algorithm == "Quick Sort":
        quick_sort()
    elif algorithm == "Merge Sort":
        merge_sort()
    elif algorithm == "Selection Sort":
        selection_sort()
    elif algorithm == "Insertion Sort":
        insertion_sort()
    # End timer and calculate time taken
    end_time = Global_Variables.time.perf_counter()
    print("Time taken:", end_time - Start_time, "seconds")
    Global_Variables.TIME_TAKEN = end_time - Start_time
    # Show the result window
    View_Results()
