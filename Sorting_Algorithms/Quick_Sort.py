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
