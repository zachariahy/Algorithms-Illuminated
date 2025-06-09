ALPHABET = ['A', 'C', 'G', 'T']


def get_sequences_from_file(filename) -> tuple:
    with open(filename, 'r') as file:
        content = file.readlines()
        line_0 = content[0].split()
        em, en = int(line_0[0]), int(line_0[1])
        line_1 = content[1].split()
        gap_pen, mismatch_pen = int(line_1[0]), int(line_1[1])
        ex = content[2].strip()
        why = content[3].strip()
    return em, en, gap_pen, mismatch_pen, ex, why


def nw(x: str, y: str, m: int, n: int, mismatch_penalty: int, gap_penalty: int) -> int:
    subproblem_solutions = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        subproblem_solutions[i][0] = i * gap_penalty
    for j in range(n+1):
        subproblem_solutions[0][j] = j * gap_penalty
    for i in range(1, m+1):
        for j in range(1, n+1):
            cost = 0 if x[i-1] == y[j-1] else mismatch_penalty
            case_1 = subproblem_solutions[i-1][j-1] + cost
            case_2 = subproblem_solutions[i-1][j] + gap_penalty
            case_3 = subproblem_solutions[i][j-1] + gap_penalty
            subproblem_solutions[i][j] = min(case_1, case_2, case_3)
    return subproblem_solutions[m][n]


def nw_reconstruction():
    pass


if __name__ == "__main__":
    m, n, gap, mismatch, x, y = get_sequences_from_file('problem17.8nw.txt')
    sol = nw(x, y, m, n, mismatch, gap)
    print(sol)  # 224

