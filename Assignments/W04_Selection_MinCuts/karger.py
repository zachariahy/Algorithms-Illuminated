from Roughgarden.utilities import read_edges_list
from random import choice, sample


def contract_edge():
    pass


def print_dict(d):
    for k, v in d.items():
        print(k, v)


def rand_contraction(al):
    # merge (contract) u, v into single node
    # remove self-loops
    # return cut represented by final 2 nodes (sets of nodes A, B)
    # pick remaining edge uniformly at random
    while len(al) > 2:
        u = choice(tuple(al))
        v = choice(al[u])

        al[u] = [node for node in al[u] if node != v]
        al[v] = [node for node in al[v] if node != u]
        al[u].extend(al[v])
        al.pop(v)

        for node in al:
            al[node] = [u if neighbor == v else neighbor for neighbor in al[node]]

        # for node in al:
        #     if node in al[node]:
        #         print(node, al[node])
        #         raise "ERROR -- self-loop"

    cut_count = len(al[next(iter(al))])
    return cut_count


if __name__ == "__main__":
    path = 'kargerMinCut.txt'
    adj_list = read_edges_list(path)

    cuts = []
    for _ in range(500):
        adj_list_copy = adj_list.copy()
        cut = rand_contraction(adj_list_copy)
        cuts.append(cut)

    min_cut = min(cuts)
    print(min_cut)

# 17
