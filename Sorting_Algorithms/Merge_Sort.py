#Merge Sort
import time
import random
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
def merge_sort(Arr):
    if len(Arr) <= 1:
        return Arr
    mid = len(Arr) // 2
    left = merge_sort(Arr[:mid])
    right = merge_sort(Arr[mid:])
    return merge(left, right)
def main():
    arr = [random.randint(0, 100) for _ in range(10)]
    start=time.time()
    merge_sort(arr)
    end=time.time()
    print(f"time takes to sort is : {end-start:.18f}")

if __name__ == "__main__":
    main()
