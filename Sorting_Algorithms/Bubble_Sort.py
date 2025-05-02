#Sama
import time
import random

def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(0, length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


random_arr = [random.randint(0, 100) for _ in range(10)]
startTime = time.time()
sorted_arr = bubble_sort(random_arr.copy())
endTime = time.time()
print("Original array:", random_arr)
print("Sorted array:", sorted_arr)
print("Time taken:", endTime - startTime, "seconds")
