from Assignments.W05_SCC.kosaraju_iter import kosaraju
from collections import defaultdict

N_LITERALS = 100000

def get_clauses_from_file(filename: str) -> list[tuple]:
    clauses = []

    with open(filename, 'r') as file:
        next(file)

        for line in file:
            line = line.split()
            x, y = int(line[0]), int(line[1])
            clauses.append((x, y))

    return clauses


def reduce_to_graph(clauses) -> (dict, dict):
    # reduce 2SAT clauses to suitable graph
    # 2 vertices per variable/literal (2n) and two directed edges per clause (2m)
    # map: "x OR y" clause to (¬x → y) and (¬y → x) in graph
    adj_list = defaultdict(list)
    adj_list_rev = defaultdict(list)

    for x, y in clauses:
        adj_list[-x].append(y)
        adj_list[-y].append(x)

        adj_list_rev[y].append(-x)
        adj_list_rev[x].append(-y)

    return adj_list, adj_list_rev


def test_satisfiable(scc: dict) -> int:
    # satisfiable iff every var resides in different component than its opposite
    # i.e., no path from x to not(x)
    # Return 0 if false, else 1
    for component in scc:
        for literal in scc[component]:
            if -literal in scc[component]:
                return 0

    return 1


def two_sat_scc(clauses: list) -> int:
    # 2SAT reduces to computing the strongly connected components of a suitable graph
    graph, graph_rev = reduce_to_graph(clauses)
    scc = kosaraju(graph, graph_rev)
    print("Testing satisfiability...")
    return test_satisfiable(scc)


def run_tests():
    tests = [
        ({"1": [1, 2], "2": [-1, -2]}, 1),
        ({"1": [1, -1], "2": [2, -2]}, 0),
        ({"1": [3], "2": [-4], "3": [5, -6], "4": [6, -5]}, 1),
    ]
    for i, (scc, expected) in enumerate(tests, 1):
        res = test_satisfiable({int(k): v for k, v in scc.items()})
        assert res == expected, f"Test {i} failed: expected {expected}, got {res}"
        print(f"Test {i} passed.")


if __name__ == "__main__":
    # run_tests()
    instances = ["2sat1.txt", "2sat2.txt", "2sat3.txt", "2sat4.txt", "2sat5.txt", "2sat6.txt"]
    results = []

    for instance in instances:
        print(f"Testing {instance}...")
        sat_clauses = get_clauses_from_file(instance)
        is_satisfiable = two_sat_scc(sat_clauses)
        results.append(is_satisfiable)
        print(f"Instance {instance}: {'Satisfiable' if is_satisfiable else 'Unsatisfiable'}")

    print("Final result: ", end='')
    for result in results:
        print(result, end='')   # 101100
