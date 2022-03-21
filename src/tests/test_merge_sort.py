import sys
sys.path.append("..")

from sorting.merge_sort import merge_sort
import random

def test_small():
    """Test a small list
    """
    for _ in range(100):
        arr = [random.randint(0, 9) for _ in range(4)]

        arr_sorted = merge_sort(arr)

        arr.sort()

        print(arr_sorted)

        assert arr == arr_sorted

def test_medium():
    """Test a medium list
    """
    for _ in range(100):
        arr = [random.randint(0, 19) for _ in range(random.randint(10, 19))]

        arr_sorted = merge_sort(arr)

        arr.sort()
        assert arr == arr_sorted

def test_large():
    """Test a large list
    """
    for _ in range(100):
        arr = [random.randint(0, 29) for _ in range(random.randint(20, 29))]

        arr_sorted = merge_sort(arr)

        arr.sort()
        assert arr == arr_sorted

def test_huge():
    """Test a huge list
    """
    for _ in range(100):
        arr = [random.randint(0, 100) for _ in range(random.randint(2, 100))]

        arr_sorted = merge_sort(arr)

        arr.sort()
        assert arr == arr_sorted
