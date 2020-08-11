import time
from console import fg, bg, fx

def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                time.sleep(0.1)
                representation(arr, i-1, i)
                swap(i - 1, i)
                swapped = True         
    return arr

def representation(array, small_index, big_index):
    print("[", end="")
    for j in range(len(array)):
        if j == big_index:
            print(fg.blue + str(array[big_index]) + fg.default, end=", " if j != len(array)-1 else "]")
        elif j==small_index:
            print(fg.red + str(array[small_index]) + fg.default, end=", " if j != len(array)-1 else "]")
        else:
            print(array[j], end=", " if j != len(array)-1 else "]")
    print()

def selection_sort(arr):      
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            # Select the smallest value
            if arr[j] < arr[minimum]:
                minimum = j 
        # Place it at the front of the 
        # sorted end of the array
        time.sleep(0.1)
        representation(arr, i, minimum)
        arr[minimum], arr[i] = arr[i], arr[minimum]
        
    return arr

def insertion_sort(arr):
        
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        while pos > 0 and arr[pos - 1] > cursor:
            # Swap the number down the list
            time.sleep(0.1)
            representation(arr, pos-1,pos)
            arr[pos] = arr[pos - 1]
            pos = pos - 1

        # Break and do the final swap
        representation(arr, pos,i)
        arr[pos] = cursor
    return arr
def merge_sort(arr):
    # The last array split
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    # Merge each side together
    return merge(left, right, arr.copy())


def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
      
        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            representation(left+right,left_cursor+right_cursor, left_cursor )
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            representation(left+right,left_cursor+right_cursor, right_cursor )
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
            
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
        
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


def partition(array, begin, end):
    pivot_idx = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx

def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return
    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx-1)
    quick_sort_recursion(array, pivot_idx+1, end)
    return array

def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    
    return quick_sort_recursion(array, begin, end)