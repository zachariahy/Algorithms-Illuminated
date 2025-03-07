from Roughgarden.utilities import read_numbers_from_file

from random import randint

NUMBERS_LIST_LENGTH = 10000
TRIALS = 10


def swap(nums: list, i: int, j: int):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


def partition(nums: list, l: int, r: int):
    # invariants:   l < r
    p = nums[l]
    i = l + 1
    for j in range(l + 1, r):
        if nums[j] < p:
            swap(nums, i, j)
            i += 1
    swap(nums, l, i - 1)
    return i - 1


def choose_pivot(nums, l, r):
    # return l  # left
    # return r - 1  # right
    return randint(l, r - 1)  # random
    # median_index = l + (r - 1 - l) // 2
    # left = nums[l]
    # right = nums[r - 1]
    # median = nums[median_index]
    #
    # if left >= median >= right or right >= median >= left:
    #     return median_index
    # if median >= right >= left or left >= right >= median:
    #     return r - 1
    # if right >= left >= median or median >= left >= right:
    #     return l


def quick_sort(nums: list, l: int, r: int, comp_count: list):
    if l >= r:
        return
    i = choose_pivot(nums, l, r)
    swap(nums, l, i)
    j = partition(nums, l, r)
    comp_count[0] += (r - l - 1)
    quick_sort(nums, l, j, comp_count)
    quick_sort(nums, j + 1, r, comp_count)


if __name__ == '__main__':
    path = 'QuickSort.txt'
    numbers_list_original = read_numbers_from_file(path)

    numbers_list_sorted = sorted(numbers_list_original)

    random_comparisons = []
    for _ in range(TRIALS):
        numbers_list = numbers_list_original.copy()

        total_comps = [0]
        quick_sort(numbers_list, 0, NUMBERS_LIST_LENGTH, total_comps)
        random_comparisons.append(total_comps[0])

        # if numbers_list == numbers_list_sorted:
        #     print("Correctly sorted!")
        # else:
        #     print("Incorrectly sorted :(")

    mean = sum(random_comparisons) / len(random_comparisons)
    print(mean)

# first element (naive):        162085
# last element (naive):         164123
# random    10-trial mean:      156548.3
#           100-trial mean:     155806.95
#           1,000-trial mean:   155799.268
#           10,000-trial mean:  155792.1239
# median-of-three:              138382
# 10,000 * log_2(10,000) = 132,880
