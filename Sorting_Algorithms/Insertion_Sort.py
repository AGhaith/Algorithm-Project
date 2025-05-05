import Utilities.Global_Variables as Global_Variables

def insertion_sort() :
    arr = Global_Variables.arr
    length = Global_Variables.LENGTH_OF_ARRAY
    for i in range (1,length):
        key=arr[i]
        j=i-1
        while((j>=0) and (key<arr[j])):
            arr[j+1]=arr[j]
            j -=1
            arr[j+1]=key
            Global_Variables.NUMBER_OF_OPERATIONS += 1
