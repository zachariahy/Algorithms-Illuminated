import random
from math import inf

NODE_ONE = 0
NODE_TWO = 1
COST = 2

# returns adjacency list in the form of a dictionary, where the key is one node, and the value is a list of tuples,
# where each tuple consists of another node and a cost associated with the edge between the two nodes
def read_weighted_edge_list(file_path) -> dict:
    adj_list = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.split()

            if len(line) <= 2:
                continue

            node_one = int(line[NODE_ONE])
            node_two = int(line[NODE_TWO])
            cost = int(line[COST])

            if node_one not in adj_list:
                adj_list[node_one] = []
            adj_list[node_one].append((node_two, cost))

            if node_two not in adj_list:
                adj_list[node_two] = []
            adj_list[node_two].append((node_one, cost))

    return adj_list

def prim(graph: dict):
    s = random.choice(list(graph.keys()))
    processed_nodes = {s}
    tree = set()

    while True:
        minimum = (None, None, inf)
        for node_one in processed_nodes:
            for node_two in graph[node_one]:
                if node_two[0] not in processed_nodes:
                    if node_two[1] < minimum[COST]:
                        minimum = (node_one, node_two[0], node_two[1])

        if minimum[NODE_ONE] is None:
            return tree

        processed_nodes.add(minimum[NODE_TWO])
        tree.add(minimum)

if __name__ == "__main__":
    # dataset = read_weighted_edge_list("problem15.9test.txt")    # 14
    dataset = read_weighted_edge_list("problem15.9.txt")    # -3612829
    mst = prim(dataset)
    total_cost = sum(edge[COST] for edge in mst)
    print(total_cost)
