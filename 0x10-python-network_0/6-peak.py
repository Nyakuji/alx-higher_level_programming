#!/usr/bin/python3
"""Script that Write a function that finds a peak in a list of unsorted integers."""
def find_peak(list_of_integers):
    """finding peak"""
    if not list_of_integers:
        return None  # Return None for an empty list

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    # At the end of the loop, low and high point to the peak
    return list_of_integers[low]
