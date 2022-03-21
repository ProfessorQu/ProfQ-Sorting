import sys
sys.path.append("..")

from sorting.quick_sort import quick_sort
import random

def test_small():
    """Test a small list
    """
    for _ in range(100):
        arr_sorted = [random.randint(0, 9) for _ in range(random.randint(2, 9))]
        arr = arr_sorted.copy()

        quick_sort(arr_sorted, 0, len(arr_sorted) - 1)

        arr.sort()
        assert arr == arr_sorted

def test_medium():
    """Test a medium list
    """
    for _ in range(100):
        arr_sorted = [random.randint(0, 19) for _ in range(random.randint(10, 19))]
        arr = arr_sorted.copy()

        quick_sort(arr_sorted, 0, len(arr_sorted) - 1)

        arr.sort()
        assert arr == arr_sorted

def test_large():
    """Test a large list
    """
    for _ in range(100):
        arr_sorted = [random.randint(0, 29) for _ in range(random.randint(20, 29))]
        arr = arr_sorted.copy()

        quick_sort(arr_sorted, 0, len(arr_sorted) - 1)

        arr.sort()
        assert arr == arr_sorted

def test_huge():
    """Test a huge list
    """
    for _ in range(100):
        arr_sorted = [random.randint(0, 100) for _ in range(random.randint(2, 100))]
        arr = arr_sorted.copy()

        quick_sort(arr_sorted, 0, len(arr_sorted) - 1)

        arr.sort()
        assert arr == arr_sorted
