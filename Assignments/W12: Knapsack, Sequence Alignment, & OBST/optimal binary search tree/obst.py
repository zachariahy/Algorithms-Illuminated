
def opt_bst(n, key_weights: list) -> int:
    # precompute weights

    subproblem_solutions = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        subproblem_solutions[i][i-1] = 0
    for s in range(n):
        for i in range(n-s):
            subproblem_solutions[i][i+s] = (sum(key_weights[i:i+s+1]) +
                                            min([subproblem_solutions[i][r-1] +
                                                 subproblem_solutions[r+1][i+s] for r in range(i, i+s+1)]))
    return subproblem_solutions[0][n-1]

if __name__ == "__main__":
    with open("problem17.8optbst.txt") as file:
        content = file.readlines()
        line_0 = content[0].split()
        n_keys = int(line_0[0])
        line_1 = content[1].strip()
        frequencies = [int(i) for i in line_1.split(',')]

    solution = opt_bst(n_keys, frequencies)

    print(solution) # 2780
