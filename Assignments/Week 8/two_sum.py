from Assignments.utilities import read_numbers_from_file

def two_sum(nums: set, t: int) -> int:
    for x in nums:
        y = t - x
        if y in nums and y != x:
            return 1
    return 0

if __name__ == "__main__":
    # data = read_numbers_from_file("problem12.4test.txt")    # 8
    # start = 3
    # stop = 10

    data = read_numbers_from_file("problem12.4.txt")    # 427
    start = -10000
    stop = 10000

    data_set = set(data)
    count = 0
    for target in range(start, stop + 1):
        count += two_sum(data_set, target)

    print(count)
