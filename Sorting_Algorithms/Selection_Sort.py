#Omar Salama

'''
==Selection sort==

Time complexities:

- Best case = 0(n^2)
- Average case = O(n^2)
- Worst case = O(n^2)

Space complexity : 
 - O(1)

'''

import time

def Selection_Sort(L):
    size = len(L)

    for i in range(size):
        minimum_indx = i

        for j in range(i+1 , size):
            if L[j] < L[minimum_indx]:
                minimum_indx = j

        L[i], L[minimum_indx] = L[minimum_indx], L[i]

    return L


L1 = [22,90,1,4,2,11,60]
print("List before sorting: " , L1)

start_time = time.time()
res = Selection_Sort(L1)
end_time = time.time()
print("List after sorting: ", res)
print("Time taken to sort the list: ", end_time - start_time)



