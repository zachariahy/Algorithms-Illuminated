from Assignments.utilities import read_numbers_from_file
import heapq
from bintrees import RBTree

ROOT = 0

def median_maintenance_heaps(nums: list):
    accumulator = 0
    small_max_heap = []
    large_min_heap = []

    for k, num in enumerate(nums):
        if not small_max_heap or num < -small_max_heap[ROOT]:
            heapq.heappush(small_max_heap, -num)
        else:
            heapq.heappush(large_min_heap, num)

        if len(small_max_heap) > len(large_min_heap) + 1:
            heapq.heappush(large_min_heap, -heapq.heappop(small_max_heap))
        elif len(small_max_heap) < len(large_min_heap):
            heapq.heappush(small_max_heap, -heapq.heappop(large_min_heap))

        median = -small_max_heap[ROOT]
        accumulator += median

    return accumulator

def median_maintenance_search_tree(nums: list):
    tree = RBTree()
    accumulator = 0

    for k, num in enumerate(nums):
        tree.insert(num, num)

        median = tree.nsmallest((k // 2) + 1)[-1][0]
        accumulator += median

    return accumulator

if __name__ == "__main__":
    # data_set = read_numbers_from_file("Median_test.txt")    # 29335
    data_set = read_numbers_from_file("Median_challenge.txt")   # 46831213

    # kth_median = median_maintenance_heaps(data_set)
    kth_median = median_maintenance_search_tree(data_set)   # much slower

    print(kth_median)
