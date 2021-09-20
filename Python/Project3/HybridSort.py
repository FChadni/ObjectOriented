"""
Name: Farjana Chadni
PID: A58365164
"""

def quick_sort(unsorted, threshold, start, end, reverse=False):
    """
    :param unsorted: unsorted given list
    :param threshold: given value when it should call insertion sort
    :param start: first index
    :param end: last index
    :param reverse: ascending or decending order
    :return: none (inplace sort)
    """
    if len(unsorted) == 1:
        return None
    if start >= end:
        return None
    val = subdivide(unsorted, start, end, reverse)
    quick_sort(unsorted, threshold, start, val - 1, reverse)
    quick_sort(unsorted, threshold, val + 1, end, reverse)
    if len(unsorted) <= threshold:
        insertion_sort(unsorted, start, end, reverse)

def subdivide(unsorted, start, end, reverse):
    """
    :param unsorted: unsorted given list
    :param threshold: given value when it should call insertion sort
    :param start: first index
    :param end: last index
    :param reverse: ascending or decending order
    :return: index of pivot
    """
    pivot = find_pivot(unsorted, start, end)
    left = start
    right = end - 1
    if reverse is False:
        while left <= right:
            while left <= right and unsorted[left] < pivot:
                left += 1
            while left <= right and pivot < unsorted[right]:
                right -= 1
            if left <= right:
                unsorted[left], unsorted[right] = unsorted[right], unsorted[left]
                left, right = left + 1, right - 1
        unsorted[left], unsorted[end] = unsorted[end], unsorted[left]
    if reverse is True:
        while left <= right:
            while left <= right and unsorted[left] > pivot:
                left += 1
            while left <= right and pivot > unsorted[right]:
                right -= 1
            if left <= right:
                unsorted[left], unsorted[right] = unsorted[right], unsorted[left]
                left, right = left + 1, right - 1
        unsorted[left], unsorted[end] = unsorted[end], unsorted[left]
    return left

def find_pivot(unsorted, start, end):
    """
    :param unsorted: unsorted given list
    :param start: first index
    :param end: last index
    :return: pivot value
    """
    first_pivot = unsorted[start]
    last_pivot = unsorted[end]
    middle_pivot = (start + end)//2
    midean = unsorted[middle_pivot]
    if first_pivot < midean < last_pivot:
        unsorted[end], unsorted[middle_pivot] = unsorted[middle_pivot], unsorted[end]
        ##swap make midean pivot with last pivot
        return midean
    if midean < first_pivot < last_pivot:
        unsorted[start], unsorted[end] = unsorted[end], unsorted[start]
        ##swap make first pivot last pivot
        return first_pivot
    return last_pivot

def excange(unsorted, start, end):
    """
    :param unsorted: unsorted given list
    :param i: first
    :param j: end
    """
    unsorted[start], unsorted[end] = unsorted[end], unsorted[start]

def insertion_sort(unsorted, start, end, reverse):
    """
    :param unsorted: unsorted given list
    :param start: first index
    :param end: last index
    :param reverse: ascending or decending order
    :return: none (inplace sort)
    """
    for start in range(1, len(unsorted)):
        end = start
        if reverse is False:
            while (end > 0) and (unsorted[end] < unsorted[end-1]):
                excange(unsorted, end, end-1)
                end -= 1
        else:
            while (end > 0) and (unsorted[end] > unsorted[end-1]):
                excange(unsorted, end, end-1)
                end -= 1

def largest_sequential_difference(lst):
    """
    :param unsorted: unsorted given list
    :param threshold: given value when it should call insertion sort
    :param start: first index
    :param end: last index
    :param reverse: ascending or decending order
    :return: largest difference
    """
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return None
    quick_sort(lst, 4, 0, len(lst) -1)
    temp = 0
    for i in range(len(lst)-1):
        gap_new = lst[i + 1] - lst[i]
        if temp < gap_new:
            temp = gap_new
    return temp
