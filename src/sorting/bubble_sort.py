def bubble_sort(arr: list):
    """Sort a list using bubble sort

    Args:
        arr (list): the list to be sorted

    Returns:
        list: the sorted list
    """
    size = len(arr)

    for _ in range(1, size):
        for j in range(0, size - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]