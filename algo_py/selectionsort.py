from algo_py.comparators import asc_comp
from algo_py.decorators import timeit

@timeit
def selectionsort(arr, comp=asc_comp):
    for i in range(len(arr)):
        extr = i 
        for j in range(i, len(arr)):
            if comp(arr[j], arr[extr]):
                extr = j
        if extr != i:
            arr[extr], arr[i] = arr[i], arr[extr]
