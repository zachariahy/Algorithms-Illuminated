from collections import deque

def dfs_topo_iter(graph: dict, s: int, seen_nodes: set, magical_ordering: deque ):
    stack = deque([s])
    while stack:
        v = stack.pop()
        if v not in seen_nodes:
            seen_nodes.add(v)
            if v in graph:
                magical_ordering.appendleft(v)
                for w in graph[v]:
                    stack.append(w)

def topo_sort(graph: dict) -> deque:
    seen_nodes = set()
    magical_ordering = deque()
    for v in graph:
        if v not in seen_nodes:
            dfs_topo_iter(graph, v, seen_nodes, magical_ordering)
    return magical_ordering

def dfs_scc_iter(graph: dict, s: int, seen_nodes: set, num_scc: int, scc: dict):
    stack = deque([s])
    while stack:
        v = stack.pop()
        if v not in seen_nodes:
            seen_nodes.add(v)
            if v in graph:
                if num_scc in scc:
                    scc[num_scc].append(v)
                else:
                    scc[num_scc] = [v]
                for w in graph[v]:
                    stack.append(w)


def kosaraju(graph: dict, graph_rev: dict) -> dict:
    magical_ordering = topo_sort(graph_rev)
    seen_nodes = set()
    num_scc = 0
    scc = {}
    for v in magical_ordering:
        if v not in seen_nodes:
            num_scc += 1
            dfs_scc_iter(graph, v, seen_nodes, num_scc, scc)
    return scc

def read_edge_list(file_path) -> (dict, dict):
    adj_list = {}
    adj_list_rev = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.split()
            tail = int(line[0])
            head = int(line[1])
            if tail not in adj_list:
                adj_list[tail] = []
            adj_list[tail].append(head)
            if head not in adj_list_rev:
                adj_list_rev[head] = []
            adj_list_rev[head].append(tail)
    return adj_list, adj_list_rev

def main():
    path = 'problem8.10.txt'
    l, l_rev = read_edge_list(path)
    components = kosaraju(l, l_rev)
    sizes = []
    for c in components:
        size = len(components[c])
        sizes.append(size)
    sizes.sort(reverse=True)
    top_five = sizes[:5]     # [434821, 969, 459, 313, 211]
    print(top_five)

if __name__ == "__main__":
    main()
