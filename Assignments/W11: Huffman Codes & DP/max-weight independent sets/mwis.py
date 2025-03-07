
NODE = 0
WEIGHT = 1

def get_nodes_from_file(filename):
    nodes = []
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            nodes.append((count, int(line)))
            count += 1
    return nodes

def wis(nodes: list):
    subproblem_solutions = [0, nodes[1][WEIGHT]]
    for i in range(2, len(nodes)):
        best_solution = max(subproblem_solutions[i-1], subproblem_solutions[i-2] + nodes[i][WEIGHT])
        subproblem_solutions.append(best_solution)
    return subproblem_solutions

def wis_reconstruction(solution: list, nodes: list):
    mwis = set()
    i = len(nodes) - 1
    while i >= 2:
        if solution[i-1] >= solution[i-2] + nodes[i][WEIGHT]:
            i -= 1
            continue
        mwis.add(nodes[i][NODE])
        i -= 2
    if i == 1:
        mwis.add(nodes[1][NODE])
    return mwis

if __name__ == "__main__":
    # dataset = get_nodes_from_file("problem16.6test.txt")    # 2617, {10, 2, 4, 7}
    dataset = get_nodes_from_file("problem16.6.txt")    # 10100110

    solutions = wis(dataset)
    max_weight_independent_set = wis_reconstruction(solutions, dataset)
    print(f"Value: {solutions[-1]}\tNodes: {max_weight_independent_set}")

    s = ""
    for node in [1, 2, 3, 4, 17, 117, 517, 997]:
        s += '1' if node in max_weight_independent_set else '0'
    print(s)
