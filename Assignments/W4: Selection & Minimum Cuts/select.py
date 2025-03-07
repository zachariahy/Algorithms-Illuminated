from Roughgarden.utilities import read_numbers_from_file, read_pi
from random import randint


def swap(nums: list, i: int, j: int):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


def partition(nums: list, l: int, r: int):
    p = nums[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        if nums[j] < p:
            swap(nums, i, j)
            i += 1
    swap(nums, l, i - 1)
    return i - 1


def choose_pivot(nums, l, r):
    return randint(l, r)  # uniformly at random


def select(nums: list, l: int, r: int, i: int):
    if len(nums) == 1:
        return nums[0]
    pi = choose_pivot(nums, l, r)
    swap(nums, l, pi)
    j = partition(nums, l, r)
    if j == i:
        return nums[j]
    elif j > i:
        return select(nums, l, j - 1, i)
    else:
        return select(nums, j + 1, r, i)


if __name__ == '__main__':
    path = 'pi.txt'
    numbers_list = read_pi(path)

    r = len(numbers_list) - 1
    nth_order_stat = r // 2
    median = select(numbers_list, 0, r, nth_order_stat)
    print(median)

# Test case #1: This file contains 10 integers, representing a 10-element array. What is the median (i.e.,
# the 5th-smallest element)? (Solution: 5469.) – PASSED
#
# Test case #2: This file contains 100 integers, representing a
# 100-element array. What is the median (i.e., the 50th order statistic)? (Solution: 4715.) – PASSED
#
# Challenge data set: Form
# an array in which the first element is the first 10 digits of pi, the second element is the next 10 digits of pi,
# and so on. (The digits of pi are available here.) Make the array as big as you can (perhaps 100,000 elements,
# or 1 million elements, or ...). What is the median of the array? [Aside: do you think this array has any duplicate
# elements?] – 999 element array median is 4962482017
#
# TODO Bonus challenge: Implement the deterministic linear-time selection algorithm from Section 6.3. For the
# challenge data set above, compare the maximum array lengths solvable in a reasonable amount of time (e.g.,
# one hour) with the randomized and deterministic linear-time selection algorithms.
