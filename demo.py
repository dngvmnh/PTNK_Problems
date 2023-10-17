from Search import *
from Sort import *
from list import *

def sort_search_demo(arr, target) : 

    bubble_sort(arr)
    # selection_sort(arr)
    # insertion_sort(arr)
    # merge_sort(arr)
    # quick_sort(arr)
    # heap_sort(arr)
    # radix_sort(arr)

    result = linear_search(arr, target)
    # result = sentinel_linear_search(arr, target)
    # result = binary_search(arr, target)
    # result = ternary_search(arr, 0, len(arr) - 1, target)
    # result = interpolation_search(arr, target)     
    # result = fibonacci_search(arr, target) 

    print(arr)

    if result != -1:
        print(f"{target} found at index {result}.")
    else:
        print(f"{target} not found.")

def list() :
    
if __name__ == '__main__' : 
    # arr = [9,8,7,6,5,4,3,2,1]
    # target = 7
    # sort_search_demo(arr, target)

    list()
