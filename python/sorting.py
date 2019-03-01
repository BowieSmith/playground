import math
import random

### Heapsort ###
def max_heapify(lst, i, n):

    def value_at(i):
        return lst[i - 1];

    leftIndex = 2 * i
    rightIndex = leftIndex + 1

    if (leftIndex > n):
        return
    if (rightIndex > n):
        maxIndex = leftIndex
    else:
        maxIndex = leftIndex if value_at(leftIndex) > value_at(rightIndex) else rightIndex

    if value_at(maxIndex) > value_at(i):
        lst[maxIndex - 1], lst[i - 1] = value_at(i), value_at(maxIndex) 
        max_heapify(lst, maxIndex, n)


def build_max_heap(lst):
    for i in range(math.floor(len(lst) / 2), 0, -1):
        max_heapify(lst, i, len(lst))

def heapsort(lst):
    build_max_heap(lst)
    for size in range(len(lst), 1, -1):
        lst[0], lst[size - 1] = lst[size - 1], lst[0]
        max_heapify(lst, 1, size - 1)


### Quicksort ###
def partition(lst, start, end):
    pivot_index = random.randint(start, start + (end - start))
    pivot_value = lst[pivot_index]
    lst[pivot_index], lst[end] = lst[end], lst[pivot_index]
        
    i = start - 1
    for j in range(start, end):
        if lst[j] <= pivot_value:
            i = i + 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[end] = lst[end], lst[i + 1]
    return i + 1

def quicksort(lst, start, end):
    if start < end:
        pivot_index = partition(lst, start, end);
        quicksort(lst, start, pivot_index - 1)
        quicksort(lst, pivot_index + 1, end)
