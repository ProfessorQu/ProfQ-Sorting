import sys
sys.path.append("..")

from helpers.max import get_max

def counting_sort(arr: list) -> list:
    """Sort an list using counting sort

    Args:
        arr (list): the list to be sorted

    Returns:
        list: the sorted list
    """
    size = len(arr)

    max_value = get_max(arr) + 1

    # Set output array and count table
    output = [0] * size
    count = [0] * max_value

    # Count all the numbers
    for i in range(size):
        count[arr[i]] += 1

    # Cumulative sum
    for i in range(1, max_value):
        count[i] += count[i - 1]

    # Fill the output array
    for i in range(size - 1, -1, -1):
        count[arr[i]] -= 1
        # arr[i] is the current element
        # count[arr[i]] is thus the index of the element
        # output[count[arr[i]]] is thus the correct location
        output[count[arr[i]]] = arr[i]

    return output