from math import sqrt

X = 1
Y = 2

def read_euclidean_format(file_path: str) -> list:
    l = []
    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            line = line.split()
            t = (float(line[X]), float(line[Y]))
            l.append(t)
    return l

def precompute_squared_euclidean_distances(graph: list) -> list:
    n_nodes = len(graph)
    l = [[0.0] * n_nodes for _ in range(n_nodes)]
    for a in range(n_nodes):
        for b in range(a + 1, n_nodes):
            ax, ay = graph[a]
            bx, by = graph[b]
            l[a][b] = l[b][a] = (ax - bx)**2 + (ay - by)**2
    return l

def nearest_neighbor_tsp(graph: list):
    dist = precompute_squared_euclidean_distances(graph)

    not_visited = set(range(1, len(graph)))
    tour_dist = []
    last = 0
    for _ in range(len(graph) - 1):
        candidates = [(dist[last][neighbor], neighbor) for neighbor in not_visited]
        distance, node = min(candidates)
        tour_dist.append(distance)
        not_visited.remove(node)
        last = node

    tour_dist.append(dist[last][0])
    tour_length = sum(sqrt(distance) for distance in tour_dist)

    return tour_length

if __name__ == "__main__":
    fs = ['nn.txt']

    for f in fs:
        g = read_euclidean_format(f)
        heuristic_tour_cost = nearest_neighbor_tsp(g)
        print(heuristic_tour_cost)  # 1203406