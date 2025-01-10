def read_numbers_from_file(file_path):
    numbers = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Convert the line to an integer and add it to the list
                number = int(line.strip())
                numbers.append(number)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except ValueError:
        print("One or more lines in the file do not contain valid integers.")
    return numbers


def merge_and_count_split_inversions(c, d):
    i = j = split_inversions = 0
    total_length = len(c) + len(d)
    b = []
    for k in range(total_length):
        if i == len(c):
            b.append(d[j])
            j += 1
        elif j == len(d):
            b.append(c[i])
            i += 1
        elif c[i] < d[j]:
            b.append(c[i])
            i += 1
        else:
            b.append(d[j])
            j += 1
            split_inversions += len(c) - i
    return b, split_inversions


def sort_and_count_inversions(a):
    length = len(a)
    if length < 2:
        return a, 0
    midpoint = length // 2
    c, left_inversions = sort_and_count_inversions(a[:midpoint])
    d, right_inversions = sort_and_count_inversions(a[midpoint:])
    b, split_inversions = merge_and_count_split_inversions(c, d)
    return b, left_inversions + right_inversions + split_inversions


path = 'IntegerArray.txt'
numbers_list = read_numbers_from_file(path)
# numbers_list = [1, 3, 5, 2, 4, 6]

print(sort_and_count_inversions(numbers_list)[1])
# print(sort_and_count_inversions(numbers_list))

# Testcase: a = [1, 3, 5, 2, 4, 6]. sort_and_count_inversions(a) returns ([1, 2, 3, 4, 5, 6], 3)
# a = list from IntegerArray.txt. sort_and_count_inversions(a) returns (sorted list, 2407905288)
