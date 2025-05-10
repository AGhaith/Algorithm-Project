#Merge Sort
import Utilities.Global_Variables as gv
import Drawing.MergeDrawing as draw

#Merge Complexity O(N)
def merge(First_Part, Second_Part, level, x_start):
    gv.NUMBER_OF_OPERATIONS += 1
    result = []
    i = j = 0
    while i < len(First_Part) and j < len(Second_Part):
        if First_Part[i] < Second_Part[j]:
            result.append(First_Part[i])
            i += 1
        else:
            result.append(Second_Part[j])
            j += 1
    result.extend(First_Part[i:])
    result.extend(Second_Part[j:])
    draw.MergeDrawing(result, level, x_start)
    return result


level = 1

def merge_sort(arr, level, x_start):
    gv.NUMBER_OF_OPERATIONS += 1 
    length = len(arr)
    if length <= 1:
        draw.MergeDrawing(arr, level, x_start)
        return arr

    draw.MergeDrawing(arr, level, x_start)

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], level + 1, x_start)
    right = merge_sort(arr[mid:], level + 1, x_start + mid)

    return merge(left, right, level, x_start)


 
def start_merge_sort():
    gv.canvas.delete("all")
    arr = gv.arr
    sorted_arr = merge_sort(arr, level, -1)
    gv.canvas.delete("all")

