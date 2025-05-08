#Sama
import Utilities.Global_Variables as gv
import Drawing.Drawing as draw
def bubble_sort(x):
    arr = gv.arr
    length = x
    for i in range(length):
        for j in range(0, length - i - 1):
            if ( x == gv.LENGTH_OF_ARRAY ):
                color_array = ["red" if x == j or x == j + 1 else "blue" for x in range(length)]
                draw.draw_array(color_array)

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            gv.NUMBER_OF_OPERATIONS += 1

