def bubble_sort(arr: list):
    """Sort a list using bubble sort

    Args:
        arr (list): the list to be sorted

    Returns:
        list: the sorted list
    """
    size = len(arr)

    # Loop over the entire list
    for _ in range(1, size):
        # Loop over the list to swap
        for j in range(0, size - 1):
            # Swap items if the current selected is greater than the next
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]