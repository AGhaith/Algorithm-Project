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

import Utilities.Global_Variables as Global_Variables
def selection_sort():
    size = Global_Variables.LENGTH_OF_ARRAY
    L = Global_Variables.arr
    for i in range(size):
        minimum_indx = i

        for j in range(i+1 , size):
            if L[j] < L[minimum_indx]:
                minimum_indx = j
                Global_Variables.NUMBER_OF_OPERATIONS += 1

        L[i], L[minimum_indx] = L[minimum_indx], L[i]






