import heapq
from audioop import reverse
from cgitb import small
from itertools import accumulate

from bintrees import RBTree
from Assignments import utilities
from Assignments.utilities import read_numbers_from_file


ROOT = 0

def median_maintenance(nums: list):
    accumulator = 0

    small_max_heap = []
    large_min_heap = []

    for k, num in enumerate(nums):
        maximum = -small_max_heap[ROOT] if small_max_heap else None
        minimum = large_min_heap[ROOT] if large_min_heap else None

        len_small_max_heap = len(small_max_heap)
        len_large_min_heap = len(large_min_heap)

        if maximum is None or num < maximum:
            heapq.heappush(small_max_heap, -num)
            if k % 2 == 1 and len_small_max_heap > len_large_min_heap:
                item = -heapq.heappop(small_max_heap)
                heapq.heappush(large_min_heap, item)
        elif minimum is None or num > minimum:
            heapq.heappush(large_min_heap, num)
            if k % 2 == 1 and len_large_min_heap > len_small_max_heap:
                item = heapq.heappop(large_min_heap)
                heapq.heappush(small_max_heap, -item)
        else:
            if len_small_max_heap > len_large_min_heap:
                heapq.heappush(large_min_heap, num)
            else:
                heapq.heappush(small_max_heap, -num)

        if len(large_min_heap) > len(small_max_heap):
            median = large_min_heap[ROOT]
        else:
            median = -small_max_heap[ROOT]
        accumulator += median

    return accumulator


if __name__ == "__main__":
    # data_set = read_numbers_from_file("Median_test.txt")    # 29335
    data_set = read_numbers_from_file("Median_challenge.txt")
    kth_median = median_maintenance(data_set)   # 46831213
    print(kth_median)