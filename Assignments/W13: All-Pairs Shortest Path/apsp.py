import math

OUT_EDGES = 0
IN_EDGES = 1

def read_directed_weighted_edge_list(file_path) -> dict:
    """
    Reads a directed weighted edge list from a file and returns an adjacency list.

    Returns:
        dict[int, list[list[tuple[int, int]], list[tuple[int, int]]]]:
            A dictionary mapping each node to two lists:
              - index 0: list of (head, cost) tuples for outgoing edges.
              - index 1: list of (tail, cost) tuples for incoming edges.
    """
    adj_list = {}
    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            line = line.split()
            tail = int(line[0]) - 1
            head = int(line[1]) - 1
            cost = int(line[2])

            # out edges
            if tail not in adj_list:
                adj_list[tail] = [[], []]
            adj_list[tail][OUT_EDGES].append((head, cost))

            # in edges
            if head not in adj_list:
                adj_list[head] = [[], []]
            adj_list[head][IN_EDGES].append((tail, cost))

    return adj_list

def bellman_ford(graph: dict, s: int) -> list | None:
    n_nodes = len(graph)
    dp = [[math.inf for _ in range(n_nodes)] for _ in range(n_nodes+1)]
    dp[0][s] = 0

    for i in range(1, n_nodes+1):   # i :== number of hops
        stable = True
        for v in range(n_nodes):    # v :== index of head node
            case_1 = dp[i-1][v]
            case_2 = min([dp[i-1][w] + cost for w, cost in graph[v][IN_EDGES]]) # w :== index of tail node
            dp[i][v] = min(case_1, case_2)

            if dp[i][v] != dp[i-1][v]:
                stable = False

        if stable:
            return dp[i-1]

    return None

def floyd_warshall():
    pass

if __name__ == "__main__":
    # g = read_directed_weighted_edge_list("problem18.8test1.txt") # -2
    # g = read_directed_weighted_edge_list("problem18.8test2.txt") # Negative Cycle
    # g = read_directed_weighted_edge_list("g1.txt")  # Negative Cycle
    # g = read_directed_weighted_edge_list("g2.txt")  # Negative Cycle
    g = read_directed_weighted_edge_list("g3.txt")  # -19

    all_min_paths = []
    for v in range(len(g)):
        min_paths = bellman_ford(g, v)
        all_min_paths.append(min_paths)

        if min_paths is None:
            print("Negative Cycle")
            quit()

    min_min_path = min([path for sublist in all_min_paths for path in sublist])
    print(min_min_path)
