#Insertion Sort


#   time complexities   
# best case = 0(n) => will not enter the while loop
# average case = Theta(n^2)
# worst case = O(n^2)
import time
import random

def insertion_sort(arr) :
    for i in range (1,len(arr)):
        key=arr[i]
        j=i-1
        while((j>=0) and (key<arr[j])):
            arr[j+1]=arr[j]
            j -=1
            arr[j+1]=key

#testing the sort and time complexity with diffrent arrays
arr = [random.randint(0, 100) for _ in range(10000)]
#arr= list(range(10000))
#print("array before sorting: ",arr)
start=time.time()
insertion_sort(arr)
end=time.time()
#print("the array after sorting : ",arr)
print(f"time takes to sort is : {end-start:.18f}")