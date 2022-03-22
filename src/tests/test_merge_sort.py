import sys
sys.path.append("..")

from sorting.merge_sort import merge_sort
import random


def test():
    """Test a huge list
    """
    for _ in range(100):
        arr = [random.randint(0, 100) for _ in range(random.randint(2, 100))]

        arr_sorted = merge_sort(arr)

        arr.sort()
        assert arr == arr_sorted
