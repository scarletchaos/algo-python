from algo_py.comparators import asc_comp
from algo_py.decorators import timeit


@timeit
def bubblesort(arr, comp=asc_comp):
    for i in range(len(arr), 0, -1):
        for j in range(i - 1):
            if comp(arr[j + 1], arr[j]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
