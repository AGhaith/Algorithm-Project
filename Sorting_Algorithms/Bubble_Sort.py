#Sama
import Utilities.Global_Variables as gv
import Drawing.Drawing as draw
def bubble_sort():
    arr = gv.arr
    length = gv.LENGTH_OF_ARRAY
    for i in range(length):
        for j in range(0, length - i - 1):
            color_array = ["red" if x == j or x == j + 1 else "blue" for x in range(length)]
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                gv.NUMBER_OF_OPERATIONS += 1
            draw.draw_array(color_array)

