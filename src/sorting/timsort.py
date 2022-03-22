MIN_MERGE = 32

def calc_minrun(size: int):
    """Calculates the minimum size of the runs for a certain number of items.

    Args:
        n (int): the number of items in the array
    """

    r = 0
    while size >= MIN_MERGE:
        r |= size & 1
        size >>= 1
    
    return size + r

def insertion_sort(arr: list, left: int, right: int) -> list:
    """Insertion sort from left index to right index
    Which is at most run_size

    Args:
        arr (list): the array to sort
        left (int): the left-most index to start from
        right (int): the right-most index to end from

    Returns:
        list: the sorted list
    """
    for i in range(left + 1, right + 1):
        j = i

        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


def merge(arr: list, left: int, middle: int, right: int):
    """Merge sorted runs

    Args:
        arr (list): the list to be merged
        left (int): the left index to 
        middle (int): _description_
        right (int): _description_
    """
    len1, len2 = middle - left + 1, right - middle
    left_arr, right_arr = [], []

    left_arr.extend(arr[left + i] for i in range(len1))
    right_arr.extend(arr[middle + 1 + i] for i in range(len2))

    i, j, k = 0, 0, left

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
    
        k += 1
    
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1
    
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1


def timsort(arr: list):
    size = len(arr)

    min_run = calc_minrun(size)

    for start in range(0, size, min_run):
        end = min(start + min_run - 1, size - 1)
        insertion_sort(arr, start, end)

    run_size = min_run
    while run_size < size:
        for left in range(0, size, 2 * size):
            pass