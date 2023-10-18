from Search import *
from Sort import *
from SLL import *
from DLL import *
import random

def sort_search(arr, target) : 

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
        print(f"{target} found at idx {result}")
    else:
        print(f"{target} not found")

def sll() :    
    e_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    target = random.randint(1,20)
    sll_list = SLL(e_list)
    # current_node = sll_list.compare(target)
    # if current_node :
    #     sll_list.insert_after(current_node, "HELLO")

    # sll_list.sll_append("Vu")
    # sll_list.sll_append("Minh")
    # sll_list.sll_append("Dang")
    sll_list.print_list()

    sll_list.bubble_sort()

    sll_list.print_list()

def dll() :
    e_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    target = f"{random.randint(1,20)}"
    dll_list = DLL()
    
    for i in range(1,len(e_list)):
        dll_list.dll_append(f'{i}')

    current_node = dll_list.compare(target)
    if current_node :
        dll_list.insert_after(current_node, "HELLO")
    
    dll_list.dll_append("Vu")
    dll_list.dll_append("Minh")
    dll_list.dll_append("Dang")

    dll_list.insert_begining("PTNK")
    dll_list.insert_end("DHQG")

    dll_list.print_list()

    
if __name__ == '__main__' : 

    arr = [9,8,7,6,5,4,3,2,1]
    target = 7
    # sort_search(arr, target)

    sll()
    # dll()
