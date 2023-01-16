#!/usr/bin/python3
# 

def find_peak(list_of_integers):
    """Funtion takes a list as an argument and finds the largest number/peak"""
    if list_of_integers == []:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        return max(list_of_integers)

    mid = int(len(list_of_integers) / 2)
    pivot = list_of_integers[mid]
    peak = 0

    if pivot > list_of_integers[mid - 1] and pivot > list_of_integers[mid + 1]:
        peak = pivot
        return peak
    elif pivot < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])

    
    
print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))