import Utilities.Global_Variables as Global_Variables
import Drawing.Drawing as draw

def insertion_sort(x):
    arr = Global_Variables.arr
    length = x
    for i in range (1,length):
        key=arr[i]
        j=i-1
        while((j>=0) and (key<arr[j])):
            if (x==Global_Variables.LENGTH_OF_ARRAY):
                color_array = ["red" if x == j or x == key else "blue" for x in range(length)]
                draw.draw_array(color_array)
            if((j>=0) and (key<arr[j])):
                arr[j+1]=arr[j]
                j -=1
                arr[j+1]=key
                Global_Variables.NUMBER_OF_OPERATIONS += 1