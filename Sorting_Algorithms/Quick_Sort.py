#omda
import random
import Utilities.Global_Variables as gv
import Drawing.Drawing as draw
import time

def quick_sort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1

    if start < end:
        gv.NUMBER_OF_OPERATIONS += 1
        pivot_index = partition(array, start, end)
        quick_sort(array, start, pivot_index - 1)
        quick_sort(array, pivot_index + 1, end)

    return array

def partition(array, start, end):
    pivot_value = array[end]
    smaller_element_index = start 

    for current_index in range(start, end):
        if array[current_index] <= pivot_value:
            gv.NUMBER_OF_OPERATIONS += 1
            array[smaller_element_index], array[current_index] = array[current_index], array[smaller_element_index]

            # Visualization Part
            if len(array) == gv.LENGTH_OF_ARRAY:
                color_array = [
                    "red" if i == end else  # pivot
                    "green" if i == smaller_element_index or i == current_index else
                    "blue"
                    for i in range(len(array))
                ]
                draw.draw_array(color_array)
                time.sleep(0.05)

            smaller_element_index += 1

    
    array[smaller_element_index], array[end] = array[end], array[smaller_element_index]
    gv.NUMBER_OF_OPERATIONS += 1 #last swap

    #Final placement visualization
    if len(array) == gv.LENGTH_OF_ARRAY:
        color_array = [
            "purple" if i == smaller_element_index else "blue"
            for i in range(len(array))
        ]
        draw.draw_array(color_array)
        time.sleep(0.05)

    return smaller_element_index
