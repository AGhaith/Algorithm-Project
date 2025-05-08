#Merge Sort
import Utilities.Global_Variables as gv
import Drawing.MergeDrawing as draw

#Merge Complexity O(N)
def merge(First_Part, Second_Part):
    result = []
    First_Part_Pointer = Second_Part_Pointer = 0
    while First_Part_Pointer < len(First_Part) and Second_Part_Pointer < len(Second_Part):
        if First_Part[First_Part_Pointer] < Second_Part[Second_Part_Pointer]:
            result.append(First_Part[First_Part_Pointer])
            First_Part_Pointer += 1
        else:
            result.append(Second_Part[Second_Part_Pointer])
            Second_Part_Pointer += 1
    result.extend(First_Part[First_Part_Pointer:])
    result.extend(Second_Part[Second_Part_Pointer:])
    return result

#Merge Sort Complexity O(NlogN)
def merge_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    mid = length // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
 
def start_merge_sort():
    arr1 = gv.arr
    sorted_arr = merge_sort(arr1)
