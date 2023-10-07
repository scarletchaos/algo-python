from algo_py.comparators import asc_comp
from algo_py.decorators import timeit    

@timeit
def quicksort(array):
    do_quicksort(array)

def do_quicksort(array, left=0, right=None, comp=asc_comp):
    if right is None:
        right = len(array)-1
    if right - left < 1:
        return
    split_index = partition(array, left, right, array[(left + right)//2], comp)
    do_quicksort(array, left, split_index - 1, comp)
    do_quicksort(array, split_index, right, comp)

def partition(array, left, right, pivot, comp):
    while True:
        #print('\t', pivot, left, array, right)
        while comp(array[left], pivot):
            left += 1

        while comp(pivot, array[right]):
            right -= 1

        
        if left >= right:
            return right + 1
        array[right], array[left] = array[left], array[right] 
        left += 1
        right -= 1
