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

def kruskal(graph: list):
    tree = set()
    union_find = DisjointSet({node for edge in graph for node in (edge[NODE_ONE], edge[NODE_TWO])})
    graph.sort(key=lambda x: x[COST])
    for edge in graph:
        if not union_find.connected(edge[NODE_ONE], edge[NODE_TWO]):
            tree.add(edge)
            union_find.merge(edge[NODE_ONE], edge[NODE_TWO])
    return tree

if __name__ == "__main__":
    dataset = read_weighted_edge_list('problem15.9-COPY.txt')    # -3612829
    # dataset = read_weighted_edge_list("clustering_small.txt")    #
    # dataset = read_weighted_edge_list("clustering_big.txt")    #
    mst = kruskal(dataset)
    total_cost = sum(edge[COST] for edge in mst)
    print(total_cost)
