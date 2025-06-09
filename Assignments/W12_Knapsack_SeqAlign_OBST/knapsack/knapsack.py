
NUMBER = 0
VALUE = 1
WEIGHT = 2

def get_items_from_file(filename):
    items = []
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            line = line.split()
            items.append((count, int(line[0]), int(line[1])))
            count += 1
    return items[0][1], items[0][2], items[1:]

def knapsack_dp(capacity: int, item_count: int, items: list):
    # Iterative, Dynamic Programming, Bottom-up Approach, using 2D array
    solutions = [[0 for c in range(capacity + 1)] for i in range(item_count + 1)]
    for i in range(1, item_count):
        for c in range(capacity + 1):
            if items[i][WEIGHT] > c:
                solutions[i][c] = solutions[i-1][c]
            else:
                solutions[i][c] = max(solutions[i-1][c], solutions[i-1][c-items[i][WEIGHT]] + items[i][VALUE])
    return solutions

def knapsack_reconstruction(capacity: int, item_count: int, items: list, solutions: list):
    optimal_solution = set()
    c = capacity - 1    # remaining capacity
    for i in reversed(range(item_count)):
        item_weight = items[i][WEIGHT]
        item_value = items[i][VALUE]
        item_num = items[i][NUMBER]
        if item_weight <= c and solutions[i-1][c-item_weight] + item_value >= solutions[i-1][c]:
            optimal_solution.add(item_num)
            c -= item_weight
    return optimal_solution

def knapsack_dp_space_optimized(capacity: int, item_count: int, items: list):
    # Iterative, Dynamic Programming, Bottom-up Approach, using 1D array
    solutions = [0 for c in range(capacity + 1)]
    for i in range(1, item_count):
        for c in reversed(range(capacity + 1)):
            if items[i][WEIGHT] <= c:
                solutions[c] = max(solutions[c], solutions[c-items[i][WEIGHT]] + items[i][VALUE])
    return solutions

def knapsack_rec_memoized(capacity: int, item_count: int, items: list):
    # Recursive, Memoized, Top-Down Approach
    pass

if __name__ == "__main__":
    knapsack_size, number_of_items, item_list = get_items_from_file("problem16.7test.txt")  # 2493893
    subproblem_solutions = knapsack_dp(knapsack_size, number_of_items, item_list)
    print(f"Max total value: {subproblem_solutions[-2][-1]}")
    solution = knapsack_reconstruction(knapsack_size, number_of_items, item_list, subproblem_solutions)
    print(f"Optimal solution: {solution}")

    knapsack_size, number_of_items, item_list = get_items_from_file("problem16.7.txt")  # 4243395
    subproblem_solutions = knapsack_dp_space_optimized(knapsack_size, number_of_items, item_list)
    print(f"Max total value: {subproblem_solutions[-1]}")
