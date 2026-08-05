# Binary Search

def binary_search(arr, item, begin=0, end=None):

    if end is None:
        end = len(arr) - 1

    if begin <= end:
        mid =  (begin + end) // 2
        if arr[mid] == item:
            return mid
        
        if item < arr[mid]:
            return binary_search(arr, item, begin, mid - 1)
        
        else:
            return binary_search(arr, item, mid + 1, end)

    return None