arr = [1,2,3,4,5,6,7,8,9]
target = 7

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  

def sentinel_linear_search(arr, target):
    n = len(arr)
    
    last_element = arr[n - 1]
    arr[n - 1] = target
    
    i = 0
    while arr[i] != target:
        i += 1
    
    arr[n - 1] = last_element
    
    if i < n - 1 or arr[n - 1] == target:
        return i 
    else:
        return -1 

def binary_search(arr, target):
    left = 0  
    right = len(arr) - 1 

    while left <= right:
        mid = left + (right - left) 

        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1 

    return -1 

def ternary_search(arr, left, right, target):
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = mid1 + (right - left) // 3

        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        if target < arr[mid1]:
            return ternary_search(arr, left, mid1 - 1, target)
        elif target > arr[mid2]:
            return ternary_search(arr, mid2 + 1, right, target)
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, target)

    return -1

def interpolation_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right and arr[left] <= target <= arr[right]:
        if left == right:
            if arr[left] == target:
                return left
            return -1

        pos = left + int(((right - left) / (arr[right] - arr[left])) * (target - arr[left]))

        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1

    return -1

def fibonacci_search(arr, target):
    n = len(arr)

    fib_m_minus_2 = 0
    fib_m_minus_1 = 1
    fib = fib_m_minus_1 + fib_m_minus_2

    while fib < n:
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib
        fib = fib_m_minus_1 + fib_m_minus_2

    offset = -1

    while fib > 1:
        i = min(offset + fib_m_minus_2, n - 1)

        if arr[i] < target:
            fib = fib_m_minus_1
            fib_m_minus_1 = fib_m_minus_2
            fib_m_minus_2 = fib - fib_m_minus_1
            offset = i
        elif arr[i] > target:
            fib = fib_m_minus_2
            fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
            fib_m_minus_2 = fib - fib_m_minus_1
        else:
            return i

    if fib_m_minus_1 and arr[offset + 1] == target:
        return offset + 1

    return -1

if __name__ == '__main__' : 

    result = linear_search(arr, target)
    result = sentinel_linear_search(arr, target)
    result = binary_search(arr, target)
    result = ternary_search(arr, 0, len(arr) - 1, target)
    result = interpolation_search(arr, target)     
    result = fibonacci_search(arr, target) 
   
    if result != -1:
        print(f"Element {target} found at index {result}.")
    else:
        print(f"Element {target} not found in the array.")
