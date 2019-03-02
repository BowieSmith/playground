import math
import random

### Sort tester ###
def test_sort(sort_function, number_trials, list_size, domain_size):
    for n in range(0, number_trials):
        l = [random.randint(1, domain_size) for _ in range(0, list_size)]
        l_copy = l[:]
        sort_function(l)
        if sorted(l_copy) != l:
            print("Original List:      ", l_copy)
            print("Sorted correctly:   ", sorted(l_copy))
            print("Sorted incorrectly: ", l)
            return "Test Failed"
    return "Test Passed!"


### Insertion sort ### In-place sort. O(n^2)
def insertion_sort(lst):
    for i in range(1, len(lst)):
        val = lst[i]
        j = i
        while (j > 0 and val < lst[j - 1]):
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = val


### Heapsort ### Sorts list in-place. O(nlogn) worst-case.
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


### Quicksort ### sorts list in-place. O(nlogn) average-case.
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

def quicksort(lst):
    def helper(list, start, end):
        if start < end:
            pivot_index = partition(lst, start, end);
            helper(lst, start, pivot_index - 1)
            helper(lst, pivot_index + 1, end)
    helper(lst, 0, len(lst) - 1)


### Mergesort ### sorts list using copies, O(n) space complexity. O(nlogn) worst-case. 
def merge(L1, L2):
    merged_list = []
    while True:
        if (L1[0] <= L2[0]):
            merged_list.append(L1[0])
            del L1[0]
        else:
            merged_list.append(L2[0])
            del L2[0]
        if not L1:
            merged_list.extend(L2)
            return merged_list
        if not L2:
            merged_list.extend(L1)
            return merged_list

def mergesort(lst):
    if len(lst) == 1:
        return lst
    middle_index = math.floor(len(lst) / 2);
    L1 = mergesort(lst[:middle_index])
    L2 = mergesort(lst[middle_index:])
    lst[:] = merge(L1, L2)
    return lst


### Countsort ### linear-Time sort. Good for small domain of integers. O(n) on well behaved lists.
def build_frequency_list(l):
    frq_list = [0 for _ in range(0, max(l) + 1)]
    for i in l:
        frq_list[i] += 1
    return frq_list

def running_total(l):
    run_total = []
    run_total.append(l[0])
    for i in range(0, len(l) - 1):
        run_total.append(run_total[i] + l[i + 1])
    return run_total

def countsort(lst):
    sorted_list = [0 for _ in range(0, len(lst))]
    freq_list = build_frequency_list(lst)
    freq_total = running_total(freq_list)
    for i in range(len(lst) - 1, -1, -1):
        sorted_list[freq_total[lst[i]] - 1] = lst[i]
        freq_total[lst[i]] -= 1
    lst[:] = sorted_list
    return sorted_list
