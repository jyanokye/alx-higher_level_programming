#!/usr/bin/python3

"""Module containing the find_peak function."""

def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers.
    
    Args:
        list_of_integers: A list of an unsorted integers.
    Returns:
        The first peak found in the list, or None if no peak is found.

    """
    loi = list_of_integers
    if loi == []:
        return None
    total = len(loi)
    if total == 1:
        return loi[0]
    elif total == 2:
        return max(loi)
    middle = int(total / 2)
    peak = loi[middle]
    if peak > loi[middle - 1] and peak > loi[middle + 1]:
        return peak
    elif peak < loi[middle - 1]:
        return find_peak(loi[:middle])
    else:
        return find_peak(loi[middle + 1:])
