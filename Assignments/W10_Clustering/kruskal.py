from scipy.cluster.hierarchy import DisjointSet

NODE_ONE = 0
NODE_TWO = 1
COST = 2

# returns list of edges, with each edge represented as three tuple: (node_1, node_2, cost)
def read_weighted_edge_list(file_path) -> list:
    edge_list = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.split()
            if len(line) <= 2:
                continue
            node_one = int(line[NODE_ONE])
            node_two = int(line[NODE_TWO])
            cost = int(line[COST])
            edge_list.append((node_one, node_two, cost))
    return edge_list

def read_hamming_nodes(file_path) -> set:
    nodes = set()
    with open(file_path, 'r') as file:
        for line in file:
            line = line.split()
            if len(line) == 2:
                continue
            line = "".join(line)
            line = int(line, 2)
            nodes.add(line)
    return nodes

def kruskal(edges: list) -> set:
    mst = set()
    union_find = DisjointSet({node for edge in edges for node in (edge[NODE_ONE], edge[NODE_TWO])})
    edges.sort(key=lambda x: x[COST])
    for edge in edges:
        if not union_find.connected(edge[NODE_ONE], edge[NODE_TWO]):
            mst.add(edge)
            union_find.merge(edge[NODE_ONE], edge[NODE_TWO])
    return mst

def single_link_cluster(edges: list, k: int) -> DisjointSet:
    union_find = DisjointSet({node for edge in edges for node in (edge[NODE_ONE], edge[NODE_TWO])})
    edges.sort(key=lambda edge: edge[COST])
    for edge in edges:
        if not union_find.connected(edge[NODE_ONE], edge[NODE_TWO]):
            union_find.merge(edge[NODE_ONE], edge[NODE_TWO])
        if union_find.n_subsets == k:
            break
    return union_find

# return largest value of k such that there is a k-clustering with spacing at least 3
def hamming_cluster(nodes: set) -> int:
    union_find = DisjointSet(nodes)
    for node in nodes:
        for shift_one in range(24):
            distance_one_node = node ^ (1 << shift_one)
            if distance_one_node in nodes:
                union_find.merge(node, distance_one_node)
            for shift_two in range(24):
                if shift_two != shift_one:
                    distance_two_node = distance_one_node ^ (1 << shift_two)
                    if distance_two_node in nodes:
                        union_find.merge(node, distance_two_node)
    return union_find.n_subsets

if __name__ == "__main__":
    dataset = read_weighted_edge_list("clustering_small.txt")    # 106
    k_clusters = 4
    disjoint_set = single_link_cluster(dataset, k_clusters)
    max_spacing = min({edge[COST] for edge in dataset if not disjoint_set.connected(edge[NODE_ONE], edge[NODE_TWO])})
    print(max_spacing)

    # dataset = read_hamming_nodes("clustering_big.txt")    # 6118
    # n_clusters = hamming_cluster(dataset)
    # print(n_clusters)
