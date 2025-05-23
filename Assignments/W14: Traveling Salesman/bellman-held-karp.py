from math import inf, sqrt

X = 0
Y = 1

def tsp_brute():
    pass

def read_euclidean_format(file_path: str) -> list:
    l = []
    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            line = line.split()
            t = (float(line[X]), float(line[Y]))
            l.append(t)
    return l

def precompute_distances(graph: list) -> list:
    n_nodes = len(graph)
    l = [[0.0] * n_nodes for _ in range(n_nodes)]
    for a in range(n_nodes):
        for b in range(a + 1, n_nodes):
            ax, ay = graph[a]
            bx, by = graph[b]
            l[a][b] = l[b][a] = sqrt((ax - bx)**2 + (ay - by)**2)
    return l

def tsp_bellman_held_karp(graph: list):
    dist = precompute_distances(graph)

    n_nodes = len(graph)
    n_subsets = 1 << n_nodes
    dp = [[inf] * n_nodes for _ in range(n_subsets)]
    dp[1][0] = 0

    for subset in range(n_subsets):
        if not subset & 1:
            continue

        for last in range(n_nodes):
            if not (subset >> last) & 1:
                continue

            prev_subset = subset & ~(1 << last)

            for k in range(n_nodes):
                if k == last or not (subset >> k) & 1:
                    continue

                case_1 = dp[subset][last]
                case_2 = dp[prev_subset][k] + dist[k][last]
                dp[subset][last] = min(case_1, case_2)

    opt_tour_cost = min([dp[n_subsets - 1][j] + dist[j][0] for j in range(1, n_nodes)])
    return opt_tour_cost

if __name__ == "__main__":
    fs = ['tsp.txt']

    for f in fs:
        g = read_euclidean_format(f)
        otc = tsp_bellman_held_karp(g)
        print(otc)  # 26442.73030895475 -> 26442