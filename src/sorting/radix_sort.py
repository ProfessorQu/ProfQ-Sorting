from itertools import count
import sys
sys.path.append("..")

from sorting.counting_sort import counting_sort
from helpers.max import get_max

def radix_sort(arr: list) -> list:
    max_value = get_max(arr)

    digits = 1
    while max_value > 0:
        max_value /= 10
        digits += 1
    
    place_value = 1

    output = arr
    while digits > 0:
        output = counting_sort(output, 10, place_value)

        place_value *= 10
        digits -= 1
    
    return output