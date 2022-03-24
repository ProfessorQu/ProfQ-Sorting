import sys
sys.path.append("..")

from profq_sorting import bucket_sort
import random


def test():
    """Test a huge list
    """
    for _ in range(100):
        arr = [random.uniform(0, 1) for _ in range(random.randint(2, 100))]

        arr_sorted = bucket_sort(arr)

        arr.sort()
        assert arr == arr_sorted
