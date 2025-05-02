#omda
import random

def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    pivot = arr[mid]

    arr = arr[:mid] + arr[mid+1:]

    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

# arr = quick_sort([3, 6, 8, 10, 1, 2, 1])
big_arr = [random.randint(0, 1_000_000) for _ in range(100_000)]
arr = quick_sort(big_arr)
print(arr)